import json
from datetime import datetime

import mitmproxy
from mitmproxy.http import HTTPFlow


class SSEInterceptor:
    def __init__(self):
        self.sse_count = 0


    def response(self, flow: HTTPFlow) -> None:
        # Check if this is an SSE response
        content_type = flow.response.headers.get("content-type", "")

        if "text/event-stream" not in content_type:
            return
        flow.marked = ":zap:"
        self.sse_count += 1
        print(f"\n📡 [SSE RESPONSE #{self.sse_count}] {datetime.now().strftime('%H:%M:%S')}")
        # print(f"   URL: {flow.request.pretty_url}")
        # print(f"   Status: {flow.response.status_code}")
        # print(f"   Content-Type: {content_type}")

        # Print relevant response headers
        # headers_of_interest = ["cache-control", "connection", "transfer-encoding"]
        # for header in headers_of_interest:
        #     if header in flow.response.headers:
        #         print(f"   {header.title()}: {flow.response.headers[header]}")

        # Print SSE data
        if flow.response.content:
            try:
                content = flow.response.content.decode('utf-8')
                print(f"   📋 SSE Data:")
                self._parse_and_print_sse_data(content)
            except Exception as e:
                print(f"   ⚠️  Could not decode SSE content: {e}")
                print(f"   Raw bytes: {len(flow.response.content)} bytes")


    def _parse_and_print_sse_data(self, content):
        """Parse and pretty-print SSE data"""
        lines = content.split('\n')
        current_event = {}

        for line in lines:
            line = line.strip()
            if not line:
                # Empty line indicates end of event
                if current_event:
                    self._print_sse_event(current_event)
                    current_event = {}
                continue

            if line.startswith('data: '):
                data = line[6:]  # Remove 'data: ' prefix
                if 'data' not in current_event:
                    current_event['data'] = []
                current_event['data'].append(data)
            elif line.startswith('event: '):
                current_event['event'] = line[7:]  # Remove 'event: ' prefix
            elif line.startswith('id: '):
                current_event['id'] = line[4:]  # Remove 'id: ' prefix
            elif line.startswith('retry: '):
                current_event['retry'] = line[7:]  # Remove 'retry: ' prefix
            elif line.startswith(': '):
                # Comment line
                if 'comments' not in current_event:
                    current_event['comments'] = []
                current_event['comments'].append(line[2:])

        # Print last event if there's no trailing empty line
        if current_event:
            self._print_sse_event(current_event)

    def _print_sse_event(self, event):
        """Pretty print a single SSE event"""
        print(f"      🔹 Event:")

        if 'event' in event:
            print(f"         Type: {event['event']}")
        if 'id' in event:
            print(f"         ID: {event['id']}")
        if 'retry' in event:
            print(f"         Retry: {event['retry']}ms")

        if 'data' in event:
            for i, data_line in enumerate(event['data']):
                # Try to parse as JSON for pretty printing
                try:
                    parsed_json = json.loads(data_line)
                    print(f"         Data[{i}]: {json.dumps(parsed_json, indent=12)[12:]}")  # Indent to align
                except:
                    # Not JSON, print as-is but truncate if too long
                    display_data = data_line[:150] + "..." if len(data_line) > 150 else data_line
                    print(f"         Data[{i}]: {display_data}")

        if 'comments' in event:
            for comment in event['comments']:
                print(f"         Comment: {comment}")


