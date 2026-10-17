# Contrato operativo — DIS/sistema-de-diseno

Lo que convierte [`../roles/sistema-de-diseno.md`](../roles/sistema-de-diseno.md)
en la auditoría obligatoria de reutilización con sus cinco salidas (§15) y en la custodia del sistema de tokens.

```yaml ads:contrato-operativo
id: contrato:dis-sistema-de-diseno
rol: DIS/sistema-de-diseno
mision_operativa: >
  Impedir que se cree un patrón nuevo sin haber buscado explícitamente sus equivalentes
  —componentes, patrones, superficies, acciones, layouts, dialogs, drawers, tablas,
  filtros, formularios, cabeceras, navegación, feedback, adjuntos— por lo que hacen y no
  por su nombre; clasificar la salida en una de las cinco de §15; detectar dos
  implementaciones que resuelven lo mismo como deuda de unificación; y mantener el sistema
  de tokens y componentes como la única sede de los valores.
conocimientos_exigibles:
  - "el sistema de diseño declarado: tokens, componentes, patrones y sus props de capacidad"
  - "las tres familias del frontend y el módulo equivalente del tenant"
  - "la memoria de diseño de la instancia: patrones creados, ampliados y deuda de unificación"
entradas_obligatorias:
  - que: "el análisis de uso y el informe de realidad actual"
    donde: "las entregas previas de DIS/investigacion-ux"
    si_falta: devolver
  - que: "el sistema de diseño vigente"
    donde: "docs/diseno/ del control repo y el código de componentes de la fuente"
    si_falta: bloquear
comprobaciones_previas:
  - id: memoria-consultada
    comprueba: "he leído la memoria de diseño: qué patrones se crearon, ampliaron o quedaron como deuda"
    como: "lectura de la memoria de diseño de la instancia"
    si_falla: devolver
  - id: busqueda-semantica
    comprueba: "he buscado equivalentes por lo que la superficie hace (entidad, acciones, estados, filtros), no por nombres"
    como: "recorrido de ui/, Shared/ y el módulo equivalente, y de las props de capacidad"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Buscar equivalentes de cada pieza nueva en componentes, patrones, superficies, acciones, layouts, dialogs, drawers, tablas, filtros, formularios, cabeceras, navegación, feedback y adjuntos"
    produce: "búsqueda de equivalentes"
    termina_cuando: "cada pieza tiene su lista de candidatos, o consta que no hay ninguno y dónde se buscó"
    checkpoint: true
  - n: 2
    hace: "Clasificar cada pieza en una de las cinco salidas: REUTILIZAR SIN CAMBIOS, REUTILIZAR AMPLIANDO, UNIFICAR IMPLEMENTACIONES EXISTENTES, REFACTORIZAR PATRÓN EXISTENTE, CREAR PATRÓN NUEVO"
    produce: "auditoría de reutilización"
    termina_cuando: "ninguna pieza queda sin salida y CREAR PATRÓN NUEVO lleva su justificación"
    checkpoint: true
  - n: 3
    hace: "Detectar implementaciones distintas que resuelven el mismo problema y declararlas deuda de unificación"
    produce: "deuda de unificación"
    termina_cuando: "cada pareja nombra las dos implementaciones y a cuál converger"
    checkpoint: true
  - n: 4
    hace: "Trazar los valores nuevos al sistema de tokens o proponer su ampliación"
    produce: "propuesta de tokens"
    termina_cuando: "ningún valor entra sin token o sin petición de ampliación"
    checkpoint: true
fuentes_a_consultar:
  - "src/components/ui/, src/components/Shared/ y el módulo equivalente de la fuente"
  - "docs/diseno/03-SISTEMA.md y 07-COMPONENTES.md del control repo"
  - "la regla frontend-replicar-es-reutilizar"
artefactos:
  - tipo: documento
    nombre: auditoría de reutilización
    estructura_minima:
      - "una fila por pieza: equivalentes encontrados, en qué familia, con qué capacidades"
      - "la salida de cada pieza entre las cinco de §15"
      - "la justificación de cada CREAR PATRÓN NUEVO"
      - "las parejas de implementaciones que resuelven lo mismo, como deuda de unificación"
      - "los valores nuevos y su token o petición de ampliación"
    obligatorio: true
evidencias_requeridas:
  - que: "los equivalentes citados existen y tienen las capacidades dichas"
    forma: "la ruta y las props citadas en la fuente"
    quien_la_puede_juzgar: "CNS/revision-de-construccion y DIS/revision-de-fidelidad"
  - que: "un CREAR PATRÓN NUEVO no tenía equivalente"
    forma: "la búsqueda que lo sostiene, con lo descartado y por qué"
    quien_la_puede_juzgar: "DIS/critica-visual"
criterios_de_calidad_medibles:
  - criterio: "cinco salidas"
    como_se_mide: "cien por cien de las piezas tienen una de las cinco salidas"
  - criterio: "crear justificado"
    como_se_mide: "cada CREAR PATRÓN NUEVO cita la búsqueda que no encontró equivalente"
  - criterio: "valores con token"
    como_se_mide: "cien por cien de los valores nuevos con token o petición"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y la auditoría completa"
  - "ningún CREAR PATRÓN NUEVO sin búsqueda documentada"
condiciones_de_devolucion:
  - "una pieza queda sin salida o un valor sin token: se devuelve al propio sistema"
  - "no hay análisis de uso: se devuelve a DIS/investigacion-ux"
reglas_de_escalado:
  - cuando: "una unificación cambia una decisión vigente del sistema"
    a_quien: "DIS/direccion-artistica"
    con_que: "la pareja a unificar y la decisión que toca"
incompatibilidades:
  - "no comparte trabajador con DIS/critica-visual ni con DIS/revision-de-fidelidad en el mismo item"
actuaciones_prohibidas:
  - "dar una pieza por nueva porque no encontró un componente con ese nombre"
  - "aceptar un valor fuera del sistema sin petición de ampliación"
  - "cerrar la auditoría con una pieza sin salida"
ejemplo_bueno: >
  Para el vacío del portal, la auditoría encuentra que Pedidos y Palets muestran dos
  vacíos distintos que resuelven lo mismo, los declara deuda de unificación, clasifica el
  nuevo como REUTILIZAR AMPLIANDO sobre EmptyState con una prop de acción, y traza el
  único color nuevo al token de aviso.
ejemplo_malo: >
  La auditoría busca «EmptyStateWithAction» por nombre, no lo encuentra, clasifica CREAR
  PATRÓN NUEVO sin mirar los dos vacíos que ya existen, y el producto acaba con tres
  formas de mostrar que no hay nada.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "cómo agrupa las piezas cuando la superficie es grande"
  - "qué unificación propone primero cuando hay varias"
metodos:
  - DIS/Fundacion
  - DIS/Reconstruccion
  - DIS/Evolucion
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: busqueda-por-lo-que-hace
    pregunta: "¿He buscado equivalentes por lo que la pieza hace, en las tres familias?"
    automatizable: parcial
  - id: cinco-salidas
    pregunta: "¿Cada pieza tiene una de las cinco salidas de §15?"
    automatizable: si
  - id: deuda-declarada
    pregunta: "¿Las implementaciones duplicadas están declaradas como deuda de unificación?"
    automatizable: si
  - id: valores-con-token
    pregunta: "¿Cada valor nuevo tiene token o petición de ampliación?"
    automatizable: si
  - id: memoria-leida
    pregunta: "¿He consultado la memoria de diseño antes de clasificar?"
    automatizable: parcial
```
