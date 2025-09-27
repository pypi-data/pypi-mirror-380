import inspect
import json
import os
from abc import abstractmethod
from typing import Any, AsyncGenerator, Generator, Union

import uvicorn
from opentelemetry import context as otel_context, trace
from opentelemetry.trace.propagation.tracecontext import TraceContextTextMapPropagator
from starlette.applications import Starlette
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse, Response, StreamingResponse
from starlette.routing import Route

from .. import models
from ..constants import Constants
from ..logger import get_logger
from ..models.openai.models import (
    CreateResponse,
    ImplicitUserMessage,
    ItemContent,
    ItemParam,
    ItemType,
    Response as OpenAIResponse,
    ResponseStreamEvent,
)
from .common.agent_run_context import AgentRunContext
from .common.id_generator.foundry_id_generator import FoundryIdGenerator

logger = get_logger()


class FoundryCBAgent:
    def __init__(self):
        async def runs_endpoint(request):
            payload = await request.json()
            try:
                request_body = _deserialize_create_response(payload)

                id_generator = FoundryIdGenerator.from_request(request_body)
                context = AgentRunContext(
                    request_body, id_generator, id_generator.response_id, id_generator.conversation_id
                )
            except Exception as e:  # noqa: BLE001
                logger.exception("Invalid request body for /runs")
                return JSONResponse({"error": str(e)}, status_code=400)

            with self.tracer.start_as_current_span(
                name=f"ContainerAgentsAdapter-{context.response_id}",
                attributes=self.get_span_attributes(request_body, context),
                kind=trace.SpanKind.SERVER,
            ):
                context_carrier = {}
                TraceContextTextMapPropagator().inject(context_carrier)

                resp = await self.agent_run(request_body, context)

                if inspect.isgenerator(resp):

                    def gen():
                        ctx = TraceContextTextMapPropagator().extract(carrier=context_carrier)
                        token = otel_context.attach(ctx)
                        try:
                            for event in resp:
                                yield _event_to_sse_chunk(event)
                        finally:
                            otel_context.detach(token)

                    return StreamingResponse(gen(), media_type="text/event-stream")
                if inspect.isasyncgen(resp):

                    async def gen():
                        ctx = TraceContextTextMapPropagator().extract(carrier=context_carrier)
                        token = otel_context.attach(ctx)
                        try:
                            async for event in resp:
                                yield _event_to_sse_chunk(event)
                        finally:
                            otel_context.detach(token)

                    return StreamingResponse(gen(), media_type="text/event-stream")
                return JSONResponse(resp.as_dict())

        async def liveness_endpoint(request):
            result = await self.agent_liveness(request)
            return _to_response(result)

        async def readiness_endpoint(request):
            result = await self.agent_readiness(request)
            return _to_response(result)

        routes = [
            Route("/runs", runs_endpoint, methods=["POST"], name="agent_run"),
            Route("/responses", runs_endpoint, methods=["POST"], name="agent_response"),
            Route("/liveness", liveness_endpoint, methods=["GET"], name="agent_liveness"),
            Route("/readiness", readiness_endpoint, methods=["GET"], name="agent_readiness"),
        ]

        self.app = Starlette(routes=routes)
        self.app.add_middleware(
            CORSMiddleware,
            allow_origins=["*"],
            allow_credentials=True,
            allow_methods=["*"],
            allow_headers=["*"],
        )
        self.tracer = None

    @abstractmethod
    async def agent_run(
        self, request_body: CreateResponse, context: AgentRunContext
    ) -> Union[OpenAIResponse, Generator[ResponseStreamEvent, Any, Any], AsyncGenerator[ResponseStreamEvent, Any]]:
        raise NotImplementedError

    async def agent_liveness(self, request) -> Union[Response, dict]:
        return Response(status_code=200)

    async def agent_readiness(self, request) -> Union[Response, dict]:
        return {"status": "ready"}

    async def run_async(
        self,
        port: int = int(os.environ.get("DEFAULT_AD_PORT", 8088)),
    ) -> None:
        """
        Awaitable server starter for use **inside** an existing event loop.
        """
        self.init_tracing()
        config = uvicorn.Config(self.app, host="0.0.0.0", port=port, loop="asyncio")
        server = uvicorn.Server(config)
        logger.info(f"Starting FoundryCBAgent server async on port {port}")
        await server.serve()

    def run(self, port: int = int(os.environ.get("DEFAULT_AD_PORT", 8088))) -> None:
        """
        Start a Starlette server on localhost:<port> exposing:
          POST  /runs
          GET   /liveness
          GET   /readiness
        """
        self.init_tracing()
        logger.info(f"Starting FoundryCBAgent server on port {port}")
        uvicorn.run(self.app, host="0.0.0.0", port=port)

    def init_tracing(self):
        exporter = os.environ.get(Constants.OTEL_EXPORTER_ENDPOINT)
        app_insights_conn_str = os.environ.get(Constants.APPLICATION_INSIGHTS_CONNECTION_STRING)
        if exporter or app_insights_conn_str:
            from opentelemetry.sdk.resources import Resource
            from opentelemetry.sdk.trace import TracerProvider

            resource = Resource.create(self.get_trace_attributes())
            provider = TracerProvider(resource=resource)
            if exporter:
                self.setup_otlp_exporter(exporter, provider)
            if app_insights_conn_str:
                self.setup_application_insights_exporter(app_insights_conn_str, provider)
            trace.set_tracer_provider(provider)
            self.init_tracing_internal()
        self.tracer = trace.get_tracer(__name__)

    def get_trace_attributes(self):
        return {
            "service.name": "azure.ai.agentshosting",
        }

    def get_span_attributes(self, request_body: CreateResponse, context: AgentRunContext):
        return {
            "azure.ai.agentshosting.responses.response_id": context.response_id or "",
            "azure.ai.agentshosting.responses.conversation_id": context.conversation_id or "",
            "azure.ai.agentshosting.responses.streaming": str(request_body.stream or False),
        }

    def init_tracing_internal(self):
        pass

    def setup_application_insights_exporter(self, connection_string, provider):
        from azure.monitor.opentelemetry.exporter import AzureMonitorTraceExporter
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        exporter_instance = AzureMonitorTraceExporter.from_connection_string(connection_string)
        processor = BatchSpanProcessor(exporter_instance)
        provider.add_span_processor(processor)
        logger.info("Tracing setup with Application Insights exporter.")

    def setup_otlp_exporter(self, endpoint, provider):
        from opentelemetry.exporter.otlp.proto.http.trace_exporter import OTLPSpanExporter
        from opentelemetry.sdk.trace.export import BatchSpanProcessor

        exporter_instance = OTLPSpanExporter(endpoint=endpoint)
        processor = BatchSpanProcessor(exporter_instance)
        provider.add_span_processor(processor)
        logger.info(f"Tracing setup with OTLP exporter: {endpoint}")


def _deserialize_create_response(payload: dict) -> CreateResponse:
    _deserialized = CreateResponse._deserialize(payload, [])

    raw_input = payload.get("input")
    if raw_input:
        if isinstance(raw_input, str):
            user_message = {"content": raw_input}  # force convert to ImplicitUserMessage
            _deserialized.input = [_deserialize_implicit_user_message(user_message)]
        elif isinstance(raw_input, list):
            _deserialized_input = []
            for input in raw_input:
                if isinstance(input, dict):
                    if "role" in input:
                        _deserialized_input.append(_deserialize_message_item_param(input))
                    elif "type" in input:
                        _deserialized_input.append(ItemParam._deserialize(input, []))
                    else:
                        _deserialized_input.append(_deserialize_implicit_user_message(input))
                else:
                    logger.warning(f"Unexpected input type in 'input' list: {type(input).__name__}")
            _deserialized.input = _deserialized_input

    raw_agent_reference = payload.get("agent")
    if raw_agent_reference:
        _deserialized.agent = _deserialize_agent_reference(raw_agent_reference)
    return _deserialized


def _event_to_sse_chunk(event: ResponseStreamEvent) -> str:
    event_data = json.dumps(event.as_dict())
    if event.type:
        return f"event: {event.type}\ndata: {event_data}\n\n"
    return f"data: {event_data}\n\n"


def _to_response(result: Union[Response, dict]) -> Response:
    return result if isinstance(result, Response) else JSONResponse(result)


def _deserialize_implicit_user_message(payload: dict) -> ImplicitUserMessage:
    _deserialized = ImplicitUserMessage._deserialize(payload, [])
    input_content = payload.get("content")
    if isinstance(input_content, list):
        _deserialized.content = _deserialize_item_content_list(input_content)
    elif not isinstance(input_content, str):  # string input, do nothing
        logger.warning(f"Unexpected content type in ImplicitUserMessage: {type(input_content)}")
    return _deserialized


def _deserialize_message_item_param(payload: dict) -> ItemParam:
    """Deserialize a input with role into an ResponsesMessageItemParam."""
    if "type" not in payload:
        payload["type"] = ItemType.MESSAGE
    _deserialized = ItemParam._deserialize(payload, [])
    input_content = payload.get("content")
    if isinstance(input_content, list):
        _deserialized.content = _deserialize_item_content_list(input_content)
    elif not isinstance(input_content, str):  # string input, do nothing
        logger.warning(f"Unexpected content type in ResponsesMessageItemParam: {type(input_content)}")
    return _deserialized


def _deserialize_item_content_list(payload: list) -> list[ItemContent]:
    _deserialized_list = []
    for item in payload:
        if isinstance(item, dict):
            _deserialized_list.append(ItemContent._deserialize(item, []))
        else:
            logger.warning(f"Unexpected item type in ItemContent list: {type(item).__name__}")
    return _deserialized_list


def _deserialize_agent_reference(payload: dict) -> models.AgentReference:
    if not payload:
        return None
    return models.AgentReference._deserialize(payload, [])
