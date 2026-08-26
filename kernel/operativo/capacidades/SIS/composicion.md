# SIS — composición del equipo

```yaml ads:composicion
id: composicion:sis-cambio
capacidad: SIS
clase_de_trabajo: "cambio del kernel operativo justificado por una fricción real"
condicion: >
  Existe un item SIS con su justificación de producto enlazada, y el cambio afecta a
  contratos, esquemas, métodos, composiciones o validadores.
roles:
  - rol: SIS/evolucion
    obligatorio: true
    agentes: "1"
  - rol: SIS/coherencia
    obligatorio: true
    agentes: "1, distinto del anterior"
combinables: []
independientes:
  - rol: SIS/coherencia
    de: [SIS/evolucion]
    motivo: >
      quien escribió el contrato no detecta que ha duplicado una verdad ni que ha dejado un
      enlace apuntando a lo que él tenía en la cabeza
ampliacion: >
  Si el cambio modifica el runtime, se añaden paquetes de CON, VER y ENT: la activación
  segura y reversible es obligatoria (b.16).
reduccion: >
  SIS/coherencia se retira cuando el cambio afecta a un solo fichero y no introduce ninguna
  verdad nueva: entonces basta el validador.
retirada: "cuando el cambio está integrado con su validador y su prueba en estado real."
```

```yaml ads:composicion
id: composicion:sis-conformidad
capacidad: SIS
clase_de_trabajo: "auditoría de conformidad de una organización instalada"
condicion: >
  Se instala el kernel en un proyecto, se audita un corpus en curso, o un cambio grande del
  kernel operativo exige revalidar.
roles:
  - rol: SIS/coherencia
    obligatorio: true
    agentes: "1"
  - rol: SIS/evolucion
    obligatorio: false
    agentes: "1"
    condicion: "algún hallazgo está en el propio kernel operativo y hay que corregirlo"
combinables: []
independientes:
  - rol: SIS/coherencia
    de: [SIS/evolucion]
    motivo: "auditar el corpus que uno mismo acaba de escribir no es una auditoría"
ampliacion: >
  Con varios packs instalados, se reparte la comprobación de extensiones por pack, con un
  integrador declarado que emite el informe único.
reduccion: "no admite reducción: sin auditoría independiente no hay informe de conformidad."
retirada: "al publicar el informe y enrutar los items de cada hallazgo."
```
