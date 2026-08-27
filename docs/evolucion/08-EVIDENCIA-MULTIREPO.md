# 08 — QUÉ ESTÁ DEMOSTRADO DE LA IMPLEMENTACIÓN MULTI-REPO

> Matriz de evidencia de los criterios de aceptación `CA-1`–`CA-17` (§99) y de los diez
> criterios de descubrimiento (§100) de
> `ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`.
>
> **Existe por una afirmación falsa.** El checkpoint de la entrega anterior decía «CA-1 a
> CA-17 verificados, y los diez criterios de descubrimiento del §100», y «test mental final
> superado: borradas las cuatro fuentes, el workspace se reconstruye». Ninguna de las tres
> tenía evidencia reproducible detrás. Un test mental no es una prueba, y «verificado» sin
> decir POR QUÉ ARTEFACTO no significa nada.

## Los cuatro grados, y qué autoriza a decir cada uno

```text
EJECUTADA      una prueba automática lo ejercita y falla si deja de cumplirse.
               Autoriza a decir «demostrado».

ESTRUCTURAL    un validador comprueba el corpus: que el artefacto existe, que dice lo que
               tiene que decir, que nadie lo contradice. Autoriza a decir «el corpus lo
               sostiene», NO «funciona en un producto real».

CONTRATO       está escrito y es coherente, y su ejecución exige runtime o piloto.
               Autoriza a decir «definido». NO autoriza a contarlo como verificado.

ABIERTO        ni una cosa ni la otra. Se dice.
```

## §99 — criterios de aceptación funcionales

| CA | qué exige | grado | qué lo sostiene |
|---|---|---|---|
| CA-1 | crear un ADS Project produce `workspace/ads` | **EJECUTADA** | `T168` sobre los cuatro casos de pack · `test_bootstrap_crea_workspace_con_ads_dentro` |
| CA-2 | el control repo declara frontend y backend en `SOURCES.toml` | **EJECUTADA** | `test_03_varias_sources_validas` |
| CA-3 | con ambos ya clonados, `check` los detecta sin volver a clonar | **EJECUTADA** | `test_adopcion_de_dos_repos_existentes` · `test_05_reutilizacion_de_source_existente` · `test_43_reconstruccion_parcial_solo_toca_lo_que_falta` |
| CA-4 | con backend ausente, `init backend` lo materializa | **EJECUTADA** | `test_04_clone_de_source_ausente` · `test_19_seleccion_de_source_en_init` |
| CA-5 | una source con remote equivocado produce error seguro | **EJECUTADA** | `test_11_remote_equivocado` — y el repositorio equivocado sigue en disco |
| CA-6 | un repo dirty no pierde cambios | **EJECUTADA** | `test_13_repo_dirty_no_se_destruye` · `test_43` con marca local en cada fuente |
| CA-7 | un component apunta a un path dentro de una source | **EJECUTADA** | `test_dos_componentes_misma_source` · `test_16_component_path_fuera_de_source` · `test_22_escape_por_enlace_simbolico_en_componente` |
| CA-8 | dos components apuntan a la misma source | **EJECUTADA** | `test_dos_componentes_misma_source` |
| CA-9 | la documentación deja de enseñar la adopción copiando ADS dentro del repo técnico | **ESTRUCTURAL** | `T161`, patrones `R2` y `R8`, sobre 279 ficheros · negativas `N161e` y `N161c` |
| CA-10 | `PROFILE` sigue siendo único por producto | **CONTRATO** | C6 «qué NO puede vivir en una fuente» · `BOOTSTRAP_PROMPT` · `T171` §100.9 comprueba que la instrucción está. **Nada detecta un PROFILE duplicado dentro de una source: no hay sources, ni runtime** |
| CA-11 | `DSP`/rutas/paquetes expresan alcance multi-source | **CONTRATO** | `E2.2` · `gate:workspace-conforme` de C6 · gate de `DSP/CAPACIDAD` · `ARQ/encaje` lo declara por paquete. Un paquete es objeto de runtime: no hay esquema canónico que validar |
| CA-12 | el checkpoint registra varias revisiones de sources | **ESTRUCTURAL** | `plantillas/CHECKPOINT.md` con su bloque `sources:` y su `based_on` multi-fuente · `E2.3`. Su ejecución es **T170**, en `contrato-definido` |
| CA-13 | existe representación de Integration Set | **ESTRUCTURAL** | `esquemas/integration-set.yaml` —`commit` con patrón de SHA, nunca una rama— y `plantillas/INTEGRATION-SET.md`, validados por `ads_lint` |
| CA-14 | `G29` no presupone una única branch/PR global | **ESTRUCTURAL** | aviso de revisión en `G29` · `C7` · `E2.4` · guardado por `T161` `R4` y `R10` con sus negativas |
| CA-15 | los validadores del kernel pasan | **EJECUTADA** | 13/13 en verde, publicados por `registrar_evidencia.py` y comprobados por `T158` |
| CA-16 | los tests de workspace pasan sin red externa | **EJECUTADA** | `GIT_ALLOW_PROTOCOL=file` en el entorno de las pruebas · `test_44` comprueba que https, ssh y git están bloqueados · `test_45` que el transporte local sigue funcionando |
| CA-17 | ninguna dependencia obligatoria de Cursor, Claude, Codex, Gemini o GitHub | **ESTRUCTURAL, parcial** | `T92` sobre `kernel/operativo` y `packs` · la suite de workspace corre contra repositorios Git locales, sin proveedor. **Alcance declarado:** `T92` no recorre `tooling/`, donde GitHub aparece como EJEMPLO de normalización de URL; y `K0.10` nombra la toolchain agentic como excepción consciente |

**Nueve de diecisiete están ejecutadas. Cinco son estructurales, dos son contrato y una es
estructural parcial.** Ninguna está «verificada» en el sentido de haber pasado por un
producto real: eso sigue sin ocurrir.

## §100 — los diez criterios de descubrimiento

El §100 pide que un agente que sólo abra `workspace/ads` **descubra** diez cosas sin
información oral. Eso exige **un agente y un piloto**, y no hay ninguno de los dos.

```text
COMPROBADO      que cada uno de los diez tiene un sitio declarado donde leerse dentro del
                proyecto recién creado, que ese sitio existe y que lo dice.
                Lo comprueba T171, y publica con esas palabras que su alcance es ese.

NO COMPROBADO   que un agente lo descubra. Es lo que el §100 pide de verdad.
```

`T171` tiene dos pruebas negativas: `N171` retira uno de los diez del prompt de arranque, y
`N171b` lo retira de **los dos** sitios donde podía leerse. Quitarlo de uno solo **no** es
infracción: el §100 pide poder descubrirlo, no que esté en un fichero concreto.

## El caso de reconstrucción

El checkpoint anterior lo daba por superado como **test mental**. Ahora es
`test_42_producto_de_cuatro_fuentes_se_reconstruye_tras_borrarlas`: cuatro repositorios Git
locales, sin red; se materializan, se **borran los cuatro**, y el workspace se reconstruye
desde el repositorio ADS de control y su manifiesto, con las mismas revisiones, el mismo
contenido y sus cuatro componentes.

Lo que ese caso **no** demuestra: que las cuatro fuentes de un producto real, con sus
permisos, sus tamaños, sus submódulos y sus LFS, se reconstruyan igual.

## Lo que sigue abierto

```text
T169 · T170              en contrato-definido. Exigen runtime y un guion con dos repos
                         reales. NO se cuentan como demostradas.
PILOTO                   nada de esto ha pasado por un producto real. La columna de uso
                         real sigue vacía.
CA-10 · CA-11            dependen de runtime para poder comprobarse de verdad.
§100 COMO DESCUBRIMIENTO comprobada la condición necesaria, no la propiedad.
CA-17 EN tooling/        T92 no lo recorre; el alcance queda escrito arriba.
PYTHON 3.11              `tomllib` es estándar desde 3.11. En 3.10 el manifiesto no se lee
                         y tres validadores fallan con un error que lo dice. No es un
                         defecto silencioso, pero es un requisito real del entorno.
```
