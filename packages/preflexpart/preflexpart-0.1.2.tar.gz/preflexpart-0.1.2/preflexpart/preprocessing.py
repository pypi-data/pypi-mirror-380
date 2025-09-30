"""Module for preprocessing for FLEXPART."""
import logging

import numpy as np
import xarray as xr

from preflexpart.input_fields import CONSTANT_FIELDS
from preflexpart.operators import omega_slope, time_rate

logger = logging.getLogger(__name__)

def preprocess(ds: dict[str, xr.DataArray]) -> dict[str, xr.DataArray]:
    """
    Preprocess the input dataset for FLEXPART.

    This function:
    - Deaccumulates precipitation and converts it to mm/h.
    - Deaccumulates radiation, heat flux, and accumulated surface stress.
    - Computes the omega slope for vertical velocity.
    - Adds constant fields to the output dataset.
    - Retains only the last lead_time step for relevant fields.

    Parameters
    ----------
    ds : xarray.Dataset
        The input dataset containing the requested parameters extracted from the GRIB file.

    Returns
    -------
    xarray.Dataset
        Processed dataset with derived variables.
    """

    ds_out = {}
    ## ---- Precipitation Processing ---- ##
    precipitation_vars = ["cp", "lsp"]
    for var in precipitation_vars:
        units = ds[var].attrs.get("units")
        if units != "m":
            logger.warn(f"Unexpected units for {var}: {units!r} (expected 'm')")

        # convert from m/hour to mm/hour
        with xr.set_options(keep_attrs=True):
            ds_out[var] = time_rate(ds[var], np.timedelta64(1, "h")) * 1000
            ds_out[var].attrs["units"] = "mm h-1"

    ## ---- Radiation, Heat Flux & Surface Stress ---- ##
    deaccumulated_vars = ["ssr", "sshf", "ewss", "nsss"]
    for var in deaccumulated_vars:
        ds_out[var] = time_rate(ds[var], np.timedelta64(1, "s"))

    ## ---- Compute Omega Slope ---- ##
    ds_out["omega"] = omega_slope(ds["sp"], ds["etadot"], ds["ak"], ds["bk"]).isel(
        level=slice(39, 137), step=slice(1, None)
    )

    ## ---- Add Constant Fields ---- ##
    for field in CONSTANT_FIELDS:
        ds_out[field] = ds[field]
    ## ---- Retain Only Last Lead Time Step ---- ##
    variables_to_keep = [
        "q", "u", "v", "t", "sp", "sd", "tcc",
        "2d", "10u", "10v", "2t"
    ]
    for var in variables_to_keep:
        ds_out[var] = ds[var].isel(step=slice(1, None))
    return ds_out
