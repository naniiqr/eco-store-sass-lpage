# SEO local — New Tree

Solo datos reales de newtree.cat. Lo que falta (horarios, coordenadas, redes) está marcado como pendiente: no se inventa.

## 1. Google Business Profile (lo de más impacto)

- **Nombre**: New Tree (sin keywords añadidas; Google lo penaliza).
- **Categoría principal**: Servicio de jardinería. **Secundarias**: Paisajista · Servicio de poda de árboles · Instalador de césped/gespa · Instalador de sistemas de riego · Empresa de mantenimiento de jardines (elige las que ofrezca el selector en tu idioma).
- **Dirección**: Camí de Reg de la Vinya s/n, Calabuig – Bàscara, Girona 17483. **Teléfono**: (+34) 972 560 033 (secundario 607 484 646). **Web**: https://newtree.cat/
- **Área de servicio**: Figueres, Girona, Roses, L'Escala, Empuriabrava, Peralada, Castelló d'Empúries, Llançà, Port de la Selva.
- **Servicios**: crea uno por cada página de servicio (disseny de jardins, sistemes de reg, instal·lació de gespa, manteniment de jardins, jardins verticals, terres i substrats, neteja de parcel·les, tanques i murs, podes, obra pública).
- **Descripció (606/750 car.)**:

```
New Tree és una empresa de jardineria fundada l'any 1977, dedicada a la jardineria privada i pública a tota la província de Girona. Oferim disseny i construcció de jardins a mida, sistemes de reg automàtic, instal·lació de gespa natural i artificial, manteniment de jardins, jardins verticals, podes, terres i substrats, neteja de parcel·les, tanques i murs de contenció, i obra pública per a ajuntaments. Treballem a Girona, Figueres, Roses, L'Escala, Empuriabrava, Peralada, Castelló d'Empúries, Llançà i Port de la Selva. Més de 50 anys d'experiència convertint un desert en un jardí. Demana pressupost.
```

- **Pendiente**: horarios, fotos reales (portada, logo, 10+ de trabajos), pedir reseñas. Cuando lleguen reseñas, responde a todas.

## 2. Consistencia NAP

Nombre, dirección y teléfono idénticos en web (footer, contacto), Google, Bing Places, Apple Business, Pàgines Grogues, Infoempresa, Cambra de Comerç y Yelp. Escribe siempre «Camí de Reg de la Vinya s/n, Calabuig – Bàscara, 17483 Girona» y «972 560 033».

## 3. Datos estructurados (JSON-LD)

Pégalo en Yoast → Ajustes → Presencia del sitio, o en un widget HTML del footer/Inici. Pendiente de añadir cuando existan: `openingHours`, `geo` (coordenadas), `sameAs` (redes), `aggregateRating`.

```json
{
  "@context": "https://schema.org",
  "@type": "LocalBusiness",
  "@id": "https://newtree.cat/#negoci",
  "name": "New Tree",
  "description": "Empresa de jardineria privada i pública fundada l'any 1977. Disseny, construcció i manteniment de jardins a la província de Girona.",
  "url": "https://newtree.cat/",
  "logo": "https://newtree.cat/wp-content/uploads/2020/04/Logo-300x261.png",
  "image": "https://newtree.cat/wp-content/uploads/2020/04/f3.jpg",
  "telephone": [
    "+34972560033",
    "+34607484646"
  ],
  "email": "info@newtree.cat",
  "foundingDate": "1977",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Camí de Reg de la Vinya s/n, Calabuig",
    "addressLocality": "Bàscara",
    "addressRegion": "Girona",
    "postalCode": "17483",
    "addressCountry": "ES"
  },
  "areaServed": [
    {
      "@type": "City",
      "name": "Girona"
    },
    {
      "@type": "City",
      "name": "Figueres"
    },
    {
      "@type": "City",
      "name": "Roses"
    },
    {
      "@type": "City",
      "name": "L'Escala"
    },
    {
      "@type": "City",
      "name": "Empuriabrava"
    },
    {
      "@type": "City",
      "name": "Peralada"
    },
    {
      "@type": "City",
      "name": "Castelló d'Empúries"
    },
    {
      "@type": "City",
      "name": "Llançà"
    },
    {
      "@type": "City",
      "name": "Port de la Selva"
    }
  ],
  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Serveis de jardineria",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Disseny de jardins"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Sistemes de reg"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Instal·lació de gespa"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Manteniment de jardins"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Jardins verticals"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Terres i substrats"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Neteja de parcel·les"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Tanques i murs de contenció"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Servei de podes"
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Obra pública"
        }
      }
    ]
  }
}
```

## 4. Páginas por zona (recomendado)

Una página corta y útil por localidad (no duplicada), con keyphrase local al inicio del title y descripción, mapa/zona, 2–3 servicios y fotos reales de esa zona:

| Página | Keyphrase | Slug |
|---|---|---|
| Jardineria a Figueres | jardineria a Figueres | /jardineria-figueres/ |
| Jardineria a Girona | jardineria a Girona | /jardineria-girona/ |
| Jardineria a Roses | jardineria a Roses | /jardineria-roses/ |
| Jardineria a L'Escala | jardineria a L'Escala | /jardineria-l-escala/ |
| Jardineria a Empuriabrava | jardineria a Empuriabrava | /jardineria-empuriabrava/ |
| Jardineria a Peralada | jardineria a Peralada | /jardineria-peralada/ |
| Jardineria a Castelló d'Empúries | jardineria a Castelló d'Empúries | /jardineria-castelló-d-empuries/ |
| Jardineria a Llançà | jardineria a Llançà | /jardineria-llanca/ |
| Jardineria a Port de la Selva | jardineria a Port de la Selva | /jardineria-port-de-la-selva/ |

Enlázalas desde el footer y desde Empresa («Treballem a…»). Evita doorway pages: solo crea las zonas donde haya trabajos reales.

## 5. On-page local

- Menciona «Girona», «l'Empordà» y la localidad en title, H1, primer párrafo y un H2 de cada página de servicio (ya hecho en las fichas SEO).
- Footer con NAP completo y enlace a Contacte (con mapa de Google incrustado, ya incluido en la plantilla).
- Alt de imágenes con servicio + zona.
- Galeria: nombra cada foto «jardí a [localitat]» cuando se conozca.
- Enlaces locales: ayuntamientos clientes (Obra pública), asociaciones de jardinería de Catalunya, directorios comarcals.

## 6. Medición

Search Console + Google Business Profile (llamadas, rutas, visitas web). Objetivo: top 3 en el «paquete local» para «jardineria Figueres», «jardiner Girona» y «jardineria a l'Empordà».
