# ARQ/Encaje — medir antes de planificar

```yaml ads:metodo
id: ARQ/Encaje
nombre: Encaje
capacidad: ARQ
disparador:
  - "DSP despacha un paquete de ARQ sobre un item que cumple C-ARQ"
carga:
  - "la capa de PRD: alcance, fuera de alcance y criterios"
  - "la especificación de DIS cuando existe"
  - "docs/arquitectura/MAPA.md, los ADR vigentes y CONVENTIONS.md"
  - "el repositorio completo"
preguntas_iniciales:
  - "¿qué contratos toca esto, y quién los consume hoy?"
  - "¿qué se rompe si me equivoco en la descomposición?"
  - "¿hay un ADR vigente que ya decidió parte de esto?"
pasos:
  - n: 1
    nombre: MEDIR EL RADIO
    modo: lineal
    hace: >
      Buscar en el repositorio quién consume cada elemento que se toca, hasta cerrar la
      lista. Se registra cada búsqueda y su salida.
    produce: "lista de ficheros y contratos afectados, con la traza de búsquedas"
    termina_cuando: "ninguna búsqueda nueva añade elementos a la lista"
    checkpoint: true
  - n: 2
    nombre: DECLARAR CONTRATOS
    modo: lineal
    hace: >
      Escribir qué contratos, endpoints o esquemas cambian, quién depende de ellos y si el
      cambio es compatible hacia atrás.
    produce: "declaración de contratos afectados"
    termina_cuando: "cada contrato afectado tiene sus consumidores identificados"
    checkpoint: true
  - n: 3
    nombre: ALTERNATIVAS
    modo: divergente
    hace: >
      Producir al menos dos caminos con su coste: esfuerzo, riesgo, deuda que crean y qué
      cierran para el futuro.
    produce: "alternativas con coste"
    termina_cuando: >
      hay dos o más alternativas con coste escrito, o está demostrado por qué sólo existe
      un camino
    checkpoint: true
  - n: 4
    nombre: ELEGIR Y REGISTRAR
    modo: convergente
    hace: >
      Elegir con motivo escrito. Si la decisión es difícilmente reversible, escribir ADR con
      contexto, decisión, alternativas y consecuencias.
    produce: "elección con motivo, y ADR cuando corresponde"
    termina_cuando: "el motivo está escrito y el ADR existe si la decisión lo exigía"
    checkpoint: true
  - n: 5
    nombre: DESCOMPONER
    modo: convergente
    hace: >
      Partir el trabajo en paquetes con orden y dependencias, comprobando las seis
      condiciones de a.5 para declarar qué puede ir en paralelo.
    produce: "grafo de paquetes con dependencias y paralelismo declarado"
    termina_cuando: "el grafo es acíclico y cada par declarado paralelo cumple las seis condiciones"
    checkpoint: true
artefactos:
  - "traza de búsquedas y radio medido"
  - "declaración de contratos"
  - "alternativas con coste"
  - "ADR cuando corresponde"
  - "grafo de paquetes"
puntos_owner:
  - "ninguno directo: ARQ escala a PRD, que traduce el coste a consecuencias de producto"
consultas:
  - "DOM: ¿este cambio de esquema es reversible y conserva la recuperabilidad? Responde sí o no, con el motivo"
  - "SEG: ¿este cambio toca autenticación, autorización, datos personales o dependencias? Responde con la superficie afectada"
  - "DIS: ¿la alternativa B conserva la intención aprobada? Responde sí o no, y qué se perdería"
checkpoints:
  - "tras cada paso"
  - "al descartar cada alternativa, con su coste"
critica:
  - "¿he medido el radio o lo he estimado?"
  - "¿mis dos alternativas son distintas, o una es la otra peor?"
  - "¿algún par de paquetes que llamo paralelo escribe el mismo fichero o decide lo mismo?"
  - "¿estoy decidiendo algo de forma que DIS no ha aprobado?"
gate: gate:plan-tecnico
salida:
  - "capa de plan técnico depositada"
  - "grafo de paquetes entregado a DSP"
devolucion:
  - "a PRD, cuando el alcance excluye contratos que hay que cambiar para conseguirlo"
  - "a DIS, con alternativas de forma, cuando lo aprobado tiene coste desproporcionado"
bloqueo:
  - "parte del sistema está fuera del repositorio y el radio no es medible"
cancelacion:
  - "el alcance se retira antes de terminar el plan"
aprendizaje:
  - "un radio que resultó mayor de lo medido señala una zona del mapa desactualizada"
  - "una alternativa descartada que después hubo que adoptar se registra con lo que la delató tarde"
prueba_de_reanudacion: >
  Un agente nuevo lee la traza de búsquedas y las alternativas descartadas con su coste, y
  continúa sin repetir el análisis. Es la prueba T102.
```
