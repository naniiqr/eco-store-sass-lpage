"""Página Jardineria (disseny de jardins) con el diseño del PDF. Escribe ../jardineria.json."""
import json, os
from design import *

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))

CHECK = [("search", "Anàlisi de l'espai", "Escoltem les teves necessitats"),
         ("pencil-ruler", "Disseny a mida", "Propostes creatives i funcionals"),
         ("seedling", "Selecció de plantes", "Espècies adaptades al clima"),
         ("cogs", "Execució professional", "Cuidem cada detall"),
         ("heart", "Jardins per gaudir", "Benestar per a tu i el teu entorn")]
PROJECTS = [("Jardí mediterrani", "Figueres"), ("Jardí amb piscina", "Empuriabrava"),
            ("Jardí contemporani", "Peralada"), ("Racó chill out", "Empuriabrava"),
            ("Jardí amb oliveres", "L'Escala"), ("Jardí amb desnivells", "Girona")]
PERKS = [("award", "Experiència i professionalitat", "Fundats l'any 1977"),
         ("drafting-compass", "Projectes personalitzats", "Ens adaptem a tu"),
         ("recycle", "Compromís amb el medi ambient", "Solucions sostenibles"),
         ("heart", "Passió per la natura", "Fem créixer espais, fem créixer persones")]
STEPS = [("01", "Escoltem les teves idees", "Entenem les teves necessitats i l'espai disponible."),
         ("02", "Dissenyem la proposta", "Et presentem un projecte personalitzat."),
         ("03", "Executem el jardí", "Amb un equip expert i materials de qualitat."),
         ("04", "Gaudeixes del resultat", "Un espai verd per viure i compartir.")]

hero_sec = hero("DISSENY DE JARDINS",
                'Dissenyem<br>jardins <span style="color:%s">amb ànima</span>' % GREEN,
                "Espais únics, funcionals i sostenibles que connecten amb la natura i milloren la teva qualitat de vida.",
                ph("Foto hero disseny jardí", 1600, 900, bg="2f4a3a", fg="ffffff"), min_h=560)

# bloque «Molt més que un jardí»: la tarjeta de cita va dentro de la foto, anclada abajo a la derecha
quote = col(settings={"background_background": "classic", "background_color": "rgba(18,35,24,0.88)",
                      "padding": pad(26, 26, 26, 26), "width": {"unit": "%", "size": 62},
                      "_position": "absolute", "_offset_orientation_h": "end", "_offset_x_end": {"unit": "px", "size": 0, "sizes": []},
                      "_offset_orientation_v": "end", "_offset_y_end": {"unit": "px", "size": 0, "sizes": []},
                      "hide_mobile": "hidden-mobile"}, gap="8", elements=[
    script(['"Jardins que', 'milloren vides"'], 34, WHITE, "left"),
    text("Disseny, natura i emoció en equilibri perfecte.", color=SOFT, font_size=14)])
right = C({"content_width": "full", "width": {"unit": "%", "size": 52}, "position": "relative"},
          [pic(ph("Foto jardí disseny detall", 900, 780, bg="2f4a3a", fg="ffffff"), "Disseny de jardins", radius=12), quote])
left = col(settings={"width": {"unit": "%", "size": 42}}, gap="20", elements=[
    eyebrow("DISSENY DE JARDINS"),
    heading(acc("Molt més<br>", "que un jardí"), size="h2", font_size=40),
    text("Dissenyem i construïm jardins que s'adapten al teu espai, al teu estil de vida i a l'entorn. "
         "Cada projecte és únic, combinant estètica, funcionalitat i sostenibilitat per crear espais verds que "
         "perdurin en el temps.", font_size=16),
    col(gap="14", elements=[ibox(i, t, d, framed=True, title_px=17, desc_px=14) for i, t, d in CHECK]),
    button("DEMANA PRESSUPOST", bg=RED, color=WHITE, link=MAIL)])
split = section(settings={"background_background": "classic", "background_color": WHITE, "padding": pad(80, 40, 80, 40)},
                elements=[row(elements=[left, right], gap="40", justify="space-between", align="flex-start")])

projects = section(
    settings={"background_background": "classic", "background_color": LIGHTGRAY_BG, "padding": pad(80, 40, 80, 40)},
    elements=[
        row(elements=[heading(acc("Projectes de", "disseny de jardins"), size="h2", font_size=36),
                      text('<a href="%s" style="color:%s;font-weight:700">VEURE TOTS ELS PROJECTES →</a>' % (GALERIA, TEXT_DARK),
                           font_size=13)], justify="space-between", align="center"),
        row(elements=[project_card(t, p, ph(t, 600, 450, bg="c9d9c2", fg="1e2a22")) for t, p in PROJECTS],
            gap="22", justify="center", align="flex-start")])

trust = perks_dark(PERKS, title="Per què confiar en Newtree?",
                   intro="Som una empresa de jardineria i paisatgisme fundada l'any 1977, amb més de 50 anys "
                         "d'experiència a l'Empordà. Ens apassiona la natura i treballem per crear espais verds que "
                         "generin benestar, bellesa i valor.",
                   btn=button("CONEIX NOSALTRES", bg=GREEN, color=WHITE, link="https://newtree.cat/empresa/"))

doc = page("Jardineria", [hero_sec, features_strip(), split, projects, trust, steps_section(STEPS), cta_banner()])
with open(os.path.join(ROOT, "jardineria.json"), "w", encoding="utf-8") as f:
    json.dump(doc, f, ensure_ascii=False, indent=2)
print("jardineria.json ok (%d secciones)" % len(doc["content"]))
