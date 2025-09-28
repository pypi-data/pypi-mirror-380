from mitmproxy.http import HTTPFlow

from numyra_gateway.streaming import AnthropicStreamParser


class AddonAnthropicSSEMarker:

    def response(self, flow: HTTPFlow) -> None:
        content_type = flow.response.headers.get("content-type", "")

        if "text/event-stream" not in content_type:
            return

        try:
            content = flow.response.content.decode('utf-8')
        except Exception as e:
            print(f"   ⚠️  Could not decode SSE content: {e}")
            print(f"   Raw bytes: {len(flow.response.content)} bytes")
            # mark with some icon for error or similar
            flow.marked = ":warning:"
            flow.comment = f"Could not decode SSE content `{e}`"
            return

        # flow.marked = ":zap:"

        parser = AnthropicStreamParser()
        message = parser.feed(content)

        if not message:
            flow.marked = ":warning:"
            flow.comment = f"Could not parse SSE message from content `{content}`"
            return

        if not message.stop_reason:
            flow.marked = ":warning:"
            flow.comment = f"No stop reason in SSE message `{message}`"
            return

        flow.marked = ":hammer_and_wrench:" if message.stop_reason == 'tool_use' else ":speech_balloon:"
        flow.comment = str(message)

