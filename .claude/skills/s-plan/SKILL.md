---
name: s-plan
description: Tạo technical plan self-contained trong plans/*.md dựa trên research + codebase analysis + solution design. Chỉ lập kế hoạch, không implement code.
user-invocable: false
---

# s-plan

Tạo một kế hoạch kỹ thuật chi tiết, self-contained, có path rõ ràng và sẵn sàng handoff.

## Requirements

1. Chỉ lập kế hoạch; không implement code.
2. Tuân thủ `CLAUDE.md`.
3. Tuân thủ `YAGNI`, `KISS`, `DRY`.
4. Ưu tiên token efficiency: viết ngắn, rõ, không lặp.
5. Lưu plan vào `plans/*.md` tại root repo.

## Naming Rules

1. Tạo timestamp bằng script:
   - `python3 .claude/skills/s-plan/scripts/plan_timestamp.py`
2. Timestamp format bắt buộc: `YYYY-MM-DD-HHmm`.
3. Tạo slug từ yêu cầu:
   - lowercase
   - `kebab-case`
   - bỏ ký tự đặc biệt
   - tối đa 6 từ
4. File name:
   - `plans/<timestamp>-<slug>.md`

## Plan Template (Concise Structured)

Nội dung plan phải có đúng các phần sau:

1. `Title`
2. `Summary`
3. `Context & Findings` (research + codebase analysis)
4. `Scope / Non-Goals`
5. `Proposed Design` (architecture/system design)
6. `Implementation Plan` (phase-by-phase, không viết code)
7. `Validation Strategy` (test/acceptance criteria)
8. `Risks & Mitigations`
9. `Assumptions`

## Output

Sau khi ghi file xong, chỉ trả:

```text
plan_path: plans/<timestamp>-<slug>.md
summary: <2-4 câu ngắn>
```
