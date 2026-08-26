# SEG — composición del equipo

```yaml ads:composicion
id: composicion:seg-consulta
capacidad: SEG
clase_de_trabajo: "condiciones y revisión de seguridad de un item ordinario"
condicion: "el item cumple C-SEG y no incorpora ni actualiza dependencias."
roles:
  - rol: SEG/condiciones
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: SEG/condiciones
    de: [CON/implementacion]
    motivo: >
      quien construyó revisa el modelo de amenaza que tenía en la cabeza, no la superficie
      que produjo
ampliacion: >
  Si el item incorpora dependencias, el mismo rol ejecuta además SEG/Dependencia; no se
  añade rol nuevo, se añade método.
reduccion: "no admite reducción: es un servicio con veto y su ausencia no se compensa."
retirada: "al entregar las condiciones y la revisión posterior."
```

```yaml ads:composicion
id: composicion:seg-dependencia
capacidad: SEG
clase_de_trabajo: "incorporación o actualización de dependencias"
condicion: "el item es de tipo DEP, o incorpora una dependencia nueva."
roles:
  - rol: SEG/condiciones
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: SEG/condiciones
    de: [CON/implementacion]
    motivo: "quien necesita la dependencia para avanzar tiende a encontrarla aceptable"
ampliacion: >
  Con un árbol de dependencias grande, se reparte la enumeración entre varios agentes por
  rama, con un integrador declarado que emite el veredicto único.
reduccion: >
  ninguna: en DEP, SEG antes de construir es obligatorio por G28 y no se retira por prisa.
retirada: "al registrar el veredicto con su fecha y su condición de revisión."
```
