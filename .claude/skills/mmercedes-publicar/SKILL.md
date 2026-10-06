---
name: mmercedes-publicar
description: Prepara el paquete de publicación manual de MMercedesEnglish para Instagram, TikTok y Facebook a partir de piezas ya producidas y aprobadas. Entrega copy por plataforma, checklist de publicación, horario sugerido y la fila del calendario editorial de Notion. Usar SIEMPRE que Mercedes diga "prepara la publicación", "qué subo hoy", "calendario de la semana", "copy para Instagram, TikTok y Facebook", o cuando la cadena llegue a la etapa 5.
---

# Paquete de publicación (puerta G3)

El contenido ya está producido. El cuello de botella es organizar qué, cómo y cuándo publicar en cada red. Esta skill no genera contenido nuevo, ni copy de diseño ni guiones. Mercedes publica a mano, siempre.

## Reglas fijas

- **Instagram:** siempre nativo en la app. Nunca Meta Business Suite ni programadores externos (el historial de la cuenta muestra pérdida de alcance).
- **TikTok:** el audio trending se añade dentro de la app al publicar. Nunca sugieras un audio en el copy ni en la lista.
- Nunca precios ni métodos de pago en feed ni en stories.
- Español neutro latinoamericano con tú, sin voseo.
- Hashtags fijos: #MMercedesEnglish #NoDigasDi #AprendeIngles #InglesParaLatinos #EnglishTips #LearnEnglish.
- Si una pieza rompe el sistema de marca, no entra al calendario: márcala con Alerta de marca y devuélvela a `mmercedes-qa`.

## Entradas necesarias

Pieza aprobada (semáforo APROBADO en `mmercedes-qa`), ficha y archivo final. Si falta alguna, dilo y no inventes.

## Copy por plataforma

Parte siempre de la ficha. No cambies el contenido pedagógico.

| Plataforma | Formato | Extensión | Contenido |
|---|---|---|---|
| Instagram | Reel o post | Caption breve, 1 a 3 frases | Hook del post, una línea de valor, CTA y los 6 hashtags fijos |
| TikTok | Video | Copy corto, 1 a 2 líneas | Hook más CTA. Sin audio. Hashtags fijos |
| Facebook | Video o imagen | Más extenso, 3 a 6 líneas | Hook, explicación breve en español, el ejemplo en inglés, CTA |

El CTA sigue el banco de `mmercedes-colores` (por defecto, link en bio, ver `mmercedes-cadena/references/conflictos.md` punto 2).

## Horario sugerido

No hay datos de analíticas en esta skill. Procede así:

1. Si Mercedes entrega sus mejores horarios por plataforma o existe un registro en `mmercedes-medir`, úsalo.
2. Si no hay datos, propón dos ventanas de prueba por plataforma y márcalas como hipótesis, por ejemplo mañana temprano y noche, en hora local de la audiencia principal. Registra el resultado para sustituirlas por datos.

Distancia mínima entre publicaciones de la misma plataforma el mismo día: la que Mercedes use hoy. No la cambies sin que lo pida.

## Checklist por plataforma (para copiar y marcar)

**Instagram (nativo)**
- [ ] Archivo final 1080×1920 sin marca de agua
- [ ] Subido desde la app de Instagram
- [ ] Portada elegida y legible
- [ ] Caption pegado, con hashtags fijos
- [ ] Audio de la app elegido si la pieza lo lleva (los videos con voz propia no necesitan audio extra)
- [ ] Etiqueta de contenido generado con IA marcada si la app lo pide para este video
- [ ] Sin precios en caption ni en pantalla

**TikTok (audio nativo)**
- [ ] Archivo final 1080×1920
- [ ] Subido desde la app de TikTok
- [ ] Audio trending añadido dentro de la app, volumen balanceado con la voz
- [ ] Copy pegado con hashtags fijos
- [ ] Etiqueta de contenido generado con IA marcada si aplica
- [ ] Sin precios

**Facebook**
- [ ] Mismo archivo o versión sin elementos específicos de otra app
- [ ] Copy extendido pegado
- [ ] Sin precios

Verifica las políticas de etiquetado de contenido generado con IA en cada app antes de publicar. Cambian con frecuencia y yo no puedo confirmarlas desde aquí.

## Calendario: fila de Notion

Base: "Calendario Editorial" (`a183e8c5-2108-47f1-8ebc-2475603bd675`). Hay otra base duplicada con el mismo nombre. Confirma con Mercedes cuál se mantiene.

| Campo | Valor |
|---|---|
| Pieza | título de la ficha |
| Tipo de contenido | según equivalencias de `matriz-formatos.md` |
| Plataforma | Instagram, TikTok, Facebook |
| Fecha | día de publicación |
| Horario sugerido | ventana elegida |
| Copy Instagram, Copy TikTok, Copy Facebook | los textos |
| Estado | Idea, Guion, Grabado (aquí significa generado), Editado, Publicado |
| Alerta de marca | marcada si hubo ruptura |
| Notas | id de la ficha, subtipo, herramienta usada |

Si el conector de Notion está disponible, crea o actualiza la fila. Si no, entrega la fila como tabla Markdown y dilo. El estado pasa a Publicado solo cuando Mercedes confirma que publicó. Nunca lo marques tú.

## Formato de entrega (calendario listo para ejecutar)

```
| Día | Hora | Plataforma | Pieza | Archivo | Copy | Checklist | Estado |
```

Más, para cada pieza, el bloque de copy de las tres plataformas y su checklist. Cierra con la lista de lo que falta antes de publicar (pendientes de revisión, audio por confirmar, etiqueta de IA por verificar).
