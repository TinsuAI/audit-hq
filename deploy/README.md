# Deploy — Audit-HQ đề án

> Static HTML host trên Tinsu VPS, phục vụ tại `https://audit-hq.sgnai.dev/`.
> Không có app code. Chỉ scp file `de-an-audit-hq.html` → nginx serve.

## Layout

```
/home/tinsu/audit-hq/              ← static root
└── index.html                     ← scp từ local `de-an-audit-hq.html`

/etc/nginx/sites-available/audit-hq.conf  ← vhost (template tại `nginx/audit-hq.conf`)
/etc/nginx/htpasswd-audit-hq              ← basic auth users
/etc/letsencrypt/live/audit-hq.sgnai.dev/ ← TLS cert
```

## One-time setup trên Tinsu VPS

SSH vào server:

```bash
ssh tinsu  # alias: 100.84.189.87 / user tinsu
```

### 1. Tạo static root

```bash
mkdir -p /home/tinsu/audit-hq
chmod 755 /home/tinsu/audit-hq
```

### 2. DNS

Thêm record `A` cho `audit-hq.sgnai.dev` → IP công khai Tinsu VPS. (Làm trên DNS provider của sgnai.dev.)

### 3. Basic-auth credentials

```bash
sudo apt install apache2-utils  # nếu chưa có htpasswd
sudo htpasswd -c /etc/nginx/htpasswd-audit-hq tinsu
# (nhập password, lưu lại để chia sẻ với reviewer)

# Thêm user khác (vd cho HQ reviewer):
sudo htpasswd /etc/nginx/htpasswd-audit-hq hq-reviewer
```

### 4. Let's Encrypt cert

```bash
sudo certbot certonly --webroot \
  -w /var/www/letsencrypt \
  -d audit-hq.sgnai.dev \
  --email admin@sgnai.dev \
  --agree-tos --non-interactive
```

### 5. nginx vhost

Từ máy local sau khi clone repo:

```bash
scp deploy/nginx/audit-hq.conf tinsu:/tmp/
ssh tinsu
sudo install -m 0644 /tmp/audit-hq.conf /etc/nginx/sites-available/
sudo ln -s ../sites-available/audit-hq.conf /etc/nginx/sites-enabled/
sudo nginx -t && sudo systemctl reload nginx
```

### 6. Verify

```bash
# Healthcheck
curl -u tinsu:<password> https://audit-hq.sgnai.dev/

# Hoặc browser
open https://audit-hq.sgnai.dev/
```

## Routine publish (từ máy local sau khi sửa MD)

```bash
make html      # regenerate de-an-audit-hq.html
make publish   # scp đến tinsu:/home/tinsu/audit-hq/index.html
```

Hoặc gộp:

```bash
make all
```

## Auto-deploy CI/CD (Phase 2)

Khi nội dung đề án ổn định và muốn auto-publish trên push, sẽ thêm:

- `.github/workflows/publish.yml` — trigger trên push main
- Self-hosted runner trên Tinsu (label `audit-hq-static`)
- Hoặc SSH-based action với deploy key trong GitHub secrets

Chưa làm trong Phase 1 vì draft thay đổi nhanh, manual `make publish` đáp ứng tốt hơn.

## Renew cert

`certbot renew` auto qua cronjob. Verify:

```bash
sudo certbot certificates
```

## Rotate basic-auth password

```bash
sudo htpasswd /etc/nginx/htpasswd-audit-hq tinsu  # overwrite
```

Reload không cần thiết — nginx đọc file mỗi request.

## Decommission

Khi đề án done hoặc chuyển sang repo code thật:

```bash
sudo rm /etc/nginx/sites-enabled/audit-hq.conf
sudo nginx -t && sudo systemctl reload nginx
sudo certbot delete --cert-name audit-hq.sgnai.dev
sudo rm -rf /home/tinsu/audit-hq /etc/nginx/htpasswd-audit-hq
```
