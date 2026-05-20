# Mapping dữ liệu thực tế ↔ Catalog 49 kiểm tra

**Ngày:** 2026-05-21
**Bối cảnh:** HQ đã duyệt đề án v10. Trọng Tín gửi 622 file dữ liệu thực (6 DN, 2015-2025). Đối chiếu xem dữ liệu hiện có đủ cho 16 MVP + 14 W.I.P trong Giai đoạn I (§4.1) hay không.

## Tóm tắt nhanh

- **Tất cả 16 MVP đều chạy được với dữ liệu hiện có** (Nhóm 1-6 phần đã có ✅).
- **HONG_AN và HIEP_QUANG** là 2 DN có độ phủ tốt nhất → chọn làm "DN chính" cho demo.
- **Có thể bỏ tuần 7-8 (sim dữ liệu giả lập)** vì đã có 6 DN thực — chỉ cần anonymize (xoá danh tính theo §6.2). Tiết kiệm 2 tuần, hoặc dùng để injection sai phạm có chủ đích cho demo.
- **Giai đoạn II (Nhóm 8-12, 16 kiểm tra)** chưa có dữ liệu — đúng kế hoạch, cần HQ + Trọng Tín cung cấp thêm theo §4.2.

## Dữ liệu HQ đã có (tóm tắt)

| Loại | Có/Không | Ghi chú |
|---|---|---|
| **BCQT TT39** (Mẫu 15/15a/16) | ✅ Tất cả 6 DN | HONG_AN 51 file, HIEP_QUANG 26, DO_THANH 15, HONG_PHUC 14, GROWATT 6, KIM_LONG 5 |
| **Định mức (BCDM/Mẫu 16)** | ✅ Tất cả 6 DN | HIEP_QUANG nhiều nhất (73 file), HONG_AN 50 |
| **Báo cáo hàng chi tiết** (BCCT export từ ECUS) | ⚠️ Một phần | HONG_AN 11, HIEP_QUANG 4, DO_THANH 4, các DN khác 1 |
| **Tờ khai XNK** (ToKhai_*.xls) | ⚠️ Chỉ HONG_AN + HIEP_QUANG | HONG_AN 57, HIEP_QUANG 11 — đủ cho chéo C1.x |
| **Bảng NXT (Nhập-Xuất-Tồn NVL)** | ⚠️ HONG_AN, HIEP_QUANG, DO_THANH | Hữu ích cho C2.x, C5.x |
| **BCTT79** (báo cáo theo TT79 cũ) | ⚠️ Chủ yếu HIEP_QUANG 41 file | TT79 đã hết hiệu lực, dùng để tham chiếu lịch sử (kỳ 2015-2019) |
| **Chứng từ scan PDF** (tờ khai sửa) | ⚠️ HONG_AN 43, HIEP_QUANG 5 | Phục vụ kiểm tra A42 / tờ khai sửa-hủy |
| **Công văn giải trình** | ⚠️ HONG_AN 8, HIEP_QUANG 2 | Tham chiếu nghiệp vụ |
| **Mã NVL / Mã SP** | ⚠️ HONG_AN 4 file | Lookup table khi đối chiếu mã |

**KHÔNG có** (đúng theo §4.2):
- Bảng cân đối kế toán, sổ TK 152/155/156 (cần cho Nhóm 10)
- Báo cáo cơ sở sản xuất (cần cho Nhóm 11)
- Danh mục TSCĐ (cần cho C11.1)
- Sổ kho phế liệu (cần cho Nhóm 8)
- Sổ BTP đa tầng (cần cho Nhóm 9)
- Danh sách NCC rủi ro (cần cho C12.3)

## Mapping 16 MVP × dữ liệu hiện có

| Mã | Tên ngắn | Dữ liệu cần | Tình trạng | DN chạy được |
|---|---|---|---|---|
| C1.1 | Lệch số lượng nhập NVL (M15 vs tờ khai) | M15 + BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG (DN có cả BCQT + tờ khai chi tiết) |
| C1.2 | Tờ khai NK có nhưng không có trong M15 | M15 + BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG |
| C1.3 | M15 có nhập nhưng không có tờ khai | M15 + BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG |
| C1.4 | Lệch số lượng xuất TP (M15a vs tờ khai) | M15a + BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG |
| C1.6 | Chuyển mục đích sử dụng không có A42 | M15 + BCCT (lọc A42) | ⚠️ Phải parse | Cần extract dòng A42 trong BCCT |
| C1.7 | Tỷ lệ chuyển mục đích sử dụng vượt ngưỡng | M15 | ✅ Đủ | Tất cả DN có BCQT |
| C2.1 | Mất cân bằng phương trình M15 | M15 | ✅ Đủ | Tất cả 6 DN |
| C2.2 | Mất cân bằng phương trình M15a | M15a | ✅ Đủ | Tất cả 6 DN |
| C2.3 | Tồn cuối âm — NVL | M15 | ✅ Đủ | Tất cả 6 DN |
| C3.1 | Cùng mã vật tư khai nhiều loại hình mâu thuẫn | BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG (có nhiều tờ khai) |
| C3.2 | Mã HS không nhất quán trong kỳ | BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG |
| C3.3 | Đơn vị tính không nhất quán | M15 + BCCT | ✅ Đủ | HONG_AN, HIEP_QUANG |
| C4.1 | NVL trong M16 không có nhập + không có tồn đầu | M16 + M15 | ✅ Đủ | Tất cả 6 DN |
| C4.3 | Tổng tiêu hao M16 vượt xuất sản xuất M15 | M16 + M15 + M15a | ✅ Đủ | Tất cả 6 DN |
| C5.1 | NVL có xuất SX trong M15 nhưng không có nhập | M15 | ✅ Đủ | Tất cả 6 DN |
| C6.1 | Tồn đầu kỳ N khác tồn cuối kỳ N-1 (NVL) | ≥2 kỳ M15 | ✅ Đủ | HONG_AN (8 kỳ), HIEP_QUANG (9 kỳ), DO_THANH (3), GROWATT (3); HONG_PHUC + KIM_LONG chỉ có 2 kỳ — đủ tối thiểu |

**Kết luận:** 16/16 MVP đều có thể demo với dữ liệu hiện có. C1.6 cần code parser BCCT extract dòng A42 — không phải vấn đề.

## Mapping 14 W.I.P × dữ liệu hiện có

| Mã | Dữ liệu cần | Tình trạng |
|---|---|---|
| C1.5 (tái xuất B13) | M15 + BCCT lọc B13 | ⚠️ Phải check có B13 trong BCCT không |
| C2.4 (tồn cuối TP âm) | M15a | ✅ |
| C4.2 (TP trong M16 không có M15a) | M16 + M15a | ✅ |
| C4.4 (cúc áo — M16 phân mảnh) | M16 | ✅ — đặc biệt với HONG_AN ngành may |
| C4.5 (định mức ≤ 0) | M16 | ✅ |
| C4.6 (định mức ngoại lai thống kê) | M16 ≥3 kỳ | ✅ HONG_AN, HIEP_QUANG, GROWATT, DO_THANH (≥3 kỳ) |
| C4.7 (phân bổ định mức bất thường) | M16 | ✅ |
| C4.8 (tồn NVL âm cộng dồn theo thời gian) | M15 + M16 + M15a + ngày tờ khai BCCT | ✅ Đủ (mới add v10) |
| C5.2 (TP "mồ côi") | M15a + M16 | ✅ |
| C5.3 (tỷ lệ truy nguồn thấp) | M15 + M15a + M16 | ✅ |
| C6.2 (tồn đầu/cuối TP liên kỳ) | ≥2 kỳ M15a | ✅ |
| C6.3 (định mức M16 đột biến giữa kỳ) | ≥2 kỳ M16 | ✅ |
| C6.4 (nhập tăng mạnh, xuất không tăng) | ≥2 kỳ M15 | ✅ |
| C6.5 (mã HS đổi giữa kỳ) | ≥2 kỳ BCCT | ✅ HONG_AN, HIEP_QUANG |

**Kết luận:** Toàn bộ 30 kiểm tra (16 MVP + 14 W.I.P) chạy được với dữ liệu hiện có. Chỉ Nhóm 7 (so sánh giữa DN) cần thêm DN để có baseline thống kê — hiện có 6 DN nhưng phân bố nhiều ngành (cơ khí, dệt may, điện tử), chưa đủ "cùng ngành".

## Mapping Giai đoạn II × dữ liệu hiện có

| Nhóm | Dữ liệu cần | Tình trạng |
|---|---|---|
| 8 (Phế liệu) | Sổ kho phế liệu, hoá đơn bán phế liệu, A42 phế liệu | ❌ Chưa có (đúng kế hoạch §4.2) |
| 9 (BTP) | Sổ BTP, sổ sản xuất, sơ đồ công đoạn | ❌ Chưa có |
| 10 (Sổ sách KT) | Bảng CĐPS, sổ TK 152/155/156, BCTC | ❌ Chưa có |
| 11 (TSCĐ) | Sổ TSCĐ, BC cơ sở sản xuất, hồ sơ máy móc E13 | ❌ Chưa có |
| 12 (NCC) | Danh mục NCC rủi ro, MST format các nước | ❌ Chưa có |

Tất cả 16 kiểm tra Giai đoạn II không demo được trong 10 tuần — đúng kế hoạch.

## Đề xuất ánh xạ DN demo

Đề án §6.1 nói "5 DN giả lập, mỗi DN 3-4 năm". Với dữ liệu thực hiện có, có thể chọn **một trong hai approach**:

**A. Dùng thẳng dữ liệu thực, anonymize.** Bỏ tuần 7-8 (sim dữ liệu). Anonymize ở tuần 1-2 khi build pipeline đọc Excel.

| Mã DN demo | DN thực | Năm dùng | Sai phạm có sẵn (chưa inject) |
|---|---|---|---|
| DN_001 (điện tử HS 85) | GROWATT (3 năm) | 2023-2025 | (cần explore) |
| DN_002 (cơ khí HS 84) | KIM_LONG (2 năm) | 2024-2025 | (cần explore) |
| DN_003 (dệt may HS 61) | HONG_AN (3 năm) | 2023-2025 | (cần explore) — case study cúc áo C4.4 |
| DN_004 (hoá chất HS 39) | DO_THANH (3 năm) | 2023-2025 | (cần explore) |
| DN_005 (sạch) | HONG_PHUC (2 năm) | 2024-2025 | Ít file → ít rủi ro tự nhiên |

> Lưu ý: ngành thực tế của các DN này chưa khớp với đề án. Cần check tên hàng/mã HS để xác định ngành. Đề án có thể điều chỉnh nhẹ §6.1 cho khớp dữ liệu thực.

**B. Dùng dữ liệu thực làm baseline, sinh thêm DN giả lập có sai phạm chủ đích.** Giữ tuần 7-8, dùng dữ liệu thực để học pattern, sinh DN_001-005 mới với sai phạm đã chuẩn bị sẵn cho demo "đẹp".

Khuyến nghị: **approach A** — tiết kiệm 2 tuần, demo trung thực, vẫn có thể inject thêm sai phạm có chủ đích vào 1-2 DN nếu cần.

## Next step

1. Đọc thử **1 file BCQT** (HONG_AN 2024 Mẫu 15) và **1 file BCCT** (HONG_AN HangChiTiet XNK 2024) để hiểu schema thực — input cho viết parser tuần 2.
2. Soạn phương án demo cụ thể: `.ai/sessions/2026-05-21-demo-plan.md`.
3. Khi sang repo MVP riêng (`audit-hq-mvp`?), copy `data/raw/` sang đó (hoặc share via symlink).
