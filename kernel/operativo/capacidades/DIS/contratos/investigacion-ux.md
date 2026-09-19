# Contrato operativo — DIS/investigacion-ux

Lo que convierte [`../roles/investigacion-ux.md`](../roles/investigacion-ux.md)
en el informe de realidad actual y el análisis de uso que la Directiva del Owner exige antes de dibujar (§12, §14).

```yaml ads:contrato-operativo
id: contrato:dis-investigacion-ux
rol: DIS/investigacion-ux
mision_operativa: >
  Reconstruir la realidad actual de la superficie dentro del producto real —qué existe,
  qué funciona, qué no, qué patrones usa, qué inconsistencias hay, qué equivalentes
  existen, qué restricciones hay— y resolver el problema de uso antes de que nadie dibuje:
  quién usa, qué intenta, qué es primario, qué sale mal y cómo se recupera, con los
  estados y los extremos que hay que estudiar.
conocimientos_exigibles:
  - "las superficies existentes del producto y su navegación, permisos y versión móvil"
  - "las tres familias donde vive casi todo el frontend: ui/, Shared/ y el módulo equivalente del tenant"
  - "los datos reales del tenant de laboratorio y sus extremos (cantidad mínima, máxima razonable, nombres largos)"
  - "las decisiones anteriores de diseño y la memoria de diseño de la instancia"
entradas_obligatorias:
  - que: "el alcance y los criterios de éxito de PRD"
    donde: "las entregas previas del item, enlazadas desde el brief"
    si_falta: devolver
  - que: "acceso a la aplicación real o a su preview con datos representativos"
    donde: "el workspace de fuentes y el entorno declarado por la instancia"
    si_falta: bloquear
comprobaciones_previas:
  - id: producto-real
    comprueba: "he abierto la pantalla actual y las anteriores y posteriores del flujo, no sólo su código"
    como: "recorrido en la aplicación o preview, con capturas"
    si_falla: devolver
  - id: equivalentes-buscados
    comprueba: "he buscado las superficies equivalentes en las tres familias antes de escribir el informe"
    como: "búsqueda por lo que la superficie hace, no por nombres de componente"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Recorrer la pantalla actual, el flujo completo y las pantallas anteriores y posteriores, con permisos y dispositivo distintos"
    produce: "recorrido documentado"
    termina_cuando: "cada pantalla del flujo tiene su captura y su nota"
    checkpoint: true
  - n: 2
    hace: "Escribir el informe de realidad actual: qué existe, qué funciona, qué no, qué patrones usa, qué inconsistencias hay, qué equivalentes hay, qué restricciones hay"
    produce: "informe de realidad actual"
    termina_cuando: "los siete apartados de §12 están escritos con evidencia, no con opinión"
    checkpoint: true
  - n: 3
    hace: "Resolver el problema de uso: quién usa, qué intenta, tarea primaria, información primero, acciones frecuentes y excepcionales, qué sale mal y cómo se recupera, qué compara y localiza, qué cambia por permisos y por dispositivo"
    produce: "análisis de uso"
    termina_cuando: "las doce preguntas de §14 tienen respuesta con datos reales"
    checkpoint: true
  - n: 4
    hace: "Enumerar los estados y extremos que Diseño tiene que estudiar: inicial, loading, vacío, error, éxito, cantidad mínima y máxima, datos extremos, móvil, escritorio, teclado"
    produce: "lista de estados y extremos"
    termina_cuando: "los once casos de §14 están nombrados con el dato real que los provoca"
    checkpoint: true
fuentes_a_consultar:
  - "la aplicación real o su preview, con el tenant de laboratorio"
  - "src/components/ui/, src/components/Shared/ y el módulo equivalente de la fuente"
  - "docs/diseno/ del control repo y la memoria de diseño"
artefactos:
  - tipo: documento
    nombre: informe de realidad actual
    estructura_minima:
      - "qué existe y qué funciona"
      - "qué no funciona, con evidencia"
      - "qué patrones utiliza y qué inconsistencias hay"
      - "qué elementos equivalentes se han localizado, en qué familia y con qué capacidades"
      - "qué restricciones existen (técnicas, de permisos, de datos)"
    obligatorio: true
  - tipo: documento
    nombre: análisis de uso
    estructura_minima:
      - "quién usa la interfaz y qué intenta conseguir"
      - "tarea primaria, información necesaria primero, acciones frecuentes y excepcionales"
      - "qué puede salir mal y cómo se recupera"
      - "qué necesita comparar y localizar rápidamente"
      - "qué cambia por permisos y por dispositivo"
      - "los estados y extremos que hay que estudiar, con el dato real de cada uno"
    obligatorio: true
  - tipo: captura
    nombre: recorrido del flujo actual
    estructura_minima:
      - "una captura por pantalla del flujo, en escritorio y móvil"
    obligatorio: true
evidencias_requeridas:
  - que: "el informe describe el producto real y no un producto imaginado"
    forma: "las capturas del recorrido con fecha y tenant"
    quien_la_puede_juzgar: "DIS/critica-visual y DIS/diseno-visual"
  - que: "los equivalentes localizados existen"
    forma: "la ruta de cada componente citado en la fuente"
    quien_la_puede_juzgar: "cualquiera con acceso a la fuente"
criterios_de_calidad_medibles:
  - criterio: "siete apartados del informe"
    como_se_mide: "los siete apartados de §12 tienen contenido con evidencia"
  - criterio: "doce preguntas de uso"
    como_se_mide: "las doce preguntas de §14 tienen respuesta con datos reales"
  - criterio: "once estados y extremos"
    como_se_mide: "cada uno nombrado con el dato que lo provoca"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y los tres artefactos completos"
  - "ningún apartado resuelto con «no aplica» sin decir por qué"
condiciones_de_devolucion:
  - "el alcance de PRD no dice para quién: se devuelve a PRD"
  - "no hay acceso a la aplicación real ni a datos representativos: se bloquea"
reglas_de_escalado:
  - cuando: "la realidad actual contradice el alcance de PRD"
    a_quien: "PRD/definicion"
    con_que: "el informe con la contradicción marcada"
incompatibilidades:
  - "no comparte trabajador con DIS/validacion-de-uso en el mismo item"
actuaciones_prohibidas:
  - "describir la pantalla desde su código sin abrirla"
  - "inventar el uso sin datos reales"
  - "dar por inexistente un equivalente sin haberlo buscado por lo que hace"
ejemplo_bueno: >
  Para el portal del cliente de maquila, la investigadora recorre el gestor de pedidos del
  tenant y el portal actual, anota que OrdersList ya admite readOnly y canExportListData,
  mide con pedidos reales que la lista larga supera las 200 filas, y escribe que el portal
  actual no distingue error de vacío.
ejemplo_malo: >
  El informe dice «el portal muestra pedidos» leído del código, sin abrir la aplicación;
  no nombra OrdersList; el análisis de uso inventa que el cliente quiere filtrar por
  fecha; el vacío y el error no se estudian y aparecen después como sorpresa en
  producción.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "qué tenant y qué datos reales usa como caso de estudio"
  - "cómo agrupa el recorrido cuando el flujo es largo"
metodos:
  - DIS/Fundacion
  - DIS/Reconstruccion
  - DIS/Evolucion
no_autocertifica:
  - gate:usabilidad
checklist:
  - id: producto-abierto
    pregunta: "¿He abierto la aplicación real y recorrido el flujo entero antes de escribir?"
    automatizable: parcial
  - id: siete-apartados
    pregunta: "¿El informe de realidad tiene los siete apartados con evidencia?"
    automatizable: si
  - id: doce-preguntas
    pregunta: "¿El análisis de uso contesta las doce preguntas con datos reales?"
    automatizable: si
  - id: estados-y-extremos
    pregunta: "¿Están nombrados los once estados y extremos con su dato?"
    automatizable: si
  - id: equivalentes-por-lo-que-hacen
    pregunta: "¿He buscado los equivalentes por lo que hacen, en las tres familias?"
    automatizable: parcial
```
