"""Páginas de servicio con el TEXTO LITERAL de newtree.cat (solo se corrigen erratas tipográficas)
dentro del diseño del rediseño (mismos colores, hero, tarjetas y banner del PDF).

Uso: python3 build_servicios.py   (escribe en ../servicios/)
"""
import json, os
from design import *

HERO_IMG = real("2020/04/f3.jpg")


def img(path, label=None):
    if path:
        return {"url": BASE + path, "id": ""}
    return ph(label or "Foto", 900, 650, bg="c9d9c2", fg="1e2a22")


def h1_green(title):
    """Título original con la última palabra en verde."""
    head, _, last = title.rpartition(" ")
    return (head + " " if head else "") + '<span style="color:%s">%s</span>' % (GREEN_ACCENT, last)


# ---------------------------------------------------------------
# Contenido: texto original de cada página
# ---------------------------------------------------------------
PAGES = [
    dict(file="disseny-i-construccio-de-jardins", title="Disseny i Construcció de Jardins",
         paras=[
             "Us oferim un servei de disseny i creació de jardins a mida, per adaptar-nos a les vostres necessitats i poder-vos oferir un servei totalment personalitzat.",
             "Cada racó té les seves pròpies característiques: l'objectiu és dissenyar el jardí intentant ressaltar els seus punts forts.",
             "Això vol dir tenir en compte tres conceptes importants: proporció, unitat i línies geomètriques.",
             "La proporció es refereix sobretot a la mida del que volem plantar, ha de ser proporcionat. Mai inserir plantes que siguin massa petites o massa grans.",
             "Els elements naturals també contribueixen a aquesta funció: els arbres que es desenvolupen horitzontalment donen una sensació de tranquil·litat; els verticals, en canvi, donen una sensació d'ordre i dinamisme.",
         ],
         side=img("2021/08/Disseny-de-jardins.jpg"),
         list_title="Tres conceptes importants", list_icon="check-circle",
         items=[("Proporció", ""), ("Unitat", ""), ("Línies geomètriques", "")],
         gallery=["2021/08/Disseny-de-jardins2.jpg", "2021/08/Disseny-de-jardins3.jpg",
                  "2021/07/gespa-artificial-6.jpeg", "2021/07/gespa-artificial-3.jpeg",
                  "2020/04/11.png", "2020/04/16.png"]),
    dict(file="sistemes-de-reg", title="Sistemes de Reg",
         paras=[
             "Els podem assessorar en quin és el millor sistema de reg automàtic.",
             "El reg automàtic permet la distribució artificial d'aigua a les plantes, la qual cosa és necessari per al seu desenvolupament, especialment en els períodes més calorosos, quan les pluges no són prou freqüents. A New Tree ens encarreguem de dissenyar i instal·lar sistemes de reg automàtic, terrasses, parcs i jardins de qualsevol mida.",
             "Programables i que funcionen de forma independent, els sistemes de reg automàtic són l'elecció perfecta per a aquells que volen regar el seu jardí en el moment que volen, fins i tot quan no són a casa. Hi ha diverses solucions molt pràctiques que et permetran tenir el teu propi sistema sense alterar l'estructura de jardí. Els nostres professionals sempre us assessoraran de la millor manera, proporcionant la realització de sistemes de reg automàtic.",
         ],
         side=img("2020/04/2.png"), list_title=None, items=[], gallery=[]),
    dict(file="installacio-de-gespa", title="Instal·lació de gespa natural i artificial",
         paras=[
             "Com a imatge clàssica de qualsevol casa, la gespa és una de les parts més importants de qualsevol jardí i la primera impressió. A part de l'estètica visual, la gespa serveix com un espai ideal perquè juguin els nens i les mascotes.",
             "Gràcies als avenços tecnològics, tenim l'opció de tenir una gespa natural o gespa artificial de molt bona qualitat.",
             "Prendre la decisió entre una gespa artificial o gespa natural per a molts propietaris necessita assessorament de professionals per decidir quina opció és la més adient en cada cas. Per ajudar-lo a decidir quin és millor per a vostè, li podrem dir els avantatges en cada cas.",
         ],
         side=img("2021/07/gespa-artificial-6.jpeg"), list_title=None, items=[],
         gallery=["2021/07/gespa-artificial-3.jpeg", "2021/07/gespa-artificial-4.jpeg",
                  "2021/07/gespa-artificial-5.jpeg", "2020/04/12.png", "2020/04/13.png", "2020/04/14.png"]),
    dict(file="manteniment-de-jardins", title="Manteniment de jardins",
         paras=[
             "Una de les millors formes de donar-li a la seva propietat un toc professional és amb els serveis de jardineria. Durant la primavera i l'estiu, les flors fragants i saludables faran que la seva propietat sigui encara més agradable i atractiva. Potser ja tingui excel·lents flors, però de vegades el manteniment de jardí és més fàcil de dir que de fer. New Tree són aquí per ajudar.",
         ],
         side=img("2021/08/mantenimet.jpg"),
         list_title="Manteniment de jardins dels experts", list_icon="check",
         items=[("Control de males herbes invasives", ""), ("Prevenció de sòls compactats", ""),
                ("Serveis de cobertura", ""), ("Serveis de reg", ""),
                ("Prevenció de danys per neu o gel…", "")],
         after=["Podem arreglar vores de jardí descuidats, podar arbres, flors mortes, escampar fertilitzants, manteniment de gespa i donarem assessorament de quines accions són les millors en cada moment.",
                "New Tree ofereix un manteniment expert per garantir que el jardí de casa tingui una vista impressionant."],
         gallery=["2020/04/11.png"]),
    dict(file="jardins-verticals", title="Jardins verticals",
         paras=[
             "Una nova tendència són els jardins verticals, pots donar un ambient diferent i acollidor tant en interior com exteriors, restaurants, sales d'espera, escoles, empreses… Oferim infinits dissenys amb nombrosos beneficis a nivell econòmic, ecològic i social.",
             "Una façana vegetal ajuda a purificar l'aire, reduir la temperatura ambient, regular la temperatura i promou la biodiversitat a la ciutat. Els jardins verticals formen part de la construcció bioclimàtica. I, és més, la gent és més feliç en un entorn verd que en un entorn gris.",
         ],
         side=img("2021/08/vertical-jpg.jpeg"),
         list_title="Beneficis", list_icon="seedling",
         items=[("Purifica l'aire", ""), ("Redueix la temperatura ambient", ""),
                ("Regula la temperatura", ""), ("Promou la biodiversitat a la ciutat", "")],
         gallery=["2020/04/5.png", "2021/08/vertical.jpg", "2021/08/vertical-j.jpg"]),
    dict(file="terres-i-substrats", title="Terres i substrats",
         paras=[
             "El sòl és fonamental per a l'èxit dels jardins sostenibles i proporciona importants beneficis ambientals. L'ús de pràctiques de jardineria sostenibles pot ajudar-nos a restaurar els beneficis que brinden els nostres sòls i és molt recomanable fer aportacions de terra, tant podem servir en format de sacs com amb box o camions.",
             "La grava funciona molt bé com coberta de la taulada en parterres o tan sols per decorar parts d'un jardí. A més d'ajudar el drenatge de l'aigua, mantenen la temperatura de la terra i contribueixen que estigui ben airejat. Això esmorteeix l'efecte de les altes temperatures i ajuda a protegir les arrels de les plantes.",
         ],
         side=img("2021/08/terres.jpeg"),
         list_title="Aportacions de terra", list_icon="box",
         items=[("Sacs", ""), ("Box", ""), ("Camions", "")],
         gallery=["2021/08/terres-4.jpeg", "2021/08/terres-5.jpeg", "2021/08/terres-.jpeg",
                  "2021/08/terres3.jpeg", "2021/08/terres-saca.jpeg", "2021/08/GRAVA.jpeg"]),
    dict(file="nateja-parceles", title="Neteja de parcel·les",
         paras=["Oferim el servei de neteja de parcel·les."],
         side=img("2021/08/neteja-de-parcelles-1.jpeg"), list_title=None, items=[],
         gallery=["2021/08/neteja-de-parcelles-1-1.jpeg"]),
    dict(file="tanques-murs", title="Tanques i murs de contenció",
         paras=["Fem tot tipus de tanques, tant les metàl·liques o de fusta totalment adaptades a l'entorn per minimitzar l'impacte visual.",
                "Murs de contenció per anivellar terrenys."],
         side=img("2021/08/tancaments.jpeg"),
         list_title=None, items=[],
         gallery=["2021/08/tancaments-2.jpeg", "2021/08/mur-de-contencio%CC%81.jpeg"]),
    dict(file="podes", title="Servei de podes",
         paras=["La poda d'arbres és fonamental, si es realitza correctament, per allargar la vida dels mateixos, ara bé s'ha de fer només si és necessari."],
         side=img("2020/04/Poda.jpg"),
         list_title="Objectius de la poda d'arbres", list_icon="check",
         items=[("Mantenir un desenvolupament correcte dels arbres, millora de la seva salut i estructura.", ""),
                ("Adequar l'arbre a l'espai on es desenvolupa.", ""),
                ("Evitar la caiguda de branques que podrien fer mal a les persones o els béns, i descarregar de pes el brancatge.", ""),
                ("Evitar que el brancatge afecti el pas de vianants, vehicles, senyals viàries…", ""),
                ("Reequilibrar els arbres o les copes mal formades, millorant la seva bellesa.", ""),
                ("Evitar que s'estenguin les malalties.", "")],
         gallery=["2020/04/19.png", "2020/04/20.png"]),
]

# Obra pública (a newtree.cat vive en /jardineria-2/)
OBRA_PUBLICA = dict(
    file="obra-publica", title="Obra pública",
    paras=["Molts ajuntaments confien amb New Tree a l'hora de fer la seva obra pública, New Tree, amb més de 50 anys d'experiència, oferim les millors solucions per cada cas."],
    side=img("2021/08/obra-publica-jardins.jpeg"), list_title=None, items=[],
    gallery=["2020/04/Obra-publica.jpg"],
    hub=[("Disseny i Construcció de Jardins", "disseny-i-construccio-de-jardins"),
         ("Sistemes de Reg", "sistemes-de-reg"),
         ("Instal·lació de Gespa", "instal%c2%b7lacio-de-gespa"),
         ("Manteniment de jardins", "manteniment-de-jardins"),
         ("Jardins verticals", "jardins-verticals"),
         ("Terres i substrats", "terres-i-substrats"),
         ("Nateja Parcel·les", "nateja-parceles"),
         ("Tanques i Murs", "tanques-murs"),
         ("Podes", "podes")],
)


# ---------------------------------------------------------------
# Secciones (identidad del rediseño: ver design.py)
# ---------------------------------------------------------------
def acc_last(title, color=RED):
    head, _, last = title.rpartition(" ")
    return acc(head, last, color) if head else '<span style="color:%s">%s</span>' % (color, last)


def hero_section(p):
    h1 = p.get("h1") or h1_green(p["title"])
    return hero("NEW TREE · JARDINERIA", h1, p.get("lead", SLOGAN), HERO_IMG, min_h=460)


def intro_section(p):
    paras = p["paras"]
    left = col(settings={"width": {"unit": "%", "size": 50}}, gap="18",
               elements=[text(paras[0], color=TEXT_DARK, font_size=20)] + [text(t, font_size=16) for t in paras[1:]] +
                        [button("DEMANA PRESSUPOST", bg=RED, color=WHITE, link=MAIL)])
    right = C({"content_width": "full", "width": {"unit": "%", "size": 45}},
              [pic(p["side"], p["title"], radius=12, height=480, shadow=True)])
    return section(settings={"background_background": "classic", "background_color": WHITE,
                             "padding": pad(80, 40, 80, 40)},
                   elements=[row(elements=[left, right], gap="40", justify="space-between", align="flex-start")])


def list_section(p):
    boxes = [C({"content_width": "full", "width": {"unit": "%", "size": 31}},
               [ibox(p["list_icon"], t, d, icon_color=WHITE, title_color=WHITE, desc_color=SOFT, framed=True,
                     title_px=17, desc_px=14)]) for t, d in p["items"]]
    els = [heading(acc_last(p["list_title"]).replace('color:%s' % RED, 'color:%s' % RED), size="h2", color=WHITE, font_size=34),
           row(elements=boxes, gap="28", justify="center", align="flex-start")]
    els += [text(t, color=SOFT, font_size=17) for t in p.get("after", [])]
    return section(settings={"background_background": "gradient", "background_color": DARKGREEN,
                             "background_color_b": DARKGREEN2, "background_gradient_type": "linear",
                             "background_gradient_angle": {"unit": "deg", "size": 135, "sizes": []},
                             "flex_gap": {"column": "36", "row": "36", "unit": "px", "isLinked": True},
                             "padding": pad(80, 40, 80, 40)}, elements=els)


def gallery_section(p):
    n = len(p["gallery"])
    w, h = (31, 240) if n >= 3 else ((48, 320) if n == 2 else (100, 380))
    cells = [C({"content_width": "full", "width": {"unit": "%", "size": w}},
               [pic(img(g), p["title"], radius=10, height=h)]) for g in p["gallery"]]
    return section(settings={"background_background": "classic", "background_color": LIGHTGRAY_BG,
                             "padding": pad(70, 40, 70, 40)},
                   elements=[row(elements=cells, gap="22", justify="center", align="flex-start")])


def hub_section(p):
    cards = [C({"content_width": "full", "width": {"unit": "%", "size": 31}},
               [button(t, bg=GREEN, link=SITE + "%s/" % slug, full=True)]) for t, slug in p["hub"]]
    return section(settings={"background_background": "classic", "background_color": WHITE,
                             "padding": pad(70, 40, 70, 40)},
                   elements=[heading(acc("Els nostres", "serveis"), size="h2", font_size=34),
                             row(elements=cards, gap="20", justify="center", align="flex-start")])


def cta_section():
    return cta_banner()


def build(p):
    secs = [hero_section(p), features_strip(), intro_section(p)]
    if p["items"]:
        secs.append(list_section(p))
    if p["gallery"]:
        secs.append(gallery_section(p))
    if p.get("hub"):
        secs.append(hub_section(p))
    secs.append(cta_banner())
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
            print(f"{p['file']}.json ok ({len(json.load(f)['content'])} secciones)")
