# PLT — composición del equipo

```yaml ads:composicion
id: composicion:plt-desbloqueo
capacidad: PLT
clase_de_trabajo: "montar la pieza de maquinaria que desbloquea a otra capacidad"
condicion: >
  Existe un bloqueo declarado por otra capacidad, con la operación concreta que hoy no puede
  ejecutarse escrita.
roles:
  - rol: PLT/maquinaria
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: PLT/maquinaria
    de: ["ninguno: PLT no juzga el trabajo de nadie ni tiene veto"]
    motivo: >
      la separación de PLT es de COLA, no de independencia: su backlog propio evita que el
      trabajo de infraestructura compita con el trabajo por item
ampliacion: >
  Con varias piezas independientes, un agente por pieza y un integrador declarado que
  comprueba que el conjunto funciona junto.
reduccion: "no admite reducción."
retirada: "cuando quien declaró el bloqueo confirma que puede ejecutar la operación."
```

```yaml ads:composicion
id: composicion:plt-backlog
capacidad: PLT
clase_de_trabajo: "trabajo del backlog propio de plataforma"
condicion: >
  El item procede del backlog propio de PLT: mantenimiento de entornos, actualización de la
  integración continua u observabilidad que ENT ha declarado necesitar.
roles:
  - rol: PLT/maquinaria
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: PLT/maquinaria
    de: ["ninguno: no hay juicio sobre trabajo ajeno que separar"]
    motivo: "se declara expresamente para que la ausencia de separación sea una decisión y no un olvido"
ampliacion: >
  Si el trabajo del backlog resulta bloquear a otra capacidad, pasa a composicion:plt-desbloqueo
  y su prioridad la reevalúa DSP.
reduccion: "no admite reducción."
retirada: "al entregar la pieza documentada y reproducible."
```
