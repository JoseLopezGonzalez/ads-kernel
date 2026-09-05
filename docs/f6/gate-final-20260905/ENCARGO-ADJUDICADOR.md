# GATE DE CERTIFICACIÓN FINAL DE `F6` · 2026-09-05 · ENCARGO DEL ADJUDICADOR

Se te crea **ahora**, y no antes, porque los tres revisores han cerrado. No has visto nada de
lo que han hecho hasta este momento, y ellos no te han visto a ti.

## Qué juzgas

La candidata **`c2437214c9353185d6b90b8fe86178302d4cf349`**, tree `bb5b674`, publicada como
`review/f6-candidate-g01-g08-20260905`. Base: `769a8b6`.

**Árbol congelado** (el único que juzgas):
`/tmp/claude-1000/-home-jose-ads-kernel/f950a505-4ab2-402f-a332-d1c02336312e/scratchpad/gate-congelado`

Intérprete: `/home/jose/.local/bin/python3.12`. El `python3` del `PATH` es 3.10 y no vale.

## Lo que tienes delante

- `…/scratchpad/DICTAMEN-REV-1.md`, `DICTAMEN-REV-2.md`, `DICTAMEN-REV-3.md`
- `…/scratchpad/LECTURA-REV-1.json`, `LECTURA-REV-2.json`, `LECTURA-REV-3.json`
- `…/scratchpad/MANIFIESTO.json` — la asignación
- `…/scratchpad/INFORME-COBERTURA.json` — lo que el instrumento midió

**La cobertura, ya medida por el coordinador y que tienes que RE-MEDIR tú:**

```text
COBERTURA DEL GATE · COMPLETA
  REV-1  87 fichas · 55204 líneas · SIN LEER 0 · cerrado sí
  REV-2  86 fichas · 55203 líneas · SIN LEER 0 · cerrado sí
  REV-3  86 fichas · 55208 líneas · SIN LEER 0 · cerrado sí
  las CUATRO restas: ∅ ∅ ∅ ∅
```

No te lo creas porque lo diga el coordinador: el coordinador es quien hundió los dos gates
anteriores. Vuelve a correr `comprobar-cobertura-de-gate.py` sobre el congelado con los tres
manifiestos de lectura y comprueba tú mismo si el gate es **VÁLIDO por cobertura**.

## Tu trabajo, en este orden

1. **¿Es VÁLIDO el gate?** Cobertura re-medida por ti. Si no lo es, dilo y para: un gate sin
   cobertura no adjudica nada.
2. **Verifica cada hallazgo de cada revisor, uno a uno.** Los tres traen hallazgos GRAVES y
   algunos se solapan. Para cada uno: ¿se reproduce con la orden que el revisor da? ¿Dice lo
   que el revisor dice que dice? Un hallazgo que no se reproduce **se rechaza y se registra
   como rechazado, con su motivo**. Los revisores se equivocan; tú lo compruebas.
3. **Resuelve las contradicciones** entre dictámenes, si las hay, con la medición y no con
   la autoridad de quien lo dijo.
4. **Adjudica las dos proposiciones**, cada una por separado:
   - `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — ¿sí o no?
   - `F6 QUEDA CERTIFICADA` — ¿sí o no?
5. **Y di qué consta A FAVOR de la candidata**, no sólo en contra. Un dictamen que sólo
   acumula cargos no es una adjudicación.

## Lo que NO puedes hacer

- No corriges nada. No escribes en ningún árbol del repositorio. Copia a un temporal tuyo
  para experimentar.
- Ninguna orden `git` que escriba: sin `commit`, `merge`, `rebase`, `reset`, `amend`,
  `cherry-pick`, `tag`, `push`, ni `checkout` que mueva un árbol. Leer, sí.
- No toques `redesign/kernel-2.0`. No uses, leas como fuente ni publiques `fd633383…`.
- No arranques PesquerApp.
- **No redondees ninguna resta a cero**, ni al revés. Y si el defecto es del coordinador,
  dilo: es lo que los dos gates anteriores adjudicaron y es lo que hay que poder decir.

## Entregable

`…/scratchpad/ADJUDICACION.md`, con: el juicio de validez del gate; la tabla de hallazgos
verificados —confirmado / rechazado, con el motivo—; las dos proposiciones adjudicadas; lo
que consta a favor; y **el alcance de lo que tú no has podido comprobar**.
