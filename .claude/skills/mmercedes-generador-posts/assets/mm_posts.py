#!/usr/bin/env python3
"""MMercedesEnglish: generador de PNG 1080x1920 (Pillow).

Subcomandos:
  como-se-dice   serie "¿Cómo se dice...?" (Opción B)
  no-digas       serie "No digas... Di..."
  broll          overlay de B-roll (estructura corta)

Uso:
  python3 mm_posts.py como-se-dice contenido.json --out ./salida [--avatar master.png]

Portátil: las fuentes viajan en ./fonts, no hay rutas de sesión. La carpeta de
fuentes se puede sustituir con la variable MM_FONTS. El avatar master se pasa con
--avatar o con la variable MM_AVATAR (PNG con fondo transparente).
"""
import argparse
import json
import math
import os
import sys
import zlib
from pathlib import Path

from PIL import Image, ImageDraw, ImageFont

HERE = Path(__file__).resolve().parent

# ── PALETA OFICIAL (mmercedes-colores). Ningún otro color existe en la marca ──
NAVY = (13, 27, 62)          # #0D1B3E
YELLOW = (255, 210, 63)      # #FFD23F
CREAM = (255, 251, 240)      # #FFFBF0
WHITE = (255, 255, 255)      # #FFFFFF
RED_C = (205, 40, 35)        # #CD2823  solo X, tachado, etiqueta, pastilla de serie
GREEN_C = (30, 150, 80)      # #1E9650  solo check y etiqueta SIGNIFICA
TIP_BG = (255, 251, 204)     # #FFFBCC  solo fondo del Tip Mercedes
GOLD = (190, 145, 0)         # #BE9100  solo label "Tip Mercedes:"
GRAY_L = (230, 230, 235)     # #E6E6EB  bordes y divisores
FOOT_GRAY = (200, 200, 215)  # tagline del footer (mmercedes-colores)
W, H = 1080, 1920
P = 52

NIVELES = {"beginner": "Beginner English Tips", "intermediate": "Intermediate English Tips"}

# ── BANCO DE CTAs (mmercedes-colores). Todos dirigen al link en bio ──
CTA_BANK = {
    "vocabulario": [
        ("¿Quieres aprender más expresiones como esta?", "Revisa el link en mi bio."),
        ("¿Lista para hablar inglés con más confianza?", "Todo lo que necesitas está en mi bio."),
        ("¿Te gustó este tip? Hay más donde este vino.", "Encuéntralos en el link de mi bio."),
    ],
    "errores": [
        ("¿Quieres dejar de cometer estos errores?", "Tengo más recursos para ti en mi bio."),
        ("¿Listo para hablar inglés sin estos errores?", "Empieza hoy: link en mi bio."),
        ("¿Cuántos de estos errores cometías tú?", "Aprende más en el link de mi bio."),
    ],
    "falsos_cognados": [
        ("¿Cuántos falsos cognados conoces?", "Descubre más en el link de mi bio."),
        ("El inglés está lleno de trampas como esta.", "Evítalas todas: link en mi bio."),
        ("¿Quieres dominar el inglés real?", "Da el primer paso: link en mi bio."),
    ],
    "gramatica": [
        ("¿Quieres más tips como este?", "Revisa el link en mi bio."),
        ("Para seguir aprendiendo inglés sin confusiones,", "revisa el link en mi bio."),
        ("Si quieres hablar inglés con más seguridad,", "todo está en el link de mi bio."),
    ],
    "verbos": [
        ("¿Quieres dominar los verbos irregulares en inglés?", "Link en mi bio."),
        ("Para más práctica con verbos en inglés,", "revisa el link en mi bio."),
        ("¿Lista para no volver a confundirte con los verbos?", "Link en mi bio."),
    ],
    "universal": [
        ("Para más contenido como este,", "revisa el link en mi bio."),
        ("Si quieres seguir aprendiendo inglés,", "todo está en mi bio."),
        ("¿Lista para llevar tu inglés al siguiente nivel?", "Link en mi bio."),
        ("Más tips, más práctica, más confianza.", "Todo en el link de mi bio."),
    ],
}

# Qué categoría del banco corresponde a cada serie (criterio: el CTA habla del
# mismo tema que la pieza)
SERIE_CTA = {
    "como-se-dice": "vocabulario",
    "no-digas": "errores",
    "broll": "universal",
}

# Frases de CTA retiradas por decisión de Mercedes (nunca deben aparecer)
CTA_PROHIBIDO = ("comentarios", "cuéntame", "cuentame", "conocías", "conocias", "conocías?")


def _stable_index(seed, n):
    """Índice reproducible: el mismo tema elige siempre el mismo CTA."""
    return zlib.crc32(seed.encode("utf-8")) % n


def pick_cta(serie, tema="", categoria=None, override=None):
    """Devuelve (linea1, linea2). override tiene prioridad si es válido."""
    if override and len(override) == 2:
        l1, l2 = override
    else:
        cat = categoria or SERIE_CTA.get(serie, "universal")
        bank = CTA_BANK[cat]
        l1, l2 = bank[_stable_index(f"{serie}|{tema}", len(bank))]
    joined = f"{l1} {l2}".lower()
    if any(bad in joined for bad in CTA_PROHIBIDO):
        raise ValueError(f"CTA no permitido (comentarios o '¿Lo conocías?'): {l1} / {l2}")
    if "bio" not in joined:
        raise ValueError(f"El CTA debe dirigir al link en bio: {l1} / {l2}")
    return l1, l2


# ── FUENTES ──
def font_dir():
    for cand in (os.environ.get("MM_FONTS"), HERE / "fonts"):
        if cand and Path(cand).is_dir():
            return Path(cand)
    raise SystemExit("No encuentro la carpeta de fuentes (assets/fonts o MM_FONTS).")


_FD = None


def F(name, size):
    global _FD
    if _FD is None:
        _FD = font_dir()
    path = _FD / name
    if not path.exists():
        raise SystemExit(f"Falta la fuente {name} en {_FD}")
    return ImageFont.truetype(str(path), size)


BS, WSB, WSR, LORA, NYC = (
    "BigShoulders-Bold.ttf", "WorkSans-Bold.ttf", "WorkSans-Regular.ttf",
    "Lora-Italic.ttf", "NothingYouCouldDo-Regular.ttf",
)


# ── PRIMITIVAS ──
def rr(d, xy, r, **kw):
    d.rounded_rectangle(xy, radius=r, **kw)


def tw(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[2] - b[0]


def th(d, t, f):
    b = d.textbbox((0, 0), t, font=f)
    return b[3] - b[1]


def ctext(d, cx, y, t, f, c):
    d.text((cx - tw(d, t, f) // 2, y), t, font=f, fill=c)


# ── GUARDIA ANTI-CASCADA ──
# Cascada = bloques con distinto margen izquierdo o distinto ancho de columna,
# desfasados, rotados o superpuestos (mmercedes-brand, "Cascada"). Cada bloque de
# contenido se registra y check_layout() detiene el render si hay alguno.
_BLOCKS = []


def reg(kind, name, x1, y1, x2, y2):
    """kind: 'card' (alineado a margen estándar), 'zona' (junto al avatar), 'texto' (solo no tapar)"""
    _BLOCKS.append((kind, name, x1, y1, x2, y2))


def check_layout(avatar_rect=None):
    cards = sorted([b for b in _BLOCKS if b[0] in ("card", "zona")], key=lambda b: b[3])
    errs = []
    for k, n, x1, y1, x2, y2 in cards:
        if x1 != P:
            errs.append(f"'{n}' no comparte el margen izquierdo ({x1} en vez de {P})")
        if k == "card" and x2 != W - P:
            errs.append(f"'{n}' no tiene el ancho de columna estándar (termina en {x2}, debe ser {W - P})")
    zr = {b[4] for b in cards if b[0] == "zona"}
    if len(zr) > 1:
        errs.append(f"los bloques junto al avatar tienen anchos distintos (bordes derechos {sorted(zr)})")
    for a, b in zip(cards, cards[1:]):
        if b[3] < a[5]:
            errs.append(f"'{b[1]}' se superpone con '{a[1]}' ({b[3]} < {a[5]})")
    if avatar_rect:
        ax1, ay1, ax2, ay2 = avatar_rect
        for k, n, x1, y1, x2, y2 in _BLOCKS:
            if k == "card" or k == "zona" or k == "texto":
                if x1 < ax2 and x2 > ax1 and y1 < ay2 and y2 > ay1:
                    errs.append(f"el avatar tapa '{n}'")
    if errs:
        raise SystemExit("CASCADA o solapamiento detectado, no se genera el PNG:\n  - " + "\n  - ".join(errs))


def ttext(d, cx, ytop, t, f, c):
    """Centra en x y ancla por el borde superior real del glifo (evita el desfase del
    tipo grande, que hacía chocar subrayados y tachados con el texto)."""
    b = d.textbbox((0, 0), t, font=f)
    d.text((cx - (b[2] - b[0]) // 2 - b[0], ytop - b[1]), t, font=f, fill=c)


def star(d, cx, cy, o, i, col):
    pts = []
    for n in range(10):
        a = math.pi * n / 5 - math.pi / 2
        r = o if n % 2 == 0 else i
        pts.append((cx + r * math.cos(a), cy + r * math.sin(a)))
    d.polygon(pts, fill=col)


def xmark(d, cx, cy, s, col, w=3):
    d.line([(cx - s, cy - s), (cx + s, cy + s)], fill=col, width=w)
    d.line([(cx + s, cy - s), (cx - s, cy + s)], fill=col, width=w)


def check(d, cx, cy, s, col, w=3):
    pts = [(cx - s * .5, cy), (cx - s * .1, cy + s * .5), (cx + s * .5, cy - s * .4)]
    d.line(pts[:2], fill=col, width=w)
    d.line(pts[1:], fill=col, width=w)


def fit(d, text, name, size, max_w, min_size=12):
    """Reduce solo la tipografía de ese texto hasta que quepa. Nunca toca zonas ni colores."""
    s = size
    while s > min_size and tw(d, text, F(name, s)) > max_w:
        s -= 1
    return F(name, s)


def wrap(d, text, font, max_w):
    """Salto de línea voluntario con \\n, y automático si una línea excede el ancho."""
    out = []
    for para in str(text).split("\n"):
        words, line = para.split(), ""
        for w_ in words:
            trial = (line + " " + w_).strip()
            if tw(d, trial, font) <= max_w or not line:
                line = trial
            else:
                out.append(line)
                line = w_
        out.append(line)
    return out


def tip_items(tip):
    """['texto', '**negrita'] o [['bold','texto']] -> [(estilo, texto)]"""
    items = []
    for it in tip:
        if isinstance(it, (list, tuple)):
            items.append((it[0], it[1]))
        elif str(it).startswith("**"):
            items.append(("bold", str(it)[2:]))
        else:
            items.append(("normal", str(it)))
    return items


# ── AVATAR MASTER (capa opcional, nunca se estira ni se recolorea) ──
def load_avatar(path):
    if not path:
        path = os.environ.get("MM_AVATAR") or None
    if not path:
        default = HERE / "avatar" / "master.png"
        path = str(default) if default.exists() else None
    if not path:
        return None
    img = Image.open(path)
    if img.mode != "RGBA" or img.getchannel("A").getextrema()[0] == 255:
        raise SystemExit(
            "El avatar debe ser un PNG con fondo transparente (recorte del master). "
            f"Recibí {path} ({img.mode}) sin transparencia."
        )
    return img.crop(img.getchannel("A").getbbox())


def avatar_size(av, max_w, max_h):
    """Tamaño con la proporción original. Un solo factor para X e Y."""
    k = min(max_w / av.width, max_h / av.height)
    return int(av.width * k), int(av.height * k)


def paste_avatar(img, av, w, h, bottom, bleed=18):
    """Sangra por el borde derecho del canvas: corte intencional, sin fade."""
    res = av.resize((w, h), Image.LANCZOS)
    img.paste(res, (W - w + bleed, bottom - h), res)


# ── BLOQUES COMUNES ──
def header(d, nivel, serie_txt):
    d.rectangle([0, 0, W, 92], fill=NAVY)
    d.rectangle([0, 92, W, 100], fill=YELLOW)
    fMM, fPIL = F(BS, 24), F(WSB, 18)
    rr(d, [P, 18, P + 52, 74], 26, fill=YELLOW)
    ctext(d, P + 26, 26, "MM", fMM, NAVY)
    p2 = NIVELES[nivel]
    p2w = tw(d, p2, fPIL) + 28
    rr(d, [P + 62, 22, P + 62 + p2w, 70], 20, outline=WHITE, width=2)
    ctext(d, P + 62 + p2w // 2, 32, p2, fPIL, WHITE)
    p3w = tw(d, serie_txt, fPIL) + 28
    rr(d, [W - P - p3w, 22, W - P, 70], 20, fill=RED_C)
    ctext(d, W - P - p3w // 2, 32, serie_txt, fPIL, WHITE)


def examples_header(d, y):
    fEH = F(WSB, 17)
    rr(d, [P, y, W - P, y + 48], 10, fill=NAVY)
    ctext(d, W // 2, y + 12, "EJEMPLOS", fEH, YELLOW)
    star(d, P + 30, y + 24, 6, 2, YELLOW)
    star(d, W - P - 30, y + 24, 6, 2, YELLOW)
    return y + 52


def tip_block(d, y, lines, step, base_h):
    items = tip_items(lines)
    fTL, fTR, fTB = F(NYC, 22), F(WSR, 17), F(WSB, 17)
    maxw = W - 2 * P - 36
    rendered = []
    for style, text in items:
        f = fTB if style == "bold" else fTR
        for ln in wrap(d, text, f, maxw):
            rendered.append((f, ln))
    tip_h = max(base_h, 48 + len(rendered) * step + 18)
    rr(d, [P, y, W - P, y + tip_h], 12, fill=TIP_BG, outline=YELLOW, width=2)
    reg("card", "tip-mercedes", P, y, W - P, y + tip_h)
    d.text((P + 18, y + 12), "Tip Mercedes:", font=fTL, fill=GOLD)
    star(d, W - P - 18, y + 22, 8, 3, YELLOW)
    star(d, W - P - 44, y + 44, 5, 2, GOLD)
    ty = y + 48
    for f, ln in rendered:
        d.text((P + 18, ty), ln, font=f, fill=NAVY)
        ty += step
    return y + tip_h + 16


def cta_block(d, y, l1, l2):
    CTA_H = 80
    rr(d, [0, y, W, y + CTA_H], 0, fill=YELLOW)
    maxw = 840
    f1 = fit(d, l1, WSB, 26, maxw)
    f2 = fit(d, l2, WSB, 22, maxw)
    rr(d, [P, y + 14, P + 48, y + 50], 12, fill=NAVY)
    d.polygon([(P + 8, y + 50), (P + 8, y + 64), (P + 28, y + 50)], fill=NAVY)
    star(d, P + 24, y + 32, 5, 2, YELLOW)
    ctext(d, W // 2 + 30, y + 8, l1, f1, NAVY)
    ctext(d, W // 2 + 30, y + 42, l2, f2, NAVY)
    return y + CTA_H


def footer(d, y):
    d.rectangle([0, y, W, H], fill=NAVY)
    fF1, fF2 = F(BS, 32), F(WSR, 18)
    rr(d, [P, y + 18, P + 52, y + 62], 26, fill=YELLOW)
    ctext(d, P + 26, y + 24, "MM", F(BS, 22), NAVY)
    d.text((P + 62, y + 22), "MMercedes", font=fF1, fill=WHITE)
    d.text((P + 62 + tw(d, "MMercedes", fF1), y + 22), "English", font=fF1, fill=YELLOW)
    star(d, P + 18, y + 90, 9, 4, YELLOW)
    d.text((P + 36, y + 82), "Tiny Tips, Big Progress", font=fF2, fill=FOOT_GRAY)


def nivel_key(c):
    n = str(c.get("nivel", "beginner")).strip().lower()
    if n not in NIVELES:
        raise SystemExit(f"nivel debe ser Beginner o Intermediate (recibí '{c.get('nivel')}')")
    return n


def pair_text(d, x, y, lines, font, fill, step):
    for ln in lines:
        d.text((x, y), ln, font=font, fill=fill)
        y += step
    return y


# ═══════════════════ ¿CÓMO SE DICE? (Opción B) ═══════════════════
def como_se_dice(c, avatar=None):
    _BLOCKS.clear()
    nivel = nivel_key(c)
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    header(d, nivel, "¿Cómo se dice...?")

    # Con avatar, la columna de contenido se estrecha solo en hook y reveal
    av_w = av_h = 0
    if avatar is not None:
        av_w, av_h = avatar_size(avatar, 430, 600)
    col_l, col_r = P, (W - av_w - 10 if avatar is not None else W - P)
    col_cx = (col_l + col_r) // 2

    y = 116
    fHK = F(LORA, 30)
    ctext(d, col_cx, y, "¿Cómo se dice en inglés...", fHK, NAVY)
    y += 48

    concepto = c["concepto_es"].strip()
    if not concepto.startswith('"'):
        concepto = f'"{concepto}"'
    fHKB = F(BS, 82)
    lines = wrap(d, concepto, fHKB, col_r - col_l - 90)
    while len(lines) > 2 and fHKB.size > 40:
        fHKB = F(BS, fHKB.size - 4)
        lines = wrap(d, concepto, fHKB, col_r - col_l - 90)
    line_h = th(d, lines[0], fHKB) + 8
    total_h = len(lines) * line_h + 32
    rr(d, [col_l, y, col_r, y + total_h], 16, fill=NAVY)
    reg("zona" if avatar is not None else "card", "gancho", col_l, y, col_r, y + total_h)
    ly = y + 16
    for ln in lines:
        ttext(d, col_cx, ly, ln, fHKB, YELLOW)
        ly += line_h
    star(d, col_l + 22, y + total_h // 2, 10, 4, YELLOW)
    star(d, col_r - 22, y + total_h // 2, 10, 4, YELLOW)
    hook_top = 116
    y += total_h + 20

    # REVEAL
    REV_Y1 = y
    expr = c["expresion_en"].upper()
    fEX = F(BS, 100)
    ex_lines = wrap(d, expr, fEX, col_r - col_l - 60)
    while (len(ex_lines) > 2 or any(tw(d, l, fEX) > col_r - col_l - 60 for l in ex_lines)) and fEX.size > 40:
        fEX = F(BS, fEX.size - 4)
        ex_lines = wrap(d, expr, fEX, col_r - col_l - 60)
    fSB = F(WSB, 26)
    rev_h = len(ex_lines) * (th(d, ex_lines[0], fEX) + 8) + 80
    REV_Y2 = REV_Y1 + rev_h
    d.rectangle([0, REV_Y1, W, REV_Y2], fill=NAVY)
    ey = REV_Y1 + 24
    for ln in ex_lines:
        ttext(d, col_cx, ey, ln, fEX, YELLOW)
        ey += th(d, ln, fEX) + 8
    ctext(d, col_cx, REV_Y2 - 42, c["subtitulo"], fSB, WHITE)
    _rw = max([tw(d, l, fEX) for l in ex_lines] + [tw(d, c["subtitulo"], fSB)]) // 2 + 30
    reg("texto", "reveal", col_cx - _rw, REV_Y1, col_cx + _rw, REV_Y2)
    star(d, P + 22, REV_Y1 + 30, 10, 4, YELLOW)
    if avatar is None:
        star(d, W - P - 22, REV_Y1 + 30, 10, 4, YELLOW)
    d.rectangle([0, REV_Y2, W, REV_Y2 + 8], fill=YELLOW)
    y = REV_Y2 + 24

    if avatar is not None:
        max_h = REV_Y2 - (hook_top - 8)
        w2, h2 = avatar_size(avatar, av_w, min(av_h, max_h))
        paste_avatar(img, avatar, w2, h2, REV_Y2)
        av_rect = (W - w2 + 18, REV_Y2 - h2, W, REV_Y2)
    else:
        av_rect = None

    # PANEL LITERAL / SIGNIFICA
    fPN, fPV, fIT = F(WSB, 18), F(WSR, 20), F(LORA, 19)
    PNL_H = 230
    rr(d, [P, y, W - P, y + PNL_H], 12, fill=WHITE, outline=GRAY_L, width=1)
    reg("card", "literal-significa", P, y, W - P, y + PNL_H)
    MID = W // 2 + 4
    d.line([(MID, y + 8), (MID, y + PNL_H - 8)], fill=GRAY_L, width=1)
    half_w = MID - P - 32
    d.ellipse([P + 16, y + 16, P + 44, y + 44], fill=RED_C)
    xmark(d, P + 30, y + 30, 6, WHITE, 2)
    rr(d, [P + 52, y + 14, P + 52 + tw(d, "LITERAL:", fPN) + 16, y + 48], 8, fill=RED_C)
    d.text((P + 60, y + 18), "LITERAL:", font=fPN, fill=WHITE)
    pair_text(d, P + 16, y + 56, wrap(d, c["literal"], fIT, half_w), fIT, NAVY, 26)
    d.ellipse([MID + 16, y + 16, MID + 44, y + 44], fill=GREEN_C)
    check(d, MID + 30, y + 30, 14, WHITE, 2)
    rr(d, [MID + 52, y + 14, MID + 52 + tw(d, "SIGNIFICA:", fPN) + 16, y + 48], 8, fill=GREEN_C)
    d.text((MID + 60, y + 18), "SIGNIFICA:", font=fPN, fill=WHITE)
    pair_text(d, MID + 16, y + 56, wrap(d, c["significa"], fPV, W - P - MID - 32), fPV, NAVY, 26)
    y += PNL_H + 20

    # EJEMPLOS
    y = examples_header(d, y)
    fEH, fENB, fESR = F(WSB, 17), F(WSB, 19), F(WSR, 18)
    ex = c["ejemplos"]
    COL = W // 2 + 4
    TABLE_H = len(ex) * 100 + 50
    rr(d, [P, y, W - P, y + TABLE_H], 10, fill=WHITE, outline=GRAY_L, width=1)
    reg("card", "ejemplos", P, y - 52, W - P, y + TABLE_H)
    d.text((P + 20, y + 12), "EN INGLÉS", font=fEH, fill=NAVY)
    d.text((COL + 16, y + 12), "EN ESPAÑOL", font=fEH, fill=NAVY)
    d.line([(P, y + 38), (W - P, y + 38)], fill=GRAY_L, width=1)
    d.line([(COL, y + 38), (COL, y + TABLE_H)], fill=GRAY_L, width=1)
    ry = y + 48
    for i, (en, es) in enumerate(ex):
        pair_text(d, P + 16, ry, wrap(d, en, fENB, COL - P - 32), fENB, NAVY, 24)
        pair_text(d, COL + 16, ry, wrap(d, es, fESR, W - P - COL - 32), fESR, NAVY, 24)
        ry += 100
        if i < len(ex) - 1:
            d.line([(P + 8, ry - 8), (W - P - 8, ry - 8)], fill=GRAY_L, width=1)
    y += TABLE_H + 20

    y = tip_block(d, y, c["tip"], step=24, base_h=180)
    l1, l2 = pick_cta("como-se-dice", c.get("tema", c["expresion_en"]), c.get("cta_categoria"), c.get("cta"))
    y = cta_block(d, y, l1, l2)
    if y > H - 110:
        raise SystemExit(f"El contenido no cabe (termina en y={y}). Acorta el texto o reduce ejemplos.")
    check_layout(av_rect)
    footer(d, y)
    return img


# ═══════════════════ NO DIGAS... DI... ═══════════════════
def no_digas(c, avatar=None):
    _BLOCKS.clear()
    nivel = nivel_key(c)
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    header(d, nivel, "No digas... Di...")

    av_w = av_h = 0
    if avatar is not None:
        av_w, av_h = avatar_size(avatar, 420, 700)
    col_l, col_r = P, (W - av_w - 10 if avatar is not None else W - P)
    col_cx = (col_l + col_r) // 2

    y = 116
    fTIT = F(BS, 88)
    t1, t2 = "NO DIGAS...", "DI"
    while tw(d, t1, fTIT) + 24 + tw(d, t2, fTIT) > col_r - col_l - 100 and fTIT.size > 40:
        fTIT = F(BS, fTIT.size - 4)
    t1w, t2w = tw(d, t1, fTIT), tw(d, t2, fTIT)
    total = t1w + 24 + t2w
    x0 = col_cx - total // 2
    tb = d.textbbox((0, 0), t1, font=fTIT)
    d.text((x0 - tb[0], y - tb[1]), t1, font=fTIT, fill=NAVY)
    d.text((x0 + t1w + 24 - d.textbbox((0, 0), t2, font=fTIT)[0], y - tb[1]), t2, font=fTIT, fill=YELLOW)
    UL_W = total + 40
    UL_Y = y + th(d, t1, fTIT) + 8
    d.rectangle([col_cx - UL_W // 2, UL_Y, col_cx + UL_W // 2, UL_Y + 6], fill=YELLOW)
    star(d, col_l + 20, y + 50, 9, 4, YELLOW)
    star(d, col_r - 20, y + 50, 9, 4, YELLOW)
    reg("texto", "titulo", col_cx - UL_W // 2, y, col_cx + UL_W // 2, UL_Y + 6)
    y = UL_Y + 32

    def phrase_zone(y1, frase, label, is_no):
        y2 = y1 + 240
        xl, xr = col_l, col_r   # NO DIGAS y DI comparten margen y ancho: sin escalón
        rr(d, [xl, y1, xr, y2], 14, fill=WHITE, outline=GRAY_L if is_no else YELLOW, width=1 if is_no else 2)
        reg("zona" if avatar is not None else "card", "zona-no-digas" if is_no else "zona-di", xl, y1, xr, y2)
        cx = (xl + xr) // 2
        if is_no:
            d.ellipse([xl + 16, y1 + 16, xl + 60, y1 + 60], fill=RED_C)
            xmark(d, xl + 38, y1 + 38, 10, WHITE, 3)
            fLBL = F(WSB, 18)
            rr(d, [xl + 72, y1 + 18, xl + 72 + tw(d, label, fLBL) + 20, y1 + 52], 8, fill=RED_C)
            d.text((xl + 82, y1 + 22), label, font=fLBL, fill=WHITE)
        else:
            d.ellipse([xl + 16, y1 + 16, xl + 60, y1 + 60], fill=GREEN_C)
            check(d, xl + 38, y1 + 38, 12, WHITE, 3)
            fDIL = F(WSB, 22)
            rr(d, [xl + 72, y1 + 16, xl + 72 + tw(d, label, fDIL) + 20, y1 + 54], 8, fill=NAVY, outline=YELLOW, width=2)
            d.text((xl + 82, y1 + 20), label, font=fDIL, fill=YELLOW)
        lines = frase if isinstance(frase, list) else wrap(d, frase, F(BS, 74), xr - xl - 60)
        size = 74
        while any(tw(d, l, F(BS, size)) > xr - xl - 60 for l in lines) and size > 36:
            size -= 2
        f = F(BS, size)
        pitch = th(d, "HI", f) + 22
        for i, ln in enumerate(lines[:2]):
            ttext(d, cx, y1 + 72 + i * pitch, ln, f, NAVY)
        return y2, xl, xr

    ND_Y1 = y
    ND_Y2, xl, xr = phrase_zone(ND_Y1, c["frase_mal"], "NO DIGAS:", True)
    TACH_Y = ND_Y2 - 18
    d.line([(xl + 16, TACH_Y), (xr - 16, TACH_Y)], fill=RED_C, width=4)
    xmark(d, (xl + xr) // 2, TACH_Y, 8, RED_C, 3)
    y = ND_Y2 + 16

    ARR_CX = col_cx
    d.line([(ARR_CX, y), (ARR_CX, y + 40)], fill=YELLOW, width=5)
    d.polygon([(ARR_CX, y + 56), (ARR_CX - 14, y + 40), (ARR_CX + 14, y + 40)], fill=YELLOW)
    y += 64

    DI_Y1 = y
    DI_Y2, _, _ = phrase_zone(DI_Y1, c["frase_bien"], "DI:", False)
    d.rectangle([xl + 16, DI_Y2 - 14, xr - 16, DI_Y2 - 8], fill=YELLOW)

    if avatar is not None:
        w2, h2 = avatar_size(avatar, av_w, min(av_h, DI_Y2 - 108))
        paste_avatar(img, avatar, w2, h2, DI_Y2)
        av_rect = (W - w2 + 18, DI_Y2 - h2, W, DI_Y2)
    else:
        av_rect = None
    y = DI_Y2 + 28

    # EJEMPLOS comparativos
    y = examples_header(d, y)
    fENB = F(WSB, 17)
    ex = c["ejemplos"]
    COL = W // 2 + 4
    TABLE_H = len(ex) * 110 + 20
    rr(d, [P, y, W - P, y + TABLE_H], 10, fill=WHITE, outline=GRAY_L, width=1)
    reg("card", "ejemplos", P, y - 52, W - P, y + TABLE_H)
    d.line([(COL, y + 8), (COL, y + TABLE_H - 8)], fill=GRAY_L, width=1)
    ry = y + 16
    for i, (mal, bien) in enumerate(ex):
        d.ellipse([P + 16, ry + 4, P + 40, ry + 28], fill=RED_C)
        xmark(d, P + 28, ry + 16, 6, WHITE, 2)
        for j, ln in enumerate(wrap(d, mal, fENB, COL - P - 70)):
            d.text((P + 50, ry + j * 20), ln, font=fENB, fill=RED_C)
        d.ellipse([COL + 16, ry + 4, COL + 40, ry + 28], fill=GREEN_C)
        check(d, COL + 28, ry + 16, 8, WHITE, 2)
        for j, ln in enumerate(wrap(d, bien, fENB, W - P - COL - 70)):
            d.text((COL + 50, ry + j * 20), ln, font=fENB, fill=GREEN_C)
        ry += 110
        if i < len(ex) - 1:
            d.line([(P + 8, ry - 8), (W - P - 8, ry - 8)], fill=GRAY_L, width=1)
    y += TABLE_H + 20

    y = tip_block(d, y, c["tip"], step=26, base_h=190)
    l1, l2 = pick_cta("no-digas", c.get("tema", " ".join(c["frase_bien"]) if isinstance(c["frase_bien"], list) else c["frase_bien"]),
                      "falsos_cognados" if c.get("falso_cognado") else c.get("cta_categoria"), c.get("cta"))
    y = cta_block(d, y, l1, l2)
    if y > H - 110:
        raise SystemExit(f"El contenido no cabe (termina en y={y}). Acorta el texto o reduce ejemplos.")
    check_layout(av_rect)
    footer(d, y)
    return img


# ═══════════════════ B-ROLL OVERLAY ═══════════════════
def broll(c, avatar=None):
    _BLOCKS.clear()
    """Reconstruido a partir de la lista de zonas de mmercedes-broll-overlay.
    No lleva avatar (regla: el B-roll de ambiente no incluye avatar de recorte)."""
    nivel = nivel_key(c)
    img = Image.new("RGB", (W, H), CREAM)
    d = ImageDraw.Draw(img)
    serie = c.get("serie", "Real English")
    if serie not in ("Real English", "Common Mistakes"):
        raise SystemExit("serie debe ser 'Real English' o 'Common Mistakes'")
    header(d, nivel, serie)

    y = 124
    ctext(d, W // 2, y, c["hook"], F(LORA, 30), NAVY)
    y += 56

    fBB = fit(d, c["expresion"], BS, 96, W - 2 * P - 120)
    bh = th(d, c["expresion"], fBB) + 56
    rr(d, [P, y, W - P, y + bh], 18, fill=NAVY)
    reg("card", "expresion", P, y, W - P, y + bh)
    ttext(d, W // 2, y + 22, c["expresion"], fBB, YELLOW)
    d.rectangle([W // 2 - 170, y + bh - 20, W // 2 + 170, y + bh - 14], fill=YELLOW)
    star(d, P + 24, y + bh // 2, 10, 4, YELLOW)
    star(d, W - P - 24, y + bh // 2, 10, 4, YELLOW)
    y += bh + 24

    RZ1 = y
    RZ_H = 250
    d.rectangle([0, RZ1, W, RZ1 + RZ_H], fill=NAVY)
    fR = F(WSB, 30)
    for k, (txt, ok) in enumerate(((c["reveal_no"], False), (c["reveal_si"], True))):
        ry = RZ1 + 34 + k * 84
        d.ellipse([P + 6, ry, P + 56, ry + 50], fill=GREEN_C if ok else RED_C)
        (check(d, P + 31, ry + 25, 16, WHITE, 3) if ok else xmark(d, P + 31, ry + 25, 11, WHITE, 3))
        f = fit(d, txt, WSB, 30, W - 2 * P - 90)
        d.text((P + 76, ry + 6), txt, font=f, fill=WHITE if not ok else YELLOW)
    ctext(d, W // 2, RZ1 + RZ_H - 48, c["subtitulo"], fit(d, c["subtitulo"], LORA, 24, W - 2 * P), WHITE)
    d.rectangle([0, RZ1 + RZ_H, W, RZ1 + RZ_H + 8], fill=YELLOW)
    y = RZ1 + RZ_H + 28

    y = examples_header(d, y)
    fEN, fES = F(WSB, 19), F(WSR, 18)
    COL = W // 2 + 4
    rows = c["ejemplos"]
    TABLE_H = len(rows) * 84 + 10
    rr(d, [P, y, W - P, y + TABLE_H], 10, fill=WHITE, outline=GRAY_L, width=1)
    reg("card", "ejemplos", P, y - 52, W - P, y + TABLE_H)
    d.line([(COL, y + 6), (COL, y + TABLE_H - 6)], fill=GRAY_L, width=1)
    ry = y + 14
    for i, (en, es) in enumerate(rows):
        pair_text(d, P + 16, ry, wrap(d, en, fEN, COL - P - 32), fEN, NAVY, 24)
        pair_text(d, COL + 16, ry, wrap(d, es, fES, W - P - COL - 32), fES, NAVY, 24)
        ry += 84
        if i < len(rows) - 1:
            d.line([(P + 8, ry - 10), (W - P - 8, ry - 10)], fill=GRAY_L, width=1)
    y += TABLE_H + 20

    y = tip_block(d, y, c["tip"], step=24, base_h=120)
    l1, l2 = pick_cta("broll", c.get("tema", c["expresion"]), c.get("cta_categoria"), c.get("cta"))
    y = cta_block(d, y, l1, l2)
    if y > H - 110:
        raise SystemExit(f"El contenido no cabe (termina en y={y}).")
    check_layout(None)
    footer(d, y)
    return img


SERIES = {"como-se-dice": como_se_dice, "no-digas": no_digas, "broll": broll}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("serie", choices=SERIES)
    ap.add_argument("contenido", help="archivo JSON con el contenido de la pieza")
    ap.add_argument("--out", default="outputs", help="carpeta de salida (se crea si no existe)")
    ap.add_argument("--avatar", help="PNG del avatar master con fondo transparente")
    ap.add_argument("--sin-avatar", action="store_true", help="ignora MM_AVATAR y el avatar por defecto")
    a = ap.parse_args(argv)

    content = json.loads(Path(a.contenido).read_text(encoding="utf-8"))
    avatar = None if (a.sin_avatar or a.serie == "broll") else load_avatar(a.avatar)
    img = SERIES[a.serie](content, avatar)
    out = Path(a.out)
    out.mkdir(parents=True, exist_ok=True)
    name = content.get("salida") or f"{a.serie.replace('-', '_')}_post.png"
    dest = out / name
    img.save(dest, dpi=(300, 300))
    print(f"listo: {dest}  ({img.width}x{img.height})  avatar={'sí' if avatar is not None else 'no'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
