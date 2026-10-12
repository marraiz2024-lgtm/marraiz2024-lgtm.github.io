---
name: mmercedes-generador-posts
description: Genera automáticamente el PNG 1080×1920px de un post de MMercedesEnglish, series ¿Cómo se dice? (Opción B), No digas/Di e Inglés básico, con el avatar master opcional, el CTA que trae la ficha y la variante de naturalidad sin X ni check. Usar SIEMPRE que Mercedes pida "genera el post de...", "arma el post de...", "crea la imagen para...", "haz el PNG de...", o dé el tema o contenido de un post nuevo para Instagram o TikTok. Los posts se componen por código: no requiere ni usa modelos de imágenes.
---

# MMercedesEnglish: generador de posts PNG

Genera el PNG 1080×1920 con Python y Pillow. El script, las fuentes y los ejemplos viajan dentro de esta skill, así que no dependen de rutas de sesión ni de otras skills.

Las series ¿Cómo se dice?, No digas... Di... e Inglés básico funcionan bien. No cambies su estructura, sus colores ni sus fuentes. Lo único que varía es el contenido, el nivel, el CTA y la capa opcional del avatar.

```
mmercedes-generador-posts/
  SKILL.md
  assets/
    mm_posts.py          generador (subcomandos como-se-dice, no-digas, ingles-basico, broll)
    fonts/               BigShoulders, WorkSans, Lora, NothingYouCouldDo (licencia OFL)
    ejemplos/            un JSON de ejemplo por serie
    avatar/master.png    (opcional) recorte del avatar master, fondo transparente
```

## Paso 1: contenido

Pregunta solo lo que falte. Si ya tienes la ficha de `mmercedes-ficha`, úsala sin preguntar de nuevo. Verifica el inglés antes de generar.

**¿Cómo se dice?**: `concepto_es`, `expresion_en`, `subtitulo`, `literal`, `significa`, 3 `ejemplos` [EN, ES], `tip`.
**No digas... Di...**: `frase_mal` y `frase_bien` (2 líneas cada una), 2 `ejemplos` [incorrecto, correcto], `tip` y `modo`. `modo: "error"` (por defecto) usa X roja y check verde y solo vale para un error genuino. `modo: "naturalidad"` se usa cuando la frase es gramatical y solo es menos natural, de otro registro o contexto, o una variante válida: omite X y check, y usa etiquetas neutras (`etiqueta_mal`, por defecto "COMÚN:"; `etiqueta_bien`, por defecto "MÁS NATURAL:"; y `titulo_1` y `titulo_2`, por defecto "EN VEZ DE..." y "DI").
**Inglés básico** (serie aprobada por Mercedes; ya publicadas: TO BE, THERE IS / THERE ARE y A / AN): `titulo_1`, `titulo_2`, `subtitulo`, 2 o 3 `columnas` con `cabecera`, `con` y 2 `ejemplos` (un `*asterisco*` pone negrita y `\n` fuerza un salto), y `tip` en español. Ejemplos: `assets/ejemplos/ingles_basico_to_be.json` (3 columnas) y `ingles_basico_a_an.json` (2 columnas).
**Todas las series**: `nivel` ("Beginner" o "Intermediate"), `cta` (obligatorio, ver el Paso 2) y `salida` (nombre descriptivo del PNG).

El nivel es obligatorio de decidir en cada post porque la pastilla del header lo muestra. Si Mercedes no lo dice, deduce el nivel real del contenido, no dejes "Beginner" por defecto.

Para el tip, cada elemento de la lista es un párrafo, y un elemento que empieza con `**` va en negrita. El script ajusta los saltos de línea.

## Paso 2: CTA (viene de la ficha)

Decisión de Mercedes (10 de octubre de 2026): el copy completo del CTA viene de la ficha (handoff editorial) y el script no lo inventa. Se pasa en `cta`, con dos líneas:

1. Primera línea: una acción concreta sobre lo aprendido, por ejemplo "Repite en voz alta: Don't lose momentum!".
2. Segunda línea: dirige al link en bio, por ejemplo "Más expresiones como esta en el link de mi bio.".

Puede pedir comentar solo si es lógico y específico del post (por ejemplo, "Completa en comentarios: I agree with ___" en un post sobre *agree*). El script avisa en esos casos para que se confirme.

El script se detiene si el CTA falta, si no menciona el link en bio o si es genérico ("Cuéntame en comentarios", "¿Lo conocías?", "¿La conocías?", "¿Cuál usas tú?", "Sígueme para más", y variantes). El banco histórico de frases ya no es fuente. Si la ficha no trae CTA, el campo queda pendiente y se devuelve a Mercedes.

## Paso 3: avatar master

- Con avatar: `--avatar NOMBRE` (un PNG de `assets/avatar/`), una ruta, o la variable `MM_AVATAR`. Con un solo PNG en `assets/avatar/` se usa ese.
- El archivo debe ser el recorte del MASTER (fotografía, fondo transparente). El script se detiene si el PNG no tiene transparencia. Nunca estira la imagen: un solo factor de escala para X e Y.
- Con avatar, el contenido se estrecha solo en la zona superior (gancho y reveal en ¿Cómo se dice?, título y bloque NO DIGAS en No digas) y el avatar sangra por el borde derecho sin cubrir ningún bloque. Sin avatar, el layout es el original completo.
- Si el master no está disponible, genera sin avatar, dilo en la entrega y no uses ninguna ilustración como sustituto.
- No incluyas el avatar en el B-roll de ambiente (regla de `mmercedes-revisor`).
- Mercedes es zurda: en fotos o poses nuevas el prop va en la mano izquierda. Las gafas son rectangulares, burdeos/rojas o negras, y nunca cat-eye ni redondas. El master actual (resaltador verde) se aprobó antes de la regla de mano izquierda, así que se revisa si se regenera.
- La foto de Mercedes no se sube a repositorios públicos. Guárdala solo dentro de la skill en la cuenta de Mercedes.
- Cada versión del master (cada prop o par de gafas) es un PNG distinto dentro de `assets/avatar/`. El prop puede variar siempre que esté en el set aprobado, y las gafas pueden variar porque Mercedes tiene varios armazones. Elige el archivo con `--avatar NOMBRE` y mira los disponibles con `--listar-avatares`. Si hay varios y no eliges, el script se detiene y los lista.
- El master incluye su propio prop, que cuenta como el único prop de la pieza. No añadas otro.
- Si el prop es un resaltador o marcador, el texto del cuerpo debe decir exactamente "MMercedesEnglish". Revísalo antes de guardar un master nuevo.

## Paso 4: ejecutar

```bash
SCRIPT=$(find . ~/.claude /mnt -path '*mmercedes-generador-posts/assets/mm_posts.py' 2>/dev/null | head -1)
python3 "$SCRIPT" como-se-dice contenido.json --out ./salida --avatar master.png
python3 "$SCRIPT" no-digas     contenido.json --out ./salida
python3 "$SCRIPT" ingles-basico contenido.json --out ./salida    # serie Inglés básico (2 o 3 columnas)
python3 "$SCRIPT" broll        contenido.json --out ./salida     # ver mmercedes-broll-overlay
```

Requiere Python 3 y Pillow (`pip install pillow`). El script crea la carpeta de salida. Si la sesión ofrece una herramienta para mostrar archivos, úsala. Si no, entrega la ruta.

## Guardia anti-cascada

Cada bloque de contenido se registra al dibujarse y el script valida el layout antes de guardar el PNG. Se detiene con un mensaje si encuentra:

- bloques con distinto margen izquierdo,
- bloques con distinto ancho de columna (fuera de la zona junto al avatar, donde todos comparten el mismo ancho),
- bloques superpuestos o desfasados,
- el avatar cubriendo cualquier bloque o texto.

No desactives la validación ni "arregles" el error moviendo un solo bloque. Si salta, revisa el contenido (texto demasiado largo, ejemplos de más) y regenera.

## Paso 5: revisar antes de entregar

Abre el PNG y verifica:

0. Sin cascada: todos los bloques alineados al mismo margen y ancho de columna (el script lo valida).
1. 1080×1920 y solo colores de la paleta oficial (ver abajo).
2. Pastilla de nivel correcta para el post.
3. Texto sin cortar ni solapado. Si una zona no cabe, el script reduce solo la tipografía de ese texto. Si aun así no cabe, acorta el contenido.
4. Tip Mercedes sobre el tema de este post, en español.
5. CTA de la ficha, en español, específico de la lección y con dirección al link en bio.
6. Con avatar: gafas rectangulares burdeos/rojas o negras iguales a la referencia, texto del prop "MMercedesEnglish", prop en la mano izquierda en poses nuevas, rostro completo, sin estirar.
7. Nombre del archivo descriptivo del tema.

Pasa el resultado por `mmercedes-qa` antes de publicar.

## Paleta oficial (constantes del script)

Navy #0D1B3E, Amarillo #FFD23F, Crema #FFFBF0, Blanco #FFFFFF, Rojo #CD2823 (solo X, tachado, etiqueta y pastilla de serie), Verde #1E9650 (solo check y etiqueta), Amarillo pálido #FFFBCC (solo Tip), Dorado #BE9100 (solo label del Tip), Gris #E6E6EB (bordes). Gris de tagline del footer (200,200,215), tal como está en `mmercedes-colores`.

Cambios respecto a la versión anterior de los scripts, todos para respetar la paleta: crema pasó de #FFFCF2 a #FFFBF0, verde de #1E9641 a #1E9650, fondo del Tip de #FFF8D7 a #FFFBCC, el texto gris azulado de la tabla de ejemplos pasó a navy y se eliminó la línea divisoria del footer, que era un color fuera de paleta.

## Inglés básico

Serie de tarjetas de gramática para nivel Beginner. El formato (header con tagline, título grande con el tema sobre una pastilla amarilla, subtítulo con subrayado, tarjetas en fila, Tip Mercedes y footer) es el de las piezas ya publicadas. Admite 2 columnas (A / AN, THERE IS / THERE ARE) o 3 (AM / IS / ARE). No lleva avatar. Dos diferencias deliberadas respecto a las piezas publicadas:

- El Tip Mercedes va en español (la pieza TO BE lo tenía en inglés, y la regla de marca pide español).
- Lleva CTA al link en bio entre el Tip y el footer (las piezas publicadas no tenían CTA). Si Mercedes prefiere la versión sin CTA, se quita la llamada a `cta_block` en `_tres`.

Las tarjetas en fila cuentan como un solo bloque para la guardia anti-cascada. El espacio sobrante se reparte entre los bloques para no dejar un hueco vacío.

## Saturday English y VERB ALERT

No tienen renderer por código todavía. Como ningún modelo de imágenes dibuja el post, estas dos series quedan pendientes de un renderer (con sus ilustraciones como assets). La especificación de diseño está en `references/especificaciones-series.md`. Hasta entonces no se producen con IA externa.

## Reglas finales

- Nunca cambiar colores, fuentes ni estructura del layout.
- Nunca inventar contenido. Si falta un dato, preguntar.
- Si el texto de una zona es muy largo, se reduce la tipografía de esa zona, no la zona.
- Subir un archivo al repositorio no lo publica en redes. La publicación la hace Mercedes a mano.
