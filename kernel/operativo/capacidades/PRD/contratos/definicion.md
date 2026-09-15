# Contrato operativo — PRD/definicion

Lo que convierte [`../roles/definicion.md`](../roles/definicion.md) en un alcance que dos
definidores competentes escriben igual.

```yaml ads:contrato-operativo
id: contrato:prd-definicion
rol: PRD/definicion
mision_operativa: >
  Escribir qué entra y qué NO entra en el item, para quién es y en qué momento se usa,
  enlazado con la definición de éxito del Owner, de modo que ninguna capa posterior tenga
  que adivinarlo ni preguntarlo.
conocimientos_exigibles:
  - "la definición de éxito del Owner en el PROFILE, con sus criterios de fallo"
  - "la dirección de producto vigente que cubre el item, leída de la memoria de producto"
  - "la diferencia entre alcance rutinario y alcance que cambia lo que el producto es"
entradas_obligatorias:
  - que: "la entrada del Owner con su expresión literal, su resultado perseguido y su evidencia de cierre"
    donde: "el encuadre del item, enlazado desde el brief"
    si_falta: bloquear
  - que: "la definición de éxito del Owner y los principios de producto"
    donde: "PROFILE.md §1 y §4 del control repo"
    si_falta: bloquear
comprobaciones_previas:
  - id: direccion-cubre
    comprueba: "existe una dirección de producto aprobada que cubre este item, o el item es de primera dirección"
    como: "búsqueda del ámbito del item en la memoria de producto y en el PROFILE"
    si_falla: escalar
  - id: un-solo-resultado
    comprueba: "el item persigue UN resultado; si persigue dos, se parte antes de definir"
    como: "lectura del resultado perseguido buscando conjunciones que escondan dos entregas"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Nombrar para quién es y en qué momento de uso entra, con el perfil de uso real"
    produce: "perfil de uso y momento"
    termina_cuando: "un tercero puede decir quién lo usa y cuándo sin preguntar"
    checkpoint: true
  - n: 2
    hace: "Escribir lo que ENTRA y, con la misma precisión, lo que queda FUERA, y qué se gana dejándolo fuera"
    produce: "alcance declarado con fuera de alcance explícito"
    termina_cuando: "cada frontera dudosa tiene una línea que la resuelve"
    checkpoint: true
  - n: 3
    hace: "Enlazar el alcance con la definición de éxito del Owner: qué criterio de éxito sirve y cuál sería el fracaso aunque funcione"
    produce: "enlace con éxito del Owner"
    termina_cuando: "el enlace cita el criterio del PROFILE por su número"
    checkpoint: false
  - n: 4
    hace: "Decidir si el alcance es rutinario o relevante; si es relevante, escalar al Owner ANTES de entregar"
    produce: "la clasificación del alcance y, cuando es relevante, la pregunta al Owner"
    termina_cuando: "el alcance está clasificado y la escalada, si la hay, emitida"
    checkpoint: true
fuentes_a_consultar:
  - "PROFILE.md §1, §4 y §8"
  - "docs/producto/DIRECCION.md y docs/producto/MEMORIA.md"
  - "el histórico de items del mismo ámbito"
artefactos:
  - tipo: documento
    nombre: alcance declarado
    estructura_minima:
      - "para quién y en qué momento de uso"
      - "qué entra, en una lista corta"
      - "qué queda fuera, en una lista corta, con lo que se gana"
      - "enlace con la definición de éxito del Owner, citada"
      - "clasificación del alcance: rutinario o relevante"
    obligatorio: true
evidencias_requeridas:
  - que: "el fuera de alcance es explícito y no se infiere"
    forma: "la lista de fuera de alcance del documento"
    quien_la_puede_juzgar: "PRD/criterio-de-exito, al escribir el criterio"
  - que: "el enlace con el éxito del Owner cita el criterio"
    forma: "la cita del PROFILE en el documento"
    quien_la_puede_juzgar: "cualquiera con el PROFILE delante"
criterios_de_calidad_medibles:
  - criterio: "sin adivinar"
    como_se_mide: "ninguna capa posterior abre una pregunta de alcance sobre este item"
  - criterio: "fuera de alcance no vacío"
    como_se_mide: "la lista de fuera de alcance tiene al menos una entrada con su ganancia"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y el documento con sus cinco partes"
  - "el alcance clasificado, y escalado al Owner antes de entregar cuando es relevante"
condiciones_de_devolucion:
  - "el item persigue dos resultados: se devuelve a ENC para partirlo"
  - "la entrada no dice qué se persigue: se devuelve a ENC"
reglas_de_escalado:
  - cuando: "el alcance cambia lo que el producto es, o es la primera dirección de producto"
    a_quien: "el Owner"
    con_que: "qué entra y qué no, en una lista corta, con lo que se gana al dejar algo fuera"
  - cuando: "el anclaje demuestra que lo pedido ya está resuelto"
    a_quien: "el Owner"
    con_que: "la evidencia de que ya existe y la propuesta de cancelar"
incompatibilidades:
  - "no comparte trabajador con PRD/criterio-de-exito en items de primera dirección de producto"
actuaciones_prohibidas:
  - "ampliar el alcance en silencio porque «ya que estamos»"
  - "dejar el fuera de alcance vacío o implícito"
  - "decidir un alcance relevante sin el Owner"
  - "escribir criterios de éxito: eso es del otro rol"
ejemplo_bueno: >
  El definidor lee la entrada «que el gestor exporte la tabla», nombra al gestor de
  almacén en el cierre de jornada, declara que entra el CSV de la tabla filtrada y que
  queda fuera el Excel con formato y la exportación programada —se gana no abrir una
  dependencia nueva—, enlaza con el criterio 1 del PROFILE, lo clasifica rutinario y
  entrega.
ejemplo_malo: >
  El definidor escribe «exportar la tabla en los formatos habituales» sin decir quién,
  cuándo ni qué queda fuera; Construcción elige Excel, el Owner quería CSV, y el fuera de
  alcance se descubre en la aceptación.
checklist:
  - id: para-quien-y-cuando
    pregunta: "¿He nombrado para quién es y en qué momento de uso entra?"
    automatizable: parcial
  - id: fuera-explicito
    pregunta: "¿El fuera de alcance está escrito, con lo que se gana al dejarlo fuera?"
    automatizable: si
  - id: enlace-citado
    pregunta: "¿He citado el criterio de éxito del Owner que sirve este item?"
    automatizable: si
  - id: alcance-clasificado
    pregunta: "¿He clasificado el alcance y, si es relevante, he escalado antes de entregar?"
    automatizable: parcial
  - id: un-resultado
    pregunta: "¿El item persigue un solo resultado, o lo he devuelto para partirlo?"
    automatizable: parcial
```
