# REGISTRO DE CONFORMIDAD — estado real de cada prueba

<!-- ads-lint: permitir-vocabulario-prohibido -->

> Este fichero existe para impedir una afirmación concreta: *«el sistema está probado»*
> cuando lo único que ocurrió es que alguien escribió la prueba.

## Los cuatro estados, y qué autoriza a decir cada uno

```text
contrato-definido        la prueba está escrita: dado / cuando / entonces / falla si.
                         NO existe validador. NO se ha ejecutado.
                         AUTORIZA A DECIR: "está definido qué habría que comprobar".

validador-implementado   existe código o guion que la comprueba.
                         NO se ha ejecutado sobre material real, o el material no existe.
                         AUTORIZA A DECIR: "es comprobable automáticamente".

prueba-ejecutada         se ha ejecutado sobre material real y hay salida registrada.
                         El resultado PUEDE ser fallo.
                         AUTORIZA A DECIR: "se ejecutó, y este fue el resultado".

prueba-superada          se ejecutó y pasó, con evidencia enlazada y reproducible.
                         AUTORIZA A DECIR: "esto funciona", y sólo en lo que la prueba cubre.

prueba-fallida           se ejecutó y falló. Es un estado legítimo y se publica igual.
```

**Regla dura:** ninguna prueba sube de estado por argumento. Sube porque se ejecutó y su
salida quedó registrada en la columna `evidencia`.

## T01–T74 — heredadas de (a) y (b)

Las setenta y cuatro pruebas de las secciones aprobadas están en estado
**`contrato-definido`**, con dos excepciones parciales que este kernel operativo mueve a
`validador-implementado`, indicadas en la tabla de abajo. **Ninguna está superada**,
porque la mayoría exige un runtime que todavía no existe.

| prueba | estado | por qué |
|---|---|---|
| T01–T24 (sección a) | contrato-definido | requieren runtime, estado persistido y dispatcher |
| T13 patrones | validador-implementado *(parcial)* | la forma del patrón se valida estructuralmente; su vigencia real no |
| T18 extensiones | validador-implementado *(parcial)* | `ads_lint` comprueba prefijo, contrato de doce campos y colisión de identificador; la colisión de autoridad se comprueba en `pruebas/T78-*` |
| T19 vetos | validador-implementado *(parcial)* | `ads_lint` exige los seis campos del contrato de veto en todo bloque `ads:veto` |
| T25 | abierta por diseño | depende de la sección (g) |
| T26–T74 (sección b) | contrato-definido | requieren runtime |

## T75 en adelante — nuevas de este kernel operativo

La numeración continúa en **T75**. Cada prueba vive en su fichero de `pruebas/` con un
bloque `ads:escenario`; esta tabla es el resumen y **se regenera desde esos bloques**.

<!-- TABLA-GENERADA: pruebas/REGISTRO-generado.md -->

Ver [`REGISTRO-generado.md`](REGISTRO-generado.md) para el estado vigente, producido por
`validadores/registro_pruebas.py` a partir de los propios escenarios.
