# Deploy — Audit-HQ đề án

Static HTML host trên Tinsu VPS qua **Docker nginx**, public qua **Cloudflare Tunnel** (`tinsu-online-server`).

```
local edit MD → make html → make publish
                              └─ scp HTML → /home/tinsu/audit-hq/html/index.html
                                              └─ docker nginx serves on 127.0.0.1:8757
                                                  └─ cloudflared tunnel → https://audit-hq.tinsu.ai/
```

URL: `https://audit-hq.tinsu.ai/` (public từ v0.2 — bỏ basic-auth)

## Cấu trúc

Repo:
```
deploy/
├── docker-compose.yml      nginx:alpine container, port 127.0.0.1:8757
├── nginx.conf              static + healthz (không auth)
├── scripts/
│   └── add-ingress.py      idempotent: add audit-hq ingress qua Cloudflare API
└── README.md               (file này)
```

Trên VPS (`/home/tinsu/audit-hq/`):
```
docker-compose.yml + nginx.conf + html/index.html
```

## One-time setup trên VPS

```bash
# 1. SSH (ssh.exe Windows, vì WSL ssh đang lỗi)
ssh tinsu                         # alias: 100.84.189.87 / tinsu

# 2. Tạo dir + scp config files (từ máy local)
ssh tinsu "mkdir -p /home/tinsu/audit-hq/html"
scp deploy/docker-compose.yml deploy/nginx.conf tinsu:/home/tinsu/audit-hq/

# 3. Start container
ssh tinsu "cd /home/tinsu/audit-hq && docker compose up -d"

# 4. Verify localhost (trên server)
ssh tinsu "curl -fsS http://127.0.0.1:8757/healthz"
# → ok

# 5. Push HTML lần đầu
make publish
```

## Cloudflare Tunnel — add public hostname

Tunnel `tinsu-online-server` là **remotely-managed** — config lưu trên Cloudflare Zero Trust dashboard, KHÔNG phải `/etc/cloudflared/config.yml` (file này được merge với remote nhưng remote thắng).

Để thêm ingress, dùng script API (không cần sudo, đọc token từ `~/.cloudflared/cert.pem`):

```bash
scp deploy/scripts/add-ingress.py tinsu:/tmp/
ssh tinsu "python3 /tmp/add-ingress.py && rm /tmp/add-ingress.py"
```

Output thành công:
```
current entries: 17
PUT success: True
new version: 28, entries: 18
```

Tạo DNS CNAME (chỉ cần lần đầu, cần sudo):

```bash
ssh tinsu "sudo cloudflared tunnel route dns tinsu-online-server audit-hq.tinsu.ai"
```

Verify từ máy local (~10s sau khi cloudflared sync):

```bash
curl -fsS https://audit-hq.tinsu.ai/healthz                                # → ok
curl -fsS https://audit-hq.tinsu.ai/ -o /dev/null -w '%{http_code}\n'      # → 200
```

## Routine publish (sau khi sửa MD local)

```bash
make all     # = make html + make publish
```

`make publish` scp HTML → `/home/tinsu/audit-hq/html/index.html`. nginx auto-serve, không restart container.

## Decommission

```bash
ssh tinsu "cd /home/tinsu/audit-hq && docker compose down && cd .. && rm -rf audit-hq"
# Cloudflare side: xoá ingress qua dashboard hoặc API + xoá DNS CNAME
```

## Auto-deploy CI/CD — Phase 2

Khi nội dung đề án ổn định và muốn auto-publish khi push GitHub: thêm `.github/workflows/publish.yml` dùng self-hosted runner trên tinsu (pattern data-hub + barry-CO). Chưa cần Phase 1 vì draft thay đổi nhanh, `make publish` đơn giản hơn.

## Domain notes

- Sử dụng `tinsu.ai` (không phải `sgnai.dev`) vì:
  - Cert tunnel (`~/.cloudflared/cert.pem`) chỉ có quyền cho zone `tinsu.ai`
  - Các service khác trong tunnel cũng dùng `*.tinsu.ai` (barry, airsur, ttdatahub, barry-co, bcqt-showcase, hub, office, kiot, trongtinerp, tamnamduoc)
- Stale DNS `audit-hq.sgnai.dev.tinsu.ai` (do thử nhầm lần đầu) là CNAME vô hại; xoá tuỳ chọn qua Cloudflare dashboard
