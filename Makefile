.PHONY: html publish clean help

# Deploy target — Tinsu VPS (Tailscale host alias `tinsu` in ~/.ssh/config)
DEPLOY_HOST  := tinsu
DEPLOY_PATH  := /home/tinsu/audit-hq
PUBLIC_URL   := https://audit-hq.sgnai.dev/

MD  := de-an-audit-hq.md
HTML := de-an-audit-hq.html
CSS := style.css

help:
	@echo "make html      → render $(MD) → $(HTML)"
	@echo "make publish   → scp $(HTML) to $(DEPLOY_HOST):$(DEPLOY_PATH)/index.html"
	@echo "make all       → html + publish"
	@echo "make clean     → remove $(HTML)"
	@echo ""
	@echo "Public URL: $(PUBLIC_URL)"

html: $(HTML)

$(HTML): $(MD) $(CSS)
	pandoc $(MD) \
		--standalone \
		--embed-resources \
		--toc --toc-depth=3 \
		--metadata title="Đề án Audit-HQ (DRAFT)" \
		--metadata lang=vi \
		--css=$(CSS) \
		-o $(HTML)
	@echo "Rendered → $(HTML)"

publish: $(HTML)
	scp $(HTML) $(DEPLOY_HOST):$(DEPLOY_PATH)/index.html
	@echo "Published → $(PUBLIC_URL)"

all: html publish

clean:
	rm -f $(HTML)
