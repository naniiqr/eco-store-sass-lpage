"""Genera una vista previa HTML de cada plantilla JSON de ../importar/ (aproximación de cómo
las dibujará Elementor). Uso: python3 preview.py   -> ../preview/index.html + una página por JSON.
"""
import json, os, glob, html as H

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
SRC = os.path.join(ROOT, "importar")
OUT = os.path.join(ROOT, "preview")
LOGO = "https://newtree.cat/wp-content/uploads/2020/04/Logo-300x261.png"
MENU = ["Inici", "Empresa", "Jardineria", "Galeria", "Plantes exemplars", "Situació i contacte"]
HSIZE = {"h1": 40, "h2": 32, "h3": 26, "h4": 20, "h5": 18, "h6": 16, "p": 16}


def px(d):
    if not isinstance(d, dict) or d.get("size") in (None, ""):
        return None
    return f"{d['size']}{d.get('unit', 'px')}"


def box(d):
    if not isinstance(d, dict):
        return None
    u = d.get("unit", "px")
    return " ".join(f"{d.get(k, 0) or 0}{u}" for k in ("top", "right", "bottom", "left"))


def container(c, top=False):
    s = c["settings"]
    st = ["display:flex", "box-sizing:border-box", "min-width:0", "position:relative"]
    direction = s.get("flex_direction", "column")
    st.append(f"flex-direction:{direction}")
    cls = "c row" if direction.startswith("row") else "c"
    st.append(f"flex-wrap:{s.get('flex_wrap', 'nowrap')}")
    g = s.get("flex_gap") or {"row": 20, "column": 20, "unit": "px"}  # 20px: gap por defecto de Elementor
    if g:
        st.append(f"gap:{g.get('row', 0)}{g.get('unit', 'px')} {g.get('column', 0)}{g.get('unit', 'px')}")
    if s.get("flex_justify_content"):
        st.append(f"justify-content:{s['flex_justify_content']}")
    if s.get("flex_align_items"):
        st.append(f"align-items:{s['flex_align_items']}")
    w = px(s.get("width"))
    st.append(f"width:{w or '100%'}")
    if s.get("padding"):
        st.append(f"padding:{box(s['padding'])}")
    bg = []
    if s.get("background_overlay_color"):
        oc = s["background_overlay_color"]
        bg.append(f"linear-gradient({oc},{oc})")
    img = (s.get("background_image") or {}).get("url")
    if img:
        bg.append(f"url('{img}')")
    if bg:
        st.append(f"background-image:{','.join(bg)};background-size:cover;background-position:center")
    if s.get("background_color"):
        st.append(f"background-color:{s['background_color']}")
    if px(s.get("min_height")):
        st.append(f"min-height:{px(s['min_height'])}")
    if px(s.get("height")):
        st.append(f"height:{px(s['height'])}")
    if s.get("border_border"):
        st.append(f"border:solid {s.get('border_color', '#ccc')};border-width:{box(s.get('border_width')) or '1px'}")
    if s.get("border_radius"):
        r = s["border_radius"]
        st.append("border-radius:" + (f"{r['top']}{r['unit']}" if r.get("isLinked") else box(r)))
    if s.get("_position") == "absolute":
        st = [x for x in st if not x.startswith(("position", "width"))]
        st += ["position:absolute", f"top:{px(s.get('_offset_y')) or '0'}", "right:0", "z-index:2"]
    if s.get("z_index") not in (None, ""):
        st.append(f"z-index:{s['z_index']}")
    inner = "".join(node(e) for e in c.get("elements", []))
    if s.get("content_width") == "boxed" and top:
        # sección a ancho completo con contenido centrado (1140px)
        outer = [x for x in st if not x.startswith(("flex-", "gap", "justify", "align", "display", "padding"))]
        pad = f"padding:{box(s['padding'])};" if s.get("padding") else ""
        inner_st = [x for x in st if x.startswith(("flex-", "gap", "justify", "align", "display"))]
        return (f'<div class="c" style="{";".join(outer)};{pad}"><div class="c in" '
                f'style="{";".join(inner_st)};max-width:1140px;margin:0 auto;width:100%;box-sizing:border-box">{inner}</div></div>')
    return f'<div class="{cls}" style="{";".join(st)}">{inner}</div>'


def icon_html(v, color, size=None):
    sty = f"color:{color};" if color else ""
    if size:
        sty += f"font-size:{size}px;"
    return f'<i class="{H.escape(v)}" style="{sty}"></i>'


def widget(w):
    t, s = w["widgetType"], w["settings"]
    if t == "heading":
        tag = s.get("header_size", "h2")
        tag = "div" if tag == "p" else tag
        size = (s.get("typography_font_size") or {}).get("size") or HSIZE.get(s.get("header_size", "h2"), 32)
        st = [f"font-size:{size}px", f"color:{s.get('title_color', '#1e2a22')}", "margin:0",
              f"font-weight:{s.get('typography_font_weight', 700)}", f"text-align:{s.get('align', 'left')}", "line-height:1.2"]
        if s.get("typography_font_style"):
            st.append(f"font-style:{s['typography_font_style']}")
        if s.get("letter_spacing"):
            st.append(f"letter-spacing:{px(s['letter_spacing'])}")
        return f'<{tag} style="{";".join(st)}">{s.get("title", "")}</{tag}>'
    if t == "text-editor":
        size = (s.get("typography_font_size") or {}).get("size") or 16
        return (f'<div class="te" style="font-size:{size}px;color:{s.get("text_color", "#6b7280")};'
                f'text-align:{s.get("align", "left")};line-height:1.65">{s.get("editor", "")}</div>')
    if t == "button":
        bg, col = s.get("background_color", "#4E8C3F"), s.get("button_text_color", "#fff")
        r = s.get("border_radius") or {}
        st = [f"background:{bg}", f"color:{col}", f"border-radius:{r.get('top', 6)}px", "padding:14px 26px",
              "font-weight:600", "text-decoration:none", "display:inline-flex", "gap:10px", "align-items:center",
              "font-size:14px", "letter-spacing:.5px", "white-space:nowrap"]
        if s.get("border_border"):
            st.append(f"border:{(s.get('border_width') or {}).get('top', 1)}px solid {s.get('border_color', col)}")
        href = (s.get("link") or {}).get("url", "#")
        ic = ' <i class="fas fa-arrow-right"></i>' if s.get("icon") else ""
        return f'<a href="{H.escape(href)}" style="{";".join(st)}">{H.escape(s.get("text", ""))}{ic}</a>'
    if t == "icon-box":
        ic = icon_html((s.get("selected_icon") or {}).get("value", "fas fa-leaf"), s.get("icon_color", "#4E8C3F"), 28)
        title = f'<div style="font-weight:700;font-size:18px;color:{s.get("title_color", "#1e2a22")};line-height:1.3">{H.escape(s.get("title_text", ""))}</div>'
        desc = (f'<div style="font-size:14px;color:{s.get("description_color", "#6b7280")};margin-top:4px;line-height:1.5">'
                f'{H.escape(s.get("description_text", ""))}</div>') if s.get("description_text") else ""
        d = "row" if s.get("position") == "left" else "column"
        return (f'<div style="display:flex;flex-direction:{d};gap:14px;align-items:flex-start">'
                f'<div style="flex:none">{ic}</div><div>{title}{desc}</div></div>')
    if t == "icon":
        return icon_html((s.get("selected_icon") or {}).get("value", "fas fa-leaf"), s.get("primary_color", "#fff"),
                         (s.get("size") or {}).get("size", 18))
    if t == "image":
        u = (s.get("image") or {}).get("url", "")
        return f'<img src="{H.escape(u)}" alt="{H.escape(s.get("alt", ""))}" style="width:100%;display:block;border-radius:6px;object-fit:cover">'
    if t == "form":
        out = '<form onsubmit="return false" style="display:flex;flex-direction:column;gap:14px;width:100%">'
        for f in s.get("form_fields", []):
            lab = H.escape(f.get("field_label", ""))
            st = "padding:12px 14px;border:1px solid #d1d5db;border-radius:6px;font:inherit;width:100%;box-sizing:border-box"
            if f.get("field_type") == "textarea":
                out += f'<label style="font-weight:600;font-size:14px">{lab}<textarea rows="5" style="{st}"></textarea></label>'
            else:
                out += f'<label style="font-weight:600;font-size:14px">{lab}<input type="{f.get("field_type", "text")}" style="{st}"></label>'
        out += (f'<button style="background:{s.get("button_background_color", "#4E8C3F")};color:#fff;border:0;border-radius:6px;'
                f'padding:14px;font:600 14px Nunito,sans-serif;cursor:pointer">{H.escape(s.get("button_text", "Enviar"))}</button></form>')
        return out
    if t == "google_maps":
        addr = H.escape(s.get("address", ""), quote=True).replace(" ", "+")
        h = (s.get("height") or {}).get("size", 380)
        return (f'<iframe src="https://maps.google.com/maps?q={addr}&z=13&output=embed" '
                f'style="width:100%;height:{h}px;border:0;border-radius:6px" loading="lazy"></iframe>')
    if t == "theme-site-logo":
        return f'<img src="{LOGO}" alt="New Tree" style="width:{(s.get("width") or {}).get("size", 120)}px">'
    if t == "nav-menu":
        return ('<nav style="display:flex;gap:22px;flex-wrap:wrap">' +
                "".join(f'<a href="#" style="color:{s.get("menu_color_text", "#1e2a22")};text-decoration:none;font-weight:600;font-size:15px">{m}</a>' for m in MENU) +
                '</nav>')
    return f'<div style="border:1px dashed #999;padding:8px;font-size:12px">[{t}]</div>'


def node(n):
    if n.get("elType") == "container":
        return container(n, top=not n.get("isInner", True))
    return f'<div class="w">{widget(n)}</div>'


def render(path):
    d = json.load(open(path, encoding="utf-8"))
    return "".join(node(c) for c in d["content"]), d.get("title", "")


CSS = """
*{box-sizing:border-box}body{margin:0;background:#e9ece8;font-family:'Nunito',sans-serif;color:#1e2a22}
.bar{position:sticky;top:0;z-index:99;background:#0b0b0b;color:#fff;padding:10px 16px;display:flex;gap:12px;align-items:center;flex-wrap:wrap;font-size:14px}
.bar select,.bar button{font:inherit;padding:6px 10px;border-radius:6px;border:1px solid #444;background:#1c1c1c;color:#fff;cursor:pointer}
.bar button.on{background:#4E8C3F;border-color:#4E8C3F}.bar .sp{flex:1}.bar small{opacity:.7}
#frame{margin:0 auto;background:#fff;container-type:inline-size;container-name:pv;transition:max-width .2s;max-width:100%}
.w{flex:0 1 auto;min-width:0}.in>.w,.c>.w{max-width:100%}.te p{margin:0 0 .6em}.te p:last-child{margin:0}
a{cursor:pointer}
@container pv (max-width:1024px){.c{padding-left:min(var(--pl,40px),24px)}}
@container pv (max-width:767px){.c{width:100%!important}.c.row{flex-direction:column!important;align-items:stretch!important}
 .c.row>.w a{width:100%}h1{font-size:32px!important}h2{font-size:26px!important}.c[style*="min-height"]{min-height:0!important}
 .c{padding-left:20px!important;padding-right:20px!important}}
"""


def page_html(name, body, title, pages):
    opts = "".join(f'<option value="{p}.html"{" selected" if p == name else ""}>{lab}</option>' for p, lab in pages)
    return f"""<!doctype html><html lang="ca"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Previsualització – {H.escape(title)}</title>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Nunito:wght@400;600;700;800&display=swap">
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.15.4/css/all.min.css">
<style>{CSS}</style></head><body>
<div class="bar"><strong>Vista prèvia</strong><select onchange="location=this.value">{opts}</select>
<button data-w="100%" class="on">Escriptori</button><button data-w="820px">Tauleta</button><button data-w="390px">Mòbil</button>
<span class="sp"></span><small>Aproximació del JSON; Elementor pot diferir lleugerament.</small></div>
<div id="frame">{body}</div>
<script>document.querySelectorAll('.bar button').forEach(b=>b.onclick=()=>{{document.getElementById('frame').style.maxWidth=b.dataset.w;
document.querySelectorAll('.bar button').forEach(x=>x.classList.toggle('on',x===b))}})</script></body></html>"""


def main():
    os.makedirs(OUT, exist_ok=True)
    for old in glob.glob(os.path.join(OUT, "*.html")):
        os.remove(old)
    header, _ = render(os.path.join(SRC, "00-header.json"))
    footer, _ = render(os.path.join(SRC, "00-footer.json"))
    files = [f for f in sorted(glob.glob(os.path.join(SRC, "*.json"))) if not os.path.basename(f).startswith("00-")]
    pages = []
    for f in files:
        stem = os.path.splitext(os.path.basename(f))[0]
        pages.append((stem, stem[3:].replace("-", " ").capitalize()))
    for f, (stem, _) in zip(files, pages):
        body, title = render(f)
        open(os.path.join(OUT, stem + ".html"), "w", encoding="utf-8").write(
            page_html(stem, header + body + footer, title, pages))
    idx = "".join(f'<li><a href="{s}.html">{l}</a></li>' for s, l in pages)
    open(os.path.join(OUT, "index.html"), "w", encoding="utf-8").write(
        f"""<!doctype html><html lang="ca"><meta charset="utf-8"><title>Previsualització New Tree</title>
<body style="font-family:Nunito,system-ui,sans-serif;max-width:640px;margin:40px auto;padding:0 16px">
<h1>Previsualització de les plantilles</h1><p>Obre cada pàgina per veure com queda el JSON abans d'importar-lo a Elementor.</p><ol>{idx}</ol></body></html>""")
    print(f"{len(pages)} pàgines a preview/")


main()
