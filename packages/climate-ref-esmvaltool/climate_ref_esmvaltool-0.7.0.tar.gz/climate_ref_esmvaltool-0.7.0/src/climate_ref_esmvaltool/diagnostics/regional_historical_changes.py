import copy
from pathlib import Path

import numpy as np
import pandas
import xarray

from climate_ref_core.constraints import (
    AddSupplementaryDataset,
    PartialDateTime,
    RequireFacets,
    RequireTimerange,
)
from climate_ref_core.datasets import ExecutionDatasetCollection, FacetFilter, SourceDatasetType
from climate_ref_core.diagnostics import DataRequirement
from climate_ref_core.metric_values.typing import SeriesDefinition
from climate_ref_core.pycmec.metric import CMECMetric, MetricCV
from climate_ref_core.pycmec.output import CMECOutput
from climate_ref_esmvaltool.diagnostics.base import ESMValToolDiagnostic
from climate_ref_esmvaltool.recipe import dataframe_to_recipe
from climate_ref_esmvaltool.types import MetricBundleArgs, OutputBundleArgs, Recipe

REGIONS = (
    "Arabian-Peninsula",
    "Arabian-Sea",
    "Arctic-Ocean",
    "Bay-of-Bengal",
    "C.Australia",
    "C.North-America",
    "Caribbean",
    "Central-Africa",
    "E.Antarctica",
    "E.Asia",
    "E.Australia",
    "E.C.Asia",
    "E.Europe",
    "E.North-America",
    "E.Siberia",
    "E.Southern-Africa",
    "Equatorial.Atlantic-Ocean",
    "Equatorial.Indic-Ocean",
    "Equatorial.Pacific-Ocean",
    "Greenland/Iceland",
    "Madagascar",
    "Mediterranean",
    "N.Atlantic-Ocean",
    "N.Australia",
    "N.Central-America",
    "N.E.North-America",
    "N.E.South-America",
    "N.Eastern-Africa",
    "N.Europe",
    "N.Pacific-Ocean",
    "N.South-America",
    "N.W.North-America",
    "N.W.South-America",
    "New-Zealand",
    "Russian-Arctic",
    "Russian-Far-East",
    "S.Asia",
    "S.Atlantic-Ocean",
    "S.Australia",
    "S.Central-America",
    "S.E.Asia",
    "S.E.South-America",
    "S.Eastern-Africa",
    "S.Indic-Ocean",
    "S.Pacific-Ocean",
    "S.South-America",
    "S.W.South-America",
    "Sahara",
    "South-American-Monsoon",
    "Southern-Ocean",
    "Tibetan-Plateau",
    "W.Antarctica",
    "W.C.Asia",
    "W.North-America",
    "W.Siberia",
    "W.Southern-Africa",
    "West&Central-Europe",
    "Western-Africa",
)


def normalize_region(region: str) -> str:
    """Normalize region name so it can be used in filenames."""
    return region.replace("&", "-and-").replace("/", "-and-")


class RegionalHistoricalAnnualCycle(ESMValToolDiagnostic):
    """
    Plot regional historical annual cycle of climate variables.
    """

    name = "Regional historical annual cycle of climate variables"
    slug = "regional-historical-annual-cycle"
    base_recipe = "ref/recipe_ref_annual_cycle_region.yml"

    variables = (
        "hus",
        "pr",
        "psl",
        "tas",
        "ua",
    )

    data_requirements = (
        DataRequirement(
            source_type=SourceDatasetType.CMIP6,
            filters=(
                FacetFilter(
                    facets={
                        "variable_id": variables,
                        "experiment_id": "historical",
                        "table_id": "Amon",
                    },
                ),
            ),
            group_by=("source_id", "member_id", "grid_label"),
            constraints=(
                RequireTimerange(
                    group_by=("instance_id",),
                    start=PartialDateTime(1980, 1),
                    end=PartialDateTime(2009, 12),
                ),
                RequireFacets("variable_id", variables),
                AddSupplementaryDataset.from_defaults("areacella", SourceDatasetType.CMIP6),
            ),
        ),
        DataRequirement(
            source_type=SourceDatasetType.obs4MIPs,
            filters=(
                FacetFilter(
                    facets={
                        "variable_id": (
                            "psl",
                            "ua",
                        ),
                        "source_id": "ERA-5",
                        "frequency": "mon",
                    },
                ),
            ),
            group_by=("source_id",),
            constraints=(
                RequireTimerange(
                    group_by=("instance_id",),
                    start=PartialDateTime(1980, 1),
                    end=PartialDateTime(2009, 12),
                ),
                RequireFacets("variable_id", ("psl", "ua")),
            ),
            # TODO: Add obs4MIPs datasets once available and working:
            #
            # obs4MIPs dataset that cannot be ingested (https://github.com/Climate-REF/climate-ref/issues/260):
            # - GPCP-V2.3: pr
            #
            # Not yet available on obs4MIPs:
            # - ERA5: hus
            # - HadCRUT5_ground_5.0.1.0-analysis: tas
        ),
    )

    facets = ()
    series = tuple(
        SeriesDefinition(
            file_pattern=f"anncyc-{region}/allplots/*_{var_name}_*.nc",
            sel={"dim0": 0},  # Select the model and not the observation.
            dimensions={"region": region, "statistic": f"{var_name} regional mean"},
            values_name=var_name,
            index_name="month_number",
            attributes=[],
        )
        for var_name in variables
        for region in REGIONS
    )

    @staticmethod
    def update_recipe(
        recipe: Recipe,
        input_files: dict[SourceDatasetType, pandas.DataFrame],
    ) -> None:
        """Update the recipe."""
        # Update the dataset.
        recipe_variables = dataframe_to_recipe(input_files[SourceDatasetType.CMIP6])
        dataset = recipe_variables["hus"]["additional_datasets"][0]
        dataset.pop("timerange")
        dataset["benchmark_dataset"] = True
        dataset["plot_label"] = "{dataset}.{ensemble}.{grid}".format(**dataset)
        recipe["datasets"] = [dataset]

        # Generate diagnostics for each region.
        diagnostics = {}
        for region in REGIONS:
            for diagnostic_name, orig_diagnostic in recipe["diagnostics"].items():
                # Create the diagnostic for the region.
                diagnostic = copy.deepcopy(orig_diagnostic)
                normalized_region = normalize_region(region)
                diagnostics[f"{diagnostic_name}-{normalized_region}"] = diagnostic

                for variable in diagnostic["variables"].values():
                    # Remove unwanted facets that are part of the dataset.
                    for facet in ("project", "exp", "ensemble", "grid"):
                        variable.pop(facet, None)
                    # Update the preprocessor so it extracts the region.
                    preprocessor_name = variable["preprocessor"]
                    preprocessor = copy.deepcopy(recipe["preprocessors"][preprocessor_name])
                    preprocessor["extract_shape"]["ids"] = {"Name": [region]}
                    variable["preprocessor"] = f"{preprocessor_name}-{normalized_region}"
                    recipe["preprocessors"][variable["preprocessor"]] = preprocessor

                # Update plot titles with region name.
                for script in diagnostic["scripts"].values():
                    for plot in script["plots"].values():
                        plot["pyplot_kwargs"] = {"title": f"{{long_name}} {region}"}
        recipe["diagnostics"] = diagnostics


class RegionalHistoricalTimeSeries(RegionalHistoricalAnnualCycle):
    """
    Plot regional historical mean and anomaly of climate variables.
    """

    name = "Regional historical mean and anomaly of climate variables"
    slug = "regional-historical-timeseries"
    base_recipe = "ref/recipe_ref_timeseries_region.yml"

    variables = (
        "hus",
        "pr",
        "psl",
        "tas",
        "ua",
    )

    data_requirements = (
        DataRequirement(
            source_type=SourceDatasetType.CMIP6,
            filters=(
                FacetFilter(
                    facets={
                        "variable_id": variables,
                        "experiment_id": "historical",
                        "table_id": "Amon",
                    },
                ),
            ),
            group_by=("source_id", "member_id", "grid_label"),
            constraints=(
                RequireTimerange(
                    group_by=("instance_id",),
                    start=PartialDateTime(1980, 1),
                    end=PartialDateTime(2014, 12),
                ),
                RequireFacets("variable_id", variables),
                AddSupplementaryDataset.from_defaults("areacella", SourceDatasetType.CMIP6),
            ),
        ),
        DataRequirement(
            source_type=SourceDatasetType.obs4MIPs,
            filters=(
                FacetFilter(
                    facets={
                        "variable_id": (
                            "psl",
                            "ua",
                        ),
                        "source_id": "ERA-5",
                        "frequency": "mon",
                    },
                ),
            ),
            group_by=("source_id",),
            constraints=(
                RequireTimerange(
                    group_by=("instance_id",),
                    start=PartialDateTime(1980, 1),
                    end=PartialDateTime(2014, 12),
                ),
            ),
            # TODO: Add obs4MIPs datasets once available and working:
            #
            # obs4MIPs dataset that cannot be ingested (https://github.com/Climate-REF/climate-ref/issues/260):
            # - GPCP-V2.3: pr
            #
            # Not yet available on obs4MIPs:
            # - ERA5: hus
            # - HadCRUT5_ground_5.0.1.0-analysis: tas
        ),
    )

    series = tuple(
        SeriesDefinition(
            file_pattern=f"{diagnostic}-{region}/allplots/*_{var_name}_*.nc",
            sel={"dim0": 0},  # Select the model and not the observation.
            dimensions={
                "region": region,
                "statistic": (
                    f"{var_name} regional mean"
                    if diagnostic == "timeseries_abs"
                    else f"{var_name} regional mean anomaly"
                ),
            },
            values_name=var_name,
            index_name="time",
            attributes=[],
        )
        for var_name in variables
        for region in REGIONS
        for diagnostic in ["timeseries_abs", "timeseries"]
    )


class RegionalHistoricalTrend(ESMValToolDiagnostic):
    """
    Plot regional historical trend of climate variables.
    """

    name = "Regional historical trend of climate variables"
    slug = "regional-historical-trend"
    base_recipe = "ref/recipe_ref_trend_regions.yml"

    data_requirements = (
        DataRequirement(
            source_type=SourceDatasetType.CMIP6,
            filters=(
                FacetFilter(
                    facets={
                        "variable_id": (
                            "hus",
                            "pr",
                            "psl",
                            "tas",
                            "ua",
                        ),
                        "experiment_id": "historical",
                        "table_id": "Amon",
                    },
                ),
            ),
            group_by=("source_id", "member_id", "grid_label"),
            constraints=(
                RequireTimerange(
                    group_by=("instance_id",),
                    start=PartialDateTime(1980, 1),
                    end=PartialDateTime(2009, 12),
                ),
                AddSupplementaryDataset.from_defaults("areacella", SourceDatasetType.CMIP6),
            ),
        ),
        DataRequirement(
            source_type=SourceDatasetType.obs4MIPs,
            filters=(
                FacetFilter(
                    facets={
                        "variable_id": (
                            "psl",
                            "tas",
                            "ua",
                        ),
                        "source_id": "ERA-5",
                        "frequency": "mon",
                    },
                ),
            ),
            group_by=("source_id",),
            constraints=(
                RequireTimerange(
                    group_by=("instance_id",),
                    start=PartialDateTime(1980, 1),
                    end=PartialDateTime(2009, 12),
                ),
            ),
            # TODO: Add obs4MIPs datasets once available and working:
            #
            # obs4MIPs dataset that cannot be ingested (https://github.com/Climate-REF/climate-ref/issues/260):
            # - GPCP-V2.3: pr
            #
            # Not yet available on obs4MIPs:
            # - ERA5: hus
            # - HadCRUT5_ground_5.0.1.0-analysis: tas
        ),
    )
    facets = ("grid_label", "member_id", "source_id", "variable_id", "region", "metric")

    @staticmethod
    def update_recipe(
        recipe: Recipe,
        input_files: dict[SourceDatasetType, pandas.DataFrame],
    ) -> None:
        """Update the recipe."""
        recipe["datasets"] = []
        recipe_variables = dataframe_to_recipe(input_files[SourceDatasetType.CMIP6])
        diagnostics = {}
        for diagnostic_name, diagnostic in recipe["diagnostics"].items():
            for variable_name, variable in diagnostic["variables"].items():
                if variable_name not in recipe_variables:
                    continue
                dataset = recipe_variables[variable_name]["additional_datasets"][0]
                dataset.pop("timerange")
                variable["additional_datasets"].append(dataset)
                diagnostics[diagnostic_name] = diagnostic
        recipe["diagnostics"] = diagnostics

    @classmethod
    def format_result(
        cls,
        result_dir: Path,
        execution_dataset: ExecutionDatasetCollection,
        metric_args: MetricBundleArgs,
        output_args: OutputBundleArgs,
    ) -> tuple[CMECMetric, CMECOutput]:
        """Format the result."""
        metric_args[MetricCV.DIMENSIONS.value] = {
            "json_structure": ["variable_id", "region", "metric"],
            "variable_id": {},
            "region": {},
            "metric": {"trend": {}},
        }
        for file in result_dir.glob("work/*_trends/plot/seaborn_barplot.nc"):
            ds = xarray.open_dataset(file)
            source_id = execution_dataset[SourceDatasetType.CMIP6].source_id.iloc[0]
            select = source_id == np.array([s.strip() for s in ds.dataset.values.astype(str).tolist()])
            ds.isel(dim0=select)
            variable_id = next(iter(ds.data_vars.keys()))
            metric_args[MetricCV.DIMENSIONS.value]["variable_id"][variable_id] = {}
            metric_args[MetricCV.RESULTS.value][variable_id] = {}
            for region_value, trend_value in zip(ds.shape_id.astype(str).values, ds[variable_id].values):
                region = region_value.strip()
                trend = float(trend_value)
                if region not in metric_args[MetricCV.DIMENSIONS.value]["region"]:
                    metric_args[MetricCV.DIMENSIONS.value]["region"][region] = {}
                metric_args[MetricCV.RESULTS.value][variable_id][region] = {"trend": trend}

        return CMECMetric.model_validate(metric_args), CMECOutput.model_validate(output_args)
