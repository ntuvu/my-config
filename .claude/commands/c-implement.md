---
name: c-implement
description: Execute a plan file from .claude/plans/ following the parallel execution algorithm — reads phases, runs parallel tasks simultaneously, sequential tasks in order, then verifies
argument-hint: <plan-slug>
model: sonnet
---

Execute the plan: **$ARGUMENTS**

## Step 1 — Load plan and execution guide

Read both files in parallel:
- `.claude/plans/$ARGUMENTS.md` — the plan to execute
- `.claude/docs/plan-execution-guide.md` — execution algorithm

If `.claude/plans/$ARGUMENTS.md` is not found, also try:
- `.claude/plans/$ARGUMENTS` (without extension check)
- List `.claude/plans/` and show matching files, ask user to confirm

## Step 2 — Display plan and confirm

Show the user a summary before starting:

```
📋 Plan: <objective>

Phases:
  Phase 1 [PARALLEL]   — <name>: N tasks
  Phase 2 [SEQUENTIAL] — <name>: N tasks
  Phase 3 [PARALLEL]   — <name>: N tasks
  ...
  Phase N [SEQUENTIAL] — Verification

Total: N tasks across N phases

⚡ Ready to execute? This will run all tasks automatically.
```

Wait for user confirmation before proceeding.

## Step 3 — Initialize execution state

```
results = {}   # stores outputs keyed by task_id
```

## Step 4 — Execute phases in order

For each phase in the plan, in sequence:

### If phase is PARALLEL

**CRITICAL: Launch ALL tasks in a SINGLE message** using multiple Agent tool calls simultaneously.

Before launching each task:
- Replace any `{{task_id}}` placeholders in the prompt with `results[task_id]`

Agent type mapping (from plan-execution-guide.md):
| Plan type    | Agent tool subagent_type |
|-------------|--------------------------|
| `explore`   | `Explore`                |
| `research`  | `general-purpose`        |
| `implement` | `general-purpose`        |
| `review`    | `general-purpose`        |

After ALL tasks complete:
- Store each output: `results[task_id] = output`
- Display: `✅ Phase N complete — N tasks finished`

### If phase is SEQUENTIAL

Execute tasks one at a time:
- Resolve `{{task_id}}` substitutions
- Run one task, wait for completion
- Store output: `results[task_id] = output`
- Proceed to next task
- Display progress after each task

## Step 5 — Verification

After all phases complete, run the verification section:

For each verification step:
- Execute the check
- Report ✅ PASSED or ❌ FAILED

Display final verification summary:
```
Verification Results:
  ✅ <criterion 1>
  ✅ <criterion 2>
  ❌ <criterion 3> — <reason>

Overall: PASSED (N/N criteria met)
```

## Step 6 — Final report

```
🎉 Implementation complete

  Plan     : .claude/plans/$ARGUMENTS.md
  Phases   : N completed
  Tasks    : N completed, N failed
  Duration : ~N minutes
  Status   : ✅ All verification criteria met
             (or ❌ N criteria failed — see above)
```

## Error handling

- **Task failure**: Log the error, continue other tasks in the phase if possible
- **Critical task failure**: Stop and report — do not proceed to dependent phases
- **Retry**: Retry failed tasks up to 2 times before marking as failed
- **Verification failure**: Report which criteria failed — do NOT silently pass
