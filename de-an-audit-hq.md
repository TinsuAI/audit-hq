# Đề án: Audit-HQ

**Hệ thống hỗ trợ quản lý rủi ro và phát hiện sai phạm trong Báo cáo Quyết toán Hải quan (BCQT) và Tờ khai Xuất Nhập khẩu (TKXNK)**

> **Bản dự thảo lần 10** — 2026-05-14
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

- Lớp ẩn danh cho dữ liệu demo (bảo vệ bí mật doanh nghiệp trong giai đoạn thử nghiệm).
- Nhật ký thao tác đầy đủ cho mọi thao tác thay đổi dữ liệu.
- Không thay đổi dữ liệu gốc — mọi đánh dấu và phát hiện là lớp phủ riêng biệt.

### 2.6 Cộng dồn rủi ro

Hệ thống không chỉ xếp hạng doanh nghiệp theo phát hiện Nghiêm trọng đơn lẻ. **Nhiều cảnh báo mức thấp phát sinh đồng thời có thể phản ánh rủi ro tổng thể cao hơn một cảnh báo Nghiêm trọng đơn lẻ.** Điểm rủi ro tổng hợp được tính dồn từ tất cả phát hiện trong kỳ, có trọng số theo mức độ. Cán bộ thấy được cả hai góc nhìn:

- **Điểm tổng** (cộng dồn) — xếp hạng tổng thể của doanh nghiệp
- **Phát hiện Nghiêm trọng riêng lẻ** — sự kiện cần xử lý ngay không phụ thuộc tổng điểm


### 2.7 Phát hiện kết hợp (combination signatures)

Ngoài cộng dồn điểm rủi ro, hệ thống phát hiện các **mẫu kết hợp** — nhiều kiểm tra cùng kích hoạt theo một bộ ba điển hình của một kiểu sai phạm. Ví dụ:

- **Bộ ba "nhập nội địa ẩn":** C1.3 (M15 có nhưng không có tờ khai) + C5.1 (xuất sản xuất không có nhập) + C8.2 (phế liệu bán không có A42) — pattern doanh nghiệp đưa nguyên vật liệu nội địa vào phạm vi miễn thuế.
- **Bộ ba "định mức ảo":** C4.3 (Σ tiêu hao M16 vượt M15) + C4.7 (phân bổ định mức bất thường) + C5.3 (tỷ lệ truy nguồn thấp) — pattern thổi phồng định mức để hợp thức hoá nguyên vật liệu dư.
- **Bộ ba "tẩu tán trước giải thể":** C6.4 (nhập tăng mạnh xuất không tăng) + C2.3 (tồn cuối âm) + C11.1 (máy móc miễn thuế không khớp danh mục) — pattern doanh nghiệp tranh thủ nhập miễn thuế rồi tẩu tán trước khi đóng MST.

Cơ quan Hải quan có thể yêu cầu hệ thống định nghĩa thêm các bộ ba khác theo kinh nghiệm nghiệp vụ. Khi một bộ ba cùng kích hoạt, hệ thống nâng mức cảnh báo tổng và đánh dấu đặc biệt trên bảng tổng quan.

### 2.8 Ranh giới sử dụng

Audit-HQ là **công cụ hỗ trợ phát hiện sơ bộ** — không phải kết luận điều tra. Mọi kết luận về sai phạm thuộc thẩm quyền cán bộ Hải quan sau quá trình kiểm tra thực tế. Hệ thống không thay thế quy trình kiểm tra sau thông quan.

---

## 3. Phạm vi thử nghiệm ban đầu

### 3.1 Dữ liệu đầu vào — chỉ dùng TKXNK và BCQT đã nộp

Giai đoạn I của Audit-HQ làm việc trên đúng dữ liệu cơ quan Hải quan đã có trong tay — không yêu cầu doanh nghiệp cung cấp gì thêm:

| Loại dữ liệu | Định dạng | Nguồn | Phạm vi thử nghiệm |
|---|---|---|---|
| Mẫu 15 (BCQT-NVL) | Excel có định dạng chuẩn theo TT 39/2018 | Doanh nghiệp nộp qua hệ thống điện tử | 5 DN × 3-4 năm |
| Mẫu 15a (BCQT-SP) | Excel có định dạng chuẩn | Doanh nghiệp nộp | 5 DN × 3-4 năm |
| Mẫu 16 (ĐMTT) | Excel có định dạng chuẩn | Doanh nghiệp nộp | 5 DN × 3-4 năm |
| BCCT TKXNK | Excel xuất từ VNACCS (hoặc doanh nghiệp tổng hợp) | Hệ thống Hải quan | 5 DN × 3-4 năm |

> **Dữ liệu BCQT là Excel có định dạng chuẩn** theo TT 39/2018, không phải tự do. Hệ thống có sẵn bộ đọc xử lý định dạng chuẩn, đồng thời có lớp tiếp nhận biến thể nhỏ giữa các doanh nghiệp.

Giai đoạn II (mở rộng) có thể yêu cầu doanh nghiệp cung cấp thêm sổ sách kế toán, sổ kho bán thành phẩm, danh mục tài sản cố định, sổ phế liệu — chi tiết tại §4.2.

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
| **Giai đoạn I** (§4.1) | TKXNK + BCQT đã nộp | 1, 2, 3, 4, 5, 6, 7 | 32 kiểm tra |
| **Giai đoạn II** (§4.2) | Cần dữ liệu / điều kiện bổ sung | 8, 9, 10, 11, 12 | 16 kiểm tra |

**Trạng thái** trong Giai đoạn I:
- ✅ Xây dựng và demo trong 2 tháng (16 kiểm tra)
- 🚧 Bổ sung trong giai đoạn thí điểm (13 kiểm tra)
- ⏳ Kích hoạt khi đã có đủ doanh nghiệp trong danh mục (3 kiểm tra Nhóm 7)

**Mức độ:** 🔴 Nghiêm trọng · 🟡 Cảnh báo · 🔵 Thông tin

### Tiền đề kỹ thuật cho mọi kiểm tra

Trước khi áp dụng các kiểm tra dưới đây, hệ thống tự xử lý các bước tiền đề:

- **Định nghĩa "kỳ":** kỳ mặc định là năm BCQT theo TT 39/2018 (từ 01/01 đến 31/12 năm tài chính). Hệ thống có thể cấu hình kỳ khác (quý / 6 tháng) khi cơ quan Hải quan yêu cầu.
- **Đơn vị tiền tệ:** trị giá BCCT có thể bằng USD; khi đối chiếu với sổ sách kế toán (Nhóm 10) hệ thống quy đổi theo tỷ giá hải quan của ngày thông quan.

### 4.0 Loại hình tờ khai theo loại hình doanh nghiệp

| Loại hình DN | Tờ khai nhập | Tờ khai xuất |
|---|---|---|
| **DNCX** — Doanh nghiệp chế xuất | E11, E15, E13 | E42 |
| **Gia công** — Gia công cho thương nhân nước ngoài | E21, E23 | E52, E54 |
| **SXXK** — Sản xuất xuất khẩu | E31, E33 | E62 |

> Tái xuất: B13 áp dụng chung. Chuyển mục đích sử dụng: A42 khi chuyển nội địa.

---

## 4.1 Giai đoạn I — Kiểm tra trên TKXNK và BCQT

> Các kiểm tra dưới đây thực hiện trên đúng dữ liệu cơ quan Hải quan đã có sẵn (TKXNK từ VNACCS + Mẫu 15/15a/16 doanh nghiệp đã nộp). Không yêu cầu doanh nghiệp cung cấp thêm dữ liệu nào.

### Nhóm 1 — Số lượng nhập / xuất (7 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C1.1** | Lệch số lượng nhập nguyên vật liệu (M15 so với tờ khai) — `nhập_trong_kỳ` (M15) khác Σ tờ khai nhập theo mã. Loại hình: DNCX E11+E15 / Gia công E21+E23 / SXXK E31+E33. Ngưỡng: <5% Thông tin · 5–20% Cảnh báo · >20% Nghiêm trọng. | Khai thiếu hoặc khai thừa nhập khẩu. | 🟡 | ✅ |
| **C1.2** | Có tờ khai nhập nhưng không có trong M15 — mã có trên BCCT nhưng không có dòng trong M15. Đánh dấu mọi trường hợp. | Bỏ sót nguyên vật liệu nhập khẩu khỏi BCQT. | 🔴 | ✅ |
| **C1.3** | Có trong M15 nhưng không có tờ khai — `nhập_trong_kỳ` > 0 mà không có tờ khai tương ứng. | M15 không có căn cứ tờ khai; doanh nghiệp có thể "mượn" mã nguyên vật liệu nhập khẩu để hợp thức hoá hàng mua nội địa không hoá đơn hoặc hàng nhập khẩu không khai báo, đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C1.4** | Lệch số lượng xuất thành phẩm (M15a so với tờ khai) — `xuất_khẩu` khác Σ tờ khai xuất theo mã thành phẩm. Loại hình: DNCX E42 / Gia công E52 / SXXK E62. Ngưỡng: <1% Thông tin · 1–5% Cảnh báo · >5% Nghiêm trọng. | Khai sai sản lượng xuất khẩu — có thể khai khống xuất khẩu để giảm lượng nguyên vật liệu miễn thuế phải giải trình, hoặc khai thiếu xuất khẩu để giấu nguồn thu. | 🟡 | ✅ |
| **C1.5** | Tái xuất M15 không có tờ khai B13 — `xuất_trả_lại` > 0 trong M15 nhưng không có B13 tương ứng. | Ghi tái xuất để giảm tồn nhưng không có tờ khai chứng minh. | 🟡 | 🚧 |
| **C1.6** | Chuyển mục đích sử dụng không có tờ khai A42 — `chuyển_mục_đích_sử_dụng` > 0 nhưng không có A42. | Hàng miễn thuế chuyển nội địa không khai báo — vi phạm điều kiện miễn thuế. | 🔴 | ✅ |
| **C1.7** | Tỷ lệ chuyển mục đích sử dụng trên tổng nhập trong kỳ vượt ngưỡng — `chuyển_mục_đích_sử_dụng` / `nhập_trong_kỳ` cao bất thường. Ngưỡng: >10% Cảnh báo · >25% Nghiêm trọng. | Doanh nghiệp lợi dụng kẽ hở miễn thuế — nhập nguyên vật liệu miễn thuế rồi chuyển nội địa với tỷ lệ cao, biến đặc quyền miễn thuế thành kênh nhập hàng tiêu thụ nội địa. | 🟡🔴 | ✅ |

### Nhóm 2 — Cân bằng và tồn kho (4 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C2.1** | Mất cân bằng phương trình M15 — `tồn_cuối` khác `tồn_đầu` + `nhập` − `xuất_trả` − `xuất_sản_xuất` − `chuyển_mục_đích_sử_dụng` − `xuất_khác`. Ngưỡng: chênh lệch khác 0 (cho phép ±0,01 làm tròn). Trường hợp đặc biệt: `tồn_đầu` = 0 nhưng `tồn_cuối` > `nhập_trong_kỳ` (tồn ảo, không thể có) — phương trình tự động không cân, đưa vào diễn giải. | Báo cáo không đáng tin cậy về mặt số học; có thể do lỗi nhập liệu, không khớp giữa các nguồn dữ liệu nội bộ doanh nghiệp, hoặc dữ liệu bị ghép từ nhiều bộ phận không đồng nhất. Trường hợp tồn ảo (tồn đầu = 0, tồn cuối > nhập): khả năng "tồn kho ảo" để treo nợ thuế — doanh nghiệp thực tế đã tiêu thụ hàng nhưng trên báo cáo vẫn thể hiện tồn để không phải nộp thuế nhập khẩu. Phải làm rõ từng cột thành phần trước khi đánh giá các kiểm tra khác. | 🔴 | ✅ |
| **C2.2** | Mất cân bằng phương trình M15a — `tồn_cuối` khác `tồn_đầu` + `nhập_kho` − `chuyển_mục_đích_sử_dụng` − `xuất_khẩu` − `xuất_khác`. | Báo cáo cân đối thành phẩm không đáng tin cậy về mặt số học; có thể do lỗi nhập liệu hoặc số liệu sản xuất/xuất khẩu/tồn không khớp giữa các nguồn nội bộ. Phải làm rõ từng cột trước khi đánh giá các kiểm tra khác. | 🔴 | ✅ |
| **C2.3** | Tồn cuối âm — nguyên vật liệu (M15) — `tồn_cuối_kỳ` < 0 trên bất kỳ mã nào. | Khả năng bỏ sót tờ khai nhập khẩu, sử dụng nguyên vật liệu không khai báo, hoặc điều chỉnh số liệu tồn kho không đúng thực tế. | 🔴 | ✅ |
| **C2.4** | Tồn cuối âm — thành phẩm (M15a) — `tồn_cuối_kỳ` < 0 trên bất kỳ mã nào. | Tương tự C2.3 cho thành phẩm — bỏ sót tờ khai, sử dụng hàng không khai báo, hoặc điều chỉnh số liệu tồn kho sai thực tế. | 🔴 | 🚧 |

### Nhóm 3 — Phân loại hàng hoá (3 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C3.1** | Cùng mã vật tư khai nhiều loại hình mâu thuẫn — một mã có trên cả tờ khai nguyên vật liệu và tờ khai máy móc thiết bị trong cùng kỳ. Cặp mâu thuẫn: E11+E13 · E31+E13 · E21+E13. | Phân loại sai dẫn đến sai phạm vi BCQT. | 🟡 | ✅ |
| **C3.2** | Mã HS không nhất quán trong kỳ (cùng mã vật tư) — ≥2 mã HS khác nhau trên các tờ khai. Ngưỡng: Khác phân nhóm (6 số) Thông tin · khác nhóm (4 số) Cảnh báo · khác chương (2 số) Nghiêm trọng. | Cố ý thay đổi mã HS để né các chính sách quản lý chuyên ngành (kiểm tra chất lượng, kiểm dịch) hoặc để hưởng thuế suất ưu đãi đặc biệt bất hợp pháp. | 🟡🔴 | ✅ |
| **C3.3** | Đơn vị tính không nhất quán (cùng mã vật tư) — ≥2 đơn vị khác nhau giữa M15 và BCCT. | Sai đơn vị tính ×1000 khiến toàn bộ nhập/xuất/tồn sai hệ thống. | 🔴 | ✅ |

### Nhóm 4 — Định mức M16 (7 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C4.1** | Nguyên vật liệu trong M16 không có nhập khẩu và không có tồn đầu kỳ — `mã_NVL` trong M16 nhưng (không có dòng trong M15) HOẶC (cả `nhập_trong_kỳ` = 0 VÀ `tồn_đầu_kỳ` = 0). Loại trừ trường hợp NVL còn tồn từ kỳ trước. | Nguyên vật liệu xuất hiện trong định mức nhưng không có nguồn nhập khẩu lẫn tồn đầu — không thể giải trình dòng vật tư từ tờ khai đến thành phẩm xuất khẩu. | 🔴 | ✅ |
| **C4.2** | Thành phẩm trong M16 không có trong M15a — `mã_SP_xuất_khẩu` trong M16 nhưng không có dòng trong M15a. | Định mức cho thành phẩm không có trong báo cáo xuất khẩu. | 🟡 | 🚧 |
| **C4.3** | Tổng tiêu hao tính theo M16 vượt xuất sản xuất M15 — Σ(`định_mức` × `xuất_khẩu_M15a`) theo mã nguyên vật liệu > `xuất_sản_xuất` trong M15. Ngưỡng: vượt >5% Cảnh báo · >20% Nghiêm trọng. | Đây là cách phổ biến nhất để lấy nguyên vật liệu miễn thuế ra bán nội địa — xây dựng định mức ảo bao gồm cả những thành phần không có thực trong sản phẩm, thổi phồng tiêu hao để hợp thức hoá nguyên vật liệu nhập khẩu dư. | 🟡🔴 | ✅ |
| **C4.4** | M16 phân mảnh: nhiều nguyên vật liệu cùng chức năng cho một thành phẩm. **Ví dụ thực tế**: 1 chiếc áo có 10 loại cúc khác nhau trong M16. Cách phát hiện: (A) ≥N mã có cùng HS 4 số trong 1 thành phẩm (mặc định) · (B) gom nhóm tên gần giống (xử lý ngôn ngữ tự nhiên) · (C) cơ quan Hải quan định nghĩa danh mục nhóm vật tư. Ngưỡng: ≥5 mã cùng HS / thành phẩm Cảnh báo · ≥10 Nghiêm trọng. | Phân mảnh nguyên vật liệu để che số lượng, hợp thức hoá nhập khẩu dư. | 🟡 | 🚧 |
| **C4.5** | Định mức bằng 0 hoặc âm — `định_mức_thực_tế` ≤ 0 trên bất kỳ dòng M16 nào. | Lỗi dữ liệu hoặc cố tình khai 0 để che tiêu hao thực tế. | 🔴 | 🚧 |
| **C4.6** | Định mức bất thường cao (giá trị ngoại lai thống kê) — `định_mức` cặp thành phẩm-nguyên vật liệu trong kỳ N vượt xa trung bình của chính cặp đó qua các kỳ trước của cùng doanh nghiệp. Ngưỡng: vượt trung bình ±3 độ lệch chuẩn Cảnh báo · ±5 độ lệch chuẩn Nghiêm trọng. Yêu cầu: doanh nghiệp có ≥3 kỳ BCQT để có cơ sở thống kê. | Thổi phồng định mức để hợp thức hoá nguyên vật liệu nhập khẩu vượt mức. | 🟡 | 🚧 |
| **C4.7** | Phân bổ định mức bất thường (mở rộng từ C4.4) — phát hiện: (a) cùng cặp thành phẩm-NVL có nhiều định mức khác nhau trong cùng kỳ; (b) một nguyên vật liệu được dùng cho quá nhiều thành phẩm không liên quan; (c) một thành phẩm có số lượng dòng nguyên vật liệu vượt ngưỡng hợp lý của ngành. | phân mảnh định mức để hợp thức hoá nhiều mã NVL nhập khẩu, gây khó truy nguồn và che giấu lượng NVL dư / thất thoát · điều chỉnh định mức tuỳ ý để cân đối tồn kho · khai báo định mức quá rộng để hợp thức hoá NVL nhập khẩu miễn thuế cho thành phẩm không phù hợp thực tế sản xuất · có dấu hiệu tính toán / nguỵ tạo định mức nhân tạo để chế số liệu quyết toán thay vì phản ánh tiêu hao sản xuất thực tế. | 🟡🔴 | 🚧 |

### Nhóm 5 — Truy nguồn nguyên vật liệu nhập khẩu (3 kiểm tra)

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C5.1** | NVL có xuất sản xuất trong M15 nhưng không có nhập khẩu — `xuất_sản_xuất` > 0 và `nhập_trong_kỳ` = 0 và `tồn_đầu_kỳ` = 0. | Tiêu hao từ nguồn không khai báo — nguyên vật liệu nội địa bị đưa vào phạm vi miễn thuế. | 🔴 | ✅ |
| **C5.2** | Thành phẩm xuất khẩu không có trong M16 (thành phẩm "mồ côi") — mã thành phẩm có `xuất_khẩu` > 0 trong M15a nhưng không có dòng M16. | Không thể giải trình nguyên vật liệu đầu vào cho thành phẩm đã xuất khẩu; doanh nghiệp có thể dùng nguyên liệu không rõ nguồn gốc (kể cả hàng lậu) để sản xuất xuất khẩu. | 🟡 | 🚧 |
| **C5.3** | Tỷ lệ truy nguồn thấp theo mã nguyên vật liệu — Σ(`định_mức` × `xuất_khẩu_M15a`) / (`xuất_sản_xuất_M15` − NVL còn ở dạng BTP và TP tồn kho cuối kỳ) thấp dưới ngưỡng. Ngưỡng: <80% Cảnh báo · <60% Nghiêm trọng. Lưu ý: phải trừ NVL còn nằm trong BTP và TP chưa xuất khẩu (sẽ xuất khẩu kỳ sau) — chỉ tính phần đáng lẽ đã ra thành phẩm xuất khẩu trong kỳ. Không áp dụng cho doanh nghiệp có TP bán nội địa lớn hoặc có nhiều tầng BTP tự sản xuất (đề nghị dùng kiểm tra Nhóm 9 bổ sung). | Phần lớn nguyên vật liệu nhập khẩu không truy được vào thành phẩm xuất khẩu cụ thể. | 🟡 | 🚧 |

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

## 4.2 Giai đoạn II — Kiểm tra mở rộng, cần dữ liệu bổ sung

> Các nhóm kiểm tra dưới đây yêu cầu **dữ liệu ngoài TKXNK và BCQT**. Doanh nghiệp sẽ cung cấp thêm theo yêu cầu của cơ quan Hải quan. Đây là giai đoạn mở rộng, triển khai sau khi Giai đoạn I đã ổn định.
>
> Đây là khu vực **bộ ba "tử huyệt"** — định mức, bán thành phẩm, phế liệu — nơi xảy ra phần lớn các vụ truy thu thuế lớn.

### Nhóm 8 — Phế liệu và phế phẩm (3 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** sổ kho phế liệu, hoá đơn bán phế liệu nội địa, danh mục tờ khai A42 đã nộp cho phế liệu.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C8.1** | Tỷ lệ phế liệu / phế phẩm thực tế vượt ngưỡng ngành — cặp NVL-thành phẩm có tỷ lệ phế thải vượt mức trung bình ngành. Nguồn ngưỡng: cơ quan Hải quan định nghĩa danh mục ngưỡng theo loại ngành sản xuất (kim loại, dệt may, điện tử, hoá chất…). Mỗi ngành có dải hợp lý riêng. | Khai phế liệu cao để giảm lượng NVL cần giải trình hoặc che tiêu thụ nội địa. | 🟡 | ⏳ |
| **C8.2** | Phế liệu bán nội địa không có tờ khai chuyển mục đích sử dụng (A42) — doanh nghiệp ghi nhận bán phế liệu trong sổ sách nhưng không có A42 tương ứng. | Vi phạm điều kiện miễn thuế — phế liệu phát sinh từ NVL miễn thuế, bán nội địa phải khai A42 và nộp thuế. | 🔴 | ⏳ |
| **C8.3** | Tỷ lệ phế liệu thay đổi đột biến giữa các kỳ — tỷ lệ phế thải kỳ N cao bất thường so với kỳ N-1 (cùng dây chuyền sản xuất). | Điều tiết phế liệu để cân đối số liệu tồn kho qua các kỳ. | 🟡 | ⏳ |

### Nhóm 9 — Sản phẩm dở dang (bán thành phẩm) (4 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** sổ kho bán thành phẩm, sổ sản xuất, sơ đồ công đoạn, định mức từng tầng bán thành phẩm.
>
> Bán thành phẩm là **vùng xám dữ liệu** lớn nhất: có thể đã tiêu hao một phần NVL, chưa hoàn thiện để xuất khẩu, luân chuyển qua nhiều công đoạn hoặc nhiều kỳ. Mỗi doanh nghiệp có cách định nghĩa BTP khác nhau, dễ phát sinh nhiều tầng (cấp 1, cấp 2, tái chế, gia công lại) — không có chuẩn hoá tuyệt đối.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C9.1** | BTP đa tầng không truy nguồn được về NVL gốc — BTP cấp 1, 2, 3... không có định mức chi tiết cho từng tầng hoặc thiếu liên kết về nguyên vật liệu ban đầu. Yêu cầu doanh nghiệp cung cấp định mức từng tầng BTP và sơ đồ công đoạn. Đặc tả chi tiết phối hợp với cơ quan Hải quan định nghĩa khi triển khai. | Làm mờ truy nguồn — NVL đã nhập khẩu "nằm" trong BTP nhiều tầng, đối chiếu với thành phẩm xuất khẩu không còn tuyến tính. | 🟡 | ⏳ |
| **C9.2** | Tồn BTP cuối kỳ N khác tồn BTP đầu kỳ N+1 — biến động không có giải trình. | BTP bị "đẩy qua lại" giữa các kỳ để điều chỉnh tồn kho mà không thay đổi dòng thực tế. | 🟡 | ⏳ |
| **C9.3** | Tồn BTP lớn không tương xứng với năng lực sản xuất khai báo — `tồn_BTP_cuối_kỳ` × thời gian gia công trung bình > năng lực dây chuyền × số ngày sản xuất trong kỳ. Yêu cầu doanh nghiệp cung cấp báo cáo cơ sở sản xuất (năng lực dây chuyền, thời gian gia công chuẩn cho mỗi BTP). | Che giấu tiêu thụ nội địa — NVL đã đưa vào BTP nhưng thực tế bị tiêu thụ / bán nội địa, khó phát hiện vì chưa "ra thành phẩm". | 🟡 | ⏳ |
| **C9.4** | Cấu thành NVL của BTP không khớp giữa định mức khai báo và sổ kho thực tế — định mức tầng BTP tính ra khác lượng NVL đã xuất kho cho BTP đó. | Tách nhỏ một quy trình sản xuất thành nhiều tầng BTP để làm loãng sai lệch định mức, tạo vùng xám dễ lợi dụng. | 🔴 | ⏳ |

### Nhóm 10 — Đối chiếu sổ sách kế toán (3 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** Bảng cân đối phát sinh, sổ chi tiết các tài khoản 152 (NVL), 155 (Thành phẩm), 156 (Hàng hoá), Báo cáo tài chính kỳ tương ứng.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C10.1** | Tồn kho đầu/cuối kỳ BCQT khác số dư các tài khoản 152, 155, 156 trên Bảng cân đối phát sinh. | Số liệu BCQT không khớp sổ sách kế toán — hai nguồn số liệu mâu thuẫn cần làm rõ. | 🔴 | ⏳ |
| **C10.2** | Doanh thu xuất khẩu sổ sách kế toán khác trị giá xuất khẩu BCCT — đối chiếu trên cùng kỳ. Ngưỡng dung sai: <2% Thông tin · 2–5% Cảnh báo · >5% Nghiêm trọng. Lưu ý: doanh thu kế toán ghi theo giá thanh toán (thường CIF/FOB DN ghi sổ), trị giá BCCT theo giá hải quan (FOB), chênh lệch nhẹ là hợp lệ. | Khai sai một trong hai phía, ảnh hưởng nghĩa vụ thuế thu nhập doanh nghiệp hoặc thuế xuất khẩu. | 🟡🔴 | ⏳ |
| **C10.3** | Giá trị nhập khẩu sổ sách kế toán khác trị giá nhập khẩu BCCT — đối chiếu trên cùng kỳ. Ngưỡng dung sai: <2% Thông tin · 2–5% Cảnh báo · >5% Nghiêm trọng. Chênh lệch nhẹ có thể hợp lệ do tỷ giá ghi sổ kế toán khác tỷ giá hải quan. | Khai sai một trong hai phía hoặc có nguồn nhập không khai báo. | 🟡🔴 | ⏳ |

### Nhóm 11 — Tài sản cố định, máy móc thiết bị và năng lực vận hành (3 kiểm tra)

> **Dữ liệu doanh nghiệp cần cung cấp thêm:** danh mục tài sản cố định (sổ TSCĐ), báo cáo cơ sở sản xuất, hồ sơ máy móc nhập khẩu miễn thuế.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C11.1** | Máy móc thiết bị miễn thuế nhập khẩu (E13) không khớp danh mục thiết bị trong báo cáo cơ sở sản xuất. | Máy móc miễn thuế đã bán nội địa, chuyển nhượng, hoặc đưa ra khỏi cơ sở mà không khai báo. | 🔴 | ⏳ |
| **C11.2** | Công suất máy móc khai báo không khớp sản lượng thực tế trong BCQT — tổng `nhập_kho_M15a` (sản lượng TP sản xuất ra trong kỳ) chia cho công suất danh nghĩa của máy móc khai báo trong báo cáo cơ sở sản xuất, vượt xa hoặc thấp xa số ngày sản xuất hợp lý của kỳ. Ngưỡng: <50% hoặc >150% so với năng lực kỳ vọng → Cảnh báo. Trường hợp >200% → Nghiêm trọng (sản lượng vượt năng lực = nhập từ nguồn khác). | Khai báo công suất không trung thực để được miễn thuế (khai cao hơn thực tế khi nhập) hoặc để hợp thức hoá lượng xuất khẩu vượt năng lực (sản phẩm gia công thuê ngoài hoặc nhập lậu). | 🟡 | ⏳ |
| **C11.3** | Tồn kho cuối kỳ bất thường so với năng lực vận hành — giá trị tồn kho NVL/TP cuối kỳ vượt sức chứa kho khai báo (báo cáo cơ sở sản xuất) hoặc vượt vốn lưu động bình quân trên báo cáo tài chính cùng kỳ. Ngưỡng: vượt 50% Cảnh báo · vượt 100% Nghiêm trọng. Yêu cầu dữ liệu bổ sung: báo cáo cơ sở sản xuất + báo cáo tài chính. | Tồn kho ảo — hàng đã thực tế tiêu thụ hoặc bán nội địa nhưng vẫn duy trì số tồn trên báo cáo để treo nợ thuế nhập khẩu. Pattern điển hình của gian lận trong doanh nghiệp chế xuất khi sắp giải thể hoặc khi muốn tránh đối chiếu tồn thực tế. | 🔴 | ⏳ |

---

### Nhóm 12 — Nhà cung cấp (3 kiểm tra)

> **Điều kiện kích hoạt:** trường nhà cung cấp trong BCCT đã được chuẩn hoá (cùng một nhà cung cấp khai cùng dạng tên); bảng tham chiếu định dạng mã số thuế các quốc gia xuất xứ; danh sách nhà cung cấp rủi ro do cơ quan Hải quan cung cấp.

| Mã | Vấn đề | Rủi ro | Mức | Trạng thái |
|---|---|---|---|---|
| **C12.1** | Nhà cung cấp mới xuất hiện đột ngột chiếm tỷ trọng lớn — nhà cung cấp chưa từng xuất hiện trong các kỳ trước nhưng kỳ này chiếm >30% kim ngạch nhập của doanh nghiệp. | Nhà cung cấp giả lập (công ty ma), hoặc thay đổi nhà cung cấp để né kiểm soát chuyển giá / kiểm soát xuất xứ. | 🟡 | ⏳ |
| **C12.2** | Mã số thuế / thông tin nhận diện nhà cung cấp không hợp lệ — định dạng MST sai, nhà cung cấp trên tờ khai không khớp dạng định danh quốc tế của nước xuất xứ. | Nhà cung cấp không có thật, hoặc khai mượn danh nhà cung cấp khác. | 🔴 | ⏳ |
| **C12.3** | Nhà cung cấp nằm trong danh sách rủi ro của cơ quan Hải quan — đối chiếu với danh sách nhà cung cấp nghi vấn (chuyển giá, gian lận xuất xứ, đã bị xử phạt trước đây). | Doanh nghiệp tiếp tục giao dịch với nhà cung cấp đã được cơ quan Hải quan đánh dấu rủi ro. | 🟡🔴 | ⏳ |

### 4.3 Tổng hợp

| Giai đoạn | Nhóm | Tổng | ✅ MVP 2 tháng | 🚧 Bổ sung thí điểm | ⏳ Cần thêm điều kiện |
|---|---|---:|---:|---:|---:|
| **Giai đoạn I** (TKXNK + BCQT) | 1 — Số lượng nhập/xuất | 7 | 6 | 1 | 0 |
| | 2 — Cân bằng và tồn kho | 4 | 3 | 1 | 0 |
| | 3 — Phân loại hàng hoá | 3 | 3 | 0 | 0 |
| | 4 — Định mức M16 | 7 | 2 | 5 | 0 |
| | 5 — Truy nguồn NVL | 3 | 1 | 2 | 0 |
| | 6 — Liên kỳ | 5 | 1 | 4 | 0 |
| | 7 — So sánh giữa các DN | 3 | 0 | 0 | 3 |
| | **Cộng Giai đoạn I** | **32** | **16** | **13** | **3** |
| **Giai đoạn II** (cần dữ liệu bổ sung) | 8 — Phế liệu / phế phẩm | 3 | 0 | 0 | 3 |
| | 9 — Sản phẩm dở dang (BTP) | 4 | 0 | 0 | 4 |
| | 10 — Đối chiếu sổ sách kế toán | 3 | 0 | 0 | 3 |
| | 11 — TSCĐ, máy móc và năng lực vận hành | 3 | 0 | 0 | 3 |
| | 12 — Nhà cung cấp | 3 | 0 | 0 | 3 |
| | **Cộng Giai đoạn II** | **16** | **0** | **0** | **16** |
| | **TỔNG TOÀN BỘ** | **48** | **16** | **13** | **19** |

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

Hệ thống chia rõ công việc giữa **quy tắc xác định** và **trí tuệ nhân tạo (AI)**:

- Phần **phát hiện sai phạm** chạy theo quy tắc xác định — vì mỗi phát hiện phải truy nguồn được về dòng dữ liệu cụ thể, có cơ sở pháp lý, và bảo vệ được trước cấp trên cũng như khi doanh nghiệp khiếu nại. Đây là phần không thể giao cho AI nếu muốn defensible.
- Phần **xử lý dữ liệu thực tế lộn xộn** giao cho AI — đó là việc con người không thể làm thủ công ở quy mô hàng chục nghìn dòng tờ khai một năm. Quy tắc cứng không bao quát được vì dữ liệu doanh nghiệp khai có vô số biến thể về tên hàng, đơn vị, mã hàng.

| Công việc AI đảm nhiệm | Khi nào dùng | Kết quả |
|---|---|---|
| Chuẩn hoá tên hàng hoá có nhiều biến thể | Khi gặp mô tả không chuẩn trong BCCT/Mẫu | Tên chuẩn (cán bộ xác nhận lần đầu, hệ thống ghi nhớ) |
| Đối chiếu mã hàng tương đồng giữa BCCT và Mẫu | Khi quy tắc cứng không đủ độ chính xác | Đề xuất ánh xạ (cán bộ xác nhận) |
| Sinh giải thích tiếng Việt cho từng phát hiện | Khi cán bộ chọn xem một phát hiện | Diễn giải dễ đọc kèm dẫn chứng pháp lý |
| Cảnh báo mã loại hình không hợp lệ | Khi tờ khai có mã không có trong QĐ 1357 | Cảnh báo và gợi ý tra cứu |

Mọi quyết định cuối cùng vẫn thuộc thẩm quyền cán bộ Hải quan.

---

## 6. Kế hoạch demo (thử nghiệm ban đầu)

### 6.1 Dữ liệu demo

5 doanh nghiệp giả lập, mỗi doanh nghiệp 3-4 năm:

| Mã DN | Ngành | Loại hình | Số năm | Sai phạm được đưa vào để minh hoạ |
|---|---|---|---|---|
| DN_001 | Điện tử (HS 85) | DNCX (E11/E42) | 4 | C1.1, C2.1, C6.1, C3.2 |
| DN_002 | Cơ khí (HS 84) | DNCX (E11/E42) | 3 | C1.2, C3.3, C3.1, C6.5 |
| DN_003 | Dệt may (HS 61) | SXXK (E31/E62) | 4 | C4.3, C4.4 (cúc áo), C5.1 |
| DN_004 | Hoá chất (HS 39) | DNCX | 3 | C1.4, C1.6, C2.3 |
| DN_005 | Cơ khí (HS 84) | DNCX | 3 | (sạch — minh chứng hệ thống không phát hiện bừa) |

> **Lưu ý về dữ liệu demo:** dữ liệu giả lập, được tạo từ dữ liệu thực đã xoá danh tính (mã doanh nghiệp, MST, tên nhà cung cấp), phục vụ mục đích demo. Không phản ánh doanh nghiệp cụ thể nào.

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

### 6.3 Kịch bản demo 5 phút

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

Toàn bộ giai đoạn xây dựng và demo gói gọn trong **10 tuần** tính từ khi cơ quan Hải quan phê duyệt nguyên tắc đề án. Lộ trình này tập trung vào **Giai đoạn I** của danh mục kiểm tra (§4.1) — các kiểm tra thực hiện trên dữ liệu TKXNK và BCQT đã nộp.

### 7.1 Tuần 1-2 — Khởi tạo và nền tảng dữ liệu

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 1 | Khởi tạo dự án, dựng kiến trúc nền, tái sử dụng mô-đun từ các hệ thống Tinsu đã vận hành | Bộ khung chạy được trên môi trường nội bộ |
| 2 | Bộ đọc Excel (Mẫu 15/15a/16 + BCCT) + Tầng dữ liệu 0-1 | Nạp được 1 doanh nghiệp, truy vấn được theo mã, theo kỳ |

### 7.2 Tuần 3-4 — Cài đặt Nhóm 1 và Nhóm 2 (9 kiểm tra)

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 3 | Nhóm 1 — Số lượng nhập / xuất (6 kiểm tra trong giai đoạn này) | Phát hiện hiện trên màn hình, có chứng cứ truy nguồn |
| 4 | Nhóm 2 — Cân bằng và tồn kho (3 kiểm tra) + cơ chế đánh dấu thao tác | 9 kiểm tra đầu hoàn chỉnh |

### 7.3 Tuần 5-6 — Cài đặt Nhóm 3, 4, 5, 6 (7 kiểm tra còn lại) và tính điểm rủi ro

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 5 | Nhóm 3 (phân loại) + Nhóm 4 (định mức MVP) + Nhóm 5 (truy nguồn MVP) + Nhóm 6 (liên kỳ MVP) | 6 kiểm tra cài đặt xong |
| 6 | Thuật toán cộng dồn điểm rủi ro + phát hiện kết hợp + dọn dẹp các kiểm tra | Đủ 16 kiểm tra MVP cho demo |

### 7.4 Tuần 7-8 — Dữ liệu demo

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 7 | Tạo dữ liệu giả lập 5 doanh nghiệp × 3-4 năm + xoá danh tính | Dữ liệu nền sạch, đã ẩn danh |
| 8 | Mô phỏng các kiểu sai phạm trên dữ liệu nền (cho từng doanh nghiệp demo) | Dữ liệu demo hoàn chỉnh, kiểm tra cân bằng số học |

### 7.5 Tuần 9-10 — Giao diện, tổng duyệt và bàn giao

| Tuần | Mục tiêu | Kết quả |
|---|---|---|
| 9 | Bảng tổng quan + trang chi tiết doanh nghiệp + xuất Excel kiến nghị kiểm tra + tổng duyệt nội bộ | Toàn bộ luồng demo 5 phút chạy được |
| 10 | Demo cho cơ quan Hải quan + bàn giao hồ sơ kỹ thuật + tổng hợp phản hồi | Báo cáo kết quả, đề xuất bước tiếp theo |

### 7.6 Vai trò các bên trong 10 tuần

| Bên | Vai trò chính |
|---|---|
| Tinsu AI | Xây dựng hệ thống, dữ liệu giả lập, tổng duyệt kỹ thuật |
| Trọng Tín | Cung cấp kinh nghiệm nghiệp vụ, tổng duyệt nghiệp vụ |
| Cơ quan Hải quan | Phê duyệt nguyên tắc, định hướng nghiệp vụ, tiếp nhận demo |

### 7.7 Định hướng sau 10 tuần

Sau khi demo và nhận phản hồi, tuỳ quyết định của cơ quan Hải quan, các bước tiếp theo có thể bao gồm:

- **Triển khai thí điểm tại Chi Cục Hải Quan Khu vực IV** với dữ liệu doanh nghiệp thực tế; cài tiếp 13 kiểm tra còn lại của Giai đoạn I (§4.1).
- **Kích hoạt Nhóm 7 so sánh giữa các doanh nghiệp** khi đã có đủ doanh nghiệp trong danh mục.
- **Mở rộng sang Giai đoạn II (§4.2)** — Nhóm 8-11 kiểm tra phế liệu, bán thành phẩm, sổ sách kế toán, tài sản cố định. Cần phối hợp với cơ quan Hải quan để yêu cầu doanh nghiệp cung cấp các dữ liệu bổ sung tương ứng.
- **Tích hợp trực tiếp với VNACCS** thay vì nạp qua tệp Excel xuất ra.
- **Mở rộng sang nhiều Chi cục**.

Các bước này không nằm trong cam kết 10 tuần vì phụ thuộc quyết định của cơ quan Hải quan sau khi xem demo.

> **Quan trọng:** Dữ liệu giả lập chỉ phục vụ mục đích demo. Khi cơ quan Hải quan vận hành thực tế, hệ thống chạy hoàn toàn trên dữ liệu của cơ quan Hải quan.

---

## 8. Câu hỏi mở cho phía Hải quan

Đây là các nội dung cần phản hồi từ cơ quan Hải quan trước khi hoàn thiện đề án và bắt đầu xây dựng.

### 8.1 Về phạm vi nghiệp vụ

1. Trong 48 kiểm tra đề xuất (32 Giai đoạn I + 16 Giai đoạn II), có kiểm tra nào cơ quan Hải quan đặc biệt quan tâm, hoặc có kiểm tra nào quan trọng mà đề án bỏ sót?
2. Trong số 15 kiểm tra MVP cho demo 2 tháng, có kiểm tra nào cơ quan Hải quan muốn ưu tiên hơn?
3. Báo cáo Excel kiến nghị kiểm tra có cần theo mẫu chính thức nào không?
4. Hiện tại Chi cục đang dùng công cụ hoặc quy trình nào để chọn doanh nghiệp kiểm tra? Audit-HQ tích hợp hay thay thế?
5. Ngưỡng đề xuất (Nghiêm trọng / Cảnh báo / Thông tin) có phù hợp thực tế nghiệp vụ không? Cần điều chỉnh gì?
6. Cơ chế cộng dồn rủi ro (§2.6) có phù hợp cách đánh giá hiện hành của cơ quan Hải quan không?

### 8.2 Về dữ liệu Giai đoạn I (TKXNK + BCQT)

7. Hệ thống xử lý dữ liệu điện tử của cơ quan Hải quan có lưu Mẫu 15/15a/16 dưới dạng có cấu trúc, hay chỉ là tệp Excel đính kèm?
8. Dữ liệu TKXNK xuất từ VNACCS có cấu trúc thống nhất cho mọi Chi cục không?
9. Quyền truy cập dữ liệu nhiều năm: hệ thống VCIS-VNACCS đã cho phép truy vấn trực tiếp, hay phải xin từng kỳ?

### 8.3 Về dữ liệu Giai đoạn II (mở rộng)

10. Cơ quan Hải quan có cơ chế yêu cầu doanh nghiệp cung cấp Bảng cân đối phát sinh, sổ tài khoản 152/155/156 không? Tần suất nào hợp lý?
11. Quy định hiện hành về sổ kho bán thành phẩm và danh mục tài sản cố định — doanh nghiệp đã phải lưu trữ chưa? Cơ quan Hải quan có quyền yêu cầu xuất khi cần kiểm tra không?
12. Báo cáo cơ sở sản xuất (theo TT 38/2015) hiện đã được số hoá chưa, hay vẫn ở dạng giấy?

### 8.4 Về kỹ thuật và vận hành

13. Hệ thống đặt tại trụ sở cơ quan Hải quan hay đặt trên máy chủ của Tinsu? Yêu cầu bảo mật cụ thể?
14. Có yêu cầu chứng nhận an toàn thông tin cấp nào?
15. Cam kết chất lượng dịch vụ (SLA) cần đáp ứng cho giai đoạn thí điểm / vận hành chính thức?
16. Cán bộ tại Chi Cục Hải Quan Khu vực IV có thể tiếp nhận hệ thống ở mức nào? Cần đào tạo bao nhiêu?


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


---

> **Đây là bản dự thảo lần 10.** Mọi nội dung là đề xuất sơ bộ và sẽ được điều chỉnh theo phản hồi của cơ quan Hải quan qua các vòng tổng hợp tiếp theo.
