# T93–T98 — reanudación y conformidad de los métodos de Diseño

Las seis pruebas que los métodos de `DIS` citan en su `prueba_de_reanudacion`. Todas
comparten la misma exigencia: **un agente nuevo continúa sin repetir lo hecho y sin volver
a molestar al Owner por lo ya decidido.**

Su estado real está en [`REGISTRO-generado.md`](REGISTRO-generado.md).

```yaml ads:escenario
id: T93
nombre: Reanudación de DIS/Fundacion sin reproponer lo descartado
cubre: ["DIS/Fundacion", "a.10 checkpoint", "memoria:decisiones-de-diseno"]
dado:
  - "una fundación interrumpida tras el paso 5, con dos territorios ya rechazados por el Owner"
  - "un agente nuevo sin acceso a la conversación"
cuando:
  - "el agente nuevo abre el paquete y lee el checkpoint y la memoria de decisiones"
entonces:
  - "continúa en el paso 6 sin volver a proponer los territorios rechazados"
  - "no pide al Owner que repita su reacción a los territorios"
  - "las direcciones que explora citan el territorio aprobado del que salen"
falla_si:
  - "se vuelve a presentar un territorio ya rechazado"
  - "se pide al Owner que resuma la conversación anterior"
  - "el checkpoint no registraba el motivo del rechazo y el agente tiene que preguntarlo"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T94
nombre: Reanudación de DIS/Reconstruccion sin recapturar
cubre: ["DIS/Reconstruccion", "a.10 checkpoint"]
dado:
  - "un inventario de veinte superficies con doce ya capturadas en todos los entornos"
  - "un agente nuevo"
cuando:
  - "el agente nuevo reanuda el método"
entonces:
  - "continúa capturando las ocho que faltan, sin recapturar las doce registradas"
  - "la extracción de patrones usa el corpus completo, no sólo su tramo"
falla_si:
  - "se recapturan superficies ya registradas"
  - "la extracción de patrones se hace sólo sobre las capturas del segundo tramo"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T95
nombre: DIS/Evolucion no se reanuda sin rama declarada
cubre: ["DIS/Evolucion", "03-ESCALA-DE-NOVEDAD", "a.10 checkpoint"]
dado:
  - "un paquete de DIS/Evolucion interrumpido cuyo checkpoint NO declara el nivel de novedad"
cuando:
  - "un agente nuevo intenta reanudarlo"
entonces:
  - "el método se reinicia desde el paso 1 y se vuelve a determinar el nivel"
  - "queda registrado que hubo reinicio y por qué"
falla_si:
  - "el agente entrante deduce la rama de lo que ve y continúa"
  - "se elige un nivel inferior al que la escala determina, para ahorrar exploración"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T96
nombre: La crítica visual no dictamina sin comparación con la categoría
cubre: ["DIS/CriticaVisual", "rubrica:excelencia-visual", "gate:excelencia-visual"]
dado:
  - "una crítica interrumpida con los ejes automatizables ya evaluados y el paso 2 sin hacer"
cuando:
  - "un agente nuevo reanuda la crítica"
entonces:
  - "ejecuta la comparación con dos productos genéricos de la categoría antes de dictaminar"
  - "el eje personalidad sólo recibe nivel después de esa comparación"
falla_si:
  - "se emite el dictamen con el eje personalidad evaluado sin comparación escrita"
  - "el dictamen contiene una propuesta de solución"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T97
nombre: Reanudación de la revisión de fidelidad sin recapturar entornos
cubre: ["DIS/RevisionDeFidelidad", "05-FIDELIDAD"]
dado:
  - "una comparación con tres de cinco entornos de la matriz ya comparados"
  - "un agente nuevo"
cuando:
  - "el agente nuevo reanuda"
entonces:
  - "compara los dos entornos que faltan y emite un veredicto sobre los cinco"
  - "las duraciones de movimiento están medidas sobre grabación, también en su tramo"
falla_si:
  - "se emite veredicto habiendo comparado sólo un subconjunto de la matriz"
  - "se acepta como deuda una diferencia descubierta durante esta comparación"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T98
nombre: La validación de uso no reconvoca al Owner por lo ya observado
cubre: ["DIS/ValidacionDeUso", "rubrica:usabilidad", "G36"]
dado:
  - "un plan de validación con dos tareas observadas y una pendiente"
  - "un agente nuevo"
cuando:
  - "el agente nuevo reanuda la validación"
entonces:
  - "convoca al Owner una sola vez, para la tarea pendiente y las demás del lote"
  - "el dictamen declara expresamente los ejes que no se pudieron evaluar"
falla_si:
  - "se vuelve a pedir al Owner que ejecute una tarea ya observada"
  - "se declara excelente un eje que exige observación sin haberla habido"
  - "se omiten del dictamen los ejes no evaluados"
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T99
nombre: Una interfaz usable puede ser rechazada por el gate visual
cubre: ["gate:usabilidad", "gate:excelencia-visual", "los dos gates independientes"]
dado:
  - "una superficie que pasa los seis ejes de usabilidad en nivel suficiente o superior"
  - "esa misma superficie resuelta con los valores por defecto de la herramienta usada"
cuando:
  - "se aplica gate:excelencia-visual"
entonces:
  - "el eje personalidad o el eje intencion queda en rechazo"
  - "el paquete NO pasa, con el gate de usabilidad íntegramente en verde"
  - "el rechazo vuelve a la exploración, no al prototipo"
falla_si:
  - "el gate visual se cierra porque el de usabilidad está en verde"
  - "el rechazo por personalidad se trata como una lista de retoques"
ejecucion: requiere-juicio-humano
estado: contrato-definido
```
