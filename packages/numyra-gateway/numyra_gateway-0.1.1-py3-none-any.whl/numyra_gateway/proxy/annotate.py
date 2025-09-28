import random

from mitmproxy import http, ctx

class Annotate:
    def response(self, flow: http.HTTPFlow):
        if not flow.response:
            return
        dur = flow.response.timestamp_end - flow.request.timestamp_start
        size = len(flow.response.content or b"")
        info = f"{dur*1000:.1f} ms, {size} B"

        flow.comment = info                    # visible as a comment bubble
        # flow.response.headers["X-Traffic-Info"] = info  # visible in Headers
        # if random.choice([True, False]) :
        #     flow.marked = 'yes' # True                 # highlight slow flows
        # ctx.log.info(f"{flow.request.method} {flow.request.url} -> {info}")


