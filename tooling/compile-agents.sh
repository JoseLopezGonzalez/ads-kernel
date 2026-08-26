#!/usr/bin/env bash
# Prepara la recompilación de AGENTS.md desde kernel + packs + PROFILE + SOURCES.toml.
#
# NO genera el texto: inventaría las fuentes y emite el encargo que un agente ejecuta.
# La compilación final la hace el Circuito 0.
#
# Se ejecuta dentro del repositorio ADS de CONTROL de un producto.
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="AGENTS.md"
KV=$(cat kernel/VERSION)

# Los packs son DIRECTORIOS con su PACK.md desde la línea 2.0. La forma plana `packs/*.md`
# era la de 1.3.0 y quedó retirada: buscarla aquí devolvía «ninguno» en todo proyecto real.
PACKS=$(find packs -mindepth 2 -maxdepth 2 -name PACK.md 2>/dev/null \
        | sed 's|^packs/||; s|/PACK.md$||' | grep -v '^legacy-' | sort | tr '\n' ' ')
[ -n "$PACKS" ] || PACKS="ninguno"

echo "Fuentes detectadas:"
echo "  kernel/KERNEL.md         v$KV   ($(wc -l < kernel/KERNEL.md) líneas)"
echo "  kernel/operativo/        el contenido operativo que un rol ejecuta"
for p in $PACKS; do
  [ "$p" = "ninguno" ] && continue
  echo "  packs/$p/PACK.md   ($(wc -l < "packs/$p/PACK.md") líneas)"
done
echo "  PROFILE.md               ($([ -f PROFILE.md ] && wc -l < PROFILE.md || echo 0) líneas)"
if [ -f SOURCES.toml ]; then
  N=$(grep -c '^\[\[sources\]\]' SOURCES.toml || true)
  echo "  SOURCES.toml             $N fuentes declaradas"
else
  echo "  SOURCES.toml             AUSENTE — este repositorio no es un ADS Project instalado"
fi
echo
echo "AGENTS.md actual: $([ -f "$OUT" ] && wc -l < "$OUT" || echo 0) líneas"
echo
echo "Encargo para el agente compilador:"
cat <<'EOF'
  Recompila AGENTS.md desde las fuentes, en este orden de prioridad:
   1. Reglas duras de seguridad (G27, y las del pack instalado si las hay)
   2. DÓNDE ESTÁ EL CÓDIGO: este es el control repo; las fuentes se resuelven por
      SOURCES.toml; no asumas que el repo actual contiene el código; comprueba el
      workspace antes de actuar cuando el paquete dependa de fuentes
   3. Rutina de sesión: arranque, cierre, journal
   4. Autoridad: qué decides tú, qué es del Owner
   5. Git POR FUENTE, y convergencia por Integration Set
   6. Validación humana por lotes
   7. ABIERTO vs PROVISIONAL, con la tabla vigente del PROFILE
   8. Reglas del pack que apliquen a esta clase de proyecto
   9. Reglas específicas del producto (PROFILE)
  10. Spikes pendientes y comandos

  Imperativo, comprobable, sin prosa explicativa. Lo que no quepa se deja en su fuente
  con un puntero.

  NO incrustes una copia de SOURCES.toml. La lista concreta de repositorios vive allí, y
  duplicarla obligaría a editar AGENTS.md cada vez que cambie una URL. Escribe la REGLA
  —«resuelve las fuentes por SOURCES.toml»—, no los datos.
EOF
