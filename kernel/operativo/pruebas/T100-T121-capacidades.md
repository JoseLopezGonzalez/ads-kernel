# T100–T121 — conformidad de las capacidades del paso 5

Las pruebas que los métodos de las quince capacidades citan en su `prueba_de_reanudacion` o
que derivan de sus gates. Su estado real está en [`REGISTRO-generado.md`](REGISTRO-generado.md).

> Ninguna de estas pruebas está ejecutada. Todas exigen un proyecto real con trabajo en
> curso, y varias exigen el runtime que esta iteración no implementa.

```yaml ads:escenario
id: T100
nombre: Reanudación de PRD/Definicion sin repreguntar al Owner
cubre: ["PRD/Definicion", "a.10 checkpoint"]
dado:
  - "un alcance a medio cerrar con una pregunta pendiente al Owner"
cuando:
  - "un agente nuevo reanuda"
entonces:
  - "continúa desde el paso anotado sin volver a preguntar lo ya contestado"
falla_si:
  - "se repite al Owner una pregunta registrada en el checkpoint"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T101
nombre: Un GAP registra por qué apareció el hueco
cubre: ["PRD/Gap", "b.16 GAP", "aprendizaje del hueco"]
dado:
  - "un item GAP cerrado"
cuando:
  - "se comprueba su capa de PRD"
entonces:
  - "existe el origen del hueco clasificado y learning_candidate resuelto"
falla_si:
  - "el GAP se tramitó como FEA y se perdió la pregunta de por qué apareció"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T102
nombre: Reanudación de ARQ/Encaje sin repetir el radio
cubre: ["ARQ/Encaje", "gate:plan-tecnico"]
dado:
  - "un radio medido a medias con su traza de búsquedas"
cuando:
  - "un agente nuevo reanuda"
entonces:
  - "no repite ninguna búsqueda registrada y completa el radio"
falla_si:
  - "se repite una búsqueda ya trazada, o se estima lo que falta"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T103
nombre: Reanudación de un diagnóstico sin repetir hipótesis descartadas
cubre: ["ARQ/Diagnostico"]
dado:
  - "un diagnóstico con reproducción conseguida y dos hipótesis descartadas"
cuando:
  - "un agente nuevo reanuda"
entonces:
  - "no vuelve a probar las hipótesis descartadas y parte de la reproducción registrada"
falla_si:
  - "se reintenta una hipótesis ya descartada con la misma evidencia"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T104
nombre: Las condiciones de dominio llegan antes de construir
cubre: ["DOM/Condiciones", "b.16 DOM dos veces"]
dado:
  - "un item que cumple C-DOM"
cuando:
  - "se compone su ruta"
entonces:
  - "las condiciones de DOM se entregan ANTES del paquete de CON, no después"
falla_si:
  - "DOM recibe la primera noticia en paralelo con CON, o después"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T105
nombre: Una migración no se declara reversible sin haber revertido
cubre: ["DOM/Migracion", "veto:integridad-de-datos"]
dado:
  - "una migración no compatible hacia atrás"
cuando:
  - "se pide su aprobación"
entonces:
  - "existe salida de la reversión EJECUTADA sobre el resultado de la migración"
falla_si:
  - "se declara reversible con la reversión sólo escrita"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T106
nombre: Construcción devuelve en vez de redecidir
cubre: ["CON/Implementacion", "a.3 CON no redecide"]
dado:
  - "una capa anterior insuficiente detectada al leer, antes de construir"
cuando:
  - "CON ejecuta su paso 1"
entonces:
  - "devuelve a la capacidad propietaria antes de construir nada"
falla_si:
  - "se construye sobre la capa insuficiente, o se corrige la decisión ajena"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T107
nombre: Un experimento no se reanuda sin criterio de descarte previo
cubre: ["CON/Experimental", "b.16 CON:experimental"]
dado:
  - "un experimento interrumpido sin criterio de descarte declarado"
cuando:
  - "un agente nuevo intenta reanudarlo"
entonces:
  - "el método se reinicia desde el paso 1 y el criterio se declara antes de seguir"
falla_si:
  - "el criterio de descarte se escribe después de ver el resultado"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T108
nombre: Reanudación de un dosier sin repetir mediciones
cubre: ["VER/Dosier", "gate:evidencia-suficiente"]
dado:
  - "un dosier con parte de los criterios ya verificados"
cuando:
  - "un agente nuevo reanuda"
entonces:
  - "continúa por los criterios que faltan sin repetir mediciones registradas"
falla_si:
  - "se agregan criterios en un veredicto global, o se omite lo no comprobado"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T109
nombre: VER:decision detecta un impacto sin item derivado
cubre: ["VER/Decision", "b.16 VER:decision", "T71"]
dado:
  - "un DIR con un impacto conocido que ningún item derivado cubre"
cuando:
  - "se ejecuta VER/Decision"
entonces:
  - "el dictamen devuelve el DIR nombrando ese impacto y qué debería cubrir"
falla_si:
  - "el DIR cierra con un impacto sin propietario, o se rechaza por preferencia"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T110
nombre: Un despliegue no empieza sin reversión comprobada
cubre: ["ENT/Despliegue", "gate:entrega-observada"]
dado:
  - "un tipo de cambio sin procedimiento de reversión probado"
cuando:
  - "se intenta desplegar"
entonces:
  - "el paquete queda bloqueado y se crea el trabajo de construir la reversión"
falla_si:
  - "se despliega sin reversión disponible"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T111
nombre: Rollback autónomo sólo con los cinco requisitos
cubre: ["ENT/Contencion", "a.3 rollback autónomo"]
dado:
  - "una señal en rojo y un rollback que destruiría datos"
cuando:
  - "ENT evalúa revertir"
entonces:
  - "NO revierte: contiene el daño y escala con las opciones y su coste"
falla_si:
  - "se revierte sin comprobar los cinco requisitos, o se esconde la contención bajo un item cancelado"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T112
nombre: El Owner se convoca por lotes, no por item
cubre: ["USO/Validacion", "G36", "b.11"]
dado:
  - "tres validaciones pendientes que requieren al Owner"
cuando:
  - "USO prepara la validación"
entonces:
  - "se convoca una sola vez, con las tres ordenadas por coste de preparación y el estado preparado"
falla_si:
  - "se convoca al Owner tres veces, una por item"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T113
nombre: Un INV cierra sin generar un segundo item
cubre: ["INV/Investigacion", "T39", "b.16 INV"]
dado:
  - "una investigación que usa CON:experimental y produce evidencia"
cuando:
  - "la evidencia contesta la pregunta"
entonces:
  - "el item INV cierra con la evidencia como resultado, sin crear ningún item nuevo"
falla_si:
  - "se fuerza un item de producto para justificar la investigación"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T114
nombre: Un veto de seguridad sobrevive al cambio de agente
cubre: ["SEG/Condiciones", "veto:seguridad"]
dado:
  - "un veto de seguridad emitido sobre un paquete"
cuando:
  - "se releva al agente que lo emitió"
entonces:
  - "el veto sigue vigente y sólo se levanta con la mitigación comprobada"
falla_si:
  - "el veto desaparece al cambiar de agente, o se levanta sin mitigación"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T115
nombre: Una dependencia no se incorpora sin veredicto fechado
cubre: ["SEG/Dependencia", "G28"]
dado:
  - "una dependencia nueva propuesta por CON"
cuando:
  - "se ejecuta SEG/Dependencia"
entonces:
  - "existe entrada en DEPENDENCIAS.md con versión, fecha, veredicto y condición de revisión"
falla_si:
  - "se incorpora por ser popular, o sin mirar lo que arrastra"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T116
nombre: La maquinaria sólo cuenta si se reproduce desde cero
cubre: ["PLT/Maquinaria", "gate:maquinaria-disponible"]
dado:
  - "una pieza de maquinaria montada en un solo sitio"
cuando:
  - "se aplica su gate"
entonces:
  - "se ejecuta el procedimiento desde cero en otro sitio y funciona"
falla_si:
  - "se da por entregada una pieza que sólo funciona donde se montó"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T117
nombre: Sin aprendizaje promovible es un resultado legítimo
cubre: ["APR/Promocion", "gate:aprendizaje-fundado", "T20"]
dado:
  - "un item cerrado con una observación que ha ocurrido una sola vez y no es incidente"
cuando:
  - "APR la evalúa"
entonces:
  - "el veredicto es «sin aprendizaje promovible» y no se escribe regla en el ledger"
falla_si:
  - "se promueve a regla una sola ocurrencia no incidental"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T118
nombre: Toda ruta declara lo que no activó y por qué
cubre: ["DSP/Enrutamiento", "a.6 traza", "T05"]
dado:
  - "un item con ruta compuesta"
cuando:
  - "se lee su ficha de ruta"
entonces:
  - "cada capacidad no activada tiene su motivo escrito"
falla_si:
  - "existe una capacidad no activada sin motivo, o una activada que no cambió nada sin traza"
ejecucion: requiere-runtime
estado: contrato-definido
```

```yaml ads:escenario
id: T119
nombre: Continúa retoma sin pedir permiso ni resumen
cubre: ["DSP/Continua", "b.14", "T36"]
dado:
  - "un repositorio frío con trabajo en curso y sin conversación previa"
cuando:
  - "el Owner escribe «Continúa»"
entonces:
  - "DSP reconstruye, verifica, consume órdenes, reporta en pocas líneas y retoma desde el checkpoint"
falla_si:
  - "se pide permiso, se pide un resumen al Owner, o se responde con un informe en lugar de trabajar"
ejecucion: requiere-runtime
estado: contrato-definido
```

```yaml ads:escenario
id: T120
nombre: Ningún cambio del sistema entra sin validador ni estado real de prueba
cubre: ["SIS/Evolucion", "gate:sistema-conforme"]
dado:
  - "un cambio del kernel operativo"
cuando:
  - "se aplica su gate"
entonces:
  - "el cambio enlaza su regla de validador, o el motivo escrito de no ser automatizable, y su prueba declara estado real"
falla_si:
  - "se declara superada una prueba escrita, o se modifica una sección aprobada sin registrar la contradicción"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T121
nombre: La auditoría de conformidad no escribe contenido ajeno
cubre: ["SIS/Conformidad", "a.3 coherencia documental"]
dado:
  - "un corpus con un documento caduco propiedad de otra capacidad"
cuando:
  - "SIS ejecuta la auditoría"
entonces:
  - "se crea un item enrutado a la capacidad propietaria, y SIS no escribe el contenido"
falla_si:
  - "SIS reescribe el documento de otra capacidad, o sincroniza dos copias en vez de borrar una"
ejecucion: guion-manual
estado: contrato-definido
```
