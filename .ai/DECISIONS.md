# DECISIONS — Audit-HQ

Log các quyết định quan trọng + lý do. Lock trong DRAFT v0.1 sau khi grill với owner.

---

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
