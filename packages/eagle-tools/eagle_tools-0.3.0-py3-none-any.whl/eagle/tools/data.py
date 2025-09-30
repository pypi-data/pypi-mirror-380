import logging
from collections.abc import Sequence
import importlib.resources
import yaml

import numpy as np
import xarray as xr
import pandas as pd

from ufs2arco.utils import expand_anemoi_dataset, convert_anemoi_inference_dataset

logger = logging.getLogger("eagle.tools")


def get_xy():
    xds = xr.open_zarr("/pscratch/sd/t/timothys/nested-eagle/v0/data/hrrr.zarr")
    return {"x": xds["x"].isel(variable=0,drop=True).load(), "y": xds["y"].isel(variable=0,drop=True).load()}


def trim_xarray_edge(xds, trim_edge):
    assert all(key in xds for key in ("x", "y"))
    xds["x"].load()
    xds["y"].load()
    condx = ( (xds["x"] > trim_edge[0]-1) & (xds["x"] < xds["x"].max().values-trim_edge[1]+1) ).compute()
    condy = ( (xds["y"] > trim_edge[2]-1) & (xds["y"] < xds["y"].max().values-trim_edge[3]+1) ).compute()
    xds = xds.where(condx & condy, drop=True)
    return xds


def open_anemoi_dataset(
    path: str,
    levels: Sequence[float | int] = None,
    vars_of_interest: Sequence[str] = None,
    trim_edge: Sequence[int] = None,
    rename_to_longnames: bool = False,
    reshape_cell_to_2d: bool = False,
    member: int | None = None,
) -> xr.Dataset:

    ads = xr.open_zarr(path)
    xds = expand_anemoi_dataset(ads, "data", ads.attrs["variables"])
    for key in ["x", "y"]:
        if key in ads:
            xds[key] = ads[key] if "variable" not in ads[key].dims else ads[key].isel(variable=0, drop=True)
            xds = xds.set_coords(key)

    xds = xds.rename({"ensemble": "member"})
    xds = subsample(xds, levels, vars_of_interest, member=member)
    if trim_edge is not None:
        xds = trim_xarray_edge(xds, trim_edge)
    if rename_to_longnames:
        xds = rename(xds)

    if reshape_cell_to_2d:
        try:
            xds = reshape_cell_to_latlon(xds)
        except:
            logger.warning("open_anemoi_dataset: could not reshape_cell_to_2d, skipping...")
    return xds


def open_anemoi_inference_dataset(
    path: str,
    model_type: str,
    lam_index: int | None = None,
    levels: Sequence[float | int] = None,
    vars_of_interest: Sequence[str] = None,
    trim_edge: Sequence[int] = None,
    rename_to_longnames: bool = False,
    load: bool = False,
    reshape_cell_to_2d: bool = False,
    lcc_info: dict | None = None,
    member: int | None = None,
) -> xr.Dataset:
    assert model_type in ("nested-lam", "nested-global", "global")

    ids = xr.open_dataset(path, chunks="auto")
    xds = convert_anemoi_inference_dataset(ids)
    xds = subsample(xds, levels, vars_of_interest, member=member)
    if "ensemble" in xds.dims:
        raise NotImplementedError(f"note to future self from eagle.tools.data: open_anemoi_dataset renames ensemble-> member, need to do this here")

    if model_type == "nested-lam":
        assert lam_index is not None
        if "lam" in model_type:
            xds = xds.isel(cell=slice(lam_index))

    if load:
        xds = xds.load()

    if trim_edge is not None and "lam" in model_type:
        for key in ["x", "y"]:
            if key in ids:
                xds[key] = ids[key] if "variable" not in ids[key].dims else ids[key].isel(variable=0, drop=True)
                xds = xds.set_coords(key)
            else:
                xds[key] = get_xy()[key]
                xds = xds.set_coords(key)
        xds = trim_xarray_edge(xds, trim_edge)

    if rename_to_longnames:
        xds = rename(xds)

    if reshape_cell_to_2d and "global" in model_type:
        try:
            xds = reshape_cell_to_latlon(xds)
        except:
            logger.warning("open_anemoi_inference_dataset: could not reshape cell -> (latitude, longitude), skipping...")

    elif reshape_cell_to_2d and "lam" in model_type:
        try:
            xds = reshape_cell_to_xy(xds, **lcc_info)
        except:
            logger.warning("open_anemoi_inference_dataset: could not reshape cell -> (y, x), skipping...")

    return xds


def open_forecast_zarr_dataset(
    path: str,
    t0: pd.Timestamp,
    levels: Sequence[float | int] = None,
    vars_of_interest: Sequence[str] = None,
    trim_edge: Sequence[int] = None,
    rename_to_longnames: bool = False,
    load: bool = False,
    reshape_cell_to_2d: bool = False,
    member: int | None = None,
) -> xr.Dataset:
    """This is for non-anemoi forecast datasets, for example HRRR forecast data preprocessed by ufs2arco"""

    xds = xr.open_zarr(path, decode_timedelta=True)
    xds = xds.sel(t0=t0).squeeze(drop=True)
    xds["time"] = xr.DataArray(
        [pd.Timestamp(t0) + pd.Timedelta(hours=fhr) for fhr in xds.fhr.values],
        coords=xds.fhr.coords,
    )
    xds = xds.swap_dims({"fhr": "time"}).drop_vars("fhr")
    xds = subsample(xds, levels, vars_of_interest, member=member)

    # Comparing to anemoi, it's sometimes easier to flatten than unpack anemoi
    if not reshape_cell_to_2d:
        if {"x", "y"}.issubset(xds.dims):
            xds = xds.stack(cell2d=("y", "x"))
        elif {"longitude", "latitude"}.issubset(xds.dims):
            xds = xds.stack(cell2d=("latitude", "longitude"))
        else:
            raise KeyError("Unclear on the dimensions here")

        xds["cell"] = xr.DataArray(
            np.arange(len(xds.cell2d)),
            coords=xds.cell2d.coords,
        )
        xds = xds.swap_dims({"cell2d": "cell"})
        xds = xds.drop_vars("cell2d")
    xds = xds.drop_vars(["t0", "valid_time"])

    if load:
        xds = xds.load()

    if trim_edge is not None:
        xds = trim_xarray_edge(xds, trim_edge)

    if rename_to_longnames:
        xds = rename(xds)
    return xds


def subsample(xds, levels=None, vars_of_interest=None, member=None):
    """Subsample vertical levels, ensemble member(s), and variables
    """

    if levels is not None:
        xds = xds.sel(level=levels)

    if member is not None:
        xds = xds.sel(member=member)

    if vars_of_interest is not None:
        if any("wind_speed" in varname for varname in vars_of_interest):
            xds = calc_wind_speed(xds, vars_of_interest)
        xds = xds[vars_of_interest]
    else:
        xds = drop_forcing_vars(xds)

    return xds


def drop_forcing_vars(xds):
    for key in [
        "cos_julian_day",
        "sin_julian_day",
        "cos_local_time",
        "sin_local_time",
        "cos_latitude",
        "sin_latitude",
        "cos_longitude",
        "sin_longitude",
        "orog",
        "orography",
        "geopotential_at_surface",
        "land_sea_mask",
        "lsm",
        "insolation",
        "cos_solar_zenith_angle",
    ]:
        if key in xds:
            xds = xds.drop_vars(key)
    return xds


def _wind_speed(u, v, long_name):
    return xr.DataArray(
        np.sqrt(u**2 + v**2),
        coords=u.coords,
        attrs={
            "long_name": long_name,
            "units": "m/s",
        },
    )

def calc_wind_speed(xds, vars_of_interest):

    if "10m_wind_speed" in vars_of_interest:
        if "ugrd10m" in xds:
            u = xds["ugrd10m"]
            v = xds["vgrd10m"]
        elif "u10" in xds:
            u = xds["u10"]
            v = xds["v10"]
        elif "10m_u_component_of_wind" in xds:
            u = xds["10m_u_component_of_wind"]
            v = xds["10m_v_component_of_wind"]
        xds["10m_wind_speed"] = _wind_speed(u, v, "10m Wind Speed")

    if "80m_wind_speed" in vars_of_interest:
        if "ugrd80m" in xds:
            u = xds["ugrd80m"]
            v = xds["vgrd80m"]
        elif "u80" in xds:
            u = xds["u80"]
            v = xds["v80"]
        elif "80m_u_component_of_wind" in xds:
            u = xds["80m_u_component_of_wind"]
            v = xds["80m_v_component_of_wind"]
        xds["80m_wind_speed"] = _wind_speed(u, v, "80m Wind Speed")

    if "100m_wind_speed" in vars_of_interest:
        if "ugrd100m" in xds:
            u = xds["ugrd100m"]
            v = xds["vgrd100m"]
        elif "u100" in xds:
            u = xds["u100"]
            v = xds["v100"]
        elif "100m_u_component_of_wind" in xds:
            u = xds["100m_u_component_of_wind"]
            v = xds["100m_v_component_of_wind"]
        xds["100m_wind_speed"] = _wind_speed(u, v, "100m Wind Speed")

    if "wind_speed" in vars_of_interest:
        if "ugrd" in xds:
            u = xds["ugrd"]
            v = xds["vgrd"]
        elif "u" in xds:
            u = xds["u"]
            v = xds["v"]
        elif "u_component_of_wind" in xds:
            u = xds["u_component_of_wind"]
            v = xds["v_component_of_wind"]
        xds["wind_speed"] = _wind_speed(u, v, "Wind Speed")
    return xds

def rename(xds):
    rename_path = importlib.resources.files("eagle.tools.config") / "rename.yaml"
    with rename_path.open("r") as f:
        rdict = yaml.safe_load(f)

    for key, val in rdict.items():
        if key in xds:
            xds = xds.rename({key: val})
    return xds

def reshape_cell_to_latlon(xds):

    lon = np.unique(xds["longitude"])
    lat = np.unique(xds["latitude"])
    if xds["latitude"][0] > xds["latitude"][-1]:
        lat = lat[::-1]

    nds = xr.Dataset()
    nds["longitude"] = xr.DataArray(
        lon,
        coords={"longitude": lon},
    )
    nds["latitude"] = xr.DataArray(
        lat,
        coords={"latitude": lat},
    )
    for key in xds.dims:
        if key != "cell":
            nds[key] = xds[key].copy()

    for key in xds.data_vars:
        dims = tuple(d for d in xds[key].dims if d != "cell")
        dims += ("latitude", "longitude")
        shape = tuple(len(nds[d]) for d in dims)
        nds[key] = xr.DataArray(
            xds[key].data.reshape(shape),
            dims=dims,
            attrs=xds[key].attrs.copy(),
        )
    return nds

def reshape_cell_to_xy(xds, n_x, n_y, trim_edge=None):
    """Note: these indices will not match the original dataset, but they will be dropped anyway"""

    x = np.arange(n_x)
    y = np.arange(n_y)

    nds = xr.Dataset()
    nds["x"] = xr.DataArray(
        x,
        coords={"x": x},
    )
    nds["y"] = xr.DataArray(
        y,
        coords={"y": y},
    )
    for key in xds.dims:
        if key != "cell":
            nds[key] = xds[key].copy()

    coords = [x for x in list(xds.coords) if x not in xds.dims]
    for key in list(xds.data_vars) + coords:
        dims = tuple(d for d in xds[key].dims if d != "cell")
        dims += ("y", "x")
        shape = tuple(len(nds[d]) for d in dims)
        nds[key] = xr.DataArray(
            xds[key].data.reshape(shape),
            dims=dims,
            attrs=xds[key].attrs.copy(),
        )

    nds = nds.set_coords(coords)
    return nds
