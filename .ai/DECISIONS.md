# DECISIONS — Audit-HQ

Log các quyết định quan trọng + lý do. Lock trong DRAFT v0.1 sau khi grill với owner.

---

## 2026-08-06 — Định mức hiệu lực kế thừa theo THÀNH PHẨM, không ghép từng cặp

**Quyết định:** Sửa luật định mức hiệu lực chốt 05/08: bản khai Mẫu 16 mới của một thành phẩm THAY TRỌN bản khai cũ của chính thành phẩm đó. Nguyên vật liệu chỉ có ở bản khai cũ mà bản mới đã bỏ thì hết hiệu lực. Trước đó luật ghép theo từng cặp (thành phẩm, NVL) — mỗi cặp lấy kỳ khai gần nhất của riêng nó.

**Ví dụ owner nêu:** thành phẩm A khai định mức 2022, 2023 không khai lại, 2025 khai bản mới. Kỳ 2022 và 2023 dùng bản 2022; kỳ 2025 dùng ĐÚNG bản 2025.

**Lý do:** ghép theo cặp tạo ra một định mức chưa từng được doanh nghiệp khai — trộn NVL của bản 2022 với NVL của bản 2025 thành một danh sách không tồn tại trên giấy tờ nào. Phát hiện dựng trên đó không giải trình được với doanh nghiệp.

**Đo trên dữ liệu 06/08/2026:** ghép theo cặp giữ thêm **774 cặp trên 126 mã thành phẩm**, ở 4 kỳ (DN 8/2025: 451 cặp / 51 mã · DN 10/2026: 302 / 58 · DN 10/2025: 19 / 15 · DN 10/2024: 2 / 2). Mười kỳ còn lại của pilot không đổi.

## 2026-08-06 — C3.3 so đơn vị tính của cả M16, không chỉ M15 với BCCT

**Quyết định:** Phạm vi C3.3 mở từ (M15 ↔ BCCT) thành (M15 ↔ M16 ↔ BCCT), đơn vị M16 lấy ở cột đơn vị tính của dòng định mức nguyên vật liệu. Mức giữ nguyên thang cũ: cùng đơn vị chuẩn bỏ qua · cùng họ quy đổi được Thông tin · khác họ hoặc không nhận dạng được Nghiêm trọng. Không thêm mã mới — đây vẫn là một câu hỏi "cùng mã vật tư có mấy đơn vị".

**Lý do:**
- Chị Duyên nêu ở đề xuất 16/06 (mục J8): đơn vị của cùng một nguyên vật liệu phải khớp giữa M16 và M15. Sổ yêu cầu ghi ở dòng 2.6.
- C4.3 nhân định mức với sản lượng rồi so với `xuất_sản_xuất` của M15. Hai vế lệch đơn vị thì kết quả sai đúng bằng hệ số quy đổi (kg vs gam là ×1000) mà không kiểm tra nào khác nhìn ra — C4.3 chỉ thấy một con số vượt ngưỡng.
- **Đo trên dữ liệu thật 06/08/2026:** sau khi quy về đơn vị chuẩn, **9 mã** có đơn vị M16 khác đơn vị M15 (5 ở DN 9/2025, 3 ở DN 12/2025, 1 ở DN 11/2024). Ngoài ra 131 cặp có đơn vị không tra được trong bảng đơn vị chuẩn; cặp nào hai bên ghi giống hệt nhau thì thang cũ đã coi là khớp, không phát sinh phát hiện.

## 2026-08-05 — C4.9 mới + định mức hiệu lực kế thừa giữa các kỳ + cổng độ phủ định mức trên C4.3

**Quyết định:** Thêm **C4.9** vào Nhóm 4 (danh mục 49 → 50, Giai đoạn I 33 → 34, 🚧 14 → 15): thành phẩm có sản xuất nhập kho trong kỳ mà không có định mức hiệu lực nào → liệt kê **từng mã**, không báo tổng. Đây là chiều M15a → M16, ngược với C4.2 (M16 → M15a); catalog cũ không có mã cho chiều này.

Kèm ba sửa đổi ngữ nghĩa C4.3 trong §4.1:
- **Định mức hiệu lực:** Mẫu 16 kế thừa giữa các kỳ, doanh nghiệp chỉ khai lại khi định mức thay đổi. Định mức áp cho kỳ N = bản khai có kỳ lớn nhất ≤ N của cùng cặp thành phẩm-NVL, gộp theo **sổ quyết toán** (ADR #19 bên mvp — mỗi sổ là ledger riêng, không cộng chéo). Trước đây lọc đúng `period_year == N` nên mã không khai lại thì mất định mức.
- **Nhường C4.1:** mã NVL có tiêu hao lý thuyết mà không có dòng nào trong M15 thuộc C4.1, C4.3 bỏ qua — không coi `xuất_sản_xuất` = 0 rồi bắn Nghiêm trọng.
- **Cổng độ phủ định mức:** có mã thành phẩm sản xuất trong kỳ mà chưa từng khai định mức ở bất kỳ kỳ nào → C4.3 trả *chưa đánh giá được* cho cả (doanh nghiệp, kỳ, sổ).

**Lý do:**
- Cả anh Dũng (2 bản ghi âm) lẫn chị Duyên (notes 05/08 và đề xuất 16/06, cách nhau 7 tuần) đều nêu luật kế thừa Mẫu 16. Anh Dũng gọi bảng liệt kê mã thiếu định mức là cốt lõi và dừng không đọc kết quả khi chưa có nó.
- **Kết quả "0 phát hiện" trên dữ liệu thiếu là kết quả giả.** Không có cổng thì thiếu định mức làm doanh nghiệp trông sạch hơn — ngược hẳn hướng phải đi.
- **Đo trên pilot (05/08/2026):** luật kế thừa xoá sạch 16/16 mã thiếu định mức cùng kỳ của DN 8/2025, và giải thích **0** cho DN 8/2024 lẫn toàn bộ DN 10 — luật tách đúng hai tình huống khác nhau, không phải luật làm mọi thứ biến mất. Trên DN 8/2025 nó đẩy 321/8.144 mã đổi bậc, 0 mã đi ngược. Áp cả hai cổng thì C4.3 còn 1.772/3.296 = 54% phát hiện, chỉ DN 8/2025 chạy được.
- **Cổng nhị phân, không ngưỡng phần trăm:** đề xuất ngưỡng 5% và thước tỷ trọng sản lượng đã bị bác. Thành phẩm chưa khai định mức thì không biết nó tiêu hao NVL nào, nên không khoanh được vùng ảnh hưởng — phải chặn cả nhóm chứ không nhiễm theo từng mã.

**Kèm theo — phạm vi C4.1 mở theo:** C4.3 nhường mã không có dòng M15 cho C4.1, nhưng C4.1 lọc đúng `period_year == year` nên không thấy mã có định mức kế thừa. Đo trên pilot 06/08/2026: **196 mã** rơi ra ngoài cả hai kiểm tra (188 ở DN 8/2025, 8 ở DN 10/2026). Phạm vi C4.1 thành hợp của (mã khai đúng kỳ) và (mã có tiêu hao lý thuyết > 0 theo định mức hiệu lực). Vẫn gắn với sản xuất trong kỳ, không mở thành "mọi mã từng khai". Sau khi sửa: khoảng hở = 0, C4.1 đi từ 36 lên 232 phát hiện trên 8 (DN, kỳ) pilot.

**Ràng buộc thực thi:**
- Kỳ sớm nhất của mỗi doanh nghiệp mặc định *chưa đánh giá được*, trừ khi cán bộ xác nhận đó đúng là năm đầu nộp BCQT (trường mới `companies.first_bcqt_year` bên mvp). Không phân biệt được "chưa từng khai" với "đã khai trước cửa sổ dữ liệu mình có".
- Trạng thái *chưa đánh giá được* phải bị loại khỏi điểm rủi ro ở **cả phần cộng điểm lẫn phần trần**. Chỉ bỏ phần cộng thì thiếu dữ liệu lại làm điểm đẹp lên.
- Trình tự: sửa đề án (xong) → mvp issue #56 và bảy ticket con #57–#63.

## 2026-07-24 — C4.3: số nhân định mức = sản lượng sản xuất, không phải xuất khẩu

**Quyết định:** §4.1 đổi công thức C4.3 từ `Σ(định_mức × xuất_khẩu_M15a)` sang `Σ(định_mức × sản_lượng_sản_xuất_M15a)`. Số nhân là lượng SP sản xuất nhập kho trong kỳ. Bổ sung bậc "mâu thuẫn vật lý" (tiêu hao lý thuyết > tồn đầu + nhập → Nghiêm trọng).

**Lý do:**
- **Đề án tự mâu thuẫn:** §4.1 (công thức) ghi xuất khẩu, nhưng kịch bản demo §6.3 ("TP_X **sản xuất** 1.000 cái... 5.000 kg cần tiêu hao... M15 xuất SX 4.000 kg") dùng sản lượng. Sửa để hợp nhất — không phải đổi ngữ nghĩa.
- **Cặp so sánh phải cùng biến cố:** C4.3 so với `xuất_sản_xuất` (NVL cấp cho sản xuất). Vế lý thuyết phải là NVL cần cho lượng **sản xuất** cùng kỳ. Dùng xuất khẩu tạo sai số đúng bằng biến động tồn thành phẩm (sản xuất ≠ bán), không phải tín hiệu tuân thủ.
- **Đo trên dữ liệu thật (3 DN pilot):** cơ sở xuất khẩu 2.371 finding → cơ sở sản xuất 2.063 (−13%); hai chiều lỗi đều sửa được (kỳ dồn tồn export giấu tiêu hao thật, kỳ rút tồn export fire khống). Chi tiết `audit-hq-pilot/notes/13` (P-07) + phiên đo 2026-07-24.

**Ràng buộc thực thi:**
- Cột số nhân **không có trong biểu chuẩn** — biểu Mẫu 15a chuẩn (HONG_AN, 002, 006) chỉ có một cột "nhập trong kỳ" = sản xuất (6) + khách trả lại (7). Chỉ 004 tách riêng. Dùng cột gộp làm proxy với giả định trả lại ≈ 0 (004 xác nhận (7)=0); với biểu tách thì loại (7).
- Ngưỡng bậc mâu thuẫn vật lý (đề xuất ≥2×) **chốt ở họp cán bộ** — chưa hard-code.
- Trình tự: sửa đề án (xong) → sửa `audit-hq-mvp/app/checks/c4_norm.py` (đổi số nhân + tách (6)/(7) ở extended resolver + skip mã không-nguồn nhường C4.1) + ADR bên mvp, chạy lại 6 DN demo + 3 pilot, giải thích từng finding đổi.

## 2026-05-13 — Người dùng: Cán bộ Hải quan (Chi cục)

**Quyết định:** Audit-HQ phục vụ cán bộ Hải quan tại đơn vị tiếp nhận **Chi Cục Hải Quan Khu vực IV**. Đề án không tách bạch phòng QLRR riêng — gọi chung "Hải quan" cho phù hợp ngôn ngữ Chi cục.

**Lý do:**
- Dữ liệu đầu vào (BCQT + TKXNK đa năm) là historical/batched, match nhu cầu pre-screen kiểm tra sau thông quan.
- "Kiểm soát rủi ro" map thẳng vào Luật Hải quan 2014 Điều 16-17 (quản lý rủi ro).
- Leverage cao: 10 cán bộ chọn 100 DN trong 10,000 để kiểm tra > 100 inspector dùng tool cho 1 DN.
- Bản v0.2 (2026-05-13): bỏ "phòng QLRR" cụ thể, tổng quát hoá thành "Hải quan" để đề án không cố định tổ chức nội bộ (Chi cục có thể tự cấu trúc).

---

## 2026-05-13 — MVP data: Excel-in (format chuẩn TT 39/2018), không tích hợp VNACCS DB

**Quyết định:** Phase 1 MVP nhận đầu vào dạng Excel có format chuẩn theo TT 39/2018 (Mẫu 15/15a/16 + BCCT). Không integrate VNACCS production DB.

**Lý do:**
- Match Path 2 của BCQT-System (đã proven).
- Mẫu 15/15a/16 nộp Hải quan theo format chuẩn TT 39/2018 — parser handle straightforward, có adapter cho biến thể nhẹ giữa DN.
- VNACCS DB integration phức tạp, để Phase 3 production.

---

## 2026-05-13 — Scope MVP: multi-DN × multi-year

**Quyết định:** MVP build cho 5 DN × 3-4 năm (15-20 DN-năm instances). Hỗ trợ cross-year continuity per DN. Cross-DN peer benchmarking defer Phase 2 (cần data HQ portfolio).

**Lý do:**
- Trọng Tín cung cấp seed data multi-DN multi-year → chicken-and-egg đã giải.
- Multi-year là differentiator vs BCQT-System (single-year per client) và Johnson (1 DN).
- Cross-DN bị chặn bởi sample bias (Trọng Tín data là DN đã clean, không đại diện DN gian lận).

---

## 2026-05-13 — Data flow: Trọng Tín seed, không bán data cho HQ

**Quyết định:** Trọng Tín cung cấp base data (đã anonymize) chỉ để build và demo tool. Khi HQ deploy production, hệ thống chạy trên data HQ tự thu thập (VNACCS, DN portal). Tinsu+Trọng Tín bán **TOOL**, không bán **DATA**.

**Lý do:**
- Tránh COI: Trọng Tín có DN khách hàng → không thể đồng thời cung cấp data DN cho HQ audit DN đó.
- Tránh vi phạm hợp đồng agency-DN (bí mật kinh doanh, Luật Sở hữu Trí tuệ Đ84).
- Tránh sample bias (Trọng Tín data = DN đã clean, không đại diện).

---

## 2026-05-13 — Codebase: repo riêng audit-hq, copy proven libs từ BCQT-System

**Quyết định:** Audit-HQ là repo độc lập, không phải fork hay extension của BCQT-System. Khi cần parser/config, copy file từ BCQT-System. Sau Phase 1 nếu cần shared, extract thành lib `tinsu-customs-core`.

**Lý do:**
- BCQT-System (1 agency, staff workflow, output forms) khác audit-hq (1 HQ, analyst workflow, output findings) về bản chất, không chỉ về mode.
- Fork sẽ tạo 2 codebase divergent maintain mãi.
- Copy-paste-then-extract = pain-driven refactor, không premature optimization.

---

## 2026-05-13 — Demo flow: γ multi-DN ranking + drill-down evidence

**Quyết định:** Demo 5-phút chạy theo flow: dashboard portfolio → top-N ranking → click DN → findings list → click finding → evidence trail panel-left/right.

**Lý do:**
- (α) single-DN deep-dive: không bán được cho HQ, BCQT-System đã làm rồi.
- (β) ranking trống evidence: HQ analyst không tin black-box risk score, không defensible khi đề xuất kiểm tra.
- (γ) ranking + drill-down evidence: defensible, dễ pitch, technical effort hợp lý.

---

## 2026-05-13 — Catalog 28 + 3 Phase 2 (đồng bộ BCQT showcase checklist v1.0)

**Quyết định (v0.2):** Đề án dùng catalog 28 checks theo cấu trúc 6 nhóm của BCQT showcase checklist (Nhóm 1-6) + bổ sung Nhóm 7 cross-DN (3 checks Phase 2). Tổng 31 checks. MVP build 15, W.I.P 13, Phase 2: 3.

**Lý do:**
- Showcase checklist đã được Tinsu chuẩn hoá với severity (🔴🟡🔵), ngưỡng cụ thể, refer Johnson 2025 case — pitch credibility cao hơn 36-category catalog tier-based ban đầu.
- 6 nhóm theo problem domain (intake / balance / classification / norms / traceability / multi-period) dễ navigate hơn tier A-F.
- Nhóm 7 cross-DN giữ là Phase 2 vì cần data HQ portfolio đa DN — chưa khả thi trong MVP synthetic.
- 15 MVP đủ demo 5-phút có signal, không quá tham vọng cho POC 4-6 tuần.

**Lịch sử:**
- v0.1: 36 categories tier A-F, MVP-15, W.I.P 18, Phase-2 3
- v0.2: 28 + 3 = 31 checks theo cấu trúc nhóm 1-7, MVP-15, W.I.P 13, Phase-2 3

---

## 2026-05-13 — Synthetic demo data (option P)

**Quyết định:** Demo data = synthetic injection trên base data Trọng Tín clean, không cố tìm raw pre-cleanup data của Trọng Tín.

**Lý do:**
- Tìm draft phiên bản pre-cleanup khó, agency không lưu trữ có hệ thống.
- Disclose rõ "synthetic, để show capability" với HQ — honesty defensible.

---

## 2026-05-13 — Pitch state (ii) + Deliverable (B) + Fastest

**Quyết định:** Đã pitch ý tưởng cho HQ, HQ quan tâm. Commit deliverable là live demo trên data anonymize. Timeline: fastest possible. Tận dụng codebase + AI Tinsu đã có.

---

## 2026-05-13 — Repo đề án vs repo code: tách bạch

**Quyết định:** Repo này (audit-hq trên TinsuAI) chỉ chứa đề án (markdown + HTML). MVP code thật sẽ tạo repo khác sau khi đề án approve.

**Lý do:**
- Tránh confuse scope.
- Repo đề án iterate nhiều với nội dung, không liên quan code.

---

## 2026-05-13 — Hosting: Docker nginx + Cloudflare Tunnel (no basic-auth từ v0.2)

**Quyết định:**
- URL: `https://audit-hq.tinsu.ai/` (zone `tinsu.ai` vì cert tunnel chỉ có quyền zone này, không phải `sgnai.dev`).
- Hosting: Tinsu VPS, container nginx:alpine bind `127.0.0.1:8757`, không cần sudo (user `tinsu` trong docker group).
- Public ingress: Cloudflare Tunnel `tinsu-online-server` (remotely-managed) — config add qua Cloudflare API (script `deploy/scripts/add-ingress.py`), không phải `/etc/cloudflared/config.yml` (file này bị remote override).
- Bảo vệ: **bỏ basic-auth từ v0.2** theo quyết định owner — draft đề án không nhạy cảm đến mức cần auth, dễ chia sẻ hơn. URL khó đoán đủ làm barrier.
- Workflow: manual `make publish` (scp HTML vào volume mount). Auto-deploy CI/CD defer Phase 2.

**Lý do:**
- Public URL cần để gửi reviewer ngoài tổ chức (HQ).
- Cloudflare Tunnel = TLS edge + DDoS protection miễn phí, không phải config Let's Encrypt.
- Docker = không sudo cho container, nhẹ, đồng bộ pattern app Tinsu khác.
- Tunnel remotely-managed (lesson learned trong session deploy): edit `/etc/cloudflared/config.yml` không có hiệu lực; phải PUT qua Cloudflare API.
- Basic-auth đủ cho draft (không phải fortress, chỉ là barrier).
- Manual publish nhanh hơn CI cho draft thay đổi liên tục.

---

## 2026-05-13 — LLM endpoint chung Tinsu

**Quyết định:** Khi audit-hq build code thật, dùng `codex-lb-demo.sgnai.dev` LLM proxy chung với data-hub, barry-CO.

**Lý do:** Đồng bộ infra, không spin up endpoint riêng.
