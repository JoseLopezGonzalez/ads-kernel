#!/usr/bin/env bash
# Crea el esqueleto de un proyecto nuevo con la misma organización (K0.14).
#
#   new-project.sh <nombre> [pack1,pack2,...]
#
# Los packs son DIRECTORIOS de packs/ que contienen un PACK.md. Los de la línea 1.3.0
# viven en packs/legacy-1.3.0/ y NO son instalables: se conservan sólo para trazabilidad.
set -euo pipefail

SRC="$(cd "$(dirname "$0")/.." && pwd)"

packs_disponibles() {
  # un pack instalable = directorio de packs/ con PACK.md, excluidos los legacy-*
  find "$SRC/packs" -mindepth 2 -maxdepth 2 -name PACK.md -print 2>/dev/null \
    | sed "s|^$SRC/packs/||; s|/PACK.md$||" \
    | grep -v '^legacy-' \
    | sort
}

uso() {
  echo "uso: new-project.sh <nombre> [pack1,pack2,...]" >&2
  echo >&2
  echo "packs instalables:" >&2
  packs_disponibles | sed 's/^/  /' >&2
  echo >&2
  echo "  (sin packs, el PROFILE deberá cubrir el saber hacer de la clase de proyecto)" >&2
}

NAME="${1:-}"
if [ -z "$NAME" ]; then uso; exit 2; fi
PACKS="${2:-}"
DST="$(cd "$(dirname "$SRC")" && pwd)/$NAME"

# ---------------------------------------------------------------------------
# 1. VALIDAR ANTES DE CREAR NADA
#    Un identificador equivocado no puede dejar a medias un proyecto.
# ---------------------------------------------------------------------------
if [ -e "$DST" ]; then echo "Ya existe $DST" >&2; exit 1; fi

LISTA=()
if [ -n "$PACKS" ]; then
  IFS=',' read -ra LISTA <<< "$PACKS"
  for p in "${LISTA[@]}"; do
    if [ ! -f "$SRC/packs/$p/PACK.md" ]; then
      echo "Pack no instalable: '$p'" >&2
      if [ -d "$SRC/packs/legacy-1.3.0/$p" ] || [ -f "$SRC/packs/legacy-1.3.0/$p.md" ]; then
        echo "  '$p' pertenece a la línea 1.3.0 y está retirado en packs/legacy-1.3.0/." >&2
        echo "  No se instala. Elige uno de los vigentes." >&2
      fi
      echo >&2
      echo "packs instalables:" >&2
      packs_disponibles | sed 's/^/  /' >&2
      exit 3
    fi
  done
fi

# ---------------------------------------------------------------------------
# 2. CREAR
# ---------------------------------------------------------------------------
mkdir -p "$DST"/{kernel,packs,docs/agentic,docs/rediseno,tooling}

# La ESPECIFICACIÓN NORMATIVA viaja con el kernel: el corpus operativo la enlaza, y sin
# ella un proyecto instalado tiene enlaces rotos y no es conforme.
# Se envía la ESPECIFICACIÓN, no la historia: (a), (b), sus enmiendas y el registro de
# decisiones, que son lo que el corpus operativo enlaza. Las auditorías y sus correcciones
# son historia del repositorio del kernel y viven allí.
for n in a-CAPACIDADES-APROBADA.md b-RECORRIDO-APROBADA.md a-ENMIENDA-E1-ENC.md \
         DECISIONES-Y-CONTRADICCIONES.md; do
  cp "$SRC/docs/rediseno/$n" "$DST/docs/rediseno/"
done
cp "$SRC/kernel/"*.md "$SRC/kernel/VERSION" "$DST/kernel/"
cp -r "$SRC/kernel/templates" "$DST/kernel/"
cp -r "$SRC/kernel/operativo" "$DST/kernel/"
find "$DST/kernel/operativo" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
cp "$SRC/kernel/PROFILE_TEMPLATE.md" "$DST/PROFILE.md"
cp "$SRC/kernel/PROJECT_TEMPLATE.md" "$DST/PROJECT.md"
cp "$SRC/kernel/BOOTSTRAP_PROMPT.md" "$DST/BOOTSTRAP_PROMPT.md"
cp "$SRC/START_HERE.md" "$DST/START_HERE.md"
cp "$SRC"/tooling/*.sh "$DST/tooling/"

if [ ${#LISTA[@]} -gt 0 ]; then
  cp "$SRC/packs/00-QUE-ES-UN-PACK.md" "$SRC/packs/COMPOSICION.md" "$DST/packs/"
  for p in "${LISTA[@]}"; do
    cp -r "$SRC/packs/$p" "$DST/packs/"; echo "  pack añadido: $p"
  done
else
  echo "  sin packs — el PROFILE deberá cubrir el saber hacer de la clase de proyecto"
fi

echo "# UPSTREAM — candidatos a KERNEL o PACK (K0.12)" > "$DST/docs/UPSTREAM.md"
echo "# JOURNAL" > "$DST/docs/JOURNAL.md"
cp "$SRC/kernel/templates/PROJECT_LEARNINGS.md" "$DST/docs/"
cp "$SRC/kernel/templates/ORG_LEARNINGS.md" "$DST/docs/agentic/"
sed -i "s/<nombre>/$NAME/" "$DST/PROJECT.md" 2>/dev/null || true

# la huella de integridad se recalcula para la copia: es SU referencia, no la nuestra
rm -f "$DST/kernel/.upstream-hash"
( cd "$DST" && ./tooling/kernel-status.sh >/dev/null 2>&1 || true )

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
