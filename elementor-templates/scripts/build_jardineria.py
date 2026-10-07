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

def button(txt, bg=GREEN, color=WHITE, border=None):
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


# =========================================================
# SECTION A - HERO
# =========================================================
hero_inner = col(
    settings={"width": {"unit": "%", "size": 60}}, gap="24",
    elements=[
        heading("DISSENY DE JARDINS", size="p", color=WHITE, font_size=14,
                extra={"letter_spacing": {"unit": "px", "size": 2, "sizes": []},
                       "typography_typography": "custom", "typography_font_weight": "600"}),
        heading('Dissenyem<br>jardins <span style="color:%s">amb ànima</span>' % GREEN,
                size="h1", color=WHITE, font_size=52, weight="700"),
        text("Espais únics, funcionals i sostenibles que connecten amb la natura i milloren la teva qualitat de vida.",
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
    elements=[heading('Natura<br>Benestar<br>Vida', size="p", align="right", color=WHITE, font_size=20,
                       extra={"typography_typography": "custom", "typography_font_style": "italic"})],
)

hero = section(
    settings={
        "background_background": "classic",
        "background_image": ph("Foto hero disseny jardí", 1600, 900, bg="2f4a3a", fg="ffffff"),
        "background_position": "center center", "background_size": "cover",
        "background_overlay_background": "classic", "background_overlay_color": "rgba(10,20,15,0.45)",
        "padding": pad(140, 40, 140, 40), "min_height": {"unit": "px", "size": 560, "sizes": []},
        "position": "relative",
    },
    elements=[hero_inner, hero_decor],
)

# =========================================================
# SECTION B - FEATURES ICON ROW (same as home)
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
        "background_background": "classic", "background_color": WHITE, "padding": pad(32, 40, 32, 40),
        "border_border": "solid",
        "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "1", "left": "0", "isLinked": False},
        "border_color": "#E5E7EB",
    },
    elements=[row(elements=[icon_box(i, t, d) for i, t, d in features], gap="24", justify="space-between", wrap="wrap")],
)

# =========================================================
# SECTION C - "MOLT MES QUE UN JARDÍ" split content
# =========================================================
checklist = [
    ("search", "Anàlisi de l'espai", "Escoltem les teves necessitats"),
    ("pencil-ruler", "Disseny a mida", "Propostes creatives i funcionals"),
    ("seedling", "Selecció de plantes", "Espècies adaptades al clima"),
    ("cogs", "Execució professional", "Cuidem cada detall"),
    ("heart", "Jardins per gaudir", "Benestar per a tu i el teu entorn"),
]

content_left = col(
    settings={"width": {"unit": "%", "size": 45}}, gap="20",
    elements=[
        heading("DISSENY DE JARDINS", size="p", color=RED, font_size=13,
                extra={"typography_typography": "custom", "typography_font_weight": "600",
                       "letter_spacing": {"unit": "px", "size": 2, "sizes": []}}),
        heading('Molt més <span style="color:%s">que un jardí</span>' % RED, size="h2", font_size=34),
        text("Dissenyem i construïm jardins que s'adapten al teu espai, al teu estil de vida i a l'entorn. "
             "Cada projecte és únic, combinant estètica, funcionalitat i sostenibilitat per crear espais "
             "verds que perdurin en el temps.", font_size=16),
        col(gap="12", elements=[icon_box(i, t, d, position="left") for i, t, d in checklist]),
        button("DEMANA PRESSUPOST", bg=RED, color=WHITE),
    ]
)

testimonial_overlay = col(
    settings={
        "background_background": "classic", "background_color": "rgba(10,20,15,0.6)",
        "padding": pad(24, 24, 24, 24),
        "_position": "absolute", "_offset_x": {"unit": "px", "size": -16}, "_offset_y": {"unit": "px", "size": -16},
        "width": {"unit": "%", "size": 70},
    },
    gap="8",
    elements=[
        heading('"Jardins que<br>milloren vides"', size="h3", color=WHITE, font_size=22,
                extra={"typography_typography": "custom", "typography_font_style": "italic"}),
        text("Disseny, natura i emoció en equilibri perfecte.", color="#E5E5E5", font_size=14),
    ]
)

content_right = C({"content_width": "full", "width": {"unit": "%", "size": 55}, "position": "relative"}, [
    image(ph("Foto jardí disseny detall", 900, 700, bg="2f4a3a", fg="ffffff")),
    testimonial_overlay,
])

content_section = section(
    settings={"background_background": "classic", "background_color": WHITE, "padding": pad(80, 40, 80, 40)},
    elements=[row(elements=[content_left, content_right], gap="40", justify="space-between", align="flex-start", wrap="wrap")],
)

# =========================================================
# SECTION D - PROJECTS (6 cards)
# =========================================================
projects = [
    ("Jardí mediterrani", "Figueres"),
    ("Jardí amb piscina", "Empuriabrava"),
    ("Jardí contemporani", "Peralada"),
    ("Racó chill out", "Empuriabrava"),
    ("Jardí amb oliveres", "L'Escala"),
    ("Jardí amb desnivells", "Girona"),
]

def project_card(title, place):
    return col(settings={"width": {"unit": "%", "size": 31.5}}, gap="8", elements=[
        image(ph(title, 600, 450, bg="c9d9c2", fg="1e2a22"), alt=title),
        row(elements=[
            col(gap="2", elements=[
                heading(title, size="h4", font_size=18, weight="600"),
                text(place, font_size=14),
            ]),
            icon("arrow-right", color=TEXT_DARK, size=14),
        ], justify="space-between", wrap="nowrap"),
    ])

projects_section = section(
    settings={"background_background": "classic", "background_color": LIGHTGRAY_BG, "padding": pad(80, 40, 80, 40)},
    elements=[
        row(elements=[
            heading('Projectes de <span style="color:%s">disseny de jardins</span>' % RED, size="h2", font_size=32),
            text("VEURE TOTS ELS PROJECTES →", font_size=13, color=TEXT_DARK),
        ], justify="space-between", wrap="nowrap"),
        row(elements=[project_card(t, p) for t, p in projects], gap="24", justify="flex-start"),
    ]
)

# =========================================================
# SECTION E - WHY TRUST (dark green, 2x2 perks)
# =========================================================
perks = [
    ("award", "Experiència i professionalitat", "Fundats l'any 1977"),
    ("drafting-compass", "Projectes personalitzats", "Ens adaptem a tu"),
    ("recycle", "Compromís amb el medi ambient", "Solucions sostenibles"),
    ("heart", "Passió per la natura", "Fem créixer espais, fem créixer persones"),
]

trust_left = col(
    settings={"width": {"unit": "%", "size": 40}}, gap="20",
    elements=[
        heading("Per què confiar en Newtree?", size="h2", color=WHITE, font_size=32, weight="700"),
        text("Som una empresa de jardineria i paisatgisme fundada l'any 1977, amb més de 50 anys d'experiència a l'Empordà. "
             "Ens apassiona la natura i treballem per crear espais verds que generin benestar, bellesa i valor.",
             color="#D7DED9", font_size=16),
        button("CONEIX NOSALTRES", border=WHITE),
    ]
)

trust_right = row(
    settings={"width": {"unit": "%", "size": 55}},
    elements=[icon_box(i, t, d, icon_color=GREEN, title_color=WHITE, desc_color="#D7DED9", position="left")
              for i, t, d in perks],
    gap="24", justify="flex-start", wrap="wrap",
)

trust_section = section(
    settings={"background_background": "classic", "background_color": DARKGREEN, "padding": pad(90, 40, 90, 40)},
    elements=[row(elements=[trust_left, trust_right], gap="40", justify="space-between", align="flex-start", wrap="wrap")],
)

# =========================================================
# SECTION F - "COM TREBALLEM" PROCESS STEPS
# =========================================================
steps = [
    ("01", "Escoltem les teves idees", "Entenem les teves necessitats i l'espai disponible."),
    ("02", "Dissenyem la proposta", "Et presentem un projecte personalitzat."),
    ("03", "Executem el jardí", "Amb un equip expert i materials de qualitat."),
    ("04", "Gaudeixes del resultat", "Un espai verd per viure i compartir."),
]

def step_item(number, title, desc):
    badge = C({
        "content_width": "full", "flex_direction": "row", "flex_justify_content": "center",
        "flex_align_items": "center", "width": {"unit": "px", "size": 48},
        "height": {"unit": "px", "size": 48}, "background_background": "classic",
        "background_color": GREEN, "border_radius": {"unit": "%", "top": "50", "right": "50", "bottom": "50", "left": "50", "isLinked": True},
    }, [heading(number, size="p", color=WHITE, font_size=16, weight="700", align="center")])
    return col(settings={"width": {"unit": "%", "size": 21}}, gap="12", elements=[
        badge,
        heading(title, size="h4", font_size=18, weight="600"),
        text(desc, font_size=14),
    ])

steps_row_elements = []
for idx, (n, t, d) in enumerate(steps):
    steps_row_elements.append(step_item(n, t, d))
    if idx < len(steps) - 1:
        steps_row_elements.append(C({
            "content_width": "full", "flex_direction": "row", "flex_justify_content": "center",
            "flex_align_items": "center", "width": {"unit": "px", "size": 24},
        }, [icon("arrow-right", color=TEXT_GRAY, size=18)]))

process_section = section(
    settings={"background_background": "classic", "background_color": WHITE, "padding": pad(80, 40, 80, 40)},
    elements=[
        heading("Com treballem", size="h2", font_size=32),
        row(elements=steps_row_elements, gap="16", justify="space-between", align="flex-start", wrap="wrap"),
    ]
)

# =========================================================
# SECTION G - BOTTOM CTA BANNER (same as home)
# =========================================================
contact_items = [
    ("phone", "Truca'ns", "(+34) 972 560 033"),
    ("whatsapp", "WhatsApp", "Envia'ns un missatge"),
    ("envelope", "Escriu-nos", "info@newtree.cat"),
]

banner_left = col(settings={"width": {"unit": "%", "size": 50}}, gap="16", elements=[
    heading("Tens un projecte de jardí?", size="h2", color=WHITE, font_size=30, weight="700"),
    text("Parlem-ne i t'ajudem a fer-lo realitat.", color="#D7DED9", font_size=16),
    button("DEMANA PRESSUPOST", bg=GREEN, color=WHITE),
])

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
    settings={"background_background": "classic", "background_color": BLACKBG,
              "padding": pad(70, 40, 70, 40), "position": "relative"},
    elements=[row(elements=[banner_left, banner_right], justify="space-between", align="center", wrap="wrap"), banner_decor],
)

# =========================================================
# ASSEMBLE PAGE
# =========================================================
page = {
    "content": [hero, features_row, content_section, projects_section, trust_section, process_section, banner_section],
    "page_settings": [],
    "version": "0.4",
    "title": "Jardineria (Disseny de jardins) - New Tree",
    "type": "page",
}

out_path = "/home/user/eco-store-sass-lpage/elementor-templates/jardineria.json"
with open(out_path, "w", encoding="utf-8") as f:
    json.dump(page, f, ensure_ascii=False, indent=2)

with open(out_path, encoding="utf-8") as f:
    reloaded = json.load(f)
print("valid json, top-level sections:", len(reloaded["content"]))
