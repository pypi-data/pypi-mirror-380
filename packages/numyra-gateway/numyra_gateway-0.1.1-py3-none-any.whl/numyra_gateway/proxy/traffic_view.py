from mitmproxy.contentviews import base, Metadata
from mitmproxy import contentviews
from mitmproxy.http import HTTPFlow

from numyra_gateway.streaming import AnthropicStreamParser


class MyTrafficView(contentviews.Contentview):
    name = "My Traffic Info"

    # def render_priority(self, data: bytes, metadata: Metadata, ):
    #     return 0

    def prettify(self, data: bytes, metadata: Metadata)->str:
        flow = metadata.flow
        if not flow:
            return 'No flow'
        if not isinstance(flow, HTTPFlow):
            return 'Not HTTPFlow'

        content_type = flow.response.headers.get("content-type", "")

        if "text/event-stream" not in content_type:
            return 'Not SSE'

        try:
            content = flow.response.content.decode('utf-8')
        except Exception as e:
            print(f"   ⚠️  Could not decode SSE content: {e}")
            print(f"   Raw bytes: {len(flow.response.content)} bytes")
            # mark with some icon for error or similar
            flow.marked = ":warning:"
            flow.comment = f"Could not decode SSE content `{e}`"
            return str(e)

        flow.marked = ":zap:"

        parser = AnthropicStreamParser()
        message = parser.feed(content)

        str_repr = str(message) if message else f"No message received with content `{content}`"
        flow.comment = str_repr
        return str_repr


class RegisterView:
    def load(self, loader):
        contentviews.add(MyTrafficView())
