# T182–T194 — runtime, gobierno Git, admisión, adaptadores e identidad

Conformidad del **segundo corte de `F6`**. Sus contratos derivados:
[`CONTRATO-RUNTIME-Y-DISPATCHER.md`](../runtime/CONTRATO-RUNTIME-Y-DISPATCHER.md) ·
[`CONTRATO-GOBIERNO-GIT-CONTROL.md`](../runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md) ·
[`CONTRATO-ADMISION.md`](../runtime/CONTRATO-ADMISION.md) ·
[`CONTRATO-ADAPTADOR.md`](../runtime/CONTRATO-ADAPTADOR.md) ·
[`CONTRATO-RAIZ-EXTERNA.md`](../runtime/CONTRATO-RAIZ-EXTERNA.md).

**Todo esto EJECUTA.** Procesos reales que se matan de verdad, repositorios Git temporales
reales sin red, dos instancias de runtime compitiendo en procesos distintos, y un adaptador
que lanza `subprocess` y mata el GRUPO de procesos. Ningún mock hace de pieza en ningún
sitio: `grep` de `mock`, `patch`, `monkeypatch`, `fake` y `stub` sobre las cinco baterías da
cero.

**Seis ejecutables:**

```text
runtime/pruebas/test_runtime.py           T182..T186 — ciclo, autoridad, reintentos, caída
runtime/pruebas/test_gobierno_git.py      T187 — g.14 y G-A8, sobre repos Git reales
runtime/pruebas/test_admision.py          T188..T190 — V2..V5, y la deuda S1-02
runtime/pruebas/test_adaptadores.py       T191 — V7, con proceso real y proyecciones
runtime/pruebas/test_identidad.py         T192 — O25: custodia, rotación y sin secretos
runtime/pruebas/escenario_e2e_runtime.py  T193 — los veinticinco pasos, de una pieza
validadores/comprobar_arranque.py         T194 — actualizar un control repo que ya existe
```

**Ninguna de ellas certifica nada.** `prueba-superada` significa que la prueba se ejecutó y
pasó. La CERTIFICACIÓN de `F6` la emite un juicio independiente y no quien construyó.

```yaml ads:escenario
id: T182
nombre: El dispatcher deriva el trabajo del estado y lo despacha por un adaptador
cubre: [F6-D, 11-ARQ 7.2, g.12 I-g4]
dado:
  - "un control repo con estado durable y varios paquetes en el estado canónico"
cuando:
  - "se abre el runtime, se derivan los elegibles y se despacha uno"
entonces:
  - "el trabajo elegible se DERIVA del estado, no de una cola en memoria"
  - "dos instancias distintas ven el mismo orden: prioridad y después identificador"
  - "el runtime recupera el estado ANTES de despachar, y no despacha si quedó MARCADO"
  - "el resultado y el acuse del efecto se escriben en la MISMA transición"
falla_si:
  - "existe una cola, un diario o una recuperación paralelos al motor de estado durable"
  - "una vista derivada se persiste y pasa a ser fuente de verdad"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T183
nombre: La autoridad sobre un paquete es exclusiva, y expira por observaciones y no por reloj
cubre: [g.6, g.2 I-g3, F6-D]
dado:
  - "dos instancias de runtime en procesos reales y un lease sobre el mismo paquete"
cuando:
  - "la segunda intenta adquirir, observar y reclamar"
entonces:
  - "`adquirir` NUNCA roba: si el lease es de otro es AUTORIDAD_NO_DISPONIBLE, sin excepciones"
  - "la reclamación tiene UNA sola puerta: PACIENCIA observaciones sin que avance el latido"
  - "sustituir el testigo del plano operacional NO permite reclamar: no está autenticado"
  - "ninguna ruta de decisión consulta el testigo; su lectura es sólo diagnóstico"
  - "quien pierde la autoridad no escribe NADA"
falla_si:
  - "un fichero del plano operacional, que cualquiera puede fabricar, decide la autoridad"
  - "el lease lleva un plazo de reloj de pared en un artefacto durable"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T184
nombre: Las cuatro clases de fallo se distinguen, y agotar los intentos abre reconciliación
cubre: [11-ARQ 7.3, g.9, g.16 G-A5]
dado:
  - "un paquete cuya ejecución falla, y otro cuya ejecución excede su límite"
cuando:
  - "se despacha hasta agotar los intentos"
entonces:
  - "reintentable, definitivo, cancelación, ambigua y pérdida de autoridad son cinco cosas distintas"
  - "una ejecución AMBIGUA no se reintenta nunca: va a `agotado` y abre reconciliación"
  - "un timeout es REINTENTABLE; un código de salida distinto de cero es DEFINITIVO"
  - "al agotar, el paquete queda `agotado`, deja de ser elegible y no se despacha"
  - "el agotamiento abre el registro auxiliar de `g.9` en la misma pasada"
falla_si:
  - "un reintento sin tope convierte el ciclo en un livelock"
  - "agotar los reintentos no deja pendencia, o la deja sin identificar el item"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T185
nombre: Pausa, reanudación y cancelación son transiciones reales del estado canónico
cubre: [11-ARQ 7.3, F6-D]
dado:
  - "paquetes listos y un vocabulario CERRADO de estados con sus transiciones declaradas"
cuando:
  - "se pausa, se reanuda y se cancela"
entonces:
  - "un paquete pausado deja de ser elegible, y reanudado vuelve a serlo"
  - "la cancelación es TERMINAL: no se reanuda"
  - "una transición fuera del vocabulario declarado es un error tipado"
falla_si:
  - "pausar o cancelar sólo cambia una variable en memoria"
  - "un estado terminal admite volver atrás"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T186
nombre: Una caída entre el efecto y su acuse no repite el efecto al recuperarse
cubre: [g.8, g.3, F6-D]
dado:
  - "los nueve puntos de fallo del runtime, con expectativa explícita cada uno"
cuando:
  - "se mata el proceso de verdad en cada punto y otra instancia recupera el trabajo"
entonces:
  - "un efecto ya aplicado NO se vuelve a ejecutar: el recibo del adaptador lo impide"
  - "el acuse y el resultado se ven juntos o no se ve ninguno"
  - "un estado que no casa con ninguna regla produce fallo CERRADO"
falla_si:
  - "un resultado confirmado se aplica dos veces"
  - "la recuperación inventa un estado que nadie escribió"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_runtime.py
estado: prueba-superada
evidencia: evidencia/runtime-salida.txt
```

```yaml ads:escenario
id: T187
nombre: Forzar una referencia del control repo es imposible por política y detectable si se intenta
cubre: [g.14, g.16 G-A8, O16]
dado:
  - "un control repo con su gobierno instalado y su tabla de propiedad como dato"
cuando:
  - "se intenta mover una ref sin fast-forward por las TRES formas: cuatro argumentos, tres argumentos sin valor viejo, y `--stdin`"
  - "se borra una ref protegida, y se fuerza con el hook retirado"
entonces:
  - "el hook `reference-transaction` RECHAZA las TRES formas: cuando Git le pasa el OID nulo, resuelve la ref por su cuenta en vez de dejarla pasar"
  - "crear una ref nueva y avanzar en fast-forward SIN valor viejo sí pasan: es el control positivo"
  - "el canal único rechaza `--force` y equivalentes ANTES de invocar Git"
  - "quitado el hook, el forzado se DENUNCIA contrastando el linaje registrado"
  - "preparar y publicar son actos distintos, y publicar compara la revisión base"
  - "con la ventana transaccional abierta no se confirma: la rama no contiene estado parcial"
falla_si:
  - "omitir el valor viejo —que Git hace opcional— salta la guarda"
  - "la prueba usa sólo la forma que el hook cubre, y confirma lo que el código hace en vez de lo que el contrato promete"
  - "`--force-with-lease` se usa como sustituto de una política explícita"
  - "la política puede eximirse a sí misma del perímetro"
  - "la detección del forzado depende de que el hook siga instalado"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_gobierno_git.py
estado: prueba-superada
evidencia: evidencia/gobierno-git-salida.txt
```

```yaml ads:escenario
id: T188
nombre: Toda lectura de Git usa una representación inequívoca, y la admisión juzga la mutación
cubre: [V6-01, V6-02, V6-03, V6-04, V6-05, V6-06, V6-07, V6-08, V6-09]
dado:
  - "un árbol Git real con forma de corpus y rutas adversariales"
cuando:
  - "se leen listas de rutas y se juzgan las mutaciones contra base, HEAD, índice y worktree"
entonces:
  - "toda lista se lee con separación por NUL y decodificación estricta"
  - "truncamiento, codificación inválida y estructura ajena dan ROJO nombrando la causa"
  - "el censo de lecturas se DERIVA del código: una lectura fuera del canal aparece y da ROJO"
  - "las seis letras de mutación se cubren, y renombrado y copia por SUS DOS PUNTAS"
  - "existir en la base NO exime, y confirmar tampoco"
falla_si:
  - "una lectura usa un separador que una ruta puede contener"
  - "una salida truncada devuelve lista vacía con éxito"
  - "el censo de lecturas se escribe a mano"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_admision.py
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T189
nombre: El censo de zonas cubre el CONTENIDO, incluida la raíz, y el instrumento se incluye a sí mismo
cubre: [V6-10, V6-11, V6-12, S1-02]
dado:
  - "el censo de zonas DERIVADO del registro canónico de fuentes y del árbol"
  - "la regla anterior REPRODUCIDA con su procedencia, que sólo miraba la topología"
cuando:
  - "se reescribe el CONTENIDO de un fichero preexistente de la RAÍZ y se confirma"
entonces:
  - "`git status` queda vacío, como en el ataque original"
  - "la regla anterior da VERDE y la de este corte da ROJO"
  - "el control positivo —el árbol sin ataque— da VERDE con las dos"
  - "el remedio es sobre el EJE, no sobre la zona: el mismo ataque cae en cuatro zonas distintas"
  - "una mutación del propio verificador o de su política da ROJO aunque vaya declarada"
  - "la sede del Owner se contrasta contra su COMMIT DE NACIMIENTO, no contra HEAD"
falla_si:
  - "una zona sin condición de contenido pasa por omisión en vez de dar ROJO"
  - "`S1-02` se declara cerrada por añadir una búsqueda de palabras"
  - "la regla anterior reproducida da ROJO siempre, y entonces no demuestra nada"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_admision.py
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T190
nombre: La matriz adversarial mide cero falsos verdes y cero falsos rojos, y cada fórmula tiene una sede
cubre: [V6-13, V6-14, V6-17, V6-18, V6-19]
dado:
  - "seis formas de nombre y contenido, y seis letras de mutación, con fixture positivo y negativo"
cuando:
  - "se ejecuta la matriz entera y se censan las fórmulas compartidas"
entonces:
  - "`falsos_verdes = 0` y `falsos_rojos = 0`, medidos y publicados"
  - "sin ancla externa el veredicto es INDETERMINADO, nunca VERDE"
  - "una segunda definición de una fórmula censada aparece y da ROJO aunque hoy coincida"
  - "si la importación de la sede falla, el instrumento NO emite"
falla_si:
  - "un control adversarial no puede ponerse rojo"
  - "la integridad de un árbol se sostiene con un digest que ese mismo árbol calcula"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_admision.py
estado: prueba-superada
evidencia: evidencia/admision-salida.txt
```

```yaml ads:escenario
id: T191
nombre: El adaptador local ejecuta un proceso real, lo mata de verdad y no repite un efecto aplicado
cubre: [V7, 11-ARQ 6, 11-ARQ 3.4, FD-5, FD-6]
dado:
  - "un adaptador de proceso local con su ficha declarada y su espacio de trabajo"
cuando:
  - "se ejecuta, se excede el límite, se cancela y se repite la misma orden"
entonces:
  - "el timeout y la cancelación matan el GRUPO, y el nieto y el bisnieto tampoco sobreviven"
  - "un descendiente que se saca del grupo con `setsid` SÍ escapa, y la ficha lo declara"
  - "una segunda llamada con recibo CERRADO devuelve `repetido` sin volver a ejecutar"
  - "una segunda llamada con recibo ABIERTO devuelve `ambiguo` y tampoco ejecuta"
  - "la selección es por CAPACIDAD declarada, y una versión de contrato incompatible se rechaza"
  - "una proyección editada a mano y una obsoleta se distinguen entre sí"
falla_si:
  - "el proceso hijo muere y el nieto queda huérfano ejecutándose"
  - "la ficha promete alcanzar a toda la descendencia y la medición lo desmiente"
  - "una caída entre ejecutar y cerrar el recibo duplica el efecto EN SILENCIO"
  - "un mock hace de adaptador y la prueba lo da por ejecución real"
  - "el adaptador escribe en el estado canónico: sería un segundo escritor"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_adaptadores.py
estado: prueba-superada
evidencia: evidencia/adaptadores-salida.txt
```

```yaml ads:escenario
id: T192
nombre: La identidad de firma vive fuera del árbol, rota con solapamiento y no filtra secretos
cubre: [O25, g.15, FD-1]
dado:
  - "una configuración externa de confianza y un anillo con identidades activas, retiradas y revocadas"
  - "un marcador secreto único inyectado en la clave"
cuando:
  - "se firma, se verifica, se atesta, se rota, se revoca y se falla"
entonces:
  - "una configuración DENTRO del árbol verificado se rechaza, también por enlace simbólico"
  - "manipular la configuración dentro del árbol NO cambia el veredicto"
  - "una retirada verifica dentro del solapamiento y falla fuera; una revocada no verifica"
  - "sin proveedor válido no se firma: fallo CERRADO, sin degradar a una firma propia"
  - "el marcador no aparece en ninguna salida, ni en el estado, ni en el diario, ni en la evidencia"
falla_si:
  - "el repositorio verificado puede cambiar qué identidad se acepta"
  - "un secreto llega a un log, a un error o a la configuración exportada"
  - "se implementa una primitiva criptográfica propia"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_identidad.py
estado: prueba-superada
evidencia: evidencia/identidad-salida.txt
```

```yaml ads:escenario
id: T193
nombre: Los veinticinco pasos del segundo escenario extremo a extremo, con dos runtimes y dos fuentes
cubre: [F6-D, g.14, V6-10, V7, g.9, g.16]
dado:
  - "un workspace con un control repo y dos repositorios de producto, todos Git reales"
  - "dos instancias de runtime en procesos distintos y un adaptador local de proceso"
cuando:
  - "se recorren los veinticinco pasos: instalar, recuperar, crear trabajo, despachar, fallar, agotar, reconciliar, pausar, cancelar, caer, recuperar por otra instancia, mutar Git y verificar la admisión"
entonces:
  - "no hay doble despacho, y un efecto confirmado no se aplica dos veces"
  - "forzar una referencia se rechaza, y el ataque de `S1-02` sobre la raíz da ROJO"
  - "el estado queda íntegro, la ventana cerrada y las fuentes limpias"
  - "dos ejecuciones desde cwd distintos producen bytes idénticos"
falla_si:
  - "algún paso se simula en vez de ejecutarse"
  - "la salida lleva reloj, duración, pid o ruta absoluta"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/escenario_e2e_runtime.py
estado: prueba-superada
evidencia: evidencia/e2e-runtime-salida.txt
```

```yaml ads:escenario
id: T194
nombre: Un control repo que ya existe se actualiza sin perder lo que el proyecto tiene
cubre: [C6, FD-3, macrocircuito de actualizacion]
dado:
  - "un proyecto instalado con su perfil retocado y su estado durable ya fundado"
  - "su kernel vendorizado, al que se le quita una pieza y se le pone una versión vieja"
cuando:
  - "se sustituyen el kernel y el tooling desde el origen y se reancla la huella"
entonces:
  - "el PROFILE del proyecto y su ESTADO DURABLE quedan intactos, byte a byte"
  - "la pieza que faltaba vuelve y la versión vieja se sustituye"
  - "la huella del proyecto se reancla a su contenido nuevo y queda LIMPIA"
  - "los validadores siguen en verde DENTRO del proyecto actualizado"
falla_si:
  - "la actualización pisa el perfil, el manifiesto o el estado del producto"
  - "el proyecto actualizado queda con enlaces rotos o con la huella divergente"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_arranque.py
estado: prueba-superada
evidencia: evidencia/arranque-salida.txt
```
