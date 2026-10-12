# Plantillas Elementor — New Tree

Generadas a partir de `Proposta_web_New_tree_compressed.pdf` para importar en `webnova.newtree.cat` (Elementor 4.3.2 / Elementor Pro 3.28.2).

## Archivos

- `inici-home.json` — página **Inici (Home)**, cuerpo completo de la página (6 secciones).
- `jardineria.json` — página **Jardineria** (disseny de jardins), cuerpo completo (7 secciones).
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
3. **Tipografía: Nunito** (decidido). Ningún widget fuerza familia, todos heredan el **Kit global**. Para aplicarla en todo el sitio: Site Settings → Global Fonts → pon **Nunito** en Primary, Secondary, Text y Accent (pesos usados: 400 texto, 600 subtítulos/etiquetas, 700 títulos). Elementor la carga desde Google Fonts; para RGPD puedes activar "Cargar Google Fonts en local" en Elementor → Ajustes → Avanzado.
   - Los dos textos decorativos en cursiva ("Natura Benestar Vida" y "Fem créixer espais, fem créixer persones") van en itálica simple como placeholder; si quieres una fuente script distinta, aplícala a esos dos widgets.
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

### Placeholders de `jardineria.json` (8)

| Sección | Placeholder / etiqueta |
|---|---|
| Hero | Foto hero disseny jardí |
| "Molt més que un jardí" | Foto jardí disseny detall (con la cita superpuesta) |
| Proyectos | Jardí mediterrani |
| Proyectos | Jardí amb piscina |
| Proyectos | Jardí contemporani |
| Proyectos | Racó chill out |
| Proyectos | Jardí amb oliveres |
| Proyectos | Jardí amb desnivells |

## Cómo importar `inici-home.json` / `jardineria.json`

1. WordPress → **Plantillas → Todas las plantillas → Añadir nueva** (o directamente en una página nueva/existente con Elementor).
2. Opción A (recomendada): crea una plantilla de tipo **Página** en la Biblioteca de Elementor, ábrela en el editor, y usa **Importar plantilla** (icono de carpeta abajo a la izquierda del panel) → sube `inici-home.json`.
3. Inserta esa plantilla como contenido de tu página "Inici" (el header y footer los pondrá automáticamente tu tema, ya que ahora van por Theme Builder — no hace falta duplicarlos aquí).
4. Reemplaza los 18 placeholders por tus fotos reales.
5. Revisa los colores/tipografías contra tu Kit global y ajusta si hace falta.
6. Comprueba el responsive (móvil/tablet) — los `flex_gap` y anchos en `%` están pensados para que Elementor apile las columnas automáticamente en pantallas pequeñas, pero conviene revisar cada sección.

## Estado

Inici y Jardineria (las 2 únicas páginas del PDF) más todas las demás páginas del menú están cubiertas. Las páginas sin mockup toman de newtree.cat **solo contenido e imágenes**; el diseño es el del PDF.

## Páginas de servicio (`servicios/`) — contenido real de newtree.cat

10 plantillas generadas con `scripts/build_servicios.py` (helpers compartidos en `scripts/lib_elementor.py`), reutilizando la línea visual de `jardineria.json` pero con los textos reales de la web actual (corregidas erratas evidentes del original). Estructura: hero → texto + imagen → lista (si aplica) → galería (si hay fotos) → banner de contacto con teléfonos, email y dirección reales.

`disseny-i-construccio-de-jardins`, `sistemes-de-reg`, `installacio-de-gespa`, `manteniment-de-jardins`, `jardins-verticals`, `terres-i-substrats`, `nateja-parceles`, `tanques-murs`, `podes`, `obra-publica`.

- `obra-publica.json` corresponde a `newtree.cat/jardineria-2/` (hub con botones a los 9 servicios). Su foto es un placeholder: la web actual no expone la URL.
- Las imágenes apuntan a `newtree.cat/wp-content/uploads/...` (hotlink). Tras importar, súbelas a la biblioteca de medios del nuevo sitio y reemplázalas.
- Los botones "DEMANA PRESSUPOST" usan `mailto:info@newtree.cat`; cámbialos por la página de contacto cuando exista.
- Regenerar: `cd scripts && python3 build_servicios.py`.

## Resto de páginas (`paginas/`)

Generadas con `scripts/build_paginas.py`: `empresa.json`, `galeria.json` (20 fotos), `plantes-exemplars.json`, `situacio-i-contacte.json`.

- Los textos de Galeria, Plantes exemplars y Situació i contacte están en castellano en la web actual; aquí se usan los títulos y el lema en catalán (como el resto del sitio).
- `plantes-exemplars`: la web actual no lista especies concretas, solo un texto genérico y dos fotos; no se inventó contenido.
- `situacio-i-contacte`: usa el widget **Form** (Elementor Pro) con Nom / Correu / Missatge / Enviar, enviando a `info@newtree.cat`, y el widget Google Maps con la dirección (la web actual no da coordenadas ni horarios).
- `empresa`: fundada en 1977, zonas de servicio y vocación de la empresa, todo del texto original.

## Importar (carpeta `importar/`) — todo listo

`importar/` contiene las 18 plantillas, una por archivo y numeradas, ya con **Nunito** fijada en cada widget de texto (no depende del Kit global). Regenerar todo: `cd scripts && python3 build_all.py`.

- `00-header.json`, `00-footer.json` → Theme Builder (tipo Header / Footer, condición "Todo el sitio").
- `01` a `16` → una plantilla de tipo **Página** cada una (Elementor → Plantillas → Importar plantillas, o dentro del editor de la página con la carpeta de importar).

## Textos (importante)

Las páginas de servicio, Empresa, Galeria, Plantes exemplars y Situació i contacte usan el **texto literal de newtree.cat** (extraído del HTML de cada URL); solo se corrigieron erratas tipográficas evidentes (p. ej. «lazona», «dissenysamb», «Camíde», «am box»). Plantes exemplars solo existe en castellano en la web actual, y se pasó a catalán conservando el sentido. Las imágenes son las de cada página original.

## Vista previa HTML (`preview/`)

`python3 scripts/preview.py` lee los JSON de `importar/` y genera una página HTML por plantilla (con header y footer) más un `index.html`. Abre `preview/index.html` en el navegador (necesita internet para fotos, tipografía e iconos). Tiene botones Escritorio / Tauleta / Mòbil. Es una aproximación: Elementor puede diferir ligeramente en espaciados.

## Header y Footer (Theme Builder, requiere Elementor Pro)

`header.json` y `footer.json` (también como `importar/00-header.json` y `00-footer.json`) son plantillas **separadas** de tipo Header y Footer; no están incluidas dentro de las páginas.

1. WordPress → Plantillas → Theme Builder → Header → Añadir nuevo → Importar → `header.json`. Publicar con condición «Todo el sitio». Repetir con Footer.
2. Header: barra superior (teléfonos, email, idiomas; solo escritorio) + logo, menú y botón «DEMANA PRESSUPOST». Tras importar, **asigna tu menú de WordPress** en el widget Nav Menu (en tablet/móvil se convierte en hamburguesa). Sticky activado.
3. Footer: logo, contacto real, enlaces a los servicios, avís legal y política de privacitat. El enlace de Instagram apunta a `#`: pon el real.
4. El logo (`Site Logo`) lo toma del logo del tema; el actual de newtree.cat tiene fondo blanco, por eso en el footer va dentro de una caja blanca redondeada. Con un logo transparente o blanco, quita la caja.

## Responsive

Revisión final aplicada a todas las plantillas (`scripts/responsive.py`): márgenes laterales siempre simétricos (40 px escritorio, 24 tablet, 20 móvil), tarjetas de 2 en 2 en tablet, una columna y contenido centrado en móvil, adornos flotantes ocultos en móvil.

## Colores de marca (importante para que no se vean los widgets «por defecto»)

Los JSON fijan los colores de marca en cada widget (incluidos iconos y formulario). Para que **todo lo que no está en los JSON** (enlaces, menú, selector de idioma, tipografías heredadas) también respete la marca, define los **Global Colors** en Site Settings: Primary `#4E8C3F` (verde), Secondary `#122318` (verde oscuro), Text `#1E2A22`, Accent `#E14D5A` (rojo). Los enlaces rojos que se ven por defecto vienen del color Accent/enlaces del Kit del tema.

**Contacte** (`situacio-i-contacte.json`): tarjeta en dos mitades — panel verde oscuro con los datos (iconos en círculo verde) y panel verde de marca con el formulario (campos blancos redondeados, botón verde oscuro a ancho completo) — y mapa debajo con esquinas redondeadas. El formulario es el widget Form de Elementor Pro.

## Diseño (identidad del PDF) — `scripts/design.py`

Todas las páginas se construyen con los mismos componentes (`design.py`), fieles al PDF: hero con foto, degradado y rótulo manuscrito («Natura Benestar Vida», fuente **Caveat** de Google Fonts), franja de 5 iconos, tarjetas con foto y degradado, bloques verde oscuro con iconos en círculo, banner final con eslogan manuscrito y footer claro. Colores: verde `#4E8C3F`, verde oscuro `#122318`, rojo `#E14D5A`, negro `#0B0B0B`; tipografía Nunito.

- Sin posicionamientos absolutos frágiles: todo va en flujo (salvo la tarjeta de cita de Jardineria, anclada abajo a la derecha de su foto con desplazamiento «desde el final»).
- Los iconos de «Caja de icono» usan `primary_color` (la clave correcta de Elementor); antes usaba `icon_color`, que Elementor ignoraba y dejaba los iconos en azul por defecto.
- Inici usa las fotos reales de newtree.cat en las tarjetas de servicio donde existen; el resto (hero, proyectos, jardí ampli) son placeholders a reemplazar.
- Regenerar todo: `cd scripts && python3 build_all.py && python3 preview.py`.
