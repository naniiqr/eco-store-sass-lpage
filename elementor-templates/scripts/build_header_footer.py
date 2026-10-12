"""Plantillas de Theme Builder (Elementor Pro): header.json y footer.json, con datos reales de newtree.cat.
Uso: python3 build_header_footer.py   (escribe ../header.json y ../footer.json)
"""
import json, os
from lib_elementor import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
GRAY = "#B9BFB9"
MAIL = "mailto:info@newtree.cat"
SITE = "https://newtree.cat/"
LOGO_W = 120


def link_icon(name, color, size, url):
    w = icon(name, color=color, size=size)
    w["settings"]["link"] = {"url": url, "is_external": "on", "nofollow": "", "custom_attributes": ""}
    return w


def logo(width, align="left"):
    return W("theme-site-logo", {"width": {"unit": "px", "size": width, "sizes": []}, "align": align})


# ------------------------------- HEADER -------------------------------
nav = W("nav-menu", {
    "layout": "horizontal", "menu": "",            # asignar el menú de WordPress tras importar
    "dropdown": "tablet", "toggle": "burger", "pointer": "underline",
    "menu_color_text": TEXT_DARK, "color_menu_item_hover": GREEN,
    "menu_typography_typography": "custom",
    "menu_typography_font_size": {"unit": "px", "size": 14, "sizes": []},
    "menu_typography_font_weight": "600",
})
lang = text('<a href="#" style="color:%s">CA</a> &nbsp;<a href="#" style="color:%s">ES</a> &nbsp;'
            '<a href="#" style="color:%s">FR</a> &nbsp;<a href="#" style="color:%s">ENG</a>' % ((WHITE,) * 4),
            color=WHITE, font_size=12)
top_info = text('(+34) 972 560 033 &nbsp;·&nbsp; (+34) 607 484 646 &nbsp;·&nbsp; info@newtree.cat',
                color="#D7DED9", font_size=12)
topbar = section(
    settings={"background_background": "classic", "background_color": DARKGREEN,
              "padding": pad(8, 40, 8, 40), "hide_tablet": "hidden-tablet", "hide_mobile": "hidden-mobile"},
    elements=[row(settings={"flex_wrap": "nowrap"}, elements=[top_info, lang], gap="16",
                  justify="space-between", align="center")],
)

cta = button("DEMANA PRESSUPOST", bg=RED, color=WHITE, link=MAIL)
cta["settings"]["hide_mobile"] = "hidden-mobile"
header_row = row(
    settings={"flex_wrap": "nowrap", "_keep_row": True},   # en móvil: logo + hamburguesa en una sola fila
    elements=[logo(LOGO_W), nav, cta],
    gap="16", justify="space-between", align="center",
)
header = section(
    settings={"background_background": "classic", "background_color": WHITE, "padding": pad(14, 40, 14, 40),
              "sticky": "top", "sticky_on": ["desktop", "tablet", "mobile"], "z_index": 100,
              "box_shadow_box_shadow_type": "yes",
              "box_shadow_box_shadow": {"horizontal": 0, "vertical": 2, "blur": 12, "spread": 0,
                                        "color": "rgba(0,0,0,0.08)"}},
    elements=[header_row],
)

# ------------------------------- FOOTER -------------------------------
def foot_title(t):
    return heading(t, size="h4", color=WHITE, font_size=16)


def foot_text(html_, color=GRAY):
    return text(html_, color=color, font_size=14)


logo_box = col(settings={"background_background": "classic", "background_color": WHITE,
                         "padding": pad(8, 8, 8, 8), "width": {"unit": "px", "size": LOGO_W + 16},
                         "border_radius": {"unit": "px", "top": "10", "right": "10", "bottom": "10",
                                           "left": "10", "isLinked": True}},
               elements=[logo(LOGO_W, "center")])

col_brand = col(settings={"width": {"unit": "%", "size": 25}}, gap="16", elements=[
    logo_box,
    foot_text("New Tree convertim un desert en un jardí"),
])

col_contact = col(settings={"width": {"unit": "%", "size": 36}}, gap="14", elements=[
    foot_title("Contacte"),
    icon_box("map-marker-alt", "Adreça", "Camí de Reg de la Vinya s/n, Calabuig – Bàscara, Girona 17483",
             icon_color=GREEN, title_color=WHITE, desc_color=GRAY, position="left"),
    icon_box("phone", "Telèfons", "(+34) 972 560 033 · (+34) 607 484 646",
             icon_color=GREEN, title_color=WHITE, desc_color=GRAY, position="left"),
    icon_box("envelope", "Correu electrònic", "info@newtree.cat",
             icon_color=GREEN, title_color=WHITE, desc_color=GRAY, position="left"),
])

services = [("Disseny i Construcció de Jardins", "disseny-i-construccio-de-jardins"),
            ("Sistemes de Reg", "sistemes-de-reg"),
            ("Instal·lació de Gespa", "instal%c2%b7lacio-de-gespa"),
            ("Manteniment de jardins", "manteniment-de-jardins"),
            ("Jardins verticals", "jardins-verticals"),
            ("Obra pública", "jardineria-2"),
            ("Terres i substrats", "terres-i-substrats"),
            ("Nateja Parcel·les", "nateja-parceles"),
            ("Tanques i Murs", "tanques-murs"),
            ("Podes", "podes")]
col_links = col(settings={"width": {"unit": "%", "size": 25}}, gap="10", elements=[
    foot_title("Jardineria"),
    foot_text("<br>".join('<a href="%s%s/" style="color:%s">%s</a>' % (SITE, s, GRAY, t) for t, s in services)),
])

top = row(elements=[col_brand, col_contact, col_links], gap="40", justify="space-between", align="flex-start")

legal = foot_text('<a href="#" style="color:%s">Avís legal</a> &nbsp;|&nbsp; '
                  '<a href="#" style="color:%s">Política de privacitat</a>' % (GRAY, GRAY))
bottom = row(
    settings={"border_border": "solid",
              "border_width": {"unit": "px", "top": "1", "right": "0", "bottom": "0", "left": "0", "isLinked": False},
              "border_color": "rgba(255,255,255,0.15)", "padding": pad(20, 0, 0, 0)},
    elements=[legal, link_icon("instagram", WHITE, 18, "#")],  # sustituir # por el Instagram real
    gap="16", justify="space-between", align="center",
)
footer = section(
    settings={"background_background": "classic", "background_color": BLACKBG, "padding": pad(60, 40, 28, 40)},
    elements=[col(settings={"flex_gap": {"column": "40", "row": "40", "unit": "px", "isLinked": True}},
                  elements=[top, bottom], gap="40")],
)

for name, title, ttype, els in [("header", "Header - New Tree", "header", [topbar, header]),
                                ("footer", "Footer - New Tree", "footer", [footer])]:
    doc = {"content": els, "page_settings": [], "version": "0.4", "title": title, "type": ttype}
    with open(os.path.join(ROOT, name + ".json"), "w", encoding="utf-8") as f:
        json.dump(doc, f, ensure_ascii=False, indent=2)
    print(name + ".json ok")
