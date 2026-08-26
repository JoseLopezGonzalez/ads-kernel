# ENT · ENTREGA Y OPERACIÓN — realidad operativa

El cambio existe **fuera del entorno de desarrollo** y se ha **observado** comportarse.
Opera la maquinaria que PLT construye; no la construye.

```yaml ads:capacidad
id: ENT
nombre: Entrega y operación
clase: estacion
mision: >
  Hacer que el cambio exista en el entorno real, observarlo durante una ventana declarada, y
  poder devolverlo al estado anterior cuando algo va mal.
capa_de_valor: >
  Añade realidad operativa: integración, migración ejecutada, despliegue, smoke tests,
  observación con señales declaradas y capacidad de reversión probada.
entrada:
  - "un paquete con dosier de VER sin evidencia en rojo"
  - "una migración probada por DOM"
  - "un incidente que exige contención inmediata"
salida:
  - "el cambio desplegado en el entorno declarado, con su commit"
  - "salida de los smoke tests"
  - "observación durante la ventana declarada, con las señales miradas"
  - "confirmación de funcionamiento real, o reversión con su evidencia"
gate: gate:entrega-observada
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/entrega/PROCEDIMIENTOS.md — cómo se despliega y cómo se revierte, por entorno"
  - "docs/entrega/HISTORIAL.md — qué se desplegó, cuándo, qué se observó y qué se revirtió"
  - "docs/entrega/SENALES.md — qué se mira tras cada tipo de cambio, y qué es rojo"
tablero: "estado/tableros/ENT.md — despliegues en curso y ventanas de observación abiertas"
metodos: [ENT/Despliegue, ENT/Contencion]
checkpoint: "en el paquete, con qué se ha desplegado, en qué entorno y qué se está observando"
autoridad:
  decide_sola:
    - "el orden de integración de ramas y paquetes"
    - "cuándo se despliega a un entorno no productivo"
    - "revertir por decisión propia cuando se cumplen los CINCO requisitos de a.3"
  escala:
    - "la publicación: es materia reservada del Owner (G05)"
    - "un rollback destructivo, irreversible, con pérdida de datos o no probado: contiene y escala"
  veta: []
owner:
  nivel: mixto
  criterio: >
    Obligatorio para publicar: la publicación es materia reservada (G05). Ninguna para
    desplegar a entornos no productivos, para ejecutar smoke tests y para revertir cuando se
    cumplen los cinco requisitos de rollback autónomo de a.3.
roles: [ENT/despliegue, ENT/observacion]
deriva_de:
  - "a.3 · ENT: operar la maquinaria, ventana de observación, rollback autónomo con cinco requisitos"
  - "b.16 · ENT es propietario global de INC y obligatorio en SIS que modifica el runtime"
materializacion: >
  Se materializa cuando un item cumple C-ENT: el resultado debe existir fuera del entorno de
  desarrollo para ser útil o verificable.
retirada: >
  Los roles se retiran al cerrar la ventana de observación. Los procedimientos, el historial
  y las señales persisten: son lo que hace posible el rollback autónomo.
```

```yaml ads:gate
id: gate:entrega-observada
aplica_a: "la capa de ENT antes de dar por entregado un cambio"
comprobaciones:
  - id: desplegado
    comprueba: "el cambio existe en el entorno declarado, con su commit identificado"
    como: "consulta al entorno: qué versión está corriendo"
    automatizable: si
  - id: smoke
    comprueba: "los smoke tests del entorno han pasado tras el despliegue"
    como: "salida de la ejecución"
    automatizable: si
  - id: ventana-declarada
    comprueba: "la ventana de observación estaba declarada ANTES de desplegar, con sus señales"
    como: "el paquete enlaza la declaración con fecha anterior al despliegue"
    automatizable: si
  - id: senales-miradas
    comprueba: "las señales declaradas se han mirado durante la ventana, con su resultado"
    como: "registro de cada señal con su valor observado"
    automatizable: si
  - id: reversion-disponible
    comprueba: "existe procedimiento de reversión probado para este tipo de cambio"
    como: "enlace al procedimiento y a su última prueba"
    automatizable: si
  - id: publicacion-autorizada
    comprueba: "si el despliegue es una publicación, el Owner la autorizó"
    como: "enlace a la autorización con su fecha"
    automatizable: si
evidencia:
  - "la versión corriendo en el entorno"
  - "salida de smoke tests"
  - "registro de señales durante la ventana"
  - "autorización del Owner cuando fue publicación"
fallo: >
  El cambio no se da por entregado. Si las señales están en rojo, se aplica el
  procedimiento de contención: revertir si se cumplen los cinco requisitos, contener y
  escalar si no.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
