# Plantilla — INFORME DE CIERRE

> **Un informe que suma obligaciones satisfechas y retiradas y lo presenta como entregado
> es un defecto de conformidad, no un redondeo** (b.10). Esta plantilla existe para que esa
> suma sea imposible: las dos cifras van en columnas distintas y con encabezados distintos.

Lo comprueba [`gate:cierre-de-item`](../recorrido/00-OBLIGACIONES-Y-CIERRE.md) en su
comprobación `informe-separa`.

```text
CIERRE — <ITEM-ID>
proceso:            <FEA|GAP|DEF|INC|INV|DEU|DEP|AUD|DIR|SIS>
ruta vigente:       r<n>
propietario global: <capacidad>
cerrado:            <fecha ISO>

TERMINACIÓN
  paquetes de la ruta vigente:  <n> cerrados · <m> cancelados · 0 abiertos

OBLIGACIONES SATISFECHAS   <N>      ← EL RESULTADO EXISTE
  <id de la obligación>
     capa vigente:  <enlace al paquete y su versión>
     criterio:      <el criterio de satisfacción, y quién lo comprobó>

OBLIGACIONES RETIRADAS     <M>      ← EL RESULTADO NO EXISTE, y consta que se decidió así
  <id de la obligación>
     retirada en:   <recomposición r<n> · fecha>
     autoridad:     <quién tuvo autoridad para retirarla>
     efecto:        <cómo afecta al resultado perseguido>

  ESTAS M NO SON FUNCIONALIDAD ENTREGADA. No se suman a las N, no aparecen como
  evidencia y no se reportan como resultado.

VIGENCIA
  ninguna obligación se apoya en una capa `invalidada`:  <sí|NO CIERRA>

INTEGRACIÓN SEMÁNTICA
  declarada por:  <rol del propietario global>   <enlace a 03-integracion.md>

APRENDIZAJE
  learning_candidate:  none | <enlace a la señal>
  paquete de APR:      no creado | <enlace>
```

## Los cuatro errores que estropean un informe de cierre

```text
1  SUMAR N+M y llamarlo entregado. Es el defecto que esta plantilla existe para impedir.
2  Cerrar con una obligación HUÉRFANA: ni satisfecha ni retirada. El item no cierra; su
   estado es `bloqueado` o `en espera` según b.4 P10.
3  Declarar retirada una obligación sin decir QUIÉN tuvo autoridad. Sin autoridad
   identificada no hay retirada: hay una obligación huérfana con mejor redacción.
4  Contar como satisfecha una obligación que se apoya en una capa `invalidada`. Una capa
   invalidada no satisface nada; una `sustituida` satisface sólo a través de la que la
   reemplaza.
```
