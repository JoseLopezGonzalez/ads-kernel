#!/usr/bin/env bash
# Comprueba si la copia vendorizada del kernel ha sido modificada localmente (K0.11).
#
# La HUELLA la define un solo sitio: kernel/operativo/validadores/huella.py. Este script
# no la recalcula por su cuenta a propósito: dos implementaciones del mismo hash derivan, y
# la que miente acaba siendo la que nadie mira.
set -euo pipefail
cd "$(dirname "$0")/.."

KV=$(cat kernel/VERSION)
HUELLA="kernel/operativo/validadores/huella.py"

if [ ! -f "$HUELLA" ]; then
  echo "kernel version : $KV"
  echo "estado         : NO COMPROBABLE — falta $HUELLA" >&2
  exit 2
fi

SUM=$(python3 "$HUELLA")
N=$(python3 "$HUELLA" --listar | tail -1)

echo "kernel version : $KV"
echo "huella local   : $SUM   ($N: kernel/, packs/ y tooling/ — .md .yaml .py .sh)"

if [ -f kernel/.upstream-hash ]; then
  UP=$(cat kernel/.upstream-hash)
  if [ "$SUM" = "$UP" ]; then
    echo "estado         : LIMPIO (coincide con el release)"
  else
    echo "estado         : DIVERGENTE — el kernel ha sido editado localmente."
    echo "                 K0.11: no se edita el kernel vendorizado."
    echo "                 Usa un override declarado en PROFILE.md §9,"
    echo "                 o promueve el cambio upstream (K0.12)."
    echo "                 Para ver qué entra en la huella: python3 $HUELLA --listar"
    exit 1
  fi
else
  echo "$SUM" > kernel/.upstream-hash
  echo "estado         : hash de referencia anotado"
fi
