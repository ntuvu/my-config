alwaysApply: true
---

When you need library documentation, web search, GitHub code examples, or browser automation — delegate to the `codex` subagent instead of calling MCP tools directly.

## Covered tools (do NOT call these directly)

- `mcp__context7__resolve-library-id` / `mcp__context7__query-docs` — library docs
- `mcp__exa__web_search_exa` / `mcp__exa__get_code_context_exa` — web search
- `mcp__grep__searchGitHub` — GitHub code search

## When to delegate

- Library/framework docs, API references, setup questions → context7 via codex
- Current info, recent releases, time-sensitive facts → exa via codex
- Real-world GitHub code examples, syntax/usage patterns → grep via codex
- Browser automation or web scraping → playwright via codex

## How to delegate

Use the Task tool to invoke the `codex` agent with a specific, self-contained prompt for the research or tool task needed. Codex CLI handles all MCP calls internally.
