# CON — composición del equipo

```yaml ads:composicion
id: composicion:con-implementacion
capacidad: CON
clase_de_trabajo: "construcción productiva de un paquete"
condicion: >
  El paquete es de construcción productiva: sus capas anteriores están depositadas y el
  item no es INV ni DIR.
roles:
  - rol: CON/implementacion
    obligatorio: true
    agentes: "1 por paquete; varios paquetes del mismo item pueden ir en paralelo si cumplen las seis condiciones de a.5"
combinables: []
independientes:
  - rol: CON/implementacion
    de: ["el rol de VER que verifica este paquete", "DIS/revision-de-fidelidad"]
    motivo: "G13 como estructura por defecto: quien construyó no verifica ni compara su propio resultado"
ampliacion: >
  Un paquete grande NO se reparte entre dos agentes del mismo rol sobre el mismo código: se
  parte en dos paquetes con la condición de paralelismo comprobada, y DSP los despacha.
reduccion: "no admite reducción."
retirada: "al depositar la capa y ser aceptada por VER."
```

```yaml ads:composicion
id: composicion:con-experimental
capacidad: CON
clase_de_trabajo: "construcción para obtener evidencia dentro de un INV o un DIR"
condicion: >
  El item es de tipo INV y necesita construir para obtener evidencia, o es de tipo DIR y
  necesita un prototipo para poder decidir.
roles:
  - rol: CON/experimental
    obligatorio: true
    agentes: "1"
combinables: []
independientes:
  - rol: CON/experimental
    de: ["el rol de INV que formuló la hipótesis, cuando la evidencia sostiene una decisión difícilmente reversible"]
    motivo: "quien formula la hipótesis tiende a construir el experimento que la confirma"
ampliacion: >
  Dos experimentos alternativos en paralelo cuando la decisión depende de comparar dos
  caminos: cada uno con su agente y con el criterio de comparación escrito antes.
reduccion: "no admite reducción."
retirada: "al entregar la evidencia y ejecutar el criterio de descarte."
```
