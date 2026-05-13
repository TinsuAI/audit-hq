# Audit-HQ — AI Agent Rules

> **Repo này là repo đề án (proposal document), KHÔNG phải repo code.**
> Khi MVP code thật bắt đầu, sẽ tạo repo khác.

## Mục đích repo

Soạn thảo + iterate đề án Audit-HQ (hệ thống Quản lý Rủi ro cho Hải quan) qua nhiều vòng feedback với HQ.

Output chính: `de-an-audit-hq.md` (source) và `de-an-audit-hq.html` (rendered, host trên `audit-hq.sgnai.dev`).

## Quy trình làm việc

1. Đọc `de-an-audit-hq.md`, `.ai/STATUS.md`, `.ai/DECISIONS.md` để hiểu trạng thái.
2. Edit `de-an-audit-hq.md` theo feedback.
3. `make html` để regen `de-an-audit-hq.html`.
4. `make publish` để scp lên Tinsu VPS (cần SSH host alias `tinsu`).
5. Commit cả `.md` lẫn `.html` (HTML để teammate không có pandoc vẫn xem được trên GitHub).
6. Update `.ai/STATUS.md` + thêm entry vào `.ai/DECISIONS.md` nếu có quyết định mới.

## Rules

- **Mọi nội dung khách hàng-facing:** tiếng Việt, full accents, tone formal.
- **Mọi con số/claim trong đề án phải defensible** với HQ — không bịa, có cơ sở pháp lý hoặc evidence trong reference projects.
- **Reference projects** (không phải dependency, chỉ tham khảo):
  - `~/workspace/client/BCQT-System` — kiến trúc + adapter pattern
  - `~/workspace/client/Johnson` — Phase 3 audit tests (cơ sở rule catalog)
  - `~/workspace/client/data-hub` — CI/CD + deploy shape
- **Không thay đổi version v0.1-DRAFT** trong file đề án trừ khi user yêu cầu bump.
- **Mọi vòng iterate** lưu summary vào `.ai/sessions/YYYY-MM-DD-<topic>.md`.

## Skills project-scoped

- `/grill-me` — Socratic interrogation về plan/design. Dùng khi user nói "grill me" hoặc muốn stress-test ý tưởng.

## Không làm

- Không thêm Dockerfile, docker-compose, app code — repo này chỉ là docs.
- Không tạo file `.py`, `.ts` v.v. — sai scope repo.
- Không bump version đề án tự động.
