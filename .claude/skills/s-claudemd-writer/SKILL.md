---
name: s-claudemd-writer
description: Format spec and writing rules for creating CLAUDE.md and agent_docs/ files
user-invocable: false
---

## CLAUDE.md Format

Target **under 80 lines** (blank lines excluded). Never exceed 150 lines.

```markdown
# CLAUDE.md

## Commands

[Essential build/test/lint commands]

## Architecture

[Primary tech stack + directory layout if non-trivial — max 8 lines]

## Key Rules

[Hard project-specific constraints — max 5 bullet points]

## Docs

[Only include this section if agent_docs/ was created]

Before starting any task, decide which files below are relevant and read them first.

- `agent_docs/architecture.md` — [one-line description]
- `agent_docs/testing.md` — [one-line description]
```

## agent_docs/ Decision Matrix

Only create if the project is complex enough to warrant it.

| File | When to create |
|------|----------------|
| `agent_docs/architecture.md` | Multiple services or non-obvious data flow |
| `agent_docs/testing.md` | Complex test setup, fixtures, mocking |
| `agent_docs/database.md` | Schema, migrations, or query patterns |
| `agent_docs/deployment.md` | Non-trivial deploy/release process |
| `agent_docs/code_style.md` | Conventions that can't be enforced by linters |

Each file must start with a **"When to read this file"** section. These files are loaded on-demand, so detail is welcome here.

## Presentation

After writing all files:

1. Show full contents of `CLAUDE.md`
2. List any `agent_docs/` files created with a one-line summary each
3. Suggest 2–3 things the user should manually add (team conventions, external service details, deployment targets)
