---
name: "mmercedes-prompt-ia"
description: "Genera el prompt completo y listo para pegar en ChatGPT o Gemini para que esa IA cree una imagen de post de MMercedesEnglish. Usar SIEMPRE que Mercedes pida: \"dame el prompt para ChatGPT\", \"genera el prompt para Gemini\", \"cómo le pido a ChatGPT que haga el post de...\", \"necesito el prompt para generar la imagen de...\", o cualquier solicitud de prompt para IA externa. Cubre todas las series: ¿Cómo se dice?, No digas/Di, VERB ALERT, B-roll."
---

# MMercedesEnglish — Generador de Prompt para IA Externa

Genera el prompt completo para ChatGPT o Gemini. El prompt resultante debe ser
autosuficiente: quien lo pegue en ChatGPT sin contexto previo debe obtener una imagen
fiel al sistema de marca MMercedesEnglish.

**INSTRUCCIÓN CRÍTICA — SIEMPRE decirle a Mercedes:**
> "Sube la imagen MASTER del avatar junto con este prompt. Sin la imagen de referencia,
> ChatGPT genera un avatar con otras gafas y cabello corto, que NO es el master.
> La imagen correcta es la foto de referencia: mujer con las gafas de la foto (Mercedes tiene varios armazones, usa el de la imagen que subes), cabello hasta los hombros con canas, suéter negro, fondo blanco."

---

## BLOQUE DE AVATAR MASTER — Insertar en TODOS los prompts que lleven avatar

```
AVATAR — OBLIGATORIO usar la imagen de referencia subida:
La mujer exacta de la foto: NO cambies NADA de su apariencia.

Descripción de verificación (si no tienes imagen de referencia, usar esto):
- Mujer latina, piel morena cálida, aproximadamente 50 años
- Cabello OSCURO con CANAS/MECHONES BLANCOS prominentes, largo hasta los hombros, ONDULADO con volumen — NO es bob corto, NO es lacio
- Gafas: EXACTAMENTE las de la imagen de referencia (mismo armazón, forma y color). Mercedes tiene varios y todos son válidos
- Aretes de argolla dorada pequeños
- Suéter NEGRO cuello V · jeans o pantalón oscuro
- Expresión segura, sonrisa cálida, actitud de maestra con autoridad

POSE: [especificar según el post — default: dedo índice levantado + mano opuesta en la cadera]
PROP: [UN SOLO prop del set aprobado, sostenido en la mano derecha]
POSICIÓN: La figura sangra ligeramente por el borde DERECHO del canvas — corte intencional, sin degradado ni fade
ROSTRO: siempre completo y visible, nunca recortado

VERIFICAR ANTES DE ENTREGAR:
□ ¿Las gafas son idénticas a las de la imagen de referencia? Si no → regenerar
□ ¿El cabello es ondulado hasta los hombros? Si es bob corto → regenerar
□ ¿La mano que sostiene el prop es la mano DERECHA? Si no → regenerar
□ ¿Hay dos manos izquierdas? → regenerar
□ ¿El avatar tiene fondo blanco limpio para recorte? Si no → regenerar
```

---

## PLANTILLA — NO DIGAS... DI...

```
INSTRUCCIÓN INICIAL: Uso la imagen del avatar de referencia que subo ahora.
OBLIGATORIO: usa EXACTAMENTE la misma mujer — mismo rostro, cabello ondulado con canas
hasta los hombros, las MISMAS gafas de la foto de referencia, tono de piel morena, suéter negro.
No alteres ningún aspecto de su apariencia.

Crea una imagen post Instagram/TikTok Reel, 1080×1920px vertical 9:16, 300 DPI.

PALETA (únicos colores — ninguno más):
Navy #0D1B3E · Amarillo #FFD23F · Crema #FFFBF0 · Blanco #FFFFFF · Amarillo pálido #FFFBCC (solo fondo del Tip Mercedes) · Dorado #BE9100 (solo label "Tip Mercedes:")
Rojo #CD2823: SOLO círculo X, línea tachada, pill de serie
Verde #1E9650: SOLO círculo check y etiqueta DI
Gris #E6E6EB: bordes y divisores

ESTRUCTURA:
1. HEADER navy (~90px): Pastilla circular amarilla "MM" navy | Pastilla borde blanco "[NIVEL] English Tips" (Beginner o Intermediate según el post, nunca fija) | Pastilla roja "No digas... Di..." | Franja amarilla 8px
2. TÍTULO (fondo crema): "NO DIGAS..." navy bold + "DI" amarillo bold mismo tamaño + subrayado amarillo + estrellas amarillas
3. ZONA NO DIGAS — fondo BLANCO PURO #FFFFFF (NUNCA rojo, NUNCA rosado), borde gris recto y limpio, esquinas redondeadas: Círculo rojo + X blanca + etiqueta roja "NO DIGAS:" + [FRASE INCORRECTA] en navy bold grande + línea tachada roja al pie
4. FLECHA amarilla hacia abajo (simple, limpia)
5. ZONA DI — fondo BLANCO PURO #FFFFFF (NUNCA verde), borde amarillo recto y limpio, esquinas redondeadas: Círculo verde + check + etiqueta navy/amarillo "DI:" + [FRASE CORRECTA] en navy bold + barra amarilla al pie
6. EJEMPLOS (header navy "EJEMPLOS" amarillo): tabla 2 columnas, círculo rojo X / círculo verde check — SIN clipart, SIN íconos temáticos, SIN ilustraciones: solo los círculos
   ❌ [INCORRECTO 1] | ✅ [CORRECTO 1]
   ❌ [INCORRECTO 2] | ✅ [CORRECTO 2]
7. TIP MERCEDES (fondo amarillo pálido #FFFBCC, borde amarillo, SIN bloque adicional al lado): "Tip Mercedes:" cursivo dorado + [TIP EN ESPAÑOL — nunca en inglés]
8. CTA (franja amarilla ancho completo): burbuja navy + [CTA LÍNEA 1] + [CTA LÍNEA 2 AL LINK EN BIO]. Elegir del banco de mmercedes-colores según el tema (errores comunes, falsos cognados, etc.). En español. PROHIBIDO "Cuéntame en comentarios" y "¿Lo conocías?"
9. FOOTER navy: pastilla "MM" + "MMercedes" blanco + "English" amarillo + "Tiny Tips, Big Progress"

[INSERTAR BLOQUE DE AVATAR MASTER AQUÍ]

RESTRICCIONES ABSOLUTAS:
- NO CASCADA: todos los bloques de contenido apilados en orden vertical, con el MISMO margen izquierdo y el MISMO ancho de columna. Sin desfase escalonado, sin bloques rotados o inclinados, sin superposición entre bloques y ningún bloque detrás del avatar.
- Fondos de zona NO DIGAS y DI: RECTANGULARES, PLANOS, sin textura brush stroke ni pinceladas irregulares
- SIN clipart, íconos temáticos, ilustraciones, dibujos en los paneles
- SIN bloque "Practica Rápido" ni secciones adicionales no especificadas
- Texto de las frases: UN SOLO COLOR (navy) — no mezclar colores dentro de la misma frase
- CTA y Tip Mercedes: SIEMPRE en español
- "MMercedesEnglish" sin espacios
```

---

## PLANTILLA — ¿CÓMO SE DICE? (Opción B)

```
INSTRUCCIÓN INICIAL: Uso la imagen del avatar de referencia que subo ahora.
OBLIGATORIO: misma mujer, mismas gafas que la foto de referencia, cabello con canas hasta los hombros, suéter negro. No alteres su apariencia.

Crea una imagen post Instagram/TikTok Reel, 1080×1920px vertical 9:16, 300 DPI.

PALETA: Navy #0D1B3E · Amarillo #FFD23F · Crema #FFFBF0 · Blanco #FFFFFF
Rojo #CD2823: solo pill de serie, círculo X, etiqueta LITERAL
Verde #1E9650: solo círculo check, etiqueta SIGNIFICA

ESTRUCTURA:
1. HEADER navy: Pastilla "MM" amarilla | "[NIVEL] English Tips" borde blanco (Beginner o Intermediate según el post) | Pastilla roja "¿Cómo se dice...?" | Franja amarilla 8px
2. HOOK (fondo crema): cursiva navy "¿Cómo se dice en inglés..." + pastilla navy grande con [CONCEPTO EN ESPAÑOL] en amarillo bold
3. REVEAL (fondo navy): [EXPRESIÓN EN INGLÉS] amarillo muy grande + sublinea blanca + estrellas amarillas + franja amarilla 8px al final
4. PANEL 2 COLUMNAS (fondo crema, borde gris, PLANO sin texturas): Izq: círculo rojo+X + "LITERAL:" + [traducción en cursiva] | Der: círculo verde+check + "SIGNIFICA:" + [explicación en español] · SIN íconos clipart ni ilustraciones
5. EJEMPLOS (header navy "EJEMPLOS" amarillo): tabla 2 col EN INGLÉS / EN ESPAÑOL — 3 filas
6. TIP MERCEDES (fondo amarillo pálido, borde amarillo): "Tip Mercedes:" dorado + [TIP EN ESPAÑOL]
7. CTA (franja amarilla): burbuja navy + [CTA LÍNEA 1] + [CTA LÍNEA 2 AL LINK EN BIO], elegidos del banco de vocabulario y expresiones de mmercedes-colores. PROHIBIDO "Cuéntame en comentarios" y "¿La conocías?"
8. FOOTER navy: MM + "MMercedes" blanco + "English" amarillo + "Tiny Tips, Big Progress"

[INSERTAR BLOQUE DE AVATAR MASTER AQUÍ]

RESTRICCIONES: NO CASCADA: todos los bloques de contenido apilados en orden vertical, con el MISMO margen izquierdo y el MISMO ancho de columna. Sin desfase escalonado, sin bloques rotados o inclinados, sin superposición entre bloques y ningún bloque detrás del avatar. · sin clipart en paneles · CTA y Tip en español · sin brush strokes · sin colores fuera de paleta · "MMercedesEnglish" sin espacios
```

---

## PLANTILLA — VERB ALERT

```
INSTRUCCIÓN INICIAL: Uso imagen de referencia del avatar. Misma mujer, mismas gafas, cabello ondulado con canas.

FORMATO: 1080×1920px vertical 9:16, 300 DPI.
PALETA: Navy #0D1B3E · Amarillo #FFD23F · Crema #FFFBF0 · Blanco #FFFFFF

ESTRUCTURA:
1. HEADER navy: MM | "[NIVEL] English Tips" | "VERB ALERT 🔔" navy/amarillo
2. BADGE central: rectángulo navy + campana amarilla + "VERB ALERT" amarillo bold
3. VERBO PRINCIPAL muy grande en navy, subrayado amarillo: [VERBO]
4. TRES FORMAS en pastillas horizontales: BASE · PAST SIMPLE · PAST PARTICIPLE
5. "¿POR QUÉ ES IMPORTANTE?": 2-3 líneas en español
6. EJEMPLOS: tabla 2 col, 3 formas en contexto
7. TIP MERCEDES: [TIP EN ESPAÑOL]
8. CTA amarillo (banco de verbos de mmercedes-colores, siempre al link en bio) + FOOTER navy

[INSERTAR BLOQUE DE AVATAR MASTER AQUÍ]

RESTRICCIONES: NO CASCADA: todos los bloques de contenido apilados en orden vertical, con el MISMO margen izquierdo y el MISMO ancho de columna. Sin desfase escalonado, sin bloques rotados o inclinados, sin superposición entre bloques y ningún bloque detrás del avatar.
```

---

## PLANTILLA: SATURDAY ENGLISH (phrasal verbs y listas numeradas)

Basada en la pieza "Phrasal Verbs: GO", aprobada por Mercedes. Se genera en ChatGPT o Gemini porque lleva ilustraciones. Subir el avatar master como referencia.

```
INSTRUCCIÓN INICIAL: Uso la imagen del avatar de referencia que subo ahora.
OBLIGATORIO: misma mujer, mismas gafas que la foto de referencia, cabello con canas hasta los hombros, suéter negro cuello V. No alteres su apariencia.

Crea una imagen post Instagram/TikTok Reel, 1080×1920px vertical 9:16, 300 DPI.

PALETA (únicos colores, ninguno más):
Navy #0D1B3E · Amarillo #FFD23F · Crema #FFFBF0 · Blanco #FFFFFF · Gris #E6E6EB (bordes)
Las ilustraciones usan solo navy, amarillo, crema, blanco y tonos de piel naturales. SIN azul claro, SIN azul real, SIN lavanda.

ESTRUCTURA (de arriba abajo, una sola columna de contenido):
1. HEADER navy: badge circular amarillo "MM" + pastilla borde blanco "[NIVEL] English Tips" + franja amarilla 8px.
2. ETIQUETA "SATURDAY ENGLISH" navy bold, con dos rayitas amarillas a cada lado.
3. TÍTULO grande navy bold: [TEMA, ej. PHRASAL VERBS].
4. PASTILLA navy con el elemento central en amarillo bold: [ej. GO], con rayitas amarillas a cada lado.
5. REJILLA de 6 ítems, 2 columnas × 3 filas, todas las celdas con el mismo tamaño, el mismo margen y el mismo ancho de columna. Cada ítem:
   - círculo amarillo con el número (01 a 06) en navy
   - el término en navy bold mayúsculas
   - la traducción al español en navy, debajo del término
   - una ilustración plana pequeña a la derecha de la celda (sin texto dentro, sin emojis, estilo limpio, no kawaii)
   - franja de ejemplo debajo, fondo BLANCO con borde gris #E6E6EB, estrella navy a la izquierda y la frase con el término en navy bold
   - separador amarillo fino entre filas
   Ítems: [01 TÉRMINO / traducción / ejemplo] ... [06 ...]
6. PANEL INFERIOR con borde amarillo, 3 columnas separadas por líneas finas, SOLO en la zona izquierda (termina antes del avatar):
   [CAJA 1: título corto + 1 frase en español] [CAJA 2: "Tip Mercedes" + tip en español] [CAJA 3: CTA en español al link en bio, ej. "Para más phrasal verbs, revisa el link en mi bio."]
7. FOOTER navy: badge "MM" + "MMercedes" blanco + "English" amarillo | "Tiny Tips, Big Progress" con estrellita amarilla.

[INSERTAR BLOQUE DE AVATAR MASTER AQUÍ]
PROP: resaltador jumbo verde con el texto exacto "MMercedesEnglish" en el cuerpo (un solo prop, sostenido con la mano derecha). Verificar la ortografía del texto del resaltador.
POSICIÓN: abajo a la derecha, sangrando por el borde derecho del canvas, sin degradado. La rejilla de ítems termina ARRIBA del avatar y el panel inferior termina ANTES del avatar: ningún ítem, franja ni panel queda detrás ni debajo del avatar.

RESTRICCIONES ABSOLUTAS:
- NO CASCADA: todas las celdas de la rejilla alineadas, mismo margen izquierdo, mismo ancho de columna y mismo alto. Sin desfase, sin rotación, sin superposición.
- Ningún texto cortado ni tapado por el avatar o por una ilustración.
- Ortografía exacta de cada término y de cada frase de ejemplo.
- Tip Mercedes y CTA en español. CTA al link en bio. PROHIBIDO "Cuéntame en comentarios".
- "MMercedesEnglish" sin espacios.
```

Diferencias respecto a la pieza de muestra, aplicadas para respetar la marca: franjas de ejemplo en blanco con borde gris (la muestra usa azul claro, fuera de paleta), badge MM en lugar del foco, Tip y CTA en español, CTA al link en bio, y ningún bloque detrás del avatar (en la muestra el avatar cubre parte del ítem 06 y del panel).

---

## PLANTILLA — B-ROLL (sin avatar)

```
Crea imagen fotorrealista de ambiente para B-roll, vertical 9:16, 1080×1920px.
Estilo flat-lay o escena natural. NO infografía, NO elementos de diseño gráfico.
AMBIENTE: [descripción de escena]
PALETA: tonos cálidos/naturales — cremas, maderas, verdes naturales. Sin colores de marca como fondos.
ILUMINACIÓN: natural, cálida, suave. No sobreexpuesta.
NO incluir el avatar de la maestra en imágenes de ambiente B-roll puro.
```

---

## RESPUESTAS PARA CORREGIR ERRORES DE CHATGPT

**Gafas distintas a la referencia:**
> "Las gafas de la mujer deben ser EXACTAMENTE las de la imagen de referencia que subí: mismo armazón, forma y color. Es un detalle de identidad. Corrige las gafas y regenera."

**Cabello bob corto en lugar de ondulado:**
> "El cabello debe ser ONDULADO, con VOLUMEN, largo hasta los HOMBROS, con canas/mechones blancos prominentes. No es un corte bob corto ni lacio. Corrige y regenera."

**Avatar genérico (no usó la referencia):**
> "Debes usar la imagen de referencia que subí como base del personaje — no generes un personaje diferente. Regenera usando la foto proporcionada."

**Dos manos izquierdas:**
> "La mano que sostiene el prop es la MANO DERECHA. El pulgar en la mano derecha apunta hacia la izquierda al sostener algo. Corrige la anatomía y regenera."

**Bloques en cascada (escalonados, con distinto ancho o margen):**
> "Los bloques están en cascada. Apílalos en una sola columna vertical, todos con el mismo margen izquierdo y el mismo ancho, sin desfase, sin rotación y sin superponerlos. Ningún bloque va detrás del avatar. Regenera."

**Fondos con brush stroke / textura irregular:**
> "Los fondos de las zonas de contenido deben ser RECTANGULARES y PLANOS — sin texturas de pincelada, sin bordes irregulares. Usa rectángulos limpios con esquinas redondeadas. Regenera."

**Texto de la frase en varios colores:**
> "El texto de la frase principal debe ser un solo color: navy #0D1B3E. No mezcles colores dentro de la misma frase. Corrige y regenera."

**CTA o Tip en inglés:**
> "El Tip Mercedes y el CTA deben estar en ESPAÑOL — nunca en inglés. Tradúcelos y regenera."

