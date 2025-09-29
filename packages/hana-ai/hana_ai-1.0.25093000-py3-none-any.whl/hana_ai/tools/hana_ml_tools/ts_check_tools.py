"""
This module is used to do some checks on the time series dataset.

The following classes are available:

    * :class `TimeSeriesCheck`
    * :class `StationarityTest`
    * :class `TrendTest`
    * :class `SeasonalityTest`
    * :class `WhiteNoiseTest`
"""

import json
import logging
from typing import Optional, Type
from pydantic import BaseModel, Field

from langchain_core.tools import BaseTool

from hana_ml import ConnectionContext
from hana_ml.algorithms.pal.tsa.stationarity_test import stationarity_test
from hana_ml.algorithms.pal.tsa.trend_test import trend_test
from hana_ml.algorithms.pal.tsa.seasonal_decompose import seasonal_decompose
from hana_ml.algorithms.pal.tsa.white_noise_test import white_noise_test

from hana_ai.tools.hana_ml_tools.utility import _CustomEncoder

logger = logging.getLogger(__name__)

def ts_char(df, key, endog):
    """
    This function is used to get the characteristics of time series data.

    Parameters
    ----------
    df : DataFrame
        The input DataFrame.
    key : str
        The key column of the DataFrame.
    endog : str
        The endogenous column of the DataFrame.
    """
    analysis_result = ''

    # Table info
    table_struct = json.dumps(df.get_table_structure())
    analysis_result += f"Table structure: {table_struct}\n"
    analysis_result += f"Key: {key}\n"
    analysis_result += f"Endog: {endog}\n"

    # Index info
    analysis_result += f"Index: starts from {df[key].min()} to {df[key].max()}. Time series length is {df.count()}\n"

    key_col_type = df.get_table_structure()[key]
    key_ = key
    df_ = df
    if 'INT' not in key_col_type.upper():
        key_ = "NEW_" + key
        df_ = df.add_id(key_, ref_col=key)

    # Intermitent Test
    zero_values = df_.filter(f'"{endog}" = 0').count()
    total_values = df_.count()
    if total_values == 0:
        zero_proportion = 1
    else:
        zero_proportion = zero_values / total_values
    analysis_result += f"Intermittent Test: proportion of zero values is {zero_proportion}\n"

    # Stationarity Test
    result = stationarity_test(df_, key_, endog).collect()
    analysis_result += "Stationarity Test: "
    for _, row in result.iterrows():
        analysis_result += f"The `{row['STATS_NAME']}` is {row['STATS_VALUE']}."
    analysis_result += "\n"

    # Trend Test
    result = trend_test(df_, key_, endog)[0].collect()
    for _, row in result.iterrows():
        if row['STAT_NAME'] == 'TREND':
            if row['STAT_VALUE'] == 1:
                analysis_result += 'Trend Test:' + " Upward trend."
            elif row['STAT_VALUE'] == -1:
                analysis_result += 'Trend Test:' + " Downward trend."
            else:
                analysis_result += 'Trend Test:' + " No trend."
    analysis_result += "\n"

    # Seasonality Test
    result = seasonal_decompose(df_, key_, endog)[0].collect()
    analysis_result += "Seasonality Test: "
    for _, row in result.iterrows():
        analysis_result += f"The `{row['STAT_NAME']}` is {row['STAT_VALUE']}."
    analysis_result += "\n"

    # Restrict time series algorithms
    available_algorithms = ["Additive Model Forecast", "Automatic Time Series Forecast"]
    analysis_result += f"Available algorithms: {', '.join(available_algorithms)}\n"

    return analysis_result

def ts_char_massive(df, group_key, key, endog):
    """
    This function is used to get the characteristics of multiple time series data grouped by group_key.

    Parameters
    ----------
    df : DataFrame
        The input DataFrame.
    group_key : str
        The column used to group multiple time series.
    key : str
        The key column (time index) of the DataFrame.
    endog : str
        The endogenous column of the DataFrame.
    """
    # 获取所有分组
    groups = df.select(group_key).distinct().collect()[group_key].to_list()
    analysis_result = f"Time Series Analysis Report ({len(groups)} groups)\n"
    analysis_result += "=" * 60 + "\n\n"

    # 遍历每个分组
    for i, group_val in enumerate(groups):
        if isinstance(group_val, str):
            df_group = df.filter(f'"{group_key}" = \'{group_val}\'')
        else:
            df_group = df.filter(f'"{group_key}" = {group_val}')

        analysis_result += f"Group {i+1}/{len(groups)}: {group_key} = {group_val}\n"
        analysis_result += "-" * 60 + "\n"

        # 表结构信息
        table_struct = json.dumps(df_group.get_table_structure())
        analysis_result += f"• Table structure: {table_struct}\n"
        analysis_result += f"• Key: {key}\n"
        analysis_result += f"• Endog: {endog}\n"

        # 索引信息
        analysis_result += f"Index: starts from {df_group[key].min()} to {df_group[key].max()}. Time series length is {df_group.count()}\n"

        # 处理非整数类型的时间键
        key_col_type = df_group.get_table_structure()[key]
        key_ = key
        df_ = df_group
        if 'INT' not in key_col_type.upper():
            key_ = "NEW_" + key
            df_ = df_group.add_id(key_, ref_col=key)

        # Intermitent Test
        zero_values = df_.filter(f'"{endog}" = 0').count()
        total_values = df_.count()
        if total_values == 0:
            zero_proportion = 1
        else:
            zero_proportion = zero_values / total_values
        analysis_result += f"Intermittent Test: proportion of zero values is {zero_proportion}\n"

        # Stationarity Test
        result = stationarity_test(df_, key_, endog).collect()
        analysis_result += "Stationarity Test: "
        for _, row in result.iterrows():
            analysis_result += f"The `{row['STATS_NAME']}` is {row['STATS_VALUE']}."
        analysis_result += "\n"

        # Trend Test
        result = trend_test(df_, key_, endog)[0].collect()
        for _, row in result.iterrows():
            if row['STAT_NAME'] == 'TREND':
                if row['STAT_VALUE'] == 1:
                    analysis_result += 'Trend Test:' + " Upward trend."
                elif row['STAT_VALUE'] == -1:
                    analysis_result += 'Trend Test:' + " Downward trend."
                else:
                    analysis_result += 'Trend Test:' + " No trend."
        analysis_result += "\n"

        # Seasonality Test
        result = seasonal_decompose(df_, key_, endog)[0].collect()
        analysis_result += "Seasonality Test: "
        for _, row in result.iterrows():
            analysis_result += f"The `{row['STAT_NAME']}` is {row['STAT_VALUE']}."
        analysis_result += "\n"

        # Restrict time series algorithms
        available_algorithms = ["Additive Model Forecast", "Automatic Time Series Forecast"]
        analysis_result += f"Available algorithms: {', '.join(available_algorithms)}\n"

    return analysis_result

class TSCheckInput(BaseModel):
    """
    The input schema for the TimeSeriesCheckTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)

class MassiveTSCheckInput(BaseModel):
    """
    The input schema for the TimeSeriesCheckTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    group_key: str = Field(description="the group key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)

class StationarityTestInput(BaseModel):
    """
    The input schema for the StationarityTestTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)
    method: Optional[str] = Field(description="the method of the stationarity test chosen from {'kpss', 'adf'}, it is optional", default=None)
    mode: Optional[str] = Field(description="the mode of the stationarity test chosen from {'level', 'trend', 'no'}, it is optional", default=None)
    lag: Optional[int] = Field(description="the lag of the stationarity test, it is optional", default=None)
    probability: Optional[float] = Field(description="the confidence level for confirming stationarity, it is optional", default=None)

class TrendTestInput(BaseModel):
    """
    The input schema for the TrendTestTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)
    method: Optional[str] = Field(description="the method of the trend test chosen from {'mk', 'difference-sign'}, it is optional", default=None)
    alpha: Optional[float] = Field(description="the significance level for the trend test, it is optional", default=None)

class SeasonalityTestInput(BaseModel):
    """
    The input schema for the SeasonalityTestTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)
    alpha: Optional[float] = Field(description="the criterion for the autocorrelation coefficient, it is optional", default=None)
    decompose_type: Optional[str] = Field(description="the type of decomposition chosen from {'additive', 'multiplicative', 'auto'}, it is optional", default=None)
    extrapolation: Optional[bool] = Field(description="whether to extrapolate the endpoints or not, it is optional", default=None)
    smooth_width: Optional[int] = Field(description="the width of the smoothing window, it is optional", default=None)
    auxiliary_normalitytest: Optional[bool] = Field(description="specifies whether to use normality test to identify model types, it is optional", default=None)
    periods: Optional[int] = Field(description="the length of the periods, it is optional", default=None)
    decompose_method: Optional[str] = Field(description="the method of decomposition chosen from {'stl', 'traditional'}, it is optional", default=None)
    stl_robust: Optional[bool] = Field(description="whether to use robust decomposition or not only valid for 'stl' decompose method, it is optional", default=None)
    stl_seasonal_average: Optional[bool] = Field(description="whether to use seasonal average or not only valid for 'stl' decompose method, it is optional", default=None)
    smooth_method_non_seasonal: Optional[str] = Field(description="the method of smoothing for non-seasonal component chosen from {'moving_average', 'super_smoother'}, it is optional", default=None)

class WhiteNoiseTestInput(BaseModel):
    """
    The input schema for the WhiteNoiseTestTool.
    """
    table_name: str = Field(description="the name of the table. If not provided, ask the user. Do not guess.")
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: str = Field(description="the endog of the dataset. If not provided, ask the user. Do not guess.")
    schema_name: Optional[str] = Field(description="the schema_name of the table, it is optional", default=None)
    lag: Optional[int] = Field(description="specifies the lag autocorrelation coefficient that the statistic will be based on, it is optional", default=None)
    probability: Optional[float] = Field(description="the confidence level used for chi-square distribution., it is optional", default=None)
    model_df: Optional[int] = Field(description="the degree of freedom of the model, it is optional", default=None)

class TimeSeriesCheck(BaseTool):
    """
    This tool calls stationarity test, intermittent check, trend test and seasonality test for the given time series data.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The characteristics of the time series data.

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
                * - schema_name
                  - the schema_name of the table, it is optional
    """
    name: str = "ts_check"
    """Name of the tool."""
    description: str = "To check the time series data for stationarity, intermittent, trend and seasonality."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = TSCheckInput
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
        # check table exists
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return f"Table {table_name} does not exist."
        # check key and endog columns exist
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Key column {key} does not exist in table {table_name}."
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Endog column {endog} does not exist in table {table_name}."
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        return ts_char(df, key, endog)

    async def _arun(
        self, **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)

class MassiveTimeSeriesCheck(BaseTool):
    """
    This tool performs time series analysis for multiple grouped time series data, 
    including stationarity, intermittency, trend and seasonality tests.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The characteristics report for multiple time series groups.

        .. note::

            args_schema is used to define the schema of the inputs as follows:

            .. list-table::
                :widths: 15 50
                :header-rows: 1

                * - Field
                  - Description
                * - table_name
                  - The name of the table. If not provided, ask the user. Do not guess.
                * - group_key
                  - The column used to group multiple time series. Required.
                * - key
                  - The time key column. If not provided, ask the user. Do not guess.
                * - endog
                  - The endogenous variable column. If not provided, ask the user. Do not guess.
                * - schema_name
                  - The schema name of the table (optional)
    """
    name: str = "massive_ts_check"
    """Name of the tool."""
    description: str = (
        "Performs comprehensive time series analysis per group(group_key Column), "
        "including stationarity, intermittency, trend and seasonality tests."
    )
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = MassiveTSCheckInput
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
        """Use the tool for massive time series analysis."""
        if "kwargs" in kwargs:
            kwargs = kwargs["kwargs"]

        # Validate required parameters
        table_name = kwargs.get("table_name")
        if not table_name:
            return "Table name is required"

        group_key = kwargs.get("group_key")
        if not group_key:
            return "Group key is required for massive time series analysis"

        key = kwargs.get("key")
        if not key:
            return "Time key is required"

        endog = kwargs.get("endog")
        if not endog:
            return "Endogenous variable is required"

        schema_name = kwargs.get("schema_name")

        # Check table existence
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return f"Table {table_name} does not exist."

        # Get table reference
        table = self.connection_context.table(table_name, schema=schema_name)

        # Validate columns exist
        required_columns = [group_key, key, endog]
        for col in required_columns:
            if col not in table.columns:
                return f"Column '{col}' does not exist in table {table_name}."

        # Select relevant columns
        df = table.select(group_key, key, endog)

        # Check if group_key has reasonable number of groups
        distinct_groups = df.select(group_key).distinct().count()
        if distinct_groups > 100:
            return (
                f"Too many groups ({distinct_groups}) for analysis. "
                "Consider filtering or using a different group key."
            )

        # Perform massive time series analysis
        return ts_char_massive(df, group_key, key, endog)

    async def _arun(
        self, **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)

class StationarityTest(BaseTool):
    """
    This tool calls stationarity test for the given time series data.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The stationarity statistics of the time series data.

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
                * - schema_name
                  - the schema_name of the table, it is optional
                * - method
                  - the method of the stationarity test chosen from {'kpss', 'adf'}, it is optional
                * - mode
                  - the mode of the stationarity test chosen from {'level', 'trend', 'no'}, it is optional
                * - lag
                  - the lag of the stationarity test, it is optional
                * - probability
                  - the confidence level for confirming stationarity, it is optional
    """
    name: str = "stationarity_test"
    """Name of the tool."""
    description: str = "To check the stationarity of the time series data."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = StationarityTestInput
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
        method = kwargs.get("method", None)
        mode = kwargs.get("mode", None)
        lag = kwargs.get("lag", None)
        probability = kwargs.get("probability", None)
        # check table exists
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return f"Table {table_name} does not exist."
        # check key and endog columns exist
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Key column {key} does not exist in table {table_name}."
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Endog column {endog} does not exist in table {table_name}."
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        result = stationarity_test(data=df,
                                   key=key,
                                   endog=endog,
                                   method=method,
                                   mode=mode,
                                   lag=lag,
                                   probability=probability).collect()
        analysis_result = {}
        for _, row in result.iterrows():
            analysis_result[row['STATS_NAME']] = row['STATS_VALUE']
        return json.dumps(analysis_result, cls=_CustomEncoder)

    async def _arun(
        self,
        **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)

class TrendTest(BaseTool):
    """
    This tool calls trend test for the given time series data.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The trend statistics of the time series data.

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
                * - schema_name
                  - the schema_name of the table, it is optional
                * - method
                  - the method of the trend test chosen from {'mk', 'difference-sign'}, it is optional
                * - alpha
                  - the significance level for the trend test, it is optional
    """
    name: str = "trend_test"
    """Name of the tool."""
    description: str = "To check the trend of the time series data."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = TrendTestInput
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
        method = kwargs.get("method", None)
        alpha = kwargs.get("alpha", None)
        schema_name = kwargs.get("schema_name", None)
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return f"Table {table_name} does not exist."
        # check key and endog columns exist
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Key column {key} does not exist in table {table_name}."
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Endog column {endog} does not exist in table {table_name}."
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        result = trend_test(data=df,
                            key=key,
                            endog=endog,
                            method=method,
                            alpha=alpha)[0].collect()
        analysis_result = {}
        for _, row in result.iterrows():
            if row['STAT_NAME'] == 'TREND':
                if row['STAT_VALUE'] == 1:
                    analysis_result['Trend'] = "Upward trend."
                elif row['STAT_VALUE'] == -1:
                    analysis_result['Trend'] = "Downward trend."
                else:
                    analysis_result['Trend'] = "No trend."
        return json.dumps(analysis_result, cls=_CustomEncoder)

    async def _arun(
        self,
        **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)

class SeasonalityTest(BaseTool):
    """
    This tool calls seasonality test for the given time series data.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The seasonality of the time series data.

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
                * - schema_name
                  - the schema_name of the table, it is optional
                * - alpha
                  - the criterion for the autocorrelation coefficient, it is optional
                * - decompose_type
                  - the type of decomposition chosen from {'additive', 'multiplicative', 'auto'}, it is optional
                * - extrapolation
                  - whether to extrapolate the endpoints or not, it is optional
                * - smooth_width
                  - the width of the smoothing window, it is optional
                * - auxiliary_normalitytest
                  - specifies whether to use normality test to identify model types, it is optional
                * - periods
                  - the length of the periods, it is optional
                * - decompose_method
                  - the method of decomposition chosen from {'stl', 'traditional'}, it is optional
                * - stl_robust
                  - whether to use robust decomposition or not only valid for 'stl' decompose method, it is optional
                * - stl_seasonal_average
                  - whether to use seasonal average or not only valid for 'stl' decompose method, it is optional
                * - smooth_method_non_seasonal
                  - the method of smoothing for non-seasonal component chosen from {'moving_average', 'super_smoother'}, it is optional
    """
    name: str = "seasonality_test"
    """Name of the tool."""
    description: str = "To check the seasonality of the time series data."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = SeasonalityTestInput
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
        alpha = kwargs.get("alpha", None)
        decompose_type = kwargs.get("decompose_type", None)
        extrapolation = kwargs.get("extrapolation", None)
        smooth_width = kwargs.get("smooth_width", None)
        auxiliary_normalitytest = kwargs.get("auxiliary_normalitytest", None)
        periods = kwargs.get("periods", None)
        decompose_method = kwargs.get("decompose_method", None)
        stl_robust = kwargs.get("stl_robust", None)
        stl_seasonal_average = kwargs.get("stl_seasonal_average", None)
        smooth_method_non_seasonal = kwargs.get("smooth_method_non_seasonal", None)
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return f"Table {table_name} does not exist."
        # check key and endog columns exist
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Key column {key} does not exist in table {table_name}."
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Endog column {endog} does not exist in table {table_name}."
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        result = seasonal_decompose(data=df,
                                    key=key,
                                    endog=endog,
                                    alpha=alpha,
                                    decompose_type=decompose_type,
                                    extrapolation=extrapolation,
                                    smooth_width=smooth_width,
                                    auxiliary_normalitytest=auxiliary_normalitytest,
                                    periods=periods,
                                    decompose_method=decompose_method,
                                    stl_robust=stl_robust,
                                    stl_seasonal_average=stl_seasonal_average,
                                    smooth_method_non_seasonal=smooth_method_non_seasonal)[0].collect()
        analysis_result = {}
        for _, row in result.iterrows():
            analysis_result[row['STAT_NAME']] = row['STAT_VALUE']
        return json.dumps(analysis_result, cls=_CustomEncoder)

    async def _arun(
        self,
        **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)

class WhiteNoiseTest(BaseTool):
    """
    This tool calls white noise test for the given time series data.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The white noise statistics of the time series data.

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
                * - schema_name
                  - the schema_name of the table, it is optional
                * - lag
                  - specifies the lag autocorrelation coefficient that the statistic will be based on, it is optional
                * - probability
                  - the confidence level used for chi-square distribution., it is optional
                * - model_df
                  - the degree of freedom of the model, it is optional
    """
    name: str = "white_noise_test"
    """Name of the tool."""
    description: str = "To check the white noise of the time series data."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = WhiteNoiseTestInput
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
        lag = kwargs.get("lag", None)
        probability = kwargs.get("probability", None)
        model_df = kwargs.get("model_df", None)
        schema_name = kwargs.get("schema_name", None)
        # check table exists
        if not self.connection_context.has_table(table_name, schema=schema_name):
            return f"Table {table_name} does not exist."
        # check key and endog columns exist
        if key not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Key column {key} does not exist in table {table_name}."
        if endog not in self.connection_context.table(table_name, schema=schema_name).columns:
            return f"Endog column {endog} does not exist in table {table_name}."
        df = self.connection_context.table(table_name, schema=schema_name).select(key, endog)
        result = white_noise_test(data=df,
                                  key=key,
                                  endog=endog,
                                  lag=lag,
                                  probability=probability,
                                  model_df=model_df).collect()
        analysis_result = {}
        for _, row in result.iterrows():
            analysis_result[row['STAT_NAME']] = row['STAT_VALUE']
        return json.dumps(analysis_result, cls=_CustomEncoder)

    async def _arun(
        self,
        **kwargs
    ) -> str:
        """Use the tool asynchronously."""
        return self._run(**kwargs)
