"""
Smart DataFrame.

The following class is available:

    * :class `SmartDataFrame`
"""
from typing import List
from langchain.llms.base import BaseLLM
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate
from langchain.schema import SystemMessage
from langchain.tools import BaseTool
from langchain.agents import AgentExecutor, create_openai_functions_agent
from hana_ml.dataframe import DataFrame
from hana_ai.tools.df_tools.fetch_tools import FetchDataTool
from hana_ai.tools.df_tools.ts_outlier_detection_tools import TSOutlierDetection
from hana_ai.tools.df_tools.ts_visualizer_tools import TimeSeriesDatasetReport
from hana_ai.tools.df_tools.automatic_timeseries_tools import AutomaticTimeSeriesFitAndSave, AutomaticTimeSeriesLoadModelAndPredict, AutomaticTimeSeriesLoadModelAndScore
from hana_ai.tools.df_tools.additive_model_forecast_tools import AdditiveModelForecastFitAndSave, AdditiveModelForecastLoadModelAndPredict
from hana_ai.tools.df_tools.intermittent_forecast_tools import IntermittentForecast

class SmartDataFrame(DataFrame):
    """
    Smart DataFrame.

    Parameters
    ----------
    dataframe : DataFrame
        Dataframe.

    Examples
    --------
    >>> from hana_ai.smart_dataframe import SmartDataFrame

    >>> sdf = SmartDataFrame(dataframe=hana_df)
    >>> sdf.configure(llm=llm, verbose=True)
    >>> sdf.ask(question="Show the samples of the dataset")
    >>> new_sdf = sdf.transform(question="Get last two rows")
    """
    llm: BaseLLM
    _dataframe: DataFrame
    tools: List[BaseTool]
    agent: AgentExecutor
    kwargs: dict
    def __init__(self, dataframe: DataFrame):
        super(SmartDataFrame, self).__init__(dataframe.connection_context, dataframe.select_statement)
        self._dataframe = dataframe
        self._is_configured = False
        self.prefix = f"Given the select statement of a dataframe: {self._dataframe.select_statement}, "

    def configure(self,
                  llm: BaseLLM,
                  tools: List[BaseTool] = None,
                  verbose: bool = False,
                  **kwargs):
        """
        Configure the Smart DataFrame.

        Parameters
        ----------
        llm : BaseLLM
            LLM.
        toolkit : List of BaseTool, optional
            The dataframe toos to be used.

            Defaults to df_tools.
        """
        conn = self._dataframe.connection_context
        self.llm = llm
        if tools is None:
            tools = [
                FetchDataTool(conn),
                TimeSeriesDatasetReport(conn),
                TSOutlierDetection(conn),
                AutomaticTimeSeriesFitAndSave(conn),
                AutomaticTimeSeriesLoadModelAndPredict(conn),
                AutomaticTimeSeriesLoadModelAndScore(conn),
                AdditiveModelForecastFitAndSave(conn),
                AdditiveModelForecastLoadModelAndPredict(conn),
                IntermittentForecast(conn)
            ]
        self.tools = tools
        self.ask_tools = tools
        self.transform_tools = []

        for tool in tools:
            if hasattr(tool, 'is_transform'):
                self.transform_tools.append(tool.set_transform(True))

        self.kwargs = kwargs
        # Create the prompt template
        prompt = ChatPromptTemplate.from_messages([
            SystemMessage(content="You are a helpful assistant with access to tools. Always use tools when appropriate."),
            HumanMessagePromptTemplate.from_template("{input}"),
            MessagesPlaceholder(variable_name="agent_scratchpad")
        ])

        # Create the agent with tool bindings
        self.ask_agent = create_openai_functions_agent(self.llm, self.ask_tools, prompt)
        self.ask_executor = AgentExecutor.from_agent_and_tools(agent=self.ask_agent, tools=self.ask_tools, verbose=verbose)
        self.transform_agent = create_openai_functions_agent(self.llm, self.transform_tools, prompt)
        self.transform_executor = AgentExecutor.from_agent_and_tools(agent=self.transform_agent, tools=self.transform_tools, verbose=verbose)
        self._is_configured = True

    def ask(self, question: str):
        """
        Ask a question.

        Parameters
        ----------
        question : str
            Question.
        verbose : bool, optional
            Verbose. Default to False.
        """
        if self._is_configured is False:
            raise Exception("The SmartDataFrame is not configured. Please call the configure method first.")
        agent_input = {
            "input": [{
                "type": "text", 
                "text": f"Context:\n{self.prefix}\n\nQuestion: {question}"
            }]
        }
        return self.ask_executor.invoke(agent_input)["output"]

    @classmethod
    def _construct(cls, dataframe: DataFrame, llm: BaseLLM, tools: List[BaseTool], **kwargs):
        sdf = cls(dataframe)
        sdf.configure(llm, tools, **kwargs)
        return sdf

    def transform(self, question: str, output_key='output'):
        """
        Transform the dataframe.

        Parameters
        ----------
        question : str
            Question.
        verbose : bool, optional
            Verbose. Default to False.
        """
        if self._is_configured is False:
            raise Exception("The SmartDataFrame is not configured. Please call the configure method first.")

        # Updated prompt to demand ONLY the SQL statement
        agent_input = {
            "input": [{
                "type": "text", 
                "text": (
                    f"Context:\n{self.prefix}\n\n"
                    f"Question: {question}\n\n"
                    "IMPORTANT: Return ONLY the SQL select statement as a string. "
                    "DO NOT include any additional text, explanations, or formatting. "
                    "ONLY the raw SQL query."
                )
            }]
        }

        result = self.transform_executor.invoke(agent_input)
        select_statement = result['output']

        # Extract SQL from response if needed
        if not select_statement.strip().upper().startswith(('SELECT')):
            import re
            # Regex to find SQL starting with SELECT/WITH
            sql_match = re.search(
                r'\b(SELECT)\b.*',
                select_statement,
                re.DOTALL | re.IGNORECASE
            )
            if sql_match:
                select_statement = sql_match.group(0).strip()
            else:
                raise ValueError(
                    "Failed to extract valid SQL from agent response: "
                    f"{select_statement[:100]}..."
                )

        # Create new SmartDataFrame with generated SQL
        sdf = self._construct(
            self._dataframe.connection_context.sql(select_statement),
            self.llm,
            self.tools,
            **self.kwargs
        )
        return sdf
