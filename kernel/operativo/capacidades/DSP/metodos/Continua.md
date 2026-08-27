# DSP/Continua — responder a «Continúa»

Implementa los siete pasos de b.14. Los pasos 1 a 4 son deterministas y **no requieren al
Owner**; el paso 5 es obligatorio, breve y **no pide permiso**.

```yaml ads:metodo
id: DSP/Continua
nombre: Continua
capacidad: DSP
disparador:
  - "el Owner dice «Continúa», «sigue» o «retoma lo de…»"
  - "se abre una sesión y hay trabajo en curso"
carga:
  - "el estado canónico completo"
  - "los tableros con sus órdenes pendientes"
preguntas_iniciales:
  - "¿hay reconciliación pendiente? Si la hay, se resuelve antes que nada"
  - "¿lo declarado corresponde con la realidad del control repo y de las fuentes?"
  - "¿siguen siendo viables todas las esperas?"
pasos:
  - n: 1
    nombre: RECONSTRUIR
    modo: lineal
    hace: >
      Leer el estado canónico completo. NO leer el kernel entero. NO depender de ninguna
      conversación anterior.
    produce: "estado reconstruido"
    termina_cuando: "todos los items y paquetes están cargados con su estado"
    checkpoint: false
  - n: 2
    nombre: VERIFICAR
    modo: lineal
    hace: >
      Contrastar lo declarado contra lo que hay: el repositorio de control para el estado,
      y las fuentes del alcance para los artefactos. ¿Existen los artefactos que los
      paquetes dicen haber producido, en la fuente donde dicen haberlos producido? ¿Hay
      transiciones multiarchivo incompletas? ¿Hay derivados divergentes? ¿Siguen viables
      las esperas? ¿Sigue el workspace conforme —`workspace check`— para las fuentes que
      los paquetes vivos declaran?
    produce: "lista de inconsistencias, o constancia de que no hay ninguna"
    termina_cuando: "las cuatro comprobaciones están hechas y las inconsistencias resueltas o escaladas"
    checkpoint: true
  - n: 3
    nombre: CONSUMIR ÓRDENES
    modo: lineal
    hace: >
      Aplicar el protocolo de a.9: leer, detectar, ELEVAR toda diferencia de la zona derivada
      a orden, validar, registrar evento, aplicar, marcar y regenerar con comparación e
      intercambio.
    produce: "órdenes consumidas con su atribución"
    termina_cuando: "no queda orden sin consumir, o se han agotado los tres intentos y el ciclo se detiene"
    checkpoint: true
  - n: 4
    nombre: SELECCIONAR
    modo: convergente
    hace: "Aplicar b.12 sobre el estado ya verificado."
    produce: "selección con su explicación"
    termina_cuando: "el frente de trabajo está elegido"
    checkpoint: false
  - n: 5
    nombre: REPORTAR
    modo: lineal
    hace: >
      UNA vez, en pocas líneas: qué retoma, por qué ése y no otro, qué espera decisión del
      Owner, qué está aparcado y qué está en inanición. NO se pide permiso.
    produce: "reporte breve"
    termina_cuando: "el reporte está dado, en pocas líneas y sin pedir permiso"
    checkpoint: false
  - n: 6
    nombre: CARGAR
    modo: lineal
    hace: >
      Entregar el control a la capacidad con custodia: cargar su checkpoint, comprobar
      `based_on`, y revalidar SÓLO la parte afectada si alguna fuente cambió.
    produce: "control transferido con el checkpoint cargado"
    termina_cuando: "la capacidad tiene su checkpoint y sabe qué parte revalidar"
    checkpoint: true
  - n: 7
    nombre: TRABAJAR
    modo: lineal
    hace: "La capacidad continúa desde su paso exacto."
    produce: "trabajo en curso"
    termina_cuando: "el paquete avanza o emite un resultado"
    checkpoint: false
artefactos:
  - "estado reconstruido y verificado"
  - "órdenes consumidas con atribución"
  - "reporte breve"
puntos_owner:
  - "paso 5: el reporte. NO es una petición de permiso"
  - "escalado cuando el paso 2 encuentra una inconsistencia irresoluble sin decidir"
consultas:
  - "ninguna: los pasos 1 a 4 son deterministas"
checkpoints:
  - "tras verificar, tras consumir órdenes y al transferir el control"
critica:
  - "¿he inventado estado para salir de una inconsistencia?"
  - "¿he regenerado encima de una edición del Owner sin elevarla a orden?"
  - "¿mi reporte pide permiso en lugar de informar?"
  - "¿he entendido «Continúa» como «haz todo lo pendiente»?"
gate: gate:despacho-coherente
salida:
  - "trabajo retomado desde el checkpoint exacto, con reporte breve"
devolucion:
  - "a la capacidad con custodia, cuando lo declarado no corresponde con lo que hay en el control repo o en la fuente donde debería estar"
bloqueo:
  - "hay una transición multiarchivo incompleta que no puede resolverse sin decidir"
cancelacion:
  - "no aplica: «Continúa» no cancela nada"
aprendizaje:
  - "toda inconsistencia encontrada en el paso 2 se registra: señala una transición mal diseñada"
prueba_de_reanudacion: >
  Este método ES la reanudación del sistema. Desde repo frío, sin conversación previa: DSP
  reconstruye, verifica, reporta breve y retoma desde el checkpoint exacto. Es T36 de (b), y
  su versión operativa es la prueba T119.
```
