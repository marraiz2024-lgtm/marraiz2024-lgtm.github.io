#!/usr/bin/env bash
# Limpieza suave de las grabaciones de la docente.
# Uso: limpiar_audio.sh <carpeta_con_webm_crudos> <carpeta_destino>
# Requiere ffmpeg. Recorta 0,08 s de clic inicial, deja 0,2 a 0,25 s de margen,
# baja el ruido ligeramente e iguala el volumen. Si un archivo no tiene pausas
# detectables, usa un recorte fijo (silenceremove se cuelga sin pausas).
set -u
src="$1"; dst="$2"; mkdir -p "$dst"
for f in "$src"/*.webm; do
  k=$(basename "$f" .webm)
  d=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$f")
  if ! timeout 40 ffmpeg -nostdin -v error -y -i "$f" -ss 0.08 \
    -af "highpass=f=70,afftdn=nr=6:nf=-45,silenceremove=start_periods=1:start_threshold=-58dB:start_silence=0.2,areverse,silenceremove=start_periods=1:start_threshold=-58dB:start_silence=0.25,areverse,loudnorm=I=-18:TP=-2" \
    -c:a libopus -b:a 56k "$dst/$k.webm"; then
    echo "recorte fijo: $k"
    timeout 60 ffmpeg -nostdin -v error -y -i "$f" -ss 0.1 -t "$(python3 -c "print(max(0.5,$d-0.3))")" \
      -af "highpass=f=70,afftdn=nr=6:nf=-45,loudnorm=I=-18:TP=-2" -c:a libopus -b:a 56k "$dst/$k.webm"
  fi
done
python3 - "$dst" <<'PY'
import json,os,sys
d=sys.argv[1]
m={f[:-5]:f for f in sorted(os.listdir(d)) if f.endswith('.webm')}
json.dump(m,open(os.path.join(d,'manifest.json'),'w'),indent=1)
print(len(m),'archivos y manifest.json en',d)
PY
