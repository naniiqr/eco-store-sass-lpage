import json, random

def wid():
    return ''.join(random.choices('0123456789abcdef', k=7))

def W(widgetType, settings):
    return {"id": wid(), "elType": "widget", "settings": settings, "elements": [], "widgetType": widgetType}

def C(settings, elements, isInner=True):
    return {"id": wid(), "elType": "container", "settings": settings, "elements": elements, "isInner": isInner}

RED = "#E14D5A"
GREEN = "#4E8C3F"
BLACKBG = "#0B0B0B"
TEXT_DARK = "#1E2A22"
WHITE = "#FFFFFF"
GRAY = "#B9BFB9"

def pad(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}

def heading(title, size="p", align="left", color=TEXT_DARK, font_size=14, weight="500"):
    return W("heading", {
        "title": title, "header_size": size, "align": align, "title_color": color,
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": font_size, "sizes": []},
        "typography_font_weight": weight,
    })

def text(content, color=GRAY, font_size=13, align="left"):
    return W("text-editor", {
        "editor": f"<p>{content}</p>", "text_color": color, "align": align,
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": font_size, "sizes": []},
    })

def button(txt, bg=RED, color=WHITE):
    return W("button", {
        "text": txt, "button_text_color": color, "background_color": bg,
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
        "size": "sm",
    })

def icon(name, color=WHITE, size=16, link=""):
    s = {
        "selected_icon": {"value": f"fab fa-{name}", "library": "fa-brands"},
        "primary_color": color,
        "size": {"unit": "px", "size": size, "sizes": []},
    }
    if link:
        s["link"] = {"url": link, "is_external": "true"}
    return W("icon", s)

def row(settings=None, elements=None, gap="16", justify="flex-start", align="center", wrap="wrap"):
    base = {
        "content_width": "full", "flex_direction": "row", "flex_wrap": wrap,
        "flex_gap": {"column": gap, "row": gap, "unit": "px", "isLinked": True},
        "flex_justify_content": justify, "flex_align_items": align,
    }
    if settings:
        base.update(settings)
    return C(base, elements or [])

def col(settings=None, elements=None, gap="8", align="flex-start"):
    base = {
        "content_width": "full", "flex_direction": "column",
        "flex_gap": {"column": gap, "row": gap, "unit": "px", "isLinked": True},
        "flex_align_items": align,
    }
    if settings:
        base.update(settings)
    return C(base, elements or [])

def top_section(settings=None, elements=None):
    base = {"content_width": "boxed", "flex_direction": "column", "width": {"unit": "%", "size": 100}}
    if settings:
        base.update(settings)
    return C(base, elements or [], isInner=False)

def dump(page, out_path):
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(page, f, ensure_ascii=False, indent=2)
    with open(out_path, encoding="utf-8") as f:
        json.load(f)
    print("written + validated:", out_path)


# =========================================================
# HEADER
# =========================================================
logo = W("theme-site-logo", {"width": {"unit": "px", "size": 140, "sizes": []}, "align": "left"})

nav_menu = W("nav-menu", {
    "menu": "",
    "layout": "horizontal",
    "pointer": "underline",
    "menu_typography_typography": "custom",
    "menu_typography_font_size": {"unit": "px", "size": 15, "sizes": []},
    "menu_typography_font_weight": "500",
    "menu_color_text": TEXT_DARK,
})

lang_switch = text('<a href="#">CA</a> <a href="#">ES</a> <a href="#">FR</a> <a href="#">ENG</a>',
                    color=TEXT_DARK, font_size=13)

header_right = row(
    elements=[lang_switch, button("DEMANA PRESSUPOST", bg=RED, color=WHITE)],
    gap="16", justify="flex-end", wrap="nowrap",
)

header_bar = row(
    settings={"width": {"unit": "%", "size": 100}},
    elements=[logo, nav_menu, header_right],
    gap="24", justify="space-between", wrap="nowrap",
)

header_root = top_section(
    settings={
        "background_background": "classic",
        "background_color": WHITE,
        "padding": pad(16, 40, 16, 40),
        "sticky": "top",
        "sticky_offset": {"unit": "px", "size": 0, "sizes": []},
        "z_index": 999,
        "border_border": "solid",
        "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "1", "left": "0", "isLinked": False},
        "border_color": "#EDEDED",
    },
    elements=[header_bar],
)

header_page = {
    "content": [header_root],
    "page_settings": [],
    "version": "0.4",
    "title": "Header - New Tree",
    "type": "header",
}
dump(header_page, "/home/user/eco-store-sass-lpage/elementor-templates/header.json")


# =========================================================
# FOOTER
# =========================================================
footer_logo = W("theme-site-logo", {"width": {"unit": "px", "size": 120, "sizes": []}, "align": "left"})

social_row = row(
    elements=[
        icon("instagram", color=WHITE, size=18, link="https://instagram.com/"),
        icon("facebook", color=WHITE, size=18, link="https://facebook.com/"),
    ],
    gap="16", justify="flex-start", wrap="nowrap",
)

legal_links = text(
    '<a href="#" style="color:%s">Avís legal</a> &nbsp;|&nbsp; '
    '<a href="#" style="color:%s">Política de privacitat</a> &nbsp;|&nbsp; '
    '<a href="#" style="color:%s">Cookies</a>' % (GRAY, GRAY, GRAY),
    color=GRAY, font_size=13,
)

location = row(
    elements=[
        W("icon", {"selected_icon": {"value": "fas fa-map-marker-alt", "library": "fa-solid"},
                   "primary_color": GRAY, "size": {"unit": "px", "size": 14, "sizes": []}}),
        text("Figueres (Girona)", color=GRAY, font_size=13),
    ],
    gap="6", justify="flex-start", wrap="nowrap",
)

footer_bar = row(
    settings={"width": {"unit": "%", "size": 100}},
    elements=[footer_logo, social_row, legal_links, location],
    gap="20", justify="space-between", align="center", wrap="wrap",
)

footer_root = top_section(
    settings={
        "background_background": "classic",
        "background_color": BLACKBG,
        "padding": pad(28, 40, 28, 40),
    },
    elements=[footer_bar],
)

footer_page = {
    "content": [footer_root],
    "page_settings": [],
    "version": "0.4",
    "title": "Footer - New Tree",
    "type": "footer",
}
dump(footer_page, "/home/user/eco-store-sass-lpage/elementor-templates/footer.json")
