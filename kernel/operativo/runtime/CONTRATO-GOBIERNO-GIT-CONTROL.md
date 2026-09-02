# CONTRATO DERIVADO · GOBIERNO GIT DEL REPOSITORIO DE CONTROL

**Qué es.** El **segundo** de los tres contratos derivados que
[`(g)` `g.17`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md) nombra y deja sin
escribir. Instancia `g.14`, y su sede normativa la fijó la resolución `O16`.

**Qué NO es.** No es el contrato Git de las FUENTES. `C7` gobierna las fuentes, **no se
toca**, y sigue acotado a ellas: `11-ARQ` §7.6 declara el hueco —*«EL CONTROL REPO NO ESTÁ
CUBIERTO: ninguna fila de la tabla de propiedad de `C7` lo alcanza»*— y esto es lo que lo
ocupa. El sujeto es distinto, y por eso la tabla de `C7` **no se copia aquí**.

---

## 1 · Lo que `g.14` fija, y esto instancia

```text
· la rama canónica del control repo NO se rige por la regla Git de las fuentes
· la unidad aislada de trabajo es la TRANSACCIÓN, no la rama
· las peticiones de integración NO se usan para el estado
· la rama canónica NUNCA contiene estado parcial
· la concurrencia entre máquinas se SERIALIZA, y la bifurcación se DETECTA
· FORZAR REFERENCIAS ESTÁ PROHIBIDO, sin excepción automática y sin que ninguna política
  pueda autorizarlo
· la política de publicación vale «esperando-owner» por defecto
```

## 2 · La tabla de propiedad — es DATO, no prosa

Vive en [`gobierno/POLITICA-CONTROL-REPO.yml`](gobierno/POLITICA-CONTROL-REPO.yml) y declara,
por actor y por materia: quién crea, confirma, publica, abre rama, integra, verifica,
revierte y retira rama; qué refs puede mover cada uno; qué operaciones exigen serialización;
qué actualización depende de una revisión base; y qué está prohibido.

**La política vive en el kernel y por tanto entra en la HUELLA**: editarla cambia la huella y
lo detecta la comprobación de integridad. Y **no puede eximirse a sí misma**: una regla que
sacara del perímetro al fichero de política se rechaza al cargarla, porque sería la puerta
para cambiar la regla y aprobarse con ella en el mismo acto.

## 3 · Las once capacidades ejecutables

```text
 1 representar propiedad y autoridad      6 confirmar la mutación
 2 obtener una concesión sobre una ref    7 detectar pérdida de autoridad
 3 contrastar la revisión base            8 rechazar doble escritor
 4 preparar la mutación sin publicarla    9 serializar entre dos procesos reales
 5 validar la política                   10 recuperar después de una caída
                                         11 dejar evidencia auditable
```

**Preparar y publicar son actos DISTINTOS**, y por eso publicar se puede rechazar: `preparar`
escribe el índice y construye el commit con `commit-tree`, que **no mueve ninguna ref**;
`confirmar` mueve la ref con **compare-and-swap** contra el valor viejo esperado.

**La concesión es DURABLE**, no un `flock`: un `flock` no sobrevive a la caída, y entonces
«recuperar después de caída» dejaría de ser demostrable.

**Antes de confirmar se exige que la ventana transaccional del estado esté CERRADA.** Es lo
que hace cierto —y no sólo prometido— que la rama canónica nunca contiene estado parcial.

## 4 · `G-A8`, y son DOS mitades

`g.16` `G-A8`: *«forzar una referencia del control repo es imposible por política, y
detectable si se intenta»*. Una sola mitad no lo cumple.

```text
IMPOSIBLE    un hook `reference-transaction` instalado en el control repo RECHAZA toda
             actualización que no sea fast-forward y todo borrado de ref protegida. El
             canal único de Git rechaza además `--force`, `--force-with-lease` y el `+` del
             refspec ANTES de invocar nada. `comprobar_hook()` mide el DIGEST del hook: si
             lo retiran o lo editan, es `HookAusente`

DETECTABLE   `verificar_refs()` contrasta el LINAJE registrado contra las refs actuales y
             DENUNCIA un forzado aunque el hook se hubiera quitado. Se registra el linaje
             completo y no sólo la cabeza: con sólo la cabeza, un forzado seguido de una
             confirmación legítima borraría la evidencia
```

**Nunca se usa `--force-with-lease` como sustituto de una política.** Es la trampa que este
contrato existe para cerrar: parece una guarda y es una bandera.

## 5 · Errores tipados

`ErrorDeGobierno` · `AutoridadDeRefNoConcedida` · `RevisionBaseObsoleta` · `DobleEscritor` ·
`RefProtegida` · `HistoriaNoLineal` · `PoliticaViolada` · `EstadoParcialEnLaRama` ·
`ForzadoDetectado` · `HookAusente` · `GitInvocacionProhibida` · `GitFallo`.

## 6 · Qué demuestra, y dónde

`T187` en [`pruebas/test_gobierno_git.py`](pruebas/test_gobierno_git.py), sobre repositorios
Git **reales** y sin red, y los pasos 19 y 20 de `T193` en
[`pruebas/escenario_e2e_runtime.py`](pruebas/escenario_e2e_runtime.py).

## 7 · Lo que este contrato NO cubre todavía

La **serialización entre MÁQUINAS** se demuestra entre procesos reales de la misma máquina;
la bifurcación entre máquinas se DETECTA —lo hace el motor con `detectar_bifurcacion`— y su
RESOLUCIÓN sigue siendo, como `g.6` la deja, materia calibrable. La publicación a un remoto
no entra en este corte: la política de publicación conserva su valor por defecto
«esperando-owner». Y **nada de esto está CERTIFICADO**.
