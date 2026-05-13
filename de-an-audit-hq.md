# Đề án: Audit-HQ

**Hệ thống hỗ trợ quản lý rủi ro và phát hiện sai phạm trong Báo cáo Quyết toán Hải quan (BCQT) và Tờ khai Xuất Nhập khẩu (TKXNK)**

> **Bản dự thảo lần 3** — 2026-05-13
> Tài liệu sẽ trải qua nhiều vòng rà soát, tổng hợp ý kiến từ phía Hải quan. Mọi nội dung dưới đây là đề xuất sơ bộ.
>
> Soạn thảo: Tinsu AI × Trọng Tín
> **Đơn vị tiếp nhận:** Chi Cục Hải Quan Khu vực IV

---

## 1. Tổng quan

### 1.1 Bối cảnh

Mỗi năm, các doanh nghiệp chế xuất (DNCX), doanh nghiệp gia công, và doanh nghiệp sản xuất xuất khẩu (SXXK) nộp cơ quan Hải quan bộ báo cáo quyết toán nguyên vật liệu — sản phẩm — định mức (Mẫu 15/BCQT-NVL, Mẫu 15a/BCQT-SP, Mẫu 16/ĐMTT theo TT 39/2018) cùng toàn bộ lịch sử Tờ khai Xuất Nhập khẩu trong kỳ. Khối lượng dữ liệu rất lớn (mỗi doanh nghiệp cỡ hàng chục nghìn dòng tờ khai mỗi năm, qua nhiều năm); việc rà soát thủ công không khả thi và phụ thuộc kinh nghiệm cán bộ.

Hiện tại cơ quan Hải quan lựa chọn doanh nghiệp để kiểm tra sau thông quan chủ yếu dựa trên:
- Tổng quy mô kim ngạch
- Loại hình hoạt động (DNCX, gia công, SXXK)
- Kinh nghiệm và đánh giá của cán bộ

Cách tiếp cận này có thể bỏ sót doanh nghiệp có sai phạm tinh vi nhưng quy mô vừa, đồng thời tốn nguồn lực kiểm tra các doanh nghiệp tuân thủ tốt.

### 1.2 Mục tiêu

Xây dựng hệ thống Audit-HQ giúp cơ quan Hải quan:

1. **Phát hiện sai phạm khả năng** từ BCQT và TKXNK đã nộp, bằng phân tích đa chiều (số học nội bộ Mẫu, đối chiếu chéo các nguồn, kiểm tra định mức M16, truy nguồn nguyên vật liệu, so sánh liên kỳ, so sánh giữa các doanh nghiệp).
2. **Xếp hạng doanh nghiệp theo mức độ rủi ro**, kèm chứng cứ truy ngược về dòng dữ liệu gốc, để cán bộ có cơ sở giải trình khi đề xuất kiểm tra.
3. **Mở rộng danh mục kiểm tra** theo thời gian khi cán bộ phát hiện kiểu sai phạm mới qua thực tế nghiệp vụ.

### 1.3 Đối tượng sử dụng

| Vai trò | Hoạt động chính | Tần suất |
|---|---|---|
| Cán bộ Hải quan | Xem danh sách doanh nghiệp, xem chi tiết phát hiện, xuất báo cáo kiến nghị kiểm tra | Hằng tuần — hằng quý |
| Cấp quản lý | Duyệt báo cáo kiến nghị, phân công | Hằng tuần |
| Cán bộ kiểm tra sau thông quan *(giai đoạn 2)* | Sử dụng chứng cứ do hệ thống nêu ra trong quá trình kiểm tra thực tế | Theo từng vụ việc |

### 1.4 Cơ sở pháp lý tham chiếu

- Luật Hải quan 2014, Điều 16-17 (Áp dụng quản lý rủi ro)
- TT 38/2015/TT-BTC, sửa đổi bởi TT 39/2018/TT-BTC, tham chiếu TT 121/2025/TT-BTC
- QĐ 1357/QĐ-TCHQ ngày 18/05/2021 (Mã loại hình xuất nhập khẩu)
- Luật Quản lý Thuế 2019, Điều 99 (Bí mật thông tin người nộp thuế)
- Nghị định 13/2023/NĐ-CP (Bảo vệ dữ liệu cá nhân)

---

## 2. Nguyên tắc thiết kế

### 2.1 Định hướng theo rủi ro, không kiểm tra đại trà

Hệ thống không kiểm tra toàn bộ doanh nghiệp — chỉ xếp hạng theo mức rủi ro để cán bộ phân bổ nguồn lực kiểm tra đúng chỗ. Phù hợp tinh thần quản lý rủi ro của Luật Hải quan 2014.

### 2.2 Có chứng cứ truy nguồn, không "hộp đen"

Mỗi phát hiện hệ thống đưa ra phải:
- Trỏ về dòng dữ liệu cụ thể trong BCCT hoặc Mẫu (số tờ khai, dòng hàng, mã NVL/sản phẩm)
- Nêu rõ điều khoản pháp lý liên quan
- Cho phép cán bộ giải trình khi báo cáo cấp trên hoặc đối thoại với doanh nghiệp

Mọi kiểm tra đều theo **quy tắc xác định** (cho cùng dữ liệu thì cho cùng kết quả). Trí tuệ nhân tạo (AI) chỉ dùng vào các việc hỗ trợ:
- Chuẩn hoá tên hàng hoá (đối chiếu tên gần giống)
- Sinh giải thích tiếng Việt dễ đọc cho phát hiện
- Gợi ý ánh xạ mã hàng (chỉ là gợi ý, cán bộ quyết định)

### 2.3 Danh mục kiểm tra mở rộng được

Mỗi loại kiểm tra là một **mô-đun độc lập**. Thêm kiểm tra mới = thêm một mô-đun, không phải sửa phần lõi. Cán bộ Hải quan (qua phối hợp với Tinsu) có thể đề xuất quy tắc mới theo nghiệp vụ thực tế phát hiện.

### 2.4 Ngưỡng có thể điều chỉnh

Hệ thống có ngưỡng mặc định cho mỗi kiểm tra (Nghiêm trọng / Cảnh báo / Thông tin). Cơ quan Hải quan có toàn quyền điều chỉnh ngưỡng theo thực tế nghiệp vụ, theo loại hình doanh nghiệp, hoặc theo ngành hàng.

### 2.5 An toàn pháp lý

- Lớp ẩn danh cho dữ liệu trình diễn (bảo vệ bí mật doanh nghiệp trong giai đoạn thử nghiệm).
- Nhật ký thao tác đầy đủ cho mọi hành động của cán bộ.
- Không thay đổi dữ liệu gốc — mọi đánh dấu và phát hiện là lớp phủ riêng biệt.

---

## 3. Phạm vi thử nghiệm ban đầu

### 3.1 Dữ liệu đầu vào

| Loại dữ liệu | Định dạng | Nguồn | Phạm vi thử nghiệm |
|---|---|---|---|
| Mẫu 15 (BCQT-NVL) | Excel có định dạng chuẩn theo TT 39/2018 | Doanh nghiệp nộp qua hệ thống điện tử | 5 DN × 3-4 năm |
| Mẫu 15a (BCQT-SP) | Excel có định dạng chuẩn | Doanh nghiệp nộp | 5 DN × 3-4 năm |
| Mẫu 16 (ĐMTT) | Excel có định dạng chuẩn | Doanh nghiệp nộp | 5 DN × 3-4 năm |
| BCCT TKXNK | Excel xuất từ VNACCS (hoặc doanh nghiệp tổng hợp) | Hệ thống Hải quan | 5 DN × 3-4 năm |

> **Dữ liệu BCQT là Excel có định dạng chuẩn** theo TT 39/2018, không phải tự do. Hệ thống có sẵn bộ đọc xử lý định dạng chuẩn, đồng thời có lớp tiếp nhận biến thể nhỏ giữa các doanh nghiệp.

### 3.2 Kết quả đầu ra

Cho mỗi doanh nghiệp:
- Danh sách phát hiện (mỗi phát hiện có mức độ 🔴/🟡/🔵, nhóm kiểm tra, chứng cứ truy nguồn, đề xuất hành động).
- Điểm rủi ro tổng hợp (có thể giải trình từng yếu tố cấu thành, không phải kết quả của thuật toán "hộp đen").
- Báo cáo Excel kiến nghị kiểm tra (xuất khi cán bộ duyệt).

Cho toàn bộ danh sách doanh nghiệp:
- Bảng tổng quan xếp hạng doanh nghiệp theo điểm rủi ro.
- Bộ lọc theo ngành, kim ngạch, loại hình.

### 3.3 Phạm vi xử lý

- **Đơn vị triển khai:** mỗi lần triển khai phục vụ một đơn vị Hải quan cấp Chi cục.
- **Quy mô thử nghiệm:** 5 doanh nghiệp × 3-4 năm dữ liệu (15-20 lượt báo cáo).
- **Quy mô triển khai thí điểm dự kiến:** 50-200 doanh nghiệp, 5 năm dữ liệu.
- **Quy mô vận hành chính thức:** Tất cả DNCX/Gia công/SXXK trong phạm vi quản lý, 10 năm dữ liệu.

---

## 4. Danh mục các kiểm tra

> **Tổng:** 28 kiểm tra (6 nhóm chính) + 3 kiểm tra so sánh giữa các doanh nghiệp (giai đoạn 2, cần dữ liệu cơ quan Hải quan toàn ngành).
>
> **Trạng thái:**
> - ✅ Xây dựng và trình diễn ngay (15 kiểm tra)
> - 🚧 Có trong danh mục, sẽ xây dựng giai đoạn thí điểm (13 kiểm tra)
> - ⏳ Giai đoạn 2 (3 kiểm tra) — cần dữ liệu cơ quan Hải quan đa doanh nghiệp
>
> **Mức độ:** 🔴 Nghiêm trọng · 🟡 Cảnh báo · 🔵 Thông tin

### 4.0 Loại hình tờ khai theo loại hình doanh nghiệp

| Loại hình DN | Tờ khai nhập | Tờ khai xuất |
|---|---|---|
| **DNCX** — Doanh nghiệp chế xuất | E11, E15, E13 | E42 |
| **Gia công** — Gia công cho thương nhân nước ngoài | E21, E23 | E52, E54 |
| **SXXK** — Sản xuất xuất khẩu | E31, E33 | E62 |

> Tái xuất: B13 áp dụng chung. Chuyển mục đích sử dụng: A42 khi chuyển nội địa.

### Nhóm 1 — Số lượng nhập / xuất (6 kiểm tra)

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C1.1** | Lệch số lượng nhập nguyên vật liệu (M15 so với tờ khai) — `nhập_trong_kỳ` (M15) khác Σ tờ khai nhập theo mã. Loại hình: DNCX E11+E15 / Gia công E21+E23 / SXXK E31+E33. Ngưỡng: <5% Thông tin · 5–20% Cảnh báo · >20% Nghiêm trọng. Rủi ro: Khai thiếu hoặc khai thừa nhập khẩu. | 🟡 | ✅ |
| **C1.2** | Có tờ khai nhập nhưng không có trong M15 — mã có trên BCCT nhưng không có dòng trong M15. Đánh dấu mọi trường hợp. Rủi ro: Bỏ sót nguyên vật liệu nhập khẩu khỏi BCQT. | 🔴 | ✅ |
| **C1.3** | Có trong M15 nhưng không có tờ khai — `nhập_trong_kỳ` > 0 mà không có tờ khai tương ứng. Rủi ro: M15 không có căn cứ tờ khai, khả năng nguyên vật liệu nội địa bị đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C1.4** | Lệch số lượng xuất thành phẩm (M15a so với tờ khai) — `xuất_khẩu` khác Σ tờ khai xuất theo mã thành phẩm. Loại hình: DNCX E42 / Gia công E52 / SXXK E62. Ngưỡng: <1% Thông tin · 1–5% Cảnh báo · >5% Nghiêm trọng. | 🟡 | ✅ |
| **C1.5** | Tái xuất M15 không có tờ khai B13 — `xuất_trả_lại` > 0 trong M15 nhưng không có B13 tương ứng. Rủi ro: Ghi tái xuất để giảm tồn nhưng không có tờ khai chứng minh. | 🟡 | 🚧 |
| **C1.6** | Chuyển mục đích sử dụng không có tờ khai A42 — `chuyển_mục_đích_sử_dụng` > 0 nhưng không có A42. Rủi ro: Hàng miễn thuế chuyển nội địa không khai báo — vi phạm điều kiện miễn thuế. | 🔴 | ✅ |

### Nhóm 2 — Cân bằng và tồn kho (5 kiểm tra)

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C2.1** | Mất cân bằng phương trình M15 — `tồn_cuối` khác `tồn_đầu` + `nhập` − `xuất_trả` − `xuất_sản_xuất` − `chuyển_mục_đích_sử_dụng` − `xuất_khác`. Ngưỡng: chênh lệch khác 0 (cho phép ±0,01 làm tròn). Rủi ro: Có cột bị chỉnh thủ công để đạt số tồn mong muốn. | 🔴 | ✅ |
| **C2.2** | Mất cân bằng phương trình M15a — `tồn_cuối` khác `tồn_đầu` + `nhập_kho` − `chuyển_mục_đích_sử_dụng` − `xuất_khẩu` − `xuất_khác`. Rủi ro: Sản lượng, xuất khẩu hoặc tồn thành phẩm bị chỉnh tay. | 🔴 | ✅ |
| **C2.3** | Tồn cuối âm — nguyên vật liệu (M15) — `tồn_cuối_kỳ` < 0 trên bất kỳ mã nào. Rủi ro: Xuất vượt nhập + tồn đầu — thiếu tờ khai nhập hoặc nguồn nguyên vật liệu không khai báo. | 🔴 | ✅ |
| **C2.4** | Tồn cuối âm — thành phẩm (M15a) — `tồn_cuối_kỳ` < 0 trên bất kỳ mã nào. Rủi ro: Xuất khẩu nhiều hơn sản xuất + tồn đầu. | 🔴 | 🚧 |
| **C2.5** | Tồn cuối lớn hơn nhập khi tồn đầu bằng 0 — `tồn_đầu_kỳ` = 0 nhưng `tồn_cuối_kỳ` > `nhập_trong_kỳ`. Rủi ro: Tồn phồng, nguồn gốc không giải trình được. | 🔴 | 🚧 |

### Nhóm 3 — Phân loại hàng hoá (3 kiểm tra)

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C3.1** | Cùng mã vật tư khai nhiều loại hình mâu thuẫn — một mã có trên cả tờ khai nguyên vật liệu và tờ khai máy móc thiết bị trong cùng kỳ. Cặp mâu thuẫn: E11+E13 · E31+E13 · E21+E13. Rủi ro: Phân loại sai dẫn đến sai phạm vi BCQT. | 🟡 | ✅ |
| **C3.2** | Mã HS không nhất quán trong kỳ (cùng mã vật tư) — ≥2 mã HS khác nhau trên các tờ khai. Ngưỡng: Khác phân nhóm (6 số) Thông tin · khác nhóm (4 số) Cảnh báo · khác chương (2 số) Nghiêm trọng. Rủi ro: Ảnh hưởng thuế suất và chính sách — khác chương là rủi ro pháp lý lớn nhất. | 🟡🔴 | ✅ |
| **C3.3** | Đơn vị tính không nhất quán (cùng mã vật tư) — ≥2 đơn vị khác nhau giữa M15 và BCCT. Rủi ro: Sai đơn vị tính ×1000 khiến toàn bộ nhập/xuất/tồn sai hệ thống. | 🔴 | ✅ |

### Nhóm 4 — Định mức M16 (6 kiểm tra)

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C4.1** | Nguyên vật liệu trong M16 không có nhập khẩu trong M15 — `mã_NVL` trong M16 nhưng `nhập_trong_kỳ` = 0 hoặc không có dòng trong M15. Rủi ro: Không thể giải trình dòng vật tư từ tờ khai đến thành phẩm xuất khẩu. | 🔴 | ✅ |
| **C4.2** | Thành phẩm trong M16 không có trong M15a — `mã_SP_xuất_khẩu` trong M16 nhưng không có dòng trong M15a. Rủi ro: Định mức cho thành phẩm không có trong báo cáo xuất khẩu. | 🟡 | 🚧 |
| **C4.3** | Tổng tiêu hao tính theo M16 vượt xuất sản xuất M15 — Σ(`định_mức` × `xuất_khẩu_M15a`) theo mã nguyên vật liệu > `xuất_sản_xuất` trong M15. Ngưỡng: vượt >5% Cảnh báo · >20% Nghiêm trọng. Rủi ro: Định mức thổi phồng để hợp thức hoá nguyên vật liệu nhập khẩu vượt mức. | 🟡 | ✅ |
| **C4.4** | M16 phân mảnh: nhiều nguyên vật liệu cùng chức năng cho một thành phẩm. **Ví dụ thực tế**: 1 chiếc áo có 10 loại cúc khác nhau trong M16. Cách phát hiện: (A) ≥N mã có cùng HS 4 số trong 1 thành phẩm (mặc định) · (B) gom nhóm tên gần giống (xử lý ngôn ngữ tự nhiên) · (C) cơ quan Hải quan định nghĩa danh mục nhóm vật tư. Ngưỡng: ≥5 mã cùng HS / thành phẩm Cảnh báo · ≥10 Nghiêm trọng. Rủi ro: Phân mảnh nguyên vật liệu để che số lượng, hợp thức hoá nhập khẩu dư. | 🟡 | 🚧 |
| **C4.5** | Định mức bằng 0 hoặc âm — `định_mức_thực_tế` ≤ 0 trên bất kỳ dòng M16 nào. Rủi ro: Lỗi dữ liệu hoặc cố tình khai 0 để che tiêu hao thực tế. | 🔴 | 🚧 |
| **C4.6** | Định mức bất thường cao (giá trị ngoại lai thống kê) — `định_mức` cặp thành phẩm-nguyên vật liệu vượt xa giá trị trung bình toàn dữ liệu. Ngưỡng: vượt trung bình ±3 độ lệch chuẩn Cảnh báo · ±5 độ lệch chuẩn Nghiêm trọng. Rủi ro: Thổi phồng định mức để hợp thức hoá nguyên vật liệu nhập khẩu vượt mức. | 🟡 | 🚧 |

### Nhóm 5 — Truy nguồn nguyên vật liệu nhập khẩu (3 kiểm tra)

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C5.1** | NVL có xuất sản xuất trong M15 nhưng không có nhập khẩu — `xuất_sản_xuất` > 0 và `nhập_trong_kỳ` = 0 và `tồn_đầu_kỳ` = 0. Rủi ro: Tiêu hao từ nguồn không khai báo — nguyên vật liệu nội địa bị đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C5.2** | Thành phẩm xuất khẩu không có trong M16 (thành phẩm "mồ côi") — mã thành phẩm có `xuất_khẩu` > 0 trong M15a nhưng không có dòng M16. Rủi ro: Không thể giải trình nguyên vật liệu đầu vào cho thành phẩm đã xuất khẩu. | 🟡 | 🚧 |
| **C5.3** | Tỷ lệ truy nguồn thấp theo mã nguyên vật liệu — Σ(`định_mức` × `xuất_khẩu_M15a`) / `xuất_sản_xuất_M15` thấp dưới ngưỡng. Ngưỡng: <80% Cảnh báo · <60% Nghiêm trọng. Rủi ro: Phần lớn nguyên vật liệu nhập khẩu không truy được vào thành phẩm xuất khẩu cụ thể. | 🟡 | 🚧 |

### Nhóm 6 — Kiểm tra liên kỳ (5 kiểm tra)

*Cần dữ liệu ≥2 kỳ BCQT.*

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C6.1** | Tồn đầu kỳ N khác tồn cuối kỳ N-1 — nguyên vật liệu (M15) — theo từng mã. Rủi ro: Điều chỉnh tồn giữa 2 kỳ không có giải trình. | 🔴 | ✅ |
| **C6.2** | Tồn đầu kỳ N khác tồn cuối kỳ N-1 — thành phẩm (M15a) — tương tự C6.1 cho thành phẩm. | 🔴 | 🚧 |
| **C6.3** | Định mức M16 thay đổi đột biến giữa các kỳ — chênh lệch tỷ lệ giữa định mức kỳ N và kỳ N-1 vượt ngưỡng (cùng cặp thành phẩm-nguyên vật liệu). Ngưỡng: >20% Cảnh báo · >50% Nghiêm trọng. Rủi ro: Thổi phồng hoặc co định mức để điều tiết lượng nguyên vật liệu cần giải trình. | 🟡 | 🚧 |
| **C6.4** | Nhập tăng mạnh nhưng xuất khẩu không tăng tương ứng — `nhập_trong_kỳ` tăng >X% trong khi `xuất_khẩu` tăng <Y%. Ngưỡng: nhập tăng >50% trong khi xuất tăng <10% Cảnh báo. Rủi ro: Tích luỹ tồn nguyên vật liệu bất thường, nguy cơ chuyển nội địa không khai báo A42. | 🟡 | 🚧 |
| **C6.5** | Mã HS thay đổi cho cùng mã vật tư giữa các kỳ — Ngưỡng: đổi nhóm (4 số) Cảnh báo · đổi chương (2 số) Nghiêm trọng. Rủi ro: Phân loại lại để chuyển sang nhóm thuế suất hoặc chính sách có lợi hơn. | 🟡🔴 | 🚧 |

### Nhóm 7 — So sánh giữa các doanh nghiệp (giai đoạn 2 — cần dữ liệu cơ quan Hải quan đa DN)

| Mã | Tên | Mức | Trạng thái |
|---|---|---|---|
| **C7.1** | Định mức bất thường so với cùng ngành — định mức doanh nghiệp vượt mức trung bình ngành (cùng chương HS hoặc cùng loại sản phẩm) một khoảng lớn. Rủi ro: Định mức bất thường so với các doanh nghiệp cùng ngành. | 🟡 | ⏳ |
| **C7.2** | Giá nhập từ cùng nhà cung cấp chênh lệch giữa các doanh nghiệp — cùng nhà cung cấp, cùng mã HS, giá khác nhau lớn. Rủi ro: Chuyển giá hoặc trốn thuế có hệ thống. | 🟡🔴 | ⏳ |
| **C7.3** | Lượng nhập / xuất cùng mã HS bất thường so với mức chung ngành — vượt xa giá trị trung vị của ngành. Rủi ro: Quy mô bất thường cần kiểm tra. | 🟡 | ⏳ |

### 4.7 Tổng hợp

| Nhóm | Tổng | Xây dựng ngay ✅ | Đang chờ 🚧 | Giai đoạn 2 ⏳ |
|---|---:|---:|---:|---:|
| 1 — Số lượng nhập/xuất | 6 | 5 | 1 | 0 |
| 2 — Cân bằng và tồn kho | 5 | 3 | 2 | 0 |
| 3 — Phân loại hàng hoá | 3 | 3 | 0 | 0 |
| 4 — Định mức M16 | 6 | 2 | 4 | 0 |
| 5 — Truy nguồn nguyên vật liệu | 3 | 1 | 2 | 0 |
| 6 — Liên kỳ | 5 | 1 | 4 | 0 |
| 7 — So sánh giữa các DN | 3 | 0 | 0 | 3 |
| **Tổng** | **31** | **15** | **13** | **3** |

> **Danh mục mở rộng được:** Catalog không cố định ở con số 31. Mỗi nghiệp vụ cơ quan Hải quan phát hiện mới có thể bổ sung vào danh mục như một mô-đun độc lập, không cần thay đổi phần lõi. Ngưỡng đề xuất có thể điều chỉnh theo thực tế.

---

## 5. Kiến trúc hệ thống (sơ bộ)

### 5.1 Mô hình dữ liệu

Hệ thống tổ chức dữ liệu thành 4 tầng. Mỗi tầng phục vụ một mục đích rõ ràng:

```
Tầng 0 — Tệp gốc:
   File Excel doanh nghiệp nộp, lưu nguyên trạng (không sửa), chỉ gắn
   thêm thông tin mô tả: mã doanh nghiệp, kỳ báo cáo, ngày nộp.

Tầng 1 — Dữ liệu chuẩn hoá:
   Sau khi đọc Excel, hệ thống chuyển vào các bảng dữ liệu có cấu trúc:
     • Bảng tờ khai xuất nhập khẩu (BCCT)
     • Bảng cân đối nguyên vật liệu (Mẫu 15)
     • Bảng cân đối thành phẩm (Mẫu 15a)
     • Bảng định mức (Mẫu 16)
   Mỗi dòng đều gắn mã doanh nghiệp để có thể truy vấn theo doanh
   nghiệp, theo kỳ, hoặc đan chéo giữa các bảng.

Tầng 2 — Phát hiện và đánh dấu:
   Kết quả từ các kiểm tra ở Mục 4. Mỗi phát hiện gắn liên kết về dòng
   dữ liệu Tầng 1 gốc. Cán bộ có thể đánh dấu (xác nhận / loại trừ /
   ghi chú) mà không thay đổi dữ liệu gốc.

Tầng 3 — Tổng hợp rủi ro:
   Tổng hợp điểm rủi ro doanh nghiệp từ phát hiện ở Tầng 2. Dùng cho
   xếp hạng và bảng tổng quan.
```

> **Nguyên tắc lõi:** Mỗi nguồn dữ liệu giữ cấu trúc gốc của nó. Khi cần phân tích đan chéo, hệ thống truy vấn cùng lúc nhiều bảng — không ép tất cả vào một bảng vạn năng.

### 5.2 Công nghệ sử dụng (gửi bộ phận công nghệ thông tin tham khảo)

| Thành phần | Công nghệ | Ghi chú |
|---|---|---|
| Phía máy chủ | Python 3.12 + thư viện FastAPI | Tái sử dụng từ hệ thống BCQT-System đã vận hành |
| Cơ sở dữ liệu | SQLite (thử nghiệm) → PostgreSQL (thí điểm) | Mở rộng dần theo quy mô |
| Đọc Excel | thư viện pandas + openpyxl + xlrd | Định dạng chuẩn TT 39/2018 cho M15/15a/16, định dạng VNACCS cho BCCT |
| Trí tuệ nhân tạo (AI) | máy chủ trung gian của Tinsu | Đồng bộ với các hệ thống khác Tinsu đang vận hành |
| Giao diện | Trang web hiển thị trên trình duyệt | Đơn giản, không cần cài phần mềm phía cán bộ |
| Đóng gói và triển khai | Docker + Cloudflare Tunnel | Đồng bộ pattern Tinsu hiện hành |

### 5.3 Vai trò trí tuệ nhân tạo (AI) trong hệ thống

AI **không** trực tiếp đưa ra phát hiện sai phạm. AI chỉ làm các việc hỗ trợ sau:

| Công việc | Khi nào dùng | Kết quả |
|---|---|---|
| Chuẩn hoá tên hàng hoá | Khi gặp mô tả không chuẩn trong BCCT/Mẫu | Tên chuẩn (cán bộ xác nhận) |
| Đối chiếu mã hàng gần giống | Khi quy tắc cứng có độ chính xác <80% | Đề xuất ánh xạ (cán bộ xác nhận) |
| Sinh giải thích tiếng Việt cho phát hiện | Khi cán bộ chọn xem một phát hiện | Diễn giải dễ đọc kèm dẫn chứng |
| Cảnh báo mã loại hình không hợp lệ | Khi tờ khai có mã không có trong QĐ 1357 | Cảnh báo và gợi ý tra cứu |

Mọi quyết định cuối cùng vẫn do cán bộ Hải quan đưa ra. AI chỉ là công cụ hỗ trợ.

---

## 6. Kế hoạch trình diễn (thử nghiệm ban đầu)

### 6.1 Dữ liệu trình diễn

5 doanh nghiệp giả lập, mỗi doanh nghiệp 3-4 năm:

| Mã DN | Ngành | Loại hình | Số năm | Sai phạm được đưa vào để minh hoạ |
|---|---|---|---|---|
| DN_001 | Điện tử (HS 85) | DNCX (E11/E42) | 4 | C1.1, C2.1, C6.1, C3.2 |
| DN_002 | Cơ khí (HS 84) | DNCX (E11/E42) | 3 | C1.2, C3.3, C3.1, C6.5 |
| DN_003 | Dệt may (HS 61) | SXXK (E31/E62) | 4 | C4.3, C4.4 (cúc áo), C5.1 |
| DN_004 | Hoá chất (HS 39) | DNCX | 3 | C1.4, C1.6, C2.3 |
| DN_005 | Cơ khí (HS 84) | DNCX | 3 | (sạch — minh chứng hệ thống không phát hiện bừa) |

> **Chờ Trọng Tín cung cấp:** dữ liệu nền từ 5 khách hàng thực tế (đã ẩn danh). Phương án mô phỏng sai phạm trên dữ liệu nền sạch.

### 6.2 Ẩn danh dữ liệu

| Trường ẩn | Cách thay |
|---|---|
| Tên doanh nghiệp | DN_001 ... DN_005 |
| Mã số thuế | dãy số ngẫu nhiên |
| Tên cá nhân | "Cán bộ A", "Đại diện DN" |
| Tên nhà cung cấp | NCC_001 ... |
| Địa chỉ | Tỉnh giả định |

| Trường giữ nguyên | Lý do |
|---|---|
| Mã HS | Cần để minh hoạ kiểm tra C3.2, C6.5, Nhóm 7 |
| Mã loại hình (E11/E13/E42…) | Dữ liệu lõi, không nhạy cảm |
| Tên vật tư | Cần để minh hoạ đối chiếu gần giống (C3.3, C4.4); thay bằng tên chung kèm biến thể |
| Số lượng / giá trị | Cần để minh hoạ phát hiện giá trị bất thường; có thể nhân với hằng số |

### 6.3 Kịch bản trình diễn 5 phút

```
0:00 — Đăng nhập cán bộ Hải quan → Bảng tổng quan 5 doanh nghiệp
0:30 — 5 doanh nghiệp được xếp hạng theo điểm rủi ro:
         #1 DN_001 (điểm rủi ro 87) — 4 phát hiện nghiêm trọng
         #2 DN_002 (76) — 3 phát hiện nghiêm trọng
         #3 DN_004 (68)
         #4 DN_003 (54)
         #5 DN_005 (12) — sạch
1:00 — Chọn DN_001 → trang chi tiết doanh nghiệp
         Các thẻ: Phát hiện / So sánh liên kỳ / Tờ khai gốc / Mẫu 15/15a/16
1:30 — Chọn phát hiện "C6.1 Tồn đầu kỳ N khác tồn cuối kỳ N-1"
         Ô bên trái: Tồn cuối năm 2023 của 5 mã nguyên vật liệu
         Ô bên phải: Tồn đầu năm 2024 của cùng 5 mã — chênh lệch
         Ghi chú: "Điều chỉnh tồn giữa 2 kỳ không có giải trình"
2:30 — Chọn phát hiện "C4.3 Tổng tiêu hao M16 vượt M15"
         Bảng: Sản phẩm TP_X sản xuất 1.000 cái, định mức M16 = 5 kg/cái
                Tính ra: 5.000 kg nguyên vật liệu X cần tiêu hao
                M15 cột xuất sản xuất X: 4.000 kg thực tế
                Chênh lệch: 1.000 kg nguyên vật liệu "biến mất"
3:30 — Chọn phát hiện "C3.3 Đơn vị tính không nhất quán"
         BCCT khai 1.000 kg, M15 khai 1.000 cái → lệch 1.000 lần
4:00 — Chọn "Xuất báo cáo kiến nghị kiểm tra" → file Excel kèm:
         + Danh sách 4 phát hiện
         + Trích xuất chứng cứ (dòng BCCT cụ thể)
         + Trích yếu pháp lý (TT 39/2018, TT 38/2015)
4:30 — Quay lại bảng tổng quan, chọn DN_005 (điểm 12) → 0 phát hiện nghiêm trọng
         "Hệ thống không phát hiện bừa — doanh nghiệp tốt vẫn được xếp hạng thấp"
5:00 — Kết thúc.
```

---

## 7. Lộ trình triển khai

### 7.1 Giai đoạn 1 — Thử nghiệm và trình diễn (đề xuất 4-6 tuần)

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 1 | Khởi tạo dự án + kiến trúc nền | Bộ khung chạy được, tái sử dụng bộ đọc và cấu hình từ BCQT-System |
| 2 | Bộ đọc Excel (Mẫu 15/15a/16 + BCCT) + Tầng dữ liệu 0-1 | Nạp được 1 doanh nghiệp, truy vấn được |
| 3 | Cài 8-10 kiểm tra đầu tiên (Nhóm 1, 2) | Phát hiện hiện trên màn hình, có chứng cứ truy nguồn |
| 4 | Hoàn thành 15 kiểm tra cho trình diễn + tính điểm rủi ro | Bảng tổng quan + xếp hạng |
| 5 | Dữ liệu giả lập 5 DN × 3-4 năm + ẩn danh | Dữ liệu trình diễn hoàn chỉnh |
| 6 | Hoàn thiện giao diện + tổng duyệt trình diễn + đóng gói | Sẵn sàng giới thiệu |

### 7.2 Giai đoạn 2 — Triển khai thí điểm tại Chi cục (đề xuất 3-6 tháng sau khi cơ quan Hải quan phê duyệt giai đoạn 1)

- Triển khai tại **Chi Cục Hải Quan Khu vực IV**.
- Nạp dữ liệu doanh nghiệp trong phạm vi quản lý (dữ liệu thực, không giả lập).
- Cán bộ Hải quan dùng thực tế, phản hồi để cải tiến.
- Cài thêm 13 kiểm tra còn lại (đang chờ).
- Bắt đầu gom dữ liệu để so sánh giữa các doanh nghiệp (Nhóm 7) khi đã có ≥30 doanh nghiệp.

### 7.3 Giai đoạn 3 — Vận hành chính thức (đề xuất 12 tháng trở lên)

- Mở rộng nhiều Chi cục.
- Tích hợp trực tiếp với cơ sở dữ liệu VNACCS (không qua Excel xuất ra nữa).
- Cổng cho doanh nghiệp nộp trực tiếp dữ liệu có cấu trúc.
- Hoàn thiện Nhóm 7 (so sánh giữa các doanh nghiệp).
- Bổ sung học máy hỗ trợ phát hiện (sau khi có >3 năm dữ liệu vận hành).

### 7.4 Vai trò các bên

| Bên | Giai đoạn 1 (Thử nghiệm) | Giai đoạn 2 (Thí điểm) | Giai đoạn 3 (Chính thức) |
|---|---|---|---|
| Tinsu AI | Xây dựng hệ thống, dữ liệu giả lập | Bảo trì, nghiên cứu kiểm tra mới | Vận hành, mở rộng |
| Trọng Tín | Cung cấp kinh nghiệm nghiệp vụ, dữ liệu nền đã ẩn danh | Đào tạo cán bộ, đầu mối nghiệp vụ | Tư vấn |
| Cơ quan Hải quan | Đơn vị đặt vấn đề, phản hồi thiết kế | Cán bộ dùng thử, cung cấp dữ liệu Chi cục | Khách hàng chính thức |

> **Quan trọng:** Dữ liệu của Trọng Tín chỉ dùng để **xây dựng và trình diễn công cụ**. Khi cơ quan Hải quan vận hành chính thức, hệ thống chạy trên dữ liệu của cơ quan Hải quan. Trọng Tín không chuyển dữ liệu khách hàng sang cơ quan Hải quan ngoài bối cảnh doanh nghiệp tự nộp BCQT.

---

## 8. Câu hỏi mở cho phía Hải quan

Đây là các nội dung cần phản hồi từ cơ quan Hải quan trước khi hoàn thiện đề án và bắt đầu xây dựng.

### 8.1 Về phạm vi nghiệp vụ

1. Trong 31 kiểm tra đề xuất, có kiểm tra nào cơ quan Hải quan đặc biệt quan tâm, hoặc có kiểm tra nào quan trọng mà đề án bỏ sót?
2. Báo cáo Excel kiến nghị kiểm tra có cần theo mẫu chính thức nào không?
3. Hiện tại Chi cục đang dùng công cụ hoặc quy trình nào để chọn doanh nghiệp kiểm tra? Audit-HQ tích hợp hay thay thế?
4. Ngưỡng đề xuất (Nghiêm trọng / Cảnh báo / Thông tin) có phù hợp thực tế nghiệp vụ không? Cần điều chỉnh gì?

### 8.2 Về dữ liệu

5. Hệ thống xử lý dữ liệu điện tử của cơ quan Hải quan có lưu Mẫu 15/15a/16 dưới dạng có cấu trúc, hay chỉ là tệp Excel đính kèm?
6. Dữ liệu TKXNK xuất từ VNACCS có cấu trúc thống nhất cho mọi Chi cục không?
7. Quyền truy cập dữ liệu nhiều năm: hệ thống VCIS-VNACCS đã cho phép truy vấn trực tiếp, hay phải xin từng kỳ?

### 8.3 Về kỹ thuật và vận hành

8. Hệ thống đặt tại trụ sở cơ quan Hải quan hay đặt trên máy chủ của Tinsu? Yêu cầu bảo mật cụ thể?
9. Có yêu cầu chứng nhận an toàn thông tin cấp nào?
10. Cam kết chất lượng dịch vụ (SLA) cần đáp ứng cho giai đoạn thí điểm / vận hành chính thức?
11. Cán bộ tại Chi Cục Hải Quan Khu vực IV có thể tiếp nhận hệ thống ở mức kỹ thuật nào? Cần đào tạo bao nhiêu?

### 8.4 Về pháp lý và ranh giới

12. Audit-HQ chỉ đưa ra **gợi ý**, không phải kết luận điều tra. Đồng ý cách dùng này?
13. Trường hợp doanh nghiệp khiếu nại kết quả phát hiện của hệ thống, cơ quan Hải quan có cần Tinsu hỗ trợ giải trình kỹ thuật không?
14. Quyền sở hữu trí tuệ đối với danh mục kiểm tra: thuộc cơ quan Hải quan, Tinsu, hay chia sẻ chung?

---

## 9. Phụ lục

### 9.1 Giải thích thuật ngữ

| Thuật ngữ | Định nghĩa |
|---|---|
| BCQT | Báo cáo Quyết toán |
| BCCT | Báo cáo Chi tiết (tổng hợp TKXNK) |
| TKXNK | Tờ khai Xuất Nhập khẩu |
| DNCX | Doanh nghiệp Chế xuất |
| GC | Gia công |
| SXXK | Sản xuất Xuất khẩu |
| KTSTQ | Kiểm tra Sau Thông quan |
| NVL | Nguyên Vật Liệu |
| TP | Thành Phẩm |
| BTP | Bán Thành Phẩm |
| Mẫu 15 | Báo cáo cân đối nguyên vật liệu (BCQT-NVL) |
| Mẫu 15a | Báo cáo cân đối thành phẩm (BCQT-SP) |
| Mẫu 16 | Định mức thực tế (ĐMTT) |
| VNACCS | Hệ thống thông quan tự động Việt Nam |
| Mã HS | Mã hài hoà mô tả hàng hoá quốc tế |
| E11 / E13 / E15 | Mã loại hình nhập DNCX (nguyên vật liệu / máy móc / gia công) |
| E21 / E23 | Mã loại hình nhập gia công |
| E31 / E33 | Mã loại hình nhập SXXK |
| E42 / E52 / E62 | Mã loại hình xuất tương ứng |
| B13 | Tái xuất |
| A42 | Chuyển mục đích sử dụng nội địa |

### 9.2 Tham chiếu

- TT 38/2015/TT-BTC, TT 39/2018/TT-BTC, TT 121/2025/TT-BTC
- QĐ 1357/QĐ-TCHQ ngày 18/05/2021
- Luật Hải quan 2014, Luật Quản lý Thuế 2019, Luật Sở hữu Trí tuệ
- Hệ thống BCQT-System (Tinsu AI) — kiến trúc, bộ đọc, lớp tiếp nhận biến thể
- Danh sách kiểm tra BCQT (Tinsu AI, phiên bản 1.0 ngày 13/05/2026) — 28 kiểm tra cơ sở

### 9.3 Lịch sử bản

| Phiên bản | Ngày | Tác giả | Thay đổi |
|---|---|---|---|
| Bản nháp 1 | 2026-05-13 | Tinsu AI | Bản đầu — chờ vòng phản hồi đầu tiên |
| Bản nháp 2 | 2026-05-13 | Tinsu AI | Tổng hợp với danh sách 28 kiểm tra từ BCQT showcase; cụ thể hoá đơn vị tiếp nhận (Chi Cục Hải Quan Khu vực IV); làm rõ Excel BCQT có định dạng chuẩn; tổng quát hoá tham chiếu cơ quan Hải quan |
| Bản nháp 3 | 2026-05-13 | Tinsu AI | Việt hoá toàn bộ thuật ngữ kỹ thuật; loại bỏ tiếng Anh trộn lẫn để phù hợp với cán bộ Hải quan |

---

> **Đây là bản dự thảo lần 3.** Mọi nội dung là đề xuất sơ bộ và sẽ được điều chỉnh theo phản hồi của cơ quan Hải quan qua các vòng tổng hợp tiếp theo.
