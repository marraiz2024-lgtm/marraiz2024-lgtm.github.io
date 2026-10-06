---
name: mmercedes-generador-posts
description: Genera automáticamente el PNG 1080×1920px de un post de MMercedesEnglish, series ¿Cómo se dice? (Opción B), No digas/Di e Inglés básico, con el avatar master opcional y el CTA al link en bio elegido según el tema. Usar SIEMPRE que Mercedes pida "genera el post de...", "arma el post de...", "crea la imagen para...", "haz el PNG de...", o dé el tema o contenido de un post nuevo para Instagram o TikTok. No requiere ChatGPT ni Gemini, Claude genera el PNG directamente.
---

# MMercedesEnglish: generador de posts PNG

Genera el PNG 1080×1920 con Python y Pillow. El script, las fuentes y los ejemplos viajan dentro de esta skill, así que no dependen de rutas de sesión ni de otras skills.

Las series ¿Cómo se dice?, No digas... Di... e Inglés básico funcionan bien. No cambies su estructura, sus colores ni sus fuentes. Lo único que varía es el contenido, el nivel, el CTA y la capa opcional del avatar.

```
mmercedes-generador-posts/
  SKILL.md
  assets/
    mm_posts.py          generador (subcomandos como-se-dice, no-digas, broll)
    fonts/               BigShoulders, WorkSans, Lora, NothingYouCouldDo (licencia OFL)
    ejemplos/            un JSON de ejemplo por serie
    avatar/master.png    (opcional) recorte del avatar master, fondo transparente
```

## Paso 1: contenido

Pregunta solo lo que falte. Si ya tienes la ficha de `mmercedes-ficha`, úsala sin preguntar de nuevo. Verifica el inglés antes de generar.

**¿Cómo se dice?**: `concepto_es`, `expresion_en`, `subtitulo`, `literal`, `significa`, 3 `ejemplos` [EN, ES], `tip`.
**No digas... Di...**: `frase_mal` y `frase_bien` (2 líneas cada una), 2 `ejemplos` [incorrecto, correcto], `tip`.
**Inglés básico** (serie aprobada por Mercedes; ya publicadas: TO BE, THERE IS / THERE ARE y A / AN): `titulo_1`, `titulo_2`, `subtitulo`, 2 o 3 `columnas` con `cabecera`, `con` y 2 `ejemplos` (un `*asterisco*` pone negrita y `\n` fuerza un salto), y `tip` en español. Ejemplos: `assets/ejemplos/ingles_basico_to_be.json` (3 columnas) y `ingles_basico_a_an.json` (2 columnas).
**Ambas** (¿Cómo se dice? y No digas): `nivel` ("Beginner" o "Intermediate"), `tema` (palabra clave, sirve para variar el CTA), `salida` (nombre descriptivo del PNG).

El nivel es obligatorio de decidir en cada post porque la pastilla del header lo muestra. Si Mercedes no lo dice, deduce el nivel real del contenido, no dejes "Beginner" por defecto.

Opcionales: `cta` (dos líneas, para forzar uno), `cta_categoria`, `falso_cognado: true` (en No digas).

Para el tip, cada elemento de la lista es un párrafo, y un elemento que empieza con `**` va en negrita. El script ajusta los saltos de línea.

## Paso 2: CTA (elegir en cada caso)

El CTA siempre dirige al link en bio, en español, y habla del tema de la pieza. El script lo elige de este banco según la serie:

| Serie | Categoría |
|---|---|
| ¿Cómo se dice? | Vocabulario y expresiones |
| No digas... Di... | Errores comunes (o Falsos cognados si `falso_cognado` es true) |
| B-roll overlay | Universales |

Dentro de la categoría el script varía de forma reproducible según `tema`: el mismo tema siempre produce el mismo CTA, y temas distintos producen CTAs distintos. Si ninguna opción encaja con el tema, pasa `cta` con dos líneas escritas por ti, en el estilo del banco de `mmercedes-colores`.

El script rechaza con error cualquier CTA que pida comentar ("Cuéntame en comentarios", "¿Lo conocías?") o que no mencione el link en bio.

## Paso 3: avatar master

- Con avatar: `--avatar ruta/master.png`, o la variable `MM_AVATAR`, o el archivo `assets/avatar/master.png` dentro de esta skill.
- El archivo debe ser el recorte del MASTER (fotografía, fondo transparente). El script se detiene si el PNG no tiene transparencia. Nunca estira la imagen: un solo factor de escala para X e Y.
- Con avatar, el contenido se estrecha solo en la zona superior (gancho y reveal en ¿Cómo se dice?, título y bloque NO DIGAS en No digas) y el avatar sangra por el borde derecho sin cubrir ningún bloque. Sin avatar, el layout es el original completo.
- Si el master no está disponible, genera sin avatar, dilo en la entrega y no uses ninguna ilustración como sustituto.
- No incluyas el avatar en el B-roll de ambiente (regla de `mmercedes-revisor`).
- La foto de Mercedes no se sube a repositorios públicos. Guárdala solo dentro de la skill en la cuenta de Mercedes.

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
5. CTA en español, al link en bio, sobre el tema de la pieza.
6. Con avatar: gafas burgundy, cabello ondulado, rostro completo, sin estirar.
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

## Saturday English

Se genera en ChatGPT o Gemini porque lleva ilustraciones. La plantilla está en `mmercedes-prompt-ia` ("SATURDAY ENGLISH") y no se produce con este script.

## Reglas finales

- Nunca cambiar colores, fuentes ni estructura del layout.
- Nunca inventar contenido. Si falta un dato, preguntar.
- Si el texto de una zona es muy largo, se reduce la tipografía de esa zona, no la zona.
- Subir un archivo al repositorio no lo publica en redes. La publicación la hace Mercedes a mano.
