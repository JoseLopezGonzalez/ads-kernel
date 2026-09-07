# `O31` · VERIFICACIÓN POR COMPOSICIÓN DE `F6` — 2026-09-07

> **Qué es este documento.** El registro final que `O31` §10 manda escribir después del
> dictamen del verificador independiente. Contiene el objeto juzgado, la identidad del
> verificador, su cobertura, los comandos y resultados, sus declaraciones literales, sus
> hallazgos, su razonamiento y el estado final.
>
> **Qué NO es.** No es una corrección. `O31` §9 es terminante: si la composición falla, se
> registra la causa material, **no se corrige en respuesta al dictamen**, no se abre otro
> gate y no se inicia otro ciclo automático. Este documento se escribe **encima** de la
> candidata congelada y no la toca.
>
> **Autoridad.** El dictamen es del verificador. Se transcribe íntegro y sin edición. Lo
> que el coordinador tenga que decir se dice en §4 y se dice que es del coordinador.

## 1 · Objeto y referencias

```text
base de O30        a672ed95686a37b5862f4486a5699bdcebb0f7fd
base de O31        4d99a5e3de7ceb27b2af6f6632456d46741f05fb
candidata          697eab9c8078b467b3741151e36fb5af792046e3
tree               92f7e0dfb9dc36f78d2bc13665bb5419af3614c0
publicada en       review/f6-o31-four-controls-candidate-20260907
resultado en       review/f6-o31-final-insufficient-20260907

sobre de ancla     /home/jose/ads-sobre-o31/sobre-o31.json
  sha256           34f23e7aceec9f7cb2a94b48d3f826cb1798bf8eee9c8c25952fa9829080b0ac
  firma            sobre-o31.json.sig, principal `ancla-o31@ads`, privada DESTRUIDA
  lo demostrable   firma, contenido y orden operacional observado.
                   NO se afirma anterioridad criptográfica — `O31` §8

checkout del verificador   /home/jose/ads-verificacion-o31, HEAD desprendido en la
                           candidata, árbol limpio antes y después
```

**Sede del estado de fase:** [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md)
§6. Este documento **no la duplica**: registra el veredicto y remite.

## 2 · Estado final registrado — `O31` §10

```text
F6 NO CERTIFICADA
F6 ABIERTA · INICIADA · EN CURSO
M-04 NO SUPERADA          (estado literal emitido por el verificador)
C-L.7 NO CERRADA          (estado literal emitido por el verificador)
V-G1 NO CERRADA
V-G2 NO CERRADA
PESQUERAPP SIGUE BLOQUEADA · NO INICIADA
```

**Causa material exacta.** Fallan cuatro de las nueve condiciones de `O31` §7 —la 1, la 2,
la 3 y la 4—, y cada una basta por sí sola. En palabras del verificador: *el delta
construyó los cuatro instrumentos que `O31` pedía y los tres que deciden —el universo, la
dispensa y el control de clase— tienen cada uno una puerta abierta que un adversario cruza
con una línea de texto, una lista de argumentos o una palabra terminada en `-ia`.*

**Lo que sí queda acreditado, y el verificador lo declara con la misma firmeza:**
`COBERTURA INTEGRAL` —56 de 56 ficheros modificados desde `a672ed9` leídos enteros, 39 955
líneas, resta VACÍA demostrada mecánicamente, **la primera cobertura integral del
expediente**—; `K01`–`K24 CONTINÚAN SATISFECHAS`; `OBLIGACIONES INTERNAS DE F6 CONTINÚAN
COMPLETAS`; `OCHO CONDICIONES DE O26 CONTINÚAN SATISFECHAS`; ninguna regresión introducida
por el delta; ningún universo vaciado por reclasificación; ningún material protegido
tocado; PesquerApp no iniciada.

## 3 · Dictamen del verificador, transcrito íntegro

> El texto que sigue es del verificador independiente final de `O31`. No se ha editado,
> resumido ni reordenado.

---

# DICTAMEN DEL VERIFICADOR INDEPENDIENTE FINAL DE `O31`

## 1 · Objeto exacto juzgado

| | |
|---|---|
| **Checkout congelado** | `/home/jose/ads-verificacion-o31`, HEAD desacoplado |
| **Commit** | `697eab9c8078b467b3741151e36fb5af792046e3` |
| **Tree** | `92f7e0dfb9dc36f78d2bc13665bb5419af3614c0` |
| **Base de `O30`** | `a672ed95686a37b5862f4486a5699bdcebb0f7fd` |
| **Base de `O31`** | `4d99a5e3de7ceb27b2af6f6632456d46741f05fb` |
| **Candidata que `O30` juzgó** | `60b640db1762e1623af2371126de01ce1c0d0b88` |
| **Sobre de ancla** | `/home/jose/ads-sobre-o31/` (fuera del repositorio) |
| **Intérprete** | `/home/jose/.local/bin/python3.12` en toda medición |

`git status --porcelain` sobre el checkout congelado: **vacío**. El árbol no se ha tocado.

## 2 · Identidad e independencia

Soy el verificador independiente único que `O31` §7 manda crear después de congelar la
candidata. No implementé nada de este delta, no participé en su construcción y no he
recibido de nadie el resultado que debía alcanzar. He trabajado sobre mi propio checkout;
**no he modificado el repositorio, no he corregido ningún hallazgo, no he creado commits ni
referencias**. Todos mis ataques se han montado sobre copias en `/tmp` obtenidas con
`git clone --no-hardlinks` y `git checkout --detach`; nunca sobre el original y nunca con
`git worktree`.

### El sobre, juzgado por lo que es

Verifiqué la firma yo mismo, con el aparato del propio corpus:

```console
firma.verificar(mensaje, firma, firmantes=firmantes, principal="ancla-o31@ads",
                espacio_de_nombres="ads-atestacion-de-raiz-externa")
→ valida=True  Good "ads-atestacion-de-raiz-externa" signature for ancla-o31@ads with ED25519 key
```

`exigir_firma_valida` no levanta. Los digests cuadran con `DIGEST.txt`:

```console
sobre-o31.json      34f23e7aceec9f7cb2a94b48d3f826cb1798bf8eee9c8c25952fa9829080b0ac  ✓
sobre-o31.json.sig  418934c3bd06f9bd0438d1b910c64841d2da17143429fd775c104c4fe12d4e47  ✓
firmantes           f167ad1cbf708d57a5471204ba8d5d9a9b282989f05f6775474aba8ef61aee4f  ✓
```

Lo juzgo por lo que él mismo dice demostrar: **firma, contenido y orden operacional
observado**. No le atribuyo anterioridad criptográfica y no baso ninguna conclusión en
ella. Su utilidad real para este dictamen ha sido una: entregarme enteras las 33
autopruebas que el implementador usó para construir el control de `C-L.7`, de modo que mis
variantes sean demostrablemente distintas.

## 3 · COBERTURA · la lectura integral y su resta mecánica

`FICHEROS MODIFICADOS DESDE a672ed9` (`git diff --name-only a672ed9 HEAD | sort`): **56**.
`FICHEROS LEÍDOS ÍNTEGRAMENTE`, de la primera línea a la última: **56**, **39 955 líneas**.

```console
$ comm -23 modificados.txt leidos.txt
[fin de la resta]                 ← VACÍA
$ comm -13 modificados.txt leidos.txt
[fin]                             ← ningún fichero de más
```

| líneas | fichero |
|---:|---|
| 13 | `.sello-producto` |
| 165 | `docs/canonico/00-EMPEZAR-AQUI.md` |
| 229 | `docs/canonico/03-GOBIERNO-Y-AUTORIDAD.md` |
| 584 | `docs/canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md` |
| 437 | `docs/canonico/07-GUIA-OPERATIVA-DE-F6.md` |
| 647 | `docs/canonico/08-INVARIANTES-CRITICOS-DE-F6.md` |
| 484 | `docs/canonico/validar-fuentes-canonicas.py` |
| 339 | `docs/evolucion/00-INDICE.md` |
| 6440 | `docs/evolucion/CHECKPOINT-ADS-NEXT.md` |
| 1006 | `docs/evolucion/verificacion/comprobar-cardinales-manuales.py` |
| 4605 | `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` |
| 1278 | `docs/evolucion/verificacion/comprobar-invariantes-criticos.py` |
| 1028 | `docs/evolucion/verificacion/comprobar-obligaciones-implementadas.py` |
| 1814 | `docs/evolucion/verificacion/comprobar-propiedades-saboteadas.py` |
| 572 | `docs/evolucion/verificacion/comprobar-universo-de-instrumentos.py` |
| 742 | `docs/evolucion/verificacion/ejercer-o26-condiciones.py` |
| 933 | `docs/evolucion/verificacion/emitir-sobre-de-ancla.py` |
| 824 | `docs/f5/validar-f5.py` |
| 526 | `docs/f6/07-VERIFICACION-FINAL-O30-20260907.md` |
| 99 | `docs/f6/08-MATRIZ-DE-LOS-CUATRO-CONTROLES-O31.md` |
| 1775 | `docs/owner/ADS-OWNER-RESOLUCIONES.md` |
| 1 | `kernel/.upstream-hash` |
| 40 | `kernel/operativo/pruebas/RECUENTOS-generado.md` |
| 48 · 49 · 12 · 12 · 33 · 189 · 407 · 80 · 923 · 15 · 79 · 17 · 139 · 146 · 122 · 27 | los **16** ficheros de `kernel/operativo/pruebas/evidencia/` del delta |
| 299 | `kernel/operativo/raiz-externa/anfitrion_firmante.py` |
| 302 | `kernel/operativo/raiz-externa/anfitrion_verificador.py` |
| 654 | `kernel/operativo/raiz-externa/instalar.py` |
| 809 | `kernel/operativo/raiz-externa/verificador.py` |
| 563 | `kernel/operativo/runtime/admision/matriz.py` |
| 628 | `kernel/operativo/runtime/admision/perimetro.py` |
| 623 | `kernel/operativo/runtime/ads_admision.py` |
| 529 | `kernel/operativo/runtime/ads_arboles.py` |
| 860 | `kernel/operativo/runtime/ads_ciclo.py` |
| 800 | `kernel/operativo/runtime/ads_estado.py` |
| 827 | `kernel/operativo/runtime/ads_runtime.py` |
| 1721 | `kernel/operativo/validadores/comprobar_evidencia.py` |
| 808 | `kernel/operativo/validadores/negativos_contratos19.py` |
| 1443 | `kernel/operativo/validadores/negativos_runtime.py` |
| 515 | `kernel/operativo/validadores/universo_de_instrumentos.py` |
| 700 | `kernel/operativo/validadores/validadores.yaml` |
| 995 | `tooling/workspace.py` |

Además, íntegros: **`O30`** y **`O31`** en la sede canónica, el registro final de `O30`
(`docs/f6/07-VERIFICACION-FINAL-O30-20260907.md`), el catálogo `K01`–`K24`
(`08-INVARIANTES-CRITICOS-DE-F6.md`), la matriz de los cuatro (`08-MATRIZ-...-O31.md`) y la
guía canónica vigente (`07-GUIA-OPERATIVA-DE-F6.md`).

**Sobre la honestidad de esta lectura.** Los prólogos `G-03`/`E-10` son byte a byte
idénticos por grupo —digest `f128a571aa06953d`, 149 líneas, en los cuatro
`raiz-externa/*.py`; digest `51247807963b0443`, 147 líneas, en los cinco
`runtime/ads_*.py`—, y lo comprobé con `sha256` antes de leerlos una vez por grupo. `T381`
exige esa identidad y pasa. No es un atajo: es que el mismo texto, verificado idéntico, no
cambia de significado al repetirse.

## 4 · Reproducción de los cuatro defectos

### 4.1 · `V-G1` sobre la base, y el estado en la candidata — el defecto SE REPRODUCE y el instrumento nuevo SÍ lo ve

Con el instrumento de la candidata corrido sobre la base de `O31` (`4d99a5e`):

```console
61 puntos ejecutables · 9 directorios · 15 sin fila ni exclusión · 0 exclusiones declaradas · 15 incumplimientos
  [U-02] `docs/canonico/validar-fuentes-canonicas.py` … NO es fila del manifiesto …
  [U-02] `docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py` …
  [U-02] `kernel/operativo/raiz-externa/verificador.py` …          (y 12 más)
rc=1
```

Sobre la candidata:

```console
62 puntos ejecutables · 9 directorios · 0 sin fila ni exclusión · 14 exclusiones declaradas · 0 incumplimientos
rc=0
```

El manifiesto pasa de **56 a 61 filas**. El defecto literal está reproducido en la base y
ausente en la candidata. **Esto, y sólo esto, es lo que el instrumento nuevo cierra.** Lo
que sigue es por qué no basta.

### 4.2 · `V-G2` · el ataque de `O31` §4.2 NO falla

`O31` §4 ordena: «Deben fallar, como mínimo: … 2. conservar el script y cambiar sus
argumentos». Lo reproduje entero, de punta a punta.

**Paso 1 · el ataque.** Sobre una copia de la candidata, a la fila `o26-impl` —la única con
`evidencia_reflexiva`— se le conserva el script y se le añaden argumentos:

```yaml
  - id: o26-impl
    script: comprobar-obligaciones-implementadas.py
    dir: docs/evolucion/verificacion
    args: ['--solo', 'CONTRATO 1']
```

**Paso 2 · el runner publica.**

```console
fila o26-impl · args declarados: ['--solo', 'CONTRATO 1']
ORDEN REAL: -I -S -E -X ads_aislado=1 docs/evolucion/verificacion/comprobar-obligaciones-implementadas.py --solo CONTRATO 1
evidencia publicada: True
# codigo:       0
  1 obligaciones medidas · 0 SIN IMPLEMENTAR · 0 faltantes individuales
```

Una obligación de **58**. Y satisface la `firma_de_exito` de la fila,
`'[1-9]\d* obligaciones medidas · 0 SIN IMPLEMENTAR · 0 faltantes'`, porque `[1-9]\d*`
admite el `1`.

**Paso 3 · el guardián.**

```console
$ python3.12 kernel/operativo/validadores/comprobar_evidencia.py
T158  SUPERADA  La evidencia publicada demuestra lo que el informe afirma
T350  SUPERADA  El estado declarado de cada escenario lo sostiene su evidencia
2 superadas · 0 fallidas
GUARDIAN rc=0
```

**Los seis ataques de §4, con la evidencia ausente y la dispensa en juego:**

```console
  CONTROL SANO · la fila legitima (debe PASAR)               rc=0  dispensa=SI   PASA (correcto)
  4.1 cambiar los argumentos a `--help`                      rc=1  dispensa=NO   FALLA (correcto)
  4.2 conservar el script y CAMBIAR SUS ARGUMENTOS           rc=0  dispensa=SI   ***PASA EN VERDE***
  4.3 conservar los argumentos y CAMBIAR EL DIRECTORIO       rc=1  dispensa=NO   FALLA (correcto)
  4.4 SEGUNDA FILA que intenta reutilizar la dispensa        rc=1  dispensa=0    FALLA (correcto)
  4.5 DUPLICAR la dispensa para otra obligacion              rc=1  dispensa=0    FALLA (correcto)
  4.6 ruta EQUIVALENTE · COPIA byte a byte en otro directorio rc=1              FALLA (correcto)
  4.6 ruta EQUIVALENTE · ENLACE SIMBOLICO al mismo fichero    rc=1              FALLA (correcto)
```

**La causa material, medida.** `O31` §4 exige ligar la dispensa a la invocación declarada
completa. La candidata construye esa identidad de siete elementos y la publica:

```console
  fila LEGITIMA                          identidad=95f8394771dfa238  dispensa=CONCEDIDA
  §4.2 args ['--solo','CONTRATO 1']      identidad=b016778935a27c28  dispensa=CONCEDIDA
  §4.2 args ['--solo','g.1']             identidad=2fb174b1b78341cc  dispensa=CONCEDIDA
```

**La identidad cambia y la dispensa se concede igual.** `identidad_de_invocacion` y
`huella_de_identidad` se calculan sólo para escribir el diagnóstico; no se comparan con
nada y por tanto no pueden denegar nada. Quien decide es `_el_declarante_mide_de_verdad`, y
su sonda es:

```python
orden = ([sys.executable, script] + list(comp.get("args") or ())
         + ["--sin-ejecutar", "--solo", obligacion])
```

Los argumentos de la fila van delante y los del juez detrás; **`argparse` se queda con el
último `--solo`**. La sonda pregunta siempre por `CONTRATO 3` y los `args:` de la fila
quedan neutralizados justo en el sitio donde tenían que decidir. El `--help` sí cae, porque
`argparse` imprime la ayuda y sale antes de medir: se corrigió el vector que `O30` nombró,
no la clase.

Y por el otro extremo la firma de éxito tampoco acota: `[1-9]\d*` admite que la corrida
mida una obligación de cincuenta y ocho. **El aparato es ciego a los `args` de la fila en
las dos puertas, la de la dispensa y la del veredicto.**

Sobre §4.6: bajo la lectura fuerte —una copia byte a byte o un enlace simbólico en otra
ruta— el ataque **sí** falla, correctamente. Bajo la lectura débil —`./docs/…`, `docs/…/`,
`docs/evolucion/../evolucion/…`— la dispensa se concede, pero esas escrituras designan
literalmente la misma ruta y normalizarlas es lo correcto. **No cuento §4.6 como fallo.** El
fallo es §4.2, y basta.

### 4.3 · `M-04` · el duodécimo árbol

`O31` §5 prescribe: retirar del manifiesto el instrumento de `K01`–`K24`, retirar su
evidencia, regenerar huella y sello, correr la batería completa. Lo hice, dos veces.

**(a) El ataque literal de §5, tal cual:**

```console
### CON LA MARCA `FUERA_DEL_MANIFIESTO_DE_VALIDADORES`: NO
      universo-de-instrumentos (`O31` §3/§5)   rc=1  ROJO   [U-02] `docs/evolucion/verificacion/comprobar-invariantes-criticos.py` es un punto ejecutable del árbol y NO es fila del manifiesto…
      integridad  (huella y sello)             rc=0  VERDE
      evidencia   (T158/T350)                  rc=1  ROJO   T158  FALLIDA
      recuentos · referencias · versiones · fuentes · cardinales-manuales   rc=0  VERDE
```

**El ataque literal produce rojo, y por el motivo correcto.** Lo digo primero porque
favorece a la candidata y porque es verdad.

**(b) El mismo ataque, más una línea de texto dentro del propio instrumento retirado:**

```python
FUERA_DEL_MANIFIESTO_DE_VALIDADORES = "instrumento de diagnostico del catalogo K01-K24"
```

```console
### CON LA MARCA `FUERA_DEL_MANIFIESTO_DE_VALIDADORES`: SI
      universo-de-instrumentos (`O31` §3/§5)   rc=0  VERDE
      integridad  (huella y sello)             rc=0  VERDE
      evidencia   (T158/T350)                  rc=0  VERDE
      recuentos · referencias · versiones · fuentes · cardinales-manuales   rc=0  VERDE
```

**Ocho de ocho en verde**, con el instrumento que mide `K01`–`K24` fuera del aparato, su
evidencia borrada, y huella y sello regenerados. Es el duodécimo árbol de `M-04`, vivo, con
un paso más que el que `O31` §5 enumera.

**La única defensa, y por qué cede.** El código conoce este ataque —lo escribe: «UN CRÍTICO
ADVERSARIAL LO VIO ANTES DE QUE ESTO SE PUBLICARA»— y lo defiende contrastando contra el
manifiesto confirmado en `HEAD`:

```python
if declaradas_en_head is not None and ruta in declaradas_en_head:
    exclusiones_ilegitimas.append((ruta, "`HEAD` la declara como fila del manifiesto…"))
```

Y razona: *«Quien quiera vaciar el universo tendría que reescribir la historia, que está
prohibido y es detectable.»* **Es falso, y lo medí:**

```console
  fila retirada + marca escrita · commit ORDINARIO=NO  -> rc=1  [U-02] … reclama `FUERA_DEL_MANIFIESTO_DE_VALIDADORES` y no puede
  fila retirada + marca escrita · commit ORDINARIO=SI  -> rc=1  [U-09] … (con la evidencia aún presente)
  fila + evidencia retiradas + marca · commit ORDINARIO=SI  -> rc=0  VERDE
```

**Un commit corriente basta.** No hay que reescribir nada: en cuanto la retirada está
confirmada, `HEAD` ya no declara la fila y la marca se acepta. El propio fichero lo admite
doce líneas más abajo, en el comentario de `U-09`: *«Una retirada deliberada se hace en el
mismo commit que la evidencia, y entonces `HEAD` ya no la tiene.»* Las dos frases están en
el mismo módulo y se contradicen. La segunda es la verdadera.

La frontera no la decide la historia: la decide **el commit anterior**, que lo escribe la
misma mano.

### 4.4 · `C-L.7` · la clase, atacada con variantes nuevas

`O31` §6 me exige demostrarlo «con variantes que el implementador no utilizó». El sobre me
entrega enteras las 33 suyas. **Ninguna de las mías aparece en esa lista.** Todas se crearon
después de recibir la candidata, se inyectan en un campo VIGENTE de la sede viva real
(`docs/evolucion/CHECKPOINT-ADS-NEXT.md`, campo `freshness`) y se juzgan con el instrumento
real.

**Control positivo — la forma clásica, que el control tiene que cazar:**

```console
  CAZADA  rc=1  forma clasica   «quedan 24 invariantes vivos en el catalogo»
                                 -> cardinal `24` cuantificando `invariantes`
```

**Mis variantes nuevas:**

```console
  ESCAPA  rc=0  V1  sufijo -ia en la linea        «la evidencia recoge 24 invariantes del catalogo»
  ESCAPA  rc=0  V2  sustantivo singular antes     «el total 24 invariantes siguen satisfechos»
  ESCAPA  rc=0  V3  signo de igualdad             «invariantes satisfechos = 24»
  CAZADA  rc=1  V4  flecha de derivacion          «invariantes satisfechos -> 24»
  CAZADA  rc=1  V5  porcentaje                    «el 100 % de los 24 invariantes siguen satisfechos»
  ESCAPA  rc=0  V6  cardinal en ingles            «24 invariants are still satisfied»
  ESCAPA  rc=0  V7  romano en minusculas          «xxiv invariantes siguen satisfechos»
  ESCAPA  rc=0  V8  separador de millar           «el corpus obligatorio suma 100.910 lineas»
  CAZADA  rc=1  V9  colectivo compuesto           «dos docenas de invariantes siguen satisfechos»
  CAZADA  rc=1  V10 cardinal entre parentesis     «invariantes satisfechos (24) y ninguno incumplido»
  CAZADA  rc=1  V11 unidad interpuesta            «24 uds. de invariantes siguen satisfechas»
  CAZADA  rc=1  V12 cardinal tras dos puntos      «invariantes: 24 satisfechos»

  ESCAPA  rc=0  G1  «la vigencia cubre 58 obligaciones internas de la fase»
  ESCAPA  rc=0  G2  «la auditoria alcanzo 57 sabotajes declarados»
  ESCAPA  rc=0  G3  «el catalogo 24 invariantes queda cerrado»
  ESCAPA  rc=0  G4  «el conjunto 58 obligaciones queda cerrado»
  ESCAPA  rc=0  H1  «la referencia fija 8 condiciones de `O26` satisfechas»
```

**Once variantes nuevas de la clase escapan.** Y no por casualidad: aislé cada mecanismo con
**pares mínimos**, en los que la única diferencia es la subrayada.

```console
  CAZADA  A1 control                 «quedan 24 invariantes vivos en el catalogo»
  ESCAPA  A2 + palabra en -ia        «quedan 24 invariantes vivos en la evidencia»

  CAZADA  B1 sustantivo PLURAL       «los totales 24 invariantes siguen satisfechos»
  ESCAPA  B2 sustantivo SINGULAR     «el total 24 invariantes siguen satisfechos»

  CAZADA  C1 sin igualdad            «invariantes satisfechos son 24»
  ESCAPA  C2 con igualdad            «invariantes satisfechos = 24»

  CAZADA  D1 romano MAYUSCULAS       «XXIV invariantes siguen satisfechos»
  ESCAPA  D2 romano minusculas       «xxiv invariantes siguen satisfechos»

  CAZADA  E3 sin separador           «el corpus obligatorio ocupa hoy 100910 lineas»
  ESCAPA  E4 con separador           «el corpus obligatorio ocupa hoy 100.910 lineas»
  CAZADA  E5 sin separador, directo  «100910 lineas obligatorias en el corpus»
  ESCAPA  E6 con separador, directo  «100.910 lineas obligatorias en el corpus»

  CAZADA  F1 sustantivo espanol      «24 invariantes are still satisfied»
  ESCAPA  F2 sustantivo ingles       «24 invariants are still satisfied»
```

**Cinco mecanismos independientes, cada uno contra una exigencia literal de `O31` §6:**

1. **Una sola palabra terminada en `-ia` exime la línea entera.** El regex de narración es
   `(?:fue|fueron|…|[a-z]{2,}(?:aron|ieron|aba|abas|aban|ia|ian))`, y `ia` casa con
   *evidencia, vigencia, auditoria, referencia, materia, historia, copia, guia*… Es el
   vocabulario propio de este corpus. No es un caso de esquina: es la mitad del diccionario
   del proyecto.
2. **Un sustantivo SINGULAR delante del cardinal lo exime** — «el total 24», «el catalogo
   24», «el conjunto 58». §6 exige reconocer **singular y plural**.
3. **Un `=` delante lo exime.** La regla existe para la salida generada; sirve igual para
   copiar estado a mano.
4. **El numeral romano en minúsculas escapa** mientras el mismo en versales se caza. §6
   exige **mayúsculas y minúsculas**.
5. **El separador de millar exime cualquier cardinal ≥ 1000** — `100.910` escapa, `100910`
   se caza. §6 exige **cifras escritas con dígitos** y exige distinguirlas de **versiones**;
   `100.910` no es una versión.

Y un sexto: **un sustantivo que no es español escapa**, contra la exigencia de reconocer
**sustantivos desconocidos**.

El control juzga instancias afinadas sobre este árbol, no la clase. Sus excepciones no son
principios: son parches con efectos colaterales que no se midieron.

## 5 · Sección C · lo verificado

| comprobación | resultado |
|---|---|
| `fd633383001d1e755e071195f9ab69e41a04926f` ancestro de HEAD | `git merge-base --is-ancestor` → **rc=1 · NO es ancestro** ✓ (vive sólo en `origin/fix/f4c-correccion-doce-hh2-post-o21-20260901`) |
| Sede del Owner append-only | base es **prefijo exacto** de la candidata (52 570 → 69 490 bytes, **0 líneas borradas**); `O17`…`O30` byte a byte; sólo se añade `O31` ✓ |
| Material protegido tocado | **ninguno**. Ni gates históricos, ni dictámenes, ni manifiestos publicados, ni enmiendas, ni contratos inmutables, ni documentos aprobados. Único fichero con «gate» en el nombre tocado: `comprobar-correccion-gate-de-cierre.py`, y sólo con **+11 líneas** de declaración al final, sin tocar su lógica ni su veredicto ✓ |
| `redesign/kernel-2.0` | no existe en el árbol; no tocado ✓ |
| PesquerApp iniciada | **no**. Las 8 menciones del delta están **todas** en `docs/owner/ADS-OWNER-RESOLUCIONES.md`, es decir, en el texto de `O31`. No hay repositorio ADS de PesquerApp: ni `kernel/operativo/`, ni `SOURCES.toml`, ni `ads/` en `la-pesquerapp` ni en `lapesquerapp-backend` ✓ |
| Universo vaciado por reclasificación | **no**. Todos los cardinales igualan o superan a los de `O30`: filas del manifiesto 56 → **61**; puntos sin fila 15 → **0**; `K01`–`K24` 24 = 24; sabotajes 57 = 57; catalogados 115 = 115; negativos 200 = 200; obligaciones 58 = 58; propiedades críticas 346 = 346; fuentes obligatorias 94 = 94; `O26` 8/8 = 8/8 ✓ |
| Guía canónica como segunda sede de estado | **no**. `07-GUIA` remite explícitamente: «La sede del estado de las fases es `03-GOBIERNO-Y-AUTORIDAD.md` §6… escribirlo aquí crearía una segunda sede mutable» ✓ |
| Declaración prematura | **ninguna**. `03-GOBIERNO` §6 sigue diciendo `F6` **ABIERTA · NO CERTIFICADA**, `M-04` **NO SUPERADA**, `C-L.7` **NO CERRADA**, PesquerApp **BLOQUEADA**. `08-MATRIZ` dice de sí misma «No es una certificación», y `CHECKPOINT` regla 7: «NINGUNO DE LOS COMANDOS CIERRA `C-L.7`». La candidata no se certifica a sí misma ✓ |
| Menores anteriores | `V-M1`…`V-M4`, `CD-7` y el nuevo `CD-8` registrados en `06-DEUDA` §11 bis/§11 ter, **ninguno declarado superado** ✓ |

### Regresiones del delta — ninguna

```console
kernel.operativo.runtime.pruebas.test_integridad_y_evidencia   Ran 63 tests   OK   rc=0
kernel.operativo.runtime.pruebas.test_admision                 Ran 101 tests  OK   rc=0
kernel.operativo.runtime.pruebas.test_raiz_externa             Ran 53 tests   OK   rc=0
tooling.tests.test_workspace                                   Ran 57 tests   OK   rc=0
docs/canonico/validar-fuentes-canonicas.py                     0 fallos            rc=0
comprobar_integridad · comprobar_evidencia · comprobar_recuentos ·
comprobar_referencias · comprobar_versiones · comprobar_fuentes ·
comprobar-universo-de-instrumentos (+autopruebas) ·
comprobar-cardinales-manuales (+autopruebas)                                       rc=0
```

`T380`/`T381` verdes: los prólogos `G-03` siguen siendo byte a byte idénticos pese a las
catorce declaraciones nuevas.

## 6 · `O31` §2 · los hechos conservados, reproducidos por mí sobre la candidata

```console
$ comprobar-invariantes-criticos.py
  LOS INCUMPLIMIENTOS, UNO A UNO
    ninguno
  24 invariantes medidos · 24 SATISFECHOS · 0 INCUMPLIDOS · 57 sabotajes declarados ·
  57 ejercidos · 115 catalogados · 59 no seleccionados · 0 sin detectar     rc=0

$ comprobar-obligaciones-implementadas.py
  FALTANTES, UNO A UNO — ninguno
  58 obligaciones medidas · 0 SIN IMPLEMENTAR · 0 faltantes individuales
  `O26` §5.1 · ACREDITADA por este instrumento                              rc=0

$ ejercer-o26-condiciones.py
  8 de 8 condiciones SATISFECHAS · 0 no ejercibles · 0 no satisfechas       rc=0
```

Mi corrida de `K01`–`K24` difiere de la evidencia publicada **sólo** en la línea `ANCLA` y
en un digest interno de `NS21a`, los dos consecuencia de que el árbol avanzó dos commits.
Los 24 invariantes, los 57 sabotajes y los cero incumplimientos son idénticos.

Hechos 4 (identidad de la candidata de `O30`), 5 (PesquerApp no iniciada) y 6 (menores
registrados, ninguno superado): verificados arriba. **Los seis hechos conservados de `O31`
§2 no sufren regresión.**

## 7 · Hallazgos

### BLOQUEANTES

**`B-01` · La dispensa reflexiva sigue siendo transferible por los argumentos de la fila.**
*Sede:* `kernel/operativo/validadores/comprobar_evidencia.py`,
`_el_declarante_mide_de_verdad` (la sonda) y `validadores.yaml`, `firma_de_exito` de
`o26-impl`.
*Hecho:* `args: ['--solo','CONTRATO 1']` obtiene la dispensa —con la identidad de
invocación cambiada— y, con la evidencia republicada por el runner, deja `T158 SUPERADA ·
T350 SUPERADA · 2 superadas · 0 fallidas · rc=0` sobre una evidencia que mide **1 obligación
de 58**. La identidad de siete elementos de §4 se calcula y se publica, pero no admite ni
deniega nada.
*Remedio:* comparar la identidad de invocación **antes** de conceder, no después de
decidir; y sustituir `[1-9]\d*` por el cardinal derivado del universo.
*Propietario:* `PLT` implementa · `SIS` propietario. *Fase:* `F6`.
*¿Afecta a una condición de §7?* **Sí — condición 2.** *¿Regresión del delta?* **No.**

**`B-02` · El control de `C-L.7` juzga instancias, no la clase.**
*Sede:* `docs/evolucion/verificacion/comprobar-cardinales-manuales.py` — regex `PASADO`,
regla del sustantivo singular anterior, regla del `=`, tratamiento de romanos y excepción
tipada `VERSION`.
*Hecho:* **once variantes nuevas** de la clase, creadas después de recibir la candidata,
escapan; cinco mecanismos aislados con pares mínimos; cada uno contradice una exigencia
literal de §6.
*Remedio:* anclar la narración en pasado a verbos reales y no a un sufijo; retirar la
exención por sustantivo singular; acotar la excepción `VERSION` a formas con dos o más
separadores; plegar mayúsculas antes de reconocer romanos; y probar cada excepción contra
un falso negativo, no sólo contra un falso positivo.
*Propietario:* `PLT` implementa · `SIS` propietario. *Fase:* `F6`.
*¿Afecta a una condición de §7?* **Sí — condición 4.** *¿Regresión del delta?* **No.**

**`B-03` · La marca de exclusión retira del universo el instrumento que mide `K01`–`K24`, y
basta un commit corriente.**
*Sede:* `kernel/operativo/validadores/universo_de_instrumentos.py`, la rama
`declaradas_en_head` y la constante `MARCA_DE_EXCLUSION`.
*Hecho:* con el ataque de §5 más una línea de texto en el fichero retirado, **ocho de ocho
controles quedan en verde** con el instrumento de `K01`–`K24` fuera del aparato y su
evidencia borrada. La defensa se apoya en el manifiesto de `HEAD`, es decir, en el mismo
manifiesto cuya completitud se juzga, un commit antes. El comentario que dice «tendría que
reescribir la historia» es falso y el propio módulo lo desmiente en `U-09`.
*Remedio:* la legitimidad de una exclusión no puede depender de `HEAD`; hay que derivarla
de una sede independiente del manifiesto —una clase canónica, un censo de
`FUENTES-CANONICAS.yml`— o exigir que toda retirada del aparato quede refrendada por un
acto separado y firmado.
*Propietario:* `PLT` implementa · `SIS` propietario. *Fase:* `F6`.
*¿Afecta a una condición de §7?* **Sí — condiciones 1 y 3.** *¿Regresión del delta?* **No**
(la base no tenía este aparato en absoluto).

### GRAVES

**`G-01` · El contraste de `argumentos` que `O31` §3 enumera no existe.**
*Sede:* `docs/evolucion/verificacion/comprobar-universo-de-instrumentos.py`. §3 exige
contrastar por fila «identificador; ejecutable; directorio de trabajo; **argumentos**;
evidencia; condición de éxito; inclusión en el runner; inclusión en el guardián». Siete se
comprueban (U-03, U-04, U-05, U-06, U-07). **`args` sólo aparece en el fichero como
variable local de `argparse`**; ninguna condición lo contrasta con nada. Es justamente el
campo que `B-01` explota.
*Remedio:* añadir una condición que contraste los `args:` declarados con la línea
`# orden:` de la evidencia publicada.
*Propietario:* `PLT`/`SIS`. *Fase:* `F6`. *¿Afecta a §7?* **Sí — condición 1.**
*¿Regresión?* **No.**

**`G-02` · El «guardián mecánicamente equivalente» no es equivalente, y hay dos cifras
caducadas vivas que lo prueban.**
*Sede:* `comprobar-universo-de-instrumentos.py`, `U-07`. Diecisiete evidencias no las
alcanza `T350` y las sostiene «el equivalente de `O31` §3», que comprueba que los bytes del
árbol coincidan con el blob de `HEAD`. Eso detecta una edición a mano; **no detecta que lo
publicado haya dejado de ser cierto**. Medido, regenerando cada instrumento sobre la
candidata:

```console
universo-obligaciones-salida.txt:
  publica:  06-DEUDA-Y-LIMITACIONES-VIGENTES.md   25d0b47c048f4f66   583 líneas
  el árbol: 06-DEUDA-Y-LIMITACIONES-VIGENTES.md   010c66a93bcdf210   584 líneas
cardinales-manuales-salida.txt:
  publica:  … 341 núcleos derivados por otra sede
  el árbol: … 344 núcleos derivados por otra sede
```

`T158` y `T350` quedan en verde sobre las dos. Es la clase exacta de `H-08` y `N158g` —«la
cobertura publicada describe un corpus distinto del vigente»— sin regla de `vigencia` que la
cubra.
*Remedio:* declarar `vigencia` para los bloques de PROCEDENCIA y para los cardinales
derivados de estas evidencias, o exigir que toda evidencia se regenere en el commit que la
contiene.
*Propietario:* `PLT`/`SIS`. *Fase:* `F6`. *¿Afecta a §7?* **Sí — condiciones 1 y 9.**
*¿Regresión?* **No.**

### MENORES

- **`m-01`** · El comentario de `universo_de_instrumentos.py` afirma que vaciar el universo
  exigiría reescribir la historia; es falso y el mismo módulo lo contradice en `U-09`.
  *Remedio:* corregir la afirmación. `SIS` · `F6`. No afecta a ninguna condición por sí solo.
- **`m-02`** · `V-M2` persiste: el sobre invoca «`O31` §6» y «§9» como amparo de relevos que
  esas secciones no conceden (§6 es `C-L.7`), y transcribe `contrastados 254` donde el árbol
  publica `255`. El sobre vive fuera del repositorio. `VER` · `F6`.
- **`m-03`** · `07-GUIA-OPERATIVA-DE-F6.md` §14 sigue enumerando las **ocho** condiciones de
  `O30` §7 y no las **nueve** de `O31` §7. No es sede de estado y remite correctamente, así
  que no crea segunda sede; es desactualización. `SIS` · `F6`.
- **`m-04`** · El sobre afirma que el ataque de `M-04` sobre la candidata «produce ROJO por
  `U-09`»; mi reproducción lo produce por **`U-02`**. Rojo en ambos casos; difiere la
  condición citada. `VER` · `F6`.
- **Menores anteriores** `V-M1`, `V-M2`, `V-M3`, `V-M4`, `CD-7` y `CD-8`: registrados,
  ninguno declarado superado, ninguno falsea una condición de §7. **No bloquean.**

## 8 · Las nueve condiciones de `O31` §7, una a una

**1 · `V-G1` queda cerrada — NO.** El defecto literal está cerrado: el universo se deriva
del árbol entero con `ast`, no de un glob, y los 15 puntos que la base tenía fuera están
ahora dentro o declarados. Pero §3 no se agota ahí. Exige que omitir un instrumento
«produzca rojo por su ausencia material, **no por una lista manual de rutas**»: `B-03`
demuestra que omitirlo produce **verde** si se acompaña de una declaración manual escrita en
el propio fichero, y que su única defensa cede ante un commit corriente. La lista manual no
ha desaparecido: se ha mudado del juez al juzgado. Exige contrastar los **argumentos** de
cada fila: `G-01` demuestra que ese contraste no existe. Y exige que todo instrumento que
sostenga una condición de certificación esté protegido por `T350` o por un guardián
**mecánicamente equivalente**: `G-02` demuestra que el sustituto no lo es, con dos cifras
caducadas vivas.

**2 · `V-G2` queda cerrada — NO.** `O31` §4.2 nombra el ataque con esas palabras y ordena
que falle. No falla: concede la dispensa con la identidad cambiada y, con la evidencia
republicada, deja toda la cadena en verde sobre una medición de una obligación de cincuenta
y ocho. La identidad de invocación de siete elementos está construida y publicada, pero es
decorativa.

**3 · `M-04` queda superada — NO.** El ataque literal de §5 **sí** produce rojo por el
motivo correcto, y lo hago constar. Pero §5 dice «se acreditará **únicamente si**», no «se
acredita siempre que»; y la deuda que `M-04` nombra es «un árbol defectuoso puede pasar en
verde». He construido ese árbol: instrumento de `K01`–`K24` fuera del aparato, evidencia
borrada, huella y sello regenerados, **ocho de ocho validadores en verde**. El defecto que
`M-04` nombra está vivo en la candidata.

**4 · `C-L.7` queda cerrada — NO.** §6 me reserva el cierre y me exige demostrarlo con
variantes que el implementador no usó. Aporté once que escapan, con cinco mecanismos
aislados por pares mínimos, cada uno contra una exigencia literal de §6.

**5 · `K01`–`K24` continúan satisfechas — SÍ.** 24 medidos, 24 satisfechos, 0 incumplidos,
57 sabotajes ejercidos, 0 sin detectar. Reproducido por mí.

**6 · Las obligaciones internas continúan completas — SÍ.** 58 medidas, 0 sin implementar, 0
faltantes. Las tres restas del universo derivado en cero. Reproducido por mí.

**7 · Las ocho condiciones de `O26` continúan satisfechas — SÍ.** 8 de 8, 0 no ejercibles, 0
no satisfechas, sobre el perfil de anfitrión declarado. Reproducido por mí.

**8 · No existe regresión BLOQUEANTE o GRAVE introducida por el delta — SÍ, no existe.** Las
274 pruebas de las cuatro baterías tocadas por el delta pasan; los ocho validadores del
corpus pasan sobre la candidata intacta; ningún cardinal encoge; ningún material protegido
se toca; la sede del Owner es estrictamente append-only. Los cinco hallazgos de arriba **no
son regresiones**: son fallos de aparato nuevo al cerrar lo que se construyó para cerrar. La
candidata es mejor que su base. No basta, porque §7 exige las nueve.

**9 · Commit, tree, evidencia y sobre corresponden al mismo objeto — NO, en sentido
estricto.** La cadena de identidad está intacta y lo digo con precisión: el sobre nombra
`697eab9c` / `92f7e0df`, que es el checkout congelado; su firma verifica; sus digests
cuadran; `comprobar_integridad` da verde en las cuatro comprobaciones; `T350` ejerce el
contraste contra el blob de `HEAD` con **0 divergencias**. Lo que no corresponde es el
**contenido** de la evidencia: `universo-obligaciones-salida.txt` publica un digest y un
recuento de líneas que el árbol candidato desmiente, y `cardinales-manuales-salida.txt`
publica `341` donde el árbol deriva `344` (`G-02`). Los tres ficheros anclan además a
`6ce736aa`, dos commits antes. Si se lee §7.9 como identidad, se satisface; si se lee como
correspondencia —y «corresponden» es la palabra—, no. Lo registro como GRAVE y no como
bloqueante porque **ningún veredicto cambia**: los reproduje todos hoy y salen igual. En
cualquiera de las dos lecturas el resultado final no varía, porque las condiciones 1, 2, 3 y
4 fallan por su cuenta.

## 9 · Límites de este dictamen

- No regeneré `negativos-salida.txt` ni `o26-sab-salida.txt` sobre la candidata: cuestan
  horas. Los leí íntegros y verifiqué que sus veredictos —200/0 y 346/283— coinciden con los
  de la candidata de `O30`. No puedo afirmar que sus cifras internas sean vigentes byte a
  byte hoy; sí que su sustancia no ha cambiado.
- No ejecuté las 21 baterías completas del runner. Ejecuté las cuatro que el delta toca y
  los ocho validadores del corpus.
- No juzgo si la adscripción de cada propiedad a su `Knn` es la correcta: juzgo que el
  vínculo está declarado y que la ejecución lo confirma, que es lo que el instrumento mide.
- Mi juicio sobre el sobre se limita a lo que él dice demostrar. No le atribuyo anterioridad
  y no la necesito: los tres bloqueantes los reproduje yo, sobre copias del árbol, con
  órdenes transcritas.
- No amplié el universo por preferencias documentales, cifras históricas ni deuda externa.
  `CD-7`, `CD-8` y los cuatro `V-M` quedan donde estaban.
- No corregí nada. No creé commits ni referencias. El checkout congelado sigue limpio.

## 10 · DECLARACIONES

**COBERTURA INTEGRAL**

**V-G1 NO CERRADA**

**V-G2 NO CERRADA**

**M-04 NO SUPERADA**

**C-L.7 NO CERRADA**

**K01–K24 CONTINÚAN SATISFECHAS**

**OBLIGACIONES INTERNAS DE F6 CONTINÚAN COMPLETAS**

**OCHO CONDICIONES DE O26 CONTINÚAN SATISFECHAS**

**F6 NO CERTIFICADA**

**F6 ABIERTA**

**PESQUERAPP SIGUE BLOQUEADA · NO INICIADA**

---

Conforme a `O31` §9: se registra la causa material, no se corrige en respuesta a este
dictamen, no se abre otro gate y no se inicia otro ciclo automático. La decisión posterior
es estrictamente humana.

**La causa material, en una línea:** el delta construyó los cuatro instrumentos que `O31`
pedía y los tres que deciden —el universo, la dispensa y el control de clase— tienen cada
uno una puerta abierta que un adversario cruza con una línea de texto, una lista de
argumentos o una palabra terminada en `-ia`.

---

*Fin del dictamen transcrito.*

## 4 · Lo que el coordinador deja dicho, y lo que no hace

**No corrige nada.** `O31` §9 lo prohíbe expresamente después del dictamen, y los tres
BLOQUEANTES y los dos GRAVES quedan REGISTRADOS y sin remedio aplicado. Su clasificación es
del verificador, no del coordinador.

**Lo que este ciclo sí consiguió, dicho sin inflarlo.** Es la **primera cobertura integral**
del expediente: 56 de 56 ficheros modificados desde `a672ed9` leídos enteros, resta vacía,
demostrada mecánicamente. Los tres gates anteriores fueron declarados NO VÁLIDOS por
cobertura y el de `O30` la dejó incompleta por su propia declaración —14 de 30 sin leer
enteros—. El defecto literal de `V-G1` está cerrado y el verificador lo confirma: el
universo se deriva del árbol con `ast` y los quince puntos que la base tenía fuera están
dentro o declarados; el manifiesto pasa de 56 a 61 filas. El ataque literal de `M-04` §5
produce rojo por el motivo correcto. Los cuatro ataques de `O31` §4 distintos del §4.2 caen.
Ningún cardinal del universo encoge, ninguna regresión, ningún material protegido tocado.

**Lo que este ciclo NO consiguió, dicho igual de claro.** `F6` no queda certificada. Los
tres instrumentos que deciden tienen cada uno una puerta abierta, y el verificador las cruzó
las tres. La más instructiva es `B-03`: la marca de exclusión que este ciclo introdujo para
declarar lo que no es un validador se defendía contrastando contra el manifiesto de `HEAD`,
y el propio módulo escribía que vaciarlo «exigiría reescribir la historia». Era falso, y el
mismo fichero lo desmiente doce líneas más abajo. Un commit corriente basta. **La lista
manual no desapareció: se mudó del juez al juzgado**, y eso es exactamente lo que `O31` §3
prohíbe.

**Sobre `C-L.7`.** El control pasa sus 33 autopruebas y los doce ataques de `O31` §6, y
falla ante once variantes nuevas. La lección es del verificador y se recoge entera: sus
exclusiones —narración, referencia, campo de registro, ordinal, fórmula— no son principios
sino parches, y cada una se midió contra el falso positivo que estorbaba sin medirla contra
el falso negativo que abría.

**`O31` §10 · parada definitiva.** Esta intervención permitía una implementación, una
comprobación adversarial previa, una única pasada de corrección, una candidata, un sobre, un
verificador y un resultado. Todo eso se hizo, y el resultado está registrado y publicado.
**Se para.** Lo que siga es, en palabras de `O31` §9, «estrictamente humano: aceptar el
riesgo, intervenir manualmente o detener el desarrollo del sistema».
