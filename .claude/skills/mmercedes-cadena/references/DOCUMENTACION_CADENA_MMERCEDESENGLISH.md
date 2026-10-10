# Documentación de la cadena de skills de MMercedesEnglish

Documento técnico y de uso. Describe qué es la cadena, cómo está construida, qué hace cada pieza, qué decisiones se tomaron, cómo se instala, qué se probó y qué falta. Se redactó a partir de los archivos del repositorio `marraiz2024-lgtm.github.io`, carpeta `.claude/`, en la rama `ccr-79e9e06c-fmjdpa`.

---

## 1. Resumen

La cadena convierte una idea (una expresión, un error común, una regla, una reflexión o un contenido largo) en piezas listas para que Mercedes las publique a mano en Instagram, TikTok y Facebook. Reúne en un solo recorrido lo que antes estaba repartido entre 13 skills sueltas, ChatGPT, Grok, Google Flow y un calendario en Notion.

El recorrido tiene 7 etapas y 3 puertas de calidad:

```
0 Triage ─► 1 Ficha ─► 2 Producción visual ─► 3 Video con IA ─► 4 Revisión ─► 5 Publicación ─► 6 Medición
              │                                                      │              │              │
          Puerta 1                                               Puerta 2       Puerta 3     (vuelve a 0 con ideas nuevas)
        inglés y pedagogía                                     marca y calidad  plataforma
```

Ninguna pieza avanza si su puerta no está en verde.

## 2. Problema que resuelve

Un análisis previo del trabajo de Mercedes encontró estos huecos:

| Hueco | Efecto |
|---|---|
| Nadie convertía la idea en una ficha con el inglés verificado | Cada skill validaba por su cuenta, a veces con afirmaciones más fuertes que la fuente |
| No había router de formatos | Se podían generar piezas que no hacían falta |
| El video no tenía revisión | Las skills de revisión solo analizaban imágenes |
| Los prompts de video estaban separados por personaje y sin guía por herramienta | Grok y Flow se usaban con el mismo prompt |
| No existía etapa de publicación | Copy, horario y checklist se rehacían cada vez |
| No existía medición | No se podía decidir con datos |
| Había contradicciones entre skills | Ver sección 9 |

## 3. Alcance

**Cubre:** producción diaria de contenido de redes (posts, B-roll, overlays, series de verbos, Saturday English, Inglés básico, videos con el avatar o con Mechita, guion de microclase), revisión, paquete de publicación manual y registro de resultados.

**No cubre:** ebooks, packs de recursos gratuitos, la landing y el formulario de suscripción, la construcción técnica del PowerPoint y la página interactiva de la microclase (siguen en su skill propia), la ejecución dentro de Grok, Flow, HeyGen, D-ID, CapCut y ChatGPT, y la verificación de audio.

## 4. Arquitectura de skills

### 4.1 Skills nuevas (6)

| Skill | Etapa | Función |
|---|---|---|
| `mmercedes-cadena` | 0 | Orquesta. Clasifica la entrada, elige formatos (máximo 3 por idea) y llama a las demás |
| `mmercedes-ficha` | 1 | Convierte la idea en la ficha pedagógica verificada, que es la fuente única |
| `mmercedes-video-ia` | 3 | Guion de voz y prompts para Grok, Google Flow, HeyGen, D-ID y CapCut |
| `mmercedes-qa` | 4 | Puerta de calidad para imagen, video y copy. Semáforo y "Alerta de marca" |
| `mmercedes-publicar` | 5 | Copy por plataforma, checklist, horario y fila del calendario de Notion |
| `mmercedes-medir` | 6 | Registro de resultados y decisiones para el calendario |

### 4.2 Skills existentes reescritas o actualizadas (7 copias en el repositorio)

| Skill | Cambio |
|---|---|
| `mmercedes-generador-posts` | Reescrita. Script portátil `mm_posts.py` con fuentes incluidas, 4 subcomandos, avatar opcional y validación anti-cascada |
| `mmercedes-broll-overlay` | Reescrita. Usa el subcomando `broll` del generador y ya no depende de rutas de sesión |
| `mmercedes-colores` | Tabla de selección del CTA por tema, CTA retirados, nivel dinámico |
| `mmercedes-prompt-ia` | CTA al link en bio, nivel dinámico, regla de gafas y prop, instrucción anti-cascada, plantillas nuevas de Saturday English e Inglés básico |
| `mmercedes-brand` | Fuente del avatar, gafas y props variables, resaltador verde con "MMercedesEnglish", CTA |
| `mmercedes-prompt-animacion` | Gafas iguales a la imagen de referencia |
| `mmercedes-revisor` | Props, gafas y nivel dinámico |

### 4.3 Skills que se reutilizan y siguen en la cuenta de Mercedes

`mmercedes-broll-texto`, `mmercedes-irregular-verbs`, `mmercedes-mechita`, `mmercedes-evaluador-slides` y `edicion-microclase-pptx-interactiva`. No están en el repositorio.

## 5. Detalle de cada etapa

### Etapa 0. Triage (`mmercedes-cadena`)

Clasifica la entrada y consulta `references/matriz-formatos.md` para elegir un formato principal y, como máximo, dos de apoyo.

| Entrada | Ruta típica |
|---|---|
| Expresión o vocabulario | Post ¿Cómo se dice? |
| Error común | Post No digas... Di... |
| Verbo irregular | VERB ALERT o imagen de la serie de verbos |
| Gramática básica Beginner | Inglés básico (2 o 3 columnas) |
| Lista numerada de 6 | Saturday English |
| Regla corta | Cápsula de Mechita |
| Reflexión | B-roll de texto, formato C |
| Voz personal | Avatar animado |
| Tema que necesita práctica | Microclase |
| Contenido largo | Atomizar en piezas, cada una con su ficha |

Modos de trabajo: pieza única, lote semanal (5 a 7 piezas, sin dos del mismo tipo seguidas y con mezcla orientativa 60% intermedio y 40% beginner) y atomizar.

Reglas propias: si ya llegan los datos completos se salta la etapa 1, se pregunta solo lo que falta, se produce solo lo pedido, el avatar y Mechita son identidades distintas, y la publicación es siempre manual.

### Etapa 1. Ficha (`mmercedes-ficha`)

Campos: id, tipo (el de Notion), serie, nivel, objetivo, hook en español, contenido propio de la serie, ejemplos, Tip Mercedes, CTA, fuente, verificación, formatos y riesgos.

Puerta 1, verificación lingüística:
- La forma inglesa debe ser natural y nativa, con variedad (americano o británico) cuando importe.
- Se distingue "incorrecto" de "poco natural". "I have a doubt" es gramatical y suena menos natural que "I have a question", así que no se titula como error absoluto.
- Cada regla lleva una fuente concreta (Cambridge, Merriam-Webster, Oxford Learner's o Collins) o se marca como opinión fundamentada.
- Si hay duda y no se puede consultar, la ficha queda "por verificar" y no avanza.

### Etapa 2. Producción visual

| Formato | Quién lo produce |
|---|---|
| ¿Cómo se dice?, No digas... Di..., Inglés básico, overlay de B-roll | Script `mm_posts.py` (Pillow) |
| Los mismos formatos con avatar, Saturday English, VERB ALERT, B-roll de verbos | Plantillas de `mmercedes-prompt-ia` o `mmercedes-irregular-verbs`, ejecutadas en ChatGPT |
| B-roll de texto | `mmercedes-broll-texto` |
| Microclase | `edicion-microclase-pptx-interactiva` |

### Etapa 3. Video con IA (`mmercedes-video-ia`)

- **Protagonista:** avatar real (fotografía de Mercedes), Mechita (2D) o sin personaje. Nunca se mezclan las reglas.
- **Guion de voz:** gancho, reveal y cierre. Palabras por duración (estimación propia a validar con el primer video): 8 s, 15 a 20 palabras; 15 s, 30 a 38; 20 s, 45 a 50; 30 s, 65 a 75.
- **Herramientas:** Grok Imagine (animar la foto o generar a Mechita con referencia), Google Flow con Veo (escenas de Mechita con timecodes), HeyGen o D-ID (un solo audio coherente), CapCut (montaje y texto de marca).
- **Reglas comunes:** vertical 9:16, imagen de referencia en cada clip, sin música generada, texto generado solo para 1 a 3 palabras y el resto en CapCut o Canva, voz coherente entre clips y cierre con el badge de la marca.
- Los límites de duración y funciones de cada herramienta cambian, así que se verifican en la herramienta antes de planificar.

### Etapa 4. Revisión (`mmercedes-qa`)

Coordina `mmercedes-revisor` (imágenes) y `mmercedes-evaluador-slides` (láminas), y añade video y copy.
- **Video:** con ffmpeg se extrae un fotograma por segundo. Se comprueba que las gafas coincidan con la referencia, el rostro sin distorsión, la boca sincronizada, las manos sin errores, el texto legible, el formato y la ausencia de marca de agua.
- **Copy:** español neutro con tú, signos ¿? ¡!, sin precios, hashtags fijos, sin audio sugerido en TikTok y CTA al link en bio.
- **Bloqueos:** gafas que no coinciden con la referencia, bob corto, estilo ilustrado en el avatar real, más de 3 bloques en cascada, Tip sobre otro tema, texto del marcador distinto de "MMercedesEnglish", colores fuera de paleta, imagen cuadrada, inglés incorrecto o sin fuente, avatar tapando contenido e imagen en cascada.
- **Salida:** semáforo APROBADO, CORREGIR o BLOQUEADO, campo "Alerta de marca" y lista de lo no verificado.

### Etapa 5. Publicación (`mmercedes-publicar`)

- Instagram siempre nativo (nunca Meta Business Suite) y TikTok con audio trending añadido en la app, nunca sugerido.
- Copy: Instagram, caption breve de 1 a 3 frases; TikTok, 1 a 2 líneas; Facebook, 3 a 6 líneas.
- CTA siempre al link en bio, elegido por tema.
- Hashtags fijos: #MMercedesEnglish #NoDigasDi #AprendeIngles #InglesParaLatinos #EnglishTips #LearnEnglish.
- Horarios: sin datos de analíticas son hipótesis, marcadas como tales.
- Checklist por plataforma que incluye verificar la etiqueta de contenido generado con IA, cuya política cambia con frecuencia.
- Fila de la base "Calendario Editorial" de Notion con los campos Pieza, Tipo de contenido, Plataforma, Fecha, Horario sugerido, tres campos de copy, Estado, Alerta de marca y Notas. El estado pasa a Publicado solo cuando Mercedes confirma.

### Etapa 6. Medición (`mmercedes-medir`)

Registro por pieza a los 3 y a los 7 días, copiado por Mercedes desde las analíticas nativas: alcance, interacciones (guardados y compartidos pesan más para contenido educativo, según el criterio del documento), retención, clics al link en bio, herramienta y protagonista. El análisis compara serie, protagonista, nivel, horario y tipo de CTA, y solo concluye con 8 a 10 piezas o más. Entrega resumen, qué repetir, ajustes al calendario e ideas nuevas que entran a la etapa 0.

## 6. Generador de posts

Archivo: `.claude/skills/mmercedes-generador-posts/assets/mm_posts.py`. Requiere Python 3 y Pillow.

### 6.1 Subcomandos y contenido

| Subcomando | Serie | Campos principales del JSON |
|---|---|---|
| `como-se-dice` | ¿Cómo se dice? | `concepto_es`, `expresion_en`, `subtitulo`, `literal`, `significa`, `ejemplos` (3), `tip` |
| `no-digas` | No digas... Di... | `frase_mal`, `frase_bien`, `ejemplos` (2), `tip` |
| `ingles-basico` | Inglés básico | `titulo_1`, `titulo_2`, `subtitulo`, `columnas` (2 o 3), `tip` |
| `broll` | Overlay de B-roll (reconstruido, pendiente de aprobación) | `hook`, `expresion`, `reveal_no`, `reveal_si`, `subtitulo`, `ejemplos`, `tip`, `serie` |

Campos comunes: `nivel` (Beginner o Intermediate, obligatorio), `tema`, `salida`, y opcionales `cta`, `cta_categoria` y `falso_cognado`. En Inglés básico, `*texto*` pone negrita y `\n` fuerza un salto de línea.

### 6.2 Comandos

```bash
python3 mm_posts.py como-se-dice contenido.json --out ./salida --avatar NOMBRE
python3 mm_posts.py --listar-avatares
```

### 6.3 Validaciones que bloquean el PNG

| Validación | Qué comprueba |
|---|---|
| Paleta | Constantes con los hex oficiales. Ningún color fuera de la paleta |
| Nivel | Debe ser Beginner o Intermediate. La pastilla del header lo muestra |
| CTA | Debe mencionar el link en bio. Rechaza "Cuéntame en comentarios", "¿Lo conocías?" y variantes |
| Anti-cascada | Todos los bloques con el mismo margen izquierdo y ancho de columna, sin superposición, y ningún bloque bajo el avatar |
| Espacio | Si el contenido no cabe, se detiene y pide acortar. Los textos largos reducen solo su tipografía |
| Avatar | PNG con transparencia obligatoria. Escala con un solo factor, sin estirar. Sangra por el borde derecho sin degradado |

### 6.4 CTA

Seis categorías: vocabulario, errores, falsos cognados, gramática, verbos y universales. La serie define la categoría (¿Cómo se dice? usa vocabulario, No digas usa errores, Inglés básico usa gramática y el overlay usa universales). Dentro de la categoría el CTA se elige por una función reproducible del tema, así que el mismo tema siempre da el mismo CTA.

### 6.5 Avatares

Cada versión del master (cada prop o par de gafas) es un PNG en `assets/avatar/`. Con varios archivos el script no adivina: se detiene y los lista. La foto no se sube al repositorio, porque es público, y `.claude/skills/.gitignore` excluye `assets/avatar/*.png`.

## 7. Reglas de marca vigentes

| Tema | Regla |
|---|---|
| Paleta | Navy #0D1B3E, Amarillo #FFD23F, Crema #FFFBF0, Blanco. Rojo #CD2823 y Verde #1E9650 solo en X, check, etiquetas y pastilla de serie. Amarillo pálido #FFFBCC solo en el Tip. Dorado #BE9100 solo en su label. Gris #E6E6EB en bordes |
| Tipografía | BigShoulders-Bold, WorkSans, Lora Italic y NothingYouCouldDo solo en "Tip Mercedes:" |
| Formato | 1080×1920, vertical 9:16 |
| Nivel | Pastilla dinámica Beginner o Intermediate |
| Idioma | Tip Mercedes y CTA en español |
| CTA | Siempre al link en bio, según el tema |
| Avatar | Fotografía realista. Gafas idénticas a la referencia. Un solo prop del set aprobado. Si es resaltador o marcador, dice exactamente "MMercedesEnglish" |
| Mechita | Personaje 2D con sus propias reglas. No se mezcla con el avatar |
| Cascada | Prohibida |
| Publicación | Manual y nativa, sin precios |

## 8. Decisiones de Mercedes

Resueltas:
1. Pastilla de nivel dinámica.
2. CTA siempre al link en bio, elegido por tema. Se retiran los CTA de comentarios.
3. Se usa el avatar master fotográfico. El prop y las gafas pueden variar dentro de lo aprobado.
4. El texto del resaltador verde es "MMercedesEnglish".
5. Saturday English con franjas blancas con borde gris y badge MM (versión B tras comparar).
6. Se acepta el cabello del master actual.
7. Los formatos ¿Cómo se dice?, No digas... Di... e Inglés básico se conservan como funcionan.
8. Nunca en cascada.

## 9. Contradicciones y estado

Todas están en `references/conflictos.md`, con su valor por defecto. Resumen:

| Estado | Puntos |
|---|---|
| Resueltos | Nivel, CTA, avatar en Pillow, deriva de colores, rutas, cascada, Saturday English, gafas, texto del resaltador, prop variable |
| Abiertos con valor por defecto | Usos de rojo y verde, tres tipos de B-roll, palabras por duración, base duplicada en Notion, texto generado en videos de Mechita, hashtag #NoDigasDi en otras series, pieza Fun vs Funny |
| Pendientes | Qué avatar llevan las microclases, y si Fun vs Funny es una serie fija |

## 10. Estructura de archivos

```
.claude/
  CLAUDE.md                                 contexto que Claude Code lee al iniciar
  skills/
    .gitignore                              excluye pyc y la foto del avatar
    mmercedes-cadena/
      SKILL.md
      references/
        matriz-formatos.md                  idea a formato y tipos de B-roll
        conflictos.md                       decisiones y contradicciones
        analisis.md                         diagnóstico del proceso previo
        MANUAL_CADENA_MMERCEDESENGLISH.md   manual para ChatGPT
        DOCUMENTACION_CADENA_MMERCEDESENGLISH.md   este documento
    mmercedes-ficha/ mmercedes-video-ia/ mmercedes-qa/ mmercedes-publicar/ mmercedes-medir/
    mmercedes-generador-posts/
      assets/mm_posts.py, fonts/, ejemplos/
    mmercedes-brand/ mmercedes-colores/ mmercedes-prompt-ia/ mmercedes-broll-overlay/
    mmercedes-prompt-animacion/ mmercedes-revisor/
```

## 11. Instalación y uso

**En Claude (cuenta de Mercedes).** Subir cada skill como zip en la configuración de Skills, quitando antes la versión anterior del mismo nombre. Existe un zip ya armado de `mmercedes-generador-posts` con el avatar master dentro. Las demás skills están en el repositorio como fuente y se empaquetan de la misma forma.

**En Claude Code.** El archivo `.claude/CLAUDE.md` se carga solo al empezar una tarea. Funciona en las sesiones nuevas cuando está en la rama principal, es decir, después de fusionar el pull request.

**En ChatGPT.** Crear un Proyecto o GPT, pegar la Parte 1 del manual en las instrucciones, subir el manual completo como conocimiento y adjuntar la foto de referencia. El zip del generador se adjunta en el chat cuando se quiere generar con Python.

**Uso típico.** Pedir "arma el contenido de [tema]". La cadena indica la etapa, pregunta solo lo que falta y entrega el paquete.

## 12. Pruebas y verificación

Realizadas durante la construcción:
- Render de las cuatro series con ejemplos reales y revisión visual de cada PNG.
- Prueba de la guardia anti-cascada con bloques desalineados simulados: bloquea y explica el error.
- Composición del avatar master recortado en ¿Cómo se dice? y No digas... Di..., sin tapar bloques.
- Prueba de selección entre varios avatares y de la lista.
- Descompresión del zip en una carpeta limpia y ejecución del script desde ahí.
- Recorte del avatar con revisión del borde sobre fondo navy.
- Comparación visual de Saturday English entre la pieza original y la versión en paleta.

No verificado:
- Audio y voz de los videos.
- Resultado real en Grok, Google Flow, HeyGen, D-ID, CapCut y ChatGPT.
- Comportamiento del manual dentro de ChatGPT, y límites de archivos en sus proyectos.
- Escritura real en Notion (la skill de publicación define la fila, pero no se escribió ninguna).
- El subcomando `broll`, reconstruido sin el script original y pendiente de aprobación de Mercedes.

## 13. Limitaciones y pendientes

- El texto "MMercedesEnglish" del resaltador del master es una superposición hecha sobre la foto y la etiqueta original se tapó con el verde del cuerpo. En un acercamiento se nota un parche leve.
- Las microclases siguen con una ilustración como avatar.
- La pieza Fun vs Funny conserva reglas anteriores y no tiene plantilla.
- Los horarios de publicación son hipótesis hasta tener analíticas.
- El manual para ChatGPT se generó con un script de apoyo que no quedó en el repositorio. Si cambia una skill, hay que regenerar el manual.

## 14. Mantenimiento

Cuando Mercedes cambia una decisión, hay que actualizar cuatro lugares para que no se contradigan:
1. La skill afectada, en `.claude/skills/`.
2. `references/conflictos.md`, con el nuevo estado.
3. `.claude/CLAUDE.md`, si la regla es de las que nunca se rompen.
4. El manual para ChatGPT, y el zip de la skill si cambió el script o el avatar.

Después se suben las skills modificadas a la cuenta de Mercedes. Subir un archivo a la rama no lo publica ni lo activa en Claude.

## 15. Glosario

| Término | Significado |
|---|---|
| Skill | Carpeta con instrucciones que Claude consulta cuando la tarea lo requiere |
| Cadena | Skills que trabajan en orden, donde la salida de una alimenta a la siguiente |
| Puerta | Punto de control. Si una pieza no pasa, no avanza |
| Ficha | Resumen verificado de una pieza, fuente única de su contenido |
| Cascada | Bloques de una imagen con distinto margen o ancho, escalonados, rotados o superpuestos |
| Alerta de marca | Marca en el calendario cuando una pieza rompe el sistema de marca |
| Master | Foto recortada del avatar, con fondo transparente, que se compone en los posts |
| RTIC | Rol, Tarea, Instrucción y Contexto, la estructura de prompt del atajo "pp" |
