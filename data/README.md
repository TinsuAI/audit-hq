# Dữ liệu nền cho Audit-HQ demo

> **CẢNH BÁO:** Thư mục `raw/` chứa **dữ liệu thực** từ khách hàng của Trọng Tín (tên DN thật, số tờ khai thật, công văn scan). KHÔNG commit, KHÔNG public. Đã gitignore ở root.

## Nguồn

- Trọng Tín cung cấp ngày **2026-05-20** (sau khi HQ duyệt nguyên tắc đề án).
- File gốc: `TONG HOP BCQT-20260520T161442Z-3-001.zip` (90MB nén, 497MB giải nén).
- 622 file Excel/PDF/Word từ 6 doanh nghiệp, độ phủ 2015–2025.

## Cấu trúc

```
raw/<DN>/<năm>/<loại báo cáo>/<file>
```

- `<DN>` (6): `DO_THANH`, `GROWATT`, `HIEP_QUANG`, `HONG_AN`, `HONG_PHUC`, `KIM_LONG`
- `<năm>`: `2015`-`2025`, `multi_year` (file phủ nhiều năm), `unknown` (không xác định được năm)
- `<loại báo cáo>`:
  - `BCQT` — Báo cáo Quyết toán TT39 (mẫu 15 NVL/SP, mẫu cũ TT38)
  - `DINH_MUC` — Báo cáo định mức (BCDM, mẫu 16, ĐMSX)
  - `HANG_CHI_TIET` — Báo cáo hàng chi tiết NK/XK (theo dõi mã hàng)
  - `TKXNK` — Tờ khai XNK (ToKhai, BaoCaoToKhai)
  - `BCTT79` — Báo cáo theo Thông tư 79 (đã hết hiệu lực, vẫn lưu để tham chiếu)
  - `NXT_TON` — Bảng nhập-xuất-tồn nguyên vật liệu, tồn kho
  - `MA_NVL_SP` — Danh mục mã NVL / mã SP
  - `PHE_LIEU` — Phế liệu (chương 8.x của catalog)
  - `SO_KE_TOAN` — Sổ kế toán (chương 10.x catalog)
  - `CHUNG_TU` — Chứng từ PDF (tờ khai sửa, invoice)
  - `CONG_VAN` — Công văn giải trình (.doc/.docx)
  - `ANH_SCAN` — Ảnh JPG/PNG (scan chứng từ)
  - `XML` — File XML (chắc là export từ ECUS)
  - `OTHER` — Chưa phân loại được

## Độ phủ tổng quát

| DN          | Năm có dữ liệu                              | File | Size  |
|-------------|---------------------------------------------|------|-------|
| HONG_AN     | 2018, 2019, 2020, 2021, 2022, 2023, 2024, 2025 | 307  | 278M  |
| HIEP_QUANG  | 2015–2025 (11 năm)                          | 220  | 55M   |
| DO_THANH    | 2023, 2024, 2025                            | 49   | 152M  |
| HONG_PHUC   | 2024, 2025                                  | 27   | 2.3M  |
| GROWATT     | 2023, 2024, 2025                            | 10   | 8.4M  |
| KIM_LONG    | 2024, 2025                                  | 9    | 1.4M  |

**HONG_AN** là DN có độ phủ tốt nhất (8 năm liền, đầy đủ BCQT + tờ khai + định mức + chứng từ sửa) — chọn làm "DN chính" cho demo.

## Loại báo cáo theo DN (file count)

| DN         | BCQT | DINH_MUC | NXT_TON | TKXNK | HANG_CHI_TIET | BCTT79 | CHUNG_TU | CONG_VAN | OTHER |
|------------|------|----------|---------|-------|---------------|--------|----------|----------|-------|
| HONG_AN    | 51   | 50       | 30      | 57    | 11            | 9      | 43       | 8        | 30    |
| HIEP_QUANG | 26   | 73       | 24      | 11    | 4             | 41     | 5        | 2        | 34    |
| DO_THANH   | 15   | 21       | 3       | 0     | 4             | 0      | 0        | 0        | 6     |
| HONG_PHUC  | 14   | 8        | 2       | 0     | 1             | 0      | 0        | 0        | 1     |
| GROWATT    | 6    | 3        | 0       | 0     | 1             | 0      | 0        | 0        | 0     |
| KIM_LONG   | 5    | 2        | 0       | 0     | 1             | 0      | 0        | 0        | 0     |

## Lưu ý xử lý

1. **Tên file Việt có dấu** — đã giữ nguyên (UTF-8). Khi viết code đọc Excel, dùng `pathlib.Path` + UTF-8 locale.
2. **Trùng tên** — đã tự thêm suffix `__dup1`, `__dup2`, `__rec1` (re-classified). Không mất file nào.
3. **File draft / "bản nháp" / "chạy lại"** — vẫn lưu để compare giữa các version (rất hữu ích để test rule `BCQT có nhiều revision`).
4. **Folder "GỬI KHÁCH" / "CHẠY"** — của Trọng Tín, không phải DN. Đã merge vào `<năm>` tương ứng, mất context "version" — nếu cần khôi phục, parse lại từ `_inbox/` (đã xóa).
5. **HIEP_QUANG `unknown`** — 9 file BCTT79 ko parse được năm, vì tên `BCTT79_*.xlsx`. Cần đọc trong sheet để xác định kỳ báo cáo.

## Tham chiếu

- Đề án: `../de-an-audit-hq.md` (49 kiểm tra, lộ trình 10 tuần)
- Mapping dữ liệu ↔ catalog: `../.ai/sessions/2026-05-21-data-mapping.md` (sẽ tạo)
- Phương án demo: `../.ai/sessions/2026-05-21-demo-plan.md` (sẽ tạo)
