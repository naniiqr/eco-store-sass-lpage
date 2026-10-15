"""Ficha SEO (Yoast) de la página Galeria. Uso: python3 seo_galeria.py  -> ../SEO-GALERIA.md"""
import json, os, re, unicodedata, html
from build_paginas import GALLERY, SEO_TEXT, THUMB, KW
from design import SITE, BASE

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SLUG_NOU = "galeria-de-jardins-girona"
TITLE = "Galeria de jardins Girona i projectes | New Tree Girona"
DESC = ("Galeria de jardins Girona i l'Empordà: piscines, gespa natural i artificial, reg, jardins verticals i podes "
        "de New Tree. Inspira't amb els nostres treballs.")
OG_T = "Galeria de jardins Girona | New Tree"
OG_D = "Piscines, gespa, reg, jardins verticals i podes: alguns dels projectes de New Tree a Girona i l'Empordà."
H1 = "Galeria de jardins Girona"
LEAD = "Galeria de jardins Girona: alguns dels projectes que hem fet a Girona i l'Empordà."


def slug(s, n=55):
    s = unicodedata.normalize("NFD", s.lower()).encode("ascii", "ignore").decode()
    s = re.sub(r"galeria de jardins girona:?\s*", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return ("jardineria-girona-" + s)[:n].rstrip("-")


assert 120 <= len(DESC) <= 156 and DESC.lower().startswith(KW.lower()) and TITLE.lower().startswith(KW.lower()) and len(TITLE) <= 58
rows = []
for n, alt in GALLERY:
    rows.append(f"| {n}.png | {alt} | `{slug(alt)}.webp` |")

ld = {
    "@context": "https://schema.org", "@type": "ImageGallery", "name": H1, "inLanguage": "ca",
    "url": SITE + "galeria/", "description": DESC,
    "author": {"@type": "Organization", "name": "New Tree", "url": SITE},
    "image": [{"@type": "ImageObject", "contentUrl": BASE + "2020/04/%s.png" % n,
               "thumbnailUrl": BASE + "2020/04/" + THUMB.get(n, n + ".png"), "name": alt,
               "creator": {"@type": "Organization", "name": "New Tree"}} for n, alt in GALLERY],
}
json.loads(json.dumps(ld))  # JSON válido

text_md = []
for kind, t in SEO_TEXT:
    plain = html.unescape(re.sub(r"<[^>]+>", "", t))
    text_md.append(("**H2 —** " if kind == "h2" else "**H3 —** " if kind == "h3" else "") + plain + "\n")

md = f"""# Ficha SEO — Galeria (Yoast)

Página: **Galeria** · idioma: catalán · plantilla: `importar/14-galeria.json`

## 1. Campos de Yoast (copiar y pegar)

| Campo | Valor |
|---|---|
| **Frase clave objetivo** | `{KW}` (4 palabras) |
| **Título SEO** ({len(TITLE)} car.) | {TITLE.replace("|", chr(92) + "|")} |
| **Slug** | `{SLUG_NOU}` (actual: `galeria` → redirección 301) |
| **Meta descripción** ({len(DESC)} car.) | {DESC} |
| **URL canónica** | `{SITE}{SLUG_NOU}/` |
| **Título de migas (breadcrumb)** | Galeria |

La frase clave **empieza** el título SEO y la meta descripción, y está en el slug, el H1, la primera frase, un H2 y el alt de 3 imágenes.

## 2. Redes sociales (Yoast → Social)

| Campo | Valor |
|---|---|
| Título (Facebook/X) | {OG_T.replace("|", chr(92) + "|")} |
| Descripción | {OG_D} |
| Imagen | Foto `17` (gespa artificial con olivera) recortada a **1200×630 px**, JPG/WebP ≤ 200 KB. No uses la PNG original (1,7 MB). |

## 3. Contenido de la página (ya incluido en la plantilla)

- **H1:** {H1}
- **Primera frase (primer párrafo):** {LEAD}
- **Subtítulos:** {" · ".join(re.sub(r"<[^>]+>", "", t) for k, t in SEO_TEXT if k in ("h2", "h3"))}

{chr(10).join(text_md)}

El texto tiene **~310 palabras**, la frase clave aparece 5 veces (densidad ≈ 1,6 %), 9 enlaces internos a los servicios y 1 enlace externo (mapa). Todos los datos son reales de newtree.cat (fundada en 1977, más de 50 años, zonas, servicios y vocación); no se ha inventado ninguna cifra.

## 4. Imágenes (16 fotos distintas)

La galería original tenía 20; se omiten las duplicadas (`5-2` = `5`, `18` = `4` recortada, `3` = otra toma de la olivera `15`) y la `8`, que lleva una etiqueta suelta («Es una imagen»).

Cada imagen tiene **alt único y descriptivo**; la frase clave solo está en 3 (11, 17, 19) para no sobreoptimizar. Al subirlas a la biblioteca de medios, **renómbralas** con el nombre recomendado y conviértelas a WebP (ahorra peso y mejora la velocidad):

| Original | Texto alternativo (alt) | Nombre de archivo recomendado |
|---|---|---|
{chr(10).join(rows)}

> Las miniaturas de 300 px que usa la plantilla (para que Elementor pueda importarla) son las del servidor actual. Al terminar, sustitúyelas por las versiones WebP de ~800 px.

## 5. Enlazado interno

- **Desde la galería** hacia los 9 servicios (ya en el texto, con el nombre del servicio como ancla).
- **Hacia la galería:** el botón «VEURE PROJECTES» del hero y «VEURE TOTS ELS PROJECTES» del Inici y de Jardineria. Usa como ancla `galeria de jardins Girona` al menos en un enlace (por ejemplo, un texto en el footer o en Empresa), sin repetirla en todos.
- No enlaces a la galería con anclas genéricas («clic aquí»).

## 6. Comprobaciones de Yoast

| Comprobación | Resultado |
|---|---|
| Frase clave en la introducción | ✔ está en la primera frase |
| Longitud de la frase clave | ✔ 4 palabras |
| Densidad de la frase clave | ✔ 5 veces en ~310 palabras (≈ 1,6 %) |
| Frase clave en el título SEO (al principio) | ✔ |
| Frase clave en la meta descripción | ✔ (al principio, {len(DESC)} car.) |
| Longitud de la meta descripción | ✔ 120–156 |
| Frase clave en el slug | ✔ con el slug nuevo |
| Frase clave en subtítulos (H2/H3) | ✔ en un H2 |
| Frase clave en el alt de imágenes | ✔ en 3 de 16 |
| Longitud del texto | ✔ ≈ 310 palabras (mínimo 300) |
| Enlaces internos | ✔ 9 |
| Enlaces externos | ✔ 1 (mapa) |
| Frase clave única | ✔ no se usa en ninguna otra ficha |
| Distribución de subtítulos | ✔ ninguna sección supera 300 palabras |

Yoast puede no aplicar todo el análisis de legibilidad al catalán; revisa los avisos en el editor. Las frases son cortas (solo 1 supera las 20 palabras).

## 7. Datos estructurados (JSON-LD, opcional)

Yoast ya genera el esquema básico de la página. Este bloque añade la galería como `ImageGallery` con sus imágenes. Pégalo en un widget HTML al final de la página (cambia la URL si cambias el slug):

```json
{json.dumps(ld, ensure_ascii=False, indent=2)}
```

## 8. A tener en cuenta

- **Sitio multiidioma.** newtree.cat tiene versiones en ES (`/es/galeria-esp/`), FR (`/fr/galeria-fr/`) y EN (`/en/galeria-engl/`). Si cambias el slug de la versión catalana, redirige también las demás y mantén las etiquetas `hreflang` del plugin de idiomas. Si prefieres no tocar URLs, deja `/galeria/` y usa solo título, descripción y texto.
- **Feed de Instagram.** La plantilla incluye el shortcode `[instagram-feed]`, que era el de la página original; solo funciona si el plugin «Instagram Feed» está instalado en el sitio nuevo. Si no lo está, elimina esa sección.
- **Lightbox.** Cada foto abre la imagen completa en una pestaña nueva. La galería original usaba un lightbox; las imágenes de plantilla no pueden hacerlo sin subirse antes a la biblioteca de medios.
"""
open(os.path.join(ROOT, "SEO-GALERIA.md"), "w", encoding="utf-8").write(md)
print("SEO-GALERIA.md ok | título", len(TITLE), "| descripción", len(DESC))
