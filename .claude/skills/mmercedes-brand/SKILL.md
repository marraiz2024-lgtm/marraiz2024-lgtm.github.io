---
name: "mmercedes-brand"
description: "Sistema de marca visual de MMercedesEnglish (colores, tipografía, avatar fotográfico realista, props, y la plantilla real de posts \"No digas...Di.../¿Cómo se dice...?\"). Usar SIEMPRE que se genere o edite cualquier pieza visual de la marca — posts, Stories, portadas, workbooks, ebooks, presentaciones, brochures, flashcards. Aplica incluso si el usuario no menciona explícitamente \"marca\" o \"avatar\"; cualquier solicitud de diseño o imagen para MMercedesEnglish debe activar este skill primero."
---


# Sistema de marca — MMercedesEnglish

## Paleta de colores
- Navy: `#0D1B3E`
- Amarillo: `#FFD23F`
- Gold/dorado: `#BE9100` (tono amarillo apagado, uso en "Tip Mercedes:" y en el sello de calidad)
- Crema: `#FFFBF0`
- Blanco: uso libre como fondo base
- Rojo `#CD2823` y Verde `#1E9650`: permitidos SOLO en tarjetas comparativas explicativas (❌/✅), nunca en quizzes ni como fondo estructural

## Tipografía
- **BigShoulders-Bold** — títulos y headlines grandes (reveals, "NO DIGAS...DI")
- **WorkSans** Regular/Bold — cuerpo, tablas de ejemplos, labels
- **Lora-Italic** — hooks y texto en itálica (ej. traducción LITERAL)
- **NothingYouCouldDo** — cursiva manuscrita, SOLO para el label "Tip Mercedes:"
- ❌ No Poppins/Nunito — esa fue una especificación anterior, ya no vigente. No usar.

## Avatar oficial — MASTER CONFIRMADO (agosto 2026)

**El avatar es fotografía 100% realista.** Nunca ilustración, dibujo, pintura ni estilo pictórico.

### Descripción física exacta del MASTER (NO negociar ningún elemento):

**Cabello:** oscuro (negro/castaño oscuro) con canas/mechones blancos prominentes, especialmente en la parte frontal y lateral. Largo hasta los hombros o ligeramente por encima. Ondulado/con volumen natural. **NO es un bob corto. NO es lacio. El cabello tiene movimiento y longitud notable.**

**Gafas:** armazón BURGUNDY/VINO/ROJO OSCURO, forma rectangular-cuadrada. **NO son negras. NO son café. Son específicamente color vino/burgundy rojizo.** Este es el detalle más frecuentemente errado — verificar siempre, incluido en video (no solo en posts estáticos). Si un video o imagen generada muestra gafas negras, se marca como error de marca y se pide corrección.

**Tono de piel:** morena cálida, latina.

**Aretes:** argolla dorada pequeña/mediana.

**Ropa:** suéter negro cuello V (a veces navy). Jeans azul oscuro o pantalón oscuro.

**Expresión:** segura, sonrisa sutil o plena, actitud de maestra con autoridad y calidez.

**Pose master aprobada:** dedo índice levantado señalando hacia arriba + mano opuesta en la cadera. Usar como referencia base salvo que se especifique otra pose. En video narrado/gesticulado, la pose puede variar de forma natural (escribiendo, señalando el contenido) siempre que el resto del avatar (gafas, cabello, ropa) se mantenga fiel al master.

**Fondo:** blanco puro para recorte limpio en posts estáticos. En video narrado con avatar de cuerpo/escritorio, se permite fondo de oficina/estudio realista (librero, planta), siempre que el avatar en sí mantenga las características físicas del master.

**Proporciones:** anatómicamente correctas. Nunca elongar brazos, cuello ni torso.

### Fuente del avatar
Siempre el PNG recortado del MASTER (fotografía, fondo transparente). No se usa ninguna ilustración como avatar. Los scripts de Pillow lo componen con `--avatar` (ver `mmercedes-generador-posts`). Si ese archivo no está disponible, se genera el post sin avatar y se avisa a Mercedes.

### Regla del avatar en posts:
- Recorte con fondo transparente antes de integrar a plantilla
- Sangra por el borde derecho del canvas — corte intencional, sin fade ni degradado
- NUNCA cortar a través de un brazo doblado, codo, o hueco entre brazo y torso
- El rostro siempre completo y visible

### Errores más frecuentes a prevenir:
- Gafas negras en lugar de burgundy → rechazar y pedir corrección (verificar también en video, no solo en imagen estática)
- Cabello bob corto en lugar de ondulado hasta los hombros → rechazar
- Avatar con fondo no blanco en la foto de recorte (posts estáticos) → rechazar
- Estilo ilustrado/pictórico → rechazar inmediatamente
- Íconos de check/estado duplicados o superpuestos en un mismo bloque (ej. dos círculos de check distintos sobre el mismo elemento) → simplificar a un solo ícono por estado

## Props de enseñanza sobredimensionados

Set aprobado — UN SOLO prop por publicación, interactuando con el contenido:
- Lápiz gigante (amarillo, punta negra, borrador rosa)
- Marcador/Sharpie gigante (blanco, "PERMANENT MARKER")
- Pizarra pequeña con base de madera + tiza
- Resaltador jumbo verde ("OVERACHIEVING")
- Resaltador jumbo amarillo ("WHAT'S GOING ON")
- Resaltador jumbo naranja ("TOLD YOU SO")
- Mano señaladora en palo (pointer hand)

El prop interactúa con el contenido, nunca flota decorativo. En video narrado se permite además utilería de escritorio realista (cuaderno, taza con logo MMercedesEnglish) como parte de la escena, sin que sustituya el prop sobredimensionado en posts estáticos.

Estilo: realista y premium, nunca caricaturesco.

## Correcciones de defectos detectados

**Elongación:** escalar el avatar siempre con proporción original — nunca distinto factor en X y Y. El prop conserva su proporción real fotografiada.

**Cascada:** todos los bloques de contenido comparten mismo margen izquierdo y ancho de columna. Ningún bloque detrás del avatar. No rotar tarjetas de contenido de forma independiente.

## Plantilla real de posts — 1080 × 1920 px (9:16)

**Header:** Badge "MM" amarillo circular + pastilla de nivel (dinámica) + pastilla de serie + franja amarilla 8px

### Pastilla de nivel (header, esquina izquierda, reemplaza a la antigua "Beginner English Tips" fija)

Texto dinámico según el post:
- **"Beginner English Tips"** si el contenido es de nivel principiante
- **"Intermediate English Tips"** si el contenido es de nivel intermedio (plural "Tips", igual que en la versión beginner, para que ambas se vean consistentes entre sí)

Esta pastilla identifica el nivel de cada post individual. No hay un tercer valor genérico aquí — cada post declara su nivel real.

### Sello de calidad "English Your Way"

Reemplaza la idea original de pastilla rectangular para "English Your Way". Ahora es un sello circular tipo medallón de calidad (estilo "Certified" / "100% Guaranteed"), **no** un sello postal (sin borde perforado).

Especificación visual:
- Forma: círculo con borde festoneado suave (roseta de picos redondeados, no puntiagudos)
- Relleno: Navy `#0D1B3E`
- Anillo/borde: Amarillo apagado, usar **Gold `#BE9100`** (no el amarillo brillante `#FFD23F`, para que no se vea "escandaloso")
- Texto interior: dos líneas centradas, "ENGLISH" arriba y "YOUR WAY" abajo, en `BigShoulders-Bold`, color blanco o amarillo brillante para contraste contra el navy
- Remate: una estrellita pequeña (mismo motivo `star()` ya usado en las plantillas) sobre el texto, en Gold o amarillo
- Ubicación: cerca del avatar (esquina donde no interfiera con el prop ni con los bloques de contenido), no en la fila de header junto a las pastillas de nivel/serie

## Sobre la segmentación por nivel (beginner / intermediate) — historial de decisiones

Se evaluaron y descartaron: un badge motivacional fijo tipo "Avanza" (generaba confusión con contenido de post existente) y su versión en inglés "Keep Going" (mismo problema). La solución vigente es la pastilla de nivel dinámica descrita arriba. Además, la mezcla editorial orientativa sigue siendo 60/40 a favor de intermedio en el calendario, sin que el beginner desaparezca.

**Cuerpo:** Título principal con subrayado amarillo + Avatar + prop + Bloques comparativos (❌ rojo / ✅ verde solo en contenido explicativo) + Ejemplos bilingüe + Tip Mercedes en ESPAÑOL

**CTA:** Frase en ESPAÑOL sobre el tema de la pieza + línea que dirige al link en bio (banco y reglas de selección en `mmercedes-colores`). Retirados: "Cuéntame en comentarios" y "¿Lo conocías?"

**Footer:** Logo MM + "MMercedes" blanco + "English" amarillo + "Tiny Tips, Big Progress"

## Tagline fijo
**"Tiny Tips, Big Progress"**

## Qué NO hacer
- Avatar ilustrado, pictórico, con gafas negras, con bob corto → NO (aplica también en video)
- Degradado/fade en borde del avatar → NO (usar sangrado por borde del canvas)
- Más de un prop sobredimensionado por publicación estática → NO
- Verde/rojo en quizzes o como fondo estructural → NO
- CTA o Tip Mercedes en inglés → NO
- CTA que pida comentar ("Cuéntame en comentarios", "¿Lo conocías?") → NO
- Colores fuera de paleta → NO
- "MMercedesEnglish" con espacios o mal escrito → NO
- Dejar la pastilla de nivel fija en "Beginner" para todo el contenido → NO (debe reflejar el nivel real del post)
- Badge motivacional de nivel tipo "Avanza" / "Keep Going" → NO (evaluado y descartado)
- Sello "English Your Way" con borde perforado tipo estampilla postal, o en amarillo brillante `#FFD23F` → NO (debe ser borde festoneado tipo sello de calidad, en Gold `#BE9100`)

## Verificación antes de entregar
1. ¿Avatar foto realista con gafas BURGUNDY y cabello ondulado hasta los hombros? (verificar también en video)
2. ¿Recortado, sangrando por borde del canvas sin fade (posts estáticos)?
3. ¿Un solo prop sobredimensionado interactuando con el contenido?
4. ¿Pastilla de nivel correcta según el post (Beginner/Intermediate English Tips)?
5. ¿Sello "English Your Way" con forma de medallón festoneado, navy y borde Gold, dos líneas centradas?
6. ¿Formato 1080×1920 vertical?
7. ¿CTA (al link en bio) y Tip Mercedes en español?
8. ¿Colores dentro de paleta?

