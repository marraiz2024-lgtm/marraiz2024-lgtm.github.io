# CLAUDE.md: Landing page MMercedesEnglish

Repo de GitHub Pages de MMercedesEnglish. Sitio estático: no hay build, no hay backend. Lo que está en la raíz del repo es lo que se publica.

URL publicada: https://marraiz2024-lgtm.github.io/
Última revisión de la página en vivo: 13 oct 2026.

Las microclases (`microclase-*.html`, `.pptx`, `audio/`, `tools/`) se rigen por `AGENTS.md`. Este archivo cubre la landing (`index.html`) y sus recursos.

## Cómo trabajar

- Respuestas breves y directas. Sin adulación. Si algo está mal o es una mala decisión, dilo.
- Antes de editar, lee el archivo actual del repo. Nunca partas de una copia antigua ni de memoria.
- Trabaja en una rama nueva por cambio. Muestra el `git diff` antes de cada commit y espera aprobación.
- No abras pull request salvo que Mercedes lo pida. Ella fusiona.
- Cambia solo lo pedido. Después de editar, verifica con diff que nada más se movió.
- No generes contenido, imágenes ni secciones nuevas si no se pidieron. Espera parámetros.
- Revisa el resultado antes de entregarlo: abre la página en local y comprueba enlaces, anclas y vista móvil.
- Si Mercedes corrige algo y da su razonamiento, aplica la corrección. No le expliques de vuelta su propio argumento.
- Prueba en local con `python3 -m http.server` desde la raíz del repo.

## Estructura del repo

- `index.html`: página principal, un solo archivo con CSS y JS integrados.
- `mapa-16-tiempos-verbales.png`: tabla de tiempos verbales, enlazada como archivo aparte.
- `flashcards_gramatica_ingles_v3.html`: tarjetas interactivas, enlazadas desde la sección de recursos.
- `microclase-*.html`, `microclase-*.pptx`, `microclase-*-avatar.webp`, `audio/`, `tools/`: microclases. Ver `AGENTS.md`.
- `AGENTS.md`: instrucciones para Codex y otros agentes, centradas en las microclases.
- `README.md`: contiene una versión antigua de la landing. La clave de Brevo que aparece ahí está desactivada (confirmado).
- `AVATAR_CON_LENTES-removebg-preview.png`: avatar ilustrado retirado. No lo usa `index.html`. Se deja en el repo por decisión de Mercedes.

Confirma con `ls` si hay más archivos antes de asumir que esta lista está completa.

## Estado de la página (revisión del 13 oct 2026)

Secciones en orden: 01 Método, 02 Tu punto de partida, 03 Así aprendemos, 04 Prueba el método (mini lección interactiva de saludos), 05 Programa, 06 Recursos gratuitos, 07 Sobre Mercedes, Testimonios (sin número, por decisión), 08 FAQ, 09 Recibe tu guía (formulario Brevo), 10 Hablemos (formulario de 3 pasos que arma un mensaje de WhatsApp en el navegador), Privacidad.

En móvil, el menú entra en pantalla y se despliega. Revisado y correcto.

Contenido vigente:

- Clases individuales: $40 al mes. Grupales: $25 al mes por participante. 8 clases de 40 minutos, material digital incluido. Pago quincenal posible.
- Evaluación diagnóstica independiente: $10, informe en 48 horas.
- Pagos coordinados por WhatsApp, fuera de la página. Pago Móvil para Venezuela, Zelle para otros países.
- Recursos gratuitos sin registro: tabla de tiempos verbales y flashcards. Los Cimientos del Inglés (Módulo 1) se entrega por el canal de WhatsApp.
- Testimonios anonimizados ("Mamá de una estudiante", "Estudiante").

Auditoría del 13 oct 2026: las 13 anclas existen, sin IDs duplicados. Los enlaces externos responden. `index.html` pesa 66 KB, sin base64, sin rutas locales y sin claves. El formulario de Brevo se probó de punta a punta y funciona.

## Reglas que no se rompen

- Seguridad: nunca claves API ni tokens en el JavaScript del cliente. Una versión anterior expuso una clave de Brevo. Ya está desactivada. Antes de cada commit, busca con grep patrones como `api-key`, `xkeysib` y `Bearer`.
- Formulario de Brevo: no modificar su código ni los IDs. Está apuntado a la lista ID 2 ("Suscriptores Ebook Gratis"). No crear otro formulario ni otra lista.
- Privacidad: no mostrar nombres ni usuarios de quienes dan testimonios.
- Pagos: se coordinan directamente con Mercedes, fuera de cualquier plataforma. No agregar pasarelas ni botones de pago a la página.
- Peso: no incrustar imágenes en base64 dentro del HTML. Usar archivos relativos. Una imagen de 2.4MB incrustada ya frenó la carga en el pasado.
- Enlaces: relativos o con hash. Nunca rutas locales de la computadora.
- Español: neutro latinoamericano, con "tú". Sin voseo.

## Sistema visual

- Paleta: navy `#0D1B3E`, amarillo `#FFD23F`, crema `#FFFBF0`. El dorado `#BE9100` no es color principal de marca; en la landing se usa solo en detalles finos (contorno de foco y dos bordes) y se conserva así por decisión de Mercedes. El verde solo indica algo correcto.
- Tipografía: Big Shoulders Display (títulos) y Work Sans (texto).
- Tagline fijo: "Tiny Tips, Big Progress".
- Avatar: fotografía real de Mercedes, compuesta, nunca generada con IA. El avatar ilustrado está retirado. Lleva suéter negro de cuello en V, jeans oscuros, lentes color vino y aros dorados pequeños. Un solo prop por pieza.
- No modificar el avatar ni inventar variantes. Si hace falta una imagen con ella, pide la foto.

## Integraciones externas

- Brevo: workflow con un disparador (contacto agregado a la lista 2). Envía la plantilla "Welcome Email on List Addition" con el enlace a Primeros Pasos en Inglés (Nivel 0).
- ManyChat (plan gratuito): dos flujos en Instagram ligados a publicaciones concretas. PRIMERO entrega Primeros Pasos. CIMIENTOS entrega El Inglés del Presente.
- WhatsApp: número y canal ya enlazados en la página. Los textos prellenados van codificados en la URL. Conservar la codificación al editar.
- Google Drive: los recursos descargables deben seguir con permiso público. Verifica el enlace antes de publicar cambios que lo toquen.

## Pendientes

Bloqueante:

- Dirección física para correos salientes (requisito CAN-SPAM). Pospuesto. Opciones: apartado postal USPS o buzón privado. Hasta resolverlo, el envío masivo no está completo.

Calidad:

- Analítica: no hay ninguna implementada. Decidir herramienta antes de instalar nada.
- Dominio propio: hoy es subdominio de GitHub Pages.

Marca:

- Fotos nuevas de Mercedes para el hero (hoy sin imagen) y para "Sobre Mercedes" (hoy un recuadro provisional con "MM").
