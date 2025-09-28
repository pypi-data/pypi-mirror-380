#!/usr/bin/env python3

import asyncio

from mitmproxy import options
from mitmproxy.tools.web.master import WebMaster


async def start_gateway():
    # Anthropic

    # combo0
    # export ANTHROPIC_BASE_URL="http://localhost:8080"
    target = "https://api.anthropic.com"

    # OpenAI

    # combo0
    # export OPENAI_BASE_URL="http://localhost:8080/v1"
    # target = "https://api.openai.com"
    # result: do not work with the bearer token but at least it gives 401 error; maybe it works with OPENAI_API_KEY

    # combo1
    # export OPENAI_BASE_URL="http://localhost:8080/backend-api/codex/responses"
    # target = "https://chatgpt.com"
    # result: didnt work, observed full url: `POST https://chatgpt.com/backend-api/codex/responses/responses HTTP/1.1`

    # combo2
    # export OPENAI_BASE_URL="http://localhost:8080/backend-api/codex"
    # target = "https://chatgpt.com"
    # result: WORKED with bearer token (auth web integrated with the account)

    print("Starting MITM Gateway...")
    print("Web interface will be available at: http://127.0.0.1:8081")
    print("Proxy listening on: http://127.0.0.1:8080")
    print(f"Reverse proxy target: {target}")
    print("Press Ctrl+C to stop")


    opts = options.Options(
        mode=[f"reverse:{target}"],
        listen_port=8080
    )
    master = WebMaster(opts)
    master.options.web_host = "127.0.0.1"
    master.options.web_port = 8081

    # import main_script
    # master.addons.add(main_script)
    # import annotate
    # master.addons.add(annotate)
    # import traffic_view
    # master.addons.add(traffic_view)
    from . import addon_list
    master.addons.add(addon_list)

    try:
        await master.run()
    except KeyboardInterrupt:
        print("\nShutting down gateway...")


def main():
    try:
        asyncio.run(start_gateway())
    except KeyboardInterrupt:
        print("\nShutting down gateway...")


if __name__ == "__main__":
    main()
