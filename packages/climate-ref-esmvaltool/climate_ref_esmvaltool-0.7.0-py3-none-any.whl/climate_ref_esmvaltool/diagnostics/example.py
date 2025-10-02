import pandas

from climate_ref_core.constraints import AddSupplementaryDataset, RequireContiguousTimerange
from climate_ref_core.datasets import FacetFilter, SourceDatasetType
from climate_ref_core.diagnostics import DataRequirement
from climate_ref_core.metric_values.typing import SeriesDefinition
from climate_ref_esmvaltool.diagnostics.base import ESMValToolDiagnostic
from climate_ref_esmvaltool.recipe import dataframe_to_recipe
from climate_ref_esmvaltool.types import Recipe


class GlobalMeanTimeseries(ESMValToolDiagnostic):
    """
    Calculate the annual mean global mean timeseries for a dataset.
    """

    name = "Global Mean Timeseries"
    slug = "global-mean-timeseries"
    base_recipe = "examples/recipe_python.yml"

    data_requirements = (
        DataRequirement(
            source_type=SourceDatasetType.CMIP6,
            filters=(FacetFilter(facets={"variable_id": ("tas",)}),),
            group_by=("source_id", "experiment_id", "member_id", "table_id", "variable_id", "grid_label"),
            constraints=(
                RequireContiguousTimerange(group_by=("instance_id",)),
                AddSupplementaryDataset.from_defaults("areacella", SourceDatasetType.CMIP6),
            ),
        ),
    )

    facets = ()
    series = (
        SeriesDefinition(
            file_pattern="timeseries/script1/*.nc",
            dimensions={"statistic": "tas annual global mean"},
            values_name="tas",
            index_name="time",
            attributes=[],
        ),
    )

    @staticmethod
    def update_recipe(
        recipe: Recipe,
        input_files: dict[SourceDatasetType, pandas.DataFrame],
    ) -> None:
        """Update the recipe."""
        # Clear unwanted elements from the recipe.
        recipe["datasets"].clear()
        recipe["diagnostics"].pop("map")
        variables = recipe["diagnostics"]["timeseries"]["variables"]
        variables.clear()

        # Prepare updated variables section in recipe.
        recipe_variables = dataframe_to_recipe(input_files[SourceDatasetType.CMIP6])
        recipe_variables = {k: v for k, v in recipe_variables.items() if k != "areacella"}
        for variable in recipe_variables.values():
            variable["preprocessor"] = "annual_mean_global"
            variable["caption"] = "Annual global mean {long_name} according to {dataset}."

        # Populate recipe with new variables/datasets.
        variables.update(recipe_variables)
