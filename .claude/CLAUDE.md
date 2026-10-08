# MMercedesEnglish: contexto del proyecto

Este repositorio es el sitio web (GitHub Pages) de MMercedesEnglish, la marca de Mercedes, profesora de inglés que enseña inglés práctico a hispanohablantes. Aquí también vive la cadena de skills que convierte una idea en piezas para Instagram, TikTok y Facebook. Tagline fijo: "Tiny Tips, Big Progress".

## Cómo trabajar con Mercedes

- Español neutro latinoamericano, con tú. Respuestas concisas, claras y directas.
- Señala errores y decisiones poco acertadas sin adular. No repitas lo que ella ya explicó.
- Prohibido: guion largo, la estructura "No es X sino Y", enumeraciones de tres elementos por reflejo, clichés y cierres con preguntas genéricas.
- Pregunta solo lo imprescindible. No generes imágenes ni contenido que ya tiene parámetros definidos o que ella no pidió.
- Revisa todo antes de entregarlo. Di con claridad qué no pudiste verificar (audio, fuentes instaladas, resultado en herramientas externas).
- Afirmaciones lingüísticas con fuente concreta (Cambridge, Merriam-Webster, Oxford Learner's, Collins) o marcadas como opinión fundamentada. Distingue "incorrecto" de "poco natural".
- Atajo "pp": si ella escribe "pp" seguido de un prompt, conviértelo en un prompt RTIC (Rol, Tarea, Instrucción, Contexto). Si falta contexto, pregunta.

## Empieza por aquí

Para cualquier tarea de contenido (posts, B-roll, videos, microclases, publicación, calendario), usa primero la skill `mmercedes-cadena` (`.claude/skills/mmercedes-cadena/SKILL.md`). Ella decide el orden y llama a las demás. Antes de producir cualquier pieza visual consulta `mmercedes-brand` y `mmercedes-colores`.

La cadena tiene 7 etapas: triage, ficha (puerta 1: inglés), producción visual, video con IA, revisión (puerta 2: marca), publicación (puerta 3: plataforma) y medición. Una pieza no pasa a la etapa siguiente si su puerta no está en verde.

Manual completo para otras IA: `.claude/skills/mmercedes-cadena/references/MANUAL_CADENA_MMERCEDESENGLISH.md`.
Contradicciones y decisiones: `.claude/skills/mmercedes-cadena/references/conflictos.md`. Léelo al inicio de cada sesión.

## Reglas que nunca se rompen

1. Paleta única: Navy #0D1B3E, Amarillo #FFD23F, Crema #FFFBF0, Blanco #FFFFFF. Rojo #CD2823 y Verde #1E9650 solo en X, check, etiquetas y pastilla de serie, nunca como fondo de panel. Amarillo pálido #FFFBCC solo en el Tip Mercedes, Dorado #BE9100 solo en su label, Gris #E6E6EB en bordes. Sin gradientes ni texturas.
2. Tipografía: BigShoulders-Bold (títulos), WorkSans (cuerpo), Lora Italic (hooks), NothingYouCouldDo solo en "Tip Mercedes:". Nunca Poppins ni Nunito.
3. Posts de redes: 1080×1920, vertical 9:16.
4. Nunca en cascada: todos los bloques con el mismo margen izquierdo y ancho de columna, sin escalones, rotación ni superposición, y ningún bloque detrás del avatar.
5. Pastilla de nivel dinámica ("Beginner English Tips" o "Intermediate English Tips"), nunca fija.
6. Tip Mercedes y CTA siempre en español. El CTA siempre dirige al link en bio y se elige según el tema. Prohibidos "Cuéntame en comentarios", "¿Lo conocías?" y "¿La conocías?".
7. Avatar: fotografía realista de Mercedes, nunca ilustración. Gafas idénticas a la imagen de referencia y estables dentro de la pieza (ella tiene varios armazones). Un solo prop del set aprobado por pieza. Si el prop es resaltador o marcador, su texto es exactamente "MMercedesEnglish".
8. Mechita es un personaje 2D distinto del avatar. No mezcles sus reglas.
9. "MMercedesEnglish" siempre junto y con esa ortografía.
10. Nunca precios ni métodos de pago en feed ni stories.
11. La publicación es siempre manual y nativa. Nunca Meta Business Suite ni programadores. En TikTok el audio trending se añade dentro de la app y nunca se sugiere.
12. Hashtags fijos: #MMercedesEnglish #NoDigasDi #AprendeIngles #InglesParaLatinos #EnglishTips #LearnEnglish.
13. Si una pieza rompe el sistema de marca, márcala como "Alerta de marca" antes de publicar.

## Dónde está cada cosa

- Skills de la cadena: `.claude/skills/`. Las skills de la cuenta de Mercedes en claude.ai son las que se cargan en sus chats. Estas copias son la fuente, y ella las sube.
- Generador de posts: `.claude/skills/mmercedes-generador-posts/assets/mm_posts.py` (series ¿Cómo se dice?, No digas... Di..., Inglés básico y B-roll). Valida paleta, nivel, CTA y cascada.
- La foto del avatar nunca se sube a este repositorio, que es público. Vive dentro de la skill en la cuenta de Mercedes (`assets/avatar/`), y el archivo `.gitignore` de `.claude/skills` la excluye.
- Calendario editorial: base de Notion "Calendario Editorial" (`a183e8c5-2108-47f1-8ebc-2475603bd675`).

## Reglas del repositorio

- Desarrolla en la rama indicada por la sesión. No abras pull request salvo que Mercedes lo pida. Fusiona ella, porque decide qué se publica.
- Subir un archivo a una rama no lo publica. Dilo cada vez que haya confusión.
- El sitio es público: todo lo que esté en la raíz de `main` queda accesible en la web. No pongas ahí nada privado.
- `README.md` y `index.html` son de la landing. No los modifiques sin que ella lo pida.
- Las microclases (`microclase-*.html` y `.pptx`) no se enlazan desde `index.html` sin que ella lo pida.
