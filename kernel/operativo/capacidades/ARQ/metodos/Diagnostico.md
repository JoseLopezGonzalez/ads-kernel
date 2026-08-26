# ARQ/Diagnostico — encontrar la causa

```yaml ads:metodo
id: ARQ/Diagnostico
nombre: Diagnostico
capacidad: ARQ
disparador:
  - "DSP despacha un paquete de diagnóstico sobre un DEF cuyo diagnóstico no es evidente"
  - "un INC entra en diagnóstico tras la contención de ENT"
carga:
  - "el encuadre con el caso concreto y las condiciones en que ocurrió"
  - "logs, telemetría y evidencia de ENT o USO"
  - "el historial de control de versiones de la zona afectada"
  - "el ledger de aprendizaje, por si esta causa ya apareció"
preguntas_iniciales:
  - "¿en qué condiciones exactas ocurre, y en cuáles no?"
  - "¿desde cuándo ocurre, y qué cambió entonces?"
  - "¿es un fallo o es una expectativa que nunca se implementó?"
pasos:
  - n: 1
    nombre: REPRODUCIR
    modo: lineal
    hace: >
      Conseguir el fallo a voluntad, con los datos y las condiciones registradas. Si no se
      consigue, se documentan las condiciones probadas antes de declarar nada.
    produce: "reproducción documentada, o lista de condiciones probadas sin éxito"
    termina_cuando: "el fallo se reproduce a voluntad, o están probadas todas las condiciones registradas"
    checkpoint: true
  - n: 2
    nombre: ACOTAR
    modo: convergente
    hace: >
      Reducir el espacio del problema: qué capa, qué módulo, qué entrada. Se usa bisección
      del historial cuando el fallo apareció en un momento identificable.
    produce: "zona acotada con la evidencia que la acota"
    termina_cuando: "el fallo está localizado en una zona que se puede leer entera"
    checkpoint: true
  - n: 3
    nombre: CAUSA, NO SÍNTOMA
    modo: convergente
    hace: >
      Explicar por qué ocurre, no dónde se ve. La explicación debe cubrir TODOS los síntomas
      observados; si sólo cubre uno, la causa es otra.
    produce: "causa con su evidencia"
    termina_cuando: "la causa explica todos los síntomas registrados"
    checkpoint: true
  - n: 4
    nombre: BUSCAR HERMANOS
    modo: divergente
    hace: >
      Buscar qué más comparte esta causa en el repositorio. Un defecto rara vez está solo y
      corregir sólo el que se vio deja los otros para dentro de un mes.
    produce: "lista de elementos afectados por la misma causa"
    termina_cuando: "la búsqueda por el patrón de la causa no encuentra nada nuevo"
    checkpoint: true
  - n: 5
    nombre: CLASIFICAR
    modo: convergente
    hace: >
      Decidir si esto es un defecto, un gap de alcance, deuda estructural o una decisión de
      producto no tomada. Si no es defecto, el item cambia de proceso según b.1.
    produce: "clasificación con su motivo"
    termina_cuando: "la clasificación está escrita y, si cambia el proceso, propuesta a DSP"
    checkpoint: true
artefactos:
  - "reproducción documentada"
  - "acotación con evidencia"
  - "causa que explica todos los síntomas"
  - "lista de hermanos"
  - "clasificación"
puntos_owner:
  - "ninguno"
consultas:
  - "DOM: ¿esta causa puede haber corrompido datos? Responde sí o no, y qué habría que revisar"
  - "SEG: ¿esta causa tiene consecuencias de seguridad? Responde con la superficie expuesta"
  - "ENT: ¿qué se desplegó entre la última vez que funcionaba y la primera que falló?"
checkpoints:
  - "tras conseguir la reproducción"
  - "al descartar cada hipótesis, con lo que la descartó"
critica:
  - "¿mi causa explica TODOS los síntomas o sólo el primero?"
  - "¿he buscado hermanos, o voy a corregir uno de cinco?"
  - "¿esto es un defecto, o una expectativa que nunca se implementó?"
gate: gate:plan-tecnico
salida:
  - "diagnóstico con causa, reproducción y hermanos"
devolucion:
  - "a ENC, cuando falta información del Owner para reproducir"
bloqueo:
  - "el fallo sólo ocurre en un entorno inaccesible"
  - "no hay logs del momento y no se puede reconstruir qué pasó"
cancelacion:
  - "el fallo deja de ocurrir por otro cambio y se documenta qué lo resolvió"
aprendizaje:
  - "toda causa se registra en el ledger: la misma causa dos veces es un aprendizaje promovible"
  - "un fallo que no se pudo reproducir por falta de logs genera un candidato de observabilidad para PLT"
prueba_de_reanudacion: >
  Un agente nuevo lee la reproducción y las hipótesis ya descartadas con su evidencia, y
  continúa sin repetirlas. Es la prueba T103.
```
