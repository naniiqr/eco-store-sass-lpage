"""Componentes de diseño compartidos (identidad del rediseño, según el PDF).
Hero con foto y rótulo manuscrito, franja de iconos, tarjetas con foto y degradado,
bloques verde oscuro con iconos en círculo, banner final con eslogan manuscrito.
"""
from lib_elementor import *

BASE = "https://newtree.cat/wp-content/uploads/"
SCRIPT = "Caveat"
SITE = "https://newtree.cat/"
GALERIA = SITE + "galeria/"
CONTACT = SITE + "situacio-i-contacte/"   # /pressupost/ está protegida con contraseña
MAIL = CONTACT
SLOGAN = "New Tree convertim un desert en un jardí"
PHONES = "(+34) 972 560 033 · (+34) 607 484 646"
ADDRESS = "Camí de Reg de la Vinya s/n, Calabuig – Bàscara, Girona 17483"
SOFT = "#D9DFDA"


def R(r):
    return {"unit": "px", "top": str(r), "right": str(r), "bottom": str(r), "left": str(r), "isLinked": True}


def SH(y=18, blur=40, a=0.18):
    return {"horizontal": 0, "vertical": y, "blur": blur, "spread": 0, "color": f"rgba(27,39,29,{a})"}


def acc(before, accent, color=RED):
    return f'{before} <span style="color:{color}">{accent}</span>'


def real(path):
    return {"url": BASE + path, "id": ""}


def eyebrow(t, color=RED):
    return heading(t, size="p", color=color, font_size=13,
                   extra={"typography_typography": "custom", "typography_font_weight": "600",
                          "letter_spacing": {"unit": "px", "size": 2, "sizes": []}})


def script(lines, size=34, color=WHITE, align="right"):
    return heading("<br>".join(lines), size="p", align=align, color=color, font_size=size,
                   extra={"typography_typography": "custom", "typography_font_family": SCRIPT,
                          "typography_font_style": "italic", "typography_font_weight": "600"})


def brush(align="flex-end"):
    return C({"content_width": "full", "width": {"unit": "px", "size": 90, "sizes": []},
              "height": {"unit": "px", "size": 4, "sizes": []}, "background_background": "classic",
              "background_color": GREEN, "border_radius": R(4)}, [])


def pic(img, alt="", radius=10, height=None, shadow=False):
    s = {"image": img, "image_size": "large", "alt": alt, "image_border_radius": R(radius)}
    if height:
        s["height"] = {"unit": "px", "size": height, "sizes": []}
        s["object-fit"] = "cover"
    if shadow:
        s["image_box_shadow_box_shadow_type"] = "yes"
        s["image_box_shadow_box_shadow"] = SH()
    return W("image", s)


def ibox(ic, title, desc="", icon_color=GREEN, title_color=TEXT_DARK, desc_color=TEXT_GRAY, position="left",
         framed=False, title_px=18, desc_px=14, icon_px=26):
    w = icon_box(ic, title, desc, icon_color=icon_color, title_color=title_color, desc_color=desc_color,
                 position=position)
    s = w["settings"]
    s["icon_size"] = {"unit": "px", "size": icon_px, "sizes": []}
    s["title_typography_font_size"] = {"unit": "px", "size": title_px, "sizes": []}
    s["description_typography_font_size"] = {"unit": "px", "size": desc_px, "sizes": []}
    if framed:
        s.update({"view": "framed", "shape": "circle", "icon_padding": {"unit": "px", "size": 12, "sizes": []}})
    return w


GRAD_SIDE = {"background_overlay_background": "gradient", "background_overlay_color": "rgba(14,20,12,0.80)",
             "background_overlay_color_b": "rgba(14,20,12,0.18)",
             "background_overlay_gradient_type": "linear",
             "background_overlay_gradient_angle": {"unit": "deg", "size": 90, "sizes": []}}
GRAD_UP = {"background_overlay_background": "gradient", "background_overlay_color": "rgba(14,20,12,0.0)",
           "background_overlay_color_b": "rgba(14,20,12,0.78)",
           "background_overlay_gradient_type": "linear",
           "background_overlay_gradient_angle": {"unit": "deg", "size": 180, "sizes": []}}


def hero(eyebrow_txt, h1, lead_txt, bg, decor=True, min_h=540, buttons=True):
    btns = [button("DEMANA PRESSUPOST", bg=GREEN, color=WHITE, link=MAIL),
            button("VEURE PROJECTES", border=WHITE, link=GALERIA)]
    left = col(settings={"width": {"unit": "%", "size": 62}}, gap="22", elements=[
        eyebrow(eyebrow_txt, WHITE),
        heading(h1, size="h1", color=WHITE, font_size=56),
        text(lead_txt, color="#E5E5E5", font_size=18),
    ] + ([row(elements=btns, gap="16", justify="flex-start")] if buttons else []))
    els = [left]
    if decor:
        els.append(col(settings={"width": {"unit": "%", "size": 28}, "hide_tablet": "hidden-tablet",
                                 "hide_mobile": "hidden-mobile"}, align="flex-end", gap="10",
                       elements=[script(["Natura", "Benestar", "Vida"], 38), brush()]))
    s = {"background_background": "classic", "background_image": bg, "background_position": "center center",
         "background_size": "cover", "padding": pad(120, 40, 120, 40),
         "min_height": {"unit": "px", "size": min_h, "sizes": []}}
    s.update(GRAD_SIDE)
    return section(settings=s, elements=[row(elements=els, gap="24", justify="space-between", align="center")])


FEATURES = [("seedling", "Disseny personalitzat", "Projectes únics i a mida"),
            ("recycle", "Solucions sostenibles", "Respecte pel medi ambient"),
            ("tint", "Estalvi d'aigua", "Espais més eficients"),
            ("award", "Més de 50 anys d'experiència", "Confiança i resultats"),
            ("handshake", "Acompanyament integral", "De la idea a la realitat")]


def features_strip():
    return section(
        settings={"background_background": "classic", "background_color": WHITE, "padding": pad(30, 40, 30, 40),
                  "border_border": "solid", "border_color": "#E5E7EB",
                  "border_width": {"unit": "px", "top": "0", "right": "0", "bottom": "1", "left": "0",
                                   "isLinked": False}},
        elements=[row(elements=[ibox(i, t, d, title_px=15, desc_px=12, icon_px=28) for i, t, d in FEATURES],
                      gap="24", justify="space-between", align="center")])


def service_card(title, sub, bg):
    content = row(elements=[
        col(gap="4", settings={"width": {"unit": "%", "size": 80}},
            elements=[heading(title, size="h3", color=WHITE, font_size=19, weight="700"),
                      text(sub, color="#E5E5E5", font_size=13)]),
        icon("arrow-right", color=WHITE, size=16)],
        wrap="nowrap", justify="space-between", align="flex-end")
    s = {"content_width": "full", "flex_direction": "column", "flex_justify_content": "flex-end",
         "width": {"unit": "%", "size": 31}, "min_height": {"unit": "px", "size": 270, "sizes": []},
         "background_background": "classic", "background_image": bg, "background_position": "center center",
         "background_size": "cover", "padding": pad(22, 22, 22, 22), "border_radius": R(12)}
    s.update(GRAD_UP)
    return C(s, [content])


def project_card(title, place, bg, w=31):
    return col(settings={"width": {"unit": "%", "size": w}}, gap="10", elements=[
        pic(bg, title, radius=10, height=220),
        row(elements=[col(gap="2", settings={"width": {"unit": "%", "size": 80}},
                          elements=[heading(title, size="h4", font_size=18, weight="700"), text(place, font_size=14)]),
                      icon("arrow-right", color=TEXT_DARK, size=14)],
            wrap="nowrap", justify="space-between", align="center")])


def perks_dark(items, title=None, intro=None, btn=None, bg=DARKGREEN):
    els = []
    if title:
        els.append(heading(title, size="h2", color=WHITE, font_size=32))
    if intro:
        els.append(text(intro, color=SOFT, font_size=16))
    if btn:
        els.append(btn)
    left = col(settings={"width": {"unit": "%", "size": 38}}, gap="20", elements=els) if els else None
    right = row(settings={"width": {"unit": "%", "size": 56 if left else 100}}, gap="24", justify="flex-start",
                align="flex-start",
                elements=[C({"content_width": "full", "width": {"unit": "%", "size": 47}},
                            [ibox(i, t, d, icon_color=WHITE, title_color=WHITE, desc_color=SOFT, framed=True,
                                  title_px=17, desc_px=14)]) for i, t, d in items])
    s = {"background_background": "gradient", "background_color": DARKGREEN, "background_color_b": DARKGREEN2,
         "background_gradient_type": "linear", "background_gradient_angle": {"unit": "deg", "size": 135, "sizes": []},
         "padding": pad(90, 40, 90, 40)}
    return section(settings=s, elements=[row(elements=[x for x in (left, right) if x], gap="40",
                                             justify="space-between", align="center")])


def steps_section(steps):
    def item(n, t, d):
        badge = C({"content_width": "full", "flex_direction": "row", "flex_justify_content": "center",
                   "flex_align_items": "center", "width": {"unit": "px", "size": 52, "sizes": []},
                   "height": {"unit": "px", "size": 52, "sizes": []}, "background_background": "classic",
                   "background_color": GREEN, "border_radius": R(26)},
                  [heading(n, size="p", color=WHITE, font_size=16, weight="700", align="center")])
        return col(settings={"width": {"unit": "%", "size": 21}}, gap="12", elements=[
            badge, heading(t, size="h4", font_size=18, weight="700"), text(d, font_size=14)])
    els = []
    for k, (n, t, d) in enumerate(steps):
        els.append(item(n, t, d))
        if k < len(steps) - 1:
            els.append(C({"content_width": "full", "flex_direction": "row", "flex_justify_content": "center",
                          "flex_align_items": "center", "width": {"unit": "px", "size": 24, "sizes": []}},
                         [icon("arrow-right", color=TEXT_GRAY, size=18)]))
    return section(settings={"background_background": "classic", "background_color": WHITE,
                             "padding": pad(80, 40, 80, 40)},
                   elements=[heading("Com treballem", size="h2", font_size=34),
                             row(elements=els, gap="16", justify="space-between", align="flex-start")])


def cta_banner(title="Tens un projecte de jardí?", sub="Parlem-ne i t'ajudem a fer-lo realitat."):
    contact = [("phone", "Truca'ns", "(+34) 972 560 033"),
               ("whatsapp", "WhatsApp", "Envia'ns un missatge"),
               ("envelope", "Escriu-nos", "info@newtree.cat")]
    left = col(settings={"width": {"unit": "%", "size": 34}}, gap="16", elements=[
        heading(title, size="h2", color=WHITE, font_size=32), text(sub, color=SOFT, font_size=16),
        button("DEMANA PRESSUPOST", bg=GREEN, color=WHITE, link=MAIL)])
    mid = row(settings={"width": {"unit": "%", "size": 42}}, gap="20", justify="flex-start", align="flex-start",
              elements=[ibox("phone", "Truca'ns", "(+34) 972 560 033", WHITE, WHITE, SOFT, "top", title_px=16, desc_px=13, icon_px=24),
                        ibox("envelope", "Escriu-nos", "info@newtree.cat", WHITE, WHITE, SOFT, "top", title_px=16, desc_px=13, icon_px=24)])
    right = col(settings={"width": {"unit": "%", "size": 16}, "hide_tablet": "hidden-tablet",
                          "hide_mobile": "hidden-mobile"}, align="flex-end", gap="8",
                elements=[script(["Fem créixer espais,", "fem créixer persones"], 26), brush()])
    s = {"background_background": "gradient", "background_color": DARKGREEN, "background_color_b": BLACKBG,
         "background_gradient_type": "linear", "background_gradient_angle": {"unit": "deg", "size": 135, "sizes": []},
         "padding": pad(70, 40, 70, 40)}
    return section(settings=s, elements=[row(elements=[left, mid, right], gap="24", justify="space-between",
                                             align="center")])


def page(title, secs):
    return {"content": secs, "page_settings": [], "version": "0.4", "title": title + " - New Tree", "type": "page"}
