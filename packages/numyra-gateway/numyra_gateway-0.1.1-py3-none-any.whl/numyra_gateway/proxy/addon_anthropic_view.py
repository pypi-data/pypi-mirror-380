from mitmproxy.http import HTTPFlow
from mitmproxy.contentviews import base, Metadata
from mitmproxy import contentviews
from typing import Optional, Tuple

from numyra_gateway.streaming import AnthropicStreamParser, AnthropicMessage


class AnthropicView(contentviews.Contentview):

    @property
    def name(self) -> str:
        return "Numyra Anthropic View"

    def prettify(self, data: bytes, metadata: Metadata) -> str:
        flow = metadata.flow

        if not flow:
            return 'No flow'
        if not isinstance(flow, HTTPFlow):
            return 'Not HTTPFlow'

        message, content = _process_flow(flow)

        if message is None:
            if not _validate_flow(flow):
                return 'Not SSE'
            return f"Could not decode SSE content"

        if message:
            str_repr = _format_anthropic_message(message)
        else:
            str_repr = f"No message received with content `{content}`"

        flow.comment = str_repr
        return str_repr

    def render_priority(self, data: bytes, metadata: Metadata) -> float:
        flow = metadata.flow
        message, _ = _process_flow(flow)

        # Highest priority if we successfully parsed an Anthropic message
        return 1.0 if message else 0.0


def _validate_flow(flow) -> bool:
    """Validate that flow is a valid HTTPFlow with SSE content"""
    if not flow or not isinstance(flow, HTTPFlow) or not flow.response or not flow.response.headers:
        return False

    content_type = flow.response.headers.get("content-type", "")
    return "text/event-stream" in content_type


def _decode_content(flow: HTTPFlow) -> Optional[str]:
    """Safely decode flow response content"""
    try:
        return flow.response.content.decode('utf-8')
    except Exception as e:
        print(f"   ⚠️  Could not decode SSE content: {e}")
        return None


def _parse_anthropic_message(content: str) -> Optional[AnthropicMessage]:
    """Parse content and return AnthropicMessage if valid"""
    try:
        parser = AnthropicStreamParser()
        return parser.feed(content)
    except Exception:
        return None


def _process_flow(flow) -> Tuple[Optional[AnthropicMessage], Optional[str]]:
    """Process flow and return (message, content)"""
    if not _validate_flow(flow):
        return None, None

    content = _decode_content(flow)
    if content is None:
        return None, None

    message = _parse_anthropic_message(content)
    return message, content


def _format_content_block(i: int, content: str, is_tool_use: bool) -> list[str]:
    """Format a single content block"""
    import json

    if is_tool_use:
        try:
            parsed_json = json.loads(content)
            pretty_json = json.dumps(parsed_json, indent=2)
            lines = [f"💬 Content block {i}:"]
            for line in pretty_json.split('\n'):
                lines.append(f"   {line}")
            return lines
        except json.JSONDecodeError:
            pass

    return [f"💬 Content block {i}: {repr(content)}"]


def _format_anthropic_message(message: AnthropicMessage) -> str:
    """Format AnthropicMessage into a nice readable string"""
    lines = []

    # Stop reason first
    if message.stop_reason:
        lines.append(f"🎯 Stop Reason: {message.stop_reason}")

    # Content blocks
    if message.content_blocks:
        is_tool_use = message.stop_reason == "tool_use"
        for i, content in message.content_blocks.items():
            lines.extend(_format_content_block(i, content, is_tool_use))
    else:
        lines.append("💬 Content: (no content)")

    # Metadata at the bottom
    lines.append("")
    lines.append(f"📧 Message ID: {message.id or 'N/A'}")
    lines.append(f"🤖 Model: {message.model or 'N/A'}")
    lines.append(f"👤 Role: {message.role or 'N/A'}")
    lines.append(f"✅ Complete: {message.is_complete}")

    if message.usage:
        usage = message.usage
        input_tokens = usage.get('input_tokens', 'N/A')
        output_tokens = usage.get('output_tokens', 'N/A')
        lines.append(f"📊 Token Usage: {input_tokens} in / {output_tokens} out")

    return "\n".join(lines)


class RegisterAnthropicView:
    def load(self, loader):
        contentviews.add(AnthropicView())
