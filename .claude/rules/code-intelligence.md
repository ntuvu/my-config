### Code Intelligence

Prefer LSP over Grep/Glob/Read for code navigation:
- `goToDefinition` / `goToImplementation` — jump to source
- `findReferences` — see all usages across the codebase
- `workspaceSymbol` — find where something is defined
- `documentSymbol` — list all symbols in a file
- `hover` — get type info without reading the file
- `incomingCalls` / `outgoingCalls` — explore call hierarchy

Before renaming or changing a function signature, use `findReferences` to locate all call sites first.

Fall back to Grep/Glob/Read when:
- LSP returns no results or incomplete results
- Searching comments, string literals, or config values
- LSP is unavailable or the file type isn't supported

After writing or editing code, check LSP diagnostics before moving on. Fix type errors and missing imports immediately.
