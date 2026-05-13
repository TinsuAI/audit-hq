#!/usr/bin/env python3
"""
Idempotently add audit-hq.tinsu.ai → http://localhost:8757 to the
remotely-managed Cloudflare Tunnel config.

The tunnel `tinsu-online-server` is *remotely-managed* in the Cloudflare
Zero Trust dashboard, so editing /etc/cloudflared/config.yml has NO effect.
Ingress entries must be set via the Cloudflare API.

This script reads the API token from ~/.cloudflared/cert.pem (the Argo
Tunnel token, which is base64-encoded JSON containing apiToken + accountID),
fetches the current tunnel configuration, inserts the audit-hq hostname
before the catch-all 404, and PUTs the updated config back.

Run on the Tinsu VPS as user `tinsu` (the one that owns the cert.pem):

    python3 deploy/scripts/add-ingress.py
"""

import base64
import json
import sys
import urllib.error
import urllib.request

CERT_PATH = "/home/tinsu/.cloudflared/cert.pem"
TUNNEL_ID = "691a9772-3168-422e-81eb-7c26e1dec9ef"
HOSTNAME = "audit-hq.tinsu.ai"
SERVICE = "http://localhost:8757"


def load_credentials():
    with open(CERT_PATH) as f:
        pem = f.read()
    b64 = "".join(line for line in pem.splitlines() if "TUNNEL" not in line)
    data = json.loads(base64.b64decode(b64))
    return data["apiToken"], data["accountID"]


def main():
    token, acct = load_credentials()
    url = f"https://api.cloudflare.com/client/v4/accounts/{acct}/cfd_tunnel/{TUNNEL_ID}/configurations"
    headers = {"Authorization": f"Bearer {token}"}

    cur = json.load(urllib.request.urlopen(
        urllib.request.Request(url, headers=headers)
    ))
    ingress = cur["result"]["config"]["ingress"]
    print(f"current entries: {len(ingress)}")

    if any(e.get("hostname") == HOSTNAME for e in ingress):
        print(f"{HOSTNAME} already present, nothing to do")
        return 0

    new_entry = {"hostname": HOSTNAME, "service": SERVICE}
    named = [e for e in ingress if "hostname" in e]
    catchall = [e for e in ingress if "hostname" not in e]
    new_ingress = named + [new_entry] + catchall

    payload = {"config": {"ingress": new_ingress}}
    if "warp-routing" in cur["result"]["config"]:
        payload["config"]["warp-routing"] = cur["result"]["config"]["warp-routing"]

    body = json.dumps(payload).encode()
    req = urllib.request.Request(
        url, data=body, method="PUT",
        headers={**headers, "Content-Type": "application/json"},
    )
    try:
        resp = json.load(urllib.request.urlopen(req))
    except urllib.error.HTTPError as exc:
        print(f"HTTP {exc.code}:", exc.read().decode(), file=sys.stderr)
        return 1

    print(f"PUT success: {resp.get('success')}")
    print(f"new version: {resp['result']['version']}, entries: {len(resp['result']['config']['ingress'])}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
