# SIS · INGENIERÍA DEL SISTEMA — dueña de la fábrica

Trabaja **sobre la fábrica**, no sobre el producto. Y por eso está sujeta al freno de racha
de a.7: no se despachan más de dos items SIS consecutivos si hay un item de producto listo
para avanzar.

```yaml ads:capacidad
id: SIS
nombre: Ingeniería del sistema
clase: sistema
mision: >
  Mantener y evolucionar el sistema operativo de la organización —contratos, plantillas,
  catálogo, composiciones, validadores y pruebas— y comprobar que una organización instalada
  es conforme.
capa_de_valor: >
  Añade capacidad de fabricar: mejora el instrumento con el que las demás capacidades
  trabajan, y demuestra con pruebas que ese instrumento cumple lo que dice cumplir.
entrada:
  - "un item de tipo SIS, que DEBE enlazar el problema real de producto que lo justifica"
  - "un aprendizaje promovido a upstream por APR"
  - "un hallazgo de la función de coherencia documental"
salida:
  - "el cambio en el kernel operativo, con su validador y su prueba"
  - "el informe de conformidad de una organización instalada"
  - "items enrutados a la capacidad competente cuando encuentra un documento huérfano"
gate: gate:sistema-conforme
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "kernel/operativo/ — el propio kernel operativo es su memoria"
  - "kernel/KERNEL_CHANGELOG.md — qué cambió del kernel y por qué"
  - "kernel/operativo/pruebas/REGISTRO.md — el estado real de cada prueba"
tablero: "estado/tableros/SIS.md — items de sistema y su justificación de producto"
metodos: [SIS/Evolucion, SIS/Conformidad]
checkpoint: "en el paquete, con qué contratos se han tocado y qué pruebas se han ejecutado"
autoridad:
  decide_sola:
    - "la forma de los contratos, esquemas, plantillas y validadores"
    - "las composiciones por defecto y su revisión"
    - "el enrutamiento de modelos y los perfiles de agente"
    - "el estado real de cada prueba, que NO se declara superada sin ejecutarse"
  escala:
    - "un cambio que contradice una sección normativa aprobada: registra y propone, no modifica"
    - "un cambio de contrato de una capacidad que altera su autoridad"
  veta: []
owner:
  nivel: opcional-acumulada
  criterio: >
    SIS no consulta al Owner en el trabajo ordinario. Escala cuando el cambio afecta a una
    sección normativa aprobada, y entonces registra la contradicción y propone un cambio
    mínimo, sin modificarla por su cuenta.
roles: [SIS/evolucion, SIS/coherencia]
deriva_de:
  - "a.3 · SIS: dueña del sistema operativo y de la función Coherencia Documental"
  - "a.7 · freno de racha SIS = 2"
  - "b.16 · SIS es propietario global de los items SIS; ENT obligatorio si modifica el runtime"
materializacion: "SIS se materializa SIEMPRE, junto a DSP. Sin ella nadie mantiene la fábrica."
retirada: >
  SIS no se retira. Lo que sí se aplica es el freno de racha: dos items SIS consecutivos
  completados, y el tercero espera a que avance un item de producto.
```

```yaml ads:gate
id: gate:sistema-conforme
aplica_a: "todo cambio del kernel operativo y todo informe de conformidad"
comprobaciones:
  - id: justificacion-de-producto
    comprueba: "el item SIS enlaza el problema real, la fricción o la capacidad de producto que lo justifica"
    como: "enlace presente y resoluble"
    automatizable: si
  - id: validador
    comprueba: "todo contrato nuevo o cambiado tiene su comprobación en un validador, o consta por qué no es automatizable"
    como: "el cambio enlaza la regla del validador que lo comprueba"
    automatizable: si
  - id: prueba-con-estado-real
    comprueba: "toda prueba declara su estado real y ninguna se declara superada sin haberse ejecutado"
    como: "comparación entre el estado declarado y la evidencia enlazada"
    automatizable: si
  - id: sin-modificar-lo-aprobado
    comprueba: "ninguna sección normativa aprobada se ha modificado; las contradicciones están registradas"
    como: "diff contra las secciones aprobadas: debe estar vacío"
    automatizable: si
  - id: fuente-unica
    comprueba: "el cambio no crea una segunda fuente de una verdad que ya existe"
    como: "búsqueda de la materia en el índice de fuente única"
    automatizable: parcial
  - id: entrega-si-runtime
    comprueba: "si el cambio modifica el runtime, tiene entrega con activación segura y reversible"
    como: "enlace al paquete de ENT"
    automatizable: si
evidencia:
  - "el enlace a la justificación de producto"
  - "la salida de los validadores ejecutados"
  - "el diff vacío contra las secciones aprobadas"
fallo: >
  El cambio no se integra. Un cambio del sistema sin validador ni prueba es una afirmación,
  y el sistema entero se apoya en no confundir afirmaciones con hechos comprobados.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
