# Especificaciones de series sin renderer por código

Estas dos series todavía no tienen renderer por código. Este documento recoge su diseño para que se pueda construir el renderer sin cambiar lo que ya funciona. No son prompts para un modelo de imágenes: por decisión de Mercedes (10 de octubre de 2026), ningún modelo dibuja el post completo ni genera o repara el avatar.

## Saturday English (listas numeradas de 6)

Pieza de referencia aprobada: "Phrasal Verbs: GO". Versión B aprobada por Mercedes tras comparar con la original.

Estructura, de arriba abajo:

1. Header navy con badge MM amarillo, pastilla de nivel (`[NIVEL] English Tips`) y franja amarilla de 8 px.
2. Etiqueta "SATURDAY ENGLISH" en navy bold con dos rayitas amarillas a cada lado.
3. Título grande en navy bold (por ejemplo, PHRASAL VERBS).
4. Pastilla navy con el elemento central en amarillo bold (por ejemplo, GO), con rayitas amarillas a cada lado.
5. Rejilla de 6 ítems, 2 columnas por 3 filas, todas las celdas del mismo tamaño y con el mismo margen y ancho de columna. Cada ítem: círculo amarillo con número, término en navy bold mayúsculas, traducción en español debajo, ilustración plana pequeña a la derecha, franja de ejemplo debajo con fondo blanco y borde gris #E6E6EB (no azul claro), estrella navy y la frase con el término en negrita. Separador amarillo fino entre filas.
6. Panel inferior con borde amarillo y 3 columnas, solo en la zona izquierda y terminando antes del avatar. Contenido en español: una caja explicativa, el Tip Mercedes y el CTA.
7. Footer navy con badge MM, "MMercedes" blanco y "English" amarillo, y el tagline.

Avatar: foto real compuesta por código, abajo a la derecha, sangrando por el borde derecho. Un solo prop del set aprobado. Ningún bloque detrás del avatar.

Pendiente de resolver antes de construir el renderer: las ilustraciones de cada ítem son assets. Hace falta definir de dónde salen (biblioteca propia o dibujadas por Mercedes) para que no las genere un modelo dentro del post.

## VERB ALERT

Estructura, de arriba abajo:

1. Header navy: badge MM, pastilla de nivel, pastilla de serie "VERB ALERT" en navy con campana amarilla.
2. Badge central: rectángulo navy con campana amarilla y "VERB ALERT" en amarillo bold.
3. Verbo principal muy grande en navy, con subrayado amarillo.
4. Tres formas en pastillas horizontales: base, past simple y past participle.
5. "¿Por qué es importante?": 2 o 3 líneas en español.
6. Ejemplos en tabla de 2 columnas con las tres formas en contexto.
7. Tip Mercedes en español.
8. CTA de la ficha (específico de la lección, al link en bio) y footer navy.

Avatar con un solo prop del set aprobado, compuesto por código.
