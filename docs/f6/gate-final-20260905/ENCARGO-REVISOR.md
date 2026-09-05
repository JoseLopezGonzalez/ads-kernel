# GATE DE CERTIFICACIÓN FINAL DE `F6` · 2026-09-05 · ENCARGO DEL REVISOR

## Qué se juzga

La candidata **`c2437214c9353185d6b90b8fe86178302d4cf349`**, tree `bb5b674`, publicada como
`review/f6-candidate-g01-g08-20260905`. Base: `769a8b6`.

**El árbol congelado está en:**
`/tmp/claude-1000/-home-jose-ads-kernel/f950a505-4ab2-402f-a332-d1c02336312e/scratchpad/gate-congelado`

Ése es el árbol que juzgas, y **sólo ése**. No leas `/home/jose/ads-kernel`: es el árbol de
trabajo del coordinador y puede moverse debajo de ti.

Intérprete: `/home/jose/.local/bin/python3.12`. El `python3` del `PATH` es 3.10 y **no vale**.

## Tu lote

Está en `…/scratchpad/LOTE-<TU-NOMBRE>.txt`. Cada línea dice una ruta y si te toca **entera**
o **un tramo** `a-b`. El reparto es mecánico y los tres lotes difieren en menos del 0,01 %.

**Lee lo tuyo. Todo lo tuyo.** Los dos gates anteriores se declararon NO VÁLIDOS por
cobertura, no por lo que los revisores dijeron. Un dictamen brillante sobre el 60 % del lote
no vale nada: el instrumento mide líneas, no impresiones.

## Lo que tienes que entregar, y en qué formato

**1 · Tu manifiesto de lectura**, en `…/scratchpad/LECTURA-<TU-NOMBRE>.json`:

```json
{"revisor": "REV-n", "cerrado": true,
 "leidas": [{"ruta": "...", "sha256": "...", "tramos": [[1, 240]]}, ...]}
```

`sha256` es el del fichero **en el árbol congelado** —el mismo que tu lote publica—.
`tramos` son los tramos que has leído DE VERDAD. `cerrado: true` sólo si has leído todo lo
asignado; si no, `false`, y dilo en el dictamen. **No redondees.** El coordinador va a pasar
tu manifiesto por `comprobar-cobertura-de-gate.py`, que resta línea a línea, y una línea de
más declarada es una falsedad que el instrumento encuentra.

**2 · Tu dictamen**, en `…/scratchpad/DICTAMEN-<TU-NOMBRE>.md`, con esta estructura:

- **Veredicto** sobre las dos proposiciones, cada una por separado y sin mezclarlas:
  - `F6 ESTÁ COMPLETAMENTE IMPLEMENTADA` — ¿sí o no?
  - `F6 QUEDA CERTIFICADA` — ¿sí o no?
- **Hallazgos**, numerados y por gravedad. Cada uno: **hecho reproducido** con la orden
  literal y su salida literal, dónde, por qué importa, y qué remedio cierra la CLASE.
- **Lo que NO has podido comprobar, y por qué.** Un alcance sin declarar es el defecto que
  este proyecto ha visto más veces.

## Qué se afirma, y que tienes que atacar

La candidata dice cerrar `G-01`…`G-08` y `D-01`…`D-05`, más los once hallazgos de una
auditoría independiente previa. Todo está en `docs/f6/05-MATRIZ-CIERRE-G01-G08.md` §5 y §6.

Línea base que el coordinador afirma:

```text
38/38 validadores en verde · 38 evidencias publicadas · 0 problemas
170 infracciones detectadas · 0 NO detectadas
582 bloques canónicos · 0 errores · 0 avisos
314 escenarios · 254 contrastados · 0 divergencias · 0 en `prueba-ejecutada`
universo obligatorio: 58 obligaciones · A=0 · B=0 · C=0
inventario de aislamiento: 58 puntos ejecutables · 58 con guarda · 0 sin guarda
huella `854dfa1b99be3824` · almacenada = calculada · estable en dos cálculos
```

**Reprodúcelo. No lo creas.** Y recuerda lo que el gate anterior dejó escrito: *un
`A=0 · B=0 · C=0` verdadero NO acredita lo que `O26` §5.1 y §5.2 le piden, porque sus
rótulos no miden eso*. Los propios rótulos de las restas lo dicen.

## Prohibiciones

- No escribes en el árbol congelado ni en `/home/jose/ads-kernel`. Si necesitas experimentar,
  **copia a un temporal tuyo**.
- Ninguna orden `git` que escriba: sin `commit`, `merge`, `rebase`, `reset`, `amend`,
  `cherry-pick`, `tag`, `push`, ni `checkout` que mueva un árbol. Leer con `git show`,
  `git diff`, `git log` sí.
- No toques `redesign/kernel-2.0`. No uses, leas como fuente ni publiques `fd633383…`.
- No arranques PesquerApp bajo ningún concepto.
- **No hables con los otros revisores.** Vuestros dictámenes valen porque son independientes.
- No corrijas nada. Tu trabajo es juzgar, no arreglar.

## Cómo leer 55 000 líneas sin engañarte

Lee con `sed -n 'a,bp'` sobre el árbol congelado, en bloques que puedas sostener. Anota los
tramos según los cierras, no al final de memoria. Si al terminar no has llegado, **dilo**:
`cerrado: false` y la cifra exacta. Un gate declarado NO VÁLIDO por cobertura honesta es
infinitamente mejor que un verde falso — y esa frase la ha pagado ya este proyecto dos veces.
