# STATUS — Audit-HQ

> **Trạng thái hiện tại:** DRAFT v0.1 — chờ feedback vòng đầu tiên.

## Tóm tắt

Đề án Audit-HQ vừa hoàn thành DRAFT v0.1 ngày 2026-05-13. Đây là proposal document gửi Tổng cục Hải quan (qua Trọng Tín) để xin POC.

## Đã làm

- ✅ Grill 9 vòng với owner, lock decisions chính
- ✅ Soạn `de-an-audit-hq.md` (DRAFT v0.1) — đầy đủ 9 sections + phụ lục
- ✅ Catalog 36 sai phạm detectable, phân tier A-F, mark MVP-15/W.I.P/Phase-2
- ✅ Demo flow 5-phút, demo data composition (5 DN synthetic × 3-4 năm)
- ✅ Render HTML qua pandoc, embed CSS
- ✅ Setup repo (Makefile, nginx config, deploy steps)
- ⏳ Push remote `TinsuAI/audit-hq` private + setup VPS host

## Đang chờ

| Việc | Owner | Block |
|---|---|---|
| Tinsu/Trọng Tín review DRAFT v0.1 | Internal | Pitch HQ |
| HQ trao đổi DRAFT, feedback vòng 1 | Trọng Tín liên hệ | Bump v0.2 |
| Trọng Tín cung cấp 5 base DN data (anonymize) | Trọng Tín | Synthetic injection cho demo |
| Sponsor HQ cụ thể (Cục/Phòng QLRR nào?) | Trọng Tín | Tinh chỉnh đề án theo Cục đó |

## Next step

1. Push repo lên `TinsuAI/audit-hq` private
2. Cài host trên Tinsu VPS (xem `deploy/README.md`) — DNS, nginx, htpasswd, cert
3. `make publish` → URL `https://audit-hq.sgnai.dev/`
4. Chia sẻ URL + credential basic-auth với Trọng Tín, đợi feedback
5. Theo feedback → iterate `de-an-audit-hq.md`, bump version `v0.2-DRAFT`

## Blockers

- Chưa xác định sponsor HQ cụ thể → mọi assumption về scope dùng cho "phòng QLRR Cục/Tổng cục" generic.
- Chưa biết format Mẫu 15/15a/16 thực tế HQ có structured hay không → đề án giả định theo TT 39/2018 chuẩn.
- Demo data: phụ thuộc Trọng Tín có file base + sẵn sàng anonymize không.

## Vòng iterate dự kiến

| Version | Trigger | Khi nào |
|---|---|---|
| v0.1-DRAFT | Internal Tinsu review | Bây giờ |
| v0.2-DRAFT | Sau review nội bộ Tinsu + Trọng Tín | TBD |
| v0.3-DRAFT | Sau feedback vòng 1 HQ | TBD |
| v1.0 | Final, sau khi HQ approve nguyên tắc POC | TBD |
