# CON/Implementacion — construir sin redecidir

```yaml ads:metodo
id: CON/Implementacion
nombre: Implementacion
capacidad: CON
disparador:
  - "DSP despacha un paquete de construcción con sus capas anteriores depositadas"
carga:
  - "las capas de PRD, DIS y ARQ cuando existen, con sus versiones"
  - "las condiciones de DOM y SEG"
  - "CONVENTIONS.md y el código de la zona afectada"
preguntas_iniciales:
  - "¿alguna capa anterior está incompleta o me obliga a decidir algo que no me toca?"
  - "¿qué de esto son las ocho cosas que no se simplifican en silencio?"
  - "¿qué condiciones de dominio y seguridad tengo que comprobar, y con qué consulta?"
pasos:
  - n: 1
    nombre: LEER Y DETECTAR HUECOS
    modo: lineal
    hace: >
      Leer las capas anteriores buscando qué tendría que decidir yo que no me corresponde.
      Todo hueco encontrado aquí se devuelve AHORA, antes de construir nada.
    produce: "lista de huecos, o constancia de que no hay ninguno"
    termina_cuando: "no queda ninguna decisión ajena pendiente de tomar para poder construir"
    checkpoint: true
  - n: 2
    nombre: CONSTRUIR
    modo: lineal
    hace: >
      Implementar lo especificado, respetando las ocho cosas que no se simplifican. Toda
      diferencia que aparezca se DECLARA en el momento, no al final.
    produce: "código con su commit"
    termina_cuando: "el comportamiento especificado existe y las diferencias están declaradas"
    checkpoint: true
  - n: 3
    nombre: TESTS
    modo: lineal
    hace: >
      Escribir los tests del comportamiento nuevo, incluidos los casos que no son el camino
      feliz: vacío, error, límite.
    produce: "tests y su salida"
    termina_cuando: "la suite pasa y cubre el comportamiento nuevo, no sólo el camino feliz"
    checkpoint: true
  - n: 4
    nombre: COMPROBAR CONDICIONES
    modo: lineal
    hace: >
      Ejecutar las consultas de comprobación que DOM declaró y recorrer las condiciones de
      SEG, dejando la evidencia de cada una.
    produce: "salida de las comprobaciones"
    termina_cuando: "todas las condiciones tienen su evidencia"
    checkpoint: true
  - n: 5
    nombre: CERRAR CONTRA EL GATE
    modo: convergente
    hace: "Recorrer las siete comprobaciones de gate:implementacion-completa y anotarlas."
    produce: "capa depositada, o lista de lo que falta"
    termina_cuando: "las siete están anotadas"
    checkpoint: true
artefactos:
  - "código y commit"
  - "tests y su salida"
  - "salida de las comprobaciones de dominio y seguridad"
  - "diferencias declaradas con su fecha"
puntos_owner:
  - "ninguno"
consultas:
  - "ARQ: ¿el plan contempla este caso que no aparece en la descomposición? Responde sí o no"
  - "DIS: ¿esta diferencia conserva la intención? Responde sí o no, y qué se perdería"
checkpoints:
  - "tras cada paso"
  - "al declarar cada diferencia"
critica:
  - "¿he decidido algo que pertenece a otra capa en vez de devolver?"
  - "¿he simplificado alguna de las ocho cosas sin declararlo?"
  - "¿mis tests cubren el vacío, el error y el límite, o sólo el camino feliz?"
gate: gate:implementacion-completa
salida:
  - "capa de implementación depositada, con su evidencia"
devolucion:
  - "a DIS, ARQ, PRD, DOM o SEG, según de quién sea la capa insuficiente, con evidencia"
bloqueo:
  - "una dependencia externa no está disponible"
  - "el entorno de construcción no está listo"
cancelacion:
  - "el item se cancela: el código construido se conserva en su rama, sin integrar"
aprendizaje:
  - "un hueco detectado en el paso 1 que se repite señala una capa que se entrega incompleta sistemáticamente"
  - "una diferencia declarada que después resultó innecesaria se registra"
prueba_de_reanudacion: >
  Un agente nuevo lee el checkpoint, ve qué partes están construidas y qué diferencias se
  han declarado, y continúa sin rehacerlas ni descubrirlas otra vez. Es la prueba T106.
```
