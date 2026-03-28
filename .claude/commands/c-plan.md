---
description: Tạo technical plan chi tiết (research + codebase analysis + solution design + review) bằng a-planner. Chỉ lập kế hoạch, không implement code.
argument-hint: [technical-request]
model: haiku
---

# c-plan

Tạo một plan self-contained, bám sát `CLAUDE.md`, và lưu vào `plans/*.md`.

## Rules

1. Chỉ tạo plan, tuyệt đối không implement code.
2. Ưu tiên token efficiency: ngắn gọn, không lặp.
3. Bắt buộc dùng Agent tool để gọi `a-planner`, không dùng bash để gọi agent.
4. Kết quả trả về cho user chỉ gồm:
   - Summary ngắn
   - Kết luận review (`GO`, `HOLD`, hoặc `NO-GO`)
   - File path plan

## Workflow

1. Đọc yêu cầu từ `$ARGUMENTS`.
2. Nếu `$ARGUMENTS` rỗng, hỏi user yêu cầu kỹ thuật cần lập plan.
3. Gọi agent:
   - `subagent_type`: `a-planner`
   - `description`: `Create and review a self-contained technical plan`
   - `prompt`: Bao gồm yêu cầu người dùng, nhấn mạnh `YAGNI`, `KISS`, `DRY`, và chỉ được tạo plan.
4. Chờ agent hoàn tất rồi trả kết quả ngắn gọn theo đúng format.
