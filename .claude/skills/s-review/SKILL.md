---
name: s-review
description: Review technical plan và đưa ra kết luận GO/HOLD/NO-GO cùng gợi ý cải thiện ngắn gọn.
user-invocable: false
---

# s-review

Review file plan vừa được tạo và trả kết luận rõ ràng, ngắn gọn.

## Input

- `plan_path` từ bước `s-plan`.

## Review Checklist

1. Plan có self-contained không (đọc độc lập được không)?
2. Có bám `CLAUDE.md` không?
3. Có giữ nguyên tắc `YAGNI`, `KISS`, `DRY` không?
4. Scope có rõ và có non-goals không?
5. Phase implementation có đủ để triển khai sau này không (nhưng chưa viết code)?
6. Validation strategy có đo được không?
7. Rủi ro chính và hướng giảm thiểu có thực tế không?
8. Path/tài liệu liên quan có rõ ràng không?

## Output Format

Trả về đúng format này:

```text
review_verdict: GO|HOLD|NO-GO
review_summary: <2-4 câu>
key_risks:
- <risk 1>
- <risk 2>
- <risk 3>
key_suggestions:
- <suggestion 1>
- <suggestion 2>
- <suggestion 3>
```

## Constraints

1. Token efficiency: ngắn gọn, không lặp.
2. Không sửa code.
3. Chỉ đề xuất thay đổi cho plan.
