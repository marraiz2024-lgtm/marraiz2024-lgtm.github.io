# Contradicciones detectadas entre skills y archivos

Detectadas al revisar los skills de MMercedesEnglish, el repositorio y el calendario de Notion. Los puntos marcados como RESUELTO fueron decididos por Mercedes y ya están aplicados en las skills de este repositorio.

| # | Contradicción | Estado | Decisión y aplicación |
|---|---|---|---|
| 1 | Pastilla de nivel fija en "Beginner" en 4 skills frente a nivel dinámico en `mmercedes-brand` | RESUELTO | Dinámica. Cada post declara su nivel (Beginner o Intermediate). El script exige `nivel`. `mmercedes-prompt-ia` y `mmercedes-colores` usan `[NIVEL] English Tips` |
| 2 | CTA: link en bio (colores) frente a "Cuéntame en comentarios" y "Lo conocías?" (generador y prompt-ia) | RESUELTO | Todos los CTA dirigen al link en bio ("Revisa el link en mi bio para más contenido" y similares). Se retiran "Cuéntame en comentarios", "¿Lo conocías?" y "¿La conocías?". El CTA se elige en cada caso según el tema de la pieza (tabla en `mmercedes-colores` y banco en el script) |
| 3 | La marca exige avatar y prop, pero el script de Pillow generaba posts sin avatar | RESUELTO en código, falta el archivo | El script compone el avatar master con `--avatar` y valida que no haya cascada ni solapamiento. Falta el PNG del master con fondo transparente, que no está en el repositorio ni en Drive |
| 4 | `AVATAR_CON_LENTES-removebg-preview.png` del repositorio es una ilustración con bob corto y aretes de perla, rasgos de Mechita, no del master | DECIDIDO, falta ejecutar | Se usa el avatar master. Pendiente: sustituir la imagen en las microclases con la foto master (necesita el archivo) |
| 5 | Uso de rojo y verde: `mmercedes-brand` los limita a tarjetas comparativas, `mmercedes-colores` los usa también en pastilla de serie y tabla | ABIERTO | Defecto: valen los usos de `mmercedes-colores`. Nunca como fondo de panel |
| 6 | Deriva de colores en el código (crema, verde, fondo del Tip, grises de la tabla) | RESUELTO | Constantes con los hex oficiales. Textos de tabla en navy. Se eliminó la línea divisoria del footer, que estaba fuera de paleta |
| 7 | Rutas fijas de una sesión anterior, herramienta `mcp__cowork__present_files` y script base de overlay inexistente | RESUELTO | Script portátil con fuentes incluidas, salida configurable con `--out`, subcomando `broll` reconstruido. Mercedes debe aprobar la primera pieza de overlay |
| 8 | Dos conceptos de B-roll (texto sin relación con la imagen frente a contenido sobre la imagen) | ABIERTO | Tres tipos nombrados en `matriz-formatos.md` |
| 9 | Guion de voz: "60 a 80 palabras" para "15 a 30 segundos" | ABIERTO | Tabla de palabras por duración en `mmercedes-video-ia` (estimación a validar con el primer video) |
| 10 | Dos bases "Calendario Editorial" en Notion, estados pensados para video grabado y tipos que no incluyen todas las series | ABIERTO | Defecto: base `a183e8c5-2108-47f1-8ebc-2475603bd675`; "Grabado" se lee como "generado" |
| 11 | Mechita pide texto generado en pantalla, pero su propio negative prompt prohíbe texto parpadeante | ABIERTO | Texto generado solo para 1 a 3 palabras. El resto se añade en CapCut o Canva |
| 12 | Hashtag fijo #NoDigasDi en piezas de otras series | ABIERTO | Se mantienen los 6 hashtags fijos |
| 13 | Imágenes generadas en cascada (bloques escalonados, con distinto margen o ancho, rotados o superpuestos) | RESUELTO en Pillow, vigilado en IA externa | Validador automático en el script. Instrucción anti-cascada en las 3 plantillas de `mmercedes-prompt-ia`, respuesta de corrección lista y punto de bloqueo en `mmercedes-qa` |
| 14 | Saturday English figura en el calendario de Notion pero ninguna skill tiene su plantilla | ABIERTO | No se tocó. Necesito un ejemplo para incorporarla a la cadena |
