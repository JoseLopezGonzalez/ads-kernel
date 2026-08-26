# Contratos transversales

Lo que vale para **todas** las capacidades. Un pack los amplía; no los sustituye.

| | contrato | qué fija |
|---|---|---|
| C1 | [`C1-EQUIPO-ROL-AGENTE-METODO.md`](C1-EQUIPO-ROL-AGENTE-METODO.md) | los siete conceptos y los veintiocho campos del contrato de rol |
| C2 | [`C2-AGENTES-Y-MODELOS.md`](C2-AGENTES-Y-MODELOS.md) | perfiles neutrales de proveedor, asignación, combinación y relevo |
| C3 | [`C3-METODO-EJECUTABLE.md`](C3-METODO-EJECUTABLE.md) | los diecisiete elementos y las siete reglas que hacen ejecutable un método |
| C4 | [`C4-MATERIALIZACION.md`](C4-MATERIALIZACION.md) | el algoritmo de materialización, ampliación y retirada |
| C5 | [`C5-HANDOFF.md`](C5-HANDOFF.md) | la forma de la entrega entre capacidades y de la devolución |
| C6 | [`C6-PRODUCTO-FUENTES-Y-WORKSPACE.md`](C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) | qué es una fuente, un componente y un workspace, y dónde vive cada verdad de un producto multi-repositorio |
| C7 | [`C7-GOBIERNO-GIT-MULTI-SOURCE.md`](C7-GOBIERNO-GIT-MULTI-SOURCE.md) | quién pide, ejecuta, bloquea y verifica cada operación Git, y cómo converge un cambio repartido entre varias fuentes |

## Lo que estos siete contratos garantizan juntos

```text
[ ] ningún rol decide fuera de su autoridad declarada
[ ] ningún equipo existe sin trabajo real que lo justifique
[ ] ningún método admite dos ejecuciones razonables con resultados distintos
[ ] ningún agente crítica lo que él mismo produjo
[ ] ningún cambio de modelo pierde la identidad ni la memoria de un rol
[ ] ninguna entrega entre equipos ocurre sin comprobación previa
[ ] ninguna devolución viaja sin evidencia
[ ] ningún paquete escribe en un repositorio que no declaró
[ ] ningún item se declara cerrado con una de sus fuentes sin integrar
```

Cada garantía tiene su prueba en [`../pruebas/`](../pruebas/REGISTRO-generado.md).
