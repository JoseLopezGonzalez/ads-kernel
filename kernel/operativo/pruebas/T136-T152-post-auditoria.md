# T136–T152 — pruebas nacidas de la auditoría independiente

Cada una nombra el hallazgo que la hizo existir. Su estado real está en
[`REGISTRO-generado.md`](REGISTRO-generado.md), y ninguna sube de estado por argumento:
sube porque se ejecutó y su salida quedó registrada.

> **Todas llevan prueba negativa.** Un validador que sólo se ha visto pasar no está
> verificado: puede comprobar menos de lo que su nombre afirma y nadie lo sabría. Cada
> prueba de aquí tiene al menos una infracción deliberada que la hace fallar, en
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py). Las
> infracciones se aplican sobre una COPIA temporal del repositorio; el corpus real no se
> toca en ningún momento.

```yaml ads:escenario
id: T136
nombre: Ningún veto arbitra a otro veto levantable
cubre: ["A-06", "a.5 regla de colisión de vetos", "veto:degradacion-de-forma", "veto:integridad-de-datos"]
dado:
  - "dos capacidades con veto sobre materias distintas, ambas con su contrato de seis campos"
  - "cada contrato declara su levantabilidad: si, no-por-regla-dura o segun-instancia"
cuando: ["se comprueba la cláusula de colisión de cada veto del corpus"]
entonces:
  - "ningún veto declara que prevalece un veto cuya levantabilidad es si"
  - "ningún veto levantable se declara prevaleciente sobre otro"
  - "toda cláusula de colisión declara el escalado al Owner"
falla_si:
  - "un veto levantable arbitra a otro"
  - "una cláusula de colisión resuelve el conflicto sin escalar al Owner"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T137
nombre: DSP no declara autoridad semántica sobre ninguna cancelación
cubre: ["A-23", "b.7 autoridad orden y ejecución", "T54"]
dado: ["la ficha de DSP y los contratos de sus roles"]
cuando: ["se recorre su autoridad declarada buscando la palabra cancelar"]
entonces:
  - "ninguna entrada de decide ni de decide_sola de DSP menciona cancelar"
  - "la cancelación aparece en propone o en escala, nunca en decide"
falla_si: ["DSP decide una cancelación, aunque sea la de una espera no viable"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T148
nombre: El arranque documentado crea un proyecto conforme con cada pack
cubre: ["A-02", "tooling/new-project.sh", "README", "START_HERE", "K0.14"]
dado:
  - "el repositorio con sus packs instalables"
  - "la documentación de arranque que cita identificadores de pack"
cuando:
  - "se ejecuta el comando real de creación, una vez por cada pack instalable, sobre un directorio temporal"
entonces:
  - "todo identificador de pack citado en la documentación de arranque existe"
  - "el comando termina con código cero"
  - "la estructura resultante contiene el kernel, el pack, las plantillas y la especificación normativa"
  - "está instalado el pack pedido y NO los demás"
  - "el proyecto no arrastra packs/legacy-1.3.0 ni ficheros compilados"
  - "ads_lint, comprobar_contratos y comprobar_packs salen en verde DENTRO del proyecto creado"
  - "un identificador inexistente falla, nombra lo escrito, lista los instalables y no deja un proyecto a medias"
falla_si:
  - "la documentación cita un pack retirado o inexistente"
  - "el proyecto creado tiene enlaces rotos o un validador en rojo"
  - "un arranque fallido deja un directorio a medio crear"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_arranque.py"
estado: prueba-superada
evidencia: "evidencia/arranque-salida.txt"
```

```yaml ads:escenario
id: T150
nombre: La huella de integridad cubre a los validadores y detecta su edición
cubre: ["A-04", "K0.11", "tooling/kernel-status.sh", "validadores/huella.py"]
dado:
  - "un kernel vendorizado con su huella de referencia anotada"
cuando:
  - "se calcula la huella y se compara con la almacenada"
  - "se comprueba qué ficheros entran en ella"
entonces:
  - "la huella cubre los validadores en Python, los scripts de tooling, los esquemas y los contratos"
  - "la huella almacenada coincide con la calculada"
  - "dos cálculos consecutivos producen el mismo valor"
falla_si:
  - "un validador o un script de tooling puede editarse sin que el estado deje de ser limpio"
  - "la definición de la huella se estrecha hasta dejar fuera lo que ejecuta la conformidad"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_integridad.py"
estado: prueba-superada
evidencia: "evidencia/integridad-salida.txt"
```

```yaml ads:escenario
id: T147
nombre: Todo documento es alcanzable por ruta, y ninguna referencia es ambigua
cubre: ["A-05", "A-28", "sustituye a T134", "a.7 modo de fallo (b)", "regla de fuente única"]
dado:
  - "el corpus completo del repositorio, con sus nombres base repetidos"
  - "una lista de exclusiones explícita, con motivo escrito por entrada"
cuando:
  - "se construye el grafo de referencias resolviendo cada enlace por RUTA NORMALIZADA"
entonces:
  - "todo documento tiene al menos una entrada: enlace por ruta, enlace a su directorio, campo prompt o validador, o cita de un identificador suyo"
  - "ningún enlace apunta a una ruta que no existe"
  - "ningún enlace apunta al nombre correcto en la carpeta equivocada"
  - "los ficheros con el mismo nombre base se resuelven por ruta, nunca por nombre"
  - "toda exclusión declara su motivo y su objetivo sigue existiendo"
  - "el informe publica qué quedó fuera del análisis y por qué"
falla_si:
  - "un documento huérfano pasa porque otro fichero comparte su nombre base"
  - "una exclusión no tiene motivo escrito, o su objetivo ya no existe"
  - "un enlace roto no se distingue de un enlace ambiguo"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_referencias.py"
estado: prueba-superada
evidencia: "evidencia/referencias-salida.txt"
```

```yaml ads:escenario
id: T138
nombre: La escala de novedad es total y sus cinco niveles son alcanzables
cubre: ["A-07", "03-ESCALA-DE-NOVEDAD", "DIS/Reconstruccion", "DIS/Fundacion"]
dado:
  - "los cinco niveles declarados con su condición formal sobre las cinco variables del encuadre de diseño"
cuando:
  - "se enumeran las treinta y dos combinaciones posibles y se evalúan los niveles en su orden"
entonces:
  - "cada combinación produce exactamente un nivel"
  - "ningún nivel queda sin combinación que lo alcance"
  - "un proyecto en blanco da N4 y un proyecto vivo sin memoria fiable da N3"
falla_si:
  - "alguna combinación no produce ningún nivel"
  - "algún nivel es inalcanzable, y con él su método"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T139
nombre: Ningún nivel de novedad omite un gate obligatorio
cubre: ["A-08", "03-ESCALA-DE-NOVEDAD", "04-CICLO-DE-CALIDAD", "gate:usabilidad", "gate:excelencia-visual"]
dado: ["los cinco niveles con sus gates, sus ejes reutilizables y sus estaciones"]
cuando: ["se comprueba cada nivel contra los dos gates de Diseño y contra la tabla de estaciones"]
entonces:
  - "los cinco niveles declaran obligatorios gate:usabilidad y gate:excelencia-visual"
  - "los nueve ejes de la rúbrica tienen régimen en cada nivel: reutilizable o propio"
  - "acabado y fidelidad nunca son reutilizables en ningún nivel"
  - "todo nivel que reutiliza algún eje declara qué evidencia demuestra la vigencia del patrón"
  - "las estaciones 8 y 9 aparecen en los cinco niveles"
  - "la tabla de 04-CICLO coincide con los bloques canónicos: una sola fuente"
falla_si:
  - "un nivel omite un gate por ser pequeño"
  - "un eje queda sin régimen declarado"
  - "dos documentos declaran estaciones distintas para el mismo nivel"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T144
nombre: El gate de usabilidad tiene portador computable en Construcción
cubre: ["A-13", "gate:usabilidad", "gate:implementacion-completa", "DIS/validacion-de-uso"]
dado: ["gate:usabilidad declara aplicarse a las capas de DIS y de CON"]
cuando: ["se busca qué comprobación de CON activa ese gate sobre lo construido"]
entonces:
  - "gate:implementacion-completa comprueba la usabilidad de la superficie construida"
  - "la comprobación cita gate:usabilidad, de modo que el vínculo es rastreable"
  - "declara que el dictamen lo emite DIS/validacion-de-uso, no quien produjo la evidencia"
falla_si: ["el aplica_a menciona CON y ninguna comprobación de CON lo activa"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T140
nombre: Las obligaciones del proceso existen y el cierre las comprueba
cubre: ["A-09", "b.3", "b.4 P10", "b.10", "b.16", "gate:cierre-de-item", "T52", "T53", "T64", "T65", "T66"]
dado:
  - "los diez procesos de b.16 en forma canónica, cada uno con sus obligaciones"
  - "el gate de cierre con las cinco condiciones de b.10"
cuando: ["se comprueba el vocabulario de obligaciones y el gate que las evalúa"]
entonces:
  - "cada proceso declara al menos una obligación, con capa exigida, capacidad productora, criterio de satisfacción y autoridad de retirada"
  - "ninguna obligación declara a DSP como autoridad de retirada"
  - "toda capacidad condicional declara una condición comprobable, y ninguna se remite a la fórmula que b.16 prohíbe"
  - "gate:cierre-de-item comprueba terminación, obligaciones resueltas, vigencia, integración y aprendizaje"
  - "el gate usa el vocabulario de b.3: satisfecha, retirada, huérfana e invalidada"
  - "la plantilla de cierre reporta satisfechas y retiradas POR SEPARADO"
falla_si:
  - "un item puede cerrar con una obligación huérfana"
  - "DSP aparece como autoridad de retirada de alguna obligación"
  - "el informe de cierre puede sumar satisfechas y retiradas"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T141
nombre: Los frenos tienen ejecutor operativo, no sólo prosa
cubre: ["A-10", "a.7 los tres frenos", "b.9 avance material", "b.12 inanición", "T06", "T07", "T08", "T41"]
dado:
  - "los cuatro frenos aprobados con sus umbrales: 2 devoluciones, ciclo de 3 o más, 2 items SIS, 3 recomposiciones"
cuando: ["se busca quién los cuenta, quién detiene y quién escala"]
entonces:
  - "DSP declara el rol y el método de supervisión, que es su cuarta función en a.3"
  - "el método cuenta los cuatro frenos y todos sus pasos declaran condición de salida"
  - "el rol exige independencia de DSP/enrutamiento, que es parte interesada en el avance material"
  - "el rol declara expresamente que NO toca la prioridad"
  - "gate:despacho-coherente comprueba que los frenos se evaluaron, que el disparado escaló con las dos posturas, y que la inanición es visible sin haber tocado prioridades"
  - "el prompt fija los umbrales aprobados, en vez de dejarlos a la memoria del agente"
falla_si:
  - "un despacho cierra su gate sin haber evaluado un solo freno"
  - "quien recompone la ruta es quien cuenta si hubo avance material"
  - "un freno escala con una sola postura escrita"
  - "se inventa un umbral distinto de los aprobados"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T142
nombre: El encuadre expresa todos los estados que sus métodos le exigen
cubre: ["A-11", "b.2 los once estados de paquete", "gate:encuadre-listo", "ENC/Escucha"]
dado:
  - "el esquema del encuadre, con su madurez y el estado de su paquete en campos distintos"
cuando: ["se comparan los estados admitidos con los que b.2 define y con los que los documentos de ENC exigen"]
entonces:
  - "estado_paquete admite los once estados de b.2, incluido esperando-owner"
  - "ninguno de los dos campos admite `aparcado`, que en b.2 es bandera global del item"
  - "todo estado citado por los documentos de ENC es declarable en el esquema"
falla_si:
  - "un documento exige un estado que el esquema no puede expresar"
  - "reaparece un vocabulario de estados paralelo al de b.2"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T145
nombre: La crítica de encuadre exigible no se evapora al bajar la incertidumbre
cubre: ["A-14", "gate:encuadre-listo", "composicion:enc-alta-incertidumbre", "C4 un rol independiente no se retira"]
dado:
  - "un encuadre que entra con incertidumbre alta y baja a media tras conversar"
  - "un nivel de Owner que no es obligatorio"
cuando: ["se comprueba si el gate sigue exigiendo el dictamen de crítica"]
entonces:
  - "el encuadre persiste con qué grado entró, en incertidumbre.grado_inicial"
  - "el gate exige el dictamen por el grado INICIAL, por el nivel de Owner o porque la composición materializó el rol"
  - "la composición declara que la crítica no se retira al bajar el grado"
falla_si:
  - "un encuadre que empezó alto pasa el gate sin dictamen porque la conversación bajó el grado"
  - "un rol materializado cuyo dictamen nadie exige queda como rol decorativo"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T151
nombre: Ninguna cifra del corpus contradice el recuento derivado
cubre: ["A-24", "regla de fuente única", "RECUENTOS-generado.md"]
dado:
  - "el corpus, que es la única fuente de cuántas capacidades, roles, métodos o campos hay"
  - "la tabla explícita de dónde se afirma cada cifra en prosa"
cuando: ["se derivan los recuentos y se comparan con lo que cada documento afirma"]
entonces:
  - "toda cifra escrita coincide con la derivada, en dígitos o en palabra"
  - "una afirmación que desaparece de un documento hace fallar la prueba, para que la tabla no acumule restos"
falla_si:
  - "un documento declara una cifra que el corpus no sostiene"
  - "una cifra se escribe a mano en un sitio que la tabla no conoce"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T152
nombre: Los puntos de entrada no se contradicen sobre la versión
cubre: ["A-12", "kernel/VERSIONES.md", "K0.11", "O2"]
dado:
  - "la política que distingue release, línea histórica, versión normativa y versión de esquema"
cuando: ["se comparan las versiones declaradas en VERSION, KERNEL.md, el CHANGELOG, README y START_HERE"]
entonces:
  - "la política nombra la versión vigente del release"
  - "la línea histórica de KERNEL.md es distinta del release: son contadores distintos"
  - "la entrada más reciente del CHANGELOG coincide con kernel/VERSION"
  - "ningún punto de entrada declara una versión que la política no reconozca"
falla_si:
  - "dos documentos declaran versiones distintas del mismo artefacto"
  - "el release cambia y ningún punto de entrada se entera"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_versiones.py"
estado: prueba-superada
evidencia: "evidencia/versiones-salida.txt"
```
