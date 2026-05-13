# STATUS — Audit-HQ

> **Trạng thái hiện tại:** DRAFT v0.2 — đã synthesize lần 1 với BCQT showcase checklist.

## Tóm tắt

Đề án Audit-HQ bump v0.2 ngày 2026-05-13. Đây là proposal document gửi **Chi Cục Hải Quan Khu vực IV** (qua Trọng Tín) để xin POC. Catalog rút gọn từ 36 (v0.1) xuống 28 + 3 Phase 2 = 31 checks, dựa trên showcase checklist v1.0 đã được Tinsu chuẩn hoá.

## Đã làm

- ✅ Grill 9 vòng với owner, lock decisions chính
- ✅ Soạn `de-an-audit-hq.md` (DRAFT v0.1 → v0.2)
- ✅ Synthesize v0.2: dùng catalog 28 checks từ Tinsu BCQT showcase + 3 Phase 2 cross-DN
- ✅ Cụ thể hoá đơn vị tiếp nhận: Chi Cục Hải Quan Khu vực IV
- ✅ Demo flow 5-phút, demo data composition (5 DN synthetic × 3-4 năm)
- ✅ Render HTML, deploy Docker nginx + Cloudflare Tunnel
- ✅ Public URL: https://audit-hq.tinsu.ai/ (đã bỏ basic-auth)
- ✅ Repo `TinsuAI/audit-hq` private, push thường xuyên

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
| v0.1-DRAFT | Internal Tinsu review | 2026-05-13 ✅ |
| v0.2-DRAFT | Synthesize với BCQT showcase checklist + cụ thể hoá Chi Cục Khu vực IV | 2026-05-13 ✅ |
| v0.3-DRAFT | Sau feedback vòng 1 Hải quan | TBD |
| v1.0 | Final, sau khi Hải quan approve nguyên tắc POC | TBD |
