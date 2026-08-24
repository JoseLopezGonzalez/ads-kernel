# PROJECT — <nombre>

Binder del proyecto. Declara de qué está compuesto este sistema de desarrollo.

## Composición

| Capa | Artefacto | Versión | Editable aquí |
|---|---|---|---|
| Kernel | `kernel/KERNEL.md` | <ver kernel/VERSION> | **NO** (K0.11) |
| Pack | `packs/<pack>.md` | | **NO** |
| Profile | `PROFILE.md` | — | **SÍ** |
| Compilado | `AGENTS.md` | generado | regenerar, no editar |

Overrides declarados del kernel: **<ninguno / listar>**

## Reglas

- `kernel/` y `packs/` son copias vendorizadas. Para otro comportamiento: **override declarado en `PROFILE.md` §9**, nunca editar la copia (`./tooling/kernel-status.sh` detecta la divergencia).
- `AGENTS.md` es compilado. Para cambiar una regla operativa, cambia el origen y recompila.
- Candidatos a promover a kernel o pack → `docs/UPSTREAM.md`, revisados al cerrar cada circuito (K0.12).

## Arranque

Ver `START_HERE.md`.
