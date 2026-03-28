---
name: s-exa
description: >-
  Web search, code context lookup, and URL crawling via Exa AI. Use when you need current information, news, facts, answers to general questions, programming help (API usage, library examples, code snippets, debugging), or the full text of a specific URL. Triggers include requests like "search for", "find recent", "what's the latest on", "how do I use", "show me examples of", "look up", "get the content from this URL", or any question requiring up-to-date web or code information. Do NOT use for local file operations, git commands, code editing, or tasks that don't require external web content.
allowed-tools: Bash(python3 $SKILL_DIR/scripts/exa.py *)
---

Search the web or find code context using the local Exa script. Run:

```
python3 $SKILL_DIR/scripts/exa.py <command> "$ARGUMENTS"
```

## Commands

### `web-search` — Search the web

```
python3 $SKILL_DIR/scripts/exa.py web-search <query> [options]
```

| Option | Description |
|--------|-------------|
| `<query>` | Websearch query |
| `--num-results <n>` | Number of search results to return (must be a number, default: 8) |
| `--livecrawl <mode>` | `fallback`: use live crawling as backup if cached content unavailable, `preferred`: prioritize live crawling (default: `fallback`) |
| `--type <type>` | `auto`: balanced search (default), `fast`: quick results |
| `--category <cat>` | Filter results to a specific category — `company`: company websites and profiles, `research paper`: academic papers and research, `people`: LinkedIn profiles and personal bios |
| `--max-chars <n>` | Maximum characters for context string optimized for LLMs (must be a number, default: 10000) |

### `code-context` — Find code examples and documentation

```
python3 $SKILL_DIR/scripts/exa.py code-context <query> [options]
```

| Option | Description |
|--------|-------------|
| `<query>` | Search query to find relevant context for APIs, Libraries, and SDKs. For example, 'React useState hook examples', 'Python pandas dataframe filtering', 'Express.js middleware', 'Next js partial prerendering configuration' |
| `--tokens <n>` | Number of tokens to return (must be a number, 1000–50000). Default is 5000 tokens. Adjust based on how much context you need — use lower values for focused queries and higher values for comprehensive documentation. |

### `crawl` — Fetch full content from a URL

```
python3 $SKILL_DIR/scripts/exa.py crawl <url> [options]
```

| Option | Description |
|--------|-------------|
| `<url>` | URL to crawl and extract content from |
| `--max-chars <n>` | Maximum characters to extract (must be a number, default: 3000) |

## Examples

```bash
# Web search
python3 $SKILL_DIR/scripts/exa.py web-search "Next.js 15 release notes" --livecrawl preferred
python3 $SKILL_DIR/scripts/exa.py web-search "transformer attention mechanism" --category "research paper"

# Code context
python3 $SKILL_DIR/scripts/exa.py code-context "React useState hook examples"
python3 $SKILL_DIR/scripts/exa.py code-context "Python pandas dataframe filtering" --tokens 10000

# Crawl a specific URL
python3 $SKILL_DIR/scripts/exa.py crawl "https://docs.anthropic.com/en/api/getting-started" --max-chars 5000
```
