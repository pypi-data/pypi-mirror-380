import re, json, webbrowser, http.client
from pathlib import Path
from praxshell.cli.utils.display import print_info, print_success, print_error

HTML_DIR = Path(__file__).resolve().parents[2] / "html"
HTML_DIR.mkdir(exist_ok=True)
OUT_FILE = HTML_DIR / "__render.html"

TEMPLATE = """<!DOCTYPE html>
<html>
<head>
  <meta charset="utf-8">
  <title>{title}</title>
  <link rel="stylesheet" href="https://pyscript.net/latest/pyscript.css" />
  <script defer src="https://pyscript.net/latest/pyscript.js"></script>
  <script src="plotly.min.js"></script>
  <style>
    body {{
      font-family: sans-serif;
      background: var(--bg);
      color: var(--fg);
      margin: 0;
      padding: 2rem;
      display: flex;
      justify-content: center;
    }}
    main {{
      background: var(--card-bg);
      border-radius: 16px;
      box-shadow: 0 4px 12px rgba(0,0,0,0.1);
      padding: 2rem;
      max-width: 900px;
      width: 100%;
    }}
    h1, h2, h3 {{
      margin-top: 1.5rem;
      margin-bottom: 0.5rem;
      font-weight: 600;
    }}
    p, li {{
      line-height: 1.6;
    }}
    pre {{
      background: var(--code-bg);
      padding: 1rem;
      border-radius: 12px;
      overflow-x: auto;
    }}
    code {{
      background: var(--code-bg);
      padding: 0.1rem 0.3rem;
      border-radius: 4px;
    }}
    ul, ol {{
      margin: 0.5rem 0 1rem 1.5rem;
    }}
    hr {{
      border: none;
      border-top: 2px solid var(--fg);
      margin: 1.5rem 0;
    }}
    div[id^="plot"] {{
      margin: 1.5rem 0;
      border-radius: 12px;
      overflow: hidden;
      box-shadow: 0 2px 8px rgba(0,0,0,0.08);
    }}
    .toggle-btn {{
      position: fixed;
      top: 1rem;
      right: 1rem;
      padding: 0.5rem 1rem;
      border: none;
      border-radius: 8px;
      cursor: pointer;
      background: var(--fg);
      color: var(--bg);
    }}
    :root {{
      --bg: #fffbea;
      --fg: #222;
      --card-bg: #ffffffcc;
      --code-bg: #fdf6e3;
    }}
    body.dark {{
      --bg: #1e1e1e;
      --fg: #ddd;
      --card-bg: #2a2a2acc;
      --code-bg: #333;
    }}
  </style>
</head>
<body>
<button class="toggle-btn" onclick="toggleMode()">Toggle Theme</button>
<main>
{content}
</main>
<script>
function toggleMode() {{
  document.body.classList.toggle("dark");
  let isDark = document.body.classList.contains("dark");
  let bg = isDark ? "#1e1e1e" : "#fffbea";
  let fg = isDark ? "#ddd" : "#222";
  document.querySelectorAll("div[id^='plot']").forEach(div => {{
    Plotly.relayout(div.id, {{
      paper_bgcolor: bg,
      plot_bgcolor: bg,
      font: {{ color: fg }}
    }});
  }});
}}
</script>
</body>
</html>
"""

def ensure_plotly():
    """Download plotly.min.js into html/ if missing."""
    js_path = HTML_DIR / "plotly.min.js"
    if js_path.exists():
        return js_path
    print_info("Downloading plotly.min.js ...")
    conn = http.client.HTTPSConnection("cdn.plot.ly")
    conn.request("GET", "/plotly-latest.min.js")
    resp = conn.getresponse()
    if resp.status != 200:
        print_error(f"Failed to fetch plotly.js: {resp.status}")
        return None
    data = resp.read()
    with open(js_path, "wb") as f:
        f.write(data)
    conn.close()
    print_success(f" Saved {js_path}")
    return js_path

def inline_format(text: str) -> str:
    text = re.sub(r"`([^`]+)`", r"<code>\1</code>", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"<a href='\2' target='_blank'>\1</a>", text)
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    return text

def parse_bullet(line: str):
    m = re.match(r"^(\s*)- (.+)", line)
    if not m: return None
    spaces, text = m.groups()
    return len(spaces) // 2, text

def parse_numbered(line: str):
    m = re.match(r"^\s*\d+\.\s+(.+)", line)
    return m.group(1) if m else None

def md_to_html(md_text: str) -> str:
    html, buffer = [], []
    in_code_block, code_type = False, None
    in_fenced_code, fenced_lang = False, None
    plot_counter = 0
    indent_stack = []
    in_ol = False

    for line in md_text.splitlines():
        # fenced code block ('''lang)
        if line.startswith("'''"):
            if not in_fenced_code:
                in_fenced_code, fenced_lang, buffer = True, line.strip("'").strip(), []
            else:
                code = "\n".join(buffer)
                cls = f" class='lang-{fenced_lang}'" if fenced_lang else ""
                html.append(f"<pre><code{cls}>{code}</code></pre>")
                in_fenced_code, fenced_lang = False, None
            continue
        if in_fenced_code:
            buffer.append(line)
            continue

        # hr
        if line.strip() == "---":
            html.append("<hr>")
            continue

        # special fences ("""""js_plotly)
        if line.startswith('"""""'):
            if not in_code_block:
                in_code_block, code_type, buffer = True, line.strip('"').strip(), []
            else:
                code = "\n".join(buffer)
                if code_type == "js_plotly":
                    plot_counter += 1
                    div_id = f"plot{plot_counter}"
                    try:
                        plot_data = json.loads(code)
                        plot_data.setdefault("layout", {})
                        plot_data["layout"].setdefault("paper_bgcolor", "#fffbea")
                        plot_data["layout"].setdefault("plot_bgcolor", "#fffbea")
                        plot_data["layout"].setdefault("font", {"color": "#222"})
                        plot_json = json.dumps(plot_data)
                    except Exception:
                        plot_json = code
                    html.append(f"<div id='{div_id}'></div>")
                    html.append(f"<script>Plotly.newPlot('{div_id}', {plot_json});</script>")
                else:
                    html.append(f"<pre><code>{code}</code></pre>")
                in_code_block, code_type = False, None
            continue
        if in_code_block:
            buffer.append(line)
            continue

        # bullets
        bullet = parse_bullet(line)
        if bullet:
            indent, text = bullet
            while len(indent_stack) < indent+1:
                html.append("<ul>")
                indent_stack.append("ul")
            while len(indent_stack) > indent+1:
                html.append("</ul>")
                indent_stack.pop()
            html.append(f"<li>{inline_format(text)}</li>")
            continue

        # numbered
        numtext = parse_numbered(line)
        if numtext:
            while indent_stack:
                html.append("</ul>")
                indent_stack.pop()
            if not in_ol:
                html.append("<ol>")
                in_ol = True
            html.append(f"<li>{inline_format(numtext)}</li>")
            continue

        # close lists
        while indent_stack:
            html.append("</ul>")
            indent_stack.pop()
        if in_ol:
            html.append("</ol>")
            in_ol = False

        # headings / paragraphs
        if line.startswith("### "):
            html.append(f"<h3>{inline_format(line[4:])}</h3>")
        elif line.startswith("## "):
            html.append(f"<h2>{inline_format(line[3:])}</h2>")
        elif line.startswith("# "):
            html.append(f"<h1>{inline_format(line[2:])}</h1>")
        elif line.strip():
            html.append(f"<p>{inline_format(line)}</p>")

    # cleanup
    while indent_stack: html.append("</ul>"); indent_stack.pop()
    if in_ol: html.append("</ol>")

    return "\n".join(html)

def compile_notebook(md_path: Path):
    """Compile one markdown file into html/__render.html"""
    ensure_plotly()

    raw_md = Path(md_path).read_text(encoding="utf-8")
    html_body = md_to_html(md_text=raw_md)
    final_html = TEMPLATE.format(title=Path(md_path).stem, content=html_body)

    OUT_FILE.write_text(final_html, encoding="utf-8")

    print_success(f"Rendered {md_path} -> {OUT_FILE}")
    webbrowser.open(OUT_FILE.as_uri())
