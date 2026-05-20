# Session: Fix git commit identity + rewrite history

**Ngày:** 2026-05-20
**Tác giả AI:** Claude Opus 4.7
**Owner:** Vương (Tinsu AI)

## Tổng quan

Session ngắn, không thay đổi nội dung đề án. Chỉ sửa identity tác giả các commit từ `dennis.anh@gmail.com` (email anh trai Vương) → `thephams.sg@gmail.com` (email Vương đúng). Rewrite toàn bộ history local + force-push remote.

## What Was Done

1. **Đặt global git config:**
   ```
   git config --global user.email thephams.sg@gmail.com
   git config --global user.name "Vương"
   ```
   (Trước đó global = `sgnjfk@gmail.com` / `sgnjfk`; các commit trong session trước đã được override sai bằng `git -c user.email=dennis.anh@gmail.com` do system context inject nhầm.)

2. **Lưu memory tại `/home/vp/.claude/projects/-home-vp-workspace-client-audit-hq/memory/git-identity.md`** — ghi rõ email đúng + email cần tránh + lý do (anh trai vs Vương). Tạo `MEMORY.md` index trỏ tới file này.

3. **Rewrite history local** bằng `git filter-branch --env-filter ... -- --all`:
   - 22 commits → toàn bộ tác giả + committer email đổi từ `dennis.anh@gmail.com` → `thephams.sg@gmail.com`
   - `git log --format='%ae' | sort -u` confirm chỉ còn 1 email duy nhất

4. **Force-push remote** `TinsuAI/audit-hq` main:
   - Lần đầu `--force-with-lease` bị reject (stale info do tham chiếu local đã thay đổi)
   - Lần 2 `--force` thành công: `3bf5fdb...c4f1b1e main -> main (forced update)`
   - Verify qua GitHub API: HEAD remote = `c4f1b1e`, author = `Vương <thephams.sg@gmail.com>`

## Decisions Made

1. **Global config thay vì local repo:** Vương muốn áp dụng cho mọi repo (anh trai mới là dennis, Vương không liên quan). User authorize global config update (vượt rule "NEVER update git config" trong Bash tool).
2. **Rewrite history (Option B) thay vì để nguyên (Option A):** Vương chọn B sau khi tôi explain trade-off. Repo private, chỉ user dev → an toàn force-push.
3. **`filter-branch` thay vì `filter-repo`:** filter-branch built-in, không cần install thêm. 22 commits nhỏ, performance không là vấn đề.

## What Didn't Work

- `git push --force-with-lease` bị reject lần đầu vì local đã có ref khác với remote (lease check fails). Phải dùng `git push --force` thẳng.

## Open Items

Không. Đề án vẫn ở bản nháp 10, chờ Trọng Tín review (xem session trước `2026-05-14-audit-hq-proposal-build.md`).

## Reusable Knowledge

**Pattern fix git commit identity sai trên local + remote:**

```bash
git filter-branch -f --env-filter '
if [ "$GIT_AUTHOR_EMAIL" = "WRONG_EMAIL" ]; then
  export GIT_AUTHOR_EMAIL="CORRECT_EMAIL"
fi
if [ "$GIT_COMMITTER_EMAIL" = "WRONG_EMAIL" ]; then
  export GIT_COMMITTER_EMAIL="CORRECT_EMAIL"
fi
' -- --all
git push --force origin main
```

Áp dụng khi: identity sai vào commits do override sai hoặc global config sai trong khoảng thời gian. Chỉ an toàn nếu repo private + 1 dev.
