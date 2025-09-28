import json
from dataclasses import dataclass, field
from typing import Dict, List, Optional
from .sse_parser import SSEParser


@dataclass
class AnthropicMessage:
    id: Optional[str] = None
    model: Optional[str] = None
    role: Optional[str] = None
    content_blocks: Dict[int, str] = field(default_factory=dict)
    stop_reason: Optional[str] = None
    usage: Optional[dict] = None
    is_complete: bool = False

    @property
    def content(self) -> str:
        """Get the complete text content from all content blocks"""
        return "".join(self.content_blocks.get(i, "") for i in sorted(self.content_blocks.keys()))


class AnthropicStreamParser:
    def __init__(self):
        self.sse_parser = SSEParser()
        self.message = AnthropicMessage()

    def feed(self, chunk: str) -> Optional[AnthropicMessage]:
        """Feed a chunk of SSE data and return the current message state"""
        events = self.sse_parser.feed(chunk)

        for event in events:
            if event.data:
                try:
                    data = json.loads(event.data)
                    self._handle_event(data)
                except json.JSONDecodeError:
                    continue

        return self.message if self.message.id else None

    def _handle_event(self, data: dict):
        event_type = data.get("type")

        if event_type == "message_start":
            message_data = data.get("message", {})
            self.message.id = message_data.get("id")
            self.message.model = message_data.get("model")
            self.message.role = message_data.get("role")
            self.message.usage = message_data.get("usage")

        elif event_type == "content_block_start":
            index = data.get("index", 0)
            if index not in self.message.content_blocks:
                self.message.content_blocks[index] = ""

        elif event_type == "content_block_delta":
            index = data.get("index", 0)
            delta = data.get("delta", {})

            if delta.get("type") == "text_delta":
                text = delta.get("text", "")
                if index not in self.message.content_blocks:
                    self.message.content_blocks[index] = ""
                self.message.content_blocks[index] += text
            elif delta.get("type") == "input_json_delta":
                partial_json = delta.get("partial_json", "")
                if index not in self.message.content_blocks:
                    self.message.content_blocks[index] = ""
                self.message.content_blocks[index] += partial_json

        elif event_type == "message_delta":
            delta = data.get("delta", {})
            if "stop_reason" in delta:
                self.message.stop_reason = delta["stop_reason"]
            if "usage" in data:
                self.message.usage = data["usage"]

        elif event_type == "message_stop":
            self.message.is_complete = True