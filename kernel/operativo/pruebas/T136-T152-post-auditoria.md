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
