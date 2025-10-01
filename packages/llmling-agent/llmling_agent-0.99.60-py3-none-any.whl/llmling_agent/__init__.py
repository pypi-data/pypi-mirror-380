"""Agent configuration and creation."""

from llmling_agent.models import AgentsManifest, AgentConfig
from llmling_agent.agent import Agent, StructuredAgent, AnyAgent, AgentContext
from importlib.metadata import version as _metadata_version

from llmling_agent.delegation import AgentPool, Team, TeamRun, BaseTeam
from dotenv import load_dotenv
from llmling_agent.messaging.messages import ChatMessage
from llmling_agent.tools import Tool, ToolCallInfo
from llmling_agent.messaging.messagenode import MessageNode
from llmling_agent.models.content import (
    PDFURLContent,
    PDFBase64Content,
    ImageBase64Content,
    ImageURLContent,
    AudioURLContent,
    AudioBase64Content,
    VideoURLContent,
)

__version__ = _metadata_version("llmling-agent")

load_dotenv()

__all__ = [
    "Agent",
    "AgentConfig",
    "AgentContext",
    "AgentPool",
    "AgentsManifest",
    "AnyAgent",
    "AudioBase64Content",
    "AudioURLContent",
    "BaseTeam",
    "ChatMessage",
    "ImageBase64Content",
    "ImageURLContent",
    "MessageNode",
    "PDFBase64Content",
    "PDFURLContent",
    "StructuredAgent",
    "Team",
    "TeamRun",
    "Tool",
    "ToolCallInfo",
    "VideoURLContent",
]
