"""Página Inici (Home) con el diseño del PDF. Escribe ../inici-home.json."""
import json, os
from design import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

# (título, subtítulo, foto real de newtree.cat o None -> placeholder a reemplazar)
SERVICES = [
    ("Disseny de jardins", "Idees que prenen vida", "2021/08/Disseny-de-jardins.jpg"),
    ("Jardineria i plantacions", "Espais plens de color", None),
    ("Sistemes de reg", "Eficiència i estalvi d'aigua", "2020/04/2.png"),
    ("Tanques i Murs de contenció", "Seguretat i estètica en el teu espai", "2021/08/tancaments.jpeg"),
    ("Piscines i exteriors", "Entorns per gaudir", None),
    ("Gespa Artificial i Natural", "Verd tot l'any", "2021/07/gespa-artificial-6.jpeg"),
    ("Jardins verticals", "Natura en vertical", "2021/08/vertical-jpg.jpeg"),
    ("Murs i elements decoratius", "Pedra, fusta i materials naturals", None),
    ("Manteniment de jardins", "Sempre al teu costat", "2021/08/mantenimet.jpg"),
    ("Neteja de parcel·les", "Terrenys nets per a nous projectes", "2021/08/neteja-de-parcelles-1.jpeg"),
    ("Podes", "Salut i bellesa per als teus arbres", "2020/04/Poda.jpg"),
    ("Terres i sustrats", "La base d'un bon jardí", "2021/08/terres.jpeg"),
]
PROJECTS = [("Jardí residencial", "Figueres"), ("Reforma d'exterior", "Peralada"),
            ("Jardí mediterrani", "Empuriabrava"), ("Zona de piscina", "Navata")]
PERKS = [("leaf", "Jardins més saludables", "per a tu i el teu planeta"),
         ("tree", "Ús de plantes autòctones", "i baix consum hídric"),
         ("tint", "Solucions sostenibles", "i duradores"),
         ("heart", "Passió per la natura", "i el detall")]

hero_sec = hero("JARDINERIA I PAISATGISME A L'EMPORDÀ",
                'Convertim<br>un desert en<br><span style="color:%s">un jardí</span>' % GREEN_ACCENT,
                "Dissenyem, construïm i cuidem espais verds que milloren la teva vida i el nostre entorn.",
                real("2020/04/f3.jpg"), min_h=620)

cards = [service_card(t, s, real(p) if p else ph(t, 700, 500, bg="d8d3c4", fg="1e2a22")) for t, s, p in SERVICES]
services = section(
    settings={"background_background": "classic", "background_color": WHITE, "padding": pad(80, 40, 80, 40)},
    elements=[heading(acc("Els nostres", "serveis"), size="h2", font_size=38),
              row(elements=cards, gap="22", justify="center", align="stretch")])

projects = section(
    settings={"background_background": "classic", "background_color": LIGHTGRAY_BG, "padding": pad(80, 40, 80, 40)},
    elements=[
        row(elements=[heading(acc("Projectes que", "inspiren"), size="h2", font_size=38),
                      text('<a href="%s" style="color:%s;font-weight:700">VEURE TOTS ELS PROJECTES →</a>' % (GALERIA, TEXT_DARK),
                           font_size=13)],
            justify="space-between", align="center"),
        row(elements=[project_card(t, p, ph(t, 500, 400, bg="c9d9c2", fg="1e2a22"), w=23) for t, p in PROJECTS],
            gap="22", justify="center", align="flex-start")])

# bloque «A Newtree»: texto claro | foto | panel verde oscuro con ventajas
about_left = col(settings={"width_tablet": {"unit": "%", "size": 100}, "width": {"unit": "%", "size": 34}, "background_background": "classic",
                           "background_color": SOFT_GREEN_BG, "padding": pad(56, 44, 56, 44),
                           "flex_justify_content": "center"}, gap="20", elements=[
    heading(acc("A Newtree fem créixer<br>", "les teves Idees"), size="h2", font_size=34),
    text("Podem dissenyar i construir el teu jardí segons les teves necessitats. New Tree, empresa fundada "
         "l'any 1977 dedicada a la jardineria privada i pública.", font_size=16),
    button("CONEIX NOSALTRES", bg=GREEN, color=WHITE, link=SITE + "empresa/")])
about_mid = C({"content_width": "full", "width_tablet": {"unit": "%", "size": 100}, "width": {"unit": "%", "size": 33}, "min_height": {"unit": "px", "size": 440, "sizes": []},
               "background_background": "classic", "background_image": real("2020/04/ama-1024x590.jpg"),
               "background_position": "center center", "background_size": "cover"}, [])
about_right = col(settings={"width_tablet": {"unit": "%", "size": 100}, "width": {"unit": "%", "size": 33}, "background_background": "gradient",
                            "background_color": DARKGREEN, "background_color_b": DARKGREEN2,
                            "background_gradient_angle": {"unit": "deg", "size": 135, "sizes": []},
                            "padding": pad(48, 40, 48, 40), "flex_justify_content": "center"}, gap="26",
                  elements=[ibox(i, t, d, icon_color=WHITE, title_color=WHITE, desc_color=SOFT, framed=True,
                                 title_px=17, desc_px=14) for i, t, d in PERKS])
about = section(settings={"background_background": "classic", "background_color": WHITE,
                          "content_width": "full", "padding": pad(0, 0, 0, 0)},
                elements=[row(elements=[about_left, about_mid, about_right], gap="0", justify="center",
                              align="stretch")])

doc = page("Inici", [hero_sec, features_strip(), services, projects, about, cta_banner("Tens un projecte de jardineria?")])
with open(os.path.join(ROOT, "inici-home.json"), "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
print("inici-home.json ok (%d secciones)" % len(doc["content"]))
