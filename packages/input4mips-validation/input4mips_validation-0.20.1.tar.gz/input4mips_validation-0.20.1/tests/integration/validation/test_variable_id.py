"""
Integration tests of the variable ID validation
"""

from __future__ import annotations

import re

import pytest

from input4mips_validation.testing import (
    get_valid_out_path_and_disk_ready_ds,
)
from input4mips_validation.validation.datasets_to_write_to_disk import (
    get_ds_to_write_to_disk_validation_result,
)
from input4mips_validation.validation.error_catching import ValidationResultsStoreError


def test_invalid_variable_id_raises(test_cvs):
    """
    Test that an invalid value raises

    For a full list of edge case tests,
    see `tests/unit/validation/test_variable_id_validation.py`.
    """
    variable_name = "mole_fraction_of_carbon_dioxide_in_air"
    invalid_value = "mole_fraction_of_co2_in_air"

    out_path, valid_disk_ready_ds = get_valid_out_path_and_disk_ready_ds(
        cv_source=test_cvs,
        variable_name=variable_name,
    )

    valid_disk_ready_ds.attrs["variable_id"] = invalid_value

    res = get_ds_to_write_to_disk_validation_result(
        valid_disk_ready_ds,
        out_path=out_path,
        cvs=test_cvs,
    )

    error_msg = re.escape("ValueError: The `variable_id`")
    with pytest.raises(ValidationResultsStoreError, match=error_msg):
        res.raise_if_errors()


def test_no_variable_id_raises(test_cvs):
    out_path, valid_disk_ready_ds = get_valid_out_path_and_disk_ready_ds(
        cv_source=test_cvs
    )

    valid_disk_ready_ds.attrs.pop("variable_id")

    res = get_ds_to_write_to_disk_validation_result(
        valid_disk_ready_ds,
        out_path=out_path,
        cvs=test_cvs,
    )

    error_msg = re.escape("MissingAttributeError: 'variable_id'")
    with pytest.raises(ValidationResultsStoreError, match=error_msg):
        res.raise_if_errors()
