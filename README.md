# Audit-HQ — Đề án

> **Hệ thống hỗ trợ Quản lý Rủi ro & phát hiện sai phạm trong BCQT + TKXNK**
> Soạn thảo bởi Tinsu AI × Trọng Tín, hướng tới khách hàng Tổng cục Hải quan.

## Repo này chứa gì?

Repo **đề án** (proposal document), **không phải repo code**. Khi MVP code thật bắt đầu, sẽ làm trong repo khác.

- [`de-an-audit-hq.md`](./de-an-audit-hq.md) — Source markdown để iterate
- [`de-an-audit-hq.html`](./de-an-audit-hq.html) — Rendered HTML, commit kèm để xem trên GitHub hoặc tải về

## Trạng thái

DRAFT v0.1 (2026-05-13). Sẽ iterate qua nhiều vòng với feedback HQ. Xem [`.ai/STATUS.md`](./.ai/STATUS.md) và [`.ai/DECISIONS.md`](./.ai/DECISIONS.md).

## URL công khai

```
https://audit-hq.tinsu.ai/
```

Host trên Tinsu VPS qua nginx. Có basic-auth bảo vệ (xem `deploy/README.md` để biết credential).

## Workflow iterate

```bash
# 1. Edit nội dung
vim de-an-audit-hq.md

# 2. Render HTML
make html

# 3. Push lên server
make publish

# 4. View tại https://audit-hq.tinsu.ai/

# 5. Commit
git add de-an-audit-hq.md de-an-audit-hq.html
git commit -m "wording: <what changed>"
git push
```

`make all` = html + publish trong 1 lệnh.

## Setup lần đầu trên VPS

Xem [`deploy/README.md`](./deploy/README.md) — nginx vhost, htpasswd, Let's Encrypt cert.

## Reference projects (sibling)

- `~/workspace/client/BCQT-System` — kiến trúc gốc cho phần technical đề án
- `~/workspace/client/Johnson` — Phase 3 audit tests làm cơ sở rule catalog
- `~/workspace/client/data-hub`, `~/workspace/client/barry-CO-main` — pattern deploy + nginx
