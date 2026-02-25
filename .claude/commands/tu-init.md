---
description: 😏 Create CLAUDE.md file
---

## Step 1: Explore the Project

Read in parallel:

- Package manifest: `package.json`, `go.mod`, `Cargo.toml`, `pyproject.toml`, `requirements.txt`
- Build/test scripts: `package.json` scripts, `Makefile`, `justfile`, `taskfile.yml`
- Directory structure: top 1–2 levels
- Lint/format config: `.eslintrc*`, `biome.json`, `.prettierrc`, `ruff.toml`, etc.
- Existing `CLAUDE.md` if present — improve it, don't replace blindly
- `.github/workflows/` (optional)

## Step 2: Decide What Belongs in CLAUDE.md

**Include:**
- Build, test, and lint commands
- Primary tech stack (names only)
- Directory layout — only if monorepo or non-obvious
- Hard constraints not inferable from code (e.g., "never commit to main", "run migrations before tests")

**Exclude:**
- Coding style details (use linters)
- Full dependency lists
- Generic best practices
- Anything only relevant to 1–2 task types

## Step 3: Decide on agent_docs/

Only create if the project is complex enough to warrant it.

| File | When to create |
|------|----------------|
| `agent_docs/architecture.md` | Multiple services or non-obvious data flow |
| `agent_docs/testing.md` | Complex test setup, fixtures, mocking |
| `agent_docs/database.md` | Schema, migrations, or query patterns |
| `agent_docs/deployment.md` | Non-trivial deploy/release process |
| `agent_docs/code_style.md` | Conventions that can't be enforced by linters |

Each file must start with a **"When to read this file"** section.

## Step 4: Write CLAUDE.md

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

[Only include if agent_docs/ was created]

Before starting any task, decide which files below are relevant and read them first.

- `agent_docs/architecture.md` — [one-line description]
- `agent_docs/testing.md` — [one-line description]
```

## Step 5: Write agent_docs/ Files (if applicable)

Write comprehensive content for each file. These are loaded on-demand, so detail is welcome here.

## Step 6: Present Results

1. Show the full contents of `CLAUDE.md`
2. List any `agent_docs/` files created with a one-line summary each
3. Suggest 2–3 things the user should manually add (team conventions, external service details, deployment targets)
