---
name: s-project-explorer
description: Background knowledge for systematically exploring a project before writing CLAUDE.md
user-invocable: false
---

## Exploration Strategy

Read these files **in parallel** when analyzing a project:

### Package Manifests
- `package.json` — Node.js: scripts, dependencies, name
- `go.mod` — Go: modules and version
- `Cargo.toml` — Rust: crate metadata
- `pyproject.toml` / `requirements.txt` — Python: dependencies and tooling
- `pom.xml` / `build.gradle` — Java/Kotlin

### Build & Test Scripts
- `Makefile`, `justfile`, `taskfile.yml` — Task runners
- `package.json` scripts — npm/yarn/pnpm commands
- `scripts/` directory — Custom shell scripts

### Project Structure
- Top 1–2 directory levels — Identify monorepo vs single package
- `.github/workflows/` — CI/CD pipeline hints (optional)

### Lint & Format Config
- `.eslintrc*`, `biome.json`, `.prettierrc` — JS/TS linting
- `ruff.toml`, `.flake8`, `pyproject.toml [tool.ruff]` — Python
- `.golangci.yml` — Go linting
- `rustfmt.toml` — Rust formatting

### Existing Config
- `CLAUDE.md` — If present: improve it, don't replace blindly
- `agent_docs/` — If present: note what's already documented

## What to Include in CLAUDE.md

**Include:**
- Build, test, and lint commands (exact runnable commands)
- Primary tech stack (names only)
- Directory layout — only if monorepo or non-obvious
- Hard constraints not inferable from code (e.g., "never commit to main", "run migrations before tests")

**Exclude:**
- Coding style details (linters handle this)
- Full dependency lists
- Generic best practices
- Anything only relevant to 1–2 task types
