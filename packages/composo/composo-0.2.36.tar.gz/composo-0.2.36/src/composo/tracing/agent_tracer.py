import contextvars
import json
import uuid
from collections import OrderedDict
from functools import wraps
from typing import Callable, Dict, List, Optional, Union

from openai.types.chat.chat_completion import ChatCompletion
from opentelemetry import context, trace
from opentelemetry.context import Context
from opentelemetry.sdk.trace import SpanProcessor
from opentelemetry.trace import Span

from ..models.api_types import (
    AgentInstance,
    LLMInput,
    LLMInteraction,
    LLMOutput,
    LLMTool,
    MultiAgentTrace,
)

# Constants
INTERACTION_TYPE_LLM = "INTERACTION_TYPE_LLM_INTERACTION"
INTERACTION_TYPE_AGENT = "INTERACTION_TYPE_AGENT_INTERACTION"
INTERACTION_TYPE = "INTERACTION_TYPE"
AgentInstanceId = str


class AgentTracer:
    """Context manager for capturing and segmenting trace spans into agent instances"""

    _active_segmenter: contextvars.ContextVar[Optional["AgentTracer"]] = (
        contextvars.ContextVar("active_segmenter", default=None)
    )

    def __init__(self, name: Optional[str] = None, agent_id: Optional[str] = None):
        # Core identifiers
        self.agent_name = name or f"agent_{uuid.uuid4().hex[:8]}"
        self.agent_id = agent_id or str(uuid.uuid4())
        self.id = self.agent_id  # Alias for compatibility

        # Span tracking - use OrderedDict to merge spans dict and sequence list
        self.spans: OrderedDict[str, Span] = OrderedDict()

        # Hierarchy tracking
        self.parent_segmenter = self.get_active()
        self.child_segmenters: List["AgentTracer"] = []

        # Context management
        self._token = None
        self.current_span = None

    def __enter__(self):
        """Start the segmenter context"""
        self._token = self._active_segmenter.set(self)

        # Create agent span
        tracer = trace.get_tracer(__name__)
        self.current_span = tracer.start_as_current_span(
            name=f"agent-{self.agent_name}",
            context=context.get_current(),
            attributes={
                "agent.id": self.agent_id,
                INTERACTION_TYPE: INTERACTION_TYPE_AGENT,
            },
        ).__enter__()

        # Register with parent
        if self.parent_segmenter:
            self.parent_segmenter.add_span_details(self.current_span)
            self.parent_segmenter.child_segmenters.append(self)

        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """End the segmenter context"""
        if self.current_span:
            # Set attributes for debugging
            self.current_span.set_attribute(
                "segmenter.interaction_span_ids", json.dumps(list(self.spans.keys()))
            )
            self.current_span.set_attribute(
                "segmenter.interaction_count", len(self.spans)
            )
            self.current_span.set_attribute("segmenter.agent_id", self.agent_id)
            self.current_span.set_attribute("segmenter.agent_name", self.agent_name)
            self.current_span.__exit__(exc_type, exc_val, exc_tb)

        if self._token:
            self._active_segmenter.reset(self._token)

    def add_span_details(self, span: Span):
        """Store span details when span ends"""
        span_id = format(span.get_span_context().span_id, "032x")
        # OrderedDict automatically maintains insertion order
        self.spans[span_id] = span

    def get_raw_spans(self) -> List[Span]:
        """Get the raw spans captured during this segmenter's lifetime"""
        return list(self.spans.values())

    def _parse_openai_span(self, span: Span) -> Optional[LLMInteraction]:
        """Parse OpenAI span into LLMInteraction"""
        input_messages, output_messages, tools = [], [], []

        try:
            # Parse input
            input_value = span.attributes.get("input.value")
            print(input_value)
            if input_value and input_value not in (None, "null", ""):
                input_data = json.loads(input_value)

                # Extract messages
                for message in input_data.get("messages", []):
                    role = message.get("role", "unknown")
                    content = message.get("content")

                    # Handle different message types
                    if (
                        role == "assistant"
                        and content is None
                        and "tool_calls" in message
                    ):
                        # Assistant message with tool calls - use tool call information as content
                        tool_calls = message.get("tool_calls", [])
                        if tool_calls:
                            # Create a description of the tool calls
                            tool_descriptions = []
                            for tool_call in tool_calls:
                                func_name = tool_call.get("function", {}).get(
                                    "name", "unknown"
                                )
                                func_args = tool_call.get("function", {}).get(
                                    "arguments", "{}"
                                )
                                tool_descriptions.append(
                                    f"Tool call: {func_name}({func_args})"
                                )
                            content = "; ".join(tool_descriptions)
                        else:
                            content = ""
                    elif role == "tool":
                        # Tool response message - content should contain the tool response
                        content = content or ""
                    elif content is None:
                        # Other messages with None content
                        content = ""

                    input_messages.append(
                        LLMInput(
                            role=role,
                            content=content,
                            type="text",
                        )
                    )
                print("input_messages", input_messages)
                # Extract tools
                for tool in input_data.get("tools", []):
                    if isinstance(tool, dict) and "function" in tool:
                        func = tool["function"]
                        tools.append(
                            LLMTool(
                                name=func.get("name", "unknown"),
                                description=func.get("description", ""),
                                parameters=json.dumps(func.get("parameters", {})),
                            )
                        )

            # Parse output
            output_value = span.attributes.get("output.value")
            if output_value and output_value not in (None, "null", ""):
                output_data = json.loads(output_value)
                chat_completion = ChatCompletion.model_validate(output_data)

                for choice in chat_completion.choices:
                    if choice.message:
                        # Regular content
                        if choice.message.content:
                            output_messages.append(
                                LLMOutput(content=choice.message.content, type="text")
                            )

                        # Tool calls
                        if choice.message.tool_calls:
                            for tool_call in choice.message.tool_calls:
                                output_messages.append(
                                    LLMOutput(
                                        content=f"Tool call: {tool_call.function.name}({tool_call.function.arguments})",
                                        type="tool_call",
                                    )
                                )

        except Exception as e:
            print(f"Error parsing OpenAI data: {e}")
            return None

        return LLMInteraction(
            input_messages=input_messages,
            output_messages=output_messages,
            tools=tools or None,
        )

    def get_agent_instance(self) -> AgentInstance:
        """Build agent instance from captured spans"""
        interactions: List[Union[LLMInteraction, AgentInstanceId]] = []

        # Use OrderedDict keys() to iterate in insertion order
        for span_id in self.spans.keys():
            span = self.spans[span_id]
            interaction_type = span.attributes.get(INTERACTION_TYPE, "unknown")

            if interaction_type == INTERACTION_TYPE_LLM:
                # Handle LLM interaction
                if span.attributes.get("llm.provider") in ["openai", "azure"]:
                    llm_interaction = self._parse_openai_span(span)
                    if llm_interaction:
                        interactions.append(llm_interaction)
            elif interaction_type == INTERACTION_TYPE_AGENT:
                # Handle child agent
                agent_id = span.attributes.get("agent.id", "unknown")
                interactions.append(agent_id)

        return AgentInstance(
            id=self.agent_id, name=self.agent_name, interactions=interactions
        )

    def get_multi_agent_trace(self) -> MultiAgentTrace:
        """Create multi-agent trace with all agent instances"""
        agent_instances = {}

        def collect_instances(segmenter: "AgentTracer"):
            instance = segmenter.get_agent_instance()
            agent_instances[instance.id] = instance
            for child in segmenter.child_segmenters:
                collect_instances(child)

        collect_instances(self)

        return MultiAgentTrace(
            root_agent_instance_id=self.agent_id,
            agent_instance_by_id=agent_instances,
        )

    @property
    def trace(self) -> MultiAgentTrace:
        """Property to get multi-agent trace - convenience wrapper for get_multi_agent_trace()"""
        return self.get_multi_agent_trace()

    @classmethod
    def get_active(cls) -> Optional["AgentTracer"]:
        """Get the currently active segmenter"""
        return cls._active_segmenter.get()


def agent_tracer(name: Optional[str] = None) -> Callable:
    """Decorator to wrap a function with an AgentTracer context.

    Usage:
        @agent_tracer(name="my_agent")
        def my_function():
            # function code here
            pass

    Args:
        name: Optional name for the agent. If not provided, uses function name.

    Returns:
        Decorated function that runs within an AgentTracer context.
    """

    def decorator(func: Callable) -> Callable:
        agent_name = name or func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            with AgentTracer(name=agent_name):
                return func(*args, **kwargs)

        return wrapper

    return decorator


class GlobalSpanProcessor(SpanProcessor):
    """Span processor that captures spans for active AgentTracer instances"""

    def on_start(self, span: Span, parent_context: Optional[Context] = None):
        """Mark LLM spans when started"""
        active = AgentTracer.get_active()
        if active and self._is_openai_llm_span(span):
            span.set_attribute(INTERACTION_TYPE, INTERACTION_TYPE_LLM)

    def on_end(self, span: Span):
        """Capture LLM spans when ended"""
        active = AgentTracer.get_active()
        if active and span.attributes.get(INTERACTION_TYPE) == INTERACTION_TYPE_LLM:
            active.add_span_details(span)

    def force_flush(self, timeout_millis: int = 30000) -> bool:
        return True

    @staticmethod
    def _is_openai_llm_span(span: Span) -> bool:
        """Check if this is an OpenAI LLM span captured by OpenInference"""
        if not span.attributes:
            return False

        attrs = span.attributes
        return (
            attrs.get("openinference.span.kind") == "LLM"
            and attrs.get("llm.system") == "openai"
        )
