# VER — composición del equipo

```yaml ads:composicion
id: composicion:ver-dosier
capacidad: VER
clase_de_trabajo: "verificación de una capa de construcción"
condicion: "existe una capa de CON depositada y el item no es de tipo DIR."
roles:
  - rol: VER/dosier
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: VER/dosier
    de: [CON/implementacion]
    motivo: >
      G13 como estructura por defecto de esta capacidad: quien construyó verifica lo que
      evitó, no lo que cometió
ampliacion: >
  Con superficie afectada en varios entornos de la matriz del pack, se reparte la captura
  entre varios agentes de VER/dosier por entorno, con un integrador declarado que escribe
  el dosier único.
reduccion: "no admite reducción: sin dosier no hay evidencia que viaje hacia adelante."
retirada: "al emitir el dosier."
```

```yaml ads:composicion
id: composicion:ver-decision
capacidad: VER
clase_de_trabajo: "verificación de la decisión de un item DIR"
condicion: "el item es de tipo DIR y ha producido su registro de decisión e items derivados."
roles:
  - rol: VER/decision
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: VER/decision
    de: ["el propietario global del DIR y toda capacidad que participó en la decisión"]
    motivo: >
      quien participó en decidir da por escrito lo que tiene en la cabeza, y no ve los
      impactos sin item derivado
ampliacion: >
  Se añade gate conjunto con cada capacidad propietaria de una decisión sustituida. Eso no
  añade roles a VER: son confirmaciones de otras capacidades.
reduccion: "ninguna: VER:decision es obligatorio en todo DIR (b.16)."
retirada: "al emitir el dictamen."
```
