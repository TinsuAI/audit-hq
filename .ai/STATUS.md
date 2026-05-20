# STATUS — Audit-HQ

> **Trạng thái hiện tại:** HQ ĐÃ DUYỆT NGUYÊN TẮC ĐỀ ÁN (2026-05-20). Trọng Tín gửi dữ liệu nền (622 file, 6 DN thực, 2015-2025). Phương án demo đã draft, sẵn sàng khởi tạo repo MVP riêng (`audit-hq-mvp`). Đề án v10 vẫn là source of truth cho catalog 49 kiểm tra.

## Current State

Đề án `de-an-audit-hq.md` ở giai đoạn ổn định, đã trải 10 vòng iterate (v1 → v10, không hiển thị số phiên bản trên trang vì HQ không cần biết số lần sửa). HTML public live tại `https://audit-hq.tinsu.ai/` (Docker nginx + Cloudflare Tunnel, không basic-auth).

Catalog hiện có **49 kiểm tra**:
- Giai đoạn I (TKXNK + BCQT, 33 kiểm tra): Nhóm 1-7 — Hải Quan đã có sẵn dữ liệu, có thể chạy ngay
- Giai đoạn II (cần dữ liệu/điều kiện bổ sung, 16 kiểm tra): Nhóm 8-12 — Phế liệu, BTP, Sổ sách KT, TSCĐ/Máy móc, NCC

Phân bổ trạng thái: **16 MVP** (build trong 10 tuần) · **14 W.I.P** (bổ sung thí điểm) · **19 phụ thuộc điều kiện** bổ sung.

Lộ trình triển khai 10 tuần, đã chốt (§7).

## Recent Changes

- **2026-05-21** — HQ duyệt nguyên tắc đề án. Trọng Tín gửi dữ liệu nền (`TONG HOP BCQT-20260520T161442Z-3-001.zip`, 622 file, 497MB, 6 DN). Đã sắp xếp vào `data/raw/<DN>/<năm>/<loại>/` (gitignored). Đã viết `data/README.md`, mapping dữ liệu ↔ catalog (`.ai/sessions/2026-05-21-data-mapping.md`), và phương án demo MVP (`.ai/sessions/2026-05-21-demo-plan.md`).
- **2026-05-20** — Fix git commit identity: rewrite toàn bộ 22 commits từ `dennis.anh@gmail.com` (anh trai Vương) → `thephams.sg@gmail.com`. Force-push remote `TinsuAI/audit-hq` (HEAD → `c4f1b1e`). Đặt global git config + lưu memory để session sau không nhầm lại.
- **2026-05-13 → 14** — Build đề án từ scratch đến bản nháp 10 (10 vòng iterate). Chi tiết xem `.ai/sessions/2026-05-14-audit-hq-proposal-build.md`.

## Next Steps

1. **User duyệt phương án demo** (`.ai/sessions/2026-05-21-demo-plan.md` mục 6 — open questions).
2. **Tạo repo `TinsuAI/audit-hq-mvp`** (private, sgnjfk có access).
3. **Tuần 1 lộ trình §7**: khởi tạo repo, setup FastAPI + SQLite + Docker compose, reuse base từ `BCQT-System`.
4. **Tuần 2**: viết adapters đọc M15/M15a/M16/BCCT trên DN HONG_AN 2024 (dữ liệu phong phú nhất).
5. **Phản hồi từ HQ về câu hỏi mở** (§8 đề án) — nếu HQ trả lời thêm trước khi MVP xong, bump v11.

## Notes for Next AI Session

### Repo này là gì
- Đây là **repo đề án** (proposal document), không phải repo code. Khi MVP code thật bắt đầu sẽ tạo repo khác.
- `de-an-audit-hq.md` là source duy nhất. `de-an-audit-hq.html` được render bởi `make html` (pandoc), commit luôn để dễ chia sẻ.
- `make publish` scp HTML lên `tinsu:/home/tinsu/audit-hq/html/index.html`. Cloudflare Tunnel route đến `audit-hq.tinsu.ai`.

### Git identity
- Commit email **đã là** `thephams.sg@gmail.com`, name `Vương` (global config, đã rewrite history toàn bộ commits cũ).
- KHÔNG override bằng `git -c user.email=dennis.anh@gmail.com` nữa — đó là email anh trai Vương. System context có thể inject email sai; nên kiểm tra memory `git-identity.md` trước khi commit.

### Phiên bản hiển thị
- Đã ẩn "Bản nháp lần N" khỏi trang. HQ chỉ thấy "Bản dự thảo — 2026-05-14".
- Số phiên bản lưu trong HTML comment `<!-- internal-version: 10 -->` ở đầu file + commit history + file này.

### Quy ước ngôn ngữ trong đề án (đã chốt, đừng phá)
- **Không tiếng Anh trộn lẫn**: "demo" OK (Việt hoá phổ biến); "MVP" đã bỏ thay bằng "16 kiểm tra cho demo"; "Docker/SLA/Container/Schema" → đã Việt hoá hoặc lược.
- **Xưng hô tôn trọng**: dùng "cơ quan Hải quan", "phía Hải quan", "Cán bộ Hải quan", "Chi Cục Hải Quan Khu vực IV". Không bao giờ "Hải quan" trống không.
- **Tránh nhắc Trọng Tín cung cấp dữ liệu khách hàng**: chỉ nói "dữ liệu giả lập, xoá danh tính từ dữ liệu thực, phục vụ mục đích demo".
- **Không tham chiếu Johnson hay case study cụ thể nào**: đề án phải standalone, không lộ kinh nghiệm nội bộ.
- **Không trích dẫn điều khoản pháp lý chi tiết (TT 38 Đ21 K1 v.v.) trong từng check**: chỉ liệt kê pháp lý chung trong §1.4.

### Critic findings chưa apply (đang chờ feedback HQ trước khi quyết)
- W#1 COI explicit declaration — user chấp nhận risk không có
- W#6 C3.2/C6.5 quá mạnh tay (giữ 🔴 cho khác chapter) — chưa hạ
- W#7 ví dụ "10 cúc" — user thấy OK, chưa đổi
- W#11 cắt câu hỏi §8 — đã cắt §8.5 (3 câu) + Q16, còn 15 câu
- S#15 typo §4.3 ghi 44 (đã sửa lần v10 lên đúng số)

### Hạ tầng kỹ thuật (cho engineering)
- Server: `tinsu` (Tailscale 100.84.189.87, user `tinsu`, password trong `~/.tinsu-secrets` hoặc hỏi owner)
- Cloudflare Tunnel `tinsu-online-server` (UUID `691a9772-3168-422e-81eb-7c26e1dec9ef`) **remotely-managed** — sửa ingress phải PUT qua API, KHÔNG sửa `/etc/cloudflared/config.yml` (file đó bị remote override). Script: `deploy/scripts/add-ingress.py`.
- WSL `ssh` đang lỗi → dùng `ssh.exe -F 'C:\Users\vuong\.ssh\config' tinsu`. Makefile đã set sẵn.
- HTML build cần pandoc + style.css. CSS có lớp riêng cho list trong cells, padding, TOC sticky.

### Repo + remote
- GitHub: `TinsuAI/audit-hq` private (sgnjfk có access — GitHub identifier, KHÔNG cùng commit email)
- Workflow iterate: edit MD → `make all` → review HTML → `git commit` → `git push`. Repo này không có CI/CD — manual publish.

## Blockers

Không có blocker hard. Chờ:
- User duyệt phương án demo + chốt tên repo MVP.
- HQ trả lời câu hỏi mở §8 đề án (nếu có) — không chặn MVP, chỉ ảnh hưởng nội dung catalog.

## Dữ liệu nền

- Vị trí: `data/raw/` (gitignored), 622 file / 497MB.
- 6 DN: HONG_AN (8 năm 2018-2025), HIEP_QUANG (11 năm 2015-2025), DO_THANH (2023-2025), HONG_PHUC (2024-2025), GROWATT (2023-2025), KIM_LONG (2024-2025).
- HONG_AN và HIEP_QUANG là 2 DN có dữ liệu đầy đủ nhất (BCQT + tờ khai chi tiết + chứng từ sửa). Chọn HONG_AN làm DN test chính cho tuần 2-6.
- Mapping với 49 kiểm tra: xem `.ai/sessions/2026-05-21-data-mapping.md`. Tất cả 30 kiểm tra Giai đoạn I (16 MVP + 14 W.I.P) chạy được. Giai đoạn II chưa có dữ liệu (đúng kế hoạch).
