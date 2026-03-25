---
name: c-plan
description: Create a structured execution plan file in .claude/plans/ for a feature or task, ready for human review before implementation
argument-hint: <feature-name or description>
model: opus
---

Create an execution plan for: **$ARGUMENTS**

## Step 1 — Read context

Read both files in parallel before doing anything else:
- `.claude/docs/plan-execution-guide.md` — execution algorithm (parallel vs sequential phases)
- `.claude/schemas/plan-schema.json` — structure reference

## Step 2 — Generate plan file name

Convert $ARGUMENTS to a descriptive slug: lowercase, spaces → hyphens, remove special characters.

Examples:
- "Create user authentication" → `create-user-authentication`
- "Refactor API layer" → `refactor-api-layer`
- "Add dark mode support" → `add-dark-mode-support`

Target file: `.claude/plans/<slug>.md`

## Step 3 — Invoke planning agent

Use the Agent tool to call the `a-plan` subagent with this prompt:

```
Create a structured execution plan for: $ARGUMENTS

Save the completed plan to: .claude/plans/<slug>.md

Requirements:
- Analyze the task and identify what can be done in parallel vs sequentially
- Design phases that maximize parallelism (tasks with no dependencies → same PARALLEL phase)
- Use {{task_id}} notation for cross-task dependencies
- Be specific enough that a subagent can execute each task independently without further clarification
- Always end with a verification phase
- Use the structure from .claude/schemas/plan-schema.json as reference
- Read .claude/docs/plan-execution-guide.md for the execution algorithm context
```

## Step 4 — Confirm and summarize

After the agent writes the file, display:

```
✅ Plan created: .claude/plans/<slug>.md

📋 Plan Summary:
  Objective : <one line>
  Phases    : <N> phases
  Tasks     : <N> total tasks
  Parallel  : Phases <list>
  Sequential: Phases <list>

👉 Review the plan, then run:
   /implement <slug>
```

## Critical constraint

⛔ **Do NOT begin any implementation.** This command creates the plan file only.
The human must review `.claude/plans/<slug>.md` and explicitly run `/implement` to proceed.
