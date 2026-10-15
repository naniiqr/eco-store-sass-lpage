"""Empresa, Galeria, Plantes exemplars y Situació i contacte con el TEXTO LITERAL de newtree.cat
(solo erratas corregidas) dentro del diseño del rediseño. Escribe en ../paginas/.
"""
import json, os
from design import *
from build_servicios import (img, hero_section, intro_section, gallery_section, acc_last)


# Miniaturas de 300 px (el servidor las genera): Elementor descarga a la biblioteca de medios cada imagen
# de la plantilla al importar; con las PNG originales (1,5-1,9 MB) la importación agotaba el tiempo.
THUMB = {
    "11": "11-300x225.png",
    "10": "10-300x220.png",
    "9": "9-300x218.png",
    "12": "12-300x225.png",
    "13": "13-300x224.png",
    "14": "14-300x222.png",
    "15": "15-300x225.png",
    "16": "16-300x223.png",
    "17": "17-300x220.png",
    "2": "2-300x200.png",
    "1": "1-300x200.png",
    "4": "4-300x200.png",
    "3": "3-300x200.png",
    "20": "20-300x255.png",
    "19": "19-300x254.png",
    "5": "5-300x200.png",
    "8": "8-300x200.png",
    "5-2": "5-2-300x200.png"
}


def thumb(n):
    return "2020/04/" + THUMB.get(n, n + ".png")


def wrap(title, secs):
    return page(title, secs)


# ---------------- EMPRESA ----------------
def empresa():
    p = dict(
        title="Empresa",
        paras=[
            "Empresa de jardineria privada i pública oferim servei a tota la província de Girona: Figueres, Roses, L'Escala, Empuriabrava, Peralada, Castelló d'Empúries, Llançà.",
            "Partint des de zero podem dissenyar i construir el teu jardí segons les teves necessitats. New Tree, empresa fundada l'any 1977 dedicada a la jardineria privada i pública.",
            "Ofereix serveis que van des de l'assessorament i disseny de jardins fins a l'execució i el manteniment d'aquests.",
            "Disposem dels recursos humans, tècnics i de maquinària necessaris per a la realització de qualsevol feina de jardineria pública, privada o de gestió del paisatge.",
            "Oferim serveis a tot Girona, Figueres, Empuriabrava, Castelló d'Empúries, Port de la Selva.",
        ],
        side=img("2020/04/arbret.png"),
    )
    vocation = [("tree", "Crear espais integrats amb l'entorn natural de la zona", ""),
                ("tint", "Crear jardins de baix manteniment, sostenibles amb els recursos hídrics", ""),
                ("leaf", "Poder portar part de la natura a cada jardí que dissenyem", ""),
                ("smile", "I, el més important, crear espais per poder gaudir", "")]
    vocation_sec = perks_dark(vocation, title="La nostra principal vocació")
    strip = dict(title="Empresa", gallery=[thumb(n) for n in ["11", "10", "9", "12", "13", "14", "15", "16", "17"]])
    return wrap("Empresa", [hero_section(p), features_strip(), intro_section(p), vocation_sec,
                            gallery_section(strip), cta_banner()])


# ---------------- GALERIA ----------------
KW = "galeria de jardins Girona"
# 16 fotos distintas de la galería original (se omiten duplicados: 5-2, 18 y 3; y la 8, que lleva una etiqueta suelta)
GALLERY = [
    ("11", "Galeria de jardins Girona: casa blanca amb piscina i palmeres"),
    ("10", "Jardinera metàl·lica amb plantes al costat d'una piscina"),
    ("16", "Jardineres negres amb plantes al voltant d'una piscina"),
    ("9", "Palmeres sobre grava blanca davant d'un mur"),
    ("13", "Gespa natural i jardí davant d'una casa moderna"),
    ("12", "Zona verda amb gespa natural i arbres plantats"),
    ("14", "Jardí amb gespa, olivera i pèrgola de fusta"),
    ("17", "Galeria de jardins Girona: gespa artificial amb olivera i grava blanca"),
    ("15", "Olivera podada com un bonsai davant d'un jardí vertical"),
    ("5", "Jardí vertical amb plantes de colors"),
    ("2", "Aspersors de reg automàtic regant la gespa"),
    ("1", "Rotlle de gespa artificial"),
    ("4", "Jardiner tallant la gespa amb una desbrossadora"),
    ("20", "Podador amb motoserra pujat a un arbre"),
    ("19", "Galeria de jardins Girona: poda d'arbres amb plataforma elevadora"),
    ("7", "Obra d'un jardí amb terra, grava i plantes noves"),
]
SVC = {"disseny i construcció de jardins": "disseny-i-construccio-de-jardins", "gespa natural i artificial": "instal%c2%b7lacio-de-gespa",
       "sistemes de reg": "sistemes-de-reg", "jardins verticals": "jardins-verticals", "podes": "podes",
       "manteniment de jardins": "manteniment-de-jardins", "terres i substrats": "terres-i-substrats",
       "neteja de parcel·les": "nateja-parceles", "tanques i murs de contenció": "tanques-murs"}


def lnk(t):
    return '<a href="%s%s/" style="color:%s;font-weight:700">%s</a>' % (SITE, SVC[t], GREEN, t)


MAPS = "https://www.google.com/maps/search/?api=1&query=Cam%C3%AD+de+Reg+de+la+Vinya+Calabuig+B%C3%A0scara+Girona"
SEO_TEXT = [
    ("h2", "Galeria de jardins Girona: què hi trobaràs"),
    ("p", "Aquesta galeria de jardins Girona reuneix imatges de la nostra feina. New Tree és una empresa de jardineria "
          "fundada l'any 1977, dedicada a la jardineria privada i pública. Per això, tenim més de 50 anys d'experiència "
          "a Girona i l'Empordà."),
    ("p", "Hi trobaràs %s, %s, %s, %s i %s. També fem %s, %s, %s i %s." % (
        lnk("disseny i construcció de jardins"), lnk("gespa natural i artificial"), lnk("sistemes de reg"),
        lnk("jardins verticals"), lnk("podes"), lnk("manteniment de jardins"), lnk("terres i substrats"),
        lnk("neteja de parcel·les"), lnk("tanques i murs de contenció"))),
    ("h3", "Del disseny al manteniment"),
    ("p", "Partint des de zero podem dissenyar i construir el teu jardí segons les teves necessitats. A més, oferim "
          "serveis que van des de l'assessorament i el disseny fins a l'execució i el manteniment. Disposem dels "
          "recursos humans, tècnics i de maquinària necessaris per a qualsevol feina de jardineria pública, privada "
          "o de gestió del paisatge."),
    ("h3", "La nostra principal vocació"),
    ("p", "Volem crear espais integrats amb l'entorn natural de la zona. Busquem jardins de baix manteniment i "
          "sostenibles amb els recursos hídrics. També volem portar part de la natura a cada jardí que dissenyem. "
          "I, el més important, crear espais per poder gaudir."),
    ("h2", "Treballem a tota la província de Girona"),
    ("p", "Oferim servei a Girona, Figueres, Roses, L'Escala, Empuriabrava, Peralada, Castelló d'Empúries, Llançà i "
          "Port de la Selva. Treballem per a particulars i per a ajuntaments: molts ajuntaments confien en New Tree "
          "per a la seva obra pública."),
    ("p", "Si t'agrada algun jardí d'aquesta galeria de jardins Girona, parlem-ne. Demana pressupost i t'assessorarem. "
          'Escriu-nos a info@newtree.cat, truca\'ns al (+34) 972 560 033 o <a href="%s" style="color:%s;font-weight:700">'
          "visita'ns a Calabuig – Bàscara</a>." % (MAPS, GREEN)),
]


def galeria():
    p = dict(
        title="Galeria de jardins Girona",
        h1='Galeria de jardins <span style="color:%s">Girona</span>' % GREEN_ACCENT,
        lead="Galeria de jardins Girona: alguns dels projectes que hem fet a Girona i l'Empordà.",
        btn2=("VEURE SERVEIS", SITE + "jardineria/"),
    )
    cells = [C({"content_width": "full", "width": {"unit": "%", "size": 23}},
               [pic(img(thumb(n)), alt, radius=12, height=220, link=BASE + "2020/04/%s.png" % n)])
             for n, alt in GALLERY]
    grid = section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                             "padding": pad(80, 40, 80, 40)},
                   elements=[heading(acc("Projectes que", "inspiren"), size="h2", font_size=36),
                             row(elements=cells, gap="18", justify="center", align="flex-start")])
    body = []
    for kind, t in SEO_TEXT:
        if kind == "p":
            body.append(text(t, font_size=17))
        else:
            body.append(heading(t, size=kind, font_size=30 if kind == "h2" else 22))
    body.append(button("DEMANA PRESSUPOST", bg=RED, color=WHITE, link=MAIL))
    seo = section(settings={"background_background": "classic", "background_color": WHITE,
                            "padding": pad(80, 40, 80, 40)},
                  elements=[col(settings={"width": {"unit": "%", "size": 72}, "flex_align_items": "flex-start"},
                                gap="18", elements=body)])
    insta = section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                              "padding": pad(70, 40, 70, 40)},
                    elements=[heading(acc("Segueix-nos a", "Instagram"), size="h2", font_size=34),
                              # requereix el plugin «Instagram Feed» (a la web actual és el shortcode [instagram-feed])
                              W("shortcode", {"shortcode": "[instagram-feed]"})])
    return wrap("Galeria de jardins Girona", [hero_section(p), grid, seo, insta, cta_banner()])


# ---------------- PLANTES EXEMPLARS ----------------
def plantes():
    # Texto de la versión catalana de la página (newtree.cat/plantes-exemplars/).
    p = dict(
        title="Plantes exemplars",
        paras=["Us oferim un servei de disseny i creació de jardins a mida, per adaptar-nos a les vostres necessitats i poder-vos oferir un servei totalment personalitzat."],
        side=img("2020/04/plantes.jpg"),
    )
    return wrap("Plantes exemplars", [hero_section(p), features_strip(), intro_section(p), cta_banner()])


# ---------------- SITUACIÓ I CONTACTE ----------------
_radius = R


def badge_item(ic, title, desc):
    """Dato de contacto con icono en círculo verde (colores de marca)."""
    w = icon_box(ic, title, desc, icon_color=GREEN, title_color=WHITE, desc_color="#D7DED9", position="left")
    w["settings"].update({"view": "stacked", "shape": "circle", "secondary_color": WHITE,
                          "icon_size": {"unit": "px", "size": 18, "sizes": []},
                          "icon_padding": {"unit": "px", "size": 14, "sizes": []}})
    return w


def contacte():
    p = dict(title="Situació i contacte")
    info = [("map-marker-alt", "Adreça", ADDRESS),
            ("phone", "Telèfons", "(+34) 972 560 033 · (+34) 607 484 646"),
            ("envelope", "Correu electrònic", "info@newtree.cat")]
    fields = [
        {"_id": "f_name", "custom_id": "name", "field_type": "text", "field_label": "Nom",
         "placeholder": "Nom", "required": "true", "width": "100"},
        {"_id": "f_email", "custom_id": "email", "field_type": "email", "field_label": "Email",
         "placeholder": "Email", "required": "true", "width": "100"},
        {"_id": "f_msg", "custom_id": "message", "field_type": "textarea", "field_label": "Missatge",
         "placeholder": "Missatge", "required": "true", "width": "100", "rows": 6},
    ]
    border = {"unit": "px", "top": "0", "right": "0", "bottom": "0", "left": "0", "isLinked": True}
    form = W("form", {
        "form_name": "Contacte", "form_fields": fields, "button_text": "Enviar",
        "email_to": "info@newtree.cat", "email_subject": "Nou missatge des de newtree.cat",
        "success_message": "Missatge enviat. Gràcies!",
        "show_labels": "", "input_size": "md",
        "column_gap": {"unit": "px", "size": 16, "sizes": []}, "row_gap": {"unit": "px", "size": 16, "sizes": []},
        # camps: blancs, cantonades arrodonides, sense vora
        "field_text_color": TEXT_DARK, "field_background_color": WHITE,
        "field_border_border": "solid", "field_border_width": border, "field_border_radius": _radius(10),
        "field_typography_typography": "custom", "field_typography_font_family": "Nunito",
        "field_typography_font_size": {"unit": "px", "size": 15, "sizes": []},
        # botó: verd molt fosc de la marca, ample complet
        "button_background_color": DARKGREEN, "button_text_color": WHITE, "button_width": "100",
        "button_border_radius": _radius(10),
        "button_typography_typography": "custom", "button_typography_font_family": "Nunito",
        "button_typography_font_weight": "700",
    })
    left = col(settings={
        "width": {"unit": "%", "size": 40}, "background_background": "classic", "background_color": DARKGREEN,
        "padding": pad(48, 40, 48, 40), "padding_mobile": pad(32, 24, 32, 24), "padding_tablet": pad(40, 32, 40, 32)},
        gap="22", elements=[
            eyebrow("CONTACTE"),
            heading(SLOGAN, size="h2", color=WHITE, font_size=28),
            col(gap="20", elements=[badge_item(i, t, d) for i, t, d in info]),
        ])
    right = col(settings={
        "width": {"unit": "%", "size": 60}, "background_background": "classic", "background_color": GREEN,
        "padding": pad(48, 40, 48, 40), "padding_mobile": pad(32, 24, 32, 24), "padding_tablet": pad(40, 32, 40, 32),
        "flex_justify_content": "center"}, gap="16", elements=[form])
    card = row(settings={"border_radius": _radius(24), "overflow": "hidden",
                         "box_shadow_box_shadow_type": "yes",
                         "box_shadow_box_shadow": {"horizontal": 0, "vertical": 20, "blur": 50, "spread": 0,
                                                   "color": "rgba(18,35,24,0.18)"}},
               elements=[left, right], gap="0", justify="center", align="stretch")
    contact_sec = section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                                    "padding": pad(90, 40, 40, 40)}, elements=[card])
    gmap = col(settings={"border_radius": _radius(20), "overflow": "hidden",
                         "box_shadow_box_shadow_type": "yes",
                         "box_shadow_box_shadow": {"horizontal": 0, "vertical": 10, "blur": 30, "spread": 0,
                                                   "color": "rgba(18,35,24,0.12)"}},
               elements=[W("google_maps", {"address": ADDRESS,
                                           "zoom": {"unit": "px", "size": 13, "sizes": []},
                                           "height": {"unit": "px", "size": 380, "sizes": []}})])
    map_sec = section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                                "padding": pad(20, 40, 90, 40)}, elements=[gmap])
    return wrap("Situació i contacte", [hero_section(p), contact_sec, map_sec])


if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "paginas")
    os.makedirs(out_dir, exist_ok=True)
    for name, fn in [("empresa", empresa), ("galeria", galeria),
                     ("plantes-exemplars", plantes), ("situacio-i-contacte", contacte)]:
        path = os.path.join(out_dir, name + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(fn(), f, ensure_ascii=False, indent=2)
        with open(path, encoding="utf-8") as f:
            print(f"{name}.json ok ({len(json.load(f)['content'])} secciones)")
