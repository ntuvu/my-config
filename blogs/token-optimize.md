### source: https://archive.ph/yti5R#selection-247.0-327.3

# You’re using Claude Code wrong. Here’s How To save 95% of tokens.

**By Simone Ruggiero** | Feb 1, 2026 | 5 min read

Let me tell you something most Claude Code users don’t realize: every time you ask Claude a question about your codebase, it’s probably reading 10x more code than it needs to.

I know because I was doing the same thing. For months.

### The problem nobody talks about
Claude Code is incredible. But it has a dirty secret: context gathering is expensive. When you ask “where is the auth middleware?”, here’s what actually happens behind the scenes:

1.  **Claude runs Glob** to list your files — tokens spent
2.  **Claude runs Grep** to search for keywords — more tokens spent
3.  **Claude reads 3–4 entire files** to find the right one — even more tokens
4.  **Claude finally reads the actual code** it needs — the only useful part

Steps 1–3 are pure waste. You’re paying for Claude to *find* information, not to *use* it. On a medium-sized codebase, 80–90% of your token budget goes to exploration, not actual coding.

I manage 20+ projects locally. My token usage was insane. I was hitting limits constantly, responses were slow, and half the context window was filled with code Claude didn’t even need.

Then I found **qmd**, and everything changed.

### What is qmd?
**qmd** is a local document indexer built specifically for AI agent workflows. You point it at your project directories, it indexes everything, and exposes the index as an MCP server that Claude Code can query directly.

Think of it as giving Claude a search engine for your codebase instead of making it read every file manually.

**Instead of:** *“Let me read all your files to find what you’re asking about”*
**Claude now does:** *“Let me search the index, get a 10-line snippet, and go straight to work”*

### The real numbers
I tracked my token usage across common workflows. The results were shocking.

#### Scenario 1 — Finding auth logic:
*   **Without qmd:** ~2,700 tokens
*   **With qmd:** ~250 tokens
*   **Saved: 91%**

#### Scenario 2 — Fixing a checkout bug:
*   **Without qmd:** ~3,950 tokens
*   **With qmd:** ~400 tokens
*   **Saved: 90%**

#### Scenario 3 — Understanding DB schema:
*   **Without qmd:** ~6,050 tokens
*   **With qmd:** ~400 tokens
*   **Saved: 93%**

**Average across all workflows: ~92% token reduction.**

---

### How to set it up (5 minutes)

#### Step 1: Install qmd
First, install Bun if you don’t have it:
`curl -fsSL https://bun.sh/install | bash`

Then install qmd:
`bun install -g https://github.com/tobi/qmd`

#### Step 2: Index your projects
For each project you work on:
`qmd collection add ./my-project --name myproject`

Customize file patterns if needed:
`qmd collection add ./my-project --name myproject --mask "**/*.{ts,tsx,md,json}"`

Generate vector embeddings for semantic search:
`qmd embed`

#### Step 3: Add qmd as an MCP server in Claude Code
Open your Claude Code MCP config at `~/.claude/mcp.json` and add qmd:

```json
{
  "mcpServers": {
    "qmd": {
      "command": "qmd",
      "args": ["mcp"]
    }
  }
}
```

#### Step 4: The secret sauce — CLAUDE.md
Claude Code doesn’t know it should use qmd unless you tell it. Add this to your project’s `CLAUDE.md` (or `~/.claude/CLAUDE.md` for a global rule):

> **Rule: always use qmd before reading files**
> Before reading files or exploring directories, always use qmd to search for information in local projects.
>
> **Available tools:**
> *   `qmd search “query”` — fast keyword search (BM25)
> *   `qmd query “query”` — hybrid search with reranking (best quality)
> *   `qmd vsearch “query”` — semantic vector search
> *   `qmd get <file>` — retrieve a specific document

---

### The three search modes explained
*   **search:** BM25 keyword search. Fastest. Use for exact terms like "auth middleware".
*   **vsearch:** Vector similarity search. Finds conceptually related content (e.g., "how does the app handle errors?").
*   **query:** Hybrid search with LLM reranking. Best quality for complex questions.

### The bottom line
If you’re using Claude Code on any non-trivial codebase and you’re not indexing it, you’re paying a token tax on every single interaction. **qmd** eliminates that tax.

**GitHub Link:** [https://github.com/tobi/qmd](https://github.com/tobi/qmd)

---
*Source: Archived Medium Article by Simone Ruggiero (Feb 2026)*
