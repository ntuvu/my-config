#!/usr/bin/env python3
"""exa — Search the web or find code context using Exa AI."""

import argparse
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path


def load_env():
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        for line in env_file.read_text().splitlines():
            if line.strip() and not line.startswith("#") and "=" in line:
                k, _, v = line.partition("=")
                os.environ.setdefault(k.strip(), v.strip())


def api_post(endpoint, payload, api_key, integration):
    req = urllib.request.Request(
        f"https://api.exa.ai/{endpoint}",
        data=json.dumps(payload).encode(),
        headers={
            "accept": "application/json",
            "content-type": "application/json",
            "x-api-key": api_key,
            "x-exa-integration": integration,
        },
    )
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            return json.loads(resp.read())
    except urllib.error.HTTPError as e:
        sys.exit(f"error: Exa API returned HTTP {e.code}")
    except urllib.error.URLError as e:
        sys.exit(f"error: request to Exa API failed ({e.reason})")


def web_search(args, api_key):
    payload = {
        "query": " ".join(args.query),
        "type": args.type,
        "numResults": args.num_results,
        "contents": {
            "text": True,
            "context": {"maxCharacters": args.max_chars},
            "livecrawl": args.livecrawl,
        },
    }
    if args.category:
        payload["category"] = args.category

    data = api_post("search", payload, api_key, "web-search-bash")
    contexts = [r["context"] for r in data.get("results", []) if r.get("context")]
    if not contexts:
        sys.exit("No search results found. Please try a different query.")
    print("\n\n".join(contexts))


def code_context(args, api_key):
    if not 1000 <= args.tokens <= 50000:
        sys.exit("error: tokens must be between 1000 and 50000")

    data = api_post(
        "context",
        {"query": " ".join(args.query), "tokensNum": args.tokens},
        api_key,
        "exa-code-bash",
    )
    content = data.get("response", "")
    if not content:
        sys.exit("No code snippets or documentation found. Please try a different query.")
    print(content)


def crawl(args, api_key):
    data = api_post(
        "contents",
        {
            "ids": [args.url],
            "contents": {
                "text": {"maxCharacters": args.max_chars},
                "livecrawl": "preferred",
            },
        },
        api_key,
        "crawling-mcp",
    )
    results = data.get("results", [])
    if not results or not results[0].get("text"):
        sys.exit("No content found for the provided URL.")
    r = results[0]
    print(f"Title: {r.get('title', '')}\nURL: {r.get('url', '')}\n\n{r['text']}")


def main():
    load_env()
    api_key = os.environ.get("EXA_API_KEY", "")
    if not api_key:
        sys.exit("error: EXA_API_KEY is not set")

    p = argparse.ArgumentParser(prog="exa")
    sub = p.add_subparsers(dest="cmd", required=True)

    ws = sub.add_parser("web-search")
    ws.add_argument("query", nargs="+")
    ws.add_argument("--num-results", type=int, default=8)
    ws.add_argument("--livecrawl", default="fallback", choices=["fallback", "preferred"])
    ws.add_argument("--type", default="auto", choices=["auto", "fast"])
    ws.add_argument("--category", default="")
    ws.add_argument("--max-chars", type=int, default=10000)

    cc = sub.add_parser("code-context")
    cc.add_argument("query", nargs="+")
    cc.add_argument("--tokens", type=int, default=5000)

    cr = sub.add_parser("crawl")
    cr.add_argument("url")
    cr.add_argument("--max-chars", type=int, default=3000)

    args = p.parse_args()
    {"web-search": web_search, "code-context": code_context, "crawl": crawl}[args.cmd](
        args, api_key
    )


if __name__ == "__main__":
    main()
