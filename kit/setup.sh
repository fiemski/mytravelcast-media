#!/bin/bash
# Przygotowanie świeżego kontenera: fonty Inter, biblioteki dla zrzutów mapy mytravelcast.
set -e
K="$(cd "$(dirname "$0")" && pwd)"
F=/usr/share/fonts/opentype/inter
if [ ! -f $F/InterDisplay-Black.otf ]; then mkdir -p $F && cp "$K"/fonts/*.otf $F/ && fc-cache -f >/dev/null 2>&1 || true; fi
python3 -c "import playwright, PIL" 2>/dev/null || pip install --break-system-packages -q playwright pillow
V="$K/vendor"; mkdir -p "$V"; cd "$V"
get(){ spec=$1; dir=$2; if [ ! -d "$dir/package" ]; then mkdir -p "$dir"; npm pack "$spec" --silent --pack-destination "$dir" >/dev/null; tar -xzf "$dir"/*.tgz -C "$dir"; fi; }
get d3@7.8.5 d3-7.8.5
get @fontsource/dm-sans@5.3.0 fontsource-dm-sans-5.3.0
get @fontsource/dm-mono@5.3.0 fontsource-dm-mono-5.3.0
echo "kit gotowy: $K"
