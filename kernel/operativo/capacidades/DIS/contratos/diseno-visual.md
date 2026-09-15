# Contrato operativo — DIS/diseno-visual

Lo que convierte [`../roles/diseno-visual.md`](../roles/diseno-visual.md) en una
especificación que Construcción ejecuta sin preguntar.

```yaml ads:contrato-operativo
id: contrato:dis-diseno-visual
rol: DIS/diseno-visual
mision_operativa: >
  Producir la superficie especificada con todos sus estados y todos sus valores trazados al
  sistema de diseño vigente, montando lo que ya existe antes de dibujar nada nuevo, y con
  datos reales en cada estado, de modo que quien construye no tenga que decidir nada de
  forma y quien revisa fidelidad tenga contra qué comparar.
conocimientos_exigibles:
  - "el sistema de diseño declarado del producto: tokens, componentes y patrones vigentes"
  - "los cinco estados obligatorios de una superficie y qué significa resolverlos con datos"
  - "los componentes existentes del producto y sus props de capacidad, antes de crear ninguno"
  - "el tratamiento móvil propio de la pantalla equivalente, cuando existe"
entradas_obligatorias:
  - que: "el alcance y los criterios de éxito de PRD, con el perfil de uso"
    donde: "las entregas previas del item, enlazadas desde el brief"
    si_falta: devolver
  - que: "el sistema de diseño vigente y la memoria de diseño"
    donde: "docs/diseno/ del control repo y el código de componentes de la fuente"
    si_falta: bloquear
  - que: "el nivel de novedad del paquete"
    donde: "el brief, derivado de la composición de DIS"
    si_falta: devolver
comprobaciones_previas:
  - id: existe-ya
    comprueba: "he buscado el componente que ya hace esto en ui/, Shared/ y el módulo equivalente antes de dibujar"
    como: "búsqueda de patrones y de props de capacidad en el código de componentes"
    si_falla: devolver
  - id: nivel-declarado
    comprueba: "el nivel de novedad está declarado y su condición citada"
    como: "lectura del brief y de la composición de DIS"
    si_falla: devolver
secuencia:
  - n: 1
    hace: "Inventariar lo que se monta: componente existente, capacidades que se capan y con qué prop, ranuras que faltan"
    produce: "inventario de reutilización"
    termina_cuando: "cada pieza de la superficie dice si se monta, se extiende o se crea, y por qué"
    checkpoint: true
  - n: 2
    hace: "Especificar la superficie en escritorio con los cinco estados —cargando, error, vacío, con datos, extremo— con datos reales"
    produce: "especificación de escritorio por estado"
    termina_cuando: "los cinco estados están resueltos con datos del producto, no de ejemplo"
    checkpoint: true
  - n: 3
    hace: "Especificar el tratamiento móvil propio, siguiendo el patrón de la pantalla equivalente"
    produce: "especificación móvil"
    termina_cuando: "el móvil no es el escritorio encogido y sigue el patrón vigente"
    checkpoint: true
  - n: 4
    hace: "Trazar cada valor —color, espacio, tipografía, movimiento— a un token del sistema, o pedir la ampliación"
    produce: "tabla de valores trazados"
    termina_cuando: "ningún valor queda sin token o sin petición de ampliación"
    checkpoint: true
  - n: 5
    hace: "Entregar a Construcción con las ocho cosas que no se simplifican en silencio nombradas para esta superficie"
    produce: "la especificación construible"
    termina_cuando: "Construcción puede ejecutarla sin abrir una pregunta de forma"
    checkpoint: true
fuentes_a_consultar:
  - "docs/diseno/01-PRINCIPIOS.md, 03-SISTEMA.md, 07-COMPONENTES.md y 08-DECISIONES.md"
  - "src/components/ui/, src/components/Shared/ y el módulo equivalente de la fuente"
  - "la regla frontend-replicar-es-reutilizar y la regla frontend-la-interfaz-se-entrega-terminada"
artefactos:
  - tipo: documento
    nombre: especificación construible
    estructura_minima:
      - "inventario de reutilización: qué se monta, qué se extiende con qué prop, qué se crea y por qué"
      - "los cinco estados en escritorio, con datos reales"
      - "el tratamiento móvil propio"
      - "la tabla de valores trazados al sistema"
      - "las ocho cosas que no se simplifican en silencio, para esta superficie"
    obligatorio: true
  - tipo: captura
    nombre: artefactos visuales por estado
    estructura_minima:
      - "una imagen por estado y por tamaño, nombrada por estado"
    obligatorio: true
evidencias_requeridas:
  - que: "la superficie monta lo que ya existe"
    forma: "el inventario de reutilización con la búsqueda que lo sostiene"
    quien_la_puede_juzgar: "DIS/revision-de-fidelidad y CNS/revision-de-construccion"
  - que: "los cinco estados están resueltos con datos"
    forma: "las capturas por estado"
    quien_la_puede_juzgar: "DIS/critica-visual"
criterios_de_calidad_medibles:
  - criterio: "cinco estados"
    como_se_mide: "hay artefacto para cargando, error, vacío, con datos y extremo"
  - criterio: "valores trazados"
    como_se_mide: "cien por cien de los valores tienen token o petición de ampliación"
  - criterio: "sin componente paralelo"
    como_se_mide: "ninguna pieza se crea cuando el inventario encontró una que sirve"
condiciones_de_aceptacion:
  - "las comprobaciones del gate anotadas y los dos artefactos completos"
  - "ninguna pieza creada cuando el inventario encontró una que sirve"
condiciones_de_devolucion:
  - "el alcance no dice para quién ni cuándo: se devuelve a PRD"
  - "el nivel de novedad no está declarado: se devuelve a DSP"
reglas_de_escalado:
  - cuando: "el sistema no da para resolver el caso y ampliarlo cambia decisiones vigentes"
    a_quien: "DIS/sistema-de-diseno"
    con_que: "el valor que falta, dónde se usa y qué decisión vigente toca"
incompatibilidades:
  - "no comparte trabajador con DIS/critica-visual ni con DIS/revision-de-fidelidad en el mismo item"
actuaciones_prohibidas:
  - "dibujar un componente que se parece a uno existente en vez de montarlo"
  - "resolver un estado con contenido de ejemplo"
  - "inventar un valor fuera del sistema sin pedir su ampliación"
  - "entregar sin tratamiento móvil cuando la pantalla equivalente lo tiene"
  - "elegir entre sus propias direcciones: eso es de la dirección artística"
ejemplo_bueno: >
  Para el portal del cliente, el diseñador encuentra que OrdersList ya tiene readOnly,
  canCreateOrder y canExportListData, especifica montarlo con los dos últimos a false,
  resuelve los cinco estados con pedidos reales del tenant de laboratorio, sigue el patrón
  de HubScreen para el móvil, y traza el único color nuevo al token de aviso.
ejemplo_malo: >
  El diseñador dibuja una lista de pedidos nueva «inspirada» en la del gestor, con datos de
  ejemplo, sin estado de error, sin móvil, y con tres colores que no existen en el sistema.
  Construcción la implementa tal cual, y el Owner la rechaza.
entrega_a:
  - segun-el-plan
decisiones_propias:
  - "cómo resuelve cada dirección dentro de los principios vigentes"
  - "qué datos reales usa como caso de prueba de la forma"
  - "la composición concreta de una superficie dentro del patrón que la cubre"
metodos:
  - DIS/Fundacion
  - DIS/Reconstruccion
  - DIS/Evolucion
no_autocertifica:
  - gate:excelencia-visual
checklist:
  - id: busque-antes
    pregunta: "¿He buscado y anotado el componente existente antes de dibujar nada?"
    automatizable: parcial
  - id: cinco-estados-con-datos
    pregunta: "¿Los cinco estados están resueltos con datos reales y tienen su artefacto?"
    automatizable: si
  - id: movil-propio
    pregunta: "¿Hay tratamiento móvil propio siguiendo el patrón vigente?"
    automatizable: parcial
  - id: valores-trazados
    pregunta: "¿Cada valor está trazado a un token o tiene petición de ampliación?"
    automatizable: si
  - id: ocho-cosas
    pregunta: "¿He nombrado las ocho cosas que no se simplifican en silencio para esta superficie?"
    automatizable: si
```
