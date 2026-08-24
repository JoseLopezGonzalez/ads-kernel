#!/usr/bin/env bash
# Comprueba si la copia vendorizada del kernel ha sido modificada localmente (K0.11).
set -euo pipefail
cd "$(dirname "$0")/.."
KV=$(cat kernel/VERSION)
SUM=$(sha256sum kernel/KERNEL.md | cut -c1-16)
echo "kernel version : $KV"
echo "hash local     : $SUM"
if [ -f kernel/.upstream-hash ]; then
  UP=$(cat kernel/.upstream-hash)
  if [ "$SUM" = "$UP" ]; then echo "estado         : LIMPIO (coincide con el release)"
  else echo "estado         : DIVERGENTE — el kernel ha sido editado localmente."
       echo "                 K0.11: no se edita el kernel vendorizado."
       echo "                 Usa un override declarado en PROFILE.md §9,"
       echo "                 o promueve el cambio upstream (K0.12)."; fi
else
  echo "$SUM" > kernel/.upstream-hash
  echo "estado         : hash de referencia anotado"
fi
