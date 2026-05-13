# Đề án: Audit-HQ

**Hệ thống hỗ trợ quản lý rủi ro & phát hiện sai phạm trong Báo cáo Quyết toán Hải quan (BCQT) và Tờ khai Xuất Nhập khẩu (TKXNK)**

> **Bản DRAFT v0.1** — 2026-05-13
> Tài liệu này sẽ trải qua nhiều vòng synthesize với feedback và input từ phía Hải quan. Mọi nội dung dưới đây là đề xuất sơ bộ, không phải cam kết cuối cùng.
>
> Soạn bởi: Tinsu AI × Trọng Tín
> Đối tượng tiếp nhận: Phòng/Cục Quản lý Rủi ro — Tổng cục Hải quan / Cục Hải quan

---

## 1. Tổng quan

### 1.1 Bối cảnh

Mỗi năm, các Doanh nghiệp chế xuất (DNCX) và Doanh nghiệp sản xuất xuất khẩu (DNSXXK) nộp lên Hải quan các bộ báo cáo quyết toán nguyên vật liệu — sản phẩm — định mức (Mẫu 15/BCQT-NVL, Mẫu 15a/BCQT-SP, Mẫu 16/ĐMTT theo TT 39/2018) cùng với toàn bộ lịch sử Tờ khai Xuất Nhập khẩu trong kỳ. Khối lượng dữ liệu rất lớn (mỗi DN cỡ hàng chục nghìn dòng TKXNK/năm, trải qua nhiều năm); việc rà soát thủ công không khả thi và phụ thuộc kinh nghiệm cán bộ.

Hiện tại phòng Quản lý Rủi ro (QLRR) lựa chọn DN để kiểm tra sau thông quan chủ yếu dựa trên:
- Tổng quy mô kim ngạch
- Loại hình hoạt động (DNCX, gia công)
- Kinh nghiệm/cảm tính cán bộ

Cách tiếp cận này bỏ sót DN có sai phạm tinh vi nhưng quy mô vừa, đồng thời tốn nguồn lực kiểm tra các DN tuân thủ tốt.

### 1.2 Mục tiêu

Xây dựng hệ thống Audit-HQ giúp phòng QLRR:

1. **Phát hiện sai phạm có thể** từ BCQT + TKXNK đã nộp, bằng phân tích đa chiều (số học, đối chiếu chéo nguồn, liên năm, liên DN).
2. **Xếp hạng DN theo rủi ro**, cung cấp evidence trail truy ngược về dòng dữ liệu gốc để cán bộ có cơ sở giải trình khi đề xuất kiểm tra.
3. **Mở rộng catalog rule-based detection** theo thời gian khi cán bộ QLRR phát hiện pattern mới.

### 1.3 Đối tượng người dùng

| Vai trò | Hành động chính | Tần suất |
|---|---|---|
| Analyst phòng QLRR | Browse top-N DN rủi ro, drill-down findings, xuất báo cáo kiến nghị kiểm tra | Hằng tuần — hằng quý |
| Trưởng phòng QLRR | Duyệt báo cáo kiến nghị, phân công | Hằng tuần |
| Cán bộ KTSTQ *(Phase 2)* | Sử dụng evidence trail audit-hq trong quá trình kiểm tra thực tế | Theo case |

> **Phạm vi đề án này:** Analyst phòng QLRR là người dùng chính. Vai trò KTSTQ là roadmap Phase 2.

### 1.4 Cơ sở pháp lý tham chiếu

- Luật Hải quan 2014, Điều 16-17 (Áp dụng quản lý rủi ro)
- TT 38/2015/TT-BTC, sửa đổi bởi TT 39/2018/TT-BTC, hiện hành tham chiếu TT 121/2025/TT-BTC
- QĐ 1357/QĐ-TCHQ ngày 18/05/2021 (Mã loại hình XNK)
- Luật Quản lý Thuế 2019, Điều 99 (Bí mật thông tin người nộp thuế)
- Nghị định 13/2023/NĐ-CP (Bảo vệ dữ liệu cá nhân)

---

## 2. Nguyên tắc thiết kế

### 2.1 Risk-based, không phải compliance-based

Hệ thống không kiểm tra toàn bộ DN — chỉ rank theo rủi ro để cán bộ phân bổ nguồn lực kiểm tra đúng chỗ. Phù hợp tinh thần "quản lý rủi ro" của Luật Hải quan 2014.

### 2.2 Evidence trail — không black-box

Mỗi finding hệ thống đưa ra phải:
- Trace về dòng dữ liệu cụ thể trong BCCT/Mẫu (số TK, dòng hàng, mã NPL/SP)
- Nêu rõ điều khoản pháp lý liên quan
- Cho phép cán bộ defendsible khi báo cáo cấp trên hoặc đối thoại với DN

Mọi rule detection đều rule-based và deterministic. AI/LLM chỉ dùng cho:
- Khớp tên material fuzzy (translation/normalization)
- Sinh giải thích plain Vietnamese cho finding
- Đề xuất mapping mã (gợi ý, không tự quyết)

### 2.3 Catalog mở rộng được

Mỗi loại sai phạm = 1 plugin Python "CheckSpec". Thêm rule mới = thêm 1 file, không sửa core. Cán bộ QLRR (qua phối hợp Tinsu) có thể đề xuất rule mới theo case nghiệp vụ phát hiện.

### 2.4 Adapter cho data heterogeneity

Mỗi DN nộp Excel theo format khác nhau (có agency hỗ trợ, không có agency, ERP khác nhau, mức chuẩn hoá khác nhau). Hệ thống có lớp adapter (YAML config + Python hooks tuỳ chọn) cho mỗi DN, tách bạch với core logic.

### 2.5 Defensible với rủi ro pháp lý

- Anonymization layer cho dữ liệu demo (bảo vệ bí mật DN trong giai đoạn POC)
- Audit log đầy đủ thao tác cán bộ
- Không thay đổi dữ liệu gốc — mọi annotation/finding là lớp phủ tách biệt

---

## 3. Phạm vi MVP

### 3.1 Đầu vào

| Loại dữ liệu | Định dạng | Nguồn | Phạm vi MVP |
|---|---|---|---|
| Mẫu 15 (BCQT-NVL) | Excel | DN nộp HQ qua hệ thống xử lý dữ liệu điện tử | 5 DN × 3-4 năm |
| Mẫu 15a (BCQT-SP) | Excel | DN nộp | 5 DN × 3-4 năm |
| Mẫu 16 (ĐMTT) | Excel | DN nộp | 5 DN × 3-4 năm |
| BCCT TKXNK | Excel | Export VNACCS hoặc DN tự lập tổng hợp | 5 DN × 3-4 năm |

> **TBD — cần Tinsu/HQ xác nhận:** Format Mẫu 15/15a/16 thực tế HQ nhận có chuẩn hoá hay từng DN có biến thể? Trong MVP đầu, giả định theo format quy định TT 39/2018.

### 3.2 Đầu ra

Cho mỗi DN trong portfolio:
- Findings list (mỗi finding có severity, category, evidence pointers, đề xuất hành động)
- Risk score tổng hợp (explainable — derive từ findings, không ML)
- Báo cáo Excel kiến nghị kiểm tra (xuất khi cán bộ duyệt)

Toàn portfolio:
- Dashboard ranked top-N DN theo risk score
- Filter theo ngành, kim ngạch, loại hình

### 3.3 Phạm vi xử lý

- **Đơn vị tenant:** 1 deployment phục vụ 1 phòng QLRR (tối đa 1 Cục)
- **Quy mô MVP:** 5 DN × 3-4 năm dữ liệu (= 15-20 DN-năm instance)
- **Quy mô Pilot dự kiến:** 50-200 DN, 5 năm dữ liệu
- **Quy mô Production:** Tất cả DNCX/DNSXXK trong phạm vi Cục, 10 năm dữ liệu

---

## 4. Catalog phát hiện sai phạm (36 categories)

Catalog tổng hợp 36 loại sai phạm có thể phát hiện được với data shape BCCT + Mẫu 15/15a/16. Được phân thành 6 tier theo data requirement.

> **MVP đánh dấu ✅ — Build & demo trong giai đoạn POC**
> **W.I.P đánh dấu 🚧 — Có trong catalog, chưa implement, sẽ build trong Pilot**
> **P2 đánh dấu ⏳ — Phase 2, cần dữ liệu HQ portfolio đa DN**

### Tier A — Kiểm tra số học nội bộ Mẫu (single-year, single-DN)

| # | Category | Cơ sở pháp lý | Status |
|---|---|---|---|
| 1 | Mẫu 15 balance equation broken: (5)+(6)−(7)−(8)−(9)−(10) ≠ (11) | TT 39/2018 Đ60 | ✅ MVP |
| 2 | Mẫu 15a balance equation broken | TT 39/2018 | 🚧 W.I.P |
| 3 | Tồn âm trong kỳ (per material per tháng) | TT 38/2015 | 🚧 W.I.P |
| 4 | Cột 10 "xuất khác" tỷ lệ bất thường (>5% lưu lượng) | TT 39/2018 | ✅ MVP |
| 5 | Cột 7 "xuất trả" outlier giữa các năm | TT 39/2018 | 🚧 W.I.P |
| 6 | Cột 8 "chuyển MĐSD" outlier — khả năng chuyển nội địa không khai thuế | TT 38/2015 Đ25 | 🚧 W.I.P |
| 7 | NVL trong Mẫu nhưng 0 nhập BCCT → mua nội địa ẩn / phantom | TT 39/2018 | 🚧 W.I.P |

### Tier B — Đối chiếu chéo nguồn (BCCT ↔ Mẫu), single-year

| # | Category | Cơ sở pháp lý | Status |
|---|---|---|---|
| 8 | BCCT nhập E11/E13 > Mẫu 15 cột (6) → under-report import ⭐ | TT 39/2018 | ✅ MVP |
| 9 | Mẫu 15a xuất > BCCT xuất E42/E62 → over-claim export | TT 39/2018 | ✅ MVP |
| 10 | Mã BCCT không xuất hiện trong Mẫu → hidden material | TT 39/2018 | 🚧 W.I.P |
| 11 | NVL trong Mẫu, 0 dòng BCCT (cả nhập lẫn xuất) → phantom | TT 39/2018 | 🚧 W.I.P |
| 12 | UOM mismatch BCCT vs Mẫu cùng material | TT 39/2018 | 🚧 W.I.P |
| 13 | HS chapter mismatch BCCT vs Mẫu | QĐ 1357 | 🚧 W.I.P |
| 14 | Tên material BCCT vs Mẫu fuzzy similarity <70% | TT 39/2018 | ✅ MVP |

### Tier C — Cross-form (Mẫu 15 ↔ 15a ↔ 16), single-year

| # | Category | Cơ sở pháp lý | Status |
|---|---|---|---|
| 15 | NVL trong Mẫu 16 không có trong Mẫu 15 list | TT 39/2018 | ✅ MVP |
| 16 | NVL trong Mẫu 15 tiêu hao nhưng không có norm Mẫu 16 | TT 39/2018 | 🚧 W.I.P |
| 17 | TP trong Mẫu 15a sản xuất nhưng không có trong Mẫu 16 | TT 39/2018 | 🚧 W.I.P |
| 18 | Tính ngược: Σ(Mẫu 16 norm × Mẫu 15a output) ≠ Mẫu 15 cột (9) ⭐ | TT 39/2018 | ✅ MVP |

### Tier D — Anomaly patterns nội tại, single-year

| # | Category | Cơ sở pháp lý | Status |
|---|---|---|---|
| 19 | Mẫu 16 norm outlier nội bộ DN (CV>0.3 hoặc max/min>2 cùng cặp NVL-TP) | TT 39/2018 | ✅ MVP |
| 20 | E11 + E13 cùng material → khai trùng loại hình | QĐ 1357 | ✅ MVP |
| 21 | Giao dịch BCCT đơn lẻ lớn bất thường (>3σ trong cùng HS) | Phân tích | 🚧 W.I.P |
| 22 | Số TK BCCT trùng lặp | TT 39/2018 | 🚧 W.I.P |
| 23 | Cluster declaration dates cuối kỳ/năm → khai gộp dồn cuối | TT 38/2015 Đ4 | ✅ MVP |
| 24 | Roundtripping: NVL cùng mã nhập + xuất cùng kỳ → sham import | TT 38/2015 | ✅ MVP |

### Tier E — Multi-year per DN

| # | Category | Cơ sở pháp lý | Status |
|---|---|---|---|
| 25 | Tồn cuối kỳ N ≠ tồn đầu N+1 (per material) ⭐ | TT 39/2018 | ✅ MVP |
| 26 | Code re-mapping: rename material year-to-year (fuzzy description match) ⭐⭐⭐ | TT 38/2015 | ✅ MVP |
| 27 | HS code drift: cùng material/mô tả, HS code khác giữa các năm ⭐⭐ | QĐ 1357 | ✅ MVP |
| 28 | Norm drift YoY: norm Mẫu 16 thay đổi >X% giữa năm không justification | TT 39/2018 | ✅ MVP |
| 29 | Phantom code: xuất hiện 1 năm rồi biến mất không có closure | TT 39/2018 | 🚧 W.I.P |
| 30 | Volume spike: HS code đột ngột nhảy bậc volume giữa năm | Phân tích | 🚧 W.I.P |
| 31 | Tỷ lệ scrap (cột 10/tổng) outlier YoY | TT 39/2018 | 🚧 W.I.P |
| 32 | Material name fuzzy similarity across "different" codes cùng năm | Phân tích | 🚧 W.I.P |
| 33 | New material code với opening stock > 0 mà năm trước không có | TT 39/2018 | 🚧 W.I.P |

### Tier F — Cross-DN peer (Phase 2 — cần data HQ portfolio)

| # | Category | Cơ sở pháp lý | Status |
|---|---|---|---|
| 34 | Peer norm outlier (same HS chapter, DN norm > Xσ peer mean) | TT 39/2018 | ⏳ P2 |
| 35 | Same supplier price drift across DN — transfer pricing flag | Luật Quản lý Thuế 2019 | ⏳ P2 |
| 36 | Same HS code volume relative outlier vs ngành | Phân tích | ⏳ P2 |

**Tổng:** 36 categories | MVP build: 15 | W.I.P: 18 | Phase 2: 3

> **Đề án mở rộng:** Catalog không cố định 36. Mỗi case nghiệp vụ HQ phát hiện mới (Tinsu phối hợp) thêm vào catalog dạng plugin, không cần thay đổi core.

---

## 5. Kiến trúc hệ thống (sơ bộ)

### 5.1 Mô hình dữ liệu

3 layers + 1 risk layer (mở rộng từ kiến trúc BCQT-System đã proven):

```
Layer 0 — Files          : Excel gốc DN nộp, immutable, metadata only
Layer 1 — Parsed/Resolved: Schema chuẩn, dn_id là first-class key
   ├── customs_declarations    (BCCT lines)
   ├── form15_lines            (NVL balance)
   ├── form15a_lines           (TP balance)
   └── form16_norms            (BOM norms)
Layer 2 — Findings       : Output của CheckSpec, link về Layer 1 evidence
   ├── findings              (per-DN, per-rule)
   ├── annotations           (cán bộ đánh dấu, không thay đổi Layer 1)
   └── traceback_pointers    (link findings → dòng cụ thể trong BCCT/Mẫu)
Layer 3 — Risk           : Aggregation từ Layer 2
   ├── dn_risk_scores
   └── ranking_views
```

> **Nguyên tắc "store separately, query together":** mỗi nguồn giữ schema gốc, query thuật toán đan chéo. Không ép vào một bảng vạn năng.

### 5.2 Tech stack (đề xuất)

| Layer | Công nghệ | Lý do |
|---|---|---|
| Backend | Python 3.12 + FastAPI + Jinja2 | Tái sử dụng từ BCQT-System (đã proven) |
| Database | SQLite (MVP) → PostgreSQL (Pilot+) | SQLite đủ cho 5 DN, không vận hành; Postgres khi scale |
| Excel parsing | pandas + openpyxl + xlrd | TT 39/2018 mẫu BCQT .xlsx, BCCT VNACCS .xls |
| LLM | OpenAI-compatible client → endpoint Tinsu | Đồng bộ stack data-hub, barry-CO |
| Frontend | Server-rendered HTML + HTMX | Đơn giản, không SPA, dễ vận hành |
| Deploy | Docker Compose + GitHub Actions | Đồng bộ pattern data-hub, barry-CO-main |

> **TBD — cần Tinsu xác nhận:** Auth provider (built-in session vs SSO HQ). MVP đề xuất built-in.

### 5.3 Vai trò LLM trong audit-hq

LLM **không** làm detection. LLM làm những việc sau:

| Use case | Khi nào trigger | Output |
|---|---|---|
| Material name normalization | Khi parse BCCT/Mẫu, gặp mô tả lộn xộn | Canonical form, draft cho cán bộ confirm |
| Fuzzy code re-mapping (rule #26) | Khi confidence rule-based <80% | Đề xuất mapping, draft |
| Plain-VN explanation cho finding | Khi cán bộ click vào finding | Diễn giải dễ đọc dùng template + LLM fill |
| Mã loại hình suggestion | Khi gặp mã không có trong QĐ 1357 | Cảnh báo + đề xuất tra cứu |

> **Endpoint:** Sử dụng LLM proxy nội bộ Tinsu (đã có sẵn cho data-hub, barry-CO).

---

## 6. Demo plan (POC)

### 6.1 Demo data composition

5 DN synthetic, mỗi DN 3-4 năm:

| Mã DN | Ngành | Loại hình | Số năm | Findings được inject |
|---|---|---|---|---|
| DN_001 | Điện tử (HS 85) | DNCX (E11/E42) | 4 | #1, #4, #25, #26 |
| DN_002 | Cơ khí (HS 84) | DNCX (E11/E42) | 3 | #8, #14, #20, #27 |
| DN_003 | Dệt may (HS 61) | DNSXXK (E31/E62) | 4 | #18, #28, #19 |
| DN_004 | Hoá chất (HS 39) | DNCX | 3 | #9, #23, #24 |
| DN_005 | Cơ khí (HS 84) | DNCX | 3 | (clean — kiểm chứng audit-hq không flag bừa) |

> **TBD — cần Trọng Tín cung cấp:** template base data từ 5 client thực tế (đã anonymize). Phương án (P) synthetic injection trên base data sạch.

### 6.2 Anonymization

| Trường ẩn | Cách thay |
|---|---|
| Tên DN | DN_001 ... DN_005 |
| MST | 4-digit random sequence |
| Tên cá nhân | "Cán bộ A", "Đại diện DN" |
| Tên NCC | SUP_001 ... |
| Địa chỉ | Tỉnh giả định |

| Trường giữ | Lý do |
|---|---|
| HS code | Cần cho finding #27 HS drift, #13 chapter mismatch |
| Mã loại hình (E11/E13/E42...) | Core data, không nhạy cảm |
| Tên material | Cần fuzzy match #14, #26; thay bằng generic name + variant |
| Số lượng/giá trị | Cần cho outlier detection; có thể scale ×constant |

### 6.3 Demo flow 5 phút

```
0:00 — Đăng nhập analyst QLRR → Dashboard portfolio 5 DN
0:30 — Top-5 ranked theo risk score:
         #1 DN_001 (risk 87) — 4 critical findings
         #2 DN_002 (risk 76) — 3 critical findings
         #3 DN_004 (risk 68)
         #4 DN_003 (risk 54)
         #5 DN_005 (risk 12) — clean
1:00 — Click DN_001 → DN detail page
         Tabs: Findings | Multi-year view | BCCT raw | Mẫu 15/15a/16
1:30 — Click finding "Code re-mapping suspected (rule #26)"
         Panel trái: 3 mã NVL năm 2023 + mô tả
         Panel phải: 3 mã NVL năm 2024 + mô tả tương tự (>85% fuzzy)
         Note: "Khả năng cao cùng material, DN đổi mã giữa 2023 và 2024"
2:30 — Click finding "Σ(norm × output) ≠ consumption (rule #18)"
         Hiển thị bảng: TP_X sản xuất 1,000 cái, norm Mẫu 16 = 5kg/cái
                                  Expected Mẫu 15 cột (9): 5,000kg
                                  Actual Mẫu 15 cột (9): 4,000kg
                                  Chênh: 1,000kg NVL "biến mất"
3:30 — Click "Cộng đồng so sánh" → "Tính năng Phase 2: cần data portfolio HQ"
4:00 — Click "Xuất báo cáo kiến nghị kiểm tra" → Excel có:
         + Danh sách 4 findings
         + Evidence dump (dòng BCCT cụ thể)
         + Trích yếu pháp lý
4:30 — Quay lại dashboard, click DN_005 (risk 12) → 0 critical findings
         "Audit-hq không cứ là flag bừa — DN tốt vẫn được xếp hạng thấp"
5:00 — End.
```

---

## 7. Lộ trình triển khai

### 7.1 Phase 1 — POC Demo (timeframe đề xuất: 4-6 tuần)

| Tuần | Mục tiêu | Deliverable |
|---|---|---|
| W1 | Repo + CI/CD + base architecture | Skeleton chạy được, copy parser/config từ BCQT-System |
| W2 | Parser Excel (Mẫu 15/15a/16 + BCCT) + Data Model Layer 0-1 | Có thể ingest 1 DN, query được |
| W3 | Implement MVP-10 finding categories đầu | Findings hiển thị, evidence trail working |
| W4 | Implement MVP-15 đầy đủ + risk scoring | Dashboard + ranking |
| W5 | Synthetic data 5 DN × 3-4 năm + anonymization | Demo data hoàn chỉnh |
| W6 | Polish UI + demo rehearsal + đóng gói | Pitch-ready |

### 7.2 Phase 2 — Pilot tại 1 Cục (timeframe đề xuất: 3-6 tháng sau POC approve)

- Triển khai 1 Cục thực tế (TBD: Hải quan Bắc Ninh? TPHCM? Theo lựa chọn HQ)
- Ingest data DN trong Cục (real, không synthetic)
- Cán bộ QLRR dùng thực tế, feedback loop
- Implement 18 W.I.P findings còn lại
- Bắt đầu seed cross-DN peer benchmarking (Tier F)

### 7.3 Phase 3 — Production (timeframe đề xuất: 12+ tháng)

- Mở rộng nhiều Cục
- Tích hợp trực tiếp VNACCS DB (không qua Excel export)
- API HQ cho DN portal nộp trực tiếp structured
- Implement Tier F đầy đủ (peer, supplier, volume cross-DN)
- ML-augmented detection (sau khi có >3 năm operational data)

### 7.4 Vai trò các bên

| Bên | Phase 1 (POC) | Phase 2 (Pilot) | Phase 3 (Production) |
|---|---|---|---|
| Tinsu AI | Build tool, demo data | Maintenance, R&D rule mới | Operate, scale |
| Trọng Tín | Cung cấp domain expertise, base data anonymize | Liên hệ HQ, đào tạo analyst | Consulting nghiệp vụ |
| HQ | Sponsor đề án, feedback design | Cung cấp data Cục, cán bộ QLRR dùng thử | Customer chính thức |

> **Lưu ý quan trọng:** Data của Trọng Tín chỉ dùng để **build và demo công cụ**. Khi HQ deploy production, hệ thống sử dụng data của HQ. Trọng Tín không chuyển dữ liệu khách hàng sang HQ ngoài bối cảnh DN đó tự nộp BCQT.

---

## 8. Câu hỏi mở cho phía Hải quan

Đây là các nội dung cần feedback HQ trước khi finalize đề án và xây dựng MVP.

### 8.1 Về phạm vi nghiệp vụ

1. Audit-HQ phục vụ Tổng cục hay Cục cụ thể? Có Cục nào đang được chọn làm pilot không?
2. Trong 36 categories đề xuất, HQ có quan tâm category nào hơn hoặc miss category nào quan trọng?
3. Output Excel kiến nghị kiểm tra có cần format theo mẫu chính thức nào không?
4. Phòng QLRR hiện đang dùng tool/quy trình nào để chọn DN kiểm tra? Audit-HQ tích hợp hay thay thế?

### 8.2 Về dữ liệu

5. HQ hiện lưu trữ Mẫu 15/15a/16 ở dạng cấu trúc nào — structured DB, Excel attachments, hay PDF? (Liên quan tới adapter Phase 2)
6. TKXNK lấy từ VNACCS có thể export Excel theo cấu trúc thống nhất, hay từng Cục có biến thể?
7. Quyền truy cập data đa năm của QLRR: hệ thống VCIS-VNACCS đã cho phép query trực tiếp, hay phải xin từng năm?

### 8.3 Về kỹ thuật & vận hành

8. Hệ thống deploy on-premise của HQ hay cloud (Tinsu host)? Yêu cầu bảo mật cụ thể?
9. HQ có yêu cầu chứng nhận an toàn thông tin (ATTT) cấp nào?
10. SLA cần cho Pilot/Production?
11. Cán bộ QLRR có kỹ năng tin học mức nào? Cần đào tạo bao nhiêu?

### 8.4 Về pháp lý & ranh giới

12. Audit-HQ phát hiện sai phạm chỉ là *gợi ý*, không phải kết luận điều tra. Đồng ý cách dùng này?
13. Trường hợp DN khiếu nại kết quả audit-hq, HQ có cần Tinsu hỗ trợ giải trình kỹ thuật không?
14. Quyền sở hữu trí tuệ catalog rule: thuộc HQ, Tinsu, hay shared?

---

## 9. Phụ lục

### 9.1 Glossary

| Thuật ngữ | Định nghĩa |
|---|---|
| BCQT | Báo cáo Quyết toán |
| BCCT | Báo cáo Chi tiết (TKXNK tổng hợp) |
| TKXNK | Tờ khai Xuất Nhập khẩu |
| DNCX | Doanh nghiệp Chế xuất |
| DNSXXK | Doanh nghiệp Sản xuất Xuất khẩu |
| QLRR | Quản lý Rủi ro |
| KTSTQ | Kiểm tra Sau Thông quan |
| NVL | Nguyên Vật Liệu |
| TP | Thành Phẩm |
| BTP | Bán Thành Phẩm |
| Mẫu 15 | Báo cáo cân đối NVL (BCQT-NVL) |
| Mẫu 15a | Báo cáo cân đối TP (BCQT-SP) |
| Mẫu 16 | Định mức thực tế (ĐMTT) |
| VNACCS | Hệ thống thông quan tự động VN |
| HS code | Mã hài hoà mô tả hàng hoá quốc tế |

### 9.2 Tham chiếu

- TT 38/2015/TT-BTC, TT 39/2018/TT-BTC, TT 121/2025/TT-BTC
- QĐ 1357/QĐ-TCHQ ngày 18/05/2021
- Luật Hải quan 2014, Luật Quản lý Thuế 2019, Luật Sở hữu Trí tuệ
- BCQT-System (Tinsu AI) — kiến trúc, parser, adapter pattern
- Johnson BCQT 2025 (Tinsu AI × Trọng Tín × Johnson) — Phase 3 audit tests làm cơ sở rule catalog

### 9.3 Changelog

| Version | Ngày | Tác giả | Thay đổi |
|---|---|---|---|
| v0.1-DRAFT | 2026-05-13 | Tinsu AI | Bản đầu — chờ vòng feedback đầu tiên |

---

> **Đây là bản DRAFT v0.1.** Mọi nội dung là đề xuất sơ bộ và sẽ được điều chỉnh theo feedback và input từ phía Hải quan qua các vòng synthesize tiếp theo.
