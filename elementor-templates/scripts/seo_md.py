"""Regenera SEO.md y SEO.csv desde seo_data.py. Uso: python3 seo_md.py"""
import csv, os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from seo_data import PAGES
ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
md = ["# Fichas SEO (Yoast + local) — New Tree\n",
      "Cada keyphrase lleva la ciudad (Girona; Inici: l'Empordà), ≤4 palabras, exacta al **inicio** de title y meta description, y también en slug, H1, primera frase y alt. Title ≤58 car., description 120–156 car. Páginas en catalán (idioma por defecto del sitio). La ficha completa de la galería está en `SEO-GALERIA.md`.\n"]
for n, kw, slug, old, t, d, h, f, alt in PAGES:
    md.append(f"## {n}\n\n```\nKeyphrase: {kw}\nURL: {slug}" + (f"   (actual: {old} → 301)" if old != slug else "") +
              f"\nTitle ({len(t)}): {t}\nMeta description ({len(d)}): {d}\nH1: {h}\nPrimera frase: {f}\nAlt imagen: {alt}\n```\n")
md.append("""## Notas

- **Sitio multiidioma.** newtree.cat tiene 4 idiomas (CA en la raíz, `/es/`, `/fr/`, `/en/`). Estas fichas son para las páginas en catalán. Si cambias un slug, hay que hacerlo y redirigirlo (301) también en cada idioma. Si no quieres tocar URLs, deja las actuales y usa solo Title y Meta description.
- **/pressupost/** está protegida con contraseña (no se enlaza ni se indexa).
- Todas las páginas de servicio apuntan a «Girona»; las páginas por zona (Figueres, Roses…) usarán su propia localidad (ver SEO-LOCAL.md).
- La primera frase con la keyphrase y el H1 de esta ficha difieren del texto literal de la web actual; aplícalos solo si aceptas ese cambio de texto.
""")
open(os.path.join(ROOT, "SEO.md"), "w", encoding="utf-8").write("\n".join(md))
with open(os.path.join(ROOT, "SEO.csv"), "w", encoding="utf-8-sig", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["Pàgina", "Keyphrase", "URL nova", "URL actual", "Title", "Meta description", "H1", "Primera frase", "Alt imatge"])
    for r in PAGES:
        w.writerow(list(r[:9]))
print("SEO.md y SEO.csv ok")
