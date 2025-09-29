"""
This module contains the tools for additive model forecast.

The following class are available:

    * :class `AdditiveModelForecastFitAndSave`
    * :class `AdditiveModelForecastLoadModelAndPredict`
"""
#pylint: disable=too-many-return-statements

import json
import logging
from typing import Optional, Type, Union
from pydantic import BaseModel, Field
from langchain_core.tools import BaseTool

from hana_ml import ConnectionContext
from hana_ml.model_storage import ModelStorage
from hana_ml.algorithms.pal.tsa.additive_model_forecast import AdditiveModelForecast

from hana_ai.tools.hana_ml_tools.utility import _CustomEncoder, generate_model_storage_version, _create_temp_table

logger = logging.getLogger(__name__)

def _guess_fourier_order(period: int) -> int:
    # Calculate base value and round to nearest integer
    base_value = round(float(period) / 36.5)

    # Apply bounds: minimum 3, maximum 10
    return max(3, min(10, base_value))

class ModelFitInput(BaseModel):
    """
    This class is used to define the schema of the inputs for fitting the model
    """
    fit_select_statement: str = Field(description="The SQL select statement of the data to fit the model. " +\
    "If not provided, ask the user. Do not guess.")
    name: str = Field(description="the name of the model in model storage. If not provided, ask the user. Do not guess.")
    version: Optional[int] = Field(description="the version of the model in model storage, it is optional", default=None)
    #fit_schema: Optional[str] = Field(description="the schema of the fit_table, it is optional", default=None)
    # init args
    growth: Optional[str] = Field(description="the growth of the model chosen from {'linear', 'logistic'}, it is optional", default=None)
    logistic_growth_capacity: Optional[float] = Field(description="the logistic growth capacity of the model only valid when growth is 'logistic', it is optional", default=None)
    seasonality_mode: Optional[str] = Field(description="the seasonality mode of the model chosen from {'additive', 'multiplicative'}, it is optional", default=None)
    #seasonality: Optional[str] = Field(description="adds seasonality to the model in a json format such that each str is in json format '{\"NAME\": \"MONTHLY\", \"PERIOD\":30, \"FOURIER_ORDER\":5 }', it is optional", default=None)
    period: Union[Optional[int], Optional[list]] = Field(description="the period of the seasonality and it could also be a list of periods, it is optional", default=None)
    num_changepoints: Optional[int] = Field(description="the number of changepoints in the model, it is optional", default=None)
    changepoint_range: Optional[float] = Field(description="the proportion of history in which trend changepoints will be estimated, it is optional", default=None)
    regressor: Optional[list] = Field(description="specifies the regressor in a list of json such that ['{\"NAME\": \"X1\", \"PRIOR_SCALE\":4, \"MODE\": \"additive\" }'], it is optional", default=None)
    changepoints: Optional[list] = Field(description="specifies a list of changepoints in the format of timestamp, such as ['2019-01-01 00:00:00, '2019-02-04 00:00:00'], it is optional", default=None)
    yearly_seasonality: Optional[str] = Field(description="Specifies whether or not to fit yearly seasonality chosen from {'auto', 'false', 'true'}, it is optional", default=None)
    weekly_seasonality: Optional[str] = Field(description="Specifies whether or not to fit weekly seasonality chosen from {'auto', 'false', 'true'}, it is optional", default=None)
    daily_seasonality: Optional[str] = Field(description="Specifies whether or not to fit daily seasonality chosen from {'auto', 'false', 'true'}, it is optional", default=None)
    seasonality_prior_scale: Optional[float] = Field(description="the parameter modulating the strength of the seasonality model, it is optional", default=None)
    holiday_prior_scale: Optional[float] = Field(description="the parameter modulating the strength of the holiday model, it is optional", default=None)
    changepoint_prior_scale: Optional[float] = Field(description="the parameter modulating the flexibility of the automatic changepoint selection, it is optional", default=None)
    # fit args
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    endog: Optional[str] = Field(description="the endog of the dataset, it is optional", default=None)
    exog: Union[Optional[str], Optional[list]] = Field(description="the exog of the dataset, it is optional", default=None)
    categorical_variable: Union[Optional[str], Optional[list]] = Field(description="the categorical variable of the dataset, it is optional", default=None)

class ModelPredictInput(BaseModel):
    """
    This class is used to define the schema of the inputs for predicting the model
    """
    predict_select_statement: str = Field(description="The SQL select statement of the data to make predictions. If not provided, ask the user. Do not guess.")
    name: str = Field(description="the name of the model. If not provided, ask the user. Do not guess.")
    version: Optional[int] = Field(description="the version of the model, it is optional", default=None)
    # predict args
    key: str = Field(description="the key of the dataset. If not provided, ask the user. Do not guess.")
    exog: Union[Optional[str], Optional[list]] = Field(description="the exog of the dataset, it is optional", default=None)
    logistic_growth_capacity: Optional[float] = Field(description="the logistic growth capacity of the model only valid when growth is 'logistic', it is optional", default=None)
    interval_width: Optional[float] = Field(description="the width of the uncertainty interval, it is optional", default=None)
    uncertainty_samples: Optional[int] = Field(description="the number of simulated draws used to estimate uncertainty intervals, it is optional", default=None)
    show_explainer: Optional[bool] = Field(description="whether to show explainer, it is optional", default=None)
    decompose_seasonality: Optional[bool] = Field(description="whether to decompose seasonality only valid when show_explainer is True, it is optional", default=None)
    decompose_holiday: Optional[bool] = Field(description="whether to decompose holiday only valid when show_explainer is True, it is optional", default=None)
    add_placeholder: Optional[bool] = Field(description="whether to add placeholder for the endog column and it is set True by default, it is optional", default=True)

class AdditiveModelForecastFitAndSave(BaseTool):
    r"""
    This tool is used to fit and predict the additive model forecast.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The result string containing the training table name, model storage name, and model storage version.

        .. note::

            args_schema is used to define the schema of the inputs as follows:

            .. list-table::
                :widths: 15 50
                :header-rows: 1

                * - Field
                  - Description
                * - fit_select_statement
                  - The SQL select statement of the training dataset.
                * - key
                  - The key (ID) column of the training dataset.
                * - endog
                  - The endogenous variable of the training dataset.
                * - exog
                  - The exogeneous variables of the training data, serving as external regressors to be included in the model.
                * - name
                  - The name of the model to save.
                * - version
                  - The version of the model to save.
                * - categorical_variable
                  - The categorical variable columns in the training table.
                * - growth
                  - The growth of the model chosen from {'linear', 'logistic'}.
                * - logistic_growth_capacity
                  - The logistic growth capacity of the model only valid when growth is 'logistic'.
                * - seasonality_mode
                  - The seasonality mode of the model chosen from {'additive', 'multiplicative'}.
                * - period
                  - The period of the seasonality or a list of periods.
                * - num_changepoints
                  - The number of changepoints in the model.
                * - changepoint_range
                  - The proportion of history in which trend changepoints will be estimated.
                * - regressor
                  - Specifies the regressor in a list of json such that ['{\"NAME\": \"X1\", \"PRIOR_SCALE\":4, \"MODE\": \"additive\" }'].
                * - changepoints
                  - Specifies a list of changepoints in the format of timestamp, such as ['2019-01-01 00:00:00, '2019-02-04 00:00:00'].
                * - yearly_seasonality
                  - Specifies whether or not to fit yearly seasonality chosen from {'auto', 'false', 'true'}.
                * - weekly_seasonality
                  - Specifies whether or not to fit weekly seasonality chosen from {'auto', 'false', 'true'}.
                * - daily_seasonality
                  - Specifies whether or not to fit daily seasonality chosen from {'auto', 'false', 'true'}.
                * - seasonality_prior_scale
                  - The parameter modulating the strength of the seasonality model.
                * - holiday_prior_scale
                  - The parameter modulating the strength of the holiday model.
                * - changepoint_prior_scale
                  - The parameter modulating the flexibility of the automatic changepoint selection.

    """
    name: str = "additive_model_forecast_fit_and_save"
    """Name of the tool."""
    description: str = "To fit the additive model forecast and save the model in model storage."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = ModelFitInput
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
        fit_select_statement = kwargs.get("fit_select_statement", None)
        if fit_select_statement is None:
            return "The SQL select statement of the training dataset is required"
        key = kwargs.get("key", None)
        if key is None:
            return "key is required"
        name = kwargs.get("name", None)
        if name is None:
            return "Model name is required"
        version = kwargs.get("version", None)
        growth = kwargs.get("growth", None)
        logistic_growth_capacity = kwargs.get("logistic_growth_capacity", None)
        seasonality_mode = kwargs.get("seasonality_mode", None)
        period = kwargs.get("period", None)
        num_changepoints = kwargs.get("num_changepoints", None)
        changepoint_range = kwargs.get("changepoint_range", None)
        regressor = kwargs.get("regressor", None)
        changepoints = kwargs.get("changepoints", None)
        yearly_seasonality = kwargs.get("yearly_seasonality", None)
        weekly_seasonality = kwargs.get("weekly_seasonality", None)
        daily_seasonality = kwargs.get("daily_seasonality", None)
        seasonality_prior_scale = kwargs.get("seasonality_prior_scale", None)
        holiday_prior_scale = kwargs.get("holiday_prior_scale", None)
        changepoint_prior_scale = kwargs.get("changepoint_prior_scale", None)
        endog = kwargs.get("endog", None)
        exog = kwargs.get("exog", None)
        categorical_variable = kwargs.get("categorical_variable", None)
        if key not in self.connection_context.sql(fit_select_statement).columns:
            return f"Key {key} does not exist in the training dataset."
        ms = ModelStorage(connection_context=self.connection_context)
        seasonality = None
        if period:
            if isinstance(period, list):
                seasonality = []
                for idx, p in enumerate(period):
                    fo = _guess_fourier_order(p)
                    seasonality.append(f'{{"NAME": "SEASONALITY_{idx}", "PERIOD":{p}, "FOURIER_ORDER":{fo} }}')
            else:
                fo = _guess_fourier_order(period)
                seasonality = f'{{"NAME": "SEASONALITY", "PERIOD":{period}, "FOURIER_ORDER":{fo} }}'
        try:
            amf = AdditiveModelForecast(
                growth=growth,
                logistic_growth_capacity=logistic_growth_capacity,
                seasonality_mode=seasonality_mode,
                seasonality=seasonality,
                num_changepoints=num_changepoints,
                changepoint_range=changepoint_range,
                regressor=regressor,
                changepoints=changepoints,
                yearly_seasonality=yearly_seasonality,
                weekly_seasonality=weekly_seasonality,
                daily_seasonality=daily_seasonality,
                seasonality_prior_scale=seasonality_prior_scale,
                holiday_prior_scale=holiday_prior_scale,
                changepoint_prior_scale=changepoint_prior_scale)
            amf.fit(data=self.connection_context.sql(fit_select_statement),
                  key=key,
                  endog=endog,
                  exog=exog,
                  holiday=None,
                  categorical_variable=categorical_variable)
        except ValueError as ve:
            # Handles invalid parameter values (e.g., alpha not in [0,1])
            return f"ValueError occurred: {str(ve)}"

        except KeyError as ke:
            # Handles missing columns in the DataFrame
            return f"KeyError occurred: {str(ke)}"

        except TypeError as te:
            # Handles type mismatches (e.g., non-numeric input where number expected)
            return f"TypeError occurred: {str(te)}"

        amf.name = name
        amf.version = generate_model_storage_version(ms, version, name)
        ms.save_model(model=amf, if_exists='replace')
        return json.dumps({"fit_select_statement": fit_select_statement, "model_storage_name": name, "model_storage_version": amf.version}, cls=_CustomEncoder)

    async def _arun(
        self,
        **kwargs
    ) -> str:
        return self._run(**kwargs
        )

class AdditiveModelForecastLoadModelAndPredict(BaseTool):
    r"""
    This tool is used to load the additive model forecast from model storage and predict.

    Parameters
    ----------
    connection_context : ConnectionContext
        Connection context to the HANA database.

    Returns
    -------
    str
        The name of the predicted results table.

        .. note::

            args_schema is used to define the schema of the inputs as follows:

            .. list-table::
                :widths: 15 50
                :header-rows: 1

                * - Field
                  - Description
                * - predict_select_statement
                  - The SQL select statement of the prediction dataset.
                * - key
                  - The key (ID) column of prediction dataset.
                * - name
                  - The name of the model to load.
                * - version
                  - The version of the model to load.
                * - exog
                  - Exogenous variables of the prediction datasets, serving as external regressors for prediction.
                * - logistic_growth_capacity
                  - Capacity for logistic growth.
                * - interval_width
                  - Width of the prediction intervals.
                * - uncertainty_samples
                  - Number of uncertainty samples to draw.
                * - show_explainer
                  - Whether to show the explainer.
                * - decompose_seasonality
                  - Whether to decompose seasonality.
                * - decompose_holiday
                  - Whether to decompose holiday effects.
    """
    name: str = "additive_model_forecast_load_model_and_predict"
    """Name of the tool."""
    description: str = "To load the additive model forecast from model storage and predict."
    """Description of the tool."""
    connection_context: ConnectionContext = None
    """Connection context to the HANA database."""
    args_schema: Type[BaseModel] = ModelPredictInput
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
        predict_select_statement = kwargs.get("predict_select_statement", None)
        if predict_select_statement is None:
            return "The select statement of prediction dataset is required"
        key = kwargs.get("key", None)
        if key is None:
            return "Key is required"
        name = kwargs.get("name", None)
        if name is None:
            return "Model name is required"
        version = kwargs.get("version", None)
        exog = kwargs.get("exog", None)
        logistic_growth_capacity = kwargs.get("logistic_growth_capacity", None)
        interval_width = kwargs.get("interval_width", None)
        uncertainty_samples = kwargs.get("uncertainty_samples", None)
        show_explainer = kwargs.get("show_explainer", None)
        decompose_seasonality = kwargs.get("decompose_seasonality", None)
        decompose_holiday = kwargs.get("decompose_holiday", None)
        add_placeholder = kwargs.get("add_placeholder", True)

        predict_df = self.connection_context.sql(predict_select_statement)
        if key not in predict_df.columns:
            return f"Key {key} does not exist in the prediction dataset."
        ms = ModelStorage(connection_context=self.connection_context)
        model = ms.load_model(name=name, version=version)
        if hasattr(model, 'version'):
            if model.version is not None:
                version = model.version
        if len(predict_df.columns) == 1:
            predict_df = predict_df.add_constant("PLACEHOLDER", 0)
        try:
            model.predict(data=predict_df,
                          key=key,
                          exog=exog,
                          logistic_growth_capacity=logistic_growth_capacity,
                          interval_width=interval_width,
                          uncertainty_samples=uncertainty_samples,
                          show_explainer=show_explainer,
                          decompose_seasonality=decompose_seasonality,
                          decompose_holiday=decompose_holiday,
                          add_placeholder=add_placeholder)
        except ValueError as ve:
            # Handles invalid parameter values (e.g., alpha not in [0,1])
            return f"ValueError occurred: {str(ve)}"

        except KeyError as ke:
            # Handles missing columns in the DataFrame
            return f"KeyError occurred: {str(ke)}"

        except TypeError as te:
            # Handles type mismatches (e.g., non-numeric input where number expected)
            return f"TypeError occurred: {str(te)}"
        ms.save_model(model=model, if_exists='replace_meta')
        if show_explainer is True:
            return json.dumps({"predicted_results_select_statement": _create_temp_table(self.connection_context,
                                                                                        model.forecast_result.select_statement,
                                                                                        self.name,
                                                                                        additional_info="PREDICTED_RESULTS"),
                               "decomposed_and_reason_code_select_statement": _create_temp_table(self.connection_context,
                                                                                                 model.reason_code.select_statement,
                                                                                                 self.name,
                                                                                                 additional_info="REASON_CODE")})
        return json.dumps({"predicted_results_select_statement": _create_temp_table(self.connection_context,
                                                                                    model.forecast_result.select_statement,
                                                                                    self.name,
                                                                                    additional_info="PREDICTED_RESULTS")})

    async def _arun(
        self,
        **kwargs
    ) -> str:
        return self._run(
            **kwargs
        )
