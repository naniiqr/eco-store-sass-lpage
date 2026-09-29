# Plantillas Elementor — New Tree

Generadas a partir de `Proposta_web_New_tree_compressed.pdf` para importar en `webnova.newtree.cat` (Elementor 4.3.2 / Elementor Pro 3.28.2).

## Archivos

- `inici-home.json` — página **Inici (Home)**, cuerpo completo de la página (6 secciones).

## Supuestos importantes

1. **No incluye header ni footer.** El menú superior y el pie de página son idénticos en las dos páginas del PDF, así que asumo que ya existen como plantillas globales en tu Theme Builder (Elementor Pro). Este JSON es solo el **contenido de la página**, para pegar dentro de tu página "Inici" sin duplicar ese header/footer.
   - Si tu sitio **no** los tiene como plantillas globales de Theme Builder, dímelo y te los genero también como secciones dentro de la página.
2. **Estructura con Containers** (`elType: "container"`), no Secciones/Columnas antiguas — correcto para Elementor 4.x.
3. **Colores estimados** (no pude leer los hex exactos del PDF, son una aproximación visual):
   - Rojo/coral (acentos y "DEMANA PRESSUPOST"): `#E14D5A`
   - Verde (botones secundarios, iconos): `#4E8C3F`
   - Verde muy oscuro (secciones destacadas): `#122318`
   - Negro (banner final): `#0B0B0B`
   - Ajusta estos valores en **Site Settings → Global Colors** tras importar, si tienes los hex reales de marca.
4. **Tipografías**: no se fuerza ninguna familia tipográfica — hereda tu Kit global de Elementor. Si usas fuentes específicas (p. ej. una script/cursiva para "Natura Benestar Vida" o "Fem créixer espais, fem créixer persones"), añádela en Global Fonts y aplícala manualmente a esos dos textos decorativos (van marcados en cursiva simple como placeholder).
5. **Iconos**: Font Awesome (incluido con Elementor/Pro), elegidos por significado (hoja, gota, reciclaje, etc.) — cámbialos si tienes un set de iconos de marca distinto.

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

## Cómo importar

1. WordPress → **Plantillas → Todas las plantillas → Añadir nueva** (o directamente en una página nueva/existente con Elementor).
2. Opción A (recomendada): crea una plantilla de tipo **Página** en la Biblioteca de Elementor, ábrela en el editor, y usa **Importar plantilla** (icono de carpeta abajo a la izquierda del panel) → sube `inici-home.json`.
3. Arrastra la plantilla resultante dentro del `<body>` de tu página "Inici" (encima/debajo de tu header y footer existentes).
4. Reemplaza los 18 placeholders por tus fotos reales.
5. Revisa los colores/tipografías contra tu Kit global y ajusta si hace falta.
6. Comprueba el responsive (móvil/tablet) — los `flex_gap` y anchos en `%` están pensados para que Elementor apile las columnas automáticamente en pantallas pequeñas, pero conviene revisar cada sección.

## Siguiente paso

Cuando confirmes que esto importa y se ve bien, seguimos con la página **Jardineria** (página 2 del PDF).
