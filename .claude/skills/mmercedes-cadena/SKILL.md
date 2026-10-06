---
name: mmercedes-cadena
description: Orquesta la producción completa de contenido de MMercedesEnglish, desde una idea, un error común, una reflexión o un contenido largo hasta el paquete listo para que Mercedes publique a mano en Instagram, TikTok y Facebook. Usar SIEMPRE que Mercedes diga "arma el contenido de...", "tengo esta idea", "convierte esto en posts o videos", "cadena", "pipeline", "qué publico hoy", "prepara la semana", o entregue un tema o texto sin decir qué pieza quiere.
---

# Cadena de contenido MMercedesEnglish

Una entrada se convierte en una ficha, la ficha en hasta 3 formatos, cada formato pasa por revisión y el paquete final queda listo para publicar a mano. Esta skill decide el orden y llama a las demás. No duplica lo que ya hacen los skills de producción.

Mercedes pide respuestas concisas, que se señalen los errores sin adularla, que no se genere nada que ya esté definido y que todo se revise antes de entregar.

## Las 7 etapas

| # | Etapa | Skill | Salida | Estado en Notion | Puerta |
|---|---|---|---|---|---|
| 0 | Triage de la entrada | esta skill | tipo de entrada y formatos propuestos | n/a | n/a |
| 1 | Ficha pedagógica | `mmercedes-ficha` | ficha canónica verificada | Idea a Guion | G1: inglés y pedagogía |
| 2 | Producción visual | skills de marca, ver tabla de rutas | PNG, prompt de imagen, PPTX o HTML | Guion a Grabado | n/a |
| 3 | Video con IA | `mmercedes-video-ia` | guion de voz y prompts por herramienta | Grabado | n/a |
| 4 | Revisión | `mmercedes-qa` | semáforo y Alerta de marca | Editado | G2: marca y calidad |
| 5 | Publicación | `mmercedes-publicar` | copy por plataforma, checklist, horario, fila de calendario | Publicado | G3: reglas de plataforma |
| 6 | Medición | `mmercedes-medir` | registro de resultados y ajuste del banco de ideas | n/a | n/a |

Ninguna pieza pasa a la etapa siguiente si su puerta no está en verde.

## Etapa 0: triage

Clasifica la entrada y consulta `references/matriz-formatos.md` para elegir formatos.

| Entrada | Ejemplo | Ruta típica |
|---|---|---|
| Expresión o vocabulario | "perder el impulso" | ¿Cómo se dice? |
| Error común de hispanohablantes | "I have a doubt" | No digas... Di... |
| Verbo irregular | take, took, taken | VERB ALERT o B-roll de verbos |
| Regla gramatical corta | some, any, no | Cápsula de Mechita o B-roll de texto |
| Reflexión o postura sobre aprender | "no necesitas ser perfecto" | B-roll de texto, formato C |
| Contenido largo (ebook, unidad, microclase) | Unit 6 | Atomizar en varias piezas |
| Tema sin forma | "algo sobre la hora" | Proponer 3 opciones de tipos distintos |

Si Mercedes escribe "ideología", entiéndelo como la idea o mensaje de fondo del contenido. Si el mensaje es de postura o filosofía de aprendizaje, va al formato de reflexión, no a una lección de gramática.

## Rutas de producción (etapa 2)

| Formato | Skill que lo produce | Quién ejecuta |
|---|---|---|
| Post ¿Cómo se dice? o No digas... Di... en PNG | `mmercedes-generador-posts` | Claude genera el PNG |
| Mismo post con avatar y prop vía ChatGPT o Gemini | `mmercedes-prompt-ia` | Mercedes pega el prompt |
| Corregir colores o CTA | `mmercedes-colores` | Claude |
| B-roll de texto (solo copy) | `mmercedes-broll-texto` | Claude |
| B-roll overlay PNG | `mmercedes-broll-overlay` | Claude |
| B-roll de verbo irregular (imagen) | `mmercedes-irregular-verbs` | Mercedes pega el prompt |
| Video del avatar real | `mmercedes-video-ia` (usa `mmercedes-prompt-animacion`) | Mercedes en Grok, HeyGen, D-ID o CapCut |
| Video de Mechita | `mmercedes-video-ia` (usa `mmercedes-mechita`) | Mercedes en Grok Imagine o Google Flow |
| Microclase de 6 minutos | `edicion-microclase-pptx-interactiva` | Claude genera PPTX y HTML |
| Lámina de clase | `mmercedes-evaluador-slides` | Claude evalúa |

Antes de producir cualquier pieza visual carga `mmercedes-brand`.

## Reglas de la cadena

1. Si Mercedes ya entregó los datos completos de la pieza, salta la etapa 1 y pasa a producción.
2. Pregunta solo lo que falta de verdad: nivel, serie o fecha. Si el tema es claro, propón los datos y avanza.
3. Produce solo los formatos que pidió. Los demás se mencionan en una línea como opción, sin generarlos.
4. Máximo 3 formatos por idea. Más que eso es duplicar trabajo.
5. El avatar (fotografía realista de Mercedes) y Mechita (personaje 2D) son dos identidades distintas con reglas distintas. Nunca apliques las reglas de una a la otra. Ver `references/conflictos.md`, punto 4.
6. Claude no puede generar dentro de ChatGPT, Gemini, Grok, Flow, HeyGen, D-ID ni CapCut. Entrega el prompt y la lista de verificación, y Mercedes ejecuta y devuelve el resultado para revisarlo.
7. La publicación es siempre manual y nativa en cada app. Nunca propongas programadores externos ni Meta Business Suite.
8. Nunca precios ni métodos de pago en feed ni stories.
9. Si algo rompe el sistema de marca, márcalo antes de pasar a publicación. Se registra como Alerta de marca.
10. Subir un archivo al repositorio no lo publica. Dilo cada vez que ocurra.

## Modos de trabajo

**Pieza única.** Etapas 0 a 5 para una sola idea.

**Lote semanal.** Entre 5 y 7 piezas. Reglas de rotación: no dos piezas del mismo tipo seguidas, no dos reflexiones seguidas, mezcla orientativa de 60% intermedio y 40% beginner (decisión registrada en `mmercedes-brand`). Entrega el calendario completo con `mmercedes-publicar`.

**Atomizar.** Parte de un contenido largo y extrae piezas cortas. De una microclase de 6 minutos salen, por ejemplo, 1 post de expresión, 1 post de error común y 1 video de 15 segundos. Cada pieza lleva su propia ficha.

## Entrega final

Un solo bloque por pieza:

1. Ficha (resumen de 6 líneas).
2. Assets producidos y prompts pendientes de ejecutar por Mercedes.
3. Resultado de la revisión (semáforo y Alerta de marca).
4. Paquete de publicación (copy por plataforma, checklist, horario).
5. Qué no se pudo verificar (audio real, fuentes instaladas, resultado de la IA externa) y qué falta por hacer.

## Decisiones abiertas

Hay contradicciones entre skills que cambian el resultado. Revisa `references/conflictos.md` al inicio de cada sesión. Mientras Mercedes no decida, usa el valor por defecto de cada punto y menciónalo en la entrega.
