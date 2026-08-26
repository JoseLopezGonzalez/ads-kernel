# DSP — composición del equipo

> **DSP es implementación software primero.** Mientras el runtime no exista, estos roles los
> ejecuta un supervisor —agente o el propio Owner— siguiendo sus métodos. Cuando el runtime
> exista, los ejecuta él y el supervisor interviene sólo en excepciones (a.3).

```yaml ads:composicion
id: composicion:dsp-supervisor
capacidad: DSP
clase_de_trabajo: "despacho y estado mientras el runtime no existe"
condicion: >
  El proyecto NO tiene todavía runtime de despacho implementado, y las funciones de DSP las
  ejecuta un agente supervisor.
roles:
  - rol: DSP/enrutamiento
    obligatorio: true
    agentes: "1"
  - rol: DSP/estado
    obligatorio: true
    agentes: "el mismo agente que enrutamiento"
combinables:
  - roles: [DSP/enrutamiento, DSP/estado]
    motivo: "ambos son mecánicos y deterministas y ninguno juzga contenido: no hay conflicto que separar"
independientes:
  - rol: DSP/enrutamiento
    de: ["toda capacidad que decida contenido: DSP no ocupa a la vez un rol de contenido y el despacho"]
    motivo: >
      un agente que decide el contenido de una capa y además el orden acabaría despachándose
      trabajo a sí mismo, y la autoridad sobre contenido y sobre orden dejarían de estar separadas
ampliacion: >
  Cuando el runtime exista, estos roles pasan a ejecutarse por software y el supervisor
  interviene sólo en excepciones: paquete estancado, contradicción de estado, ruta a
  recomponer o conflicto que el runtime no debe resolver solo.
reduccion: "ninguna: sin despacho no hay sistema operativo."
retirada: "no se retira mientras exista el proyecto."
```
