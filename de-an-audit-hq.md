# Đề án: Audit-HQ

**Hệ thống hỗ trợ quản lý rủi ro & phát hiện sai phạm trong Báo cáo Quyết toán Hải quan (BCQT) và Tờ khai Xuất Nhập khẩu (TKXNK)**

> **Bản DRAFT v0.2** — 2026-05-13
> Tài liệu sẽ trải qua nhiều vòng synthesize với feedback và input từ Hải quan. Mọi nội dung dưới đây là đề xuất sơ bộ, không phải cam kết cuối cùng.
>
> Soạn bởi: Tinsu AI × Trọng Tín
> **Đơn vị tiếp nhận:** Chi Cục Hải Quan Khu vực IV

---

## 1. Tổng quan

### 1.1 Bối cảnh

Mỗi năm, các doanh nghiệp chế xuất (DNCX), doanh nghiệp gia công, và doanh nghiệp sản xuất xuất khẩu (SXXK) nộp Hải quan bộ báo cáo quyết toán nguyên vật liệu — sản phẩm — định mức (Mẫu 15/BCQT-NVL, Mẫu 15a/BCQT-SP, Mẫu 16/ĐMTT theo TT 39/2018) cùng với toàn bộ lịch sử Tờ khai Xuất Nhập khẩu trong kỳ. Khối lượng dữ liệu rất lớn (mỗi DN cỡ hàng chục nghìn dòng TKXNK/năm, trải qua nhiều năm); việc rà soát thủ công không khả thi và phụ thuộc kinh nghiệm cán bộ.

Hiện tại Hải quan lựa chọn DN để kiểm tra sau thông quan chủ yếu dựa trên:
- Tổng quy mô kim ngạch
- Loại hình hoạt động (DNCX, gia công, SXXK)
- Kinh nghiệm/cảm tính cán bộ

Cách tiếp cận này có thể bỏ sót DN có sai phạm tinh vi nhưng quy mô vừa, đồng thời tốn nguồn lực kiểm tra các DN tuân thủ tốt.

### 1.2 Mục tiêu

Xây dựng hệ thống Audit-HQ giúp Hải quan:

1. **Phát hiện sai phạm khả năng** từ BCQT + TKXNK đã nộp, bằng phân tích đa chiều (số học nội bộ Mẫu, đối chiếu chéo nguồn, định mức M16, truy nguồn NVL, liên năm, liên DN).
2. **Xếp hạng DN theo rủi ro**, cung cấp evidence trail truy ngược về dòng dữ liệu gốc để cán bộ có cơ sở giải trình khi đề xuất kiểm tra.
3. **Mở rộng catalog rule-based detection** theo thời gian khi cán bộ phát hiện pattern mới qua thực tế nghiệp vụ.

### 1.3 Đối tượng người dùng

| Vai trò | Hành động chính | Tần suất |
|---|---|---|
| Cán bộ Hải quan | Browse DN trong portfolio, drill-down findings, xuất báo cáo kiến nghị kiểm tra | Hằng tuần — hằng quý |
| Cấp quản lý | Duyệt báo cáo kiến nghị, phân công | Hằng tuần |
| Cán bộ kiểm tra sau thông quan *(Phase 2)* | Sử dụng evidence trail audit-hq trong quá trình kiểm tra thực tế | Theo case |

### 1.4 Cơ sở pháp lý tham chiếu

- Luật Hải quan 2014, Điều 16-17 (Áp dụng quản lý rủi ro)
- TT 38/2015/TT-BTC, sửa đổi bởi TT 39/2018/TT-BTC, tham chiếu TT 121/2025/TT-BTC
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
- Cho phép cán bộ defensible khi báo cáo cấp trên hoặc đối thoại với DN

Mọi rule detection đều rule-based và deterministic. AI/LLM chỉ dùng cho:
- Chuẩn hoá tên material fuzzy (translation/normalization)
- Sinh giải thích plain Vietnamese cho finding
- Đề xuất mapping mã (gợi ý, không tự quyết)

### 2.3 Catalog mở rộng được

Mỗi loại sai phạm = 1 plugin Python "CheckSpec". Thêm rule mới = thêm 1 file, không sửa core. Cán bộ Hải quan (qua phối hợp Tinsu) có thể đề xuất rule mới theo case nghiệp vụ phát hiện.

### 2.4 Ngưỡng có thể điều chỉnh

Hệ thống đề xuất ngưỡng mặc định cho mỗi rule (Critical/Warning/Info). Hải quan có toàn quyền điều chỉnh ngưỡng theo thực tế nghiệp vụ, theo loại hình DN, hoặc theo ngành hàng.

### 2.5 Defensible với rủi ro pháp lý

- Anonymization layer cho dữ liệu demo (bảo vệ bí mật DN trong giai đoạn POC)
- Audit log đầy đủ thao tác cán bộ
- Không thay đổi dữ liệu gốc — mọi annotation/finding là lớp phủ tách biệt

---

## 3. Phạm vi MVP

### 3.1 Đầu vào

| Loại dữ liệu | Định dạng | Nguồn | Phạm vi MVP |
|---|---|---|---|
| Mẫu 15 (BCQT-NVL) | Excel có format chuẩn (theo TT 39/2018) | DN nộp qua hệ thống xử lý dữ liệu điện tử | 5 DN × 3-4 năm |
| Mẫu 15a (BCQT-SP) | Excel có format chuẩn | DN nộp | 5 DN × 3-4 năm |
| Mẫu 16 (ĐMTT) | Excel có format chuẩn | DN nộp | 5 DN × 3-4 năm |
| BCCT TKXNK | Excel export từ VNACCS (hoặc DN tổng hợp) | Hệ thống Hải quan | 5 DN × 3-4 năm |

> **Đầu vào BCQT là Excel có format chuẩn** theo TT 39/2018 — không phải free-form. Hệ thống parser xử lý format chuẩn được, đồng thời có adapter cho biến thể nhẹ giữa các DN.

### 3.2 Đầu ra

Cho mỗi DN trong portfolio:
- Findings list (mỗi finding có severity 🔴/🟡/🔵, category, evidence pointers, đề xuất hành động)
- Risk score tổng hợp (explainable — derive từ findings, không ML)
- Báo cáo Excel kiến nghị kiểm tra (xuất khi cán bộ duyệt)

Toàn portfolio:
- Dashboard ranked top-N DN theo risk score
- Filter theo ngành, kim ngạch, loại hình

### 3.3 Phạm vi xử lý

- **Đơn vị triển khai:** 1 deployment phục vụ 1 đơn vị Hải quan (cấp Chi cục)
- **Quy mô MVP:** 5 DN × 3-4 năm dữ liệu (= 15-20 DN-năm instance)
- **Quy mô Pilot dự kiến:** 50-200 DN, 5 năm dữ liệu
- **Quy mô Production:** Tất cả DNCX/Gia công/SXXK trong phạm vi quản lý, 10 năm dữ liệu

---

## 4. Catalog các kiểm tra

> **Tổng:** 28 check (6 nhóm chính) + 3 check cross-DN (Phase 2 — cần dữ liệu HQ portfolio).
>
> **Trạng thái:**
> - ✅ MVP — Build & demo trong POC (15 check)
> - 🚧 W.I.P — Có trong catalog, chưa implement, sẽ build trong Pilot (13 check)
> - ⏳ P2 — Phase 2, cần dữ liệu HQ portfolio đa DN (3 check)
>
> **Mức độ:** 🔴 Critical · 🟡 Warning · 🔵 Info

### 4.0 Loại hình tờ khai theo loại hình doanh nghiệp

| Loại hình DN | Tờ khai nhập | Tờ khai xuất |
|---|---|---|
| **DNCX** — Doanh nghiệp chế xuất | E11, E15, E13 | E42 |
| **Gia công** — Gia công cho thương nhân nước ngoài | E21, E23 | E52, E54 |
| **SXXK** — Sản xuất xuất khẩu | E31, E33 | E62 |

> Tái xuất: B13 áp dụng chung. Chuyển mục đích sử dụng: A42 khi chuyển nội địa.

### Nhóm 1 — Số lượng nhập/xuất (6 checks)

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C1.1** | Lệch số lượng nhập NVL (M15 vs HQ) — `nhap_trong_ky` ≠ Σ tờ khai nhập theo mã. Loại hình: DNCX E11+E15 / GC E21+E23 / SXXK E31+E33. Ngưỡng: <5% Info · 5–20% Warning · >20% Critical. Rủi ro: Khai thiếu/thừa nhập khẩu. | 🟡 | ✅ |
| **C1.2** | Có TK nhập HQ nhưng không có trong M15 — Mã có trên BCCT nhưng không có dòng trong M15. Flag tất cả. Rủi ro: Bỏ sót NVL khỏi BCQT. | 🔴 | ✅ |
| **C1.3** | Có trong M15 nhưng không có TK HQ — `nhap_trong_ky` > 0 nhưng không có tờ khai tương ứng. Rủi ro: M15 không có căn cứ TK — có thể NVL nội địa bị đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C1.4** | Lệch số lượng xuất TP (M15a vs HQ) — `xuat_khau` ≠ Σ TK xuất theo mã TP. Loại hình: DNCX E42 / GC E52 / SXXK E62. Ngưỡng: <1% Info · 1–5% Warning · >5% Critical. | 🟡 | ✅ |
| **C1.5** | Tái xuất M15 không có TK B13 — `xuat_tra_lai` > 0 trong M15 nhưng không có B13 tương ứng. Rủi ro: Ghi tái xuất để giảm tồn nhưng không có TK chứng minh. | 🟡 | 🚧 |
| **C1.6** | Chuyển mục đích sử dụng không có TK A42 — `chuyen_mdsd` > 0 nhưng không có A42. Rủi ro: Hàng miễn thuế chuyển nội địa không khai báo — vi phạm điều kiện miễn thuế. | 🔴 | ✅ |

### Nhóm 2 — Cân bằng và tồn kho (5 checks)

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C2.1** | Mất cân bằng phương trình M15 — `ton_cuoi` ≠ `ton_dau` + `nhap` − `xuat_tra` − `xuat_sx` − `chuyen_mdsd` − `xuat_khac`. Ngưỡng: Delta ≠ 0 (±0.01 làm tròn). Rủi ro: Có cột bị chỉnh thủ công để đạt số tồn mong muốn. | 🔴 | ✅ |
| **C2.2** | Mất cân bằng phương trình M15a — `ton_cuoi` ≠ `ton_dau` + `nhap_kho` − `chuyen_mdsd` − `xuat_khau` − `xuat_khac`. Rủi ro: Sản lượng, xuất khẩu hoặc tồn TP bị chỉnh tay. | 🔴 | ✅ |
| **C2.3** | Tồn cuối âm — NVL (M15) — `ton_cuoi_ky` < 0 trên bất kỳ mã NVL nào. Rủi ro: Xuất vượt nhập + tồn đầu — thiếu TK nhập hoặc nguồn NVL không khai báo. | 🔴 | ✅ |
| **C2.4** | Tồn cuối âm — Thành phẩm (M15a) — `ton_cuoi_ky` < 0 trên bất kỳ mã TP nào. Rủi ro: Xuất khẩu nhiều hơn sản xuất + tồn đầu. | 🔴 | 🚧 |
| **C2.5** | Tồn cuối lớn hơn nhập khi tồn đầu = 0 — `ton_dau_ky` = 0 nhưng `ton_cuoi_ky` > `nhap_trong_ky`. Rủi ro: Tồn phồng, nguồn gốc không giải trình được. | 🔴 | 🚧 |

### Nhóm 3 — Phân loại hàng hoá (3 checks)

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C3.1** | Cùng mã vật tư khai nhiều loại hình mâu thuẫn — Một mã có trên cả TK NVL và TK máy móc cùng kỳ. Cặp mâu thuẫn: E11+E13 · E31+E13 · E21+E13. Rủi ro: Phân loại sai dẫn đến sai phạm vi BCQT. | 🟡 | ✅ |
| **C3.2** | HS code không nhất quán trong kỳ (cùng mã vật tư) — ≥2 mã HS khác nhau trên các TK. Ngưỡng: Khác subheading (6 số) Info · heading (4 số) Warning · chapter (2 số) Critical. Rủi ro: Ảnh hưởng thuế suất và chính sách. | 🟡🔴 | ✅ |
| **C3.3** | Đơn vị tính không nhất quán (cùng mã vật tư) — ≥2 đơn vị tính khác nhau giữa M15 và BCCT. **Thực tế Johnson 2025**: 3 mã sai đơn vị ×1.000 làm sai toàn bộ số liệu M15. Rủi ro: Sai đơn vị ×1000 → toàn bộ nhập/xuất/tồn sai hệ thống. | 🔴 | ✅ |

### Nhóm 4 — Định mức M16 (6 checks)

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C4.1** | NVL trong M16 không có nhập khẩu trong M15 — `ma_nvl` trong M16 nhưng `nhap_trong_ky` = 0 hoặc không có dòng M15. Rủi ro: Không thể giải trình dòng vật tư từ TK đến TP xuất khẩu. | 🔴 | ✅ |
| **C4.2** | TP trong M16 không có trong M15a — `ma_sp_xk` trong M16 nhưng không có dòng M15a. Rủi ro: Định mức cho TP không có trong báo cáo xuất khẩu. | 🟡 | 🚧 |
| **C4.3** | Tổng tiêu hao phái sinh M16 vượt xuất SX M15 — Σ(`định_mức` × `xuat_khau_15a`) theo mã NVL > `xuat_sx` trong M15. Ngưỡng: >5% Warning · >20% Critical. Rủi ro: Định mức thổi phồng để hợp thức hoá NVL nhập khẩu vượt mức. | 🟡 | ✅ |
| **C4.4** | M16 phân mảnh: nhiều NVL cùng chức năng cho một TP. **Ví dụ thực tế**: 1 chiếc áo có 10 loại cúc khác nhau trong M16. Phương pháp: (A) ≥N mã cùng HS 4-số trong 1 TP (mặc định) · (B) NLP cluster tên gần giống · (C) HQ định nghĩa danh mục. Ngưỡng: ≥5 mã cùng HS/TP Warning · ≥10 Critical. Rủi ro: Phân mảnh NVL để che số lượng. | 🟡 | 🚧 |
| **C4.5** | Định mức bằng 0 hoặc âm — `dinh_muc_thuc_te` ≤ 0 trên bất kỳ dòng M16. Rủi ro: Lỗi dữ liệu hoặc cố tình khai 0 để che tiêu hao thực tế. | 🔴 | 🚧 |
| **C4.6** | Định mức bất thường cao (outlier thống kê) — `dinh_muc` cặp TP-NVL vượt xa mean. Ngưỡng: mean ±3σ Warning · ±5σ Critical. Rủi ro: Thổi phồng định mức. | 🟡 | 🚧 |

### Nhóm 5 — Truy nguồn NVL nhập khẩu (3 checks)

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C5.1** | NVL có xuất SX trong M15 nhưng không có nhập HQ — `xuat_sx` > 0 và `nhap_trong_ky` = 0 và `ton_dau_ky` = 0. Rủi ro: Tiêu hao từ nguồn không khai báo — NVL nội địa bị đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C5.2** | TP xuất khẩu không có M16 (TP mồ côi) — Mã TP có `xuat_khau` > 0 trong M15a nhưng không có dòng M16. Rủi ro: Không thể giải trình NVL đầu vào. | 🟡 | 🚧 |
| **C5.3** | Tỷ lệ traceability thấp theo mã NVL — Σ(`định_mức` × `xuat_khau_15a`) / `xuat_sx_M15` < ngưỡng. Ngưỡng: <80% Warning · <60% Critical. Rủi ro: Phần lớn NVL không truy được vào TP cụ thể. | 🟡 | 🚧 |

### Nhóm 6 — Kiểm tra liên kỳ (5 checks)

*Cần dữ liệu ≥2 kỳ BCQT.*

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C6.1** | Tồn đầu kỳ N ≠ Tồn cuối kỳ N-1 — NVL (M15) — Theo từng mã. Rủi ro: Điều chỉnh tồn giữa 2 kỳ không có giải trình. | 🔴 | ✅ |
| **C6.2** | Tồn đầu kỳ N ≠ Tồn cuối kỳ N-1 — Thành phẩm (M15a) — Tương tự C6.1 cho TP. | 🔴 | 🚧 |
| **C6.3** | Định mức M16 thay đổi đột biến giữa các kỳ — \|`định_mức(N)` − `định_mức(N-1)`\| / `định_mức(N-1)` vượt ngưỡng. Ngưỡng: >20% Warning · >50% Critical. Rủi ro: Thổi phồng hoặc co định mức để điều tiết NVL cần giải trình. | 🟡 | 🚧 |
| **C6.4** | Nhập tăng mạnh nhưng xuất khẩu không tăng tương ứng — `nhap_trong_ky` tăng >X% trong khi `xuat_khau` tăng <Y%. Ngưỡng: Nhập >50% nhưng xuất <10% → Warning. Rủi ro: Tích luỹ tồn bất thường, nguy cơ chuyển nội địa không khai A42. | 🟡 | 🚧 |
| **C6.5** | HS code thay đổi cho cùng mã vật tư giữa các kỳ — Ngưỡng: Đổi heading (4 số) Warning · chapter (2 số) Critical. Rủi ro: Phân loại lại để chuyển sang nhóm thuế suất có lợi hơn. | 🟡🔴 | 🚧 |

### Nhóm 7 — Cross-DN benchmarking (Phase 2 — cần dữ liệu HQ portfolio)

| Mã | Tên | Mức | MVP |
|---|---|---|---|
| **C7.1** | Peer norm outlier — Định mức DN > Xσ mean của ngành (cùng HS chapter / cùng loại sản phẩm). Rủi ro: Định mức bất thường vs peer cùng ngành. | 🟡 | ⏳ P2 |
| **C7.2** | Same supplier price drift across DN — Giá nhập cùng NCC + cùng HS chênh lệch giữa các DN. Rủi ro: Chuyển giá / trốn thuế tập thể. | 🟡🔴 | ⏳ P2 |
| **C7.3** | Same HS code volume relative outlier vs ngành — Volume nhập/xuất 1 HS của DN vượt xa median của ngành. Rủi ro: Quy mô bất thường cần kiểm tra. | 🟡 | ⏳ P2 |

### 4.7 Tổng hợp

| Nhóm | Tổng | MVP ✅ | W.I.P 🚧 | P2 ⏳ |
|---|---:|---:|---:|---:|
| 1 — Số lượng nhập/xuất | 6 | 5 | 1 | 0 |
| 2 — Cân bằng & tồn kho | 5 | 3 | 2 | 0 |
| 3 — Phân loại hàng hoá | 3 | 3 | 0 | 0 |
| 4 — Định mức M16 | 6 | 2 | 4 | 0 |
| 5 — Truy nguồn NVL | 3 | 1 | 2 | 0 |
| 6 — Liên kỳ | 5 | 1 | 4 | 0 |
| 7 — Cross-DN | 3 | 0 | 0 | 3 |
| **Tổng** | **31** | **15** | **13** | **3** |

> **Đề án mở rộng:** Catalog không cố định. Mỗi case nghiệp vụ Hải quan phát hiện mới có thể thêm vào catalog dạng plugin, không cần thay đổi core. Ngưỡng đề xuất có thể điều chỉnh theo thực tế nghiệp vụ.

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
| Database | SQLite (MVP) → PostgreSQL (Pilot+) | SQLite đủ cho 5 DN; Postgres khi scale |
| Excel parsing | pandas + openpyxl + xlrd | TT 39/2018 mẫu BCQT .xlsx, BCCT VNACCS .xls |
| LLM | OpenAI-compatible client → endpoint Tinsu | Đồng bộ stack data-hub, barry-CO |
| Frontend | Server-rendered HTML + HTMX | Đơn giản, không SPA, dễ vận hành |
| Deploy | Docker Compose + Cloudflare Tunnel | Đồng bộ pattern Tinsu hiện hành |

### 5.3 Vai trò LLM trong audit-hq

LLM **không** làm detection. LLM làm những việc sau:

| Use case | Khi nào trigger | Output |
|---|---|---|
| Material name normalization | Khi parse BCCT/Mẫu, gặp mô tả lộn xộn | Canonical form, draft cho cán bộ confirm |
| Fuzzy code re-mapping | Khi confidence rule-based <80% | Đề xuất mapping, draft |
| Plain-VN explanation cho finding | Khi cán bộ click vào finding | Diễn giải dễ đọc dùng template + LLM fill |
| Mã loại hình suggestion | Khi gặp mã không có trong QĐ 1357 | Cảnh báo + đề xuất tra cứu |

> **Endpoint:** Sử dụng LLM proxy nội bộ Tinsu (`codex-lb-demo.sgnai.dev`).

---

## 6. Demo plan (POC)

### 6.1 Demo data composition

5 DN synthetic, mỗi DN 3-4 năm:

| Mã DN | Ngành | Loại hình | Số năm | Findings được inject |
|---|---|---|---|---|
| DN_001 | Điện tử (HS 85) | DNCX (E11/E42) | 4 | C1.1, C2.1, C6.1, C3.2 |
| DN_002 | Cơ khí (HS 84) | DNCX (E11/E42) | 3 | C1.2, C3.3, C3.1, C6.5 |
| DN_003 | Dệt may (HS 61) | SXXK (E31/E62) | 4 | C4.3, C4.4 (cúc áo), C5.1 |
| DN_004 | Hoá chất (HS 39) | DNCX | 3 | C1.4, C1.6, C2.3 |
| DN_005 | Cơ khí (HS 84) | DNCX | 3 | (clean — kiểm chứng audit-hq không flag bừa) |

> **TBD — Trọng Tín cung cấp:** template base data từ 5 client thực tế (đã anonymize). Phương án synthetic injection trên base data sạch.

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
| HS code | Cần cho C3.2, C6.5, C7.x |
| Mã loại hình (E11/E13/E42...) | Core data, không nhạy cảm |
| Tên material | Cần fuzzy match (C3.3, C4.4); thay bằng generic name + variant |
| Số lượng/giá trị | Cần cho outlier detection; có thể scale ×constant |

### 6.3 Demo flow 5 phút

```
0:00 — Đăng nhập Hải quan → Dashboard portfolio 5 DN
0:30 — Top-5 ranked theo risk score:
         #1 DN_001 (risk 87) — 4 critical findings
         #2 DN_002 (risk 76) — 3 critical findings
         #3 DN_004 (risk 68)
         #4 DN_003 (risk 54)
         #5 DN_005 (risk 12) — clean
1:00 — Click DN_001 → DN detail page
         Tabs: Findings | Multi-year view | BCCT raw | Mẫu 15/15a/16
1:30 — Click finding "C6.1 Tồn đầu kỳ N ≠ tồn cuối kỳ N-1"
         Panel trái: Tồn cuối 2023 cho 5 mã NVL
         Panel phải: Tồn đầu 2024 cho cùng 5 mã — chênh lệch X
         Note: "Điều chỉnh tồn giữa 2 kỳ không có giải trình"
2:30 — Click finding "C4.3 Tổng tiêu hao M16 vượt M15"
         Bảng: TP_X sản xuất 1,000 cái, M16 norm = 5kg/cái
                Σ(norm × output) = 5,000kg expected NVL X
                M15 cột xuất_sx X = 4,000kg actual
                Chênh: 1,000kg NVL "biến mất"
3:30 — Click finding "C3.3 UOM mismatch" 
         BCCT khai 1,000 kg, M15 khai 1,000 cái → ×1.000 mismatch
         Reference Johnson 2025: 3 mã cùng pattern
4:00 — Click "Xuất báo cáo kiến nghị kiểm tra" → Excel với:
         + Danh sách 4 findings
         + Evidence dump (dòng BCCT cụ thể)
         + Trích yếu pháp lý (TT 39/2018, TT 38/2015)
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
| W3 | Implement 8-10 finding categories đầu (Nhóm 1, 2) | Findings hiển thị, evidence trail working |
| W4 | Implement đủ MVP-15 + risk scoring | Dashboard + ranking |
| W5 | Synthetic data 5 DN × 3-4 năm + anonymization | Demo data hoàn chỉnh |
| W6 | Polish UI + demo rehearsal + đóng gói | Pitch-ready |

### 7.2 Phase 2 — Pilot tại Chi cục (timeframe đề xuất: 3-6 tháng sau POC approve)

- Triển khai tại **Chi Cục Hải Quan Khu vực IV**
- Ingest data DN trong phạm vi quản lý (real, không synthetic)
- Cán bộ dùng thực tế, feedback loop
- Implement 13 W.I.P findings còn lại
- Bắt đầu seed cross-DN benchmarking (Nhóm 7) khi đã có ≥30 DN

### 7.3 Phase 3 — Production (timeframe đề xuất: 12+ tháng)

- Mở rộng nhiều Chi cục
- Tích hợp trực tiếp VNACCS DB (không qua Excel export)
- API HQ cho DN portal nộp trực tiếp structured
- Implement Nhóm 7 đầy đủ (cross-DN peer)
- ML-augmented detection (sau khi có >3 năm operational data)

### 7.4 Vai trò các bên

| Bên | Phase 1 (POC) | Phase 2 (Pilot) | Phase 3 (Production) |
|---|---|---|---|
| Tinsu AI | Build tool, demo data | Maintenance, R&D rule mới | Operate, scale |
| Trọng Tín | Cung cấp domain expertise, base data anonymize | Đào tạo cán bộ, đầu mối nghiệp vụ | Consulting |
| Hải quan | Sponsor đề án, feedback design | Cán bộ dùng thử, cung cấp data Chi cục | Customer chính thức |

> **Quan trọng:** Data của Trọng Tín chỉ dùng để **build và demo công cụ**. Khi Hải quan deploy production, hệ thống sử dụng data của Hải quan. Trọng Tín không chuyển dữ liệu khách hàng sang Hải quan ngoài bối cảnh DN đó tự nộp BCQT.

---

## 8. Câu hỏi mở cho phía Hải quan

Đây là các nội dung cần feedback Hải quan trước khi finalize đề án và xây dựng MVP.

### 8.1 Về phạm vi nghiệp vụ

1. Trong 31 checks đề xuất, có check nào Hải quan đặc biệt quan tâm hoặc có check nào quan trọng mà đề án bỏ sót?
2. Output Excel kiến nghị kiểm tra có cần format theo mẫu chính thức nào không?
3. Hệ thống hiện đang sử dụng tool/quy trình nào để chọn DN kiểm tra? Audit-HQ tích hợp hay thay thế?
4. Ngưỡng đề xuất (Critical/Warning) có phù hợp thực tế nghiệp vụ Chi cục không? Cần điều chỉnh gì?

### 8.2 Về dữ liệu

5. Hệ thống xử lý dữ liệu điện tử của Hải quan có lưu Mẫu 15/15a/16 ở dạng structured database, hay chỉ là Excel attachments?
6. TKXNK lấy từ VNACCS có thể export Excel theo cấu trúc thống nhất cho mọi Chi cục không?
7. Quyền truy cập dữ liệu đa năm: hệ thống VCIS-VNACCS đã cho phép query trực tiếp, hay phải xin từng kỳ?

### 8.3 Về kỹ thuật & vận hành

8. Hệ thống deploy on-premise của Hải quan hay cloud (Tinsu host)? Yêu cầu bảo mật cụ thể?
9. Có yêu cầu chứng nhận an toàn thông tin (ATTT) cấp nào?
10. SLA cần cho Pilot/Production?
11. Cán bộ tại Chi Cục Hải Quan Khu vực IV có kỹ năng tin học mức nào? Cần đào tạo bao nhiêu?

### 8.4 Về pháp lý & ranh giới

12. Audit-HQ phát hiện sai phạm chỉ là *gợi ý*, không phải kết luận điều tra. Đồng ý cách dùng này?
13. Trường hợp DN khiếu nại kết quả audit-hq, Hải quan có cần Tinsu hỗ trợ giải trình kỹ thuật không?
14. Quyền sở hữu trí tuệ catalog rule: thuộc Hải quan, Tinsu, hay shared?

---

## 9. Phụ lục

### 9.1 Glossary

| Thuật ngữ | Định nghĩa |
|---|---|
| BCQT | Báo cáo Quyết toán |
| BCCT | Báo cáo Chi tiết (TKXNK tổng hợp) |
| TKXNK | Tờ khai Xuất Nhập khẩu |
| DNCX | Doanh nghiệp Chế xuất |
| GC | Gia công |
| SXXK | Sản xuất Xuất khẩu |
| KTSTQ | Kiểm tra Sau Thông quan |
| NVL | Nguyên Vật Liệu |
| TP | Thành Phẩm |
| BTP | Bán Thành Phẩm |
| Mẫu 15 | Báo cáo cân đối NVL (BCQT-NVL) |
| Mẫu 15a | Báo cáo cân đối TP (BCQT-SP) |
| Mẫu 16 | Định mức thực tế (ĐMTT) |
| VNACCS | Hệ thống thông quan tự động VN |
| HS code | Mã hài hoà mô tả hàng hoá quốc tế |
| E11/E13/E15 | Mã loại hình nhập DNCX (NVL/máy móc/GC) |
| E21/E23 | Mã loại hình nhập gia công |
| E31/E33 | Mã loại hình nhập SXXK |
| E42/E52/E62 | Mã loại hình xuất tương ứng |
| B13 | Tái xuất |
| A42 | Chuyển mục đích sử dụng nội địa |

### 9.2 Tham chiếu

- TT 38/2015/TT-BTC, TT 39/2018/TT-BTC, TT 121/2025/TT-BTC
- QĐ 1357/QĐ-TCHQ ngày 18/05/2021
- Luật Hải quan 2014, Luật Quản lý Thuế 2019, Luật Sở hữu Trí tuệ
- BCQT-System (Tinsu AI) — kiến trúc, parser, adapter pattern
- BCQT Showcase checklist — danh sách 28 checks cơ sở (v1.0, 2026-05-13)
- Johnson BCQT 2025 (Tinsu AI × Trọng Tín × Johnson) — case thực tế UOM ×1000 (C3.3)

### 9.3 Changelog

| Version | Ngày | Tác giả | Thay đổi |
|---|---|---|---|
| v0.1-DRAFT | 2026-05-13 | Tinsu AI | Bản đầu — chờ vòng feedback đầu tiên |
| v0.2-DRAFT | 2026-05-13 | Tinsu AI | Synthesize với checklist 28 checks từ BCQT showcase; chính xác hoá đơn vị tiếp nhận (Chi Cục Hải Quan Khu vực IV); làm rõ Excel BCQT có format chuẩn; tổng quát hoá tham chiếu Hải quan (không cụ thể QLRR) |

---

> **Đây là bản DRAFT v0.2.** Mọi nội dung là đề xuất sơ bộ và sẽ được điều chỉnh theo feedback và input từ phía Hải quan qua các vòng synthesize tiếp theo.
