#!/usr/bin/env python3
"""Agrega transiciones entre diapositivas de un .pptx.

Uso: python add_transitions.py entrada.pptx salida.pptx "2:fade,5:wipe,7:push,11:fade-slow"

Cada par es <número de diapositiva>:<efecto>. Efectos: fade, wipe, push, cover, split.
Con el sufijo -slow la transición es lenta. La diapositiva 1 no necesita transición.
pptxgenjs no escribe transiciones, así que se insertan en el XML de cada diapositiva.
En el XML, <p:transition> va justo después de </p:clrMapOvr> y antes de <p:timing>.
"""
import re
import sys
import zipfile

EFFECTS = {
    "fade": "<p:fade/>",
    "wipe": '<p:wipe dir="l"/>',
    "push": '<p:push dir="l"/>',
    "cover": '<p:cover dir="l"/>',
    "split": '<p:split orient="horz" dir="out"/>',
}


def main(src, dst, spec):
    plan = {}
    for pair in spec.split(","):
        num, eff = pair.split(":")
        slow = eff.endswith("-slow")
        eff = eff.replace("-slow", "")
        if eff not in EFFECTS:
            sys.exit("Efecto desconocido: " + eff)
        plan[int(num)] = (EFFECTS[eff], "slow" if slow else "med")
    zin = zipfile.ZipFile(src)
    zout = zipfile.ZipFile(dst, "w", zipfile.ZIP_DEFLATED)
    for item in zin.infolist():
        data = zin.read(item.filename)
        m = re.fullmatch(r"ppt/slides/slide(\d+)\.xml", item.filename)
        if m and int(m.group(1)) in plan:
            xml = data.decode("utf-8")
            if "<p:transition" in xml:
                sys.exit("La diapositiva %s ya tiene transición" % m.group(1))
            if "</p:clrMapOvr>" not in xml:
                sys.exit("Falta clrMapOvr en la diapositiva %s" % m.group(1))
            eff, spd = plan[int(m.group(1))]
            xml = xml.replace(
                "</p:clrMapOvr>",
                '</p:clrMapOvr><p:transition spd="%s">%s</p:transition>' % (spd, eff),
                1,
            )
            data = xml.encode("utf-8")
        zout.writestr(item, data)
    zout.close()
    print("Transiciones agregadas a", len(plan), "diapositivas")


if __name__ == "__main__":
    if len(sys.argv) != 4:
        sys.exit(__doc__)
    main(*sys.argv[1:])
