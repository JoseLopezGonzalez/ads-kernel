# PLANTILLA — DEVOLUCIÓN

Una devolución sin los cuatro campos **no es una devolución**: se rechaza y el paquete
vuelve a quien la emitió, sin gastar ninguna de las dos del freno de a.7.

```text
DEVOLUCIÓN — <ITEM-ID>/<nn>
de:          <CAP que devuelve> · rol <rol concreto>
a:           <CAP a cuya capa le falta algo>   ← la capacidad CONCRETA, no «hacia atrás»
devolución nº: 1 | 2      ← no existe la 3ª: se escala con las dos posturas escritas

QUÉ FALTA
  <en la capa concreta. No «el diseño está incompleto», sino qué elemento falta>

POR QUÉ ES INSUFICIENTE
  <qué no puede hacer el receptor con la capa tal como está>

QUÉ LO CERRARÍA
  <el artefacto o la comprobación concreta que resolvería el hueco>

EVIDENCIA
  <captura · medición · traza · grabación · salida de test · enlace al contrato roto>
  ← el tipo lo exige el handoff correspondiente en circuitos/

EFECTO SOBRE LA CAPA
  vigente | sustituida | invalidada     ← lo decide la capacidad PROPIETARIA de la capa,
                                          nunca quien devuelve (b.3, b.9)
```

## Lo que una devolución NO puede hacer

```text
NO PUEDE   invalidar la capa por su cuenta: eso es autoridad de su propietario
NO PUEDE   proponer la solución en lugar de nombrar el hueco
NO PUEDE   devolver «hacia atrás» sin nombrar la capacidad concreta
NO PUEDE   ser la tercera entre el mismo par sobre el mismo paquete
NO PUEDE   viajar sin la evidencia que el handoff exige
```

## Qué obliga a hacer al sistema

> Toda devolución obliga a DSP a **crear o reabrir el paquete de corrección en el mismo
> ciclo** (b.7). Un `devuelto` sin paquete de corrección es un defecto de despacho, no un
> estado legítimo.
