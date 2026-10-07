"""Páginas restantes del menú (Empresa, Galeria, Plantes exemplars, Situació i contacte).

Solo se toma contenido e imágenes de newtree.cat; el diseño es el del PDF (reutiliza
los helpers y secciones de build_servicios.py). Escribe en ../paginas/.
"""
import json, os
from lib_elementor import *
from build_servicios import (img, eyebrow, hero_section, intro_section, gallery_section,
                             cta_section, MAIL)

SLOGAN = "New Tree convertim un desert en un jardí"
ADDRESS = "Camí de Reg de la Vinya s/n, Calabuig – Bàscara, Girona 17483"


def wrap(title, secs):
    return {"content": secs, "page_settings": [], "version": "0.4",
            "title": title + " - New Tree", "type": "page"}


# ---------------- EMPRESA ----------------
def empresa():
    p = dict(
        title="Empresa",
        h1="Una empresa de <span style=\"color:%s\">jardineria</span>" % GREEN,
        lead="Empresa de jardineria privada i pública.",
        paras=[
            "Partint des de zero podem dissenyar i construir el teu jardí segons les teves necessitats. New Tree, empresa fundada l'any 1977, dedicada a la jardineria privada i pública.",
            "Oferim serveis que van des de l'assessorament i disseny de jardins fins a l'execució i el manteniment d'aquests.",
            "Disposem dels recursos humans, tècnics i de maquinària necessaris per a la realització de qualsevol feina de jardineria pública, privada o de gestió del paisatge.",
        ],
        side=img("2020/04/arbret.png"),
    )
    vocation = [("tree", "Integrats amb l'entorn", "Espais integrats amb l'entorn natural de la zona"),
                ("tint", "Baix manteniment", "Jardins sostenibles amb els recursos hídrics"),
                ("leaf", "Natura a cada jardí", "Portar part de la natura a cada jardí que dissenyem"),
                ("smile", "Espais per gaudir", "El més important: crear espais per poder gaudir")]
    vocation_sec = section(
        settings={"background_background": "classic", "background_color": DARKGREEN,
                  "padding": pad(80, 40, 80, 40)},
        elements=[
            heading("La nostra vocació", size="h2", color=WHITE, font_size=32),
            row(elements=[C({"content_width": "full", "width": {"unit": "%", "size": 23}},
                            [icon_box(i, t, d, icon_color=GREEN, title_color=WHITE, desc_color="#D7DED9")])
                          for i, t, d in vocation], gap="24", justify="space-between", align="flex-start"),
        ])
    zones = ["Girona", "Figueres", "Roses", "L'Escala", "Empuriabrava", "Peralada",
             "Castelló d'Empúries", "Llançà", "Port de la Selva"]
    zones_sec = section(
        settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                  "padding": pad(70, 40, 70, 40)},
        elements=[
            heading("Treballem a tota la província de Girona", size="h2", font_size=30),
            row(elements=[icon_box("map-marker-alt", z, "", position="left") for z in zones],
                gap="20", justify="flex-start", align="flex-start"),
        ])
    return wrap("Empresa", [hero_section(p), intro_section(p), vocation_sec, zones_sec, cta_section()])


# ---------------- GALERIA ----------------
def galeria():
    nums = ["11", "10", "9", "12", "13", "14", "15", "16", "17", "2", "1", "4", "3",
            "18", "20", "19", "5", "7", "8", "5-2"]
    cells = [C({"content_width": "full", "width": {"unit": "%", "size": 23.5}},
               [image(img("2020/04/%s.png" % n), alt="Galeria New Tree")]) for n in nums]
    grid = section(settings={"background_background": "classic", "background_color": WHITE,
                             "padding": pad(80, 40, 80, 40)},
                   elements=[eyebrow("PROJECTES"),
                             heading("Galeria", size="h2", font_size=32),
                             row(elements=cells, gap="20", justify="flex-start", align="flex-start")])
    p = dict(h1="<span style=\"color:%s\">Galeria</span>" % GREEN, lead=SLOGAN)
    return wrap("Galeria", [hero_section(p), grid, cta_section()])


# ---------------- PLANTES EXEMPLARS ----------------
def plantes():
    p = dict(
        title="Plantes exemplars",
        h1="Plantes <span style=\"color:%s\">exemplars</span>" % GREEN,
        lead=SLOGAN,
        paras=["Us oferim un servei de disseny i creació de jardins a mida, per adaptar-nos a les vostres necessitats i poder-vos oferir un servei totalment personalitzat."],
        side=img("2020/04/plantes-1024x683.jpg"),
    )
    extra = section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                              "padding": pad(60, 40, 60, 40)},
                    elements=[row(elements=[
                        C({"content_width": "full", "width": {"unit": "%", "size": 40}},
                          [image(img("2020/04/arbret.png"), alt="Plantes exemplars")]),
                        col(settings={"width": {"unit": "%", "size": 55}}, gap="16", elements=[
                            heading("Vols veure els nostres exemplars?", size="h3", font_size=26),
                            text("Visita'ns a Calabuig – Bàscara o contacta amb nosaltres.", font_size=16),
                            button("DEMANA INFORMACIÓ", bg=GREEN, link=MAIL),
                        ])], gap="40", justify="space-between", align="center")])
    return wrap("Plantes exemplars", [hero_section(p), intro_section(p), extra, cta_section()])


# ---------------- SITUACIÓ I CONTACTE ----------------
def contacte():
    p = dict(h1="Situació i <span style=\"color:%s\">contacte</span>" % GREEN, lead=SLOGAN)
    info = [("map-marker-alt", "Adreça", ADDRESS),
            ("phone", "Telèfons", "(+34) 972 560 033 · (+34) 607 484 646"),
            ("envelope", "Correu electrònic", "info@newtree.cat")]
    fields = [
        {"_id": "f_name", "custom_id": "name", "field_type": "text", "field_label": "Nom",
         "placeholder": "Nom", "required": "true", "width": "100"},
        {"_id": "f_email", "custom_id": "email", "field_type": "email", "field_label": "Correu electrònic",
         "placeholder": "Correu electrònic", "required": "true", "width": "100"},
        {"_id": "f_msg", "custom_id": "message", "field_type": "textarea", "field_label": "Missatge",
         "placeholder": "Missatge", "required": "true", "width": "100", "rows": 5},
    ]
    form = W("form", {"form_name": "Contacte", "form_fields": fields, "button_text": "Enviar",
                      "button_background_color": GREEN, "button_text_color": WHITE,
                      "email_to": "info@newtree.cat", "email_subject": "Nou missatge des de newtree.cat",
                      "success_message": "Missatge enviat. Gràcies!"})
    left = col(settings={"width": {"unit": "%", "size": 45}}, gap="20", elements=[
        eyebrow("CONTACTE"),
        heading("Parlem del teu jardí", size="h2", font_size=32),
        col(gap="14", elements=[icon_box(i, t, d, position="left") for i, t, d in info]),
    ])
    right = col(settings={"width": {"unit": "%", "size": 50}}, gap="16", elements=[form])
    contact_sec = section(settings={"background_background": "classic", "background_color": WHITE,
                                    "padding": pad(80, 40, 40, 40)},
                          elements=[row(elements=[left, right], gap="40", justify="space-between",
                                        align="flex-start")])
    map_sec = section(settings={"background_background": "classic", "background_color": WHITE,
                                "padding": pad(20, 40, 80, 40)},
                      elements=[W("google_maps", {"address": ADDRESS,
                                                  "zoom": {"unit": "px", "size": 13, "sizes": []},
                                                  "height": {"unit": "px", "size": 380, "sizes": []}})])
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
