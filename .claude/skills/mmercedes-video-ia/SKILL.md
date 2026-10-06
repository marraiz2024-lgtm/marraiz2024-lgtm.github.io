---
name: mmercedes-video-ia
description: Genera el guion de voz y los prompts de video de MMercedesEnglish listos para pegar en Grok (Imagine), Google Flow (Veo), HeyGen, D-ID, CapCut u otra herramienta, a partir de una ficha. Decide si el protagonista es el avatar real de Mercedes o Mechita, ajusta el prompt a cada herramienta y entrega la lista de verificación del resultado. Usar SIEMPRE que Mercedes pida un video, un prompt para Grok o Flow, "anima esto", "clip de Mechita", "avatar explicando" o cuando la cadena llegue a la etapa 3.
---

# Video con IA: de la ficha al prompt

Esta skill une `mmercedes-prompt-animacion` (avatar real) y `mmercedes-mechita` (personaje 2D), y añade lo que ambas no cubren: elección de protagonista, diferencias entre herramientas, ritmo de palabras por segundo y revisión del resultado. Carga esas dos skills para los bloques de personaje, voz, sets y negative prompt. No los copies aquí, para que no se desfasen.

Claude no puede generar el video. Entrega: **Guion, Prompt por herramienta, Parámetros, Qué verificar.**

## Paso 1: elegir protagonista

| Protagonista | Es | Reglas | Cuándo |
|---|---|---|---|
| Avatar real | Fotografía de Mercedes | Identidad exacta: cabello oscuro con canas hasta los hombros, las mismas gafas de la imagen de referencia (Mercedes tiene varios armazones), argollas doradas, suéter negro cuello V. Nunca ilustración | Voz y rostro personales, reflexiones, explicaciones cortas, CTA |
| Mechita | Personaje 2D | Bob oscuro con canas, gafas burgundy, perlas, camiseta negra cuello V, jeans cropped, ballet flats. Estilo vector con sombreado suave | Diálogos modelo, drills, cápsulas de regla, contenido de curso por unidades |
| Sin personaje | B-roll animado | Zoom lento sobre imagen de ambiente y texto aparte | Reflexiones y tips sin voz, solo música |

Nunca mezcles las reglas. Un rasgo correcto en Mechita (bob, perlas) es un error en el avatar real, y al revés.

## Paso 2: guion de voz

Estructura de 3 partes: **Hook, Reveal, Cierre.** El hook engancha al hispanohablante, el reveal pronuncia la forma correcta con énfasis y la repite una vez, el cierre invita a guardar o comentar (según el CTA decidido en la ficha).

Duración y palabras (estimación propia, ajusta con el primer video):

| Duración | Palabras en español |
|---|---|
| 8 s | 15 a 20 |
| 15 s | 30 a 38 |
| 20 s | 45 a 50 |
| 30 s | 65 a 75 |

Las frases en inglés se cuentan aparte: cada una ocupa unos 2 segundos con pausa. Tono: cercano, didáctico, energía de clase.

## Paso 3: elegir herramienta y adaptar el prompt

| Herramienta | Uso principal | Entrada | Notas de adaptación |
|---|---|---|---|
| Grok (Imagine) | Animar la foto del avatar o generar Mechita desde imagen de referencia | Imagen de referencia más texto | Usa el prompt de `mmercedes-prompt-animacion`. Mantén "no music, no subtitles, no zoom" |
| Google Flow (Veo) | Escenas de Mechita con varios movimientos y diálogo | Texto con timecodes y, si tu versión lo ofrece, imágenes de referencia o fotogramas inicial y final | Usa la estructura de `mmercedes-mechita` con timecodes cada 3 a 5 segundos |
| HeyGen o D-ID | Avatar hablando con un solo audio coherente | Foto más guion o audio | Mejor cuando la voz debe ser idéntica durante todo el video. Activa la preservación de rasgos al máximo |
| CapCut | Montaje, texto en pantalla, audio, recorte | Clips ya generados | Aquí se pone el texto de marca. Exporta 1080×1920, 30 fps |
| Otra | Cualquiera | Adapta el bloque base | Verifica límites de duración y de referencia antes de generar |

Los límites de duración por clip y las funciones cambian con frecuencia. Verifica en la herramienta antes de planificar. Si el guion supera el límite, segmenta con cortes secos y sube la misma imagen de referencia en cada clip.

## Reglas comunes a todas las herramientas

1. Vertical 9:16, 1080×1920.
2. Sube siempre la imagen de referencia. Sin ella el personaje deriva.
3. Pide cero música. El audio trending de TikTok se añade dentro de la app al publicar, y en Instagram el audio se elige en la app.
4. **Texto en pantalla:** para 1 a 3 palabras sueltas se puede pedir generado. Para frases, no. La IA deforma tipografías y la marca exige BigShoulders y WorkSans. Añade el texto en CapCut o Canva sobre el clip.
5. La voz puede cambiar entre clips de una misma serie. Si pasa, regenera con la voz fijada o pasa todo por HeyGen o D-ID con un solo audio.
6. Genera primero la versión continua. Segmenta solo si la herramienta lo exige.
7. Sin precios, sin logos inventados. El único elemento de marca permitido es el badge MMercedesEnglish con "Tiny Tips, Big Progress" en el último segundo.
8. Los videos con persona realista pueden requerir la etiqueta de contenido generado con IA al publicar. Se verifica en `mmercedes-publicar`.

## Entrega

```
GUION (palabras: N, duración: S)
PROMPT [herramienta]  (listo para pegar)
PARÁMETROS            (formato, duración, fps, voz, referencia a subir)
QUÉ VERIFICAR         (lista del paso siguiente)
SEGMENTACIÓN          (tabla de clips, si el guion supera el límite)
```

## Qué verificar en el resultado (pasa a `mmercedes-qa`)

Avatar real: gafas iguales a la referencia en todos los fotogramas, cabello ondulado con canas, rostro sin distorsión (no tolerable), boca sincronizada, manos sin dedos extra, texto del resaltador o marcador exacto ("MMercedesEnglish"), fondo según el set.
Mechita: bob, gafas burgundy, perlas, misma ropa en todos los clips, texto sin parpadeo, sin cambios de voz entre clips.
Ambos: texto legible en el formato final, sin marca de agua de la herramienta, duración dentro del objetivo.

## Si falla

Usa las frases de corrección de `mmercedes-prompt-animacion` (rostro, gafas) y `mmercedes-mechita` (consistencia). Reduce la intensidad del movimiento antes de regenerar. Si falla dos veces con la misma herramienta, cambia de herramienta antes de insistir una tercera.
