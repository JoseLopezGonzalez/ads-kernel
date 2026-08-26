# DIS/Evolucion — el trabajo diario sobre un sistema establecido

El método más usado. Tiene **tres ramas** y la escala de novedad decide cuál se ejecuta:
aplicación (N0), extensión (N1) y divergente (N2). No es discrecional.

```yaml ads:metodo
id: DIS/Evolucion
nombre: Evolucion
capacidad: DIS
disparador:
  - "la escala de novedad devuelve N0, N1 o N2"
  - "existe memoria de diseño con dirección aprobada"
carga:
  - "el encuadre del item y su nivel de novedad con el motivo citado"
  - "docs/diseno/01-PRINCIPIOS.md, 03-SISTEMA.md, 07-COMPONENTES.md, 08-DECISIONES.md"
  - "los datos reales de la superficie afectada"
  - "la deuda de diseño registrada de esa superficie"
preguntas_iniciales:
  - "¿existe un patrón vigente cuyo alcance cubra este caso, con sus criterios cumplidos?"
  - "¿qué se descartó ya en esta materia, según 08-DECISIONES?"
  - "¿esta superficie tiene deuda registrada que este trabajo pueda saldar o empeorar?"
pasos:
  - n: 1
    nombre: RECUPERAR
    modo: lineal
    hace: >
      Aplicar el test de a.8: buscar patrón vigente cuyo alcance cubra el caso, comprobar
      sus criterios y comprobar que no se introduce nada fuera de su alcance. El resultado
      fija la rama.
    produce: "rama elegida —aplicación, extensión o divergente— con el motivo citado"
    termina_cuando: "la rama está escrita en el checkpoint con la pregunta de la escala que la determinó"
    checkpoint: true
  - n: 2
    nombre: APLICAR
    modo: lineal
    hace: >
      RAMA APLICACIÓN (N0). Resolver la superficie con el patrón vigente, sin explorar.
      Se comprueban los cinco estados con datos reales y se registra que el patrón se
      aplicó, para que su frecuencia de uso quede medida.
    produce: "superficie resuelta con el patrón, y registro de aplicación"
    termina_cuando: "los cinco estados están resueltos y ningún valor cae fuera del sistema"
    checkpoint: true
  - n: 3
    nombre: EXTENDER
    modo: divergente
    hace: >
      RAMA EXTENSIÓN (N1). Producir al menos DOS alternativas de cómo el sistema puede
      cubrir el caso nuevo, comparadas contra los principios vigentes.
    produce: "dos o más alternativas con lo que gana y sacrifica cada una"
    termina_cuando: "cada alternativa está evaluada contra los principios, uno por uno"
    checkpoint: true
  - n: 4
    nombre: EXPLORAR
    modo: divergente
    hace: >
      RAMA DIVERGENTE (N2). Producir al menos TRES direcciones distintas en dos de las
      cinco dimensiones, resueltas con datos reales. PROHIBIDO descartar en esta fase.
    produce: "tres o más direcciones desarrolladas"
    termina_cuando: "DIS/critica-visual confirma que difieren en al menos dos dimensiones"
    checkpoint: true
  - n: 5
    nombre: CRITICAR
    modo: convergente
    hace: >
      DIS/critica-visual dictamina. En N0 no se ejecuta este paso: el patrón ya fue
      criticado cuando se aprobó.
    produce: "dictamen de crítica"
    termina_cuando: "el dictamen es conforme, o el trabajo vuelve al paso 3 o 4"
    checkpoint: true
  - n: 6
    nombre: CONVERGER
    modo: convergente
    hace: >
      Elegir y escribir el motivo de cada descarte en 08-DECISIONES. PROHIBIDO añadir
      alternativas nuevas en esta fase.
    produce: "elección con motivo de cada descarte"
    termina_cuando: "todo lo descartado tiene motivo escrito en la memoria"
    checkpoint: true
  - n: 7
    nombre: ACTUALIZAR EL SISTEMA
    modo: convergente
    hace: >
      DIS/sistema-de-diseno incorpora lo nuevo: valores, componentes o patrones, con clase,
      alcance, criterios comprobables y caducidad.
    produce: "sistema actualizado y patrón declarado cuando lo hay"
    termina_cuando: "lo nuevo está en el sistema o está declarado expresamente como excepción con su motivo"
    checkpoint: true
  - n: 8
    nombre: REVISAR CONSISTENCIA
    modo: convergente
    hace: >
      Comprobar que el cambio no ha dejado dos formas de resolver lo mismo en el producto,
      extrayendo los valores de las superficies vecinas.
    produce: "informe de consistencia"
    termina_cuando: >
      no queda ninguna superficie vecina resolviendo lo mismo de otra forma, o la
      diferencia está registrada como deuda con su motivo
    checkpoint: true
  - n: 9
    nombre: INCORPORAR APRENDIZAJE
    modo: lineal
    hace: >
      Registrar en el historial qué reveló este trabajo: un patrón que no cubría lo que
      decía, una excepción que se repite por tercera vez, una reacción del Owner que ya
      había ocurrido.
    produce: "entrada de historial, y learning_candidate resuelto"
    termina_cuando: "learning_candidate está resuelto con none o con un enlace"
    checkpoint: true
artefactos:
  - "declaración de rama con su motivo"
  - "alternativas o direcciones, según la rama"
  - "dictamen de crítica, salvo en N0"
  - "decisiones y descartes escritos"
  - "sistema actualizado"
  - "informe de consistencia"
puntos_owner:
  - "N2: primera instancia de patrón visual — obligatorio (a.8)"
  - "N1: cola de validación por lotes si extiende un owner_approved_pattern — no detiene el item"
  - "N0: ninguno"
consultas:
  - "ARQ: ¿el componente afectado se comparte con otras superficies? Responde con la lista"
  - "DIS/investigacion-visual, en N2, cuando el material vigente no basta para abrir direcciones"
checkpoints:
  - "tras cada paso ejecutado"
  - "al descartar cada alternativa, con su motivo, antes de seguir"
critica:
  - "¿se eligió N0 para ahorrar exploración cuando el caso no está cubierto por el alcance del patrón?"
  - "¿las alternativas son distintas o es la misma con dos acabados?"
  - "¿la superficie vecina quedó resolviendo lo mismo de otra forma?"
  - "¿se escribieron los descartes o sólo lo elegido?"
gate: gate:excelencia-visual
salida:
  - "superficie especificada y construible"
  - "sistema actualizado y patrones declarados"
  - "memoria con decisiones y descartes"
devolucion:
  - "a ENC, cuando el encuadre no permite determinar el nivel de novedad"
  - "a CON, cuando la revisión de fidelidad devuelve infiel"
bloqueo:
  - "el patrón que cubriría el caso está caducado y actualizarlo cambia superficies aprobadas"
cancelacion:
  - "un item DIR sustituye la dirección antes de converger: el trabajo se conserva como material"
aprendizaje:
  - "un patrón cuyo alcance no cubría lo que parecía cubrir se corrige en su ficha"
  - "una excepción repetida tres veces se incorpora al sistema o se elimina"
prueba_de_reanudacion: >
  Un agente nuevo abre el paquete, lee la rama elegida y las alternativas ya descartadas
  con su motivo, y continúa sin volver a proponerlas. Si el checkpoint no declara la rama,
  el método se reinicia desde el paso 1: sin rama declarada no hay trabajo comparable. Es
  la prueba T95.
```
