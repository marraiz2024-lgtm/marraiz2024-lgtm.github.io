# Análisis del proceso actual de contenido (idea a emisión)

Fuentes revisadas: 13 skills de MMercedesEnglish (marca, colores, generador de posts, prompt para IA externa, B-roll texto, B-roll overlay, verbos irregulares, animación del avatar, Mechita, revisor, evaluador de láminas, microclase), el repositorio de GitHub Pages, el calendario de Notion y los materiales de Drive (ebooks, packs, posts de Beginner English Tips).

## Proceso real hoy

```
IDEA (sin skill)
  |
  v
CONTENIDO (sin skill: Mercedes define concepto, ejemplos, tip)
  |
  +--> Post PNG ............ generador-posts (Pillow)  o  prompt-ia (ChatGPT/Gemini)
  +--> B-roll texto ........ broll-texto  -> broll-overlay (PNG) -> Grok/CapCut
  +--> B-roll verbos ....... irregular-verbs (prompt ChatGPT)
  +--> Video avatar real ... prompt-animacion (Grok/HeyGen/D-ID/CapCut)
  +--> Video Mechita ....... mechita (Grok Imagine/Flow)
  +--> Microclase .......... edicion-microclase (PPTX + HTML)
  |
  v
REVISIÓN: revisor (imagen), evaluador-slides (láminas). Video y copy sin revisor
  |
  v
PUBLICACIÓN: reglas en Notion y en las preferencias (nativo, audio TikTok, hashtags). Sin skill
  |
  v
MEDICIÓN (sin skill)
```

## Lo que funciona

- El sistema de marca está bien documentado y tiene lista de errores frecuentes (gafas negras, bob, fondos con pincelada).
- Cada serie tiene plantilla estructurada y reproducible.
- Las respuestas de corrección para ChatGPT están escritas y ahorran iteraciones.
- La microclase tiene lista final de verificación y reglas aprendidas de errores reales.
- El calendario de Notion ya tiene campos por plataforma, Estado y Alerta de marca.

## Huecos de la cadena

| Hueco | Efecto |
|---|---|
| Nadie convierte una idea en ficha verificada | El inglés se valida dentro de cada skill, a veces con afirmaciones absolutas ("no significa X") que son más fuertes que la fuente |
| No hay router de formatos | Mercedes decide a mano qué skill llamar y puede generar piezas que no necesita |
| Video sin revisión | El revisor solo analiza imágenes. Las gafas negras en video son un error que la marca ya nombró |
| Prompts de video separados por personaje y sin guía por herramienta | Grok y Flow se usan con el mismo prompt sin adaptarlo. La voz cambia entre clips |
| No hay etapa de publicación | El copy por plataforma, el horario y la checklist se rehacen cada vez |
| No hay medición | No se puede decidir con datos entre series, horarios ni CTA |
| Contradicciones entre skills | Ver `conflictos.md`: nivel fijo frente a dinámico, CTA, avatar sin foto en el PNG, avatar del repositorio |

## Riesgos técnicos

- Los skills de generación de PNG dependen de rutas de una sesión anterior y de un archivo base que puede no existir.
- Las herramientas de IA externa (Grok, Flow, ChatGPT) no pueden ser ejecutadas desde Claude. Todo prompt es un contrato con un humano que debe devolver el resultado.
- La consistencia del avatar con IA depende de la imagen de referencia. Por eso conviene componer la foto real en un script determinista cuando se pueda.

## Diseño de la cadena nueva

Se agregan 6 skills y se reutilizan los 13 existentes sin duplicarlos.

| Skill nueva | Cubre el hueco de |
|---|---|
| `mmercedes-cadena` | Orquestación, triage y modos de trabajo (pieza, lote, atomizar) |
| `mmercedes-ficha` | Idea a contenido verificado y fuente única |
| `mmercedes-video-ia` | Guion, prompts por herramienta y revisión de video |
| `mmercedes-qa` | Puerta de calidad para video y copy, y coordinación con los revisores |
| `mmercedes-publicar` | Copy por plataforma, checklist, horario, fila de Notion |
| `mmercedes-medir` | Registro y decisión con datos |

Tres puertas de calidad (G1 inglés, G2 marca, G3 plataforma) y un estado en Notion para cada etapa.
