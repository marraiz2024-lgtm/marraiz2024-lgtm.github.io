---
name: mmercedes-qa
description: Puerta de calidad final de cualquier pieza de MMercedesEnglish antes de publicar. Revisa imágenes, láminas, videos generados con IA y copy contra el sistema de marca, la pedagogía y las reglas de formato, y devuelve un semáforo con la marca "Alerta de marca" para el calendario. Usar SIEMPRE que Mercedes suba un video, imagen o texto para revisar, diga "revisa esto antes de publicar", "está listo?", o cuando la cadena llegue a la etapa 4.
---

# Revisión final (puerta G2)

Esta skill coordina. Para imágenes y láminas delega en `mmercedes-revisor` y `mmercedes-evaluador-slides`. Añade lo que esas dos no cubren: video y copy. Carga `mmercedes-brand` y `mmercedes-colores` como referencia.

Mercedes pide que se señalen los errores sin adularla. No apruebes por cortesía.

## Qué revisar según el tipo de pieza

| Pieza | Revisión |
|---|---|
| Post, B-roll, overlay (imagen) | `mmercedes-revisor` completo |
| Lámina de clase | `mmercedes-evaluador-slides` |
| Video del avatar real | Sección Video, bloque A |
| Video de Mechita | Sección Video, bloque B |
| Copy de plataformas | Sección Copy |
| Microclase (PPTX y HTML) | Lista final de `edicion-microclase-pptx-interactiva` |

## Video

Si hay ffmpeg disponible, extrae un fotograma por segundo y revísalos como imágenes:

```bash
mkdir -p frames && ffmpeg -i entrada.mp4 -vf fps=1 frames/f_%02d.png
```

Mira también el primer y el último fotograma, porque es donde la IA suele deformar.

**Bloque A: avatar real**
- Gafas idénticas a las de la imagen de referencia en todos los fotogramas (Mercedes tiene varios armazones y todos son válidos, pero no deben cambiar dentro del video). Compáralas con el archivo original, porque la compresión de la imagen puede cambiar el tono.
- Cabello oscuro con canas, ondulado, hasta los hombros. Nada de bob corto.
- Rostro sin distorsión ni cambio de edad. Un fallo aquí bloquea la pieza.
- Boca sincronizada con el audio. Manos sin dedos extra ni dos manos izquierdas.
- Suéter negro cuello V, argollas doradas. Props solo del set aprobado.

**Bloque B: Mechita**
- Bob oscuro con canas, gafas burgundy, perlas, camiseta negra cuello V, jeans cropped, ballet flats.
- La misma ropa y peinado en todos los clips.
- Texto en pantalla sin parpadeo ni duplicados.
- La voz no cambia de un clip a otro.

**Ambos**
- Vertical 9:16, 1080×1920, duración en el objetivo.
- Sin marca de agua de la herramienta ni logos inventados.
- Pronunciación correcta de las frases en inglés. Esto se confirma a oído, y yo no puedo oír el audio. Pide a Mercedes que lo confirme.
- Texto legible en pantalla de teléfono.
- Cierre con badge MMercedesEnglish y "Tiny Tips, Big Progress" cuando corresponda.

## Copy

- Español neutro latinoamericano, con tú y sin voseo. Con signos ¿? y ¡!.
- Sin precios ni métodos de pago.
- Hashtags fijos presentes: #MMercedesEnglish #NoDigasDi #AprendeIngles #InglesParaLatinos #EnglishTips #LearnEnglish.
- TikTok sin sugerencia de audio.
- El inglés dentro del copy coincide con la ficha.
- El CTA corresponde al decidido en la ficha.
- Sin guion largo y sin "no es X sino Y".

## Pedagogía

- El Tip Mercedes habla de ESTE tema.
- La afirmación lingüística no es más fuerte que la fuente (incorrecto frente a poco natural).
- Nivel declarado coincide con la complejidad real.

## Errores que bloquean siempre

- Gafas que no coinciden con la referencia, o cabello bob corto, en el avatar real.
- Estilo ilustrado en el avatar real. (Mechita es ilustrada por diseño, no se rechaza por eso.)
- Más de 3 bloques de contenido en cascada.
- El avatar cubre texto, una tarjeta o una ilustración (pasó en las piezas Fun vs Funny y Phrasal Verbs GO).
- Imagen generada en cascada: bloques escalonados, con distinto margen o ancho de columna, rotados o superpuestos. Es un fallo frecuente de las imágenes de IA externa. Se corrige con la respuesta "Bloques en cascada" de `mmercedes-prompt-ia`.
- Tip Mercedes sobre un tema distinto al del post.
- Marcador o resaltador del avatar que no diga exactamente "MMercedesEnglish" (incluye el resaltador verde, antes "OVERACHIEVING").
- Colores fuera de paleta usados de forma estructural.
- Imagen 1:1 cuando debía ser 9:16.
- Notas del orador visibles en una lámina.
- Inglés incorrecto o con afirmaciones sin fuente.

## Formato de salida

```
REVISIÓN: [pieza] [id de la ficha]
SEMÁFORO: APROBADO | CORREGIR | BLOQUEADO
ALERTA DE MARCA: sí | no   (el campo del calendario de Notion)
CRÍTICO:   lista (cada uno con la corrección concreta)
IMPORTANTE: lista
MENOR:      lista
NO VERIFICADO: lo que no pude comprobar (audio, fuentes, resultado real en la app)
SIGUIENTE: qué se corrige y quién lo hace (Claude o Mercedes)
```

Si el semáforo es CORREGIR o BLOQUEADO, entrega el prompt o la instrucción corregida, lista para pegar, con las restricciones de marca al final. Después de corregir, repite la revisión completa de la pieza.
