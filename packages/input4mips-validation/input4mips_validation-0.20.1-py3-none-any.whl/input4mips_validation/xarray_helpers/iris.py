"""
Helpers for interchanging with iris
"""

from __future__ import annotations

from pathlib import Path
from typing import Any

import cftime
import iris
import ncdata.iris_xarray
import netCDF4
import xarray as xr
from iris.cube import CubeList

from input4mips_validation.xarray_helpers.variables import (
    XRVariableHelper,
    XRVariableProcessorLike,
)

iris.FUTURE.save_split_attrs = True


def ds_from_iris_cubes(  # noqa: PLR0913
    cubes: CubeList,
    xr_variable_processor: XRVariableProcessorLike = XRVariableHelper(),
    time_unit: str | None = None,
    time_calendar: str | None = None,
    raw_file: Path | str | None = None,
    time_dimension: str | None = None,
    xr_load_kwargs: dict[str, Any] | None = None,
) -> xr.Dataset:
    """
    Load an [xarray.Dataset][] from [iris.cube.CubeList][]

    This is a thin wrapper around [ncdata.iris_xarray.cubes_to_xarray][]
    that also handles setting bounds as co-ordinates and climatology variables.

    TODO: raise issue in https://github.com/pp-mo/ncdata to handle the edge cases,
    these fixes should be there rather than here.

    Parameters
    ----------
    cubes
        Cubes from which to create the dataset

    xr_variable_processor
        Helper to use for processing the variables in xarray objects.

    time_calendar
        Calendar to use for the time decoding.

        Only required if there is a climatology variable in `cubes`
        and `raw_file` and `time_dimension` are not provided.

    time_unit
        Unit to use for the time decoding.

        Only required if there is a climatology variable in `cubes`
        and `raw_file` and `time_dimension` are not provided.

    raw_file
        Raw file from which the data was loaded.

        Only required if there is a climatology variable in `cubes`
        and `time_calendar` and `time_unit` are not provided.

    time_dimension
        Time dimension of the data.

        Only required if there is a climatology variable in `cubes`
        and `time_calendar` and `time_unit` are not provided.

    xr_load_kwargs
        Passed to [`ncdata.iris_xarray.cubes_to_xarray`][].

        If not supplied, we use `dict(use_cftime=True)`.

    Returns
    -------
    :
        Loaded dataset

    Raises
    ------
    ValueError
        There is a climatology variable in `cubes`
        and the right combination of `time_unit`, `time_calendar`
        and `raw_file` is not provided.
    """
    if xr_load_kwargs is None:
        xr_load_kwargs = dict(use_cftime=True)

    ds = ncdata.iris_xarray.cubes_to_xarray(cubes, xr_load_kwargs=xr_load_kwargs)

    bnds_guess = xr_variable_processor.get_ds_bounds_variables(
        ds,
    )
    climatology_guess = xr_variable_processor.get_ds_climatology_bounds_variables(
        ds,
    )

    set_as_coords = (*bnds_guess, *climatology_guess)
    if set_as_coords:
        ds = ds.set_coords(set_as_coords)

    if climatology_guess:
        if (time_unit is None or time_calendar is None) and (
            raw_file is None or time_dimension is None
        ):
            msg = (
                f"Guessed that there are climatology variables ({climatology_guess=}) "
                "Hence we require `time_unit` and `time_calendar` or `raw_file`. "
                f"Received {time_unit=}, {time_calendar=}, "
                f"{raw_file=} and {time_dimension=}"
            )
            raise ValueError(msg)

        if time_unit is None or time_calendar is None:
            if raw_file is None:
                raise AssertionError

            if time_dimension is None:
                raise AssertionError

            # Use netCDF4 to ensure as fast reading as possible
            with netCDF4.Dataset(raw_file, "r") as ds_netcdf4:
                time_calendar = ds_netcdf4[time_dimension].getncattr("calendar")
                time_unit = ds_netcdf4[time_dimension].getncattr("units")

        if time_unit is None:
            raise AssertionError

        if time_calendar is None:
            raise AssertionError

        for climatology_v in climatology_guess:
            ds[climatology_v] = (
                ds[climatology_v].dims,
                cftime.num2date(
                    ds[climatology_v],
                    time_unit,
                    calendar=time_calendar,
                ),
            )

    return ds
