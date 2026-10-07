import json, random

def wid():
    return ''.join(random.choices('0123456789abcdef', k=7))

def W(widgetType, settings):
    return {"id": wid(), "elType": "widget", "settings": settings, "elements": [], "widgetType": widgetType}

def C(settings, elements, isInner=True):
    return {"id": wid(), "elType": "container", "settings": settings, "elements": elements, "isInner": isInner}

# ---- brand tokens (estimated from the PDF - adjust in Elementor Site Settings > Global Colors) ----
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
    s = {
        "title": title,
        "header_size": size,
        "align": align,
        "title_color": color,
    }
    if font_size:
        s["typography_typography"] = "custom"
        s["typography_font_size"] = {"unit": "px", "size": font_size, "sizes": []}
        s["typography_font_weight"] = weight
    if extra:
        s.update(extra)
    return W("heading", s)

def text(content, color=TEXT_GRAY, font_size=16, align="left"):
    return W("text-editor", {
        "editor": f"<p>{content}</p>",
        "text_color": color,
        "align": align,
        "typography_typography": "custom",
        "typography_font_size": {"unit": "px", "size": font_size, "sizes": []},
    })

def button(txt, bg=GREEN, color=WHITE, border=None):
    s = {
        "text": txt,
        "button_text_color": color,
        "background_color": bg,
        "border_radius": {"unit": "px", "top": "6", "right": "6", "bottom": "6", "left": "6", "isLinked": True},
        "size": "md",
        "icon": {"value": "fas fa-arrow-right", "library": "fa-solid"},
        "icon_align": "right",
    }
    if border:
        s["background_color"] = "transparent"
        s["border_border"] = "solid"
        s["border_width"] = {"unit": "px", "top": "1", "right": "1", "bottom": "1", "left": "1", "isLinked": True}
        s["border_color"] = border
        s["button_text_color"] = border
    return W("button", s)

def icon_box(icon, title, desc, icon_color=GREEN, title_color=TEXT_DARK, desc_color=TEXT_GRAY):
    return W("icon-box", {
        "selected_icon": {"value": f"fas fa-{icon}", "library": "fa-solid"},
        "title_text": title,
        "description_text": desc,
        "position": "top",
        "title_size": "h4",
        "icon_color": icon_color,
        "title_color": title_color,
        "description_color": desc_color,
    })

def icon(name, color=WHITE, size=18):
    return W("icon", {
        "selected_icon": {"value": f"fas fa-{name}", "library": "fa-solid"},
        "primary_color": color,
        "size": {"unit": "px", "size": size, "sizes": []},
    })

def image(img, alt=""):
    return W("image", {"image": img, "image_size": "large", "alt": alt})

def row(settings=None, elements=None, gap="20", justify="flex-start", align="center", wrap="wrap"):
    base = {
        "content_width": "full",
        "flex_direction": "row",
        "flex_wrap": wrap,
        "flex_gap": {"column": gap, "row": gap, "unit": "px", "isLinked": True},
        "flex_justify_content": justify,
        "flex_align_items": align,
    }
    if settings:
        base.update(settings)
    return C(base, elements or [])

def col(settings=None, elements=None, gap="16", align="flex-start"):
    base = {
        "content_width": "full",
        "flex_direction": "column",
        "flex_gap": {"column": gap, "row": gap, "unit": "px", "isLinked": True},
        "flex_align_items": align,
    }
    if settings:
        base.update(settings)
    return C(base, elements or [])

def section(settings=None, elements=None, boxed=True):
    base = {
        "content_width": "boxed" if boxed else "full",
        "flex_direction": "column",
        "width": {"unit": "%", "size": 100},
    }
    if settings:
        base.update(settings)
    return C(base, elements or [], isInner=False)

def pad(t, r, b, l):
    return {"unit": "px", "top": str(t), "right": str(r), "bottom": str(b), "left": str(l), "isLinked": False}


# =========================================================
# SECTION A - HERO
# =========================================================
hero_inner = col(
    settings={"width": {"unit": "%", "size": 60}},
    gap="24",
    elements=[
        heading("JARDINERIA I PAISATGISME A L'EMPORDÀ", size="p", color=WHITE, font_size=14,
                extra={"letter_spacing": {"unit": "px", "size": 2, "sizes": []}, "typography_typography": "custom",
                       "typography_font_weight": "600"}),
        heading(
            'Convertim<br>un desert en<br><span style="color:%s">un jardí</span>' % GREEN,
            size="h1", color=WHITE, font_size=52, weight="700"
        ),
        text("Dissenyem, construïm i cuidem espais verds que milloren la teva vida i el nostre entorn.",
             color="#E5E5E5", font_size=18),
        row(elements=[
            button("DEMANA PRESSUPOST", bg=GREEN, color=WHITE),
            button("VEURE PROJECTES", border=WHITE),
        ], gap="16", justify="flex-start"),
    ]
)

hero_decor = col(
    settings={"width": {"unit": "%", "size": 100}, "flex_align_items": "flex-end",
              "_position": "absolute", "_offset_x": {"unit": "px", "size": 0}, "_offset_y": {"unit": "px", "size": 40}},
    align="flex-end",
    elements=[
        heading('Natura<br>Benestar<br>Vida', size="p", align="right", color=WHITE, font_size=20,
                extra={"typography_typography": "custom", "typography_font_style": "italic"}),
    ]
)

hero = section(
    settings={
        "background_background": "classic",
        "background_image": ph("Foto hero jardí", 1600, 900, bg="2f4a3a", fg="ffffff"),
        "background_position": "center center",
        "background_size": "cover",
        "background_overlay_background": "classic",
        "background_overlay_color": "rgba(10,20,15,0.45)",
        "padding": pad(140, 40, 140, 40),
        "min_height": {"unit": "px", "size": 640, "sizes": []},
        "position": "relative",
    },
    elements=[hero_inner, hero_decor],
)

# =========================================================
# SECTION B - FEATURES ICON ROW
# =========================================================
features = [
    ("seedling", "Disseny personalitzat", "Projectes únics i a mida"),
    ("recycle", "Solucions sostenibles", "Respecte pel medi ambient"),
    ("tint", "Estalvi d'aigua", "Espais més eficients"),
    ("award", "Més de 50 anys d'experiència", "Confiança i resultats"),
    ("handshake", "Acompanyament integral", "De la idea a la realitat"),
]

features_row = section(
    settings={
        "background_background": "classic",
        "background_color": WHITE,
        "padding": pad(32, 40, 32, 40),
        "border_border": "solid",
        "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "1", "left": "0", "isLinked": False},
        "border_color": "#E5E7EB",
    },
    elements=[row(
        elements=[icon_box(i, t, d) for i, t, d in features],
        gap="24", justify="space-between", wrap="wrap",
    )],
)

# =========================================================
# SECTION C - SERVICES GRID
# =========================================================
services = [
    ("Disseny de jardins", "Idees que prenen vida"),
    ("Jardineria i plantacions", "Espais plens de color"),
    ("Sistemes de reg", "Eficiència i estalvi d'aigua"),
    ("Tanques i Murs de contenció", "Seguretat i estètica en el teu espai"),
    ("Piscines i exteriors", "Entorns per gaudir"),
    ("Gespa Artificial i Natural", "Verd tot l'any"),
    ("Jardins verticals", "Natura en vertical"),
    ("Murs i elements decoratius", "Pedra, fusta i materials naturals"),
    ("Manteniment de jardins", "Sempre al teu costat"),
    ("Neteja de parcel·les", "Terrenys nets per a nous projectes"),
    ("Podes", "Salut i bellesa per als teus arbres"),
    ("Terres i sustrats", "La base d'un bon jardí"),
]

def service_card(title, subtitle):
    card_content = col(
        settings={"flex_justify_content": "flex-end", "width": {"unit": "%", "size": 100},
                  "flex_align_items": "flex-start"},
        gap="4",
        elements=[
            heading(title, size="h3", color=WHITE, font_size=20, weight="600"),
            text(subtitle, color="#E5E5E5", font_size=14),
        ]
    )
    arrow_wrap = C({
        "content_width": "full", "_position": "absolute",
        "_offset_x": {"unit": "px", "size": -16}, "_offset_y": {"unit": "px", "size": 16},
        "_offset_x_end": {"unit": "px", "size": 16},
    }, [icon("arrow-right", color=WHITE, size=16)])
    return C({
        "content_width": "full",
        "flex_direction": "column",
        "width": {"unit": "%", "size": 31.5},
        "min_height": {"unit": "px", "size": 220, "sizes": []},
        "background_background": "classic",
        "background_image": ph(title, 700, 500, bg="d8d3c4", fg="1e2a22"),
        "background_position": "center center",
        "background_size": "cover",
        "background_overlay_background": "classic",
        "background_overlay_color": "rgba(10,20,15,0.35)",
        "padding": pad(20, 20, 20, 20),
        "position": "relative",
    }, [card_content, arrow_wrap])

services_section = section(
    settings={"background_background": "classic", "background_color": WHITE, "padding": pad(80, 40, 80, 40)},
    elements=[
        heading('Els nostres <span style="color:%s">serveis</span>' % RED, size="h2", font_size=36),
        row(elements=[service_card(t, s) for t, s in services], gap="20", justify="flex-start"),
    ]
)

# =========================================================
# SECTION D - PROJECTS
# =========================================================
projects = [
    ("Jardí residencial", "Figueres"),
    ("Reforma d'exterior", "Peralada"),
    ("Jardí mediterrani", "Empuriabrava"),
    ("Zona de piscina", "Navata"),
]

def project_card(title, place):
    return col(
        settings={"width": {"unit": "%", "size": 23}},
        gap="8",
        elements=[
            image(ph(title, 500, 400, bg="c9d9c2", fg="1e2a22"), alt=title),
            row(elements=[
                col(gap="2", elements=[
                    heading(title, size="h4", font_size=18, weight="600"),
                    text(place, font_size=14),
                ]),
                icon("arrow-right", color=TEXT_DARK, size=14),
            ], justify="space-between", wrap="nowrap"),
        ]
    )

projects_section = section(
    settings={"background_background": "classic", "background_color": LIGHTGRAY_BG, "padding": pad(80, 40, 80, 40)},
    elements=[
        row(elements=[
            heading('Projectes que <span style="color:%s">inspiren</span>' % RED, size="h2", font_size=32),
            text("VEURE TOTS ELS PROJECTES →", font_size=13, color=TEXT_DARK),
        ], justify="space-between", wrap="nowrap"),
        row(elements=[project_card(t, p) for t, p in projects], gap="24", justify="flex-start"),
    ]
)

# =========================================================
# SECTION E - ABOUT / CTA SPLIT (dark green)
# =========================================================
about_left = col(
    settings={"width": {"unit": "%", "size": 45}},
    gap="20",
    elements=[
        heading('A Newtree fem créixer<br><span style="color:%s">les teves Idees</span>' % RED,
                size="h2", color=WHITE, font_size=34, weight="700"),
        text("Podem dissenyar i construir el teu jardí segons les teves necessitats. "
             "New Tree, empresa fundada l'any 1977 dedicada a la jardineria privada i pública.",
             color="#D7DED9", font_size=16),
        button("CONEIX NOSALTRES", border=WHITE),
    ]
)

about_perks = [
    ("leaf", "Jardins més saludables", "per a tu i el teu planeta"),
    ("tree", "Ús de plantes autòctones", "i baix consum hídric"),
    ("tint", "Solucions sostenibles", "i duradores"),
    ("heart", "Passió per la natura", "i el detall"),
]

about_overlay = col(
    settings={
        "background_background": "classic",
        "background_color": "rgba(10,20,15,0.55)",
        "padding": pad(28, 28, 28, 28),
        "_position": "absolute", "_offset_x": {"unit": "px", "size": -20}, "_offset_y": {"unit": "px", "size": 0},
    },
    gap="16",
    elements=[icon_box(i, t, d, icon_color=GREEN, title_color=WHITE, desc_color="#D7DED9") for i, t, d in about_perks]
)

about_right = C({
    "content_width": "full", "width": {"unit": "%", "size": 55}, "position": "relative",
}, [
    image(ph("Foto jardí ampli", 900, 700, bg="2f4a3a", fg="ffffff")),
    about_overlay,
])

about_section = section(
    settings={"background_background": "classic", "background_color": DARKGREEN, "padding": pad(90, 40, 90, 40)},
    elements=[row(elements=[about_left, about_right], gap="40", justify="space-between", align="center", wrap="wrap")],
)

# =========================================================
# SECTION F - BOTTOM CTA BANNER (black)
# =========================================================
contact_items = [
    ("phone", "Truca'ns", "972 50 00 00"),
    ("whatsapp", "WhatsApp", "Envia'ns un missatge"),
    ("envelope", "Escriu-nos", "info@newtree.cat"),
]

banner_left = col(
    settings={"width": {"unit": "%", "size": 50}},
    gap="16",
    elements=[
        heading("Tens un projecte de jardineria?", size="h2", color=WHITE, font_size=30, weight="700"),
        text("Parlem-ne i t'ajudem a fer-lo realitat.", color="#D7DED9", font_size=16),
        button("DEMANA PRESSUPOST", bg=GREEN, color=WHITE),
    ]
)

banner_right = row(
    settings={"width": {"unit": "%", "size": 45}},
    elements=[icon_box(i, t, d, icon_color=GREEN, title_color=WHITE, desc_color="#D7DED9") for i, t, d in contact_items],
    gap="20", justify="flex-start", wrap="wrap",
)

banner_decor = col(
    settings={"_position": "absolute", "_offset_x": {"unit": "px", "size": 0}, "_offset_y": {"unit": "px", "size": -30}},
    align="flex-end",
    elements=[heading('Fem créixer espais,<br>fem créixer persones', size="p", align="right", color=WHITE,
                       font_size=16, extra={"typography_typography": "custom", "typography_font_style": "italic"})],
)

banner_section = section(
    settings={
        "background_background": "classic", "background_color": BLACKBG,
        "padding": pad(70, 40, 70, 40), "position": "relative",
    },
    elements=[
        row(elements=[banner_left, banner_right], justify="space-between", align="center", wrap="wrap"),
        banner_decor,
    ],
)

# =========================================================
# ASSEMBLE PAGE
# =========================================================
page = {
    "content": [hero, features_row, services_section, projects_section, about_section, banner_section],
    "page_settings": [],
    "version": "0.4",
    "title": "Inici (Home) - New Tree",
    "type": "page",
}

out_path = "/home/user/eco-store-sass-lpage/elementor-templates/inici-home.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(page, f, ensure_ascii=False, indent=2)

print("written", out_path)
# sanity check
with open(out_path, encoding="utf-8") as f:
    reloaded = json.load(f)
print("valid json, top-level sections:", len(reloaded["content"]))
