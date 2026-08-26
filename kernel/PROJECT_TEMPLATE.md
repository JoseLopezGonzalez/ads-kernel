# PROJECT — <nombre>

Binder del producto. Declara de qué está compuesto este sistema de desarrollo.

> **Este repositorio es el control plane versionado del producto.** No contiene el código.
> Los repositorios técnicos se declaran en `SOURCES.toml` —en la raíz de este repositorio— y se materializan
> como hermanos de éste dentro del workspace.

## Composición organizativa

| Capa | Artefacto | Versión | Editable aquí |
|---|---|---|---|
| Kernel | `kernel/KERNEL.md` | <ver kernel/VERSION> | **NO** (K0.11) |
| Pack | `packs/<pack>/PACK.md` | | **NO** |
| Profile | `PROFILE.md` | — | **SÍ** |
| Compilado | `AGENTS.md` | generado | regenerar, no editar |

Overrides declarados del kernel: **<ninguno / listar>**

## Composición técnica del producto

**No se repite aquí.** Su fuente única es `SOURCES.toml`: qué fuentes
existen, dónde se materializan y qué componentes lógicos viven en cada una. Copiar sus URLs
en esta tabla crearía dos verdades que envejecerían por separado.

```bash
python3 tooling/workspace.py status     # qué fuentes hay y en qué estado
```

## Reglas

- La composición técnica vive **sólo** en `SOURCES.toml`. Ningún documento la duplica.
- `kernel/` y `packs/` son copias vendorizadas. Para otro comportamiento: **override declarado en `PROFILE.md` §9**, nunca editar la copia (`./tooling/kernel-status.sh` detecta la divergencia).
- `AGENTS.md` es compilado. Para cambiar una regla operativa, cambia el origen y recompila.
- Candidatos a promover a kernel o pack → `docs/UPSTREAM.md`, revisados al cerrar cada circuito (K0.12).

## Arranque

Ver `START_HERE.md`.

> Los dos ficheros de este binder —`SOURCES.toml` y `AGENTS.md`— se nombran sin enlazar: en
> la plantilla todavía no existen, y un enlace roto en el kernel viajaría a cada proyecto.
