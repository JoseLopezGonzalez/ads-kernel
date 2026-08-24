#!/usr/bin/env bash
# Compila kernel + packs + profile en un AGENTS.md operativo.
# NO genera el texto: extrae las secciones marcadas como operativas y avisa
# de lo que un agente debe redactar. La compilación final la hace el Circuito 0.
set -euo pipefail
cd "$(dirname "$0")/.."

OUT="AGENTS.md"
KV=$(cat kernel/VERSION)
PACKS=$(ls packs/*.md 2>/dev/null | xargs -n1 basename 2>/dev/null | tr '\n' ' ' || echo "ninguno")

{
  echo "<!-- GENERADO. No editar a mano."
  echo "     Fuentes: kernel v$KV | packs: $PACKS | PROFILE.md"
  echo "     Regenerar: ./tooling/compile-agents.sh -->"
  echo
} > "$OUT.header"

echo "Fuentes detectadas:"
echo "  kernel/KERNEL.md         v$KV   ($(wc -l < kernel/KERNEL.md) líneas)"
for p in packs/*.md; do echo "  $p   ($(wc -l < "$p") líneas)"; done
echo "  PROFILE.md               ($(wc -l < PROFILE.md) líneas)"
echo
echo "Objetivo de compilación: < 400 líneas (K0.2)."
echo "AGENTS.md actual: $([ -f "$OUT" ] && wc -l < "$OUT" || echo 0) líneas"
echo
echo "Encargo para el agente compilador:"
cat <<'EOF'
  Recompila AGENTS.md desde las tres fuentes, en este orden de prioridad:
   1. Reglas duras de seguridad (G27, y W6/M8 si aplican)
   2. Rutina de sesión: arranque, cierre, journal
   3. Autoridad: qué decides tú, qué es del Owner
   4. Velocidad por riesgo y Git
   5. Validación humana por lotes
   6. ABIERTO vs PROVISIONAL, con la tabla vigente del PROFILE
   7. Reglas del pack que apliquen a esta clase de proyecto
   8. Reglas específicas del producto (PROFILE)
   9. Spikes pendientes y comandos
  Imperativo, comprobable, sin prosa explicativa. Si no cabe en 400 líneas,
  lo que sobra es contexto: déjalo en su fuente y pon un puntero.
EOF
rm -f "$OUT.header"
