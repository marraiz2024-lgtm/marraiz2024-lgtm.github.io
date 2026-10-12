#!/usr/bin/env python3
"""Empaqueta las skills de MMercedesEnglish en zips (uno por skill) y un paquete unico con
manifiesto de huellas SHA-256, para registrarlas y compararlas por contenido.

Uso: python3 empaquetar_skills.py SALIDA [--con-avatar RUTA_PNG]
  SALIDA            carpeta donde se escriben los zips y MANIFIESTO.md
  --con-avatar PNG  crea ademas un zip de mmercedes-generador-posts con ese avatar dentro
La foto del avatar nunca se incluye en el paquete general.
"""
import glob, hashlib, os, sys, zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
_c = [os.environ.get("MM_SYNCED")] + glob.glob(os.path.expanduser("~/.claude/skills/synced/*/"))
SYN = next((Path(c) for c in _c if c and Path(c).is_dir()), None)

GRUPOS = [
    ("NUEVA", REPO, ["mmercedes-cadena", "mmercedes-ficha", "mmercedes-video-ia", "mmercedes-qa", "mmercedes-publicar", "mmercedes-medir"]),
    ("REESCRITA", REPO, ["mmercedes-generador-posts", "mmercedes-broll-overlay", "mmercedes-brand", "mmercedes-prompt-animacion", "mmercedes-revisor"]),
    ("VERSION DE LA CUENTA (10 y 11 oct)", REPO, ["mmercedes-colores", "mmercedes-prompt-ia"]),
    ("SIN CAMBIOS", SYN, ["mmercedes-broll-texto", "mmercedes-irregular-verbs", "mmercedes-mechita", "mmercedes-evaluador-slides", "edicion-microclase-pptx-interactiva"]),
]


def archivos(root, s):
    return [f for f in sorted((root / s).rglob("*"))
            if f.is_file() and "__pycache__" not in f.parts and not (f.suffix == ".png" and "avatar" in f.parts)]


def main():
    if len(sys.argv) < 2:
        sys.exit(__doc__)
    out = Path(sys.argv[1]); out.mkdir(parents=True, exist_ok=True)
    avatar = sys.argv[sys.argv.index("--con-avatar") + 1] if "--con-avatar" in sys.argv else None
    filas, huellas = [], []
    for tipo, root, lista in GRUPOS:
        if root is None:
            print("Aviso: no encuentro las skills de la cuenta (defina MM_SYNCED). Se omite:", tipo); continue
        for s in lista:
            if not (root / s / "SKILL.md").exists():
                print("Aviso: falta", s); continue
            z = out / f"{s}.zip"
            fs = archivos(root, s)
            with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
                for f in fs: zf.write(f, Path(s) / f.relative_to(root / s))
            filas.append((tipo, s, len(fs), z.stat().st_size // 1024))
            huellas += [(s, str(f.relative_to(root / s)), hashlib.sha256(f.read_bytes()).hexdigest()) for f in fs]
    if avatar:
        z = out / "mmercedes-generador-posts-CON-AVATAR.zip"
        with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
            for f in archivos(REPO, "mmercedes-generador-posts"):
                zf.write(f, Path("mmercedes-generador-posts") / f.relative_to(REPO / "mmercedes-generador-posts"))
            zf.write(avatar, "mmercedes-generador-posts/assets/avatar/" + Path(avatar).name)
    bt = "`"
    c = lambda x: bt + x + bt
    m = ["# Manifiesto de registro: cadena de skills de MMercedesEnglish\n",
         "Cada skill es un zip con su carpeta completa en la raíz. Un archivo .skill es el mismo zip con otra extensión.\n",
         "| Tipo | Skill | Archivos | KB (zip) |", "|---|---|---|---|"]
    m += [f"| {t} | {c(s)} | {n} | {k} |" for t, s, n, k in filas]
    m += ["\n## Notas\n",
          "1. Compara por contenido (huellas SHA-256) antes de copiar y no pises la versión de la cuenta sin aprobación de Mercedes.",
          f"2. {c('mmercedes-colores')} y {c('mmercedes-prompt-ia')} son la versión de la cuenta de Mercedes del 10 y 11 de octubre. No las sustituyas por versiones anteriores.",
          f"3. La foto del avatar no viaja en el paquete general. {c('mmercedes-generador-posts-CON-AVATAR.zip')} la incluye, si se generó.",
          f"4. Decisiones: {c('mmercedes-cadena/references/conflictos.md')}. Documentación: {c('mmercedes-cadena/references/DOCUMENTACION_CADENA_MMERCEDESENGLISH.md')}.",
          "\n## Huellas SHA-256\n", "| Skill | Archivo | SHA-256 |", "|---|---|---|"]
    m += [f"| {c(s)} | {c(f)} | {c(h)} |" for s, f, h in huellas]
    (out / "MANIFIESTO.md").write_text("\n".join(m) + "\n", encoding="utf-8")
    paquete = out.parent / (out.name + ".zip")
    with zipfile.ZipFile(paquete, "w", zipfile.ZIP_DEFLATED) as zf:
        for f in sorted(out.iterdir()):
            if "CON-AVATAR" in f.name: continue
            zf.write(f, Path(out.name) / f.name)
    print(f"{len(filas)} skills, {len(huellas)} archivos con huella. Paquete: {paquete} ({paquete.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    main()
