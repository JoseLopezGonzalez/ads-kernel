# ENT/Contencion — observar, y actuar cuando algo se pone rojo

```yaml ads:metodo
id: ENT/Contencion
nombre: Contencion
capacidad: ENT
disparador:
  - "un despliegue abre su ventana de observación"
  - "una señal declarada se pone en rojo"
  - "entra un item INC"
carga:
  - "las señales y la ventana declaradas"
  - "docs/entrega/PROCEDIMIENTOS.md — reversión por tipo de cambio"
  - "el estado del entorno antes del despliegue"
preguntas_iniciales:
  - "¿esta señal en rojo la causa este cambio, o es anterior?"
  - "¿se cumplen los cinco requisitos para revertir por decisión propia?"
  - "¿hay alguna operación en curso que no pueda detenerse con seguridad?"
pasos:
  - n: 1
    nombre: MIRAR
    modo: lineal
    hace: "Leer cada señal declarada y registrar su valor, incluidos los que están bien."
    produce: "registro de señales con sus valores"
    termina_cuando: "todas las señales declaradas tienen valor registrado"
    checkpoint: true
  - n: 2
    nombre: ATRIBUIR
    modo: convergente
    hace: >
      Determinar si la señal en rojo la causa este cambio: comparar con el estado anterior al
      despliegue y con el comportamiento en otros entornos.
    produce: "atribución con su evidencia"
    termina_cuando: "está escrito si la causa es este cambio, otra cosa, o no se sabe"
    checkpoint: true
  - n: 3
    nombre: COMPROBAR LOS CINCO REQUISITOS
    modo: lineal
    hace: >
      Comprobar uno a uno: procedimiento probado, reversión segura en el estado actual, no
      destruye datos, responde a una señal roja definida de antemano, deja evento y evidencia.
    produce: "los cinco requisitos con su resultado"
    termina_cuando: "los cinco están comprobados, con sí o no por cada uno"
    checkpoint: true
  - n: 4
    nombre: ACTUAR
    modo: convergente
    hace: >
      Si los CINCO se cumplen: revertir, dejando evento y evidencia. Si falla cualquiera:
      CONTENER el daño y ESCALAR, sin revertir.
    produce: "reversión ejecutada, o contención con escalado"
    termina_cuando: "el daño está detenido y la decisión está registrada"
    checkpoint: true
  - n: 5
    nombre: SEPARAR LO QUE SIGUE VIVO
    modo: lineal
    hace: >
      Si hay una operación de contención que no puede detenerse con seguridad, separarla en
      un ITEM ENLAZADO que sigue activo. Nunca se esconde trabajo activo bajo un item cancelado.
    produce: "item enlazado activo, cuando corresponde"
    termina_cuando: "no queda ninguna operación en curso sin item que la represente"
    checkpoint: true
artefactos:
  - "registro de señales con valores"
  - "atribución con evidencia"
  - "los cinco requisitos comprobados"
  - "evento y evidencia de la reversión, o de la contención"
puntos_owner:
  - "inmediato cuando el rollback no cumple los cinco requisitos: se contiene y se le presentan las opciones con lo que se pierde en cada una"
consultas:
  - "ARQ: ¿esta señal en rojo es compatible con el cambio desplegado? Responde con la hipótesis y su evidencia"
  - "DOM: ¿revertir en este punto puede dejar datos inconsistentes? Responde sí o no"
checkpoints:
  - "tras cada lectura de señales"
  - "antes de revertir, con los cinco requisitos escritos"
critica:
  - "¿estoy revirtiendo sin haber comprobado los cinco requisitos porque hay prisa?"
  - "¿he atribuido la causa a este cambio sin compararlo con el estado anterior?"
  - "¿queda alguna operación viva que no esté representada por un item?"
gate: gate:entrega-observada
salida:
  - "confirmación de funcionamiento real, o contención ejecutada con su evidencia"
devolucion:
  - "a la capacidad propietaria de la capa que originó la señal en rojo"
bloqueo:
  - "no hay telemetría ni logs que mirar"
cancelacion:
  - "el item se cancela globalmente: toda contención en curso se separa en item enlazado activo"
aprendizaje:
  - "todo incidente genera paquete de APR: es el único tipo con aprendizaje obligatorio (b.16)"
  - "un fallo que ninguna señal vigilaba genera una señal nueva"
prueba_de_reanudacion: >
  Un agente nuevo lee el registro de señales y si la reversión llegó a ejecutarse. Antes de
  actuar comprueba el estado real del entorno: en contención, el estado declarado puede ir
  por detrás del real. Es la prueba T111.
```
