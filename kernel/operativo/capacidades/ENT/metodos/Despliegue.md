# ENT/Despliegue — llevarlo al entorno real de forma reversible

```yaml ads:metodo
id: ENT/Despliegue
nombre: Despliegue
capacidad: ENT
disparador:
  - "un paquete tiene dosier de VER sin evidencia en rojo y cumple C-ENT"
carga:
  - "el dosier de VER"
  - "la migración probada de DOM con su ventana de incompatibilidad"
  - "docs/entrega/PROCEDIMIENTOS.md y SENALES.md"
preguntas_iniciales:
  - "¿existe procedimiento de reversión probado para este tipo de cambio?"
  - "¿qué señales voy a mirar y durante cuánto tiempo?"
  - "¿esto es una publicación? Si lo es, ¿tengo autorización escrita?"
pasos:
  - n: 1
    nombre: COMPROBAR LA VUELTA
    modo: lineal
    hace: >
      Antes de tocar nada, comprobar que existe procedimiento de reversión probado. Si no
      existe, se bloquea y se crea el trabajo de crearlo.
    produce: "confirmación de reversión disponible, con enlace a su última prueba"
    termina_cuando: "la reversión está disponible y probada, o el paquete está bloqueado"
    checkpoint: true
  - n: 2
    nombre: DECLARAR VENTANA Y SEÑALES
    modo: lineal
    hace: >
      Escribir qué se va a mirar, durante cuánto tiempo y qué valor cuenta como rojo. ANTES
      de desplegar: declararlo después es elegir las señales que salieron bien.
    produce: "ventana y señales declaradas, con fecha"
    termina_cuando: "cada señal tiene su umbral de rojo escrito"
    checkpoint: true
  - n: 3
    nombre: INTEGRAR
    modo: lineal
    hace: "Integrar ramas y paquetes en el orden que respeta las dependencias declaradas."
    produce: "rama integrada"
    termina_cuando: "la integración está hecha y la suite pasa sobre el resultado integrado"
    checkpoint: true
  - n: 4
    nombre: MIGRAR
    modo: lineal
    hace: >
      Ejecutar la migración de DOM respetando su ventana de incompatibilidad y su cobertura.
    produce: "migración ejecutada con sus recuentos"
    termina_cuando: "los recuentos cuadran con los de la prueba, o la diferencia está explicada"
    checkpoint: true
  - n: 5
    nombre: DESPLEGAR Y COMPROBAR
    modo: lineal
    hace: "Desplegar al entorno y ejecutar los smoke tests."
    produce: "versión corriendo y salida de smoke tests"
    termina_cuando: "los smoke tests pasan, o se ejecuta la reversión"
    checkpoint: true
artefactos:
  - "confirmación de reversión disponible"
  - "ventana y señales declaradas"
  - "migración ejecutada con recuentos"
  - "versión corriendo y smoke tests"
puntos_owner:
  - "autorización de publicación, cuando el despliegue es una publicación (G05)"
consultas:
  - "PLT: ¿el entorno está disponible y en qué estado? Responde con la versión corriendo"
  - "DOM: ¿la ventana de incompatibilidad sigue siendo la declarada? Responde sí o no"
checkpoints:
  - "tras cada paso"
critica:
  - "¿he comprobado la reversión o la doy por hecha?"
  - "¿declaré las señales antes de desplegar, o las estoy eligiendo ahora?"
  - "¿esto es una publicación y tengo autorización?"
gate: gate:entrega-observada
salida:
  - "cambio desplegado, con smoke tests pasados y ventana abierta"
devolucion:
  - "a CON, cuando el artefacto no arranca"
  - "a DOM, cuando la migración falla sobre datos reales"
bloqueo:
  - "no existe reversión probada"
  - "el entorno no está disponible"
cancelacion:
  - "el despliegue se detiene y se revierte lo aplicado, con su registro"
aprendizaje:
  - "todo despliegue entra en el historial con lo que pasó de verdad"
  - "un fallo que ninguna señal vigilaba genera una señal nueva en SENALES.md"
prueba_de_reanudacion: >
  Un agente nuevo lee el checkpoint y sabe exactamente en qué paso quedó el despliegue: si
  la migración se ejecutó, si el despliegue llegó a aplicarse. Ante duda, comprueba el
  estado real del entorno antes de repetir nada. Es la prueba T110.
```
