---
name: mmercedes-prompt-ia
description: Compatibility route for requests that explicitly ask for an external-AI prompt for a MMercedesEnglish visual. Do not create prompts that regenerate Mercedes or replace a code-composed series template.
---

# Compatibilidad — prompts de imagen

Un prompt para generar el post completo con un modelo de imágenes no es la ruta de producción para MMercedesEnglish: ese método puede cambiar el texto, inventar la composición o regenerar el avatar. Mantén el texto exacto y la plantilla de la serie con el renderer especializado.

Cuando Mercedes solicite explícitamente un prompt:

1. Determina si pide el post completo o solo un recurso auxiliar.
2. Para el post completo, redirige a `mmercedesenglish-visual-generator` y al renderer de la serie. No escribas un prompt alternativo para que un modelo redibuje la plantilla.
3. Nunca incluyas descripciones faciales como sustituto de una foto aprobada ni instruyas a un modelo a crear, reparar o estilizar la identidad de Mercedes.
4. Si pidió un recurso auxiliar sin personas, texto ni logo (por ejemplo un fondo), elabora únicamente ese prompt y aclara que debe integrarse al diseño con código sin cambiar el layout de la serie.

## Prompts que mejor han funcionado

Mercedes registró en [references/prompts-que-funcionan.md](references/prompts-que-funcionan.md) los prompts que más se acercan a la imagen que quiere para cada serie: AVATAR, NO DIGAS DI, COMO SE DICE, FALSE COGNATE, plantilla de láminas Basic y captions (GROKPROMPT). Léelo antes de escribir cualquier prompt o de definir la intención visual de una pieza. Toma de ahí el tono, el gancho, la composición y el nivel de realismo.

Ese archivo tiene una tabla "Choques y decisiones" con lo que Mercedes decidió donde los prompts contradecían reglas (avatar, cabello, mano, lentes, props, método, False Cognate, hashtags y audiencia). Aplícala. El punto 10 (colores de láminas Basic) sigue pendiente: avísale a Mercedes si lo tocas.

Consulta la versión previa archivada en `../_versiones-previas-2026-10-10/mmercedes-prompt-ia/SKILL.md` solo para rastrear requisitos históricos; sus plantillas de post, CTA y avatar ya no se usan.
