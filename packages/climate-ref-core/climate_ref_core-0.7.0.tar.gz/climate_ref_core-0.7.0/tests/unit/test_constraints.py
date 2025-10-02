import operator
from collections.abc import Callable
from datetime import datetime

import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from climate_ref_core.constraints import (
    AddSupplementaryDataset,
    GroupConstraint,
    PartialDateTime,
    RequireContiguousTimerange,
    RequireFacets,
    RequireOverlappingTimerange,
    RequireTimerange,
    apply_constraint,
)
from climate_ref_core.datasets import SourceDatasetType


class TestRequireFacets:
    constraint = RequireFacets(dimension="variable_id", required_facets=["tas", "pr"])

    @pytest.mark.parametrize(
        "data, expected",
        [
            (pd.DataFrame(columns=["variable_id", "path"]), False),
            (pd.DataFrame({"variable_id": ["tas", "pr"], "path": ["tas.nc", "pr.nc"]}), True),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "pr"],
                        "extra": ["a", "b"],
                        "path": ["tas.nc", "pr.nc"],
                    }
                ),
                True,
            ),
            (pd.DataFrame({"variable_id": ["tas"], "path": ["tas.nc"]}), False),
            (pd.DataFrame({"variable_id": ["tas"], "extra": ["a"], "path": ["tas.nc"]}), False),
        ],
    )
    def test_apply(self, data, expected):
        empty = data.loc[[]]
        expected_data = data if expected else empty
        assert_frame_equal(self.constraint.apply(data, empty), expected_data)

    def test_invalid_dimension(self):
        data = pd.DataFrame({"invalid": ["tas", "pr"], "path": ["tas.nc", "pr.nc"]})
        with pytest.raises(KeyError):
            self.constraint.apply(data, data)

    @pytest.mark.parametrize(
        "data, expected_rows",
        [
            (
                pd.DataFrame(
                    {
                        "variable_id": [],
                        "source_id": [],
                        "path": [],
                    }
                ),
                [],
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tos", "areacello", "tos"],
                        "source_id": ["A", "B", "B"],
                        "path": ["tos_A.nc", "areacello_B.nc", "tas_B.nc"],
                    }
                ),
                [1, 2],
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tos", "areacello", "tos", "areacello"],
                        "source_id": ["A", "A", "B", "B"],
                        "path": ["tos_A.nc", "areacello_A.nc", "tos_B.nc", "areacello_B.nc"],
                    }
                ),
                [0, 1, 2, 3],
            ),
        ],
    )
    def test_apply_group_by(self, data, expected_rows):
        constraint = RequireFacets(
            dimension="variable_id",
            required_facets=("tos", "areacello"),
            group_by="source_id",
        )
        result = constraint.apply(group=data, data_catalog=data)
        expected = data.loc[expected_rows]
        assert_frame_equal(result, expected)


class TestAddSupplementaryDataset:
    constraint = AddSupplementaryDataset.from_defaults("areacella", SourceDatasetType.CMIP6)

    @pytest.mark.parametrize(
        "data_catalog, expected_rows",
        [
            (
                # Test that missing supplementary files are handled gracefully.
                pd.DataFrame(
                    {
                        "variable_id": ["tas"],
                        "source_id": ["ACCESS-ESM1-5"],
                        "grid_label": ["gn"],
                        "table_id": ["Amon"],
                        "experiment_id": ["historical"],
                        "member_id": ["r1i1p1f1"],
                        "version": ["v20210316"],
                    }
                ),
                [0],
            ),
            (
                # Test that missing supplementary files are handled gracefully.
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "areacella", "areacella", "tas"],
                        "source_id": ["X", "X", "X", "Y"],
                        "grid_label": ["gn"] * 4,
                        "table_id": ["Amon", "fx", "fx", "Amon"],
                        "experiment_id": ["historical"] * 4,
                        "member_id": ["r1i1p1f1", "r1i1p1f1", "r2i1p1f1", "r2i1p1f1"],
                        "version": ["v20210316", "v20210316", "v20210317", "v20210317"],
                    }
                ),
                [0, 3, 1],
            ),
            (
                # Test that the grid_label matches.
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "areacella", "areacella"],
                        "source_id": ["ACCESS-ESM1-5"] * 3,
                        "grid_label": ["gn", "gn", "gr"],
                        "table_id": ["Amon", "fx", "fx"],
                        "experiment_id": ["historical", "piControl", "historical"],
                        "member_id": ["r1i1p1f1", "r2i1p1f1", "r1i1p1f1"],
                        "version": ["v20210316"] * 3,
                    }
                ),
                [0, 1],
            ),
            (
                # Test that the source_id matches.
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "areacella", "areacella"],
                        "source_id": ["ACCESS-ESM1-5", "X", "ACCESS-ESM1-5"],
                        "grid_label": ["gn"] * 3,
                        "table_id": ["Amon", "fx", "fx"],
                        "experiment_id": ["historical"] * 3,
                        "member_id": ["r1i1p1f1", "r1i1p1f1", "r2i1p1f1"],
                        "version": ["v20210316"] * 3,
                    }
                ),
                [0, 2],
            ),
            (
                # Test that the latest version is selected.
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "areacella", "areacella"],
                        "source_id": ["ACCESS-ESM1-5"] * 3,
                        "grid_label": ["gn"] * 3,
                        "table_id": ["Amon", "fx", "fx"],
                        "experiment_id": ["historical"] * 3,
                        "member_id": ["r1i1p1f1"] * 3,
                        "version": ["v20210316", "v202200101", "v20230101"],
                    }
                ),
                [0, 2],
            ),
            (
                # Test that the best match for each "tas" dataset is selected.
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "areacella", "tas", "areacella"],
                        "source_id": ["ACCESS-ESM1-5"] * 4,
                        "grid_label": ["gn"] * 4,
                        "table_id": ["Amon", "fx", "Amon", "fx"],
                        "experiment_id": ["historical", "historical", "ssp585", "ssp585"],
                        "member_id": ["r1i1p1f1", "r1i1p1f1", "r2i1p1f1", "r1i1p1f1"],
                        "version": ["v20210316", "v20220101", "v20210316", "v20210316"],
                    }
                ),
                [0, 2, 1, 3],
            ),
        ],
    )
    def test_apply(self, data_catalog, expected_rows):
        group = data_catalog[data_catalog["variable_id"] == "tas"]
        result = self.constraint.apply(group=group, data_catalog=data_catalog)
        expected = data_catalog.loc[expected_rows]
        assert (result == expected).all().all()


class TestPartialDateTime:
    @pytest.mark.parametrize(
        "pdt, dt, expected",
        [
            (PartialDateTime(year=2000), datetime(2000, 1, 1), True),
            (PartialDateTime(year=2000), datetime(1999, 12, 31), False),
            (PartialDateTime(year=2000, month=6), datetime(2000, 6, 15), True),
            (PartialDateTime(year=2000, month=6), datetime(2000, 5, 31), False),
            (PartialDateTime(year=2000, month=6, day=15), datetime(2000, 6, 15), True),
            (PartialDateTime(year=2000, month=6, day=15), datetime(2000, 6, 14), False),
            (PartialDateTime(year=2000, month=6, day=15, hour=12), datetime(2000, 6, 15, 12), True),
            (PartialDateTime(year=2000, month=6, day=15, hour=12), datetime(2000, 6, 15, 11), False),
        ],
    )
    def test_eq(self, pdt: PartialDateTime, dt: datetime, expected: bool) -> None:
        assert (pdt == dt) == expected

    @pytest.mark.parametrize(
        "pdt, dt, expected",
        [
            (PartialDateTime(year=2000), datetime(1999, 1, 1), False),
            (PartialDateTime(year=2000), datetime(2000, 12, 1), False),
            (PartialDateTime(year=2000), datetime(2001, 12, 31), True),
            (PartialDateTime(year=2000, month=6), datetime(2000, 6, 15), False),
            (PartialDateTime(year=2000, month=6), datetime(1999, 7, 15), False),
            (PartialDateTime(year=2000, month=6), datetime(2000, 7, 31), True),
            (PartialDateTime(year=2000, month=6, day=15), datetime(2000, 6, 14), False),
            (PartialDateTime(year=2000, month=6, day=15), datetime(2000, 6, 16), True),
            (PartialDateTime(year=2000, month=6, day=15, hour=12), datetime(2000, 6, 15, 12), False),
            (PartialDateTime(year=2000, month=6, day=15, hour=12), datetime(2000, 6, 15, 13), True),
        ],
    )
    def test_lt(self, pdt: PartialDateTime, dt: datetime, expected: bool) -> None:
        assert (pdt < dt) == expected

    def test_gt(self):
        assert (PartialDateTime(year=2000, month=2) > datetime(2000, 1, 1)) == True  # noqa: E712

    @pytest.mark.parametrize("op", [operator.eq, operator.lt, operator.gt])
    def test_not_implemented(self, op: Callable) -> None:
        with pytest.raises(TypeError):
            assert op(PartialDateTime(year=2000), object())


class TestRequireTimerange:
    @pytest.mark.parametrize(
        "data, start, end, expected",
        [
            (
                pd.DataFrame(
                    {
                        "variable_id": [],
                        "start_time": [],
                        "end_time": [],
                        "path": [],
                    }
                ),
                PartialDateTime(year=2000),
                PartialDateTime(year=2001),
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                        ],
                    }
                ),
                PartialDateTime(year=2000, month=1),
                PartialDateTime(year=2000, month=12),
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                        ],
                    }
                ),
                PartialDateTime(year=2000, month=1),
                None,
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                        ],
                    }
                ),
                None,
                PartialDateTime(year=2000, month=5),
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas"],
                        "start_time": [
                            datetime(2000, 2, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                        ],
                    }
                ),
                PartialDateTime(year=2000, month=1),
                None,
                False,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                        ],
                    }
                ),
                None,
                PartialDateTime(year=2001, month=1),
                False,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas", "tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                            datetime(2003, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                            datetime(2003, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200112.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200112.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200301-200312.nc",
                        ],
                    }
                ),
                PartialDateTime(year=2000, month=1),
                PartialDateTime(year=2003, month=12),
                False,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas", "areacella"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                            None,
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                            None,
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200112.nc",
                            "areacella_fx_ACCESS-ESM1-5_historical_r1i1p1f1_gn.nc",
                        ],
                    }
                ),
                PartialDateTime(year=2000, month=1),
                PartialDateTime(year=2001, month=12),
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["pr", "tas", "tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2001, 12, 16, 12),
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                        ],
                        "path": [
                            "pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200112.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200112.nc",
                        ],
                    }
                ),
                PartialDateTime(year=2000, month=1),
                PartialDateTime(year=2001, month=12),
                True,
            ),
        ],
    )
    def test_apply(
        self,
        data: pd.DataFrame,
        start: PartialDateTime,
        end: PartialDateTime,
        expected: bool,
    ) -> None:
        constraint = RequireTimerange(group_by=["variable_id"], start=start, end=end)
        empty = data.loc[[]]
        expected_data = data if expected else empty
        assert_frame_equal(constraint.apply(data, empty), expected_data)

    def test_apply_partial(self) -> None:
        data = pd.DataFrame(
            {
                "variable_id": ["pr", "tas"],
                "start_time": [
                    datetime(2000, 1, 16, 12),
                    datetime(2000, 1, 16, 12),
                ],
                "end_time": [
                    datetime(2000, 12, 16, 12),
                    datetime(2002, 12, 16, 12),
                ],
                "path": [
                    "pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                    "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200212.nc",
                ],
            }
        )
        start = PartialDateTime(year=2000, month=1)
        end = PartialDateTime(year=2001, month=12)
        expected_rows = [1]
        expected_data = data.loc[expected_rows]

        constraint = RequireTimerange(group_by=["variable_id"], start=start, end=end)
        assert_frame_equal(constraint.apply(data, data), expected_data)


class TestContiguousTimerange:
    constraint = RequireContiguousTimerange(group_by=["variable_id"])

    @pytest.mark.parametrize(
        "data, expected_rows",
        [
            (
                pd.DataFrame(
                    {
                        "variable_id": [],
                        "start_time": [],
                        "end_time": [],
                        "path": [],
                    }
                ),
                [],
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200112.nc",
                        ],
                    }
                ),
                [0, 1],
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas", "tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                            datetime(2003, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                            datetime(2003, 12, 16, 12),
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200112.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200112.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200301-200312.nc",
                        ],
                    }
                ),
                [],
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas", "areacella"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                            None,
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                            None,
                        ],
                        "path": [
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200101-200112.nc",
                            "areacella_fx_ACCESS-ESM1-5_historical_r1i1p1f1_gn.nc",
                        ],
                    }
                ),
                [0, 1, 2],
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["pr", "tas", "tas"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2000, 1, 16, 12),
                            datetime(2002, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2000, 12, 16, 12),
                            datetime(2002, 12, 16, 12),
                        ],
                        "path": [
                            "pr_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200001-200012.nc",
                            "tas_Amon_ACCESS-ESM1-5_historical_r1i1p1f1_gn_200201-200212.nc",
                        ],
                    }
                ),
                [0],
            ),
        ],
    )
    def test_apply(self, data: pd.DataFrame, expected_rows: list[int]) -> None:
        expected_data = data.loc[expected_rows]
        assert_frame_equal(self.constraint.apply(data, data.loc[[]]), expected_data)


class TestOverlappingTimerange:
    constraint = RequireOverlappingTimerange(group_by=["variable_id"])

    @pytest.mark.parametrize(
        "data, expected",
        [
            (
                pd.DataFrame(
                    {
                        "variable_id": [],
                        "start_time": [],
                        "end_time": [],
                        "path": [],
                    }
                ),
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas", "pr"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2001, 12, 16, 12),
                            datetime(2002, 12, 16, 12),
                            datetime(2014, 12, 16, 12),
                        ],
                        "path": [
                            "tas_2000-2001.nc",
                            "tas_2001-2002.nc",
                            "pr_2001-2014.nc",
                        ],
                    }
                ),
                True,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "pr"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2002, 1, 16, 12),
                        ],
                        "end_time": [
                            datetime(2001, 12, 16, 12),
                            datetime(2002, 12, 16, 12),
                        ],
                        "path": [
                            "tas_2000-2001.nc",
                            "pr_2002-2002.nc",
                        ],
                    }
                ),
                False,
            ),
            (
                pd.DataFrame(
                    {
                        "variable_id": ["tas", "tas", "areacella"],
                        "start_time": [
                            datetime(2000, 1, 16, 12),
                            datetime(2001, 1, 16, 12),
                            None,
                        ],
                        "end_time": [
                            datetime(2000, 12, 16, 12),
                            datetime(2001, 12, 16, 12),
                            None,
                        ],
                        "path": [
                            "tas_2000-2000.nc",
                            "tas_2001-2001.nc",
                            "areacella.nc",
                        ],
                    }
                ),
                True,
            ),
        ],
    )
    def test_apply(self, data, expected):
        empty = data.loc[[]]
        expected_data = data if expected else empty
        assert_frame_equal(self.constraint.apply(data, empty), expected_data)


@pytest.fixture
def data_catalog():
    return pd.DataFrame(
        {
            "variable": ["tas", "pr", "rsut", "tas", "tas"],
            "source_id": ["CESM2", "CESM2", "CESM2", "ACCESS", "CAS"],
            "path": ["tas_CESM2.nc", "pr_CESM2.nc", "rsut_CESM2.nc", "tas_ACCESS.nc", "tas_CAS.nc"],
        }
    )


def test_apply_constraint_operation(data_catalog):
    #  operation that appends the "rsut" variable to the group
    class ExampleOperation(GroupConstraint):
        def apply(self, group: pd.DataFrame, data_catalog: pd.DataFrame) -> pd.DataFrame:
            return pd.concat([group, data_catalog[data_catalog["variable"] == "rsut"]])

    result = apply_constraint(
        data_catalog[data_catalog["variable"] == "tas"],
        ExampleOperation(),
        data_catalog,
    )

    assert_frame_equal(
        result,
        pd.DataFrame(
            {
                "variable": ["tas", "tas", "tas", "rsut"],
                "source_id": ["CESM2", "ACCESS", "CAS", "CESM2"],
                "path": ["tas_CESM2.nc", "tas_ACCESS.nc", "tas_CAS.nc", "rsut_CESM2.nc"],
            },
            index=[0, 3, 4, 2],
        ),
    )


def test_apply_constraint_operation_mutable(data_catalog):
    class MutableOperation(GroupConstraint):
        def apply(self, group: pd.DataFrame, data_catalog: pd.DataFrame) -> pd.DataFrame:
            group["variable"] = "new"
            return group

    orig_data_catalog = data_catalog.copy()
    result = apply_constraint(
        data_catalog,
        MutableOperation(),
        None,
    )

    assert (result["variable"] == "new").all()

    # Mutating the group impacts the original data catalog
    with pytest.raises(AssertionError):
        assert_frame_equal(data_catalog, orig_data_catalog)


def test_apply_constraint_empty():
    assert (
        apply_constraint(
            pd.DataFrame({"variable_id": [], "path": []}),
            RequireFacets(dimension="variable_id", required_facets=["tas", "pr"]),
            pd.DataFrame({"variable_id": [], "path": []}),
        )
        is None
    )


def test_apply_constraint_validate(data_catalog):
    result = apply_constraint(
        data_catalog,
        RequireFacets(dimension="variable", required_facets=["tas", "pr"]),
        pd.DataFrame(),
    )
    assert_frame_equal(result, data_catalog)


def test_apply_constraint_validate_invalid(data_catalog):
    assert (
        apply_constraint(
            data_catalog,
            RequireFacets(dimension="variable", required_facets=["missing", "pr"]),
            pd.DataFrame(),
        )
        is None
    )
