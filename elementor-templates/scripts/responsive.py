"""Pasada final de responsive y simetría, aplicada a TODAS las plantillas.

- Márgenes laterales siempre iguales (izquierda = derecha) y más estrechos en tablet/móvil.
- Tablet (<=1024): tarjetas de 2 en 2, columnas grandes apiladas.
- Móvil (<=767): todo en una columna, centrado, con 20px a cada lado.
"""
import copy


def _sym(p, side, vscale=1.0):
    """Padding simétrico: mismo valor a izquierda y derecha."""
    t, b = float(p.get("top") or 0), float(p.get("bottom") or 0)
    return {"unit": "px", "top": str(round(t * vscale)), "right": str(side), "bottom": str(round(b * vscale)),
            "left": str(side), "isLinked": False}


def _walk(node, top, fn_c, fn_w, parent_dir="column"):
    if node.get("elType") == "container":
        fn_c(node, top)
        d = node["settings"].get("flex_direction", "column")
        for e in node.get("elements", []):
            _walk(e, False, fn_c, fn_w, d)
    else:
        fn_w(node, parent_dir)


def _container(c, top):
    s = c["settings"]
    # 1) simetría lateral: si hay padding horizontal, izquierda = derecha
    p = s.get("padding")
    if p:
        side = p.get("left") or p.get("right") or "0"
        s["padding"] = dict(p, left=side, right=side)
        if top and float(side) > 0:
            s["padding_tablet"] = _sym(p, 24, 0.8)
            s["padding_mobile"] = _sym(p, 20, 0.65)
    # 2) anchos: tarjetas 2 por fila en tablet, todo a 100% en móvil
    w = s.get("width") or {}
    if w.get("unit") == "%" and 0 < float(w.get("size", 100)) < 100:
        size = float(w["size"])
        s.setdefault("width_tablet", {"unit": "%", "size": 48 if size <= 35 else 100, "sizes": []})
        s.setdefault("width_mobile", {"unit": "%", "size": 100, "sizes": []})
    elif w.get("unit") == "px" and float(w.get("size", 0)) <= 32:       # flechas decorativas entre pasos
        els = c.get("elements", [])
        if len(els) == 1 and els[0].get("widgetType") == "icon":
            s["hide_tablet"] = "hidden-tablet"
            s["hide_mobile"] = "hidden-mobile"
    # 3) apilar y centrar en móvil
    keep_row = s.pop("_keep_row", False)
    if s.get("flex_direction") == "row" and keep_row:
        s["flex_justify_content_mobile"] = "space-between"
        s["flex_align_items_mobile"] = "center"
    elif s.get("flex_direction") == "row":
        s["flex_direction_mobile"] = "column"
        s["flex_wrap_mobile"] = "wrap"
        s["flex_justify_content_mobile"] = "center"
        s["flex_align_items_mobile"] = "center"
    else:
        s["flex_align_items_mobile"] = "center"
    if s.get("_position") == "absolute":                                 # adornos flotantes
        s["hide_mobile"] = "hidden-mobile"
    if s.get("min_height"):
        base = float(s["min_height"].get("size", 0))
        # los contenedores con foto (tarjetas, hero, bloques) conservan un alto mínimo en móvil
        keep = max(200, round(base * 0.55)) if s.get("background_image") else 0
        s["min_height_mobile"] = {"unit": "px", "size": keep, "sizes": []}
    if s.get("height") and s["height"].get("unit") == "px" and float(s["height"].get("size", 0)) > 60:
        pass


def _widget(w, parent_dir="column"):
    s, t = w["settings"], w["widgetType"]
    # ancho completo solo dentro de columnas; en filas el widget conserva su tamaño natural
    full = {"_element_width": "inherit"} if parent_dir.startswith("column") else {}                                 # ocupa el ancho completo de su contenedor
    if t == "heading":
        s.update(full); s["align_mobile"] = "center"
    elif t == "text-editor":
        s.update(full); s["align_mobile"] = "center"
    elif t == "button":
        s["align_mobile"] = "center"
    elif t == "image":
        s.update(full)
    elif t == "icon-box":
        s["position_mobile"] = "top"; s["text_align_mobile"] = "center"
    elif t == "icon":
        s["align_mobile"] = "center"
    elif t in ("form", "google_maps"):
        s.update(full)
    elif t == "theme-site-logo":
        s["align_mobile"] = "center" if s.get("align") == "center" else "left"


def apply(doc, header_footer=False):
    doc = copy.deepcopy(doc)
    for c in doc["content"]:
        _walk(c, True, _container, _widget)
    if header_footer:
        return doc
    return doc
