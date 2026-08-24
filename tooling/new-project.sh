#!/usr/bin/env bash
# Crea el esqueleto de un proyecto nuevo con la misma organización (K0.14).
# uso: new-project.sh <nombre> [pack1,pack2]
set -euo pipefail
NAME="${1:?uso: new-project.sh <nombre> [pack1,pack2]}"
PACKS="${2:-}"
SRC="$(cd "$(dirname "$0")/.." && pwd)"
DST="../$NAME"
[ -e "$DST" ] && { echo "Ya existe $DST"; exit 1; }

mkdir -p "$DST"/{kernel,packs,docs/agentic,tooling}
cp "$SRC/kernel/"*.md "$SRC/kernel/VERSION" "$DST/kernel/"
cp -r "$SRC/kernel/templates" "$DST/kernel/"
cp "$SRC/kernel/PROFILE_TEMPLATE.md" "$DST/PROFILE.md"
cp "$SRC/kernel/PROJECT_TEMPLATE.md" "$DST/PROJECT.md"
cp "$SRC/kernel/BOOTSTRAP_PROMPT.md" "$DST/BOOTSTRAP_PROMPT.md"
cp "$SRC/START_HERE.md" "$DST/START_HERE.md"
cp "$SRC"/tooling/*.sh "$DST/tooling/"

if [ -n "$PACKS" ]; then
  IFS=',' read -ra P <<< "$PACKS"
  for p in "${P[@]}"; do
    [ -f "$SRC/packs/$p.md" ] || { echo "Pack no encontrado: $p"; exit 1; }
    cp "$SRC/packs/$p.md" "$DST/packs/"; echo "  pack añadido: $p"
  done
else
  echo "  sin packs — el PROFILE deberá cubrir el saber hacer de la clase de proyecto"
fi

echo "# UPSTREAM — candidatos a KERNEL o PACK (K0.12)" > "$DST/docs/UPSTREAM.md"
echo "# JOURNAL" > "$DST/docs/JOURNAL.md"
cp "$SRC/kernel/templates/PROJECT_LEARNINGS.md" "$DST/docs/"
cp "$SRC/kernel/templates/ORG_LEARNINGS.md" "$DST/docs/agentic/"
sed -i "s/<nombre>/$NAME/" "$DST/PROJECT.md" 2>/dev/null || true
( cd "$DST" && git init -q && git add -A
  if git -c advice.detachedHead=false commit -qm "chore: semilla ADS (kernel $(cat kernel/VERSION))" 2>/dev/null; then
    echo "  commit inicial hecho"
  else
    echo "  AVISO: git init hecho pero sin commit (identidad de git no configurada)."
    echo "         Configura user.name/user.email y haz el primer commit a mano."
  fi )

cat <<EOF

Proyecto '$NAME' creado en $DST  (kernel $(cat "$SRC/kernel/VERSION"))

Siguiente:
  1. cd $DST && git remote add origin <tu-repo> && git push -u origin main
  2. Rellenar PROFILE.md  — a mano, o por conversación (ver START_HERE.md paso 3)
  3. Completar PROJECT.md
  4. Pegar BOOTSTRAP_PROMPT.md en tu agente principal

Lee START_HERE.md si es la primera vez.
EOF
