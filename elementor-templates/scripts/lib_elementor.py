import json, random

def wid():
    return ''.join(random.choices('0123456789abcdef', k=7))

def W(widgetType, settings):
    return {"id": wid(), "elType": "widget", "settings": settings, "elements": [], "widgetType": widgetType}

def C(settings, elements, isInner=True):
    return {"id": wid(), "elType": "container", "settings": settings, "elements": elements, "isInner": isInner}

RED = "#E14D5A"
GREEN = "#4E8C3F"
DARKGREEN = "#122318"
BLACKBG = "#0B0B0B"
TEXT_DARK = "#1E2A22"
TEXT_GRAY = "#6B7280"
WHITE = "#FFFFFF"
LIGHTGRAY_BG = "#F6F7F5"

def ph(text, w=800, h=600, bg="e8e4da", fg="4e8c3f"):
    q = text.replace(' ', '+')
    return {"url": f"https://placehold.co/{w}x{h}/{bg}/{fg}?text={q}", "id": ""}

def heading(title, size="h2", align="left", color=TEXT_DARK, font_size=None, weight="700", extra=None):
    s = {"title": title, "header_size": size, "align": align, "title_color": color}
    if font_size:
        s["typography_typography"] = "custom"
        s["typography_font_size"] = {"unit": "px", "size": font_size, "sizes": []}
        s["typography_font_weight"] = weight
    if extra:
        s.update(extra)
    return W("heading", s)

def text(content, color=TEXT_GRAY, font_size=16, align="left"):
    return W("text-editor", {
        "editor": f"<p>{content}</p>", "text_color": color, "align": align,
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": font_size, "sizes": []},
    })

def button(txt, bg=GREEN, color=WHITE, border=None, link=None):
    s = {
        "text": txt, "button_text_color": color, "background_color": bg,
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
        "size": "md", "icon": {"value": "fas fa-arrow-right", "library": "fa-solid"}, "icon_align": "right",
    }
    if border:
        s["background_color"] = "transparent"
        s["border_border"] = "solid"
        s["border_width"] = {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True}
        s["border_color"] = border
        s["button_text_color"] = border
    if link:
        s["link"] = {"url": link, "is_external": "", "nofollow": "", "custom_attributes": ""}
    return W("button", s)

def icon_box(icon, title, desc, icon_color=GREEN, title_color=TEXT_DARK, desc_color=TEXT_GRAY, position="top"):
    return W("icon-box", {
        "selected_icon": {"value": f"fas fa-{icon}", "library": "fa-solid"},
        "title_text": title, "description_text": desc, "position": position,
        "title_size": "h4", "icon_color": icon_color, "title_color": title_color, "description_color": desc_color,
    })

def icon(name, color=WHITE, size=18):
    return W("icon", {
        "selected_icon": {"value": f"fas fa-{name}", "library": "fa-solid"},
        "primary_color": color, "size": {"unit": "px", "size": size, "sizes": []},
    })

def image(img, alt=""):
    return W("image", {"image": img, "image_size": "large", "alt": alt})

def row(settings=None, elements=None, gap="20", justify="flex-start", align="center", wrap="wrap"):
    base = {
        "content_width": "full", "flex_direction": "row", "flex_wrap": wrap,
        "flex_gap": {"column": gap, "row": gap, "unit": "px", "isLinked": True},
        "flex_justify_content": justify, "flex_align_items": align,
    }
    if settings:
        base.update(settings)
    return C(base, elements or [])

def col(settings=None, elements=None, gap="16", align="flex-start"):
    base = {
        "content_width": "full", "flex_direction": "column",
        "flex_gap": {"column": gap, "row": gap, "unit": "px", "isLinked": True},
        "flex_align_items": align,
    }
    if settings:
        base.update(settings)
    return C(base, elements or [])

def section(settings=None, elements=None, boxed=True):
    base = {"content_width": "boxed" if boxed else "full", "flex_direction": "column",
            "width": {"unit": "%", "size": 100}}
    if settings:
        base.update(settings)
    return C(base, elements or [], isInner=False)

def pad(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


