"""
This module is used to generate a report for the time series dataset.

The following classes are available:

    * :class `TimeSeriesDatasetReport`
    * :class `ForecastLinePlot`
"""

import json
import logging
import os
from pathlib import Path
import tempfile
from typing import Optional, Type
from pydantic import BaseModel, Field

from langchain_core.tools import BaseTool

from hana_ml import ConnectionContext
from hana_ml.visualizers.visualizer_base import forecast_line_plot
from hana_ml.visualizers.unified_report import UnifiedReport

logger = logging.getLogger(__name__)

class TSDatasetInput(BaseModel):
    """
    The input schema for the TSDatasetTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)
    output_dir: Optional[str] = Field(description="the output directory to save the report, it is optional", default=None)

class ForecastLinePlotInput(BaseModel):
    """
    The input schema for the ForecastLinePlot tool.
    """
    predict_result: str = Field(description="the name of the predicted result table. If not provided, ask the user. Do not guess.")
    actual_table: Optional[str] = Field(description="the name of the actual data table, it is optional", default=None)
    predict_schema: Optional[str] = Field(description="the schema of the predicted result table, it is optional", default=None)
    actual_schema: Optional[str] = Field(description="the schema of the actual data table, it is optional", default=None)
    confidence: Optional[tuple] = Field(description="the column names of confidence bounds, it is optional", default=None)
    output_dir: Optional[str] = Field(description="the output directory to save the line plot, it is optional", default=None)

class TimeSeriesDatasetReport(BaseTool):
    """
    This tool generates a report for a time series dataset.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The path of the generated report.

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
                  - the endog of the dataset. If not provided, ask the user. Do not guess
    """
    name: str = "ts_dataset_report"
    """Name of the tool."""
    description: str = "To generate timeseries report for a given HANA table. "
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = TSDatasetInput
    return_direct: bool = False
    bas: bool = False

    def __init__(
        self,
        connection_context: ConnectionContext,
        return_direct: bool = False
    ) -> None:
        super().__init__(  # type: ignore[call-arg]
            connection_context=connection_context,
            return_direct=return_direct
        )

    def set_bas(self, bas: bool) -> None:
        """
        Set the bas flag to True or False.
        """
        self.bas = bas

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
        output_dir = kwargs.get("output_dir", None)
        # check hana has the table
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return json.dumps({"error": f"Table {table_name} does not exist."})
        # check key in the table
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return json.dumps({"error": f"Key {key} does not exist in table {table_name}."})
        # check endog in the table
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return json.dumps({"error": f"Endog {endog} does not exist in table {table_name}."})
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        ur = UnifiedReport(df).build(key=key, endog=endog)
        if output_dir is None:
            destination_dir = os.path.join(tempfile.gettempdir(), "hanaml_report")
        else:
            destination_dir = output_dir
        if not os.path.exists(destination_dir):
            try:
                os.makedirs(destination_dir, exist_ok=True)
            except Exception as e:
                logger.error("Error creating directory %s: %s", destination_dir, e)
                raise

        output_file = os.path.join(
                    destination_dir,
                    f"{table_name}_ts_report")
        ur.display(save_html=output_file)
        if not self.bas:
            ur.display() #directly display in jupyter
        return json.dumps({"html_file": str(Path(output_file + ".html").as_posix())}, ensure_ascii=False)

    async def _arun(
        self, **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)

class ForecastLinePlot(BaseTool):
    """
    This tool generates a line plot for the forecasted result.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The path of the generated line plot.

        .. note::

            args_schema is used to define the schema of the inputs as follows:

            .. list-table::
                :widths: 15 50
                :header-rows: 1

                * - Field
                  - Description
                * - predict_result
                  - the name of the predicted result table. If not provided, ask the user. Do not guess.
                * - actual_table
                  - the name of the actual data table, it is optional
                * - confidence
                  - the column names of confidence bounds, it is optional
    """
    name: str = "forecast_line_plot"
    """Name of the tool."""
    description: str = "To generate line plot for the forecasted result. "
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = ForecastLinePlotInput
    """Input schema of the tool."""
    return_direct: bool = False
    bas: bool = False

    def __init__(
        self,
        connection_context: ConnectionContext,
        return_direct: bool = False
    ) -> None:
        super().__init__(  # type: ignore[call-arg]
            connection_context=connection_context,
            return_direct=return_direct
        )

    def set_bas(self, bas: bool) -> None:
        """
        Set the bas flag to True or False.
        """
        self.bas = bas

    def _run(
        self,
        **kwargs
    ) -> str:
        """Use the tool."""

        if "kwargs" in kwargs:
            kwargs = kwargs["kwargs"]
        predict_result = kwargs.get("predict_result", None)
        predict_schema = kwargs.get("predict_schema", None)
        if predict_result is None:
            return "Prediction result table is required"
        actual_table = kwargs.get("actual_table", None)
        actual_schema = kwargs.get("actual_schema", None)
        confidence = kwargs.get("confidence", None)
        output_dir = kwargs.get("output_dir", None)
        # check predict_result in the hana db
        if not self.connection_context.has_table(predict_result, schema=predict_schema):
            return json.dumps({"error": f"Table {predict_result} does not exist."})
        # check actual_table in the hana db
        if actual_table is not None and not self.connection_context.has_table(actual_table, schema=actual_schema):
            return json.dumps({"error": f"Table {actual_table} does not exist."})
        predict_df = self.connection_context.table(predict_result, schema=predict_schema)
        if confidence is None:
            if "YHAT_LOWER" in predict_df.columns and "YHAT_UPPER" in predict_df.columns:
                # check if "YHAT_LOWER" column has values
                if not predict_df["YHAT_LOWER"].collect()["YHAT_LOWER"].isnull().all():
                    confidence = ("YHAT_LOWER", "YHAT_UPPER")
            elif "LO80" in predict_df.columns and "HI80" in predict_df.columns:
                if not predict_df["LO80"].collect()["LO80"].isnull().all():
                    confidence = ("LO80", "HI80")
            elif "LO95" in predict_df.columns and "HI95" in predict_df.columns:
                if not predict_df["LO95"].collect()["LO95"].isnull().all():
                    if confidence is None:
                        confidence = ("LO95", "HI95")
                    else:
                        confidence = confidence + ("LO95", "HI95")
            elif "PI1_LOWER" in predict_df.columns and "PI1_UPPER" in predict_df.columns:
                if not predict_df["PI1_LOWER"].collect()["PI1_LOWER"].isnull().all():
                    confidence = ("PI1_LOWER", "PI1_UPPER")
            elif "PI2_LOWER" in predict_df.columns and "PI2_UPPER" in predict_df.columns:
                if not predict_df["PI2_LOWER"].collect()["PI2_LOWER"].isnull().all():
                    if confidence is None:
                        confidence = ("PI2_LOWER", "PI2_UPPER")
                    else:
                        confidence = confidence + ("PI2_LOWER", "PI2_UPPER")

        if actual_table is None:
            fig = forecast_line_plot(predict_df, confidence=confidence)
        else:
            fig = forecast_line_plot(predict_df, self.connection_context.table(actual_table, schema=actual_schema), confidence)
        if output_dir is None:
            destination_dir = os.path.join(tempfile.gettempdir(), "hanaml_chart")
        else:
            destination_dir = output_dir
        if not os.path.exists(destination_dir):
            try:
                os.makedirs(destination_dir, exist_ok=True)
            except Exception as e:
                logger.error("Error creating directory %s: %s", destination_dir, e)
                raise
        output_file = os.path.join(
                    destination_dir,
                    f"{predict_result}_forecast_line_plot.html",
                )
        with Path(output_file).open("w", encoding="utf-8") as f:
            f.write(fig.to_html(full_html=True))
        if not self.bas:
            fig.show() #directly display in jupyter
        return json.dumps({"html_file": str(Path(output_file).as_posix())}, ensure_ascii=False)

    async def _arun(
        self, **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs
        )
