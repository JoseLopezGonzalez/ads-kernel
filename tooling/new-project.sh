#!/usr/bin/env bash
# Crea un ADS Project nuevo: un WORKSPACE de producto con su repositorio ADS de control.
#
#   new-project.sh <nombre> [pack1,pack2,...] [--en <directorio>]
#
# Un ADS Project gobierna un PRODUCTO, no un repositorio. Por eso lo que se crea es:
#
#   <nombre>/          el WORKSPACE. NO es un repositorio Git. Es el contenedor.
#   └── ads/           el repositorio de CONTROL. Es el único que se inicializa.
#
# Los repositorios técnicos —frontend, backend, móvil— NO se crean aquí. Se declaran
# después en ads/SOURCES.toml y se materializan como hermanos de ads/ con:
#
#   python3 tooling/workspace.py init
#
# Contrato: kernel/operativo/contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md
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
  echo "uso: new-project.sh <nombre> [pack1,pack2,...] [--en <directorio>]" >&2
  echo >&2
  echo "packs instalables:" >&2
  packs_disponibles | sed 's/^/  /' >&2
  echo >&2
  echo "  (sin packs, el PROFILE deberá cubrir el saber hacer de la clase de proyecto)" >&2
  echo "  --en  dónde crear el workspace. Por defecto, junto a este repositorio." >&2
}

NAME=""
PACKS=""
DONDE=""
while [ $# -gt 0 ]; do
  case "$1" in
    --en) DONDE="${2:-}"; shift 2 || { uso; exit 2; } ;;
    -h|--help) uso; exit 0 ;;
    *)
      if [ -z "$NAME" ]; then NAME="$1"
      elif [ -z "$PACKS" ]; then PACKS="$1"
      else echo "argumento inesperado: '$1'" >&2; uso; exit 2
      fi
      shift ;;
  esac
done

if [ -z "$NAME" ]; then uso; exit 2; fi

BASE="${DONDE:-$(cd "$(dirname "$SRC")" && pwd)}"
WORKSPACE="$BASE/$NAME"
ADS="$WORKSPACE/ads"

# Una sola variable para la rama que se CREA y la que se DOCUMENTA. Escribirlas dos veces
# es lo que permitió que divergieran.
RAMA_INICIAL="main"

# ---------------------------------------------------------------------------
# 1. VALIDAR ANTES DE CREAR NADA
#    Un identificador equivocado no puede dejar a medias un workspace.
# ---------------------------------------------------------------------------
if [ -e "$WORKSPACE" ]; then echo "Ya existe $WORKSPACE" >&2; exit 1; fi

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
# 2. CREAR EL WORKSPACE Y, DENTRO, EL REPOSITORIO DE CONTROL
#    El workspace es un directorio corriente. NO se inicializa Git en él: si lo
#    fuera, los repositorios técnicos quedarían anidados dentro de otro repositorio
#    y su historia dejaría de ser independiente.
# ---------------------------------------------------------------------------
mkdir -p "$ADS"/{kernel,packs,docs/agentic,docs/rediseno,tooling}

# La ESPECIFICACIÓN NORMATIVA viaja con el kernel: el corpus operativo la enlaza, y sin
# ella un proyecto instalado tiene enlaces rotos y no es conforme.
# Se envía la ESPECIFICACIÓN, no la historia: (a), (b), sus enmiendas y el registro de
# decisiones, que son lo que el corpus operativo enlaza. Las auditorías y sus correcciones
# son historia del repositorio del kernel y viven allí.
for n in a-CAPACIDADES-APROBADA.md b-RECORRIDO-APROBADA.md a-ENMIENDA-E1-ENC.md \
         a-ENMIENDA-E2-MULTIREPO.md DECISIONES-Y-CONTRADICCIONES.md; do
  cp "$SRC/docs/rediseno/$n" "$ADS/docs/rediseno/"
done
cp "$SRC/kernel/"*.md "$SRC/kernel/VERSION" "$ADS/kernel/"
cp -r "$SRC/kernel/templates" "$ADS/kernel/"
cp -r "$SRC/kernel/operativo" "$ADS/kernel/"
find "$ADS/kernel/operativo" -name '__pycache__' -type d -prune -exec rm -rf {} + 2>/dev/null || true
cp "$SRC/kernel/PROFILE_TEMPLATE.md" "$ADS/PROFILE.md"
cp "$SRC/kernel/PROJECT_TEMPLATE.md" "$ADS/PROJECT.md"
cp "$SRC/kernel/BOOTSTRAP_PROMPT.md" "$ADS/BOOTSTRAP_PROMPT.md"
cp "$SRC/START_HERE.md" "$ADS/START_HERE.md"
cp "$SRC"/tooling/*.sh "$SRC"/tooling/*.py "$ADS/tooling/"
mkdir -p "$ADS/tooling/tests" && cp "$SRC"/tooling/tests/*.py "$ADS/tooling/tests/"

# 3. LA COMPOSICIÓN DEL PRODUCTO
#    Se instala SIN fuentes. Es válido y es lo correcto: un producto nuevo todavía no
#    tiene código, y el Circuito 0 decidirá su arquitectura física.
cp "$SRC/kernel/operativo/plantillas/SOURCES.toml" "$ADS/SOURCES.toml"

if [ ${#LISTA[@]} -gt 0 ]; then
  cp "$SRC/packs/00-QUE-ES-UN-PACK.md" "$SRC/packs/COMPOSICION.md" "$ADS/packs/"
  for p in "${LISTA[@]}"; do
    cp -r "$SRC/packs/$p" "$ADS/packs/"; echo "  pack añadido: $p"
  done
else
  echo "  sin packs — el PROFILE deberá cubrir el saber hacer de la clase de proyecto"
fi

echo "# UPSTREAM — candidatos a KERNEL o PACK (K0.12)" > "$ADS/docs/UPSTREAM.md"
echo "# JOURNAL" > "$ADS/docs/JOURNAL.md"
cp "$SRC/kernel/templates/PROJECT_LEARNINGS.md" "$ADS/docs/"
cp "$SRC/kernel/templates/ORG_LEARNINGS.md" "$ADS/docs/agentic/"
sed -i "s/<nombre>/$NAME/" "$ADS/PROJECT.md" 2>/dev/null || true

# la huella de integridad se recalcula para la copia: es SU referencia, no la nuestra
rm -f "$ADS/kernel/.upstream-hash"
( cd "$ADS" && ./tooling/kernel-status.sh >/dev/null 2>&1 || true )

# ---------------------------------------------------------------------------
# 4. GIT, SÓLO EN EL REPOSITORIO DE CONTROL
# ---------------------------------------------------------------------------
# La rama inicial se fija EXPLÍCITAMENTE. `git init` sin más toma su nombre de
# `init.defaultBranch`, que con una configuración global vacía —o antigua— es `master`,
# y el comando que este mismo script documenta abajo es `git push -u origin main`.
# Se documentaba una rama y se creaba otra.
#   · git >= 2.28 acepta `-b`
#   · por debajo, `symbolic-ref` sobre un repositorio recién creado y sin commits hace
#     exactamente lo mismo y no depende de ninguna versión
( cd "$ADS" && { git init -q -b "$RAMA_INICIAL" 2>/dev/null \
                 || { git init -q && git symbolic-ref HEAD "refs/heads/$RAMA_INICIAL"; }; } \
  && git add -A
  if git -c advice.detachedHead=false commit -qm "chore: semilla ADS (kernel $(cat kernel/VERSION))" 2>/dev/null; then
    echo "  commit inicial hecho en ads/"
  else
    echo "  AVISO: git init hecho pero sin commit (identidad de git no configurada)."
    echo "         Configura user.name/user.email y haz el primer commit a mano."
  fi )

cat <<EOF

Proyecto '$NAME' creado  (kernel $(cat "$SRC/kernel/VERSION"))

  workspace          $WORKSPACE
                     no es un repositorio Git: es el contenedor del producto

  control repo ADS   $ADS
                     el único repositorio que ADS ha inicializado, en la rama $RAMA_INICIAL

Siguiente:
  1. cd $ADS && git remote add origin <repo-ADS-del-producto> && git push -u origin $RAMA_INICIAL
  2. Rellenar PROFILE.md  — a mano, o por conversación (ver START_HERE.md paso 5)
  3. Completar PROJECT.md
  4. Declarar los repositorios técnicos en SOURCES.toml, y materializarlos:
         python3 tooling/workspace.py check
         python3 tooling/workspace.py init
  5. Pegar BOOTSTRAP_PROMPT.md en tu agente principal

Los repositorios de código NO se crean aquí: se declaran en SOURCES.toml y aparecen
como hermanos de ads/ dentro del workspace.

Lee START_HERE.md si es la primera vez.
EOF
