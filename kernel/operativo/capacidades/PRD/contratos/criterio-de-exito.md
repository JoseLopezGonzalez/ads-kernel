# Contrato operativo — PRD/criterio-de-exito

Lo que convierte [`../roles/criterio-de-exito.md`](../roles/criterio-de-exito.md) en
criterios que un tercero comprueba sin preguntar a quien los escribió.

```yaml ads:contrato-operativo
id: contrato:prd-criterio-de-exito
rol: PRD/criterio-de-exito
mision_operativa: >
  Escribir, sobre el alcance ya declarado, qué tendrá que ser cierto para dar el item por
  hecho —criterio a criterio, con qué se mira y dónde— y qué lo convertiría en un fracaso
  aunque funcione técnicamente, de modo que VER pueda verificarlo y el Owner aceptarlo sin
  preguntar.
conocimientos_exigibles:
  - "qué hace que un criterio sea comprobable por un tercero: qué se mira, dónde y qué se espera ver"
  - "la definición de éxito y los criterios de fallo del Owner en el PROFILE"
  - "la diferencia entre un criterio medible y un juicio que sólo el Owner puede emitir"
entradas_obligatorias:
  - que: "el alcance declarado de PRD/definicion con su fuera de alcance"
    donde: "el handoff emitido a este paquete, o la entrega previa del item"
    si_falta: devolver
  - que: "la evidencia de cierre que el Owner declaró en la entrada"
    donde: "el encuadre del item"
    si_falta: bloquear
comprobaciones_previas:
  - id: alcance-cerrado
    comprueba: "el alcance tiene fuera de alcance explícito; no se escribe criterio sobre un alcance abierto"
    como: "lectura del documento de alcance buscando la lista de fuera"
    si_falla: devolver
  - id: evidencia-declarada-cabe
    comprueba: "la evidencia de cierre del Owner es alcanzable con el alcance declarado"
    como: "cruce de cada evidencia de cierre con lo que entra en el alcance"
    si_falla: escalar
secuencia:
  - n: 1
    hace: "Escribir un criterio por resultado observable: qué se mira, dónde, y qué se espera ver"
    produce: "lista de criterios de éxito"
    termina_cuando: "cada criterio dice qué, dónde y qué se ve, sin adjetivos"
    checkpoint: true
  - n: 2
    hace: "Para cada criterio, declarar la evidencia que se considerará suficiente y quién la puede juzgar"
    produce: "criterio → evidencia suficiente → quién juzga"
    termina_cuando: "ningún criterio queda sin evidencia declarada"
    checkpoint: true
  - n: 3
    hace: "Escribir la definición de fracaso: qué haría que el item fuera un fracaso aunque funcione"
    produce: "definición de fracaso"
    termina_cuando: "cita al menos un criterio de fallo del Owner o explica por qué ninguno aplica"
    checkpoint: false
  - n: 4
    hace: "Marcar los criterios que dependen del juicio del Owner y prepararlos para su cola de validación"
    produce: "criterios marcados para el Owner, con qué tendría que ver"
    termina_cuando: "cada criterio de juicio dice qué vería el Owner para darlo por bueno"
    checkpoint: true
fuentes_a_consultar:
  - "PROFILE.md §1 y §13"
  - "el alcance declarado del item"
  - "docs/verificacion/COBERTURA.md, para no repetir un criterio que ya se mide"
artefactos:
  - tipo: documento
    nombre: criterios de éxito y fracaso
    estructura_minima:
      - "una fila por criterio: qué se mira, dónde, qué se espera ver, evidencia suficiente, quién juzga"
      - "la definición de fracaso, citando el criterio de fallo del Owner"
      - "los criterios que exigen juicio del Owner, marcados"
    obligatorio: true
evidencias_requeridas:
  - que: "cada criterio es comprobable por un tercero"
    forma: "la fila del criterio con sus tres columnas rellenas"
    quien_la_puede_juzgar: "VER/dosier, que tendrá que verificarlo"
criterios_de_calidad_medibles:
  - criterio: "sin adjetivos"
    como_se_mide: "ningún criterio contiene «bien», «rápido», «correcto» o «adecuado» sin una medida"
  - criterio: "cobertura del alcance"
    como_se_mide: "cada elemento que entra en el alcance tiene al menos un criterio"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y el documento con sus tres partes"
  - "cada elemento del alcance tiene al menos un criterio, y ningún criterio lleva adjetivo sin medida"
condiciones_de_devolucion:
  - "el alcance no tiene fuera explícito: se devuelve a PRD/definicion"
  - "la evidencia de cierre del Owner no cabe en el alcance y el Owner no ha decidido: se devuelve a ENC"
reglas_de_escalado:
  - cuando: "un criterio depende de un juicio que sólo el Owner puede emitir"
    a_quien: "el Owner, por la cola de validación por lotes"
    con_que: "el criterio en una frase y qué tendría que ver él para darlo por bueno"
  - cuando: "la evidencia de cierre declarada por el Owner no cabe en el alcance"
    a_quien: "el Owner"
    con_que: "la evidencia, el alcance, y la diferencia"
incompatibilidades:
  - "no comparte trabajador con PRD/definicion en items de primera dirección de producto"
actuaciones_prohibidas:
  - "escribir un criterio que sólo su autor sabe verificar"
  - "redefinir el alcance para que el criterio salga"
  - "dar por comprobable un juicio del Owner"
ejemplo_bueno: >
  Sobre el alcance «CSV de la tabla filtrada», el criterio dice: en la pantalla de stock,
  con el filtro «almacén 2» puesto, el botón Exportar descarga un CSV cuyas filas coinciden
  una a una con la tabla visible; evidencia suficiente: el CSV y la captura de la tabla;
  juzga VER. Fracaso: que el gestor siga exportando a mano porque el CSV no abre en su
  hoja —criterio de fallo 1 del Owner—.
ejemplo_malo: >
  «La exportación funciona correctamente y es rápida.» Nadie sabe qué mirar, dónde, ni
  cuánto es rápido, y VER inventa el criterio al verificar.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "la formulación de cada criterio de éxito"
  - "la definición de fracaso"
  - "qué evidencia se considerará suficiente para cada criterio"
metodos:
  - PRD/Definicion
  - PRD/Gap
no_autocertifica:
  - gate:intencion-definida
checklist:
  - id: que-donde-que-se-ve
    pregunta: "¿Cada criterio dice qué se mira, dónde y qué se espera ver?"
    automatizable: parcial
  - id: evidencia-por-criterio
    pregunta: "¿Cada criterio tiene su evidencia suficiente y quién la juzga?"
    automatizable: si
  - id: fracaso-escrito
    pregunta: "¿La definición de fracaso está escrita y cita el criterio de fallo del Owner?"
    automatizable: si
  - id: juicio-del-owner-marcado
    pregunta: "¿Los criterios que exigen juicio del Owner están marcados con qué tendría que ver?"
    automatizable: parcial
  - id: cobertura-del-alcance
    pregunta: "¿Cada elemento que entra en el alcance tiene al menos un criterio?"
    automatizable: si
```
