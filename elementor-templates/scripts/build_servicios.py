"""Genera los JSON de Elementor de las páginas de servicio con el contenido real de newtree.cat.

Uso: python3 build_servicios.py   (escribe en ../servicios/)
"""
import json, os
from lib_elementor import *

BASE = "https://newtree.cat/wp-content/uploads/"
HERO_IMG = {"url": BASE + "2020/04/f3.jpg", "id": ""}
MAIL = "mailto:info@newtree.cat"


def img(path, label=None):
    """Imagen real del sitio actual; sin path -> placeholder descriptivo."""
    if path:
        return {"url": BASE + path, "id": ""}
    return ph(label or "Foto", 900, 650, bg="c9d9c2", fg="1e2a22")


# ---------------------------------------------------------------
# Contenido por página (textos tal cual de la web actual)
# ---------------------------------------------------------------
PAGES = [
    dict(
        file="disseny-i-construccio-de-jardins", title="Disseny i Construcció de Jardins",
        h1="Disseny i construcció de <span style=\"color:%s\">jardins</span>" % GREEN,
        lead="Disseny i creació de jardins a mida.",
        paras=[
            "Us oferim un servei de disseny i creació de jardins a mida, per adaptar-nos a les vostres necessitats i poder-vos oferir un servei totalment personalitzat.",
            "Cada racó té les seves pròpies característiques: l'objectiu és dissenyar el jardí intentant ressaltar els seus punts forts.",
            "Això vol dir tenir en compte tres conceptes importants: proporció, unitat i línies geomètriques.",
            "La proporció es refereix sobretot a la mida del que volem plantar, ha de ser proporcionat.",
            "Els elements naturals també contribueixen a aquesta funció: els arbres que es desenvolupen horitzontalment donen una sensació de tranquil·litat; els verticals, en canvi, donen una sensació d'ordre i dinamisme.",
        ],
        side=img("2021/08/Disseny-de-jardins.jpg"),
        list_title="Tres conceptes clau", list_icon="check-circle",
        items=[("Proporció", "La mida del que plantem ha de ser proporcionada."),
               ("Unitat", ""), ("Línies geomètriques", "")],
        gallery=["2021/08/Disseny-de-jardins2.jpg", "2021/08/Disseny-de-jardins3.jpg",
                 "2021/07/gespa-artificial-6.jpeg"],
    ),
    dict(
        file="sistemes-de-reg", title="Sistemes de Reg",
        h1="Sistemes de <span style=\"color:%s\">reg</span>" % GREEN,
        lead="Els podem assessorar en quin és el millor sistema de reg automàtic.",
        paras=[
            "El reg automàtic distribueix artificialment l'aigua necessària per al desenvolupament de les plantes, especialment en períodes de calor quan falten pluges.",
            "Oferim serveis de disseny i instal·lació de sistemes de reg automàtic per a terrasses, parcs i jardins de diverses dimensions.",
            "Programables i que funcionen de forma independent, els sistemes de reg automàtic són l'elecció perfecta per a aquells que volen regar el seu jardí en el moment que volen.",
        ],
        side=img("2020/04/2.png"),
        list_title="Reg automàtic", list_icon="tint",
        items=[("Disseny", "Per a terrasses, parcs i jardins de diverses dimensions"),
               ("Instal·lació", "Sistemes de reg automàtic"),
               ("Programables", "Funcionen de forma independent")],
        gallery=[],
    ),
    dict(
        file="installacio-de-gespa", title="Instal·lació de Gespa",
        h1="Instal·lació de <span style=\"color:%s\">gespa</span>" % GREEN,
        lead="Instal·lació de gespa natural i artificial.",
        paras=[
            "La gespa és una de les parts més importants de qualsevol jardí i la primera impressió. Més enllà de l'aspecte estètic, ofereix un espai adequat perquè hi juguin els infants i les mascotes.",
            "Gràcies als avenços tecnològics, és possible disposar de gespa natural o gespa artificial de molt bona qualitat.",
            "Us recomanem demanar assessorament professional per triar entre gespa artificial o natural, ja que la decisió depèn de les circumstàncies de cada cas. Us expliquem els avantatges de cada opció.",
        ],
        side=img("2021/07/gespa-artificial-6.jpeg"),
        list_title="Natural o artificial", list_icon="leaf",
        items=[("Gespa natural", "Avantatges segons cada cas"),
               ("Gespa artificial", "De molt bona qualitat")],
        gallery=["2021/07/gespa-artificial-3.jpeg", "2021/07/gespa-artificial-4.jpeg",
                 "2021/07/gespa-artificial-5.jpeg"],
    ),
    dict(
        file="manteniment-de-jardins", title="Manteniment de Jardins",
        h1="Manteniment de <span style=\"color:%s\">jardins</span>" % GREEN,
        lead="Manteniment de jardins dels experts.",
        paras=[
            "Els serveis de jardineria ofereixen un toc professional. Durant les estacions càlides, les plantes floreixen i embelleixen la propietat, però el manteniment pot resultar complicat. Us oferim assistència especialitzada.",
            "Podem arreglar vores de jardí descuidades, podar arbres, treure flors mortes, escampar fertilitzants, fer el manteniment de gespa i us assessorarem de quines accions són les millors en cada moment.",
            "New Tree ofereix un manteniment expert per garantir que el jardí de casa tingui una vista impressionant.",
        ],
        side=img("2021/08/mantenimet.jpg"),
        list_title="Què inclou", list_icon="check",
        items=[("Control de males herbes invasives", ""), ("Prevenció de sòls compactats", ""),
               ("Serveis de cobertura", ""), ("Serveis de reg", ""),
               ("Prevenció de danys per neu o gel", "")],
        gallery=[],
    ),
    dict(
        file="jardins-verticals", title="Jardins Verticals",
        h1="Jardins <span style=\"color:%s\">verticals</span>" % GREEN,
        lead="Una nova tendència per a interiors i exteriors.",
        paras=[
            "Una nova tendència són els jardins verticals: podeu donar un ambient diferent i acollidor tant en interior com en exteriors, restaurants, sales d'espera, escoles, empreses… Oferim infinitat de dissenys amb nombrosos beneficis a nivell econòmic, ecològic i social.",
            "Una façana vegetal ajuda a purificar l'aire, reduir la temperatura ambient, regular la temperatura i promou la biodiversitat a la ciutat. Els jardins verticals formen part de la construcció bioclimàtica. I, a més, la gent és més feliç en un entorn verd que en un entorn gris.",
        ],
        side=img("2021/08/vertical-jpg.jpeg"),
        list_title="Beneficis", list_icon="seedling",
        items=[("Purifica l'aire", ""), ("Redueix i regula la temperatura", ""),
               ("Promou la biodiversitat", ""), ("Construcció bioclimàtica", "")],
        gallery=["2021/08/vertical.jpg", "2021/08/vertical-j.jpg"],
    ),
    dict(
        file="terres-i-substrats", title="Terres i Substrats",
        h1="Terres i <span style=\"color:%s\">substrats</span>" % GREEN,
        lead="El sòl, essencial per a jardins sostenibles.",
        paras=[
            "L'ús de pràctiques de jardineria sostenibles pot ajudar-nos a restaurar els beneficis que brinden els nostres sòls. Recomanem fer aportacions de terra en format de sacs, box o camions.",
            "Respecte a la grava, funciona molt bé com a coberta en parterres o simplement per decorar parts d'un jardí. Millora el drenatge, manté la temperatura i airea el sòl, cosa que protegeix les arrels de les plantes.",
        ],
        side=img("2021/08/terres.jpeg"),
        list_title="Formats d'aportació", list_icon="box",
        items=[("Sacs", ""), ("Box", ""), ("Camions", "")],
        gallery=["2021/08/terres-4.jpeg", "2021/08/terres-5.jpeg", "2021/08/terres3.jpeg",
                 "2021/08/terres-saca.jpeg", "2021/08/GRAVA.jpeg"],
    ),
    dict(
        file="nateja-parceles", title="Neteja de Parcel·les",
        h1="Neteja de <span style=\"color:%s\">parcel·les</span>" % GREEN,
        lead="Oferim el servei de neteja de parcel·les.",
        paras=["Oferim el servei de neteja de parcel·les. Contacteu-nos i us farem arribar un pressupost."],
        side=img("2021/08/neteja-de-parcelles-1.jpeg"),
        list_title=None, list_icon=None, items=[],
        gallery=["2021/08/neteja-de-parcelles-1-1.jpeg"],
    ),
    dict(
        file="tanques-murs", title="Tanques i Murs de Contenció",
        h1="Tanques i murs de <span style=\"color:%s\">contenció</span>" % GREEN,
        lead="Totalment adaptats a l'entorn.",
        paras=[
            "Fem tot tipus de tanques, tant metàl·liques com de fusta, totalment adaptades a l'entorn per minimitzar l'impacte visual.",
            "Murs de contenció per anivellar terrenys.",
        ],
        side=img("2021/08/tancaments.jpeg"),
        list_title="Què fem", list_icon="check",
        items=[("Tanques metàl·liques", ""), ("Tanques de fusta", ""),
               ("Murs de contenció", "Per anivellar terrenys")],
        gallery=["2021/08/tancaments-2.jpeg", "2021/08/mur-de-contenci%C3%B3.jpeg"],
    ),
    dict(
        file="podes", title="Podes",
        h1="Servei de <span style=\"color:%s\">podes</span>" % GREEN,
        lead="Per allargar la vida dels arbres.",
        paras=[
            "La poda d'arbres és fonamental, si es realitza correctament, per allargar-ne la vida; ara bé, s'ha de fer només si és necessari.",
        ],
        side=img("2020/04/Poda.jpg"),
        list_title="Objectius de la poda", list_icon="check",
        items=[("Desenvolupament correcte", "Millora de la salut i l'estructura dels arbres"),
               ("Adequar l'arbre a l'espai", "On es desenvolupa"),
               ("Evitar la caiguda de branques", "Que podrien fer mal a les persones o als béns"),
               ("Evitar afectacions", "Al pas de vianants, vehicles i senyals viàries"),
               ("Reequilibrar", "Arbres o copes mal formades"),
               ("Evitar malalties", "Que no s'estenguin")],
        gallery=["2020/04/19.png", "2020/04/20.png"],
    ),
]

# Obra pública (a newtree.cat vive en /jardineria-2/) — hub con enlaces a los servicios
OBRA_PUBLICA = dict(
    file="obra-publica", title="Obra Pública",
    h1="Obra <span style=\"color:%s\">pública</span>" % GREEN,
    lead="Més de 50 anys d'experiència.",
    paras=["Molts ajuntaments confien en New Tree a l'hora de fer la seva obra pública. Amb més de 50 anys d'experiència, oferim les millors solucions per a cada cas."],
    side=img(None, "Foto obra pública"),
    list_title=None, list_icon=None, items=[],
    gallery=[],
    hub=[("Disseny i Construcció de Jardins", "disseny-i-construccio-de-jardins"),
         ("Sistemes de Reg", "sistemes-de-reg"),
         ("Instal·lació de Gespa", "instal%c2%b7lacio-de-gespa"),
         ("Manteniment de Jardins", "manteniment-de-jardins"),
         ("Jardins Verticals", "jardins-verticals"),
         ("Terres i Substrats", "terres-i-substrats"),
         ("Neteja de Parcel·les", "nateja-parceles"),
         ("Tanques i Murs", "tanques-murs"),
         ("Podes", "podes")],
)


# ---------------------------------------------------------------
# Secciones
# ---------------------------------------------------------------
def eyebrow(t, color=RED):
    return heading(t, size="p", color=color, font_size=13,
                   extra={"typography_typography": "custom", "typography_font_weight": "600",
                          "letter_spacing": {"unit": "px", "size": 2, "sizes": []}})


def hero_section(p):
    inner = col(settings={"width": {"unit": "%", "size": 60}}, gap="20", elements=[
        eyebrow("NEW TREE · JARDINERIA", color=WHITE),
        heading(p["h1"], size="h1", color=WHITE, font_size=48),
        text(p["lead"], color="#E5E5E5", font_size=18),
        row(elements=[button("DEMANA PRESSUPOST", bg=GREEN, link=MAIL)], gap="16"),
    ])
    return section(settings={
        "background_background": "classic", "background_image": HERO_IMG,
        "background_position": "center center", "background_size": "cover",
        "background_overlay_background": "classic", "background_overlay_color": "rgba(10,20,15,0.55)",
        "padding": pad(120, 40, 120, 40), "min_height": {"unit": "px", "size": 420, "sizes": []},
    }, elements=[inner])


def intro_section(p):
    left = col(settings={"width": {"unit": "%", "size": 50}}, gap="18", elements=[
        eyebrow(p["title"].upper()),
        heading("New Tree convertim un desert en un jardí", size="h2", font_size=30),
    ] + [text(t, font_size=16) for t in p["paras"]])
    right = C({"content_width": "full", "width": {"unit": "%", "size": 45}}, [image(p["side"], alt=p["title"])])
    return section(settings={"background_background": "classic", "background_color": WHITE,
                             "padding": pad(80, 40, 80, 40)},
                   elements=[row(elements=[left, right], gap="40", justify="space-between",
                                 align="flex-start")])


def list_section(p):
    boxes = [icon_box(p["list_icon"], t, d, position="left") for t, d in p["items"]]
    return section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                             "padding": pad(70, 40, 70, 40)},
                   elements=[heading(p["list_title"], size="h2", font_size=30),
                             row(elements=[C({"content_width": "full", "width": {"unit": "%", "size": 31}}, [b])
                                           for b in boxes], gap="24", justify="flex-start", align="flex-start")])


def gallery_section(p):
    n = len(p["gallery"])
    w = 31.5 if n >= 3 else 48
    cells = [C({"content_width": "full", "width": {"unit": "%", "size": w}}, [image(img(g), alt=p["title"])])
             for g in p["gallery"]]
    return section(settings={"background_background": "classic", "background_color": WHITE,
                             "padding": pad(70, 40, 70, 40)},
                   elements=[heading("Galeria", size="h2", font_size=30),
                             row(elements=cells, gap="24", justify="flex-start", align="flex-start")])


def hub_section(p):
    cards = [C({"content_width": "full", "width": {"unit": "%", "size": 31.5}},
               [button(t, bg=GREEN, link="https://newtree.cat/%s/" % slug)]) for t, slug in p["hub"]]
    return section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                             "padding": pad(70, 40, 70, 40)},
                   elements=[heading("Els nostres serveis", size="h2", font_size=30),
                             row(elements=cards, gap="20", justify="flex-start", align="flex-start")])


def cta_section():
    contact = [("phone", "Truca'ns", "(+34) 972 560 033 · (+34) 607 484 646"),
               ("envelope", "Escriu-nos", "info@newtree.cat"),
               ("map-marker-alt", "Visita'ns", "Camí de Reg de la Vinya s/n, Calabuig – Bàscara, Girona 17483")]
    left = col(settings={"width": {"unit": "%", "size": 45}}, gap="16", elements=[
        heading("Tens un projecte de jardí?", size="h2", color=WHITE, font_size=30),
        text("Parlem-ne i t'ajudem a fer-lo realitat.", color="#D7DED9", font_size=16),
        button("DEMANA PRESSUPOST", bg=GREEN, link=MAIL),
    ])
    right = row(settings={"width": {"unit": "%", "size": 50}},
                elements=[icon_box(i, t, d, icon_color=GREEN, title_color=WHITE, desc_color="#D7DED9",
                                   position="left") for i, t, d in contact],
                gap="20", justify="flex-start", wrap="wrap")
    return section(settings={"background_background": "classic", "background_color": BLACKBG,
                             "padding": pad(70, 40, 70, 40)},
                   elements=[row(elements=[left, right], justify="space-between", align="center")])


def build(p):
    secs = [hero_section(p), intro_section(p)]
    if p["items"]:
        secs.append(list_section(p))
    if p["gallery"]:
        secs.append(gallery_section(p))
    if p.get("hub"):
        secs.append(hub_section(p))
    secs.append(cta_section())
    return {"content": secs, "page_settings": [], "version": "0.4",
            "title": p["title"] + " - New Tree", "type": "page"}


if __name__ == "__main__":
    out_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "servicios")
    os.makedirs(out_dir, exist_ok=True)
    for p in PAGES + [OBRA_PUBLICA]:
        path = os.path.join(out_dir, p["file"] + ".json")
        with open(path, "w", encoding="utf-8") as f:
            json.dump(build(p), f, ensure_ascii=False, indent=2)
        with open(path, encoding="utf-8") as f:
            n = len(json.load(f)["content"])
        print(f"{p['file']}.json ok ({n} secciones)")
