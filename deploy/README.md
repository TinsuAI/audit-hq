# Deploy — Audit-HQ đề án

Static HTML host trên Tinsu VPS qua **Docker nginx**, public qua **Cloudflare Tunnel**.

```
local edit MD → make html → make publish
                              └─ scp HTML → /home/tinsu/audit-hq/html/index.html
                                              └─ docker nginx serves on 127.0.0.1:8757
                                                  └─ cloudflared tunnel → https://audit-hq.sgnai.dev/
```

URL: `https://audit-hq.sgnai.dev/`
Basic-auth credentials: shared riêng (user `tinsu`, password do Tinsu admin giữ).

## Cấu trúc

```
deploy/
├── docker-compose.yml      Single nginx:alpine container, port 127.0.0.1:8757
├── nginx.conf              Static + basic-auth + healthz
├── htpasswd.example        Template (htpasswd thật gitignored)
└── README.md               (file này)
```

Trên VPS:

```
/home/tinsu/audit-hq/
├── docker-compose.yml
├── nginx.conf
├── htpasswd                Basic auth credentials
└── html/
    └── index.html          File HTML đề án (sinh từ make publish)
```

## One-time setup trên VPS

```bash
# 1. Sao chép setup files lên server
scp deploy/docker-compose.yml deploy/nginx.conf deploy/htpasswd tinsu:/home/tinsu/audit-hq/
ssh tinsu "mkdir -p /home/tinsu/audit-hq/html"

# 2. Start container
ssh tinsu "cd /home/tinsu/audit-hq && docker compose up -d"

# 3. Verify (local trên server)
ssh tinsu "curl -fsS http://127.0.0.1:8757/healthz && echo OK"
ssh tinsu "curl -fsSu tinsu:<password> http://127.0.0.1:8757/ -o /dev/null -w '%{http_code}\n'"

# 4. Push HTML lần đầu
make publish
```

## Cloudflare Tunnel — bước duy nhất cần sudo

Cloudflared tunnel `tinsu-online-server` (UUID `691a9772-3168-422e-81eb-7c26e1dec9ef`) cần thêm ingress rule cho audit-hq:

```bash
ssh tinsu
# Backup config
sudo cp /etc/cloudflared/config.yml /etc/cloudflared/config.yml.bak.audit-hq

# Edit /etc/cloudflared/config.yml — thêm 2 dòng TRƯỚC dòng `service: http_status:404`:
sudo nano /etc/cloudflared/config.yml
```

Thêm khối sau (đặt trước `- service: http_status:404`):

```yaml
  - hostname: audit-hq.sgnai.dev
    service: http://localhost:8757
```

Reload + tạo DNS:

```bash
sudo systemctl reload cloudflared

# Tạo CNAME audit-hq.sgnai.dev → tunnel (auto qua Cloudflare API)
sudo cloudflared tunnel route dns tinsu-online-server audit-hq.sgnai.dev
```

Verify từ máy ngoài:

```bash
curl -fsSu tinsu:<password> https://audit-hq.sgnai.dev/ -o /dev/null -w '%{http_code}\n'
# expect: 200
```

## Routine publish (sau khi sửa MD local)

```bash
make all     # = make html + make publish
```

`make publish` scp HTML đến `/home/tinsu/audit-hq/html/index.html`. nginx serve trực tiếp, không cần restart container.

## Rotate basic-auth password

Local:

```bash
NEW_PASS=$(python3 -c "import secrets, string; print(''.join(secrets.choice(string.ascii_letters+string.digits) for _ in range(14)))")
HASH=$(openssl passwd -apr1 "$NEW_PASS")
echo "tinsu:$HASH" > deploy/htpasswd
echo "New password: $NEW_PASS"
scp deploy/htpasswd tinsu:/home/tinsu/audit-hq/htpasswd
ssh tinsu "docker exec audit-hq nginx -s reload || (cd /home/tinsu/audit-hq && docker compose restart)"
```

## Decommission

```bash
ssh tinsu "cd /home/tinsu/audit-hq && docker compose down && cd .. && rm -rf audit-hq"
# Sudo: xoá ingress rule trong /etc/cloudflared/config.yml + reload cloudflared
sudo cloudflared tunnel route dns --overwrite-dns tinsu-online-server <bỏ qua>
```

## Auto-deploy CI/CD — Phase 2

Khi nội dung đề án ổn định và muốn auto-publish trên push GitHub: thêm `.github/workflows/publish.yml` dùng self-hosted runner trên tinsu (tham khảo pattern `data-hub` + `barry-CO`). Chưa cần trong Phase 1 vì draft thay đổi nhanh, `make publish` đơn giản hơn.
