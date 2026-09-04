# T210–T225 — árboles adversariales, contención, raíz externa, multimáquina, sesión nueva y el escenario de F6

Conformidad de la **segunda mitad del macrobloque 3 de `F6`**. Sus contratos derivados:
[`CONTRATO-ARBOLES-ADVERSARIALES.md`](../runtime/CONTRATO-ARBOLES-ADVERSARIALES.md) ·
[`CONTRATO-CONTENCION.md`](../runtime/CONTRATO-CONTENCION.md) ·
[`CONTRATO-RAIZ-EXTERNA.md`](../runtime/CONTRATO-RAIZ-EXTERNA.md) ·
[`CONTRATO-GOBIERNO-GIT-CONTROL.md`](../runtime/CONTRATO-GOBIERNO-GIT-CONTROL.md) ·
[`CONTRATO-ADAPTADOR.md`](../runtime/CONTRATO-ADAPTADOR.md).

> **`H-02` · `T225` ha BAJADO a `prueba-ejecutada`, y no es una degradación del
> aparato: es el dato.** La auditoría independiente del 2026-09-04 midió que catorce
> escenarios del corpus declaraban `estado: prueba-superada` sobre una evidencia que **no
> los nombra en ninguna línea de veredicto**. La derivación de
> [`validadores/registro_pruebas.py`](../validadores/registro_pruebas.py) ya sacaba
> `prueba-ejecutada` y escribía el motivo, pero DESCARTABA la divergencia por no ser
> contrastable, y `T350` quedaba en verde. Desde esa pasada, un `estado` superior al
> derivado es DIVERGENCIA se pueda contrastar o no, y la regla dura de
> [`REGISTRO.md`](REGISTRO.md) —«ninguna prueba sube de estado por argumento»— vale también
> para lo que la evidencia **no sostiene**, y no sólo para lo que **contradice**.
>
> `prueba-ejecutada` es el estado exacto: `escenario_e2e_f6.py` —veintiún pasos— se ejecuta,
> termina con código 0 y su salida queda registrada; lo que no consta es el veredicto **de
> este escenario** por separado. Subirlo otra vez exige que la salida lo NOMBRE, no que
> alguien lo declare.

**Todo esto EJECUTA.** Repositorios Git temporales reales, un remoto bare con dos clones y
dos procesos independientes, contenedores y espacios de nombres del anfitrión, claves
Ed25519 efímeras generadas fuera de todo repositorio y destruidas al terminar, y procesos
que se matan de verdad. Ningún mock hace de pieza en ningún sitio.

**Cinco ejecutables:**

```text
runtime/pruebas/test_arboles.py        T210..T213 — V6-15, el derivador y su matriz
runtime/pruebas/test_contencion.py     T214..T216 — FD-5, la contención del anfitrión
runtime/pruebas/test_raiz_externa.py   T217..T220 — V6-16, firma asimétrica e independencia
runtime/pruebas/test_multimaquina.py   T221..T222 — g.14 entre MÁQUINAS, con remoto real
runtime/pruebas/test_sesion_nueva.py   T223..T224 — la pieza 4 de §6.4, y el nivel de §6.5
```

**Ninguna de ellas certifica nada.** `prueba-superada` significa que la prueba se ejecutó y
pasó. La CERTIFICACIÓN de `F6` la emite un juicio independiente y no quien construyó.

```yaml ads:escenario
id: T210
nombre: El conjunto de árboles adversariales se DERIVA de su sede y nunca se enumera
cubre: [V6-15, 11-ARQ 20.5]
dado:
  - "los documentos inmutables de los gates, cada uno con la cabecera de su árbol"
cuando:
  - "el derivador recorre las sedes y construye el conjunto"
entonces:
  - "se derivan ÁRBOLES, no identificadores genéricos de hallazgo"
  - "cada entrada lleva su DOCUMENTO y su CABECERA de procedencia, y el hallazgo que lo cerró"
  - "el octavo árbol `DD-01` está dentro, y se conserva propietario `SIS` y fase `F4c`"
  - "una entrada inexistente, un duplicado o un fixture sin árbol adjudicado dan ROJO"
  - "la salida es estructurada y determinista: mismos bytes desde cualquier `cwd`"
falla_si:
  - "el conjunto se escribe a mano, o aparece un cardinal escrito al lado de la enumeración"
  - "un árbol citado por la entrada no está cubierto por la suite, o al revés"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_arboles.py
estado: prueba-superada
evidencia: evidencia/arboles-salida.txt
```

```yaml ads:escenario
id: T211
nombre: Cada ataque se aplica de verdad, y la versión vulnerable lo acepta
cubre: [V6-15, 11-ARQ 20.5]
dado:
  - "un repositorio Git temporal real por árbol, y la versión histórica de su propiedad"
cuando:
  - "se materializa el árbol atacado y se juzga con la versión de la época"
entonces:
  - "el CONTROL DEL ATAQUE exige que el árbol atacado difiera del sano en lo que el ataque cambia"
  - "la versión VULNERABLE ACEPTA el árbol atacado, que es la reproducción histórica"
  - "retirado el INGREDIENTE del ataque, la misma versión vulnerable vuelve a dar ROJO"
falla_si:
  - "una prueba pasa porque el ataque no llegó a aplicarse"
  - "la versión vulnerable dice VERDE a todo, y entonces no demuestra nada"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_arboles.py
estado: prueba-superada
evidencia: evidencia/arboles-salida.txt
```

```yaml ads:escenario
id: T212
nombre: La implementación vigente rechaza cada árbol POR LA PROPIEDAD que le toca
cubre: [V6-15, V6-01, V6-05, V6-06, V6-08, V6-10]
dado:
  - "el mismo árbol atacado que la versión histórica acepta"
cuando:
  - "lo juzga el verificador de admisión vigente"
entonces:
  - "el veredicto es ROJO, y el hallazgo NOMBRA la propiedad que lo produce"
  - "el árbol SANO sigue dando verde: no hay falso rojo"
falla_si:
  - "el rojo se acredita sólo por un código de salida distinto de cero"
  - "la versión vulnerable y la vigente no se distinguen sobre el mismo árbol"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_arboles.py
estado: prueba-superada
evidencia: evidencia/arboles-salida.txt
```

```yaml ads:escenario
id: T213
nombre: La matriz de cuatro columnas cierra con las dos restas vacías
cubre: [V6-15, V6-18]
dado:
  - "el conjunto derivado de la entrada y la suite de regresión construida"
cuando:
  - "se ejecuta la suite entera y se publica su matriz"
entonces:
  - "`entrada − suite = ∅` y `suite − entrada = ∅`, sobre el mismo conjunto de ÁRBOLES"
  - "cada fila publica árbol sano · ataque presente · versión vulnerable · versión vigente"
  - "el punto ejecutable emite el mismo JSON byte a byte desde cualquier `cwd`"
falla_si:
  - "alguna de las dos restas es no vacía"
  - "una fila se publica sin su control del ataque o sin su control del control"
ejecucion: validador-estructural
validador: kernel/operativo/runtime/pruebas/test_arboles.py
estado: prueba-superada
evidencia: evidencia/arboles-salida.txt
```

```yaml ads:escenario
id: T214
nombre: Las capacidades de contención del anfitrión se DETECTAN ejerciéndolas
cubre: [FD-5, 11-ARQ 6.5]
dado:
  - "un anfitrión cuyos mecanismos de contención se desconocen de antemano"
cuando:
  - "se ejecuta la detección, sonda a sonda"
entonces:
  - "cada sonda EJERCE la vía real, y no se limita a mirar si existe un fichero"
  - "cada backend publica su disponibilidad, su nivel de aislamiento y su motivo"
  - "un mecanismo presente pero inservible se declara NO disponible, con el error del sistema"
falla_si:
  - "una sonda declara disponible un mecanismo que no puede contener nada"
  - "la detección se escribe a mano en vez de ejercerse"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T215
nombre: Con contención fuerte, un descendiente que hace `setsid` NO escapa
cubre: [FD-5, 11-ARQ 6.5]
dado:
  - "una tarea que lanza hijo, nieto y bisnieto, los tres haciendo `setsid`"
cuando:
  - "se cancela la tarea, o vence su límite, con la política de árbol de procesos"
entonces:
  - "el grupo completo se cancela y NINGUNA de las tres generaciones sobrevive"
  - "la contención sobrevive a los cambios de grupo de procesos"
  - "si la política exige contención fuerte y el anfitrión no la ofrece, el adaptador FALLA CERRADO"
falla_si:
  - "se degrada en silencio a `killpg`"
  - "un descendiente sigue vivo después de la cancelación o del timeout"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T216
nombre: El backend simple conserva su nivel INFERIOR declarado, y su límite se mide
cubre: [FD-5]
dado:
  - "la misma tarea de tres generaciones, con el backend simple"
cuando:
  - "se cancela la tarea"
entonces:
  - "el descendiente que hizo `setsid` SÍ sobrevive, y la prueba lo comprueba por PID"
  - "el nivel de aislamiento declarado es `grupo-de-procesos`, explícitamente inferior"
  - "la ficha del adaptador declara el nivel REAL, no el aspiracional"
falla_si:
  - "el backend simple se presenta con el nivel del fuerte"
  - "la limitación del `setsid` se oculta en vez de medirse"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_contencion.py
estado: prueba-superada
evidencia: evidencia/contencion-salida.txt
```

```yaml ads:escenario
id: T217
nombre: La raíz externa es un paquete y un proceso SEPARADOS, con su confianza fuera del árbol
cubre: [V6-16, g.15, O18, O25, 11-ARQ 11.8]
dado:
  - "un control repo verificado y una instalación de la raíz externa fuera de él"
cuando:
  - "el instalador materializa el paquete y el verificador se ejecuta como proceso propio"
entonces:
  - "la instalación se RECHAZA si el destino cae dentro del árbol verificado, también por enlace"
  - "la configuración de confianza vive FUERA, y el árbol no puede cambiar qué identidad se acepta"
  - "la evidencia se escribe FUERA del árbol verificado"
  - "sin proveedor, sin clave o sin ancla NO se emite veredicto favorable"
falla_si:
  - "la raíz externa se ejecuta dentro del mismo proceso que el runtime"
  - "un cambio dentro del árbol altera la política que la raíz externa aplica"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_raiz_externa.py
estado: prueba-superada
evidencia: evidencia/raiz-externa-salida.txt
```

```yaml ads:escenario
id: T218
nombre: La firma es ASIMÉTRICA, y quien verifica no puede firmar
cubre: [V6-16, g.15, O25]
dado:
  - "una identidad Ed25519 efímera, generada fuera de todo repositorio"
cuando:
  - "se firma una atestación con `ssh-keygen -Y sign` y se verifica con `-Y verify`"
entonces:
  - "firmar y verificar son dos programas distintos, y el verificador no tiene clave privada"
  - "rotación, solapamiento por épocas, retirada y revocación funcionan y se prueban"
  - "una clave desconocida se rechaza, y una atestación manipulada también"
  - "la clave privada no aparece en logs, errores, evidencia ni configuración exportada"
falla_si:
  - "se usa HMAC o cualquier clave simétrica como demostración de la raíz externa"
  - "se implementa criptografía propia en vez de delegar en la herramienta del anfitrión"
  - "una clave privada entra en cualquier repositorio o sobrevive al final de la prueba"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_raiz_externa.py
estado: prueba-superada
evidencia: evidencia/raiz-externa-salida.txt
```

```yaml ads:escenario
id: T219
nombre: La identidad de la raíz externa NO PUEDE escribir en el árbol verificado
cubre: [V6-16, g.12, g.15, O18]
dado:
  - "un aislamiento real del anfitrión, con identidad distinta y montaje de sólo lectura"
cuando:
  - "la identidad externa INTENTA de verdad las ocho escrituras"
entonces:
  - "modificar, crear y borrar un fichero fallan, con el mensaje real del sistema"
  - "cambiar una ref, alterar la configuración y cambiar la política fallan"
  - "sustituir la clave pública aceptada falla"
  - "modificar la atestación DESPUÉS de firmarla falla o queda detectado antes de aceptarse"
  - "los dos controles del control pasan: escribir en lo propio y leer el árbol montado"
falla_si:
  - "la independencia se acredita sólo por ejecutar desde otro directorio"
  - "todos los intentos fallan porque el entorno no arrancó, y no por el aislamiento"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_raiz_externa.py
estado: prueba-superada
evidencia: evidencia/raiz-externa-salida.txt
```

```yaml ads:escenario
id: T220
nombre: Un veredicto falseado desde dentro del árbol es DESMENTIDO por la atestación externa
cubre: [V6-16, V6-17, g.16 G-A9]
dado:
  - "un árbol que se autodeclara conforme y una raíz externa con su propia identidad"
cuando:
  - "la raíz externa atesta sobre el MISMO commit y el MISMO `tree`"
entonces:
  - "la atestación externa desmiente la autodeclaración, y gana la externa"
  - "la atestación queda vinculada al SHA del commit y al `tree`, nunca a un nombre de rama"
  - "el árbol no tiene la clave, y por eso no puede fabricar el veredicto"
falla_si:
  - "una autoridad interna puede sustituir a la raíz externa"
  - "el veredicto se sostiene sólo por un digest calculado por el propio árbol"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_raiz_externa.py
estado: prueba-superada
evidencia: evidencia/raiz-externa-salida.txt
```

```yaml ads:escenario
id: T221
nombre: Dos máquinas sobre la misma autoridad, y sólo una confirma
cubre: [g.14, g.6, g.16 G-A8, C7]
dado:
  - "un remoto bare temporal, dos clones, dos procesos independientes e identidades distintas"
cuando:
  - "los dos intentan publicar sobre la misma autoridad a la vez"
entonces:
  - "exactamente uno confirma, y el otro DETECTA la pérdida de autoridad"
  - "no hay `force` y no hay historia reescrita"
  - "una publicación obsoleta falla, y una legítima posterior funciona"
  - "la serialización NO depende de un `flock` compartido entre las dos máquinas"
falla_si:
  - "los dos confirman"
  - "la serialización deja de funcionar cuando los cerrojos locales no se comparten"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_multimaquina.py
estado: prueba-superada
evidencia: evidencia/multimaquina-salida.txt
```

```yaml ads:escenario
id: T222
nombre: Caída, reconciliación, ref protegida, remoto manipulado y linaje completo
cubre: [g.14, g.8, g.9, g.16 G-A8]
dado:
  - "el mismo remoto y los mismos dos clones, y caídas provocadas en dos ventanas distintas"
cuando:
  - "se cae ANTES del push, y después se cae DESPUÉS del push y antes del acuse"
entonces:
  - "la caída anterior al push se recupera"
  - "la caída posterior al push y anterior al acuse se RECONCILIA, sin repetir el efecto"
  - "una ref protegida no puede borrarse"
  - "un remoto manipulado no puede fingir autoridad"
  - "el linaje COMPLETO detecta un forzado anterior aunque después exista un commit legítimo"
falla_si:
  - "se registra sólo la cabeza del linaje, y un forzado seguido de un commit legítimo lo borra"
  - "una ausencia de acuse se lee como efecto no aplicado"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_multimaquina.py
estado: prueba-superada
evidencia: evidencia/multimaquina-salida.txt
```

```yaml ads:escenario
id: T223
nombre: La prueba de humo abre una sesión REALMENTE nueva, y es idempotente
cubre: [F6-G, 11-ARQ 6.4, 11-ARQ 6.5]
dado:
  - "un proceso propio, con entorno construido entero, `cwd` propio y espacio vacío"
cuando:
  - "se recorren los diez pasos, y luego se repiten desde otra sesión limpia"
entonces:
  - "no se reutiliza proceso, memoria, módulos importados, variables de entorno, `cwd` ni temporales"
  - "se instala o descubre el adaptador, se carga su ficha y se verifican versión y capacidades"
  - "se ejecuta una operación REAL, se recibe progreso y se obtiene resultado"
  - "se producen recibo y evidencia, y la idempotencia se mide por el efecto en disco"
falla_si:
  - "la sesión hereda `os.environ` del proceso que la lanza"
  - "un `skip` se presenta como éxito funcional"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_sesion_nueva.py
estado: prueba-superada
evidencia: evidencia/sesion-nueva-salida.txt
```

```yaml ads:escenario
id: T224
nombre: La sesión abierta sobre una fuente localiza el control repo, con sus cuatro desenlaces
cubre: [F6-G, 11-ARQ 6.4, 11-ARQ 6.7]
dado:
  - "una fuente con su puntero y un control repo hermano, y las tres variantes que lo rompen"
cuando:
  - "el entorno lee el puntero y resuelve el control repo por IDENTIDAD del remoto canónico"
entonces:
  - "`LO_ENCUENTRA` abre el hermano y opera con él como contexto principal"
  - "`NO_LO_ENCUENTRA` dice qué remoto buscaba y no adivina"
  - "`NO_SE_PUDO_COMPROBAR` es un impedimento real, y es DISTINTO de la ausencia"
  - "`ENCUENTRA_DOS` es un error explícito"
  - "el nivel de §6.5 se DERIVA de las celdas de cobertura, y no se escribe"
falla_si:
  - "la ausencia y el impedimento se colapsan en un solo desenlace"
  - "se presupone un nivel alcanzado en vez de derivarlo de la evidencia"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/test_sesion_nueva.py
estado: prueba-superada
evidencia: evidencia/sesion-nueva-salida.txt
```

```yaml ads:escenario
id: T225
nombre: El escenario extremo a extremo del macrobloque 3, con sus veintiún pasos
cubre: [F6-D, F6-F, F6-G, V6-15, V6-16, g.14, g.15, g.16 G-A8, g.16 G-A9, 11-ARQ 7.2, 11-ARQ 8, 11-ARQ 9.6]
dado:
  - "un control repo, dos repositorios de producto, un remoto bare y dos clones que representan dos máquinas"
  - "dos runtimes, un adaptador local real, la raíz externa instalada fuera del árbol y claves Ed25519 efímeras"
cuando:
  - "se recorre un macrocircuito completo desde su FASE 0 hasta su cierre, con `Continúa` por medio"
entonces:
  - "instalación · FASE 0 · encuadre · composición de rutas · materialización de equipo"
  - "items y paquetes · despacho · progreso · handoff · gate de capa"
  - "mutación Git · admisión V2–V5 · firma externa asimétrica · publicación remota"
  - "concurrencia entre máquinas · caída del runtime · recuperación · `Continúa`"
  - "no repetición del efecto · cierre del macrocircuito · evidencia verificable desde la raíz externa"
  - "la salida es byte a byte idéntica desde tres `cwd` distintos"
falla_si:
  - "algún paso se cumple con un mock en lugar de con el proceso, el repositorio o la clave reales"
  - "el escenario continúa tras un paso fallido, midiendo el estado equivocado en los siguientes"
  - "una ruta absoluta de la máquina entra en la evidencia publicada"
ejecucion: requiere-runtime
validador: kernel/operativo/runtime/pruebas/escenario_e2e_f6.py
estado: prueba-ejecutada
evidencia: evidencia/e2e-f6-salida.txt
```
