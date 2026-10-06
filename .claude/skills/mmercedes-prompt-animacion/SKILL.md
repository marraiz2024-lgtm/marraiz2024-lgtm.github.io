---
name: "mmercedes-prompt-animacion"
description: "Genera el prompt completo para animar el avatar de MMercedesEnglish en Grok, HeyGen, D-ID o CapCut. Usar SIEMPRE que Mercedes pida: \"dame el prompt para animar\", \"cómo animo el avatar\", \"prompt para Grok\", \"prompt para HeyGen\", \"quiero que el avatar explique el post\", \"anima la imagen\", o cualquier solicitud de animación del avatar o del post. Incluye script de voz, descripción de movimiento y parámetros técnicos según la herramienta."
---

# MMercedesEnglish — Generador de Prompt de Animación

Genera el prompt completo para animar el avatar o el post en la herramienta indicada.

## PRINCIPIO FUNDAMENTAL DEL AVATAR

**Las fotos del avatar son fotos REALES de Mercedes, no ilustraciones ni imágenes generadas.**
- Se pueden usar diferentes poses, diferentes props y diferentes ángulos para dar variedad
- Lo que NUNCA puede modificarse ni interpretarse son los rasgos y la fisonomía — son los de Mercedes
- Cualquier herramienta de animación debe PRESERVAR la identidad visual exacta de la persona en la foto

---

## PASO 1 — Recopilar datos

1. **¿Cuál es el contenido del post?**
2. **¿Qué herramienta?** Grok / HeyGen / D-ID / CapCut
3. **¿Animar avatar sobre imagen fija, o generar video desde cero?**
4. **¿Duración?** (default: 15-30 segundos)
5. **¿Idioma?** (default: español, con frases en inglés pronunciadas claramente)

---

## PASO 2 — Script de voz

Estructura de 3 partes, máximo 60-80 palabras:

**HOOK** (3-5 seg): pregunta o afirmación que engancha al alumno hispanohablante

**REVEAL** (5-10 seg): corrección o expresión correcta pronunciada con énfasis, repetida una vez

**CIERRE/CTA** (3-5 seg): invitación a comentar o guardar, corto y directo

Tono: cercano, didáctico, con energía — como Mercedes habla en clase.

---

## PASO 3 — Prompts por herramienta

### GROK

```
Animate this image as a short educational video for Instagram Reels.

IDENTITY — CRITICAL: The woman in this photo is the real person behind this brand.
Preserve her appearance EXACTLY as shown:
- Do not alter her face, facial features, skin tone, or age
- Do not change her hair (dark with white/gray streaks, shoulder-length, wavy)
- Do not change her glasses (keep EXACTLY the frames shown in the reference photo; she owns several pairs and every one is valid, but they must not change during the video)
- Do not change her clothing or body proportions
- Different poses and props are acceptable — her face and physical identity are not

MOVEMENT: Natural, subtle teacher gestures only:
- Gentle head movement toward camera
- Natural blinking and slight facial expression changes
- Small hand gestures synchronized with speech
- Lip-sync to audio
No exaggerated movement, no cartoon behavior, no body morphing, no face distortion

SCRIPT: [SCRIPT COMPLETO]

VOICE: Warm, confident, conversational teacher tone. Natural pace with emphasis on key phrase.

CAMERA: Static medium shot. No zooms, pans, cuts, or dramatic camera movement.

BACKGROUND: Keep original clean white background. Do not add or change the background.

FORMAT: Portrait vertical 1080×1920px, [N] seconds, 30fps.

DO NOT: add subtitles, captions, watermarks, music, logos, extra objects, or any visual effects.
DO NOT distort, age, or alter the person's face in any way.
```

### HEYGEN

```
- Sube la foto de referencia como "Photo Avatar"
- En "Script": [SCRIPT COMPLETO]
- Voz: femenina, español latinoamericano, tono cálido
- Gestures/expressions: nivel medio — natural, no exagerado
- CRÍTICO: en la configuración de identidad, activar "preserve facial features" al máximo
- Resolución: 1080×1920 vertical para Reels
- Duración objetivo: [N] segundos
```

### D-ID

```
- Foto: imagen del avatar con fondo blanco
- Script: [SCRIPT COMPLETO]
- Idioma: Spanish (Latin America)
- Voz: femenina, neutral, cálida — velocidad 0.95
- Driver: el más natural disponible (no exagerado)
- Exportar: MP4, vertical 1080×1920
```

### CAPCUT

```
- Importar PNG del post o foto del avatar como imagen base
- Aplicar "Talking Photo" o "AI Portrait" si disponible
- Voz: grabar el script o usar TTS en español
- Zoom sutil en capa de fondo: 100% → 103% en [N] segundos
- El avatar queda estático o con fade-in
- Exportar: 1080×1920, 30fps, calidad alta
```

---

## PASO 4 — Entrega

Entrega los 3 componentes separados: **Script · Prompt de animación · Parámetros técnicos**

Al final, nota con errores a vigilar:
- Boca desincronizada con el audio
- Distorsión del rostro (NO tolerable — el rostro es la identidad real de Mercedes)
- Cambio de las gafas respecto a la foto de referencia
- Texto del prop que se distorsione con el movimiento

**Si la herramienta no fue especificada:** entregar el script primero y preguntar la herramienta.

---

## RESPUESTAS PARA CORREGIR ERRORES

**Si la herramienta distorsiona el rostro:**
> "El rostro de la persona en la foto NO puede distorsionarse ni modificarse — es la identidad real de la persona. Reduce la intensidad del movimiento y regenera preservando los rasgos faciales exactos."

**Si cambia las gafas:**
> "Las gafas son las de la foto de referencia: mismo armazón, forma y color. Es un rasgo de identidad de la persona real. Regenera preservando las gafas originales."

