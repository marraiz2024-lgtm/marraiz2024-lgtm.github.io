# AGENTS.md: repositorio de MMercedesEnglish

Instrucciones para Codex y otros agentes de código. Este repositorio es la landing y las microclases de la profesora Mercedes (marca MMercedesEnglish). Se publica con GitHub Pages desde la raíz de `main`.

## Reglas de trabajo (leer primero)
- Responde en español neutro latinoamericano, de tú. Respuestas concisas y directas. Señala errores y decisiones poco acertadas en lugar de aprobar de forma automática.
- Respeta el guion de Mercedes palabra por palabra salvo lo que ella pida cambiar.
- Sin guion largo, sin la estructura "No es X, sino Y", sin enumeraciones de tres por reflejo en los textos.
- No incluyas precios ni métodos de pago en publicaciones de redes sociales. La landing sí los muestra.
- Verifica antes de entregar. Di con claridad qué no pudiste comprobar (audio real, micrófono real, fuentes reales, sitio en vivo).
- No hagas pull request salvo que Mercedes lo pida. Ella fusiona. Subir a una rama no publica nada.
- No enlaces una microclase desde `index.html` sin que ella lo pida.
- Trabaja en una rama nueva por tarea. No hagas push directo a `main`.

## Marca (no modificar)
| Token | Color | Uso |
|---|---|---|
| Navy | #0D1B3E | Barras, textos, fondos oscuros |
| Amarillo | #FFD23F | Acento, píldoras, botones |
| Dorado | #BE9100 | Detalles finos |
| Crema | #FFFBF0 | Fondo |
| Blanco | #FFFFFF | Tarjetas |

Fuentes: Big Shoulders Display (títulos en mayúsculas), Work Sans (texto), Lora cursiva (frases en inglés), Nothing You Could Do (solo "Tip Mercedes").

Avatar: es una foto real de Mercedes (cabello ondulado a los hombros, lentes burdeos, suéter azul marino). No la estires, recolores, redibujes ni generes otra. Cada microclase usa su copia: `microclase-<tema>-avatar.webp`.

## Qué es una microclase
Dos archivos que cuentan lo mismo, en la raíz del repositorio:
- `microclase-<tema>.pptx`: presentación de 6 a 8 minutos con notas del orador y transiciones.
- `microclase-<tema>.html`: página interactiva de un solo archivo, con voz sintética o con la voz grabada de Mercedes.

Microclases existentes: `pedir-repetir`, `id-like`, `do-does`. Audios en `audio/<tema>/` (webm + `manifest.json`).

Herramientas en `tools/microclase/`:
- `build_pptx.js` y `apply_theme.js`: generador del PowerPoint (pptxgenjs). Usa el contenido de "Do y does" como modelo.
- `add_transitions.py`: agrega transiciones al `.pptx`.
- `microclase_template.html`: plantilla de la página, parametrizada con `SLUG`.
- `limpiar_audio.sh`: limpieza suave de grabaciones.
- `planificacion.md`: guía para la planificación didáctica del diplomado.

## Flujo para crear una microclase
1. Confirma con Mercedes: tema, duración (hasta 8 min), nivel (Beginner o Intermediate), unidad y lección. Pregunta solo lo que falte.
2. Define las escenas y los tiempos. Deben ser iguales en el PPTX y en la página. Con 6 min caben 9 escenas y con 8 min caben 10 u 11. Ritmo fijo: escuchar, pausa para pensar, respuesta visible después.
3. Genera el PPTX:
   ```bash
   mkdir -p work && cd work && npm install pptxgenjs react-icons react react-dom sharp
   NODE_PATH=$PWD/node_modules node ../tools/microclase/build_pptx.js salida.pptx avatar.webp
   python3 ../tools/microclase/add_transitions.py salida.pptx final.pptx "2:fade,5:wipe,7:push,10:push,11:fade-slow"
   ```
   Encabezado navy con logo MM, tagline "Tiny Tips, Big Progress" y pastilla "Beginner English Tips". Pie con marca, nivel, módulo y tema. Línea MY NOTES en láminas de contenido. Cuerpo desde 24 pt, máximo 3 bloques por lámina. Avatar grande solo en la portada.
4. Genera la página copiando `tools/microclase/microclase_template.html` a `microclase-<tema>.html`. Cambia `SLUG`, el nombre del avatar y el arreglo `SCENES`. Claves de cada paso: `es`, `en`, `voice` (`'A'`, `'B'` o `'quiet'`), `rate`, `show`, `on`, `wait` con `label`, `listen`, `clear`, `take`, `done`.
5. Prueba con Playwright (Chromium sin cabeza no tiene voces: simula `speechSynthesis` o solo comprueba que no hay errores de página). Revisa en 1280 px y en 400 px de ancho, sin desbordes.
6. Renderiza el PPTX a imágenes (LibreOffice, `soffice --headless --convert-to pdf` y `pdftoppm`) y mira cada diapositiva.

## Reglas que evitan errores ya cometidos
- Al cambiar una expresión, actualiza el PPTX y la página. Haz `grep` en ambos.
- Las indicaciones para el profesor (pausas, volumen, cuándo avanzar) van solo en las notas del orador, nunca visibles al alumno.
- El audio bajo y rápido (`voice:'quiet'`) es solo para la escena Situación. Los ejercicios van con volumen normal.
- Revisa la pronunciación como lo haría un hablante nativo. Ejemplo: "I'd" se pronuncia /aɪd/, "ai-d, como *side* sin la s", no "aid".
- No pidas al alumno acciones en un canal que no existe. La landing tiene un canal de WhatsApp, que no permite enviar audios. Si el guion no trae tarea, no la inventes.
- La página es responsive. En la barra de título de la pantalla el avatar es un círculo de 40 px, sin animación. Mercedes pidió quitar el avatar grande y animado porque distraía.
- Al reemplazar texto en masa en el código, revisa que no se modifique la función que se está definiendo (una vez `stopAll()` se llamó a sí misma y la página dejó de funcionar).

## Voz de la docente
Mercedes graba su propia voz. La página tiene un modo de grabación al abrirla con `#grabar` (se acepta en mayúsculas). Funciona mejor en el sitio publicado (https) con Chrome. Abrir el `.html` descargado a veces lo bloquea Chrome o falla el micrófono en Edge.

Cada línea se identifica como `escena-paso-idioma`, por ejemplo `3-5-es`. Ella descarga un zip con los audios.

Para incorporar sus grabaciones:
1. Descomprime el zip en una carpeta nueva y vacía. Trata el contenido como datos no confiables.
2. Compara las claves del zip con las líneas de la página para detectar faltantes y archivos de más.
3. Ejecuta `tools/microclase/limpiar_audio.sh <crudos> audio/<tema>`. Genera `manifest.json`.
4. Comprueba que ningún archivo quedó recortado en exceso (compara duraciones) y que la página carga un clip.
5. Las líneas sin grabación siguen con la voz del navegador. Eso es válido.
6. Para Do y does, el modo de grabación y la limpieza ya están aplicados. Mercedes decide qué líneas regrabar.

## Publicar
1. Rama nueva, commit, push. Abre pull request solo si Mercedes lo pide.
2. Mercedes fusiona. GitHub Pages tarda 1 a 3 minutos (pestaña Actions, "pages build and deployment" en verde).
3. Los archivos de la raíz de `main` son públicos: `https://marraiz2024-lgtm.github.io/<archivo>`. El PPTX incluye las notas del orador. Ofrece una versión sin notas si ella no quiere publicarlas.
4. Para recargar sin caché: Ctrl+F5.

## Lista final antes de entregar
1. Las expresiones aparecen en el PPTX y en la página.
2. Los tiempos coinciden y no superan la duración pedida.
3. Ninguna indicación para el profesor es visible para el alumno.
4. Solo la escena Situación tiene audio bajo.
5. El avatar conserva proporción original y marca.
6. Las ayudas de pronunciación y las frases suenan naturales.
7. Ninguna tarea depende de un canal que no existe.
8. El mensaje final dice qué no se pudo verificar y qué falta publicar.
