import os
import rasterio
import datetime
import numpy as np
import xarray as xr
from tqdm import tqdm
from rasterio.features import geometry_mask
from rasterio.mask import mask as rasterio_mask

from ..core.spatial import clip_dem_to_roi, check_overlap, reproject_shp, handle_reprojection
from ..core.data_io import save_as_zarr, load_shapefile


def prepare_modis(data_dir, save_dir, dem_path, shp_path, oparams_file=None,
                  priority='MODIS', save_name='MODIS', save_dem=True, dem_name='DEM'):
    """Prepare MODIS data for processing by clipping to ROI and organizing into xarray Dataset."""
    
    roi = load_shapefile(shp_path)
    
    # Setup output directories
    os.chdir(data_dir)
    subdirs = os.listdir(data_dir)
    
    modis_save_dir = os.path.join(save_dir, save_name)
    if not os.path.exists(modis_save_dir):
        os.makedirs(modis_save_dir)
    if save_dem:
        dem_save_dir = os.path.join(save_dir, 'DEM')
        if not os.path.exists(dem_save_dir):
            os.makedirs(dem_save_dir)
    
    # Get DEM CRS for reprojection checks
    with rasterio.open(dem_path) as dem_src:
        dem_crs = dem_src.crs

    modis_data_list = []
    time_list = []
    lat = None
    lon = None
    first_valid = True

    for k in tqdm(range(len(subdirs)), desc="Processing directories"):
        currD = os.path.join(data_dir, subdirs[k])
        files = os.listdir(currD)
        os.chdir(currD)
        
        # Find Snow Cover file
        scfile = [f for f in files if 'Snow_Cover' in f and f.endswith('.tif')]
        if not scfile:
            tqdm.write(f'No Snow Cover data found in {currD}.')
            continue
        
        fname = scfile[0]
        DateSve = datetime.datetime.strptime(fname[9:16], '%Y%j').strftime('%Y-%m-%d')
        img_path = os.path.join(currD, scfile[0])
        
        with rasterio.open(img_path) as src:
            # Handle CRS mismatches
            if src.crs != dem_crs:
                if priority == 'MODIS' and k == 0:
                    # Reproject DEM to MODIS CRS
                    dem_file = os.path.basename(dem_path)
                    if save_dem:
                        reprojected_dem = os.path.join(dem_path, f"reprojected_{dem_file}")
                    else:
                        reprojected_dem = os.path.join(os.path.dirname(dem_path), f"reprojected_{dem_file}")
                    handle_reprojection(img_path, dem_path, reprojected_dem, priority=priority)
                    dem_path = reprojected_dem
                    with rasterio.open(dem_path) as new_dem:
                        dem_crs = new_dem.crs
                elif priority == 'DEM':
                    # Reproject MODIS to DEM CRS
                    reprojected_image = os.path.join(currD, f"reprojected_{scfile[0]}")
                    handle_reprojection(img_path, dem_path, reprojected_image, priority=priority)
                    img_path = reprojected_image
                    src = rasterio.open(img_path)
            
            # Reproject ROI on first valid image
            if first_valid:
                reprojected_roi = reproject_shp(roi, src.crs)
                first_valid = False
            
            if not check_overlap(src, reprojected_roi):
                tqdm.write(f"ROI does not overlap with raster in {currD}. Skipping...")
                continue

            try:
                SCA, out_transf = rasterio_mask(src, [reprojected_roi.geometry.iloc[0]],
                                                crop=True, all_touched=True, pad=True)
                SCA = SCA[0]
            except ValueError as e:
                tqdm.write(f"Masking failed in {currD}: {e}")
                continue
        
        # Create coordinate grid on first successful processing
        if lat is None or lon is None:
            ROI_mask = geometry_mask(reprojected_roi.geometry,
                                    transform=out_transf,
                                    invert=True,
                                    out_shape=SCA.shape)
            ROI_mask = np.where(ROI_mask == 0, np.nan, 1)
            
            bounds = rasterio.transform.array_bounds(SCA.shape[0], SCA.shape[1], out_transf)
            X, Y = np.meshgrid(np.linspace(bounds[0], bounds[2], SCA.shape[1]),
                               np.linspace(bounds[3], bounds[1], SCA.shape[0]))
            lat = Y[:, 0].tolist()
            lon = X[0, :].tolist()
        
        SCA_ROI = SCA * ROI_mask
        modis_data_list.append(SCA_ROI)
        time_list.append(DateSve)
    
    # Create final dataset
    if modis_data_list:
        modis_array = np.stack(modis_data_list, axis=0)
        
        ds = xr.Dataset(
            data_vars={
                'NDSI': (('time', 'lat', 'lon'), modis_array)
            },
            coords={
                'time': time_list,
                'lat': lat,
                'lon': lon
            }
        )
        
        save_as_zarr(ds, modis_save_dir, 'MODIS', oparams_file)
        
        if save_dem:
            clip_dem_to_roi(dem_path, roi, dem_save_dir, dem_name, oparams_file)
        
        return ds
    else:
        raise ValueError("No valid MODIS data found in the specified directory.")