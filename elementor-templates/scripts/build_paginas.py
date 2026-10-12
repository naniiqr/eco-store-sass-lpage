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
def galeria():
    nums = ["11", "10", "9", "12", "13", "14", "15", "16", "17", "2", "1", "4", "3",
            "18", "20", "19", "5", "7", "8", "5-2"]
    cells = [C({"content_width": "full", "width": {"unit": "%", "size": 23}},
               [pic(img(thumb(n)), "Galeria New Tree", radius=10, height=210)]) for n in nums]
    grid = section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                             "padding": pad(80, 40, 80, 40)},
                   elements=[row(elements=cells, gap="18", justify="center", align="flex-start")])
    return wrap("Galeria", [hero_section(dict(title="Galeria")), grid, cta_banner()])


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
