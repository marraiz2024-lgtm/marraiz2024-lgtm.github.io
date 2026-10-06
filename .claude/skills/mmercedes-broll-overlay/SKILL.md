---
name: mmercedes-broll-overlay
description: Genera el PNG 1080×1920px de texto overlay para B-roll de MMercedesEnglish. Usar SIEMPRE que Mercedes pida "arma el B-roll de...", "genera el overlay para...", "haz el texto para el B-roll de...", "necesito el overlay de [tema]", o cualquier solicitud de texto superpuesto sobre imagen o video de ambiente. Se anima en Grok o CapCut. No es un post de redes, es overlay sobre imagen B-roll.
---

# MMercedesEnglish: B-roll text overlay

Genera el PNG 1080×1920 de overlay de texto para animar en Grok o CapCut sobre una imagen de B-roll (escritorio, parque, café).

Usa el mismo script que los posts: `mmercedes-generador-posts/assets/mm_posts.py`, subcomando `broll`. Ya no depende del archivo `build_what_are_you_up_to.py` ni de rutas de sesión.

**Aviso:** el subcomando `broll` se reconstruyó a partir de la lista de zonas de la versión anterior de esta skill, porque el script base original no estaba disponible. Mercedes debe aprobar la primera pieza antes de usarlo en serie. Mantiene la paleta, las fuentes y el orden de zonas.

## Qué es un overlay

- B-roll es una imagen de ambiente con el texto encima. No es un post educativo completo.
- No lleva avatar. El avatar de recorte no se usa en B-roll de ambiente.
- Se anima en Grok o CapCut. El PNG es la capa de texto.

## Paso 1: contenido

Pregunta solo lo que falta: tema o expresión, si hay falso amigo o error común (para el bloque con X roja y check verde) y el tip (si no hay, propón uno).

```json
{
  "nivel": "Beginner",
  "serie": "Real English",
  "tema": "what are you up to",
  "hook": "¿Sabes qué significa...",
  "expresion": "\"What are you up to?\"",
  "reveal_no": "NO significa: estar arriba",
  "reveal_si": "SIGNIFICA: ¿Qué estás haciendo?",
  "subtitulo": "inglés conversacional, uso diario",
  "ejemplos": [["Hey! What are you up to?", "¿Qué estás haciendo?"], ["Not much, just having coffee.", "No mucho, tomando café."]],
  "tip": ["Esta frase la escucharás todo el tiempo. ¡Guárdala para no olvidarla!"],
  "salida": "broll_what_are_you_up_to.png"
}
```

- `serie`: "Real English" para expresiones coloquiales, "Common Mistakes" para errores.
- `nivel`: Beginner o Intermediate, según el contenido real.
- `ejemplos`: entre 2 y 3 filas.
- CTA: lo elige el script del banco de Universales de `mmercedes-colores`, siempre al link en bio. Retirados: "Guarda este video", "¿La conocías?" y cualquier CTA que pida comentar. Si hace falta uno distinto, pasa `cta` con dos líneas.

## Paso 2: ejecutar

```bash
SCRIPT=$(find . ~/.claude /mnt -path '*mmercedes-generador-posts/assets/mm_posts.py' 2>/dev/null | head -1)
python3 "$SCRIPT" broll contenido.json --out ./salida
```

Estructura de zonas (no cambiar): header navy con pastilla MM, nivel y serie roja; hook en cursiva navy; burbuja navy con la expresión en amarillo, subrayado y estrellas; zona reveal navy con X roja y check verde; sección EJEMPLOS; Tip Mercedes con fondo amarillo pálido; CTA al link en bio; footer navy.

## Animación en Grok o CapCut

**Grok:** sube el PNG como imagen base. Prompt: "Animate this text overlay with a subtle zoom-in effect (scale 100% to 103%). Keep all text perfectly readable. Vertical 9:16, [N] seconds, no camera shake."

**CapCut:** importa la imagen B-roll de fondo, oscurécela al 50% con una capa negra semitransparente, importa el PNG encima, aplica zoom lento tipo Ken Burns al fondo. El overlay queda estático o con fade-in por zonas.

## Reglas

- No cambiar colores, fuentes ni estructura.
- Nombre de salida descriptivo: `broll_[tema].png`.
- Si el texto de una línea es muy largo, el script reduce solo esa línea.
- Pasa el resultado por `mmercedes-qa` antes de publicar.
