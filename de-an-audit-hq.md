# Đề án: Audit-HQ

**Hệ thống hỗ trợ quản lý rủi ro và phát hiện sai phạm trong Báo cáo Quyết toán Hải quan (BCQT) và Tờ khai Xuất Nhập khẩu (TKXNK)**

> **Bản dự thảo lần 6** — 2026-05-14
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
| Cán bộ kiểm tra sau thông quan | Sử dụng chứng cứ do hệ thống nêu ra trong quá trình kiểm tra thực tế | Theo từng vụ việc |

### 1.4 Cơ sở pháp lý tham chiếu

- Luật Hải quan 2014, Điều 16-17 (Áp dụng quản lý rủi ro)
- TT 38/2015/TT-BTC, sửa đổi bởi TT 39/2018/TT-BTC, tham chiếu TT 121/2025/TT-BTC
- QĐ 1357/QĐ-TCHQ ngày 18/05/2021 (Mã loại hình xuất nhập khẩu)
- Luật Quản lý Thuế 2019, Điều 99 (Bí mật thông tin người nộp thuế)
- Nghị định 13/2023/NĐ-CP (Bảo vệ dữ liệu cá nhân)

---

## 2. Nguyên tắc thiết kế

### 2.1 Định hướng theo rủi ro, không kiểm tra đại trà

Hệ thống không kiểm tra toàn bộ doanh nghiệp — chỉ xếp hạng theo mức rủi ro để cán bộ phân bổ nguồn lực kiểm tra đúng chỗ.

### 2.2 Có chứng cứ truy nguồn, không "hộp đen"

Mỗi phát hiện hệ thống đưa ra phải:
- Trỏ về dòng dữ liệu cụ thể trong BCCT hoặc Mẫu (số tờ khai, dòng hàng, mã NVL/sản phẩm)
- Nêu rõ điều khoản pháp lý liên quan
- Cho phép cán bộ giải trình khi báo cáo cấp trên hoặc đối thoại với doanh nghiệp

Mọi kiểm tra đều theo **quy tắc xác định** (cho cùng dữ liệu thì cho cùng kết quả). Trí tuệ nhân tạo (AI) dùng vào việc hỗ trợ:
- Chuẩn hoá tên hàng hoá (đối chiếu tên gần giống)
- Sinh giải thích tiếng Việt dễ đọc cho phát hiện
- Gợi ý ánh xạ mã hàng (chỉ là gợi ý, cán bộ quyết định)

### 2.3 Danh mục kiểm tra mở rộng được

Mỗi loại kiểm tra là một mô-đun độc lập. Thêm kiểm tra mới = thêm một mô-đun, không phải sửa phần lõi. Cán bộ Hải quan (qua phối hợp với Tinsu) có thể đề xuất quy tắc mới theo nghiệp vụ thực tế phát hiện.

### 2.4 Ngưỡng có thể điều chỉnh

Hệ thống có ngưỡng mặc định cho mỗi kiểm tra (Nghiêm trọng / Cảnh báo / Thông tin). Cơ quan Hải quan có toàn quyền điều chỉnh ngưỡng theo thực tế nghiệp vụ, theo loại hình doanh nghiệp, hoặc theo ngành hàng.

### 2.5 An toàn pháp lý

- Lớp ẩn danh cho dữ liệu trình diễn (bảo vệ bí mật doanh nghiệp trong giai đoạn thử nghiệm).
- Nhật ký thao tác đầy đủ cho mọi thao tác thay đổi dữ liệu.
- Không thay đổi dữ liệu gốc — mọi đánh dấu và phát hiện là lớp phủ riêng biệt.

### 2.6 Cộng dồn rủi ro

Hệ thống không chỉ xếp hạng doanh nghiệp theo phát hiện Nghiêm trọng đơn lẻ. **Nhiều cảnh báo mức thấp phát sinh đồng thời có thể phản ánh rủi ro tổng thể cao hơn một cảnh báo Nghiêm trọng đơn lẻ.** Điểm rủi ro tổng hợp được tính dồn từ tất cả phát hiện trong kỳ, có trọng số theo mức độ. Cán bộ thấy được cả hai góc nhìn:

- **Điểm tổng** (cộng dồn) — xếp hạng tổng thể của doanh nghiệp
- **Phát hiện Nghiêm trọng riêng lẻ** — sự kiện cần xử lý ngay không phụ thuộc tổng điểm

---

## 3. Phạm vi thử nghiệm ban đầu

### 3.1 Dữ liệu đầu vào — chỉ dùng TKXNK và BCQT đã nộp

Giai đoạn đầu của Audit-HQ làm việc trên đúng dữ liệu cơ quan Hải quan đã có trong tay — không yêu cầu doanh nghiệp cung cấp gì thêm:

| Loại dữ liệu | Định dạng | Nguồn | Phạm vi thử nghiệm |
|---|---|---|---|
| Mẫu 15 (BCQT-NVL) | Excel có định dạng chuẩn theo TT 39/2018 | Doanh nghiệp nộp qua hệ thống điện tử | 5 DN × 3-4 năm |
| Mẫu 15a (BCQT-SP) | Excel có định dạng chuẩn | Doanh nghiệp nộp | 5 DN × 3-4 năm |
| Mẫu 16 (ĐMTT) | Excel có định dạng chuẩn | Doanh nghiệp nộp | 5 DN × 3-4 năm |
| BCCT TKXNK | Excel xuất từ VNACCS (hoặc doanh nghiệp tổng hợp) | Hệ thống Hải quan | 5 DN × 3-4 năm |

> **Dữ liệu BCQT là Excel có định dạng chuẩn** theo TT 39/2018, không phải tự do. Hệ thống có sẵn bộ đọc xử lý định dạng chuẩn, đồng thời có lớp tiếp nhận biến thể nhỏ giữa các doanh nghiệp.

Giai đoạn sau (mở rộng) có thể yêu cầu doanh nghiệp cung cấp thêm sổ sách kế toán, sổ kho bán thành phẩm, danh mục tài sản cố định, sổ phế liệu — chi tiết tại §4.2.

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
- **Quy mô vận hành chính thức:** Tất cả DNCX/Gia công/SXXK trong phạm vi quản lý, 5 năm dữ liệu.

---

## 4. Danh mục các kiểm tra

> **Bộ ba "tử huyệt" của các vụ truy thu thuế lớn:**
>
> 1. **Định mức (Mẫu 16)** — công cụ chính để hợp thức hoá gian lận
> 2. **Bán thành phẩm (sản phẩm dở dang)** — vùng xám dữ liệu, khó kiểm tra
> 3. **Phế liệu, phế phẩm** — lỗ hổng quản lý tiêu thụ nội địa
>
> Danh mục kiểm tra dưới đây tập trung đáng kể vào ba khu vực này.

Đề án chia danh mục kiểm tra thành **hai giai đoạn** theo dữ liệu cần dùng:

| Giai đoạn | Dữ liệu | Nhóm | Tổng |
|---|---|---|---|
| **Đầu** (§4.1) | TKXNK + BCQT đã nộp | 1, 2, 3, 4, 5, 6, 7 | 32 kiểm tra |
| **Sau** (§4.2) | Cần dữ liệu bổ sung từ doanh nghiệp | 8, 9, 10, 11 | 12 kiểm tra |

**Trạng thái** trong giai đoạn đầu:
- ✅ Xây dựng và trình diễn trong 2 tháng (15 kiểm tra)
- 🚧 Bổ sung trong giai đoạn thí điểm (14 kiểm tra)
- ⏳ Kích hoạt khi đã có đủ doanh nghiệp trong danh mục (3 kiểm tra Nhóm 7)

**Mức độ:** 🔴 Nghiêm trọng · 🟡 Cảnh báo · 🔵 Thông tin

### 4.0 Loại hình tờ khai theo loại hình doanh nghiệp

| Loại hình DN | Tờ khai nhập | Tờ khai xuất |
|---|---|---|
| **DNCX** — Doanh nghiệp chế xuất | E11, E15, E13 | E42 |
| **Gia công** — Gia công cho thương nhân nước ngoài | E21, E23 | E52, E54 |
| **SXXK** — Sản xuất xuất khẩu | E31, E33 | E62 |

> Tái xuất: B13 áp dụng chung. Chuyển mục đích sử dụng: A42 khi chuyển nội địa.

---

## 4.1 Giai đoạn đầu — Kiểm tra trên TKXNK và BCQT

> Các kiểm tra dưới đây thực hiện trên đúng dữ liệu cơ quan Hải quan đã có sẵn (TKXNK từ VNACCS + Mẫu 15/15a/16 doanh nghiệp đã nộp). Không yêu cầu doanh nghiệp cung cấp thêm dữ liệu nào.

### Nhóm 1 — Số lượng nhập / xuất (6 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C1.1** | Lệch số lượng nhập nguyên vật liệu (M15 so với tờ khai) — `nhập_trong_kỳ` (M15) khác Σ tờ khai nhập theo mã. Loại hình: DNCX E11+E15 / Gia công E21+E23 / SXXK E31+E33. Ngưỡng: <5% Thông tin · 5–20% Cảnh báo · >20% Nghiêm trọng. | Khai thiếu hoặc khai thừa nhập khẩu. | 🟡 | ✅ |
| **C1.2** | Có tờ khai nhập nhưng không có trong M15 — mã có trên BCCT nhưng không có dòng trong M15. Đánh dấu mọi trường hợp. | Bỏ sót nguyên vật liệu nhập khẩu khỏi BCQT. | 🔴 | ✅ |
| **C1.3** | Có trong M15 nhưng không có tờ khai — `nhập_trong_kỳ` > 0 mà không có tờ khai tương ứng. | M15 không có căn cứ tờ khai; doanh nghiệp có thể "mượn" mã nguyên vật liệu nhập khẩu để hợp thức hoá hàng mua nội địa không hoá đơn hoặc hàng nhập khẩu không khai báo, đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C1.4** | Lệch số lượng xuất thành phẩm (M15a so với tờ khai) — `xuất_khẩu` khác Σ tờ khai xuất theo mã thành phẩm. Loại hình: DNCX E42 / Gia công E52 / SXXK E62. Ngưỡng: <1% Thông tin · 1–5% Cảnh báo · >5% Nghiêm trọng. | Khai sai sản lượng xuất khẩu — có thể khai khống xuất khẩu để giảm lượng nguyên vật liệu miễn thuế phải giải trình, hoặc khai thiếu xuất khẩu để giấu nguồn thu. | 🟡 | ✅ |
| **C1.5** | Tái xuất M15 không có tờ khai B13 — `xuất_trả_lại` > 0 trong M15 nhưng không có B13 tương ứng. | Ghi tái xuất để giảm tồn nhưng không có tờ khai chứng minh. | 🟡 | 🚧 |
| **C1.6** | Chuyển mục đích sử dụng không có tờ khai A42 — `chuyển_mục_đích_sử_dụng` > 0 nhưng không có A42. | Hàng miễn thuế chuyển nội địa không khai báo — vi phạm điều kiện miễn thuế. | 🔴 | ✅ |

### Nhóm 2 — Cân bằng và tồn kho (5 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C2.1** | Mất cân bằng phương trình M15 — `tồn_cuối` khác `tồn_đầu` + `nhập` − `xuất_trả` − `xuất_sản_xuất` − `chuyển_mục_đích_sử_dụng` − `xuất_khác`. Ngưỡng: chênh lệch khác 0 (cho phép ±0,01 làm tròn). | Báo cáo không đáng tin cậy về mặt số học; có thể do lỗi nhập liệu, không khớp giữa các nguồn dữ liệu nội bộ doanh nghiệp, hoặc dữ liệu bị ghép từ nhiều bộ phận không đồng nhất. Phải làm rõ từng cột thành phần trước khi đánh giá các kiểm tra khác trên cùng kỳ. | 🔴 | ✅ |
| **C2.2** | Mất cân bằng phương trình M15a — `tồn_cuối` khác `tồn_đầu` + `nhập_kho` − `chuyển_mục_đích_sử_dụng` − `xuất_khẩu` − `xuất_khác`. | Báo cáo cân đối thành phẩm không đáng tin cậy về mặt số học; có thể do lỗi nhập liệu hoặc số liệu sản xuất/xuất khẩu/tồn không khớp giữa các nguồn nội bộ. Phải làm rõ từng cột trước khi đánh giá các kiểm tra khác. | 🔴 | ✅ |
| **C2.3** | Tồn cuối âm — nguyên vật liệu (M15) — `tồn_cuối_kỳ` < 0 trên bất kỳ mã nào. | Khả năng bỏ sót tờ khai nhập khẩu, sử dụng nguyên vật liệu không khai báo, hoặc điều chỉnh số liệu tồn kho không đúng thực tế. | 🔴 | ✅ |
| **C2.4** | Tồn cuối âm — thành phẩm (M15a) — `tồn_cuối_kỳ` < 0 trên bất kỳ mã nào. | Tương tự C2.3 cho thành phẩm — bỏ sót tờ khai, sử dụng hàng không khai báo, hoặc điều chỉnh số liệu tồn kho sai thực tế. | 🔴 | 🚧 |
| **C2.5** | Tồn cuối lớn hơn nhập khi tồn đầu bằng 0 — `tồn_đầu_kỳ` = 0 nhưng `tồn_cuối_kỳ` > `nhập_trong_kỳ`. | "Tồn kho ảo" để treo nợ thuế — doanh nghiệp thực tế đã tiêu thụ hàng nhưng trên báo cáo vẫn thể hiện tồn kho lớn để không phải nộp thuế nhập khẩu. | 🔴 | 🚧 |

### Nhóm 3 — Phân loại hàng hoá (3 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C3.1** | Cùng mã vật tư khai nhiều loại hình mâu thuẫn — một mã có trên cả tờ khai nguyên vật liệu và tờ khai máy móc thiết bị trong cùng kỳ. Cặp mâu thuẫn: E11+E13 · E31+E13 · E21+E13. | Phân loại sai dẫn đến sai phạm vi BCQT. | 🟡 | ✅ |
| **C3.2** | Mã HS không nhất quán trong kỳ (cùng mã vật tư) — ≥2 mã HS khác nhau trên các tờ khai. Ngưỡng: Khác phân nhóm (6 số) Thông tin · khác nhóm (4 số) Cảnh báo · khác chương (2 số) Nghiêm trọng. | Cố ý thay đổi mã HS để né các chính sách quản lý chuyên ngành (kiểm tra chất lượng, kiểm dịch) hoặc để hưởng thuế suất ưu đãi đặc biệt bất hợp pháp. | 🟡🔴 | ✅ |
| **C3.3** | Đơn vị tính không nhất quán (cùng mã vật tư) — ≥2 đơn vị khác nhau giữa M15 và BCCT. | Sai đơn vị tính ×1000 khiến toàn bộ nhập/xuất/tồn sai hệ thống. | 🔴 | ✅ |

### Nhóm 4 — Định mức M16 (7 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C4.1** | Nguyên vật liệu trong M16 không có nhập khẩu trong M15 — `mã_NVL` trong M16 nhưng `nhập_trong_kỳ` = 0 hoặc không có dòng trong M15. | Không thể giải trình dòng vật tư từ tờ khai đến thành phẩm xuất khẩu. | 🔴 | ✅ |
| **C4.2** | Thành phẩm trong M16 không có trong M15a — `mã_SP_xuất_khẩu` trong M16 nhưng không có dòng trong M15a. | Định mức cho thành phẩm không có trong báo cáo xuất khẩu. | 🟡 | 🚧 |
| **C4.3** | Tổng tiêu hao tính theo M16 vượt xuất sản xuất M15 — Σ(`định_mức` × `xuất_khẩu_M15a`) theo mã nguyên vật liệu > `xuất_sản_xuất` trong M15. Ngưỡng: vượt >5% Cảnh báo · >20% Nghiêm trọng. | Đây là cách phổ biến nhất để lấy nguyên vật liệu miễn thuế ra bán nội địa — xây dựng định mức ảo bao gồm cả những thành phần không có thực trong sản phẩm, thổi phồng tiêu hao để hợp thức hoá nguyên vật liệu nhập khẩu dư. | 🟡🔴 | ✅ |
| **C4.4** | M16 phân mảnh: nhiều nguyên vật liệu cùng chức năng cho một thành phẩm. **Ví dụ thực tế**: 1 chiếc áo có 10 loại cúc khác nhau trong M16. Cách phát hiện: (A) ≥N mã có cùng HS 4 số trong 1 thành phẩm (mặc định) · (B) gom nhóm tên gần giống (xử lý ngôn ngữ tự nhiên) · (C) cơ quan Hải quan định nghĩa danh mục nhóm vật tư. Ngưỡng: ≥5 mã cùng HS / thành phẩm Cảnh báo · ≥10 Nghiêm trọng. | Phân mảnh nguyên vật liệu để che số lượng, hợp thức hoá nhập khẩu dư. | 🟡 | 🚧 |
| **C4.5** | Định mức bằng 0 hoặc âm — `định_mức_thực_tế` ≤ 0 trên bất kỳ dòng M16 nào. | Lỗi dữ liệu hoặc cố tình khai 0 để che tiêu hao thực tế. | 🔴 | 🚧 |
| **C4.6** | Định mức bất thường cao (giá trị ngoại lai thống kê) — `định_mức` cặp thành phẩm-nguyên vật liệu vượt xa giá trị trung bình toàn dữ liệu. Ngưỡng: vượt trung bình ±3 độ lệch chuẩn Cảnh báo · ±5 độ lệch chuẩn Nghiêm trọng. | Thổi phồng định mức để hợp thức hoá nguyên vật liệu nhập khẩu vượt mức. | 🟡 | 🚧 |
| **C4.7** | Phân bổ định mức bất thường (mở rộng từ C4.4) — phát hiện: (a) cùng cặp thành phẩm-NVL có nhiều định mức khác nhau trong cùng kỳ; (b) một nguyên vật liệu được dùng cho quá nhiều thành phẩm không liên quan; (c) một thành phẩm có số lượng dòng nguyên vật liệu vượt ngưỡng hợp lý của ngành. | phân mảnh định mức để hợp thức hoá nhiều mã NVL nhập khẩu, gây khó truy nguồn và che giấu lượng NVL dư / thất thoát · điều chỉnh định mức tuỳ ý để cân đối tồn kho · khai báo định mức quá rộng để hợp thức hoá NVL nhập khẩu miễn thuế cho thành phẩm không phù hợp thực tế sản xuất · có dấu hiệu tính toán / nguỵ tạo định mức nhân tạo để chế số liệu quyết toán thay vì phản ánh tiêu hao sản xuất thực tế. | 🟡🔴 | 🚧 |

### Nhóm 5 — Truy nguồn nguyên vật liệu nhập khẩu (3 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C5.1** | NVL có xuất sản xuất trong M15 nhưng không có nhập khẩu — `xuất_sản_xuất` > 0 và `nhập_trong_kỳ` = 0 và `tồn_đầu_kỳ` = 0. | Tiêu hao từ nguồn không khai báo — nguyên vật liệu nội địa bị đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C5.2** | Thành phẩm xuất khẩu không có trong M16 (thành phẩm "mồ côi") — mã thành phẩm có `xuất_khẩu` > 0 trong M15a nhưng không có dòng M16. | Không thể giải trình nguyên vật liệu đầu vào cho thành phẩm đã xuất khẩu; doanh nghiệp có thể dùng nguyên liệu không rõ nguồn gốc (kể cả hàng lậu) để sản xuất xuất khẩu. | 🟡 | 🚧 |
| **C5.3** | Tỷ lệ truy nguồn thấp theo mã nguyên vật liệu — Σ(`định_mức` × `xuất_khẩu_M15a`) / `xuất_sản_xuất_M15` thấp dưới ngưỡng. Ngưỡng: <80% Cảnh báo · <60% Nghiêm trọng. | Phần lớn nguyên vật liệu nhập khẩu không truy được vào thành phẩm xuất khẩu cụ thể. | 🟡 | 🚧 |

### Nhóm 6 — Kiểm tra liên kỳ (5 kiểm tra)

*Cần dữ liệu ≥2 kỳ BCQT.*

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C6.1** | Tồn đầu kỳ N khác tồn cuối kỳ N-1 — nguyên vật liệu (M15) — theo từng mã. | Điều chỉnh tồn giữa 2 kỳ không có giải trình. | 🔴 | ✅ |
| **C6.2** | Tồn đầu kỳ N khác tồn cuối kỳ N-1 — thành phẩm (M15a) — tương tự C6.1 cho thành phẩm. | — | 🔴 | 🚧 |
| **C6.3** | Định mức M16 thay đổi đột biến giữa các kỳ — chênh lệch tỷ lệ giữa định mức kỳ N và kỳ N-1 vượt ngưỡng (cùng cặp thành phẩm-nguyên vật liệu). Ngưỡng: >20% Cảnh báo · >50% Nghiêm trọng. | Thổi phồng hoặc co định mức để điều tiết lượng nguyên vật liệu cần giải trình. | 🟡 | 🚧 |
| **C6.4** | Nhập tăng mạnh nhưng xuất khẩu không tăng tương ứng — `nhập_trong_kỳ` tăng >X% trong khi `xuất_khẩu` tăng <Y%. Ngưỡng: nhập tăng >50% trong khi xuất tăng <10% Cảnh báo. | Tích luỹ tồn nguyên vật liệu bất thường, nguy cơ chuyển nội địa không khai báo A42. **Cảnh báo đặc biệt:** doanh nghiệp sắp giải thể, bỏ trốn — tranh thủ nhập lượng lớn hàng miễn thuế rồi tẩu tán ra thị trường trước khi đóng mã số thuế. | 🟡 | 🚧 |
| **C6.5** | Mã HS thay đổi cho cùng mã vật tư giữa các kỳ — Ngưỡng: đổi nhóm (4 số) Cảnh báo · đổi chương (2 số) Nghiêm trọng. | Phân loại lại để chuyển sang nhóm thuế suất hoặc chính sách có lợi hơn. | 🟡🔴 | 🚧 |

### Nhóm 7 — So sánh giữa các doanh nghiệp (3 kiểm tra)

*Kích hoạt khi cơ quan Hải quan đã có đủ doanh nghiệp trong danh mục (≥30 doanh nghiệp cùng ngành).*

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C7.1** | Định mức bất thường so với cùng ngành — định mức doanh nghiệp vượt mức trung bình ngành (cùng chương HS hoặc cùng loại sản phẩm) một khoảng lớn. | — | 🟡 | ⏳ |
| **C7.2** | Giá nhập từ cùng nhà cung cấp chênh lệch giữa các doanh nghiệp — cùng nhà cung cấp, cùng mã HS, giá khác nhau lớn. | Chuyển giá hoặc trốn thuế có hệ thống. | 🟡🔴 | ⏳ |
| **C7.3** | Lượng nhập / xuất cùng mã HS bất thường so với mức chung ngành — vượt xa giá trị trung vị của ngành. | Quy mô bất thường cần kiểm tra. | 🟡 | ⏳ |

---

## 4.2 Giai đoạn sau — Kiểm tra mở rộng, cần dữ liệu bổ sung

> Các nhóm kiểm tra dưới đây yêu cầu **dữ liệu ngoài TKXNK và BCQT**. Doanh nghiệp sẽ cung cấp thêm theo yêu cầu của cơ quan Hải quan. Đây là giai đoạn mở rộng, triển khai sau khi giai đoạn đầu đã ổn định.
>
> Đây là khu vực **bộ ba "tử huyệt"** — định mức, bán thành phẩm, phế liệu — nơi xảy ra phần lớn các vụ truy thu thuế lớn.

### Nhóm 8 — Phế liệu và phế phẩm (3 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** sổ kho phế liệu, hoá đơn bán phế liệu nội địa, danh mục tờ khai A42 đã nộp cho phế liệu.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C8.1** | Tỷ lệ phế liệu / phế phẩm thực tế vượt ngưỡng ngành — cặp NVL-thành phẩm có tỷ lệ phế thải cao bất thường so với mặt bằng ngành. | Khai phế liệu cao để giảm lượng NVL cần giải trình hoặc che tiêu thụ nội địa. | 🟡 | ⏳ |
| **C8.2** | Phế liệu bán nội địa không có tờ khai chuyển mục đích sử dụng (A42) — doanh nghiệp ghi nhận bán phế liệu trong sổ sách nhưng không có A42 tương ứng. | Vi phạm điều kiện miễn thuế — phế liệu phát sinh từ NVL miễn thuế, bán nội địa phải khai A42 và nộp thuế. | 🔴 | ⏳ |
| **C8.3** | Tỷ lệ phế liệu thay đổi đột biến giữa các kỳ — tỷ lệ phế thải kỳ N cao bất thường so với kỳ N-1 (cùng dây chuyền sản xuất). | Điều tiết phế liệu để cân đối số liệu tồn kho qua các kỳ. | 🟡 | ⏳ |

### Nhóm 9 — Sản phẩm dở dang (bán thành phẩm) (4 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** sổ kho bán thành phẩm, sổ sản xuất, sơ đồ công đoạn, định mức từng tầng bán thành phẩm.
>
> Bán thành phẩm là **vùng xám dữ liệu** lớn nhất: có thể đã tiêu hao một phần NVL, chưa hoàn thiện để xuất khẩu, luân chuyển qua nhiều công đoạn hoặc nhiều kỳ. Mỗi doanh nghiệp có cách định nghĩa BTP khác nhau, dễ phát sinh nhiều tầng (cấp 1, cấp 2, tái chế, gia công lại) — không có chuẩn hoá tuyệt đối.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C9.1** | BTP đa tầng không truy nguồn được về NVL gốc — BTP cấp 1, 2, 3... không có liên kết về nguyên vật liệu ban đầu. | Làm mờ truy nguồn — NVL đã nhập khẩu "nằm" trong BTP nhiều tầng, đối chiếu với thành phẩm xuất khẩu không còn tuyến tính. | 🟡 | ⏳ |
| **C9.2** | Tồn BTP cuối kỳ N khác tồn BTP đầu kỳ N+1 — biến động không có giải trình. | BTP bị "đẩy qua lại" giữa các kỳ để điều chỉnh tồn kho mà không thay đổi dòng thực tế. | 🟡 | ⏳ |
| **C9.3** | Tồn BTP lớn không tương xứng với năng lực sản xuất khai báo — số lượng BTP tồn vượt xa năng lực dây chuyền. | Che giấu tiêu thụ nội địa — NVL đã đưa vào BTP nhưng thực tế bị tiêu thụ / bán nội địa, khó phát hiện vì chưa "ra thành phẩm". | 🟡 | ⏳ |
| **C9.4** | Cấu thành NVL của BTP không khớp giữa định mức khai báo và sổ kho thực tế — định mức tầng BTP tính ra khác lượng NVL đã xuất kho cho BTP đó. | Tách nhỏ một quy trình sản xuất thành nhiều tầng BTP để làm loãng sai lệch định mức, tạo vùng xám dễ lợi dụng. | 🔴 | ⏳ |

### Nhóm 10 — Đối chiếu sổ sách kế toán (3 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** Bảng cân đối phát sinh, sổ chi tiết các tài khoản 152 (NVL), 155 (Thành phẩm), 156 (Hàng hoá), Báo cáo tài chính kỳ tương ứng.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C10.1** | Tồn kho đầu/cuối kỳ BCQT khác số dư các tài khoản 152, 155, 156 trên Bảng cân đối phát sinh. | Số liệu BCQT không khớp sổ sách kế toán — hai nguồn số liệu mâu thuẫn cần làm rõ. | 🔴 | ⏳ |
| **C10.2** | Doanh thu xuất khẩu sổ sách kế toán khác trị giá xuất khẩu BCCT. | Khai sai một trong hai phía, ảnh hưởng nghĩa vụ thuế. | 🟡🔴 | ⏳ |
| **C10.3** | Giá trị nhập khẩu sổ sách kế toán khác trị giá nhập khẩu BCCT. | Khai sai một trong hai phía hoặc có nguồn nhập không khai báo. | 🟡🔴 | ⏳ |

### Nhóm 11 — Tài sản cố định và máy móc thiết bị (2 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** danh mục tài sản cố định (sổ TSCĐ), báo cáo cơ sở sản xuất, hồ sơ máy móc nhập khẩu miễn thuế.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C11.1** | Máy móc thiết bị miễn thuế nhập khẩu (E13) không khớp danh mục thiết bị trong báo cáo cơ sở sản xuất. | Máy móc miễn thuế đã bán nội địa, chuyển nhượng, hoặc đưa ra khỏi cơ sở mà không khai báo. | 🔴 | ⏳ |
| **C11.2** | Công suất máy móc khai báo không khớp sản lượng thực tế trong BCQT — sản lượng vượt hoặc thấp xa năng lực thiết bị khai báo. | Khai báo công suất không trung thực để được miễn thuế / để hợp thức hoá lượng xuất khẩu. | 🟡 | ⏳ |

---

### 4.3 Tổng hợp

| Giai đoạn | Nhóm | Tổng | ✅ MVP 2 tháng | 🚧 Bổ sung thí điểm | ⏳ Cần thêm điều kiện |
|---|---|---:|---:|---:|---:|
| **Đầu** (TKXNK + BCQT) | 1 — Số lượng nhập/xuất | 6 | 5 | 1 | 0 |
| | 2 — Cân bằng và tồn kho | 5 | 3 | 2 | 0 |
| | 3 — Phân loại hàng hoá | 3 | 3 | 0 | 0 |
| | 4 — Định mức M16 | 7 | 2 | 5 | 0 |
| | 5 — Truy nguồn NVL | 3 | 1 | 2 | 0 |
| | 6 — Liên kỳ | 5 | 1 | 4 | 0 |
| | 7 — So sánh giữa các DN | 3 | 0 | 0 | 3 |
| | **Cộng giai đoạn đầu** | **32** | **15** | **14** | **3** |
| **Sau** (cần dữ liệu bổ sung) | 8 — Phế liệu / phế phẩm | 3 | 0 | 0 | 3 |
| | 9 — Sản phẩm dở dang (BTP) | 4 | 0 | 0 | 4 |
| | 10 — Đối chiếu sổ sách kế toán | 3 | 0 | 0 | 3 |
| | 11 — Tài sản cố định và máy móc | 2 | 0 | 0 | 2 |
| | **Cộng giai đoạn sau** | **12** | **0** | **0** | **12** |
| | **TỔNG TOÀN BỘ** | **44** | **15** | **14** | **15** |

> **Danh mục mở rộng được:** danh mục không cố định ở con số 44. Mỗi nghiệp vụ cơ quan Hải quan phát hiện mới có thể bổ sung vào danh mục như một mô-đun độc lập, không cần thay đổi phần lõi. Ngưỡng đề xuất có thể điều chỉnh theo thực tế.

---

## 5. Kiến trúc hệ thống (sơ bộ)

### 5.1 Mô hình dữ liệu

Hệ thống tổ chức dữ liệu thành 4 tầng:

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
   Tổng hợp điểm rủi ro doanh nghiệp từ phát hiện ở Tầng 2 (theo cơ
   chế cộng dồn tại §2.6). Dùng cho xếp hạng và bảng tổng quan.
```

> **Nguyên tắc lõi:** Mỗi nguồn dữ liệu giữ cấu trúc gốc của nó. Khi cần phân tích đan chéo, hệ thống truy vấn cùng lúc nhiều bảng — không ép tất cả vào một bảng vạn năng.

### 5.2 Hạ tầng kỹ thuật (gửi bộ phận công nghệ thông tin tham khảo)

- **Ngôn ngữ và nền tảng:** Python (đang vận hành trên các hệ thống Tinsu) — phổ biến, ổn định, dễ tuyển nhân sự.
- **Cơ sở dữ liệu:** quan hệ chuẩn (SQLite cho thử nghiệm, PostgreSQL cho thí điểm trở lên).
- **Giao diện:** trang web hiển thị trên trình duyệt thông thường — cán bộ không cần cài phần mềm.
- **Đóng gói:** container (Docker) — triển khai nhanh, đồng bộ giữa các môi trường.
- **Trí tuệ nhân tạo:** dùng máy chủ trung gian nội bộ Tinsu (chung với các hệ thống Tinsu khác).
- **Mô hình triển khai:** một bản triển khai phục vụ một đơn vị Hải quan (cấp Chi cục), có thể đặt tại trụ sở Hải quan hoặc trên máy chủ Tinsu tuỳ yêu cầu.

### 5.3 Vai trò trí tuệ nhân tạo (AI)

AI **không** trực tiếp đưa ra phát hiện sai phạm. AI chỉ làm các việc hỗ trợ sau:

| Công việc | Khi nào dùng | Kết quả |
|---|---|---|
| Chuẩn hoá tên hàng hoá | Khi gặp mô tả không chuẩn trong BCCT/Mẫu | Tên chuẩn (cán bộ xác nhận) |
| Đối chiếu mã hàng gần giống | Khi quy tắc cứng có độ chính xác thấp | Đề xuất ánh xạ (cán bộ xác nhận) |
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

Toàn bộ giai đoạn xây dựng và trình diễn gói gọn trong **2 tháng** (8 tuần) tính từ khi cơ quan Hải quan phê duyệt nguyên tắc đề án. Lộ trình này tập trung vào **giai đoạn đầu** của danh mục kiểm tra (§4.1) — các kiểm tra thực hiện trên dữ liệu TKXNK và BCQT đã nộp.

### 7.1 Tuần 1-2 — Khởi tạo và nền tảng dữ liệu

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 1 | Khởi tạo dự án, dựng kiến trúc nền, tái sử dụng mô-đun từ các hệ thống Tinsu đã vận hành | Bộ khung chạy được trên môi trường nội bộ |
| 2 | Bộ đọc Excel (Mẫu 15/15a/16 + BCCT) + Tầng dữ liệu 0-1 | Nạp được 1 doanh nghiệp, truy vấn được theo mã, theo kỳ |

### 7.2 Tuần 3-4 — Cài đặt 15 kiểm tra cho trình diễn

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 3 | Nhóm 1 (số lượng nhập/xuất) + Nhóm 2 (cân bằng) — 8 kiểm tra đầu | Phát hiện hiện trên màn hình, có chứng cứ truy nguồn về dòng dữ liệu gốc |
| 4 | Nhóm 3, 4, 5, 6 — 7 kiểm tra còn lại + thuật toán cộng dồn điểm rủi ro | Đủ 15 kiểm tra cho trình diễn |

### 7.3 Tuần 5-6 — Dữ liệu trình diễn và giao diện

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 5 | Dữ liệu giả lập 5 doanh nghiệp × 3-4 năm + ẩn danh | Dữ liệu trình diễn hoàn chỉnh, mô phỏng đủ 4 kiểu sai phạm chính |
| 6 | Bảng tổng quan + trang chi tiết doanh nghiệp + xuất Excel kiến nghị kiểm tra | Toàn bộ luồng trình diễn 5 phút chạy được |

### 7.4 Tuần 7-8 — Tổng duyệt và bàn giao

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 7 | Tổng duyệt nội bộ Tinsu × Trọng Tín, sửa lỗi, hoàn thiện tài liệu hướng dẫn | Hệ thống sẵn sàng trình diễn |
| 8 | Trình diễn cho cơ quan Hải quan + bàn giao hồ sơ kỹ thuật + tổng hợp phản hồi | Báo cáo kết quả 2 tháng, đề xuất bước tiếp theo |

### 7.5 Vai trò các bên trong 2 tháng

| Bên | Vai trò chính |
|---|---|
| Tinsu AI | Xây dựng hệ thống, dữ liệu giả lập, tổng duyệt kỹ thuật |
| Trọng Tín | Cung cấp kinh nghiệm nghiệp vụ, dữ liệu nền đã ẩn danh, tổng duyệt nghiệp vụ |
| Cơ quan Hải quan | Phê duyệt nguyên tắc, định hướng nghiệp vụ, tiếp nhận trình diễn |

### 7.6 Định hướng sau 2 tháng

Sau khi trình diễn và nhận phản hồi, tuỳ quyết định của cơ quan Hải quan, các bước tiếp theo có thể bao gồm:

- **Triển khai thí điểm tại Chi Cục Hải Quan Khu vực IV** với dữ liệu doanh nghiệp thực tế; cài tiếp 14 kiểm tra còn lại của giai đoạn đầu (§4.1).
- **Kích hoạt Nhóm 7 so sánh giữa các doanh nghiệp** khi đã có đủ doanh nghiệp trong danh mục.
- **Mở rộng sang giai đoạn sau (§4.2)** — Nhóm 8-11 kiểm tra phế liệu, bán thành phẩm, sổ sách kế toán, tài sản cố định. Cần phối hợp với cơ quan Hải quan để yêu cầu doanh nghiệp cung cấp các dữ liệu bổ sung tương ứng.
- **Tích hợp trực tiếp với VNACCS** thay vì nạp qua tệp Excel xuất ra.
- **Mở rộng sang nhiều Chi cục**.

Các bước này không nằm trong cam kết 2 tháng vì phụ thuộc quyết định của cơ quan Hải quan sau khi xem trình diễn.

> **Quan trọng:** Dữ liệu của Trọng Tín chỉ dùng để **xây dựng và trình diễn công cụ**. Khi cơ quan Hải quan vận hành thực tế, hệ thống chạy trên dữ liệu của cơ quan Hải quan. Trọng Tín không chuyển dữ liệu khách hàng sang cơ quan Hải quan ngoài bối cảnh doanh nghiệp tự nộp BCQT.

---

## 8. Câu hỏi mở cho phía Hải quan

Đây là các nội dung cần phản hồi từ cơ quan Hải quan trước khi hoàn thiện đề án và bắt đầu xây dựng.

### 8.1 Về phạm vi nghiệp vụ

1. Trong 44 kiểm tra đề xuất (32 giai đoạn đầu + 12 giai đoạn sau), có kiểm tra nào cơ quan Hải quan đặc biệt quan tâm, hoặc có kiểm tra nào quan trọng mà đề án bỏ sót?
2. Trong số 15 kiểm tra MVP cho trình diễn 2 tháng, có kiểm tra nào cơ quan Hải quan muốn ưu tiên hơn?
3. Báo cáo Excel kiến nghị kiểm tra có cần theo mẫu chính thức nào không?
4. Hiện tại Chi cục đang dùng công cụ hoặc quy trình nào để chọn doanh nghiệp kiểm tra? Audit-HQ tích hợp hay thay thế?
5. Ngưỡng đề xuất (Nghiêm trọng / Cảnh báo / Thông tin) có phù hợp thực tế nghiệp vụ không? Cần điều chỉnh gì?
6. Cơ chế cộng dồn rủi ro (§2.6) có phù hợp cách đánh giá hiện hành của cơ quan Hải quan không?

### 8.2 Về dữ liệu giai đoạn đầu (TKXNK + BCQT)

7. Hệ thống xử lý dữ liệu điện tử của cơ quan Hải quan có lưu Mẫu 15/15a/16 dưới dạng có cấu trúc, hay chỉ là tệp Excel đính kèm?
8. Dữ liệu TKXNK xuất từ VNACCS có cấu trúc thống nhất cho mọi Chi cục không?
9. Quyền truy cập dữ liệu nhiều năm: hệ thống VCIS-VNACCS đã cho phép truy vấn trực tiếp, hay phải xin từng kỳ?

### 8.3 Về dữ liệu giai đoạn sau (mở rộng)

10. Cơ quan Hải quan có cơ chế yêu cầu doanh nghiệp cung cấp Bảng cân đối phát sinh, sổ tài khoản 152/155/156 không? Tần suất nào hợp lý?
11. Quy định hiện hành về sổ kho bán thành phẩm và danh mục tài sản cố định — doanh nghiệp đã phải lưu trữ chưa? Cơ quan Hải quan có quyền yêu cầu xuất khi cần kiểm tra không?
12. Báo cáo cơ sở sản xuất (theo TT 38/2015) hiện đã được số hoá chưa, hay vẫn ở dạng giấy?

### 8.4 Về kỹ thuật và vận hành

13. Hệ thống đặt tại trụ sở cơ quan Hải quan hay đặt trên máy chủ của Tinsu? Yêu cầu bảo mật cụ thể?
14. Có yêu cầu chứng nhận an toàn thông tin cấp nào?
15. Cam kết chất lượng dịch vụ (SLA) cần đáp ứng cho giai đoạn thí điểm / vận hành chính thức?
16. Cán bộ tại Chi Cục Hải Quan Khu vực IV có thể tiếp nhận hệ thống ở mức nào? Cần đào tạo bao nhiêu?

### 8.5 Về pháp lý và ranh giới

17. Audit-HQ chỉ đưa ra **gợi ý**, không phải kết luận điều tra. Đồng ý cách dùng này?
18. Trường hợp doanh nghiệp khiếu nại kết quả phát hiện của hệ thống, cơ quan Hải quan có cần Tinsu hỗ trợ giải trình kỹ thuật không?
19. Quyền sở hữu trí tuệ đối với danh mục kiểm tra: thuộc cơ quan Hải quan, Tinsu, hay chia sẻ chung?

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
| BTP | Bán Thành Phẩm (sản phẩm dở dang) |
| TSCĐ | Tài sản cố định |
| Mẫu 15 | Báo cáo cân đối nguyên vật liệu (BCQT-NVL) |
| Mẫu 15a | Báo cáo cân đối thành phẩm (BCQT-SP) |
| Mẫu 16 | Định mức thực tế (ĐMTT) |
| TK 152 | Tài khoản kế toán Nguyên vật liệu |
| TK 155 | Tài khoản kế toán Thành phẩm |
| TK 156 | Tài khoản kế toán Hàng hoá |
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

### 9.3 Lịch sử bản

| Phiên bản | Ngày | Tác giả | Thay đổi |
|---|---|---|---|
| Bản nháp 1 | 2026-05-13 | Tinsu AI | Bản đầu — chờ vòng phản hồi đầu tiên |
| Bản nháp 2 | 2026-05-13 | Tinsu AI | Tổng hợp với danh sách 28 kiểm tra; cụ thể hoá đơn vị tiếp nhận (Chi Cục Hải Quan Khu vực IV); làm rõ Excel BCQT có định dạng chuẩn |
| Bản nháp 3 | 2026-05-13 | Tinsu AI | Việt hoá toàn bộ thuật ngữ kỹ thuật; loại bỏ tiếng Anh trộn lẫn để phù hợp với cán bộ Hải quan |
| Bản nháp 4 | 2026-05-13 | Tinsu AI | Bỏ tham chiếu trường hợp cụ thể; xưng hô "cơ quan Hải quan" thay cho "Hải quan" trống không; nén lộ trình triển khai về 2 tháng / 8 tuần |
| Bản nháp 5 | 2026-05-14 | Tinsu AI | Tách danh mục kiểm tra thành 2 giai đoạn (đầu = TKXNK + BCQT; sau = cần dữ liệu bổ sung); thêm "Bộ ba tử huyệt" và §2.6 cộng dồn rủi ro; cập nhật rủi ro 8 kiểm tra; thêm C4.7 phân bổ định mức bất thường; thêm Nhóm 8-11 (phế liệu, BTP, sổ sách kế toán, tài sản cố định / máy móc) — 12 kiểm tra giai đoạn sau; giản lược §5 hạ tầng kỹ thuật |
| Bản nháp 6 | 2026-05-14 | Tinsu AI | Tách các bảng kiểm tra thành 5 cột (Mã / Vấn đề / Rủi ro / Mức / Trạng thái) cho dễ theo dõi; viết lại rủi ro C2.1 và C2.2 (cũ tối nghĩa); bổ sung rủi ro C1.4 (đang thiếu); chỉnh §2.1, §2.2, §2.5; rút quy mô vận hành chính thức từ 10 năm xuống 5 năm dữ liệu; tăng khoảng cách hiển thị danh sách trong giao diện |

---

> **Đây là bản dự thảo lần 6.** Mọi nội dung là đề xuất sơ bộ và sẽ được điều chỉnh theo phản hồi của cơ quan Hải quan qua các vòng tổng hợp tiếp theo.
