# system/build_context.py
# Builds a single live context JSON by merging system/status.json + system/links.json.
# Output: context/index.json  (and optionally copies to docs/context/ for GitHub Pages)
import json, pathlib, datetime, sys, shutil

ROOT = pathlib.Path(__file__).resolve().parents[1]
STATUS = ROOT / "system" / "status.json"
LINKS  = ROOT / "system" / "links.json"
OUT    = ROOT / "context" / "index.json"
DOCS   = ROOT / "docs" / "context" / "index.json"  # if Pages is set to /docs

def read_json(path):
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as e:
        print(f"[build_context] failed to read {path}: {e}", file=sys.stderr)
        return {}

def main():
    status = read_json(STATUS)
    links  = read_json(LINKS)
    ctx = {
        "updated_at": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
        "status": {
            "phase": status.get("phase", "INIT"),
            "active_project": status.get("active_project", ""),
            "version": status.get("version", "v1.0.0"),
            "note": status.get("note", ""),
        },
        "projects": links.get("projects", []),
        "canon": links.get("canon", []),
        "links_doc": "LINKS.md"
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(ctx, indent=2), encoding="utf-8")
    # Optional copy to docs/
    DOCS.parent.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(OUT, DOCS)
    print(f"[build_context] wrote {OUT}")
    print(f"[build_context] copied to {DOCS} (for GitHub Pages)")

if __name__ == "__main__":
    main()
