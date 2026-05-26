# Thư viện văn bản pháp lý — Audit-HQ

> Văn bản pháp lý liên quan trực tiếp đến nghiệp vụ Audit-HQ (quản lý rủi ro hải quan, BCQT, định mức, phân loại hàng hóa). Lưu để: (1) tham chiếu khi soạn đề án, (2) ingest vào RAG cho AI assistant trong MVP, (3) tránh nhầm lẫn pháp lý khi build features.
>
> **Nguyên tắc lưu**: trích điều khoản cốt lõi + paraphrase, KHÔNG copy full văn bản (bản quyền + bloat). Mỗi file có frontmatter để AI parse.
>
> Khi ingest vào RAG: chunk theo điều/khoản, embed body + title + scope. Frontmatter giúp filter (vd. tìm "văn bản hiệu lực 2024+ về BCQT").

## Đã ingest

| Số văn bản | Tên ngắn | Phạm vi | File |
|---|---|---|---|
| 81/2019/TT-BTC | Quản lý rủi ro hải quan | Phân loại tuân thủ DN, 5 mức + 9 hạng rủi ro | [thong-tu-81-2019-tt-btc.md](thong-tu-81-2019-tt-btc.md) |

## Cần ingest dần (backlog)

- **TT 39/2018/TT-BTC** sửa đổi TT 38/2015 — Thủ tục hải quan, kiểm tra giám sát, thuế XNK. Là cơ sở pháp lý cho M15/M15a/M16/BCQT.
- **TT 38/2015/TT-BTC** — Thủ tục hải quan gốc.
- **Nghị định 08/2015/NĐ-CP** — Luật Hải quan thi hành; Điều 10 (DN ưu tiên).
- **TT 72/2015/TT-BTC** — Chế độ DN ưu tiên (chi tiết Mức 1).
- **TT 06/2024/TT-BTC** — Sửa đổi TT 81/2019 (cần fetch để check thay đổi).
- **Quyết định 2218/QĐ-TCHQ** (26/8/2020) — Quy trình quản lý rủi ro 5 bước.
- **Luật Hải quan 54/2014/QH13** — Khung cao nhất.

## Quy ước

- Mỗi file 1 văn bản. Tên file = số văn bản kebab-case.
- Update frontmatter khi văn bản có sửa đổi.
- Khi văn bản hết hiệu lực: KHÔNG xoá, đổi `status: superseded` + link tới văn bản mới.
- Khi có câu hỏi pháp lý phát sinh trong session, fetch + lưu vào đây cho session sau.
