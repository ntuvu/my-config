### source: https://karanbansal.in/blog/claude-code-lsp/#setting-it-up

# THE 2-MINUTE CLAUDE CODE UPGRADE YOU'RE PROBABLY MISSING: LSP

**Date:** February 28, 2026

Right now, every Claude Code user is running without LSP. That means every time you ask "where is processPayment defined?", Claude Code does what you'd do with a terminal. It greps. It searches text patterns across your entire codebase, reads through dozens of files, and tries to figure out which match is the actual definition.

It works. But it's slow, it's fuzzy, and on large codebases it regularly misses or gets confused. Search for User in a real project and you get 847 matches across 203 files: class definitions, variable names, comments, imports, CSS classes, SQL columns. The thing you actually wanted? Buried somewhere in the middle. Claude Code has to read through each match to narrow it down. That takes 30-60 seconds. Sometimes longer.

There's a feature that changes this entirely. It's called LSP, the Language Server Protocol. It's not enabled by default. It's not prominently documented. The setup requires a flag discovered through a GitHub issue, not the official docs. But once it's on, the same query ("where is processPayment defined?") returns the exact file and line number in 50 milliseconds. Not 30 seconds. Fifty milliseconds. With 100% accuracy.

That's not an incremental improvement. That's a category change in how Claude Code navigates your code.

## TL;DR

Claude Code ships without LSP enabled. Enabling it gives Claude the same code intelligence your IDE has: go-to-definition, find references, type info, real-time error detection. From my debug logs: ~50ms per query vs 30-60s with grep. Two minutes of setup.

---

## WHAT YOU'RE CURRENTLY RUNNING

By default, Claude Code navigates your codebase with text search tools: Grep, Glob, and Read. It's the same as having a very fast developer with grep and find at a terminal. Smart pattern matching, but fundamentally just matching text.

The core problem: grep treats code as text. But code is not text. It has structure, meaning, and relationships. When you ask "where is getUserById defined?", you want the one function definition, not the 50 places that call it plus the 12 comments that mention it. Grep can't tell the difference. LSP can.

## WHAT LSP ACTUALLY IS

Before 2016, every code editor had to build its own language support from scratch. VS Code needed a Python plugin. Vim needed a separate Python plugin. Emacs, Sublime, Atom — each one reinventing the same work. Twenty editors times fifty languages meant a thousand separate implementations, most of them incomplete.

**Before LSP:** M × N (e.g., 4 editors × 4 languages = 16 plugins)
**With LSP:** M + N (e.g., 4 editors + 4 languages = 8 implementations)

In 2016, Microsoft had an insight: separate the language intelligence from the editor. Create a protocol, a standard way for any editor to talk to any language server. The editor says "where is this symbol defined?" in JSON-RPC. The language server (a separate process that deeply understands one language) answers.

That's LSP. It turned a thousand-implementation problem into a seventy-implementation one. And it's why your VS Code Python experience is exactly as good as your Neovim Python experience — they're both talking to Pyright.

## THE PERFORMANCE GAP

AI coding assistants had the exact same problem that editors had before LSP. Without it, Claude Code does text search. Grep, Glob, Read. It works. But the cost is measured in seconds per query, multiplied by dozens of queries per task. It adds up fast.

| Method | Process | Result |
| :--- | :--- | :--- |
| **Without LSP** | `grep -r "User"` (847 matches, 203 files) | ~30-60 seconds, maybe correct |
| **With LSP** | `goToDefinition` JSON-RPC | ~50ms, 100% accurate |

LSP is ~900× faster with guaranteed accuracy.

## WHAT CLAUDE CODE GETS FROM LSP

LSP gives Claude Code two categories of superpowers: things that happen automatically and things it can actively request.

### PASSIVE: SELF-CORRECTING EDITS

This is the most valuable part. After every file edit, the language server pushes diagnostics: type errors, missing imports, undefined variables. Claude Code sees these immediately and fixes them in the same turn, before you ever see the error.

1. You ask Claude: "Add email param"
2. Claude edits `createUser()`
3. LSP detects 3 errors in call sites
4. Claude fixes all 3
5. Result: 0 errors ✓

All 4 steps happen in a single turn. Without LSP, you'd have to manually find errors, paste them back to Claude, and iterate.

### ACTIVE: ON-DEMAND CODE INTELLIGENCE

Claude Code can explicitly ask the language server questions:

*   **goToDefinition** — "Where is processOrder defined?" → exact file and line
*   **findReferences** — "Find all places that call validateUser" → every call site with location
*   **hover** — "What type is the config variable?" → full type signature and docs
*   **documentSymbol** — "List all functions in this file" → every symbol with location
*   **workspaceSymbol** — "Find the PaymentService class" → search symbols across the entire project
*   **goToImplementation** — "What classes implement AuthProvider?" → concrete implementations of interfaces
*   **incomingCalls / outgoingCalls** — "What calls processPayment?" → full call hierarchy tracing

---

## SETTING IT UP

It takes about 2 minutes, and you only do it once.

### PREREQUISITES

*   Claude Code version 2.0.74 or later (run `claude --version` to check)
*   The language server binary for your language(s) installed and in `$PATH`

### STEP 1: ENABLE THE LSP TOOL

Add this to your `~/.claude/settings.json`:

```json
"env": { "ENABLE_LSP_TOOL": "1" }
```

*Note: `ENABLE_LSP_TOOL` is not officially documented as of February 2026. It was discovered via GitHub Issue #15619. I also recommend adding `export ENABLE_LSP_TOOL=1` to your shell profile (`.zshrc` or `.bashrc`).*

### STEP 2: INSTALL THE LANGUAGE SERVER

Install the binary for each language you work with:

| Language | Plugin | Install Command |
| :--- | :--- | :--- |
| Python | pyright-lsp | `npm i -g pyright` |
| TypeScript/JS | typescript-lsp | `npm i -g typescript-language-server typescript` |
| Go | gopls-lsp | `go install golang.org/x/tools/gopls@latest` |
| Rust | rust-analyzer-lsp | `rustup component add rust-analyzer` |
| Java | jdtls-lsp | `brew install jdtls` |
| C/C++ | clangd-lsp | `brew install llvm` |
| C# | csharp-lsp | `dotnet tool install -g csharp-ls` |
| PHP | php-lsp | `npm i -g intelephense` |

### STEP 3: INSTALL AND ENABLE THE PLUGIN

First, update the marketplace catalog:
`claude plugin marketplace update claude-plugins-official`

Then install the plugin for your language:
`claude plugin install pyright-lsp Python` (example)

Verify it's installed and enabled:
`claude plugin list`

**The #1 gotcha:** If status is `disabled`, run `claude plugin enable <name>` and restart. You can also explicitly set them in `~/.claude/settings.json`:

```json
{
  "env": {
    "ENABLE_LSP_TOOL": "1"
  },
  "enabledPlugins": {
    "pyright-lsp@claude-plugins-official": true,
    "typescript-lsp@claude-plugins-official": true,
    "gopls-lsp@claude-plugins-official": true
  }
}
```

### STEP 4: RESTART CLAUDE CODE

LSP servers initialize at startup. After restarting, verify by asking: "What type is [some variable]?"

---

## WHAT HAPPENS AT STARTUP

When Claude Code starts, all enabled LSP servers launch simultaneously and begin indexing your entire project immediately. By the time you ask your first question, the index is already warm. This means operations work for any symbol in your project, not just files you've opened.

## USING IT IN PRACTICE

Just talk to Claude Code naturally. It routes to the right LSP operation automatically:
*   "Where is authenticate defined?" → `goToDefinition`
*   "Find all usages of UserService" → `findReferences`
*   "What type is response?" → `hover`
*   "What calls processPayment?" → `incomingCalls`

You can also press **Ctrl+O** to see diagnostics pushed by LSP servers in real time.

## THE GOTCHAS

| Issue | Cause | Fix |
| :--- | :--- | :--- |
| LSP tool not available | `ENABLE_LSP_TOOL` not set | Add to `settings.json`, restart |
| Plugin not found | Stale marketplace catalog | `claude plugin marketplace update` |
| Plugin installed but disabled | Not enabled after install | `claude plugin enable <name>` + restart |
| Executable not found | Binary not in `$PATH` | Install binary, verify with `which` |

## DEBUG CHECKLIST

1.  Check binary: `which pyright-langserver`
2.  Check plugin status: `claude plugin list` (must be `enabled`)
3.  Check logs: `~/.claude/debug/latest` — search for "Total LSP servers loaded: N"

## NUDGING CLAUDE TO ACTUALLY USE LSP

Claude may default to Grep/Read. To fix this, add instructions to your `~/.claude/CLAUDE.md`:

### Code Intelligence

Prefer LSP over Grep/Glob/Read for code navigation:
- `goToDefinition` / `goToImplementation` to jump to source
- `findReferences` to see all usages across the codebase
- `workspaceSymbol` to find where something is defined
- `documentSymbol` to list all symbols in a file
- `hover` for type info without reading the file
- `incomingCalls` / `outgoingCalls` for call hierarchy

Before renaming or changing a function signature, use `findReferences` to find all call sites first. Use Grep/Glob only for text/pattern searches where LSP doesn't help. After editing code, check LSP diagnostics and fix errors immediately.
