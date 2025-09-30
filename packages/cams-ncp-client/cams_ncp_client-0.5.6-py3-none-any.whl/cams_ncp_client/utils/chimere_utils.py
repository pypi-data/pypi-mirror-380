from pathlib import Path
from typing import Dict, Optional

import numpy as np
import pandas as pd
import xarray as xr
from sklearn.neighbors import BallTree


def convert_to_ugm3(ds: xr.Dataset, var_name: str, ppb_to_ugm3_conversion_factors: Optional[Dict[str, float]] = None) -> xr.Dataset:
    """
    Convert the variable in the dataset to μg/m3 if it is in ppb vol.
    Args:
        ds (xr.Dataset): Input dataset
        var_name (str): Variable name to convert
        ppb_to_ugm3_conversion_factors (Optional[Dict[str, float]]): Optional dictionary with conversion factors from ppb to μg/m3.
            If None, the default conversion factors will be used.
    Returns:
        xr.Dataset: Dataset with converted variable
    """
    # ds_var = ds[var_name]
    units = ds[var_name].attrs['units']
    print(f'var_name: {var_name} units: {units}')
    if units == 'ppb vol':
        conversion_factors = ppb_to_ugm3_conversion_factors or _ppb_to_ugm3_conversion_factors()
        if var_name not in conversion_factors:
            raise ValueError(f"No conversion factor for variable {var_name}")
        factor = conversion_factors[var_name]
        ds[var_name] *= factor
        ds[var_name].attrs['units'] = 'μg/m3'
    return ds


def _ppb_to_ugm3_conversion_factors() -> Dict[str, float]:
    """
    Get default conversion factors from ppb to ug/m3 for common pollutants.

    Returns:
        Dict[str, float]: Dictionary with pollutant names as keys and conversion factors as values.
    1 ppb vol NO2 = 1.91 μg/m3 NO2
    1 ppb vol O3 = 2.0  μg/m3 O3
    1 ppb vol SO2 = 2.66 μg/m3 SO2
    """
    conversion_factors = {
        "NO2": 1.88,
        # 'NO2': 1.91,
        "O3": 2.0,
        "SO2": 2.66,
    }
    return conversion_factors


def find_nearest_gridpoints(grid_lats, grid_lons, station_lats, station_lons):
    """Find nearest grid points for all stations at once.."""
    grid_rad = np.deg2rad(np.column_stack([grid_lats.ravel(), grid_lons.ravel()]))
    stations_rad = np.deg2rad(np.column_stack([station_lats, station_lons]))

    # Build BallTree with haversine metric
    tree = BallTree(grid_rad, metric="haversine")

    # Query for nearest neighbors
    distances, flat_indices = tree.query(stations_rad, k=1, return_distance=True)

    # Convert flat indices to 2D indices
    y_indices, x_indices = np.unravel_index(flat_indices.ravel(), grid_lats.shape)
    return y_indices, x_indices


def get_station_concentrations(stations_df: pd.DataFrame, nc_file: Path, var_name: str, data_version: str,
                               nc_engine='h5netcdf', ppb_to_ugm3_conversion_factors: Optional[Dict[str, float]] = None) -> pd.DataFrame:
    """
    Similar to the get_station_concentrations in cams_utils.py, but adapted for chimere files (v2020 and v2023).

    Get concentrations (in the nc-file) for all stations in stations_df.
    The stations in stations_df must have columns 'name', 'lat', 'lon'.
    The nc_file must be Chimere NetCDF file if version 2020 or 2023 and must have a variable named var_name.
    The method parameter specifies how to select the nearest grid point for each station (default is "nearest").

    Args:
        stations_df (pd.DataFrame): DataFrame containing station information with columns 'name', '
        lat', 'lon'. (Cfr: StationClient.find_stations_df())
        nc_file (Path): Path to the netcdf file containing data. (Cfr: CamsFileClient.download_cams_file())
        var_name (str): Variable name in the netcdf file to extract concentrations.
        data_version (str): Version of the data ('v2020' or 'v2023').

    Returns:
        A DataFrame with timestamps as index and station names as columns, containing the concentrations for each station.
    """
    with xr.open_dataset(nc_file, engine=nc_engine, decode_timedelta=False) as ds:
        station_names = stations_df["name"].values
        station_lats = xr.DataArray(stations_df["lat"].values, dims=["station"])
        station_lons = xr.DataArray(stations_df["lon"].values, dims=["station"])

        if data_version == 'v2023':
            grid_lats = ds["nav_lat"].values
            grid_lons = ds["nav_lon"].values

            # find nearest grid points for all stations
            y_indices, x_indices = find_nearest_gridpoints(grid_lats, grid_lons, station_lats, station_lons)

            # Extract data using integer indexing
            station_data = ds.isel(y=xr.DataArray(y_indices, dims=["station"]), x=xr.DataArray(x_indices, dims=["station"]))
            station_data = convert_to_ugm3(station_data.isel(bottom_top=0), var_name, ppb_to_ugm3_conversion_factors)

            result_df = station_data[var_name].to_pandas()

            result_df.columns = station_names
            # convert to pandas timestamp in UTC
            result_df.index = pd.to_datetime(result_df.index, utc=True)
            result_df.index.name = "timestamp"
        elif data_version == 'v2020':
            grid_lats = ds["lat"].values
            grid_lons = ds["lon"].values

            # find nearest grid points for all stations
            y_indices, x_indices = find_nearest_gridpoints(grid_lats, grid_lons, station_lats, station_lons)

            # Extract data using integer indexing
            station_data = ds.isel(south_north=xr.DataArray(y_indices, dims=["station"]), west_east=xr.DataArray(x_indices, dims=["station"]))
            station_data = convert_to_ugm3(station_data.isel(bottom_top=0), var_name, ppb_to_ugm3_conversion_factors)

            result_df = station_data[var_name].to_pandas()

            base_date = ds["Times"].values[0]
            if isinstance(base_date, bytes):
                base_date_str = base_date.decode('utf-8')
            else:
                base_date_str = str(base_date)
            base_date_str = base_date_str.replace("_", "T")
            # convert to pandas timestamp in UTC
            base_time = pd.Timestamp(base_date_str, tz="UTC")
            result_df.columns = station_names
            result_df.index = pd.to_timedelta(result_df.index, unit="h") + base_time
            result_df.index.name = "timestamp"
        else:
            raise ValueError(f"Unknown data_version: {data_version}")
        return result_df