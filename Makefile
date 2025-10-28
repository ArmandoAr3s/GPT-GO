# MindSync Makefile — simple bootstrap
.PHONY: init sync check context links

init:
	@mkdir -p nucleus/templates system projects/GPT-GO/docs context docs/context
	@if [ ! -f BOOT.md ]; then echo "# BOOT" > BOOT.md; fi
	@if [ ! -f system/status.json ]; then echo '{"updated_at":"2025-10-28","phase":"INIT","active_project":"","version":"v1.0.0","owner":"","note":"init"}' > system/status.json; fi
	@if [ ! -f system/links.json ]; then echo '{"projects":[],"canon":[{"name":"BOOT","path_or_url":"./BOOT.md"}],"artifacts":[]}' > system/links.json; fi
	@echo "Initialized basic structure."

check:
	@python - << 'PY'
import json,sys
from pathlib import Path
ok=True
for p in ["system/status.json","system/links.json"]:
    path=Path(p)
    try:
        json.loads(path.read_text(encoding="utf-8"))
        print(f"[check] OK  {p}")
    except Exception as e:
        print(f"[check] FAIL {p}: {e}"); ok=False
sys.exit(0 if ok else 1)
PY

links:
	@if [ -f system/linkgen.py ]; then python system/linkgen.py; else echo "No system/linkgen.py; skip"; fi

context:
	@python system/build_context.py

sync: check links context
	@echo "Sync complete. Artifacts: LINKS.md, context/index.json, docs/context/index.json"
