"""Build the static portfolio website in docs/ from the repository's markdown.

Every markdown file becomes a styled HTML page with shared navigation, a table
of contents and working cross-links. docs/index.html becomes the portfolio home.
docs/case-study.html is hand-written and is left untouched.

Usage (from the repository root):
    python scripts/build_site.py

Standard library only. Supports the markdown subset used in this repo:
headings, paragraphs, lists (nested, task lists), tables, fenced code,
blockquotes, horizontal rules, links, bold, italics and inline code.
"""
from __future__ import annotations

import html
import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DOCS = ROOT / "docs"
REPO_URL = "https://github.com/AkanshaBB31/TPM_work"
SKIP_DIRS = {".git", "docs", "scripts", "_private", "__pycache__"}


# --------------------------------------------------------------------------- markdown

def slugify(text: str) -> str:
    text = re.sub(r"<[^>]+>", "", text)
    text = re.sub(r"[^\w\s-]", "", text.lower())
    return re.sub(r"[\s_]+", "-", text).strip("-")


class Renderer:
    def __init__(self, link_fn):
        self.link_fn = link_fn
        self.toc: list[tuple[str, str]] = []
        self.title = ""

    # ---- inline -----------------------------------------------------------
    def inline(self, text: str) -> str:
        codes: list[str] = []

        def keep_code(m):
            codes.append(f"<code>{html.escape(m.group(1))}</code>")
            return f"\x00{len(codes) - 1}\x00"

        text = re.sub(r"`([^`]+)`", keep_code, text)
        text = html.escape(text, quote=False)

        def link(m):
            label, target = m.group(1), html.unescape(m.group(2))
            href = self.link_fn(target)
            ext = href.startswith("http") and not href.startswith(REPO_URL)
            attrs = ' target="_blank" rel="noopener"' if ext else ""
            return f'<a href="{html.escape(href)}"{attrs}>{label}</a>'

        text = re.sub(r"\[([^\]]+)\]\(([^)\s]+)\)", link, text)
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<![\*\w])\*(?!\s)(.+?)(?<!\s)\*(?![\*\w])", r"<em>\1</em>", text)
        text = re.sub(r"\x00(\d+)\x00", lambda m: codes[int(m.group(1))], text)
        return text

    # ---- blocks -----------------------------------------------------------
    def render(self, md: str) -> str:
        lines = md.replace("\r\n", "\n").split("\n")
        return self.blocks(lines)

    def blocks(self, lines: list[str]) -> str:
        out: list[str] = []
        i, n = 0, len(lines)
        while i < n:
            line = lines[i]
            s = line.strip()
            if not s:
                i += 1
                continue
            # fenced code
            if s.startswith("```"):
                lang = s[3:].strip()
                buf = []
                i += 1
                while i < n and not lines[i].strip().startswith("```"):
                    buf.append(lines[i])
                    i += 1
                i += 1
                cls = f' class="lang-{html.escape(lang)}"' if lang else ""
                out.append(f"<pre><code{cls}>{html.escape(chr(10).join(buf))}</code></pre>")
                continue
            # heading
            m = re.match(r"^(#{1,6})\s+(.*)$", s)
            if m:
                level, body = len(m.group(1)), self.inline(m.group(2))
                hid = slugify(body)
                if level == 1 and not self.title:
                    self.title = html.unescape(re.sub(r"<[^>]+>", "", body))
                if level == 2:
                    self.toc.append((hid, html.unescape(re.sub(r"<[^>]+>", "", body))))
                out.append(f'<h{level} id="{hid}">{body}</h{level}>')
                i += 1
                continue
            # horizontal rule
            if re.match(r"^-{3,}$", s):
                out.append("<hr>")
                i += 1
                continue
            # table
            if s.startswith("|") and i + 1 < n and re.match(r"^\|?\s*:?-{2,}", lines[i + 1].strip()):
                rows = []
                while i < n and lines[i].strip().startswith("|"):
                    rows.append(lines[i].strip())
                    i += 1
                out.append(self.table(rows))
                continue
            # blockquote
            if s.startswith(">"):
                buf = []
                while i < n and lines[i].strip().startswith(">"):
                    buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                    i += 1
                out.append(f"<blockquote>{self.blocks(buf)}</blockquote>")
                continue
            # list
            if re.match(r"^\s*([-*]|\d+\.)\s+", line):
                buf = []
                while i < n and (re.match(r"^\s*([-*]|\d+\.)\s+", lines[i]) or
                                 (lines[i].startswith("  ") and lines[i].strip())):
                    buf.append(lines[i])
                    i += 1
                out.append(self.list_block(buf))
                continue
            # paragraph
            buf = []
            while i < n and lines[i].strip() and not re.match(
                    r"^(#{1,6}\s|```|>|\||-{3,}$|\s*([-*]|\d+\.)\s+)", lines[i].strip()):
                buf.append(self.inline(lines[i].strip()))
                i += 1
            out.append("<p>" + "<br>".join(buf) + "</p>")
        return "\n".join(out)

    def table(self, rows: list[str]) -> str:
        def cells(r):
            r = r.strip().strip("|")
            return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", r)]

        head = cells(rows[0])
        body = [cells(r) for r in rows[2:]]
        h = "".join(f"<th>{self.inline(c)}</th>" for c in head)
        b = "".join("<tr>" + "".join(f"<td>{self.inline(c)}</td>" for c in r) + "</tr>" for r in body)
        return f'<div class="table-wrap"><table><thead><tr>{h}</tr></thead><tbody>{b}</tbody></table></div>'

    def list_block(self, lines: list[str]) -> str:
        indent = len(lines[0]) - len(lines[0].lstrip())
        ordered = bool(re.match(r"^\s*\d+\.", lines[0]))
        items: list[list[str]] = []
        for ln in lines:
            ind = len(ln) - len(ln.lstrip())
            if ind <= indent and re.match(r"^\s*([-*]|\d+\.)\s+", ln):
                items.append([re.sub(r"^\s*([-*]|\d+\.)\s+", "", ln)])
            elif items:
                items[-1].append(ln)
        tag = "ol" if ordered else "ul"
        parts = []
        task_list = False
        for it in items:
            first, rest = it[0], it[1:]
            box = re.match(r"^\[( |x|X)\]\s+(.*)$", first)
            if box:
                task_list = True
                mark = "☑" if box.group(1).lower() == "x" else "☐"
                content = f'<span class="box" aria-hidden="true">{mark}</span>{self.inline(box.group(2))}'
            else:
                content = self.inline(first)
            sub = [r for r in rest if re.match(r"^\s*([-*]|\d+\.)\s+", r)]
            cont = [r.strip() for r in rest if r not in sub]
            if cont:
                content += "<br>" + "<br>".join(self.inline(c) for c in cont)
            if sub:
                content += self.list_block(sub)
            parts.append(f"<li>{content}</li>")
        cls = ' class="tasks"' if task_list else ""
        return f"<{tag}{cls}>" + "".join(parts) + f"</{tag}>"


# --------------------------------------------------------------------------- site model

def md_files() -> list[Path]:
    files = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = sorted(d for d in dirnames if d not in SKIP_DIRS)
        for f in sorted(filenames):
            if f.endswith(".md"):
                files.append(Path(dirpath) / f)
    return files


def site_path(repo_rel: str) -> str | None:
    """Map a repo-relative path to its site-relative output path (or None)."""
    p = repo_rel.replace("\\", "/")
    if p.startswith("docs/"):
        return p[len("docs/"):] or "index.html"
    if p in ("", ".", "README.md"):
        return "index.html"
    full = ROOT / p
    if full.is_dir():
        return p.rstrip("/") + "/index.html" if (full / "README.md").exists() else None
    if p.endswith("README.md"):
        return p[: -len("README.md")] + "index.html"
    if p.endswith(".md"):
        return p[:-3] + ".html"
    return None


def make_link_fn(src_rel: str, out_rel: str):
    src_dir = os.path.dirname(src_rel)
    out_dir = os.path.dirname(out_rel)

    def fn(target: str) -> str:
        if re.match(r"^(https?:|mailto:|#)", target):
            return target
        path, _, anchor = target.partition("#")
        repo_rel = os.path.normpath(os.path.join(src_dir, path)).replace("\\", "/")
        if repo_rel == ".":
            repo_rel = ""
        sp = site_path(repo_rel)
        if sp is None:  # code, data, licence: link to GitHub
            kind = "tree" if (ROOT / repo_rel).is_dir() else "blob"
            return f"{REPO_URL}/{kind}/main/{repo_rel}" + (f"#{anchor}" if anchor else "")
        rel = os.path.relpath(sp, out_dir or ".").replace("\\", "/")
        return rel + (f"#{anchor}" if anchor else "")

    return fn


def areas() -> list[dict]:
    result = []
    for d in sorted(p for p in ROOT.iterdir() if p.is_dir() and re.match(r"^\d\d-", p.name)):
        readme = (d / "README.md").read_text(encoding="utf-8") if (d / "README.md").exists() else ""
        m = re.search(r"^#\s+(.*)$", readme, re.M)
        title = m.group(1) if m else d.name
        short = title.split("·", 1)[-1].strip()
        num = d.name[:2]
        intro = ""
        for para in readme.split("\n\n")[1:]:
            para = para.strip()
            if para and not para.startswith(("|", "#", "*", ">")):
                intro = para
                break
        items = re.findall(r"^\|\s*\[([^\]]+)\]\(([^)]+)\)\s*\|\s*(.+?)\s*\|", readme, re.M)
        result.append({"dir": d.name, "num": num, "short": short, "intro": intro, "items": items})
    return result


# --------------------------------------------------------------------------- templates

def page(title: str, body: str, out_rel: str, area_list: list[dict], current: str = "",
         toc: list[tuple[str, str]] | None = None, source: str = "", crumbs: str = "",
         prev_next: str = "", description: str = "") -> str:
    depth = out_rel.count("/")
    up = "../" * depth
    nav = "".join(
        f'<a href="{up}{a["dir"]}/index.html"{" aria-current=\"page\"" if a["dir"] == current else ""}>'
        f'<span class="n">{a["num"]}</span>{html.escape(a["short"])}</a>' for a in area_list)
    toc_html = ""
    if toc and len(toc) > 2:
        toc_html = '<aside class="toc"><div class="toc-h">On this page</div>' + "".join(
            f'<a href="#{i}">{html.escape(t)}</a>' for i, t in toc) + "</aside>"
    src = (f'<a class="src" href="{REPO_URL}/blob/main/{source}">View source on GitHub ↗</a>'
           if source else "")
    desc = html.escape(description or "Program & delivery management portfolio: frameworks, templates and playbooks.")
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)}</title>
<meta name="description" content="{desc}">
<link rel="stylesheet" href="{up}assets/site.css">
<script>try{{var t=localStorage.getItem('cs-theme');if(t)document.documentElement.setAttribute('data-theme',t)}}catch(e){{}}</script>
</head>
<body>
<div class="topbar"><div class="wrap">
  <a class="brand" href="{up}index.html">TPM_work</a>
  <a class="toplink" href="{up}case-study.html">Case study</a>
  <a class="toplink" href="{REPO_URL}">GitHub ↗</a>
  <button class="theme-btn" id="themeBtn" type="button" aria-label="Toggle colour theme">◐</button>
</div></div>
<div class="wrap layout">
  <nav class="sidenav" aria-label="Skill areas"><div class="toc-h">Skill areas</div>{nav}</nav>
  <main class="doc">
    {crumbs}
    <article>{body}</article>
    {prev_next}
    <div class="docfoot">{src}<span>All examples are fictional · <a href="{up}COMPLIANCE.html">Compliance</a></span></div>
  </main>
  {toc_html}
</div>
<script src="{up}assets/site.js"></script>
</body>
</html>
"""


def home(area_list: list[dict]) -> str:
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    skills = re.search(r"## Skills matrix\n\n(.*?)\n\n", readme, re.S)
    rows = []
    if skills:
        for line in skills.group(1).splitlines()[2:]:
            c = [x.strip() for x in line.strip().strip("|").split("|")]
            if len(c) == 3:
                filled = c[2].count("●")
                bar = f'<span class="meter" role="img" aria-label="{filled} of 5"><i style="width:{filled * 20}%"></i></span>'
                rows.append(f"<tr><td><strong>{html.escape(c[0])}</strong></td><td>{html.escape(c[1])}</td><td>{bar}</td></tr>")
    cards = []
    for a in area_list:
        link_fn = make_link_fn(f'{a["dir"]}/README.md', "index.html")
        plain = Renderer(lambda t: t)
        links = "".join(
            f'<li><a href="{html.escape(link_fn(href))}">'
            f'{html.escape(re.sub(r"[-_]", " ", re.sub(r"[`/]|[.]md$|[.]html$", "", label)).strip().capitalize())}</a>'
            f'<span>{plain.inline(re.sub(r"[(][^)]*[)]", "", desc).replace("[", "").replace("]", ""))}</span></li>'
            for label, href, desc in a["items"])
        cards.append(f"""<section class="area-card">
  <a class="area-h" href="{a['dir']}/index.html"><span class="n">{a['num']}</span>{html.escape(a['short'])} →</a>
  <p>{Renderer(lambda t: t).inline(a['intro'])}</p>
  <ul>{links}</ul>
</section>""")
    body = f"""
<header class="hero">
  <span class="badge">Technical Program Manager · Program Manager · Release Manager</span>
  <h1>Program &amp; Delivery Management Portfolio</h1>
  <p class="lede">Frameworks, templates, playbooks and automation I use to run software delivery programs: governance, release management, quality service levels, stakeholder communication and data-driven reporting. Every example uses a fictional company and invented data.</p>
  <div class="cta">
    <a class="btn primary" href="case-study.html">See it applied: the end-to-end case study →</a>
    <a class="btn" href="{REPO_URL}">Browse on GitHub ↗</a>
  </div>
</header>
<h2 id="areas">Skill areas</h2>
<div class="areas">{''.join(cards)}</div>
<h2 id="skills">Skills matrix</h2>
<div class="table-wrap"><table><thead><tr><th>Skill area</th><th>Evidence in this portfolio</th><th>Depth</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
<h2 id="principles">Operating principles</h2>
<ol class="principles">
  <li><strong>Criteria over opinion.</strong> "Ready" means the stated criteria are met.</li>
  <li><strong>Surface risk early.</strong> Warn before breaches, and escalate before there are surprises.</li>
  <li><strong>Automate the gathering, not the judgment.</strong> Scripts collect; people decide.</li>
  <li><strong>One source of truth.</strong> Reports come from the tracker, never copied by hand.</li>
  <li><strong>Trends over snapshots.</strong> Direction tells you more than a single value.</li>
</ol>
"""
    return page("TPM Portfolio · Program & Delivery Management", body, "index.html", area_list,
                toc=[("areas", "Skill areas"), ("skills", "Skills matrix"), ("principles", "Operating principles")],
                description="Technical program management portfolio: governance, release management, quality, reporting and automation frameworks with a fictional end-to-end case study.")


# --------------------------------------------------------------------------- build

def build() -> None:
    area_list = areas()
    area_by_dir = {a["dir"]: a for a in area_list}
    written = []

    for f in md_files():
        src_rel = f.relative_to(ROOT).as_posix()
        if src_rel == "README.md":
            continue  # replaced by the custom home page
        out_rel = site_path(src_rel)
        r = Renderer(make_link_fn(src_rel, out_rel))
        body = r.render(f.read_text(encoding="utf-8"))
        top = src_rel.split("/")[0]
        area = area_by_dir.get(top)
        depth = out_rel.count("/")
        up = "../" * depth
        crumbs = f'<div class="crumbs"><a href="{up}index.html">Home</a>'
        prev_next = ""
        if area:
            crumbs += f' / <a href="{up}{area["dir"]}/index.html">{html.escape(area["short"])}</a>'
            siblings = [h for _, h, _ in area["items"] if h.endswith(".md") and "/" not in h]
            name = f.name
            if name in siblings:
                i = siblings.index(name)
                prev_l = f'<a href="{siblings[i - 1][:-3]}.html">← {siblings[i - 1][:-3].replace("-", " ")}</a>' if i > 0 else "<span></span>"
                next_l = f'<a href="{siblings[i + 1][:-3]}.html">{siblings[i + 1][:-3].replace("-", " ")} →</a>' if i + 1 < len(siblings) else "<span></span>"
                prev_next = f'<div class="prevnext">{prev_l}{next_l}</div>'
        crumbs += "</div>"
        title = (r.title or f.stem) + " · TPM Portfolio"
        out = DOCS / out_rel
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page(title, body, out_rel, area_list, current=top, toc=r.toc, source=src_rel,
                            crumbs=crumbs, prev_next=prev_next), encoding="utf-8")
        written.append(out_rel)

    (DOCS / "index.html").write_text(home(area_list), encoding="utf-8")
    (DOCS / ".nojekyll").write_text("", encoding="utf-8")
    written.append("index.html")
    print(f"Built {len(written)} pages into docs/")


if __name__ == "__main__":
    build()
