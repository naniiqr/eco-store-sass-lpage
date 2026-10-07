"""Regenera todo y deja cada plantilla lista para importar en ../importar/ (con Nunito fijada).

Uso: python3 build_all.py
"""
import json, os, runpy, shutil

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
OUT = os.path.join(ROOT, "importar")
FONT = "Nunito"

# (archivo origen relativo a elementor-templates, nombre final)
FILES = [
    ("header.json", "00-header.json"),
    ("footer.json", "00-footer.json"),
    ("inici-home.json", "01-inici.json"),
    ("paginas/empresa.json", "02-empresa.json"),
    ("jardineria.json", "03-jardineria.json"),
    ("servicios/disseny-i-construccio-de-jardins.json", "04-disseny-i-construccio-de-jardins.json"),
    ("servicios/sistemes-de-reg.json", "05-sistemes-de-reg.json"),
    ("servicios/installacio-de-gespa.json", "06-installacio-de-gespa.json"),
    ("servicios/manteniment-de-jardins.json", "07-manteniment-de-jardins.json"),
    ("servicios/jardins-verticals.json", "08-jardins-verticals.json"),
    ("servicios/terres-i-substrats.json", "09-terres-i-substrats.json"),
    ("servicios/nateja-parceles.json", "10-nateja-parceles.json"),
    ("servicios/tanques-murs.json", "11-tanques-murs.json"),
    ("servicios/podes.json", "12-podes.json"),
    ("servicios/obra-publica.json", "13-obra-publica.json"),
    ("paginas/galeria.json", "14-galeria.json"),
    ("paginas/plantes-exemplars.json", "15-plantes-exemplars.json"),
    ("paginas/situacio-i-contacte.json", "16-situacio-i-contacte.json"),
]

# prefijo de los controles de tipografía por widget
TYPO = {"heading": [""], "text-editor": [""], "button": [""],
        "icon-box": ["title_", "description_"]}


def set_font(node):
    if isinstance(node, dict):
        prefixes = TYPO.get(node.get("widgetType")) if node.get("elType") == "widget" else None
        if prefixes:
            for p in prefixes:
                node["settings"][p + "typography_typography"] = "custom"
                node["settings"][p + "typography_font_family"] = FONT
        for v in node.values():
            set_font(v)
    elif isinstance(node, list):
        for v in node:
            set_font(v)


def main():
    for gen in ("build_inici.py", "build_header_footer.py", "build_jardineria.py",
                "build_servicios.py", "build_paginas.py"):
        runpy.run_path(os.path.join(HERE, gen), run_name="__main__")
    if os.path.isdir(OUT):
        shutil.rmtree(OUT)
    os.makedirs(OUT)
    for src, dst in FILES:
        with open(os.path.join(ROOT, src), encoding="utf-8") as f:
            data = json.load(f)
        set_font(data["content"])
        assert data["content"] and data.get("type"), src
        with open(os.path.join(OUT, dst), "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"\n{len(FILES)} plantillas listas en importar/")


if __name__ == "__main__":
    main()
