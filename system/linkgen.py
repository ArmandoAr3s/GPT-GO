import json, sys, pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parents[1]
links_json = ROOT / "system" / "links.json"
out_md = ROOT / "LINKS.md"

def h(sec): 
    return f"## {sec}"

def md_link(name, url):
    return f"- [{name}]({url})" if (url or "").startswith(("http://","https://")) else f"- {name}: `{url}`"

def main():
    now = datetime.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%SZ")
    if not links_json.exists():
        print("system/links.json not found", file=sys.stderr)
        sys.exit(1)
    data = json.loads(links_json.read_text(encoding="utf-8") or "{}")
    projects = data.get("projects", [])
    canon = data.get("canon", [])
    artifacts = data.get("artifacts", [])

    lines = []
    lines.append("# 🔗 LINKS — Registry (auto-generated)")
    lines.append("")
    lines.append(f"_Last update (UTC): {now}_")
    lines.append("")

    lines.append(h("Kanonikë"))
    if canon:
        for c in canon:
            lines.append(md_link(c.get("name","—"), c.get("path_or_url","")))
    else:
        lines.append("- —")
    lines.append("")

    lines.append(h("Projekte"))
    if projects:
        for p in projects:
            name = p.get("name","—")
            repo = p.get("repo","")
            docs = p.get("docs_index","")
            status = p.get("status","")
            owner = p.get("owner","")
            lines.append(f"- **{name}** — status: _{status}_; owner: _{owner}_")
            if repo: lines.append(f"  - repo: {repo}")
            if docs: lines.append(f"  - docs: {docs}")
    else:
        lines.append("- —")
    lines.append("")

    lines.append(h("Artefakte"))
    if artifacts:
        for a in artifacts:
            lines.append(md_link(a.get("name","—"), a.get("permalink","")))
    else:
        lines.append("- —")
    lines.append("")

    out_md.write_text("\n".join(lines), encoding="utf-8")
    print(f"Wrote {out_md}")

if __name__ == "__main__":
    main()
