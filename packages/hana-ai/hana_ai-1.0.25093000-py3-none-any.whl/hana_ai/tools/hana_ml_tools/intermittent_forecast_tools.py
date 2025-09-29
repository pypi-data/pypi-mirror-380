"""
This module contains the tools for intermittent demand forecasting.

The following class is available:

    * :class `IntermittentForecast`
"""

import json
import logging
from typing import List, Optional, Type, Union
from pydantic import BaseModel, Field

from langchain_core.tools import BaseTool

from hana_ml import ConnectionContext
from hana_ml.algorithms.pal.tsa.exponential_smoothing import CrostonTSB

from hana_ai.tools.hana_ml_tools.utility import _CustomEncoder, _create_temp_table

logger = logging.getLogger(__name__)

class IntermittentForecastInput(BaseModel):
    """
    The input schema for the IntermittentForecast tool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema name of the table, it is optional", default=None)
    alpha: Optional[float] = Field(description="Smoothing parameter for demand, it is optional", default=0.1)
    beta: Optional[float] = Field(description="Smoothing parameter for probability, it is optional", default=0.1)
    forecast_num: Optional[int] = Field(description="Number of values to be forecast, it is optional", default=1)
    method: Optional[str] = Field(description="Method to be used from sporadic or constant, it is optional", default="sporadic")
    accuracy_measure: Union[str, List] = Field(description="The metric to quantify how well a model fits input data. Options: 'mpe', 'mse', 'rmse', 'et', 'mad', 'mase', 'wmape', 'smape', 'mape'., it is optional", default=None)
    ignore_zero: Optional[bool] = Field(description="Ignore zero values or not in the dataset and only valid when ``accuracy_measure`` is 'mpe' or 'mape'., it is optional", default=False)
    remove_leading_zeros: Optional[bool] = Field(description="When it is set to True, the leading zeros are ignored for calculating measure, it is optional", default=False)


class IntermittentForecast(BaseTool):
    """
    This tool generates forecast for the intermittent demand dataset.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The name of the predicted result table and the statistics of the forecast.

        .. note::

            args_schema is used to define the schema of the inputs as follows:

            .. list-table::
                :widths: 15 50
                :header-rows: 1

                * - Field
                  - Description
                * - table_name
                  - the name of the table. If not provided, ask the user. Do not guess.
                * - key
                  - the key of the dataset. If not provided, ask the user. Do not guess.
                * - endog
                  - the endog of the dataset. If not provided, ask the user. Do not guess.
                * - alpha
                  - Smoothing parameter for demand, it is optional
                * - beta
                  - Smoothing parameter for probability, it is optional
                * - forecast_num
                  - Number of values to be forecast, it is optional
                * - method
                  - Method to be used from sporadic or constant, it is optional
                * - accuracy_measure
                  - The metric to quantify how well a model fits input data. Options: 'mpe', 'mse', 'rmse', 'et', 'mad', 'mase', 'wmape', 'smape', 'mape'., it is optional
                * - ignore_zero
                  - Ignore zero values or not in the dataset and only valid when ``accuracy_measure`` is 'mpe' or 'mape'., it is optional
                * - remove_leading_zeros
                  - When it is set to True, the leading zeros are ignored for calculating measure, it is optional

    """
    name: str = "intermittent_forecast"
    """Name of the tool."""
    description: str = "To generate forecast for the intermittent demand dataset. "
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = IntermittentForecastInput
    return_direct: bool = False

    def __init__(
        self,
        connection_context: ConnectionContext,
        return_direct: bool = False
    ) -> None:
        super().__init__(  # type: ignore[call-arg]
            connection_context=connection_context,
            return_direct=return_direct
        )

    def _run(
        self,
        **kwargs
    ) -> str:
        """Use the tool."""

        if "kwargs" in kwargs:
            kwargs = kwargs["kwargs"]
        table_name = kwargs.get("table_name", None)
        if table_name is None:
            return "Table name is required"
        key = kwargs.get("key", None)
        if key is None:
            return "Key is required"
        endog = kwargs.get("endog", None)
        if endog is None:
            return "Endog is required"
        schema_name = kwargs.get("schema_name", None)
        alpha = kwargs.get("alpha", 0.1)
        beta = kwargs.get("beta", 0.1)
        forecast_num = kwargs.get("forecast_num", 1)
        method = kwargs.get("method", "sporadic")
        accuracy_measure = kwargs.get("accuracy_measure", None)
        ignore_zero = kwargs.get("ignore_zero", False)
        remove_leading_zeros = kwargs.get("remove_leading_zeros", False)

        # Check if the table exists
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return json.dumps({
                "error": f"Table {table_name} does not exist in the database."
            }, cls=_CustomEncoder)
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return json.dumps({
                "error": f"Key {key} does not exist in the table {table_name}."
            }, cls=_CustomEncoder)
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return json.dumps({
                "error": f"Endog {endog} does not exist in the table {table_name}."
            }, cls=_CustomEncoder)
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        croston_tsb = CrostonTSB(
            alpha=alpha,
            beta=beta,
            forecast_num=forecast_num,
            method=method,
            accuracy_measure=accuracy_measure,
            ignore_zero=ignore_zero,
            remove_leading_zeros=remove_leading_zeros,
            expost_flag=False)

        result = croston_tsb.fit_predict(
            data=df,
            key=key,
            endog=endog
        )
        outputs = {
            "result_select_statement": _create_temp_table(self.connection_context, result.select_statement, self.name)
        }
        for _, row in croston_tsb.stats_.collect().iterrows():
            outputs[row[croston_tsb.stats_.columns[0]]] = row[croston_tsb.stats_.columns[1]]
        for _, row in croston_tsb.metrics_.collect().iterrows():
            outputs[row[croston_tsb.metrics_.columns[0]]] = row[croston_tsb.metrics_.columns[1]]
        return json.dumps(outputs, cls=_CustomEncoder)

    async def _run_async(
        self, **kwargs) -> str:
        """Use the tool asynchronously."""
        return self._run(
            **kwargs
        )
