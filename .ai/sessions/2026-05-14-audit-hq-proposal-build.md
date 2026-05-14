# Session: Build đề án Audit-HQ từ scratch (v1 → v10)

**Ngày:** 2026-05-13 → 2026-05-14
**Tác giả AI:** Claude Opus 4.7
**Owner:** Vương (Tinsu AI)

## Tổng quan

Toàn bộ session từ ý tưởng ban đầu đến bản dự thảo sẵn sàng gửi Hải Quan. 10 vòng iterate qua nhiều loại phản hồi: grill (9 câu), tổng hợp với showcase checklist, Việt hoá ngôn ngữ, nén timeline, domain-expert review, critic review độc lập, refinement chi tiết.

Tổng kết quả:
- Repo `TinsuAI/audit-hq` private đã được tạo, push thường xuyên
- Đề án `de-an-audit-hq.md` (~600 dòng) ở bản nháp 10
- HTML render đã deploy tại `https://audit-hq.tinsu.ai/` (Docker nginx + Cloudflare Tunnel)
- Catalog 49 kiểm tra chia 2 giai đoạn

## What Was Done

### Giai đoạn 1: Grill + initial draft (v1)

- 9 câu grill (skill `grill-me` cài đặt project-scoped từ Matt Pocock template, được customize cho audit-hq context):
  1. Ai là người dùng? → Phòng QLRR Cục/Tổng cục Hải quan (sau đó tổng quát hoá thành "Hải quan")
  2. Dữ liệu HQ có gì? → Excel BCCT + Mẫu 15/15a/16
  3. MVP "xong" trông như thế nào? → 5 DN × 3-4 năm + findings list + Excel report
  4. Trọng Tín có data + COI + data representativeness? → có Trọng Tín partner, tool vs data tách bạch
  5. Trạng thái pitch + deliverable + timeline? → (ii) đã pitch, HQ quan tâm, fastest possible
  6. Codebase audit-hq vs BCQT-System? → Repo riêng, copy proven libs
  7. Demo flow + wow moment? → multi-DN ranking + drill-down evidence
  8. Synthetic data, 5 DN × 3-4 năm, anonymize tất cả
  9. Catalog 36 finding categories (MVP-15)

- v1: Catalog 36 kiểm tra theo tier A-F. 9 sections + phụ lục.

### Giai đoạn 2: Synthesize + cleanup (v2-v4)

- **v2**: User chỉ tới Tinsu BCQT showcase checklist (`https://bcqt-showcase.tinsu.ai/static/internal/hq-audit-checklist-20260513.md`). Replace tier-based 36 với 28 checks chia 6 nhóm theo problem domain + thêm 3 cross-DN Phase 2.
- **v3**: Việt hoá toàn bộ thuật ngữ kỹ thuật (MVP, POC, Pilot, evidence trail, drill-down, dashboard, schema, layer...). Đối tượng đọc là cán bộ HQ, không phải lập trình viên.
- **v4**: Bỏ mọi tham chiếu Johnson (case study Tinsu nội bộ); chuyển xưng hô "Hải quan" trống không thành "cơ quan Hải quan"; nén timeline từ "Phase 1/2/3 trải dài 18+ tháng" về "2 tháng (8 tuần)".

### Giai đoạn 3: Tách 2 giai đoạn + nhiều nhóm mới (v5-v6)

- **v5**: User feedback dài về catalog. Tách §4 thành 2 giai đoạn theo data needed:
  - Giai đoạn đầu (sau đổi tên "Giai đoạn I"): TKXNK + BCQT, HQ đã có sẵn
  - Giai đoạn sau ("Giai đoạn II"): cần dữ liệu/điều kiện bổ sung
  
  Thêm framing "Bộ ba tử huyệt" (định mức + BTP + phế liệu), §2.6 cộng dồn rủi ro, 4 nhóm mới (Nhóm 8 Phế liệu, Nhóm 9 BTP, Nhóm 10 Sổ sách KT, Nhóm 11 TSCĐ).
  
  Cập nhật rủi ro 8 kiểm tra theo user feedback (C1.3, C2.3, C2.4, C2.5, C3.2, C4.3, C5.2, C6.4). Thêm C4.7 (phân bổ định mức bất thường).

- **v6**: Tách bảng catalog từ 4 cột thành 5 cột — `Mã | Vấn đề | Rủi ro | Mức | Trạng thái` (script Python parse 11 bảng, 44 dòng). Sửa CSS list spacing. Viết lại C2.1/C2.2 risk (user phát hiện wording cũ tối nghĩa). Bổ sung C1.4 missing risk. 10 năm → 5 năm vận hành chính thức.

### Giai đoạn 4: Domain-expert review (v7)

- Tôi review độc lập 44 kiểm tra như domain expert. Tìm ra:
  - **C4.1 bug**: false positive với NVL có tồn đầu > 0 từ kỳ trước. Sửa: thêm điều kiện `tồn_đầu_kỳ = 0`.
  - **C2.5 redundant với C2.1**: toán học là một dạng cụ thể. User chọn merge C2.5 vào C2.1.
  - **C4.6 dataset không rõ**: outlier so với gì? Chốt: cùng DN qua các kỳ.
  - **C5.3 false positive**: với BTP và TP nội địa. Thêm note loại trừ.
  - **C10.2/C10.3 thiếu dung sai**: thêm ngưỡng 2-5%.
  - **C8.1 ngưỡng từ đâu**: chốt = HQ định nghĩa danh mục theo ngành.
  - **C9.1, C9.3, C11.2 vague**: chốt phép tính cụ thể.

  Tôi đề xuất sửa cả chiều của C4.3 (thấp + cao), nhưng user phản biện đúng: chiều "thấp" là bình thường vì còn tồn TP/BTP. Skip.

### Giai đoạn 5: Batch suggestions + cleanup (v8)

- Thêm §2.7 phát hiện kết hợp (combination signatures) với 3 bộ ba điển hình.
- Thêm "Tiền đề kỹ thuật" ở đầu §4 (sau đó user yêu cầu bỏ "lọc tờ khai huỷ" và "ánh xạ mã hàng" — chỉ giữ định nghĩa "kỳ" và đơn vị tiền tệ).
- Thêm C1.7 (tỷ lệ chuyển MĐSD trên tổng nhập).
- Thêm Nhóm 12 (Nhà cung cấp) — ban đầu trong Giai đoạn I.
- Bỏ §9.3 Lịch sử bản (changelog).

### Giai đoạn 6: Critic review độc lập + áp dụng (v9-v10)

- Đổi "Giai đoạn đầu/sau" → "Giai đoạn I/II" (v9).
- Gọi Agent với subagent_type=critic để review toàn bộ document. Critic trả 4 CRITICAL + 7 WARNING + 6 SUGGESTION.
- User chọn áp dụng:
  - **CRITICAL #4**: thêm kiểm tra tồn ảo (C11.3 Tồn kho vs năng lực vận hành).
  - **CRITICAL #2/#3**: timeline 8 → 10 tuần (cộng dồn cả critic warning #3); §8.5 ranh giới pháp lý gộp thành §2.8 tuyên bố cứng (sau đó user bỏ bớt câu "Tinsu cam kết giải trình" và "Tinsu không tham gia tố tụng" — chỉ giữ câu Audit-HQ là gợi ý sơ bộ).
  - **SUGGESTION**: thay "trình diễn" → "demo" (19 chỗ).
  - **SKIP**: không trích dẫn điều khoản pháp lý per check; không tuyên bố COI explicit.

### Giai đoạn 7: Micro-refinements

- Chuyển Nhóm 12 (NCC) từ Giai đoạn I sang Giai đoạn II (đặc trưng là cần điều kiện dữ liệu).
- Viết lại §5.3 AI role: từ "AI không trực tiếp đưa ra phát hiện. AI chỉ làm các việc hỗ trợ" (defensive, sounding dim) → "Hệ thống chia rõ công việc giữa quy tắc xác định và AI" (positive framing).
- Bỏ Q16 (cán bộ Chi Cục đào tạo).
- Ẩn số phiên bản khỏi trang ("Bản nháp 10" → "Bản dự thảo"), giữ trong HTML comment.
- Thêm C4.8 (tồn NVL âm tại thời điểm trong kỳ — `tồn_đầu + Σ nhập − Σ định mức × xuất < 0`).

## Decisions Made

1. **Audit-HQ là tool, không phải data marketplace.** Trọng Tín không chuyển dữ liệu khách hàng sang HQ — chỉ build và demo công cụ. Wording trong đề án thay "Trọng Tín cung cấp data" bằng "dữ liệu giả lập, xoá danh tính từ dữ liệu thực".
2. **Catalog chia 2 giai đoạn theo data availability**, không phải theo độ ưu tiên. Cán bộ HQ phân biệt rõ "có thể chạy với data đang có" vs "cần xin thêm".
3. **Không trích dẫn điều khoản pháp lý chi tiết per check** (user override critic). §1.4 list pháp lý chung là đủ.
4. **MVP scope co lại nhiều vòng**: 36 → 28 → 31 → 47 → 49 (full catalog), nhưng MVP build trong 10 tuần chỉ 16 kiểm tra. 14 W.I.P bổ sung thí điểm, 19 phụ thuộc điều kiện.
5. **Timeline 10 tuần** thay vì 8 tuần (critic warning về Johnson — 1 DN còn cần 6 tháng).
6. **Hosting docker nginx + Cloudflare Tunnel** thay vì nginx-on-host. User trong docker group, không sudo. Tunnel "remotely-managed" → phải PUT ingress qua Cloudflare API (script `deploy/scripts/add-ingress.py`).
7. **Đề án và repo code tách bạch**: repo `audit-hq` chỉ chứa đề án + deploy + skills. Repo code MVP sẽ tạo riêng khi HQ approve POC.

## What Didn't Work

1. **Đề xuất ban đầu trích dẫn pháp lý per check** — user reject thẳng, "không cần trong từng check, đủ trong §1.4".
2. **C4.3 mở rộng 2 chiều (cao + thấp)** — tôi đề xuất từ domain review, nhưng user chỉ ra chiều "thấp" là bình thường (còn tồn TP/BTP chưa XK). Skip đề xuất.
3. **Tinsu cam kết "chỉ giải trình thuật toán" + "không tham gia tố tụng"** — tôi viết theo critic, user thấy thừa và đẩy Tinsu vào thế ràng buộc pháp lý không cần thiết. Bỏ.
4. **Phương án ban đầu host trên server qua nginx-on-host** — user override: dùng Docker để không sudo. Tôi đã đi sâu vào nginx config + Let's Encrypt trước khi pivot.
5. **Khi cần SSH từ WSL**: WSL ssh đang lỗi (MTU issue). Phải dùng `ssh.exe -F` của Windows.
6. **Tunnel `tinsu-online-server` ban đầu tôi tưởng locally-managed** → edit `/etc/cloudflared/config.yml` + reload. Không có hiệu lực vì tunnel **remotely-managed**. Sửa bằng cách dùng Cloudflare API qua cert.pem token.
7. **Domain `sgnai.dev`** ban đầu tôi tưởng là domain Tinsu chính (do thấy `codex-lb-demo.sgnai.dev`). Thực tế tunnel cert chỉ có quyền zone `tinsu.ai`. Đổi URL sang `audit-hq.tinsu.ai`.

## Open Items

1. Trọng Tín review v10 — chưa có timeline.
2. Trọng Tín liên hệ Chi Cục Hải Quan Khu vực IV — chưa có lịch.
3. Sponsor cụ thể ở HQ (cá nhân nào) — chưa biết.
4. Trọng Tín chuẩn bị 5 DN nền giả lập — chưa bắt đầu (làm khi HQ approve POC).
5. Repo code MVP — chưa tạo (làm khi HQ approve POC).

## Reusable Knowledge

Có 2 điểm có thể đáng lưu vào shared knowledge base (~/dotfiles/ai/knowledge/):

1. **Cloudflare Tunnel locally-managed vs remotely-managed**: Khi tunnel được tạo qua Cloudflare Zero Trust dashboard hoặc đã được migrate sang remote management, edit `/etc/cloudflared/config.yml` KHÔNG có hiệu lực — config bị remote override. Phải sửa qua dashboard hoặc Cloudflare API (POST `/accounts/{accountID}/cfd_tunnel/{tunnelID}/configurations`). Cert.pem trong `~/.cloudflared/` thường có `apiToken` đủ quyền (base64-decoded JSON với fields `apiToken`, `accountID`, `zoneID`).

2. **SSH từ WSL có MTU issue khi qua Tailscale**: Large transfers (>50MB) drop. Workaround: dùng `ssh.exe` của Windows với `-F 'C:\Users\<user>\.ssh\config'`. WSL SSH config (`~/.ssh/config`) và Windows SSH config là 2 file riêng biệt.

Tôi sẽ KHÔNG tự ghi vào knowledge base mà chỉ flag ở đây. Owner quyết.
