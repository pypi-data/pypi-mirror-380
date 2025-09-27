import os
import re
import time

from langchain_core.runnables import RunnableConfig
from langgraph.graph.state import CompiledStateGraph

from ..logger import get_logger
from ..models.openai.models import CreateResponse, Response
from .base import FoundryCBAgent
from .common.agent_run_context import AgentRunContext
from .langgraph_models import (
    LangGraphRequestConverter,
    LangGraphResponseConverter,
    LangGraphStreamResponseConverter,
)


class LangGraphAdapter(FoundryCBAgent):
    """
    Adapter for LangGraph Agent.
    """

    def __init__(self, graph: CompiledStateGraph):
        """
        Initialize the LangGraphAdapter with a CompiledStateGraph.

        Args:
            graph (StateGraph): The LangGraph StateGraph to adapt.
        """
        super().__init__()
        self.graph = graph
        self.logger = get_logger()

    async def agent_run(self, request_body: CreateResponse, context: AgentRunContext):
        input_data = self.convert_request(request_body)
        self.logger.debug(f"Converted input data: {input_data}")
        if not request_body.stream:
            response = await self.agent_run_non_stream(input_data, context)
            return response
        else:
            return self.agent_run_astream(input_data, context)

    def init_tracing_internal(self):
        # add instrumentor
        from opentelemetry.instrumentation.langchain import LangchainInstrumentor

        LangchainInstrumentor().instrument()
        # set env vars for langsmith
        os.environ["LANGSMITH_OTEL_ENABLED"] = "true"
        os.environ["LANGSMITH_TRACING"] = "true"
        os.environ["LANGSMITH_OTEL_ONLY"] = "true"

    def setup_otlp_exporter(self, endpoint, provider):
        endpoint = self.format_otlp_endpoint(endpoint)
        return super().setup_otlp_exporter(endpoint, provider)

    def get_trace_attributes(self):
        attrs = super().get_trace_attributes()
        attrs["service.namespace"] = "azure.ai.agentshosting.langgraph"
        return attrs

    async def agent_run_non_stream(self, input_data: dict, context: AgentRunContext):
        """
        Run the agent with non-streaming response.

        Args:
            request_body (CreateRunRequest): The request body to run the agent with.

        Returns:
            RunObject: The result of the agent run.
        """

        try:
            # TODO: handling context
            config = self.create_runnable_config(context)
            result = await self.graph.ainvoke(input_data, config=config, stream_mode="updates")
            output = self.convert_response(result, context)
            return output
        except Exception as e:
            self.logger.error(f"Error during agent run: {e}")
            raise e

    async def agent_run_astream(self, input_data: dict, context: AgentRunContext):
        """
        Run the agent with streaming response.

        Args:
            request_body (CreateResponse): The request body to run the agent with.

        Returns:
            StreamingResponse: The streaming response of the agent run.
        """
        try:
            self.logger.info(f"Starting streaming agent run {context.response_id}")
            config = self.create_runnable_config(context)
            stream = self.graph.astream(input=input_data, config=config, stream_mode="messages")
            response_converter = LangGraphStreamResponseConverter(stream, context, self.logger)
            async for result in response_converter.convert():
                yield result
        except Exception as e:
            self.logger.error(f"Error during streaming agent run: {e}")
            raise e

    def convert_request(self, request_body: CreateResponse) -> dict:
        """
        Convert the CreateResponse to a format suitable for the LangGraph graph.

        Args:
            request_body (CreateResponse): The request body to convert.

        Returns:
            dict: The converted request body.
            dict: The run context.
        """
        converter = LangGraphRequestConverter(request_body, self.logger)
        return converter.convert()

    def convert_response(self, response: dict, context: AgentRunContext) -> Response:
        """
        Convert the response from the LangGraph graph to a format suitable for the FoundryCBAgent.

        Args:
            response (dict): The response from the LangGraph graph.

        Returns:
            dict: The converted response.
        """
        converter = LangGraphResponseConverter(context, response, self.logger)
        output = converter.convert()

        agent_id = context.get_agent_id_object()
        conversation = context.get_conversation_object()
        response = Response(
            object="response",
            id=context.response_id,
            agent=agent_id,
            conversation=conversation,
            metadata=context.request.metadata,
            created_at=int(time.time()),
            output=output,
        )
        return response

    def create_runnable_config(self, context: AgentRunContext) -> RunnableConfig:
        """
        Create a RunnableConfig from the converted request data.
        """
        return RunnableConfig(
            configurable={
                "thread_id": context.conversation_id,
            },
        )

    def format_otlp_endpoint(self, endpoint: str) -> str:
        m = re.match(r"^(https?://[^/]+)", endpoint)
        if m:
            return f"{m.group(1)}/v1/traces"
        return endpoint
