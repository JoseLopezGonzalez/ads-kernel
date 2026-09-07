# `O30` · VERIFICACIÓN INDEPENDIENTE FINAL DE `F6` — 2026-09-07

> **Qué es este documento.** El registro final que `O30` §14 manda escribir después del
> dictamen del verificador independiente. Contiene el objeto juzgado, la identidad del
> verificador, su cobertura, los comandos y resultados, sus declaraciones literales, sus
> hallazgos, su razonamiento, sus límites y el estado final.
>
> **Qué NO es.** No es una corrección. `O30` §10 es terminante: después del dictamen no se
> corrige la candidata, no se abre otro gate, no se propone otra tanda y no se inicia
> PesquerApp. Este documento se escribe **encima** de la candidata congelada y no la toca.
>
> **Autoridad.** El dictamen es del verificador, no del coordinador. Se transcribe íntegro
> y sin edición. Donde el coordinador tiene algo que decir, se dice en §4 y se dice que es
> del coordinador.

## 1 · OBJETO Y REFERENCIAS

```text
base del encargo   a672ed95686a37b5862f4486a5699bdcebb0f7fd
candidata          60b640db1762e1623af2371126de01ce1c0d0b88
tree               40c66896669c4dba1ae20e68b1fbf1a6e0073fef
publicada en       review/f6-o30-final-candidate-20260906
resultado en       review/f6-o30-final-insuficiente-20260906

sobre de ancla     /home/jose/ads-sobre-o30/sobre-o30.json
  sha256           0194000c96858e7e63eb721a83d367e8480e8e067ae0222e889f882a7196ec3c
  firma            sobre-o30.json.sig, principal `ancla-o30@ads`, clave privada DESTRUIDA
  emitido          FUERA del repositorio, DESPUÉS de publicar la candidata y ANTES de
                   crear al verificador

checkout del verificador   /home/jose/ads-verificacion-o30, HEAD desprendido en la
                           candidata, árbol limpio antes y después
```

**Sede del estado de fase:** [`03-GOBIERNO-Y-AUTORIDAD.md`](../canonico/03-GOBIERNO-Y-AUTORIDAD.md)
§6. Este documento **no la duplica**: registra el veredicto y remite.

**Sede de `M-04` y `C-L.7`:**
[`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md).

## 2 · ESTADO FINAL REGISTRADO — `O30` §14

```text
F6 NO CERTIFICADA
F6 ABIERTA · INICIADA · EN CURSO
M-04 NO SUPERADA          (estado literal emitido por el verificador)
C-L.7 NO CERRADA          (estado literal emitido por el verificador)
PESQUERAPP SIGUE BLOQUEADA · NO INICIADA
```

**Causa material exacta.** Fallan tres de las ocho condiciones de `O30` §7 —la 4, la 5 y
la 6— y cada una basta por sí sola.

## 3 · DICTAMEN DEL VERIFICADOR, TRANSCRITO ÍNTEGRO

> El texto que sigue es del verificador independiente final. No se ha editado, resumido ni
> reordenado.

---

# DICTAMEN DEL VERIFICADOR INDEPENDIENTE FINAL DE `O30`

## 1 · OBJETO EXACTO JUZGADO, VERIFICADO POR MÍ

```text
commit   60b640db1762e1623af2371126de01ce1c0d0b88
tree     40c66896669c4dba1ae20e68b1fbf1a6e0073fef
checkout /home/jose/ads-verificacion-o30   ·  git status --porcelain → 0 líneas
base del encargo   a672ed95686a37b5862f4486a5699bdcebb0f7fd  ·  30 ficheros modificados
```

`git rev-parse HEAD` y `HEAD^{tree}` coinciden **exactamente** con `4_candidata` del sobre
y con `DIGEST.txt`. El árbol está limpio: nada de lo que juzgo es trabajo sin confirmar.

**Sobre de ancla.** Firma comprobada por mí con el propio `firma.exigir_firma_valida`
contra el principal `ancla-o30@ads` → **`FIRMA VÁLIDA`**. `sha256(sobre-o30.json)` =
`0194000c96858e7e63eb721a83d367e8480e8e067ae0222e889f882a7196ec3c`, idéntico al publicado.
El texto literal de `O30` del sobre tiene `sha256 d8ab5eb8…`, **y ése es exactamente el
hash del bloque `O30` extraído de la sede del Owner en la candidata**: el sobre no describe
la resolución, la contiene byte a byte. Además comprobé que `6_catalogo_K01_K24` ==
`docs/canonico/08-INVARIANTES-CRITICOS-DE-F6.md` (38 121 bytes, idénticos),
`10_manifiesto` == `validadores.yaml` (30 597 bytes, idénticos), `11_guia_canonica.sha256`
== sha256 real de la guía, y que las matrices `7` y `8` están contenidas literalmente en
sus evidencias.

## 2 · MI IDENTIDAD Y POR QUÉ SOY INDEPENDIENTE

No he intervenido en este expediente. No soy el coordinador, ni ninguno de los agentes de
construcción, ni el auditor previo que emitió `B1` y `G1`–`G4`. No he escrito ni corregido
una línea de la candidata. Trabajé sobre un checkout congelado que **no modifiqué** (0
líneas de `git status` al principio y al final), no creé commit, rama, tag ni referencia
alguna, y no toqué `/home/jose/ads-kernel` salvo para leer. Todos mis sabotajes viven en
copias bajo `/tmp/v30/`.

## 3 · COBERTURA · LO QUE LEÍ ENTERO, LO QUE NO, Y LA RESTA

**Leídos ÍNTEGRAMENTE (16 de 30):** `.sello-producto` · `kernel/.upstream-hash` ·
`docs/canonico/00-EMPEZAR-AQUI.md` · `06-DEUDA-Y-LIMITACIONES-VIGENTES.md` ·
`07-GUIA-OPERATIVA-DE-F6.md` · `08-INVARIANTES-CRITICOS-DE-F6.md` · y las evidencias
`fuentes` · `integridad` · `invariantes-criticos-autopruebas` · `o26-condiciones` ·
`recuentos` · `referencias` · `universo-obligaciones` · `universo-rutas` · `versiones`. De
`docs/owner/ADS-OWNER-RESOLUCIONES.md` leí íntegra la entrada `O30` y la cabecera de
reglas, y verifiqué mecánicamente el resto (ver §5.A).

**NO leídos de extremo a extremo (14 de 30)** — de todos ellos leí el **diff completo**
contra la base y porciones sustanciales, y los ejercí ejecutándolos:
`docs/evolucion/00-INDICE.md` (113 KB; diff de 2 líneas leído entero) ·
`comprobar-invariantes-criticos.py` (1278) · `comprobar-obligaciones-implementadas.py`
(1028) · `comprobar-propiedades-saboteadas.py` (1814) · `ejercer-o26-condiciones.py` (742)
· `matriz.py` (563) · `perimetro.py` (628) · `comprobar_evidencia.py` (1589; ~950 leídas) ·
`negativos_contratos19.py` (808) · `negativos_runtime.py` (1443) · `validadores.yaml` (639)
· y las evidencias `invariantes-criticos` (reproducida entera por mí) · `negativos` (407) ·
`o26-sab` (923).

> **`MODIFICADO − LEÍDO ≠ ∅`.** La resta contiene las 14 entradas de arriba. **Lo digo y no
> lo maquillo.** Razón: 16 274 líneas de corpus modificado, de las que leí íntegras las 16
> sedes normativas y de evidencia donde vive el juicio, y de las 14 restantes leí el 100 %
> del diff de este ciclo más las regiones que sostienen cada conclusión. Es cobertura
> suficiente para lo que dictamino y **no es la lectura íntegra que el sobre pide**. Ninguna
> de mis conclusiones descansa en un fichero que no haya leído o ejecutado.

## 4 · COMANDOS Y RESULTADOS · REPRODUCIDOS POR MÍ, NO ACEPTADOS

Los dos instrumentos que el encargo me obliga a correr, **corridos por mí sobre la
candidata**:

```console
comprobar-invariantes-criticos.py
  ANCLA commit 60b640db1762… · tree 40c66896669c…
  24 invariantes medidos · 24 SATISFECHOS · 0 INCUMPLIDOS · 57 sabotajes
  declarados · 57 ejercidos · 115 catalogados · 59 no seleccionados · 0 sin detectar
  LOS INCUMPLIMIENTOS, UNO A UNO: ninguno                              EXIT=0

comprobar-obligaciones-implementadas.py
  ANCLA commit 60b640db1762… · tree 40c66896669c…
  58 obligaciones medidas · 0 SIN IMPLEMENTAR · 0 faltantes individuales
  FALTANTES, UNO A UNO: ninguno · pendientes de O26-IMPL: ∅            EXIT=0

--autopruebas del catálogo:      23 controles · 0 sin detectar         EXIT=0
ejercer-o26-condiciones.py:      8 de 8 SATISFECHAS · 0 no ejercibles  EXIT=0
test_admision.py:                Ran 101 tests · OK                    EXIT=0
ads_admision matriz (V6-18):     28 controles · falsos_verdes 0 · falsos_rojos 0
comprobar_negativos (evidencia): 200 infracciones detectadas · 0 NO detectadas
```

Batería completa sobre el árbol limpio: `integridad`, `evidencia`, `contratos`,
`referencias`, `recuentos`, `fuentes`, `arranque` → **todos rc=0**; `ads_lint` → **0
errores, 0 avisos**. `comprobar_integridad` compara huella almacenada y calculada:
**coinciden** (`6bfac55f1740f35b`).

Lancé además `registrar_evidencia.py` entero sobre una copia. Regeneró 44 de sus
componentes antes de que el anfitrión lo terminara en el último. **De esos 44, 42 cuerpos
son byte a byte idénticos a la evidencia publicada.** Los dos que difieren están explicados
y son benignos: `negativos` difiere sólo en el digest de la clase `EVIDENCIA` (el runner
estaba reescribiendo ese directorio mientras corría) y cierra igual en `200 · 0 NO
detectadas`; `o26-condiciones` difiere en un nombre de directorio temporal y —esto
importa— en que **mi corrida ancla la condición 3 a `60b640db1762`/`40c66896669c`**, la
candidata, mientras la publicada ancla a `a35763b0a53f`/`36f7a1e7beeb`.

## 5 · RAZONAMIENTO POR GRUPOS

### A · Integridad de `O30` y append-only de la sede

Reconstruí la sede en los **trece commits** de la cadena del sobre y comprobé dos cosas por
separado. Primera: cada versión es **prefijo byte a byte exacto** de la siguiente (`todas
las versiones son prefijo exacto de la siguiente: True`). Segunda, normalizando el
separador final: **0 alarmas** de mutación o desaparición de una entrada previa; cada
commit sólo **añade** una resolución. `O17`…`O29` están intactas byte a byte, y `O30` entra
por adición pura (`@@ -1308,3 +1308,227 @@`, 224 líneas añadidas, 0 retiradas). El hash del
bloque `O30` en la candidata es el mismo que el del sobre firmado fuera del repositorio
antes de crearme.

**Material protegido de §15:** `fd633383001d1e755e071195f9ab69e41a04926f` **NO es ancestro**
de la candidata (`merge-base --is-ancestor` → rc=1). `redesign/kernel-2.0` no existe en
este repositorio. Del diff base→candidata: **0** gates, **0** dictámenes, **0**
manifiestos, **0** enmiendas, **0** contratos inmutables, **0** ficheros de `docs/f6/`,
**0** de `docs/rediseno/`, **0** de `docs/evolucion/verificacion/manifiestos/`. Sobre el
árbol hay 64 documentos de gate, 5 dictámenes, 19 manifiestos, 6 enmiendas y 4 aprobadas:
ninguno tocado.

Una observación menor sobre el propio sobre, no sobre la candidata: sus instrucciones citan
«`O30` §13» y «`O30` §15», y **`O30` tiene §1 a §10 y ninguna más**. Lo que esas citas
designan son campos del sobre, no secciones de la resolución. No altera nada material.

→ **`O30` es íntegra y la sede es append-only, demostrado y no supuesto.**

### B · `K01`…`K24`

Corrido por mí: 24 medidos, 24 satisfechos, 0 incumplidos, 57 sabotajes declarados y **57
ejercidos**, 0 sin detectar, con el ancla en el commit y el tree de la candidata. Leí
íntegra la sede del catálogo. El conjunto y la formulación literal se **derivan** de `O30`
§2 y se contrastan en los dos sentidos; no hay cardinal escrito a mano ni en la sede ni en
el instrumento. Las autopruebas ponen rojo al propio juez en los trece modos (23 controles,
0 sin detectar), incluido `C-12`, que exige que el blob de la evidencia sea el de `HEAD`.

El criterio de `O30` §3 es explícito: ocho piezas por invariante. Las veinticuatro las
tienen, medidas. `O30` §3 **no** exige que un invariante sea inderrotable, y el propio
instrumento lo dice antes que sus cifras. Mi hallazgo `V-G1` (§6) alcanza al mecanismo de
`K22`, pero no priva a `K22` de ninguna de sus ocho piezas: **por la medida que `O30`
establece, los veinticuatro están satisfechos.** Lo digo así de preciso porque la tentación
de mezclar las dos cosas es exactamente lo que `O30` §1 corrigió.

Registro también, sin proponerlo como `K25` —no lo es, se adscribe honestamente a `K22`—,
que el catálogo publica 59 sabotajes catalogados **no seleccionados**, y que eso lo declara
él mismo, invariante a invariante.

→ **Satisfechas.**

### C · Obligaciones internas de `F6` y `CONTRATO 3`

58 obligaciones medidas, `0 SIN IMPLEMENTAR`, `0 faltantes individuales`, resta `∅`, con
`R1`–`R5` verdes una a una y el ancla en la candidata. Verifiqué la mecánica: `R4` liga
cada evidencia **blob a blob contra `HEAD`**, y `R5` no se conforma con `EXIT=0` sino que
exige que la salida **nombre** el escenario —«una batería ajena que pasa no ejecuta la
condición de cierre»—. El universo no se escribe: se deriva de seis componentes con su
procedencia, digest y tamaño, y publica sus ocho exclusiones con motivo. `CONTRATO 3`
figura cubierto por `T158` y `T350` y su condición de cierre se ejecuta.

La obligación circular `o26-impl` está rota por una dispensa que **sólo** alcanza a la
ausencia del fichero, se deriva del corpus y se publica en la salida. Sobre la candidata
intacta se concede **una** dispensa, a `o26-impl`, y es la legítima: lo comprobé.

→ **Completas.**

### D · Las ocho condiciones de `O26` §1

8 de 8 satisfechas, 0 no ejercibles, ejercidas por sus canales reales sobre la candidata,
con el perfil del anfitrión declarado y no universalizado (`O29` §7). La 6 corre en
**contenedor real** con UID 4242 frente al 1000 del runtime, repositorio montado de sólo
lectura, y los ocho intentos de escritura **IMPEDIDOS por el sistema de ficheros**. La 8
ejerce los seis ataques y el control sano.

**Ataqué la 7, que es donde el auditor anterior encontró el `BLOQUEANTE` `B1`.** Leí el
diff: la función pasó de construir un anillo vacío y preguntar `hasattr` a ejercer los
cuatro gestos sobre identidades reales. Y no me fié de la lectura: **saboteé `rotacion.py`
de cuatro maneras distintas** sobre cuatro copias.

| sabotaje | resultado |
|---|---|
| `verifica_en` siempre permisivo | **7 NO SATISFECHA** — 4 gestos en rojo, cada uno con su motivo |
| se retira la rama `REVOCADA` | **7 NO SATISFECHA** — «la revocación no revoca nada» |
| solapamiento → `10**9` | **7 NO SATISFECHA** — «la retirada no retira nada» |
| `exigir_valida` nunca falla cerrado | **7 NO SATISFECHA** — «aceptó una identidad revocada» |

En los cuatro casos las otras siete condiciones siguieron satisfechas y el **control sano**
siguió verde: el ejercicio discrimina, no enrojece por todo. **`B1` está materialmente
cerrado.**

→ **Satisfechas.**

### E · `M-04`

`O30` §6 me obliga a ejercer su condición de cierre y no a leer una etiqueta. La condición
es: *que `F6` implemente todos los puntos del contrato del verificador **y los EJECUTE**,
con cero falsos verdes y cero falsos rojos, medidos y publicados*, y su enunciado de fondo
es *la proposición general de que un árbol defectuoso puede pasar en verde*.

Lo que ejercí y **le es favorable**: la matriz de `V6-18`, corrida por mí, da **28
controles, 0 falsos verdes, 0 falsos rojos**, con las seis formas y las seis letras y un
adversarial por punto emitible; construye repositorios Git reales; declara `esperado`
**antes** de ejecutar; cuenta un `INDETERMINADO` como falso verde si se esperaba rojo; y
`M5` está genuinamente cerrado — la frontera con los 19 puntos de §20.1 se **deriva del
contrato** y se publica. `test_admision.py` da 101 OK. Y el verificador de admisión **sí
denuncia** el árbol adversarial que yo mismo construí (`V6-05` sobre `validadores.yaml`,
`V6-10` sobre la evidencia borrada).

Y lo que **la impide cerrarse**: construí un **duodécimo árbol adversarial** en el que la
proposición de `M-04` se cumple. Retirando del manifiesto la fila del instrumento que mide
`K01`–`K24`, borrando su evidencia y regenerando huella y sello —una operación que el
coordinador ejecuta en cada ciclo—, la **batería entera del corpus queda en verde**:
`integridad`, `evidencia` (`T158` **y** `T350`), `contratos`, `referencias`, `recuentos`,
`fuentes`, `arranque`, todos rc=0, y `ads_lint` con 0 errores. El instrumento que mide la
primera de las ocho condiciones de `O30` §7 desaparece del aparato **sin que nada del
aparato lo diga**.

Que el verificador de admisión lo denuncie en un acto separado **no lo convierte en verde
legítimo**: la batería que publica la evidencia de la certificación es la que dice verde
sobre un árbol al que le falta un medidor. Eso es «cero falsos verdes» incumplido, y es la
clase entera de `M-04`, la misma por la que `S1-02` fue bloqueante cuando `git status`
salía vacío con 38/38 en verde.

→ **`M-04 NO SUPERADA`**, con causa material propia y medida por mí, no por herencia de la
etiqueta del corpus.

### F · `C-L.7`

Su condición de cierre tiene dos mitades: *que ningún campo vigente del bloque reanudable
copie un estado, recuento, ordinal o enumeración que otra sede derive* — **y que se
compruebe por CLASE, no por instancia**. Su fila añade que *sólo un gate independiente
posterior puede cerrarla*. Yo soy ese verificador, así que la ejercí.

Ejecuté el barrido publicado de la regla 7 sobre el árbol sano: **sale vacío**, como anota,
y comprobé antes que mira campos de verdad (14 campos vigentes, no el conjunto vacío).
Después lo ataqué:

| sabotaje en campo vigente | resultado |
|---|---|
| «los catorce hallazgos» (minúsculas) | **CAZADO** — control positivo |
| «los CATORCE HALLAZGOS» (versales) | **CAZADO** — la corrección de caja funciona |
| el mismo cardinal separado de su sustantivo por un salto de línea | **ESCAPA** |
| «los 24 invariantes críticos» | **ESCAPA** |
| «las 58 obligaciones internas» | **ESCAPA** |
| «los 57 sabotajes declarados» | **ESCAPA** |

Los tres últimos son **cifras que este mismo ciclo deriva**. El barrido las deja pasar
porque su lista de sustantivos está escrita a mano y su alcance es por línea: es una
comprobación **por instancia**, que es literalmente lo que la condición de cierre excluye.
El corpus lo declara él mismo con esas palabras, y no lo oculta.

A eso se suma la población viva: `KD-02` y `LE-02` figuran como hallazgos vivos **no
corregidos** («NINGUNO SE CORRIGIÓ, y se dice por qué»), y `OC-1` a `OC-4` se registran
como «la misma familia… una razón más para que siga NO CERRADA». La clase **ha ganado
población**, no la ha perdido.

→ **`C-L.7 NO CERRADA`**, por su propia condición de cierre ejercida y medida por mí.

### G · Defectos internos

**`V-G1` · GRAVE — la evidencia de los instrumentos que miden `O30` está fuera de las dos
comprobaciones de cobertura.**
· *Sede*: `kernel/operativo/validadores/comprobar_evidencia.py`, comprobación 8 del bucle
de `T158`, y el alcance de `T350`.
· *Hecho medido*: la comprobación 8 —cuyo motivo escrito es «un validador nuevo sin
registrar quedaría fuera de la evidencia en silencio»— enumera **sólo**
`kernel/operativo/validadores/*.py`. **32 de las filas del manifiesto declaran `dir:` fuera
de ahí**, incluidas las cinco que miden las condiciones de `O30`. Y `T350`, que es el otro
guardián, sólo alcanza a la evidencia que algún `ads:escenario` declara: comprobé que
`invariantes-criticos-salida.txt`, `o26-impl-salida.txt`, `o26-sab-salida.txt`,
`o26-condiciones-salida.txt` y `universo-obligaciones-salida.txt` están declaradas por
**cero** escenarios, mientras `contratos-salida.txt` lo está por 23 y `admision-salida.txt`
por 17. Verificado en los dos sentidos: al hacerle lo mismo a `contratos`, **`T350` lo caza
en el acto**; al hacérselo a `invariantes-criticos`, **nadie dice nada**.
· *Remedio*: extender la comprobación de completitud del manifiesto a todo `dir:`
declarado, y exigir que la evidencia de todo componente `tipo: validador` esté cubierta por
`T350` o por un guardián equivalente.
· *Propietario*: `PLT` implementa · `SIS` propietario. · *Fase*: `F6`.

**`V-G2` · GRAVE — la dispensa reflexiva y la exención directa siguen siendo
TRANSFERIBLES.**
· *Sede*: `comprobar_evidencia._dispensa_reflexiva` y el campo
`se_excluye_de_su_propia_comprobacion`.
· *Hecho medido*: las tres condiciones nuevas cierran los tres vectores del auditor
anterior —lo comprobé: el ataque por otra obligación cae por la condición 5, el segundo
reclamante cae por la 6, la fila gemela cae por la 7—. **No cierran un cuarto.** La
condición 5 sondea el **script** con argumentos fijos (`--sin-ejecutar --solo
<obligación>`) y **nunca mira los `args` declarados de la fila**. Con eso obtuve la
dispensa para `coartada-v6`, una fila fabricada, `tipo: validador`, que jamás ha producido
evidencia y **cuya invocación real es `--help`** —no mide nada y no participa en ningún
ciclo—, dejando **intacto** al legítimo `o26-impl`: `T158 SUPERADA · 2 superadas · 0
fallidas · rc=0`. La afirmación escrita en el corpus, «LA DISPENSA ES ÚNICA POR OBLIGACIÓN,
Y ESTO ES LO QUE LA HACE INTRANSFERIBLE», es falsa como está redactada. La exención directa
`se_excluye_de_su_propia_comprobacion` también se transfiere a cualquier fila (`T158`
verde), aunque ahí `T350` sí actúa de respaldo cuando la evidencia está declarada por un
escenario.
· *Remedio*: derivar la dispensa de la **invocación declarada de la fila** —sondeando
`script` + `dir` + `args`— y no del script suelto; y someter
`se_excluye_de_su_propia_comprobacion` a una derivación equivalente.
· *Propietario*: `PLT` implementa · `SIS` propietario. · *Fase*: `F6`.

**Bordes que declaro por honradez:** `V-G1` y `V-G2` **no falsean la evidencia de esta
candidata**. Comprobé que sobre el árbol intacto el manifiesto está completo, los
instrumentos corrieron todos, y se concede una sola dispensa, la legítima. Explotarlos
exige escribir el manifiesto, lo que `ads_admision verificar` denuncia y `git status`
muestra. Son GRAVES porque el control cuya función declarada es garantizar la cobertura de
la evidencia está ciego precisamente sobre los instrumentos que sostienen la certificación,
y porque uno de ellos había sido declarado cerrado en la pasada única que `O30` §3 permite.

**Menores, registrados sin declararlos superados:**

| id | qué es | sede | remedio | propietario | fase |
|---|---|---|---|---|---|
| `V-M1` | la firma de `invariantes-criticos` pone suelo de 50 a los sabotajes: bajar de 57 a 53 pasa en verde. Medido: vaciar `K13` de 5 a 1 deja 53 y la firma lo admite | `validadores.yaml` | derivar el cardinal del catálogo en vez de un suelo | `SIS` | `F6` |
| `V-M2` | el sobre cita «`O30` §13» y «§15», que no existen: `O30` tiene §1–§10 | `emitir-sobre-de-ancla.py` | citar los campos del sobre, no secciones inexistentes | `VER` | `F6` |
| `V-M3` | `CD-7`, **confirmado por mí**: instalado sin packs, `ads_lint` da 3 enlaces rotos en `kernel/operativo/00-INDICE.md:54,123,124`. Y confirmé que viene de la base: el fichero es byte a byte idéntico en `a672ed9` y en la candidata (`sha256 189dbc5f…`) | `00-INDICE.md` · `new-project.sh` | embarcar los dos documentos o remitir | `PLT`/`SIS` | `F6` |
| `V-M4` | observabilidad: la evidencia congelada ancla al commit anterior (§5.H) | `evidencia/` | ninguna posible en el ciclo; se resuelve reproduciendo | `VER` | `F6` |

Ninguno de los cuatro falsea por sí mismo una de las ocho condiciones. `V-M1` roza `O30`
§7.1 y lo dejo dicho: no la falsea hoy porque yo ejercí los 57 y ninguno quedó sin
detectar.

### H · Suficiencia y certificación

Las ocho de `O30` §7, una a una, con lo que yo medí:

| # | condición | veredicto |
|---|---|---|
| 1 | `K01`–`K24` satisfechas | **SÍ** — 24/24, 57 sabotajes, 0 sin detectar |
| 2 | ninguna obligación interna sin implementar | **SÍ** — 58 medidas, resta `∅` |
| 3 | las ocho de `O26` ejercidas y satisfechas | **SÍ** — 8/8 por canales reales; `B1` cerrado y atacado |
| 4 | `M-04 SUPERADA` | **NO** |
| 5 | `C-L.7 CERRADA` | **NO** |
| 6 | ningún BLOQUEANTE ni GRAVE interno | **NO** — `V-G1` y `V-G2` |
| 7 | identidad exacta del commit y el tree | **SÍ** |
| 8 | sobre emitido antes de crear al verificador | **SÍ**, en lo comprobable (ver §7) |

Sobre la condición 7 y la asimetría que el coordinador declara: comprobé `git diff
--name-only a35763b 60b640d` y la diferencia es **exactamente** los cinco ficheros
declarados —`.sello-producto` y las cuatro evidencias derivadas—, ni uno más. La
declaración es cierta. Y la asimetría es real: ninguna evidencia puede contener el hash del
commit que la contiene. Lo que la resuelve no es la declaración sino la reproducción, y la
hice: mis corridas de los instrumentos sobre la candidata publican `ANCLA commit
60b640db1762… · tree 40c66896669c…`. **La condición 7 se satisface por mi reproducción, no
por la evidencia congelada.** Doy `G2`/`G3`/`G4` por resueltos y dejo el residuo como
`V-M4`, de observabilidad.

**Concurren tres causas independientes de no certificación: las condiciones 4, 5 y 6.**
Cualquiera de las tres bastaría.

### I · PesquerApp

Comprobé que **ningún fichero ni directorio del árbol tiene «pesquer» en su nombre**. El
diff base→candidata la menciona en **8 líneas, todas normativas o documentales**: `O30` §9
y §10 en la sede del Owner, y los §1 y §15 de la guía operativa, que reproducen el estado
condicionado y el bloqueo. Ni código, ni configuración, ni material suyo, ni acto de
inicio. Y como `F6` no queda certificada, `O30` §9 es terminante: continúa bloqueada.

## 6 · MIS ATAQUES, UNO A UNO

| # | ataque | esperaba | ocurrió |
|---|---|---|---|
| 1 | dispensa a una fila fantasma por **otra** obligación del canal (`P-08`) | rojo | **ROJO** — condición 5: `--solo P-08` termina con 2 |
| 2 | segundo reclamante de `CONTRATO 3` con `args` distintos | rojo | **ROJO** — condición 6, unicidad, nombrando a los dos |
| 3 | **sustituir** al legítimo: quitar la dispensa a `o26-impl` y dársela a una fila fabricada | rojo | **DISPENSA CONCEDIDA** a la fila fabricada |
| 4 | fila fantasma con invocación real `--help`, `o26-impl` eliminada | rojo | **`T158 SUPERADA` · rc=0** |
| 5 | `ads:escenario` forjado + fila fantasma, **legítimo intacto** | rojo | **`T158` y `T350` SUPERADAS · rc=0** |
| 6 | ídem + huella y sello regenerados | que `T150` lo cazara | **`T150` SUPERADA**: la defensa en profundidad se disuelve al regenerar |
| 7 | **borrar del manifiesto la fila que mide `K01`–`K24`** y su evidencia | que algo lo dijera | **batería entera verde, `ads_lint` 0 errores** |
| 8 | lo mismo sobre `contratos`, que sí está cubierto | rojo | **`T350` FALLIDA** — el respaldo funciona donde alcanza |
| 9 | `se_excluye_de_su_propia_comprobacion` a un componente cualquiera | rojo | `T158` verde; **`T350` lo caza** |
| 10 | cuatro sabotajes distintos de `rotacion.py` | rojo en la condición 7 | **ROJO en las cuatro**, cada una por su motivo, control sano intacto |
| 11 | vaciar `K13` de 5 sabotajes a 1 | rojo o denuncia | el instrumento **publica** los no seleccionados; la firma lo admite hasta 50 (`V-M1`) |
| 12 | barrido de `C-L.7`: 6 sabotajes | cazar los 6 | **caza 2, escapan 4** |
| 13 | instalar el producto sin packs y pasarle su propio lint | confirmar `CD-7` | **3 enlaces rotos**, confirmado |

## 7 · LÍMITES DE MI VERIFICACIÓN

1. **`MODIFICADO − LEÍDO ≠ ∅`**: 14 de los 30 ficheros no los leí de extremo a extremo (§3).
2. **No puedo probar criptográficamente la anterioridad temporal del sobre.** Verifiqué su
   firma, su digest, su contenido byte a byte contra el árbol y que se emitió fuera del
   repositorio con la clave declarada destruida. La afirmación «antes de crear al
   verificador» la acepto por esa evidencia, no por una marca de tiempo de confianza.
3. **`registrar_evidencia.py` no completó bajo mi control**: el anfitrión lo terminó en su
   último componente tras regenerar 44. Comparé esos 44 y 42 son idénticos (§4). Los dos
   instrumentos obligatorios los corrí yo, enteros.
4. **El perfil del anfitrión acota lo demostrado**: `cgroup v2` está montado y **no es
   ejercitable** aquí; la custodia productiva de claves es externa y este ciclo no la
   ejerce. Ninguna afirmación mía es universal.
5. **No juzgo la adscripción** de cada propiedad a su `Knn`: eso lo decide `O30` §2.
6. `O26` §5.2 sigue **no acreditada** por su instrumento (283 propiedades pendientes de
   346). `O30` §1 retiró esa medida de la condición de cierre, legítimamente y por
   autoridad competente, y ordenó conservarla como evidencia histórica —lo que el corpus
   hace, con el cambio de código de salida declarado y razonado—. **Que no gobierne no las
   declara satisfechas**, y así lo dejo registrado.

## 8 · DECLARACIONES

> **O30 ÍNTEGRA**
> **K01–K24 SATISFECHAS**
> **OBLIGACIONES INTERNAS DE F6 COMPLETAS**
> **OCHO CONDICIONES DE O26 SATISFECHAS**
> **M-04 NO SUPERADA**
> **C-L.7 NO CERRADA**
> **F6 NO CERTIFICADA**
> **F6 ABIERTA**
>
> **PESQUERAPP SIGUE BLOQUEADA · NO INICIADA**

---

**Causa material exacta de la no certificación:** fallan tres de las ocho condiciones de
`O30` §7 —la 4, la 5 y la 6— y cada una basta por sí sola. `M-04` no se supera porque
construí un duodécimo árbol adversarial en el que la batería completa del corpus da verde
tras retirar del manifiesto el instrumento que mide `K01`–`K24`. `C-L.7` no se cierra
porque su barrido comprueba por instancia y no por clase —cuatro de mis seis sabotajes
escaparon, tres de ellos cardinales que este mismo ciclo deriva— y porque su población de
instancias vivas ha crecido. Y quedan dos defectos GRAVES internos: la cobertura de
evidencia está ciega sobre los cinco instrumentos que miden las condiciones de `O30`, y la
dispensa reflexiva sigue siendo transferible por un cuarto vector que la pasada única no
cerró.

**Lo que sí queda acreditado, y lo digo con la misma firmeza:** el catálogo `K01`–`K24`
está satisfecho por la medida que `O30` establece; la resta de obligaciones internas es
vacía; las ocho condiciones de `O26` se ejercen de verdad sobre la candidata, y el
`BLOQUEANTE` `B1` está materialmente corregido —lo ataqué de cuatro maneras y las cuatro lo
pusieron rojo—; la sede del Owner es append-only demostrado byte a byte; el material
protegido está intacto; y el objeto juzgado es exactamente el commit y el tree del sobre
firmado.

Conforme a `O30` §10: este dictamen se registra y se publica, la candidata **no se
corrige** en respuesta a él, no se abre otro gate, no se propone otra tanda y no se inicia
PesquerApp. **Se para.**

---

*Fin del dictamen transcrito.*

## 4 · LO QUE EL COORDINADOR DEJA DICHO, Y LO QUE NO HACE

**No corrige nada.** `O30` §10 lo prohíbe expresamente después del dictamen, y las dos
GRAVES —`V-G1` y `V-G2`— quedan REGISTRADAS y sin remedio aplicado. Esto no es
conformidad: es la regla que el propio encargo impone, y romperla sería exactamente lo que
el auditor del ciclo anterior reprochó cuando el coordinador tocó un artefacto mientras su
auditoría seguía abierta.

**Los hallazgos del verificador se recogen tal cual.** `V-G1`, `V-G2`, `V-M1`, `V-M2`,
`V-M3` y `V-M4` figuran arriba con identificador, sede, remedio, propietario y fase, y
ninguno se declara superado. Su clasificación es del verificador, no del coordinador.

**Lo que este ciclo sí cerró, dicho sin inflarlo.** El `BLOQUEANTE` `B1` del auditor
anterior está materialmente corregido y el verificador lo confirmó atacándolo de cuatro
maneras. Los tres vectores de `G1` caen; el cuarto, que nadie había visto, es `V-G2`. La
asimetría de `G2`/`G3`/`G4` se declaró en vez de esconderse y el verificador la dio por
resuelta por reproducción, dejando `V-M4` de observabilidad. `M2`…`M5` están cerrados y
`M5` lo confirmó él. `CD-7` lo encontró y registró este ciclo, y el verificador lo confirmó
como `V-M3`.

**Lo que este ciclo NO consiguió, dicho igual de claro.** `F6` no queda certificada. Es el
tercer gate consecutivo que no certifica, y la razón ya no es de cobertura del gate: es
material y está medida. `M-04` cae por un árbol adversarial nuevo, el duodécimo, que
demuestra su proposición de fondo. `C-L.7` cae por su propia condición de cierre, ejercida.
Y quedan dos GRAVES internas.

**`O30` §10 · fin de la recursión.** Este era el último ciclo automático de corrección y
certificación de `F6`. El resultado está registrado y publicado. No se abre otro gate, no
se propone otra tanda automática, no se inicia PesquerApp. **Se para.** Lo que siga
necesita una orden nueva y separada del Owner.
