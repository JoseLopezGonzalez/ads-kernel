# REGISTRO DE CONFORMIDAD — estado real de cada prueba


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

**Y la evidencia tampoco se escribe a mano.** La publica
[`validadores/registrar_evidencia.py`](../validadores/registrar_evidencia.py), que descubre
los validadores del manifiesto canónico, los invoca por su ruta completa terminada en
`.py`, captura stdout, stderr y código de salida **por separado**, escribe en un temporal y
publica con reemplazo atómico **sólo si el código fue cero**. Una ejecución que falla deja
intacta la evidencia anterior.

Que lo publicado demuestre lo que el informe afirma lo comprueba **T158**
([`comprobar_evidencia.py`](../validadores/comprobar_evidencia.py)). Existe por un defecto
real: ocho de diez ficheros de evidencia de una entrega anterior contenían
`python3: can't open file` —el procedimiento construía el nombre del script sin extensión y
redirigía el error del intérprete dentro del fichero— mientras el informe seguía afirmando
«todos EXIT 0». Nada lo detectó porque nada comprobaba la evidencia.

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
| T25 | **cubierta por `G-A2`** | la sección (g) existe y está APROBADA, y su condición de aceptación `G-A2` la cubre, incluida su cualificación. Se demuestra en `T175` |
| T26–T74 (sección b) | contrato-definido | requieren runtime |

## T159–T171 — la enmienda E2, un producto no es un repositorio

Viven en [`T159-T170-multirepo.md`](T159-T170-multirepo.md) —el nombre se conserva porque la
enmienda `E2`, que no se reescribe, lo enlaza por esa ruta— y las ejecutan **tres**
validadores distintos, porque comprueban cosas distintas:

```text
comprobar_fuentes.py             el ADS Project es VÁLIDO, sin tocar el disco
tooling/tests/test_workspace.py  el workspace se MATERIALIZA, con repos Git locales
                                 temporales. SIN RED: Git sólo tiene permitido el
                                 transporte `file`, y una prueba lo comprueba.
comprobar_arranque.py            el arranque produce la topología correcta, en la rama
                                 documentada, y el proyecto creado declara dónde se lee
                                 cada criterio de descubrimiento del §100
```

## T172–T181 — el estado durable, ejecutado

Viven en [`T172-T181-estado-durable.md`](T172-T181-estado-durable.md) y son las primeras
pruebas del corpus que **ejecutan un motor**, no un validador de documentos. Crean almacenes
reales, **matan procesos** en fronteras controladas y lanzan **procesos concurrentes**. La
distinción con la batería documental no es de estilo: un verde de `ads_lint` no dice nada
sobre si una transición sobrevive a un corte de corriente.

```text
validadores/entorno.py                          T172 — la guarda de entorno, antes de correr
runtime/pruebas/test_estado_durable.py          T173..T179 — el motor, caso a caso
runtime/pruebas/escenario_extremo_a_extremo.py  T180 — los quince pasos de una sola pieza
validadores/comprobar_arranque.py               T181 — la norma viaja al proyecto instalado
```

**Ninguna de ellas certifica nada.** `prueba-superada` significa que la prueba se ejecutó y
pasó; la CERTIFICACIÓN de `F6` la emite un juicio independiente y no quien construyó.

Dos quedan en `contrato-definido` y lo dicen: **T169** —integración parcial— exige runtime,
y **T170** —reanudación multi-fuente— exige un guion manual con dos repositorios reales.
**Seguirán en `contrato-definido` mientras no exista runtime y un piloto real**, y ningún
informe puede contarlas como demostradas.

**T171 declara su propio alcance.** Comprueba que cada criterio del §100 tiene un sitio
donde leerse en el proyecto recién creado. Eso es cobertura ESTRUCTURAL: no demuestra que un
agente lo descubra, que es lo que el §100 pide de verdad y lo que sigue pendiente de piloto.

## T75 en adelante — nuevas de este kernel operativo

La numeración continúa en **T75**. Cada prueba vive en su fichero de `pruebas/` con un
bloque `ads:escenario`; esta tabla es el resumen y **se regenera desde esos bloques**.

<!-- TABLA-GENERADA: pruebas/REGISTRO-generado.md -->

Ver [`REGISTRO-generado.md`](REGISTRO-generado.md) para el estado vigente, producido por
`validadores/registro_pruebas.py` a partir de los propios escenarios.

Y [`RECUENTOS-generado.md`](RECUENTOS-generado.md) para cuántas capacidades, roles, métodos
y campos hay realmente. **Ninguna de esas cifras se escribe a mano en ningún documento**:
se derivan del corpus y `comprobar_recuentos.py` comprueba que nadie afirme otra (T151).
