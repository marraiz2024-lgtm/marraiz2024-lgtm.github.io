---
name: mmercedes-ficha
description: Convierte una idea, error común, expresión, reflexión o contenido largo en la ficha pedagógica canónica de una pieza de MMercedesEnglish, con el inglés verificado y los campos que alimentan posts, B-roll, videos y copy. Usar SIEMPRE como primer paso cuando Mercedes dé un tema o texto nuevo ("quiero hacer algo sobre...", "esta frase la dicen mal", "arma la ficha", "verifica este inglés") o cuando la cadena llegue a la etapa 1.
---

# Ficha pedagógica

La ficha es la fuente única de contenido. Todo lo demás (PNG, prompts, guion de voz, copy) se copia de ella. Si la ficha cambia, se regenera lo que depende de ella.

Español neutro latinoamericano con tú. Sin guion largo. Sin la estructura "no es X sino Y". Sin enumeraciones de tres elementos por reflejo.

## Proceso

1. **Recibe la entrada.** Si ya trae los datos completos, solo valida y normaliza.
2. **Completa lo que falta.** Pregunta solo lo imprescindible: nivel (Beginner o Intermediate) y serie, si no se deducen.
3. **Verifica el inglés (puerta G1).** Ver sección siguiente.
4. **Elige el CTA** del banco de `mmercedes-colores` según el tipo de contenido.
5. **Propón formatos** con `mmercedes-cadena/references/matriz-formatos.md`. No los produzcas.
6. **Entrega la ficha** en el formato de abajo y pide confirmación solo si hay una duda lingüística abierta.

## Verificación lingüística (puerta G1)

- La forma inglesa debe ser natural y nativa. Indica la variedad (inglés americano o británico) cuando importe.
- **Distingue "incorrecto" de "poco natural".** "I have a doubt" es gramatical. Suena menos natural que "I have a question" en la mayoría de contextos. Si lo es, titula la pieza con ese matiz ("Sound more natural") y no con una afirmación absoluta. Nunca escribas "no existe" ni "está mal" si solo es poco común.
- Revisa falsos amigos, registro (formal e informal) y contexto de uso.
- Cada regla o afirmación lleva una fuente concreta: Cambridge Dictionary, Merriam-Webster, Oxford Learner's Dictionaries o Collins. Si no hay fuente, escribe "opinión fundamentada" en el campo de verificación. Nunca escribas "los estudios muestran" sin citar el estudio.
- Si tienes duda y hay búsqueda web disponible, consulta la fuente antes de afirmar. Si no, deja el campo en estado `por verificar` y no avances a producción.
- Los 3 ejemplos deben ser frases que un nativo diría. Nada de ejemplos inventados para encajar la regla.
- Revisa el español: ortografía, signos de apertura (¿ y ¡), tú sin voseo.

## Formato de la ficha

```
FICHA
id:            AAAA-MM-DD-slug
tipo (Notion): No digas...Di... | Beginner Tips | Real English | Saturday English | Otro
serie:         ¿Cómo se dice? | No digas... Di... | VERB ALERT | Verbos irregulares | B-roll | Mechita | Microclase
nivel:         Beginner | Intermediate
objetivo:      qué podrá hacer el alumno tras verla (una frase)
hook_es:       gancho en español
contenido:
  (¿Cómo se dice?)  concepto_es, expresion_en (MAYÚSCULAS), subtitulo, literal, significa
  (No digas... Di...) frase_mal, frase_bien, por_que
  (Verbo)           base, past_simple, participle, traduccion
  (Reflexión)       3 a 6 líneas de máximo 7 palabras cada una
ejemplos:      3 pares EN / ES (2 pares comparativos en No digas... Di...)
tip_mercedes:  2 a 5 líneas en español, sobre ESTE tema
cta:           frase y línea de acción del banco
fuente:        diccionario o referencia concreta, o "opinión fundamentada"
verificacion:  OK | por verificar (qué falta)
formatos:      principal + hasta 2 de apoyo
riesgos:       posibles choques con marca (p. ej. avatar, colores, prop)
```

## Reglas de contenido que ya se aplicaron en la marca

- El Tip Mercedes y el CTA van siempre en español.
- Máximo 3 bloques de contenido en un post, sin contar header, tip, CTA y footer.
- Un solo prop sobredimensionado por pieza estática.
- En B-roll de ambiente con texto, cada línea tiene máximo 6 o 7 palabras y no lleva emojis.
- Ofrece 2 o 3 versiones del texto de B-roll para que Mercedes elija.
- Rota los tipos de contenido: no dos reflexiones seguidas ni dos tips seguidos.

## Cuando la entrada es un contenido largo

Extrae piezas independientes. Cada una necesita su propia ficha, un solo concepto y un hook que funcione sin ver la pieza original. Lista las piezas candidatas con una línea cada una y deja que Mercedes elija cuáles se producen.
