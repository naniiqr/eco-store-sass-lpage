# Plantillas Elementor — New Tree

Generadas a partir de `Proposta_web_New_tree_compressed.pdf` para importar en `webnova.newtree.cat` (Elementor 4.3.2 / Elementor Pro 3.28.2).

## Archivos

- `inici-home.json` — página **Inici (Home)**, cuerpo completo de la página (6 secciones).
- `header.json` — plantilla de **Header** (Theme Builder), para usar en todo el sitio.
- `footer.json` — plantilla de **Footer** (Theme Builder), para usar en todo el sitio.

## Header y Footer (nuevos, separados de la página)

Confirmado que aún no existen como plantillas globales, así que van aparte para que se apliquen a **todas** las páginas del sitio (Inici, Jardineria, etc.) desde el Theme Builder, en lugar de repetirse dentro de cada página.

- `header.json`: logo (widget dinámico "Site Logo", toma el logo que ya tengas en Apariencia → Personalizar), menú de navegación (widget Nav Menu — **tras importar, edítalo y asigna tu menú de WordPress**, el ID de menú no viaja en el JSON), selector de idioma (de momento como texto simple "CA ES FR ENG" — si usas WPML o Polylang, sustitúyelo por el widget nativo de ese plugin), y botón "DEMANA PRESSUPOST" en rojo. Incluye posición *sticky* (fijo al hacer scroll).
- `footer.json`: logo, iconos de Instagram/Facebook (con enlaces de ejemplo `#` — sustitúyelos por tus redes reales), enlaces legales (Avís legal / Política de privacitat / Cookies — de momento apuntan a `#`) y ubicación "Figueres (Girona)".

### Cómo importarlos

1. WordPress → **Plantillas → Todas las plantillas → Añadir nueva**.
2. Elige tipo **Header**, ponle nombre, y en el editor usa **Importar plantilla** → sube `header.json`.
3. Repite para **Footer** con `footer.json`.
4. En cada plantilla, pulsa **Publicar** y define las condiciones de visualización (normalmente "Todo el sitio" / "Entire Site").
5. Asigna el menú real al widget Nav Menu y revisa los enlaces de redes/legales.

## Supuestos importantes

1. **Estructura con Containers** (`elType: "container"`), no Secciones/Columnas antiguas — correcto para Elementor 4.x.
2. **Colores estimados** (no pude leer los hex exactos del PDF, son una aproximación visual):
   - Rojo/coral (acentos y "DEMANA PRESSUPOST"): `#E14D5A`
   - Verde (botones secundarios, iconos): `#4E8C3F`
   - Verde muy oscuro (secciones destacadas): `#122318`
   - Negro (banner final): `#0B0B0B`
   - Ajusta estos valores en **Site Settings → Global Colors** tras importar, si tienes los hex reales de marca.
3. **Tipografías**: no se fuerza ninguna familia tipográfica — hereda tu Kit global de Elementor. Si usas fuentes específicas (p. ej. una script/cursiva para "Natura Benestar Vida" o "Fem créixer espais, fem créixer persones"), añádela en Global Fonts y aplícala manualmente a esos dos textos decorativos (van marcados en cursiva simple como placeholder).
4. **Iconos**: Font Awesome (incluido con Elementor/Pro), elegidos por significado (hoja, gota, reciclaje, etc.) — cámbialos si tienes un set de iconos de marca distinto.

## Imágenes a reemplazar (18 placeholders)

Cada imagen del JSON apunta a un placeholder visual (`placehold.co`) con una etiqueta que indica qué foto va ahí. Tras importar, verás el texto directamente sobre la imagen — solo tienes que hacer clic en cada una dentro de Elementor y sustituirla por tu foto real de la Biblioteca de medios.

| Sección | Placeholder / etiqueta |
|---|---|
| Hero | Foto hero jardí (imagen de fondo grande) |
| Servicios | Disseny de jardins |
| Servicios | Jardineria i plantacions |
| Servicios | Sistemes de reg |
| Servicios | Tanques i Murs de contenció |
| Servicios | Piscines i exteriors |
| Servicios | Gespa Artificial i Natural |
| Servicios | Jardins verticals |
| Servicios | Murs i elements decoratius |
| Servicios | Manteniment de jardins |
| Servicios | Neteja de parcel·les |
| Servicios | Podes |
| Servicios | Terres i sustrats |
| Proyectos | Jardí residencial |
| Proyectos | Reforma d'exterior |
| Proyectos | Jardí mediterrani |
| Proyectos | Zona de piscina |
| A Newtree / CTA | Foto jardí ampli (imagen grande junto al texto "les teves Idees") |

## Cómo importar `inici-home.json`

1. WordPress → **Plantillas → Todas las plantillas → Añadir nueva** (o directamente en una página nueva/existente con Elementor).
2. Opción A (recomendada): crea una plantilla de tipo **Página** en la Biblioteca de Elementor, ábrela en el editor, y usa **Importar plantilla** (icono de carpeta abajo a la izquierda del panel) → sube `inici-home.json`.
3. Inserta esa plantilla como contenido de tu página "Inici" (el header y footer los pondrá automáticamente tu tema, ya que ahora van por Theme Builder — no hace falta duplicarlos aquí).
4. Reemplaza los 18 placeholders por tus fotos reales.
5. Revisa los colores/tipografías contra tu Kit global y ajusta si hace falta.
6. Comprueba el responsive (móvil/tablet) — los `flex_gap` y anchos en `%` están pensados para que Elementor apile las columnas automáticamente en pantallas pequeñas, pero conviene revisar cada sección.

## Siguiente paso

Cuando confirmes que esto importa y se ve bien, seguimos con la página **Jardineria** (página 2 del PDF).
