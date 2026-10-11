const pptxgen = require("pptxgenjs");
const React = require("react");
const RDS = require("react-dom/server");
const sharp = require("sharp");
const fa = require("react-icons/fa");
const { applyTheme } = require("./apply_theme.js");

// Uso: NODE_PATH=<node_modules> node build_pptx.js <salida.pptx> <avatar.webp|jpg|png>
const OUT = process.argv[2] || "microclase.pptx";
const AVATAR_SRC = process.argv[3] || "avatar.webp";

const THEME = {
  name: "MMercedesEnglish",
  headFontFace: "Big Shoulders Display",
  bodyFontFace: "Work Sans",
  colors: {
    dk1: "0D1B3E", lt1: "FFFFFF", dk2: "BE9100", lt2: "FFFBF0",
    accent1: "FFD23F", accent2: "0D1B3E", accent3: "BE9100",
    accent4: "FFFBF0", accent5: "FFFFFF", accent6: "FFD23F",
    hlink: "0D1B3E", folHlink: "BE9100",
  },
};

const pres = new pptxgen();
pres.layout = "LAYOUT_WIDE"; // 13.333 x 7.5
pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
pres.title = "Microclase: Sorry, could you say that again?";
pres.author = "MMercedesEnglish";
const C = pres.SchemeColor;

const EN = "Lora";
const HAND = "Nothing You Could Do";
const FOOT = "MMercedesEnglish  |  Beginner  |  Microclase  |  Do and does";

async function icon(Comp, hex = "#0D1B3E") {
  const svg = RDS.renderToStaticMarkup(React.createElement(Comp, { color: hex, size: 256 }));
  const buf = await sharp(Buffer.from(svg)).png().toBuffer();
  return "image/png;base64," + buf.toString("base64");
}

function frameObjects(withNotes) {
  const o = [
    { rect: { x: 0, y: 0, w: 13.333, h: 0.85, fill: { color: C.text1 } } },
            { text: { text: "Tiny Tips, Big Progress", options: { x: 1.3, y: 0.13, w: 5, h: 0.6, valign: "middle", fontFace: "Work Sans", fontSize: 16, bold: true, color: C.background1, margin: 0 } } },
            { text: { text: FOOT, options: { x: 0.6, y: 7.08, w: 9, h: 0.32, valign: "middle", fontFace: "Work Sans", fontSize: 11, color: C.text1, margin: 0 } } },
  ];
  if (withNotes) {
    o.push({ text: { text: "MY NOTES", options: { x: 0.6, y: 6.42, w: 1.3, h: 0.5, valign: "middle", fontFace: "Work Sans", fontSize: 12, bold: true, color: C.text1, margin: 0 } } });
    o.push({ line: { x: 1.95, y: 6.72, w: 10.8, h: 0, line: { color: C.text1, width: 1, dashType: "sysDot" } } });
    o.push({ line: { x: 0.6, y: 7.0, w: 12.15, h: 0, line: { color: C.text1, width: 1, dashType: "sysDot" } } });
  }
  return o;
}

const titlePh = {
  placeholder: {
    options: { name: "title", type: "title", x: 0.6, y: 1.0, w: 12.1, h: 0.9, fontFace: "Big Shoulders Display", fontSize: 36, bold: true, color: C.text1, align: "left", valign: "middle", margin: 0 },
    text: "Título",
  },
};

pres.defineSlideMaster({
  title: "MM_CONTENT", background: { color: C.background2 },
  objects: [...frameObjects(true), titlePh],
  slideNumber: { x: 12.0, y: 7.08, w: 0.75, h: 0.32, fontFace: "Work Sans", fontSize: 11, color: C.text1, align: "right" },
});
pres.defineSlideMaster({
  title: "MM_OPEN", background: { color: C.background2 },
  objects: [...frameObjects(false), titlePh],
  slideNumber: { x: 12.0, y: 7.08, w: 0.75, h: 0.32, fontFace: "Work Sans", fontSize: 11, color: C.text1, align: "right" },
});
pres.defineSlideMaster({
  title: "MM_COVER", background: { color: C.background2 },
  objects: frameObjects(false),
  slideNumber: { x: 12.0, y: 7.08, w: 0.75, h: 0.32, fontFace: "Work Sans", fontSize: 11, color: C.text1, align: "right" },
});

// ---------- helpers ----------
const card = (s, name, x, y, w, h, fill = C.background1) =>
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: name, x, y, w, h, rectRadius: 0.12, fill: { color: fill }, line: { color: C.text1, width: 1.5 } });

const txt = (s, name, runs, x, y, w, h, o = {}) =>
  s.addText(runs, { objectName: name, isTextBox: true, x, y, w, h, margin: 0, valign: "middle", fontFace: "Work Sans", fontSize: 24, color: C.text1, ...o });

const dlg = (lines, size = 24) => {
  const r = [];
  lines.forEach(([who, line], i) => {
    r.push({ text: who + "  ", options: { bold: true, fontFace: "Work Sans", fontSize: size } });
    r.push({ text: line, options: { italic: true, fontFace: EN, fontSize: size, breakLine: i < lines.length - 1 } });
  });
  return r;
};

const phraseChips = (s, chips, y, h1, h2) => {
  const xs = [0.6, 4.7, 8.8];
  chips.forEach((c, i) => {
    const mid = i === 1;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: `Chip ${i + 1} fondo`, x: xs[i], y, w: 3.93, h: h1 + h2, rectRadius: 0.12, fill: { color: C.background1 }, line: { color: C.text1, width: 1.5 } });
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: `Chip ${i + 1} frase`, x: xs[i], y, w: 3.93, h: h1, rectRadius: 0.12, fill: { color: mid ? C.accent1 : C.text1 }, line: { color: C.text1, width: 1.5 } });
    txt(s, `Chip ${i + 1} texto frase`, c[0], xs[i] + 0.2, y, 3.53, h1, { fontFace: EN, italic: true, bold: true, fontSize: 28, color: mid ? C.text1 : C.background1, align: "center" });
    txt(s, `Chip ${i + 1} descripción`, c[1], xs[i] + 0.25, y + h1 + 0.1, 3.43, h2 - 0.2, { fontSize: 24, align: "center" });
  });
};

const T = (t) => t.toUpperCase();
const hdr = (s) => {
  s.addShape(pres.shapes.OVAL, { objectName: "Logo MM fondo", x: 0.5, y: 0.13, w: 0.6, h: 0.6, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 } });
  s.addText("MM", { objectName: "Logo MM", isTextBox: true, x: 0.5, y: 0.13, w: 0.6, h: 0.6, align: "center", valign: "middle", fontFace: "Big Shoulders Display", fontSize: 20, bold: true, color: C.text1, margin: 0 });
  s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: "Pastilla nivel", x: 9.75, y: 0.2, w: 3.0, h: 0.45, rectRadius: 0.22, fill: { color: C.accent1 }, line: { color: C.accent1, width: 0 } });
  s.addText("Beginner English Tips", { objectName: "Texto pastilla nivel", isTextBox: true, x: 9.75, y: 0.2, w: 3.0, h: 0.45, align: "center", valign: "middle", fontFace: "Work Sans", fontSize: 14, bold: true, color: C.text1, margin: 0 });
};

(async () => {
  const ic = {
    ear: await icon(fa.FaVolumeUp),
    ask: await icon(fa.FaQuestionCircle),
    chat: await icon(fa.FaCommentDots),
    ok: await icon(fa.FaCheckCircle),
    no: await icon(fa.FaTimesCircle),
  };
  const avBuf = await sharp(AVATAR_SRC).jpeg({ quality: 90 }).toBuffer();
  const av = "image/jpeg;base64," + avBuf.toString("base64");
  const AVR = 1122 / 1402;

  const avatarPanel = (s, x, y, h) => {
    const imgH = h - 0.2, imgW = imgH * AVR;
    s.addShape(pres.shapes.ROUNDED_RECTANGLE, { objectName: "Marco avatar", x, y, w: imgW + 0.2, h, rectRadius: 0.12, fill: { color: C.text1 }, line: { color: C.text1, width: 1 } });
    s.addImage({ objectName: "Avatar Mercedes", data: av, x: x + 0.1, y: y + 0.1, w: imgW, h: imgH, altText: "Mercedes, profesora de MMercedesEnglish" });
    return imgW + 0.2;
  };
  const slide = (master, section, title) => {
    const s = pres.addSlide({ masterName: master, sectionTitle: section }); hdr(s);
    if (title) s.addText(T(title), { placeholder: "title" });
    return s;
  };
  const sec = (t) => pres.addSection({ title: t });
  const bar = (s, name, runs, y, h, fill = C.text1, size = 30) => {
    card(s, name, 0.6, y, 12.13, h, fill);
    txt(s, name + " texto", runs, 0.95, y, 11.4, h, { fontSize: size });
  };

  // 1 PORTADA
  sec("Apertura");
  let s = slide("MM_COVER", "Apertura");
  card(s, "Pastilla microclase", 0.6, 1.3, 2.6, 0.5, C.accent1);
  txt(s, "Texto pastilla", "Microclase · 8 min", 0.6, 1.3, 2.6, 0.5, { fontSize: 16, bold: true, align: "center" });
  txt(s, "Título portada", T("Do or does?"), 0.6, 1.95, 7.7, 2.2, { fontFace: "Big Shoulders Display", fontSize: 72, bold: true, valign: "top" });
  txt(s, "Subtítulo portada", "El auxiliar que te ayuda a preguntar y a negar en presente simple.", 0.6, 3.5, 7.4, 1.5, { fontSize: 26, valign: "top" });
  card(s, "Lema", 0.6, 6.1, 4.2, 0.55, C.text1);
  txt(s, "Texto lema", "Tiny Tips, Big Progress", 0.6, 6.1, 4.2, 0.55, { fontSize: 18, bold: true, color: C.accent1, align: "center" });
  avatarPanel(s, 8.53, 1.15, 5.2);
  s.addNotes("[0:00 a 0:30] APERTURA\nHola. En inglés, casi todas las preguntas tienen un ayudante: do o does. Hoy aprendes cuándo usar cada uno, cómo cambia el verbo y cómo responder de forma corta.\nPiensa: ¿cómo preguntarías “¿Ella trabaja aquí?” en inglés? (Pausa de 3 segundos. En clase en vivo, pide que lo escriban en el chat.) Vamos a verlo.");

  // 2 DE AFIRMACIÓN A PREGUNTA
  sec("Do y does");
  s = slide("MM_CONTENT", "Do y does", "De afirmación a pregunta");
  const two = (x, label, sentence, dark) => {
    card(s, label + " fondo", x, 2.05, 5.95, 2.5, dark ? C.accent1 : C.background1);
    txt(s, label + " etiqueta", label, x + 0.3, 2.2, 5.3, 0.5, { fontSize: 24, bold: true });
    txt(s, label + " frase", sentence, x + 0.3, 2.75, 5.3, 1.6, { fontFace: EN, italic: true, bold: true, fontSize: 32 });
  };
  two(0.6, "Afirmación", "She works here.", false);
  two(6.78, "Pregunta", "Does she work here?", true);
  bar(s, "Barra regla", [
    { text: "La  ", options: { color: C.background1, bold: true } },
    { text: "-s", options: { color: C.accent1, bold: true } },
    { text: "  pasa a ", options: { color: C.background1, bold: true } },
    { text: "does", options: { color: C.accent1, bold: true } },
    { text: ". El verbo vuelve a su forma base.", options: { color: C.background1, bold: true } },
  ], 4.85, 1.2, C.text1, 26);
  s.addNotes("[0:30 a 1:10] DE AFIRMACIÓN A PREGUNTA\nMira la oración: “She works here.” Para preguntar, pones “does” al inicio: “Does she work here?”\nFíjate en un detalle: la s pasa de “works” a “does”, y el verbo vuelve a su forma base, “work”.");

  // 3 DO
  s = slide("MM_CONTENT", "Do y does", "Do: I, you, we, they");
  phraseChips(s, [["Do", "el auxiliar"], ["you", "I, you, we, they"], ["like coffee?", "verbo en forma base"]], 2.05, 1.0, 1.5);
  card(s, "Barra significado y respuesta", 0.6, 4.8, 12.13, 1.3, C.text1);
  txt(s, "Significado", [
    { text: "Significa:  ", options: { color: C.accent1, bold: true } },
    { text: "¿Te gusta el café?", options: { color: C.background1, bold: true } },
  ], 0.95, 4.85, 11.4, 0.6, { fontSize: 28 });
  txt(s, "Respuesta corta", [
    { text: "Respuesta corta:  ", options: { color: C.accent1, bold: true } },
    { text: "Yes, I do.  /  No, I don’t.", options: { color: C.background1, fontFace: EN, italic: true, bold: true } },
  ], 0.95, 5.45, 11.4, 0.55, { fontSize: 24 });
  s.addNotes("[1:10 a 2:00] DO\nCon I, you, we y they, usamos “do”. Mira: “Do you like coffee?” Significa: “¿Te gusta el café?”\nSeñala cada segmento: “Do” es el auxiliar; “you” es quien hace la acción; “like coffee” va después, con el verbo en forma base.\nPara responder, usa una respuesta corta: “Yes, I do.” o “No, I don’t.” No repites el verbo.");

  // 4 DOES
  s = slide("MM_CONTENT", "Do y does", "Does: he, she, it");
  phraseChips(s, [["Does", "el auxiliar"], ["she", "he, she, it"], ["speak English?", "verbo en forma base"]], 2.05, 1.0, 1.5);
  card(s, "Barra significado y respuesta", 0.6, 4.8, 12.13, 1.3, C.text1);
  txt(s, "Significado", [
    { text: "Significa:  ", options: { color: C.accent1, bold: true } },
    { text: "¿Ella habla inglés?", options: { color: C.background1, bold: true } },
  ], 0.95, 4.85, 11.4, 0.6, { fontSize: 28 });
  txt(s, "Respuesta corta", [
    { text: "Respuesta corta:  ", options: { color: C.accent1, bold: true } },
    { text: "Yes, she does.  /  No, she doesn’t.", options: { color: C.background1, fontFace: EN, italic: true, bold: true } },
  ], 0.95, 5.45, 11.4, 0.55, { fontSize: 24 });
  s.addNotes("[2:00 a 2:50] DOES\nCon he, she e it, usamos “does”. Mira: “Does she speak English?” Significa: “¿Ella habla inglés?”\nOtra vez, el verbo queda en forma base: “speak”, no “speaks”.\nPara responder: “Yes, she does.” o “No, she doesn’t.”");

  // 5 ERROR COMÚN
  sec("El error más común");
  s = slide("MM_CONTENT", "El error más común", "El error más común");
  card(s, "Incorrecto fondo", 0.6, 2.05, 5.95, 2.2);
  s.addImage({ objectName: "Ícono incorrecto", data: ic.no, x: 0.9, y: 2.25, w: 0.6, h: 0.6, altText: "Incorrecto" });
  txt(s, "Etiqueta incorrecto", "Incorrecto", 1.7, 2.25, 4.5, 0.6, { fontSize: 24, bold: true });
  txt(s, "Frase incorrecta", "Does she works here?", 0.9, 3.0, 5.4, 1.1, { fontFace: EN, italic: true, bold: true, fontSize: 28 });
  card(s, "Correcto fondo", 6.78, 2.05, 5.95, 2.2, C.accent1);
  s.addImage({ objectName: "Ícono correcto", data: ic.ok, x: 7.08, y: 2.25, w: 0.6, h: 0.6, altText: "Correcto" });
  txt(s, "Etiqueta correcto", "Correcto", 7.88, 2.25, 4.5, 0.6, { fontSize: 24, bold: true });
  txt(s, "Frase correcta", "Does she work here?", 7.08, 3.0, 5.4, 1.1, { fontFace: EN, italic: true, bold: true, fontSize: 28 });
  card(s, "Barra tip", 0.6, 4.55, 12.13, 1.55, C.background1);
  txt(s, "Tip Mercedes", [
    { text: "Tip Mercedes:  ", options: { fontFace: HAND, color: C.accent3, bold: true, breakLine: false } },
    { text: "“Does” ya lleva la -s, así que el verbo no la repite. Se pronuncia /dʌz/ y rima con buzz.", options: {} },
  ], 0.95, 4.6, 11.4, 1.45, { fontSize: 26 });
  s.addNotes("[2:50 a 3:35] EL ERROR MÁS COMÚN\nEste es el error más común: “Does she works here?” Es incorrecto. “Does” ya lleva la s, así que el verbo no la repite. Lo correcto es “Does she work here?”\nUn tip de pronunciación: “does” rima con “buzz”, no con “doze”.");

  // 6 NEGATIVOS
  sec("Negativos");
  s = slide("MM_CONTENT", "Negativos", "Negativos: don’t y doesn’t");
  phraseChips(s, [["don’t", "con I, you, we, they"], ["doesn’t", "con he, she, it"], ["+ verbo base", "work, like, speak"]], 2.05, 1.0, 1.5);
  card(s, "Barra ejemplos", 0.6, 4.8, 12.13, 1.3, C.text1);
  txt(s, "Ejemplos", [
    { text: "I don’t like tea.", options: { color: C.accent1, fontFace: EN, italic: true, bold: true, breakLine: true } },
    { text: "She doesn’t work today.", options: { color: C.background1, fontFace: EN, italic: true, bold: true } },
  ], 0.95, 4.8, 11.4, 1.3, { fontSize: 28, paraSpaceAfter: 6 });
  s.addNotes("[3:35 a 4:25] NEGATIVOS\nPara decir que no, usamos “don’t” con I, you, we y they, y “doesn’t” con he, she e it. “I don’t like tea.” “She doesn’t work today.”\nDespués va el verbo en forma base. La regla es la misma: el auxiliar lleva la s, el verbo no.");

  // 7 PRÁCTICA EN ECO
  sec("Práctica");
  s = slide("MM_CONTENT", "Práctica", "Repite después de mí");
  card(s, "Frases eco", 0.6, 2.05, 8.6, 3.0);
  txt(s, "Lista eco", [
    { text: "1  Do you like coffee?", options: { breakLine: true } },
    { text: "2  Does she speak English?", options: { breakLine: true } },
    { text: "3  He doesn’t work on Sunday.", options: {} },
  ], 0.95, 2.05, 7.9, 3.0, { fontFace: EN, italic: true, bold: true, fontSize: 28, paraSpaceAfter: 14 });
  card(s, "Instrucción eco", 0.6, 5.25, 8.6, 0.85, C.accent1);
  s.addImage({ objectName: "Ícono audio", data: ic.ear, x: 0.9, y: 5.38, w: 0.6, h: 0.6, altText: "Altavoz" });
  txt(s, "Texto instrucción", "Escucha, pausa y repite.", 1.75, 5.25, 7.2, 0.85, { fontSize: 26, bold: true });
  avatarPanel(s, 9.5, 2.05, 4.0);
  s.addNotes("[4:25 a 5:10] PRÁCTICA EN ECO\nAhora repite después de mí, en voz alta. Di cada frase con volumen normal y claro, haz una pausa de 4 segundos para que repitan y pasa a la siguiente.\n1. “Do you like coffee?” (Pausa de 4 segundos.)\n2. “Does she speak English?” (Pausa de 4 segundos.)\n3. “He doesn’t work on Sunday.” (Pausa de 4 segundos.)\nMuy bien.");

  // 8 ¿DO O DOES? (preguntas)
  s = slide("MM_CONTENT", "Práctica", "¿Do o does?");
  const qs = ["you speak Spanish?", "she live here?", "they work on Monday?", "he play soccer?"];
  qs.forEach((q, i) => {
    const x = i % 2 === 0 ? 0.6 : 6.78, y = i < 2 ? 2.05 : 3.95;
    card(s, `Pregunta ${i + 1} fondo`, x, y, 5.95, 1.65, i % 3 === 0 ? C.background1 : C.accent1);
    txt(s, `Pregunta ${i + 1} número`, String(i + 1), x + 0.25, y, 0.6, 1.65, { fontFace: "Big Shoulders Display", fontSize: 40, bold: true });
    txt(s, `Pregunta ${i + 1} frase`, [
      { text: "____  ", options: { bold: true } },
      { text: q, options: {} },
    ], x + 0.95, y, 4.85, 1.65, { fontFace: EN, italic: true, fontSize: 24 });
  });
  s.addNotes("[5:10 a 5:55] ¿DO O DOES?\nElige do o does. Lee cada oración y haz una pausa de 4 segundos tras cada una.\nUno: “you speak Spanish”. Dos: “she live here”. Tres: “they work on Monday”. Cuatro: “he play soccer”.\nAvanza al siguiente slide solo después de las cuatro pausas.");

  // 9 RESPUESTAS
  s = slide("MM_CONTENT", "Práctica", "Respuestas");
  const as = ["Do you speak Spanish?", "Does she live here?", "Do they work on Monday?", "Does he play soccer?"];
  card(s, "Respuestas fondo", 0.6, 2.05, 12.13, 2.65);
  as.forEach((a, i) => {
    const x = i % 2 === 0 ? 0.95 : 6.95, y = i < 2 ? 2.2 : 3.45;
    txt(s, `Respuesta ${i + 1}`, a, x, y, 5.6, 1.0, { fontFace: EN, italic: true, bold: true, fontSize: 26 });
  });
  card(s, "Regla final", 0.6, 4.95, 12.13, 1.15, C.accent1);
  txt(s, "Regla final texto", [
    { text: "I, you, we, they → do.   ", options: { bold: true } },
    { text: "He, she, it → does.", options: { bold: true } },
  ], 0.95, 4.95, 11.4, 1.15, { fontSize: 28 });
  s.addNotes("[5:55 a 6:25] RESPUESTAS\nUno: “Do you speak Spanish?” Dos: “Does she live here?” Tres: “Do they work on Monday?” Cuatro: “Does he play soccer?”\nRecuerda: I, you, we y they usan do. He, she e it usan does.");

  // 10 ROLEPLAY
  sec("Tu turno");
  s = slide("MM_CONTENT", "Tu turno", "Tu turno: la entrevista");
  card(s, "Escucha fondo", 0.6, 2.05, 6.2, 1.9, C.accent1);
  s.addImage({ objectName: "Ícono audio", data: ic.ear, x: 0.9, y: 2.7, w: 0.7, h: 0.7, altText: "Altavoz" });
  txt(s, "Escucha texto", [
    { text: "Escucha la pregunta.", options: { bold: true, breakLine: true } },
    { text: "Piensa durante 5 segundos.", options: {} },
  ], 1.9, 2.05, 4.7, 1.9, { fontSize: 26, paraSpaceAfter: 6 });
  card(s, "Responde fondo", 0.6, 4.2, 6.2, 1.9);
  s.addImage({ objectName: "Ícono pregunta", data: ic.ask, x: 0.9, y: 4.85, w: 0.7, h: 0.7, altText: "Pregunta" });
  txt(s, "Responde texto", "Responde en voz alta con una respuesta corta.", 1.9, 4.2, 4.7, 1.9, { fontSize: 26, bold: true });
  card(s, "Ayuda fondo", 7.1, 2.05, 5.63, 4.05, C.text1);
  txt(s, "Ayuda etiqueta", "Respuestas cortas", 7.4, 2.2, 5.0, 0.6, { fontSize: 22, bold: true, color: C.accent1 });
  txt(s, "Ayuda frases", [
    { text: "Yes, I do.", options: { breakLine: true } },
    { text: "No, I don’t.", options: { breakLine: true } },
    { text: "Yes, she does.", options: { breakLine: true } },
    { text: "No, she doesn’t.", options: {} },
  ], 7.4, 2.85, 5.0, 3.1, { fontFace: EN, italic: true, bold: true, fontSize: 28, color: C.background1, paraSpaceAfter: 10, valign: "top" });
  s.addNotes("[6:25 a 7:10] TU TURNO\nAhora responde con una respuesta corta. Escucha: “Do you speak English?” (Pausa de 5 segundos.) Por ejemplo: “Yes, I do.”\nAhora: “Does your friend live here?” (Pausa de 5 segundos.) Por ejemplo: “No, she doesn’t.”\nResponde lo que sea verdad para ti. Lee las preguntas con volumen normal y claro.");

  // 11 CIERRE
  sec("Cierre");
  s = slide("MM_OPEN", "Cierre", "Hoy aprendiste");
  card(s, "Regla do", 0.6, 2.05, 8.6, 1.2, C.accent1);
  txt(s, "Regla do texto", "I, you, we, they  →  do", 0.95, 2.05, 7.9, 1.2, { fontSize: 30, bold: true });
  card(s, "Regla does", 0.6, 3.45, 8.6, 1.2, C.text1);
  txt(s, "Regla does texto", "he, she, it  →  does", 0.95, 3.45, 7.9, 1.2, { fontSize: 30, bold: true, color: C.background1 });
  card(s, "Pregunta de salida", 0.6, 4.85, 8.6, 1.9);
  txt(s, "Pregunta", [
    { text: "Pregunta de salida:", options: { fontSize: 24, breakLine: true } },
    { text: "Corrige: He don’t like tea.", options: { fontFace: EN, italic: true, bold: true, fontSize: 30 } },
  ], 0.95, 4.85, 7.9, 1.9, { paraSpaceAfter: 6 });
  avatarPanel(s, 9.5, 2.05, 4.0);
  s.addNotes("[7:10 a 7:45] CIERRE\nHoy aprendiste que do va con I, you, we y they, y does va con he, she e it. Después del auxiliar, el verbo queda en forma base.\nPregunta de salida: corrige “He don’t like tea.” (Pausa de 5 segundos.) La respuesta es: “He doesn’t like tea.” Hasta la próxima.");

  await pres.writeFile({ fileName: OUT });
  await applyTheme(OUT, THEME);
  console.log("done");
})();
