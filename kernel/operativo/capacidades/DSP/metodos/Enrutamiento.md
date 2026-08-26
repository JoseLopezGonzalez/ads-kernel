# DSP/Enrutamiento — componer, crear y despachar

```yaml ads:metodo
id: DSP/Enrutamiento
nombre: Enrutamiento
capacidad: DSP
disparador:
  - "ENC entrega un encuadre en estado listo-para-dsp"
  - "una capacidad emite un resultado que exige recomponer"
  - "hay ejecutores libres y paquetes listos"
carga:
  - "el encuadre o el resultado emitido"
  - "las composiciones por defecto y el estado persistido"
  - "el frente de trabajo en curso"
preguntas_iniciales:
  - "¿qué tipo de proceso es, según el RESULTADO PERSEGUIDO?"
  - "¿qué capacidades NO se activan, y por qué?"
  - "¿qué paquetes pueden ir en paralelo, comprobando las seis condiciones?"
pasos:
  - n: 1
    nombre: CREAR EL ITEM
    modo: lineal
    hace: >
      Escribir la ficha con el encuadre entregado por ENC, asignar tipo de proceso según el
      resultado perseguido y prioridad normal por defecto.
    produce: "ficha del item"
    termina_cuando: "el item tiene identidad persistente y tipo asignado con motivo"
    checkpoint: false
  - n: 2
    nombre: COMPONER LA RUTA
    modo: convergente
    hace: >
      Aplicar la regla de derivación de b.16: propietario global, obligatorias, condicionales
      con su condición comprobada, y el motivo de cada NO activada.
    produce: "ruta r1 con su traza"
    termina_cuando: "toda capacidad no activada tiene motivo escrito"
    checkpoint: true
  - n: 3
    nombre: CREAR PAQUETES
    modo: lineal
    hace: >
      Crear cada paquete con su objetivo, su contexto mínimo por enlaces y su declaración de
      acoplamiento completa.
    produce: "paquetes en estado propuesto"
    termina_cuando: "cada paquete declara qué escribe, qué contratos toca y de qué depende"
    checkpoint: true
  - n: 4
    nombre: COMPROBAR PARALELISMO
    modo: convergente
    hace: >
      Por cada par de paquetes candidatos a ir en paralelo, comprobar LAS SEIS condiciones de
      a.5. Si falla cualquiera, se secuencia.
    produce: "declaración de paralelismo por par"
    termina_cuando: "cada par tiene las seis comprobadas, o está secuenciado"
    checkpoint: true
  - n: 5
    nombre: SELECCIONAR
    modo: convergente
    hace: >
      Aplicar b.12: filtrar, excluir por condiciones y por capacidad, atender frenos, ordenar
      por prioridad, grado de desbloqueo, antigüedad e identificador.
    produce: "selección con su orden"
    termina_cuando: "el primero está elegido y el desempate es determinista"
    checkpoint: false
  - n: 6
    nombre: EXPLICAR
    modo: lineal
    hace: >
      Escribir qué se eligió, por qué, y qué se excluyó y por qué. Sin esto, el dispatcher es
      una caja negra.
    produce: "registro de selección"
    termina_cuando: "el registro existe y nombra los excluidos con su motivo"
    checkpoint: false
  - n: 7
    nombre: DESPACHAR
    modo: lineal
    hace: "Entregar el paquete a la capacidad responsable, que materializa su equipo según C4."
    produce: "paquete en curso"
    termina_cuando: "la capacidad ha tomado custodia"
    checkpoint: true
artefactos:
  - "ficha del item y ruta con traza"
  - "paquetes con acoplamiento declarado"
  - "declaración de paralelismo por par"
  - "registro de selección"
puntos_owner:
  - "sólo cuando un freno se dispara o un desbloqueador amplía el alcance"
consultas:
  - "la capacidad propietaria de una capa, para solicitar su invalidación; DSP no la invalida"
  - "el Owner, cuando la propiedad global de un DIR o un AUD es ambigua"
checkpoints:
  - "tras componer la ruta, crear paquetes, comprobar paralelismo y despachar"
critica:
  - "¿he decidido algo de contenido?"
  - "¿he declarado paralelos dos paquetes por escribir ficheros distintos?"
  - "¿está escrito el motivo de cada capacidad no activada?"
  - "¿he elevado alguna prioridad para resolver una inanición?"
gate: gate:despacho-coherente
salida:
  - "item, ruta, paquetes y despacho, con toda su traza"
devolucion:
  - "a ENC, cuando el encuadre no permite componer ruta"
bloqueo:
  - "el estado tiene una inconsistencia irresoluble sin decidir"
cancelacion:
  - "el item se cancela globalmente: pasa por cancelando y sólo llega a cancelado sin paquetes abiertos"
aprendizaje:
  - "una ruta recompuesta tres veces sin avance material dispara el freno y se registra"
  - "una composición por defecto que siempre se recompone está mal definida: se propone a SIS"
prueba_de_reanudacion: >
  DSP no tiene checkpoint propio: el estado persistido y sus eventos SON su registro. Un
  agente nuevo reconstruye leyendo el estado y aplicando b.14. Es la prueba T118.
```
