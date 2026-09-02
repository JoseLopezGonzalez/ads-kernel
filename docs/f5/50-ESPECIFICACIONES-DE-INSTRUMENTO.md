# 50 · ESPECIFICACIONES DE INSTRUMENTO QUE `F5` DEBE A `F6`

**Tres hallazgos vivos tienen la fase desdoblada: `F5` escribe LA ESPECIFICACIÓN, `F6`
construye EL INSTRUMENTO.** Este documento es la mitad de `F5`, y **sólo esa mitad**.

> **LO QUE ESTE DOCUMENTO NO HACE, y es lo primero que hay que leer.**
> **NO CIERRA NINGÚN HALLAZGO.** Redactar la especificación de un instrumento no es
> construirlo, y declarar cerrado un hallazgo por haber escrito su especificación violaría
> el criterio de aceptación que prohíbe declarar superado nada por haberse redactado una
> enmienda. **Los tres siguen VIVOS**, en su sede, con su estado intacto.
>
> **Y uno de ellos no lo puede cerrar `F5` de ninguna manera:** la condición de cierre de la
> clase declara que **sólo un gate independiente posterior puede cerrarla**, y que **barrer
> no es certificar**.

**Sede del estado de los tres:**
[`06-DEUDA-Y-LIMITACIONES-VIGENTES.md`](../canonico/06-DEUDA-Y-LIMITACIONES-VIGENTES.md),
que **no cambia** y sigue publicándolos como vivos.

---

## 1 · `ESP-1` — La regla de ALCANCE DE RÓTULO para el barrido mecánico

**Hallazgo que la espera:** el barrido que debe detectar recuentos copiados **enmudece tras
el primer rótulo histórico**, contra la regla que el propio cambio escribe.

**LA ESPECIFICACIÓN, y es lo que `F6` tiene que implementar:**

```text
E-1.1  UN RÓTULO HISTÓRICO ACOTA, NO APAGA. Su alcance es el BLOQUE que rotula —desde el
       rótulo hasta el siguiente elemento del mismo nivel—, y NO el resto del fichero

E-1.2  el barrido CONTINÚA después de ese bloque, y vuelve a exigir la regla en todo lo
       que quede fuera de él

E-1.3  el alcance se DERIVA de la estructura del documento, no de la distancia en líneas
       ni de un número fijo

E-1.4  un rótulo histórico que no cierre su bloque de forma reconocible es un DEFECTO del
       documento rotulado, y el barrido lo señala en vez de callarse

E-1.5  el barrido PUBLICA cuántos bloques históricos excluyó y cuáles. Una exclusión
       silenciosa es la puerta que este hallazgo dejó abierta
```

**PRUEBA QUE `F6` DEBE SUPERAR:** un fichero con un rótulo histórico en medio y una
infracción **después** de ese bloque. El barrido debe **detectarla**. Hoy no la detecta, y
ésa es exactamente la promesa falsa que el hallazgo registra.

## 2 · `ESP-2` — La GUARDA DE TRUNCAMIENTO del extractor de campos

**Hallazgo que la espera:** el extractor **trunca en silencio** ante una valla de código sin
sangría, y la guarda que debía detectarlo **pasa igual**, porque sólo comprueba que el
resultado no esté vacío.

**LA ESPECIFICACIÓN:**

```text
E-2.1  la guarda compara el conjunto EXTRAÍDO contra el conjunto COMPLETO DERIVADO de la
       fuente, no contra el conjunto vacío

E-2.2  «no vacío» NO es una comprobación de completitud, y no se acepta como tal

E-2.3  si los dos conjuntos difieren, la guarda FALLA y NOMBRA los elementos que faltan

E-2.4  el fallo es CERRADO: ante estructura inesperada, el extractor se detiene en vez de
       devolver lo que haya podido leer

E-2.5  una valla de código sin sangría es estructura VÁLIDA de entrada, y el extractor la
       atraviesa sin truncar
```

**PRUEBA QUE `F6` DEBE SUPERAR:** un fichero cuyo campo contenga una valla sin sangría. El
extractor debe devolver el conjunto **completo**, y si no puede, **fallar nombrando lo que
falta**.

## 3 · `ESP-3` — La regla de CLASE contra recuentos y enumeraciones copiados

**Condición de cierre que la espera:** que ningún campo vigente copie un estado, recuento,
ordinal o enumeración que otra sede derive — **y que se compruebe POR CLASE, no por
instancia**.

**LA ESPECIFICACIÓN:**

```text
E-3.1  LA CLASE, definida: un campo VIGENTE no puede afirmar un ESTADO, un RECUENTO, un
       ORDINAL ni una ENUMERACIÓN cuya verdad viva en otra sede y pueda cambiar sin que
       este campo se entere

E-3.2  LO QUE SÍ PUEDE: remitir a la sede, o publicar el COMANDO que lo deriva junto a la
       afirmación

E-3.3  LA COMPROBACIÓN ES POR CLASE: se busca la FORMA —un cardinal, un ordinal o una lista
       cerrada dentro de un campo vigente—, no una lista de instancias conocidas. Cerrar
       instancias y dejar la clase abierta es el modo de fallo que este hallazgo persigue

E-3.4  INSENSIBLE A LA CAJA DE LETRA. El barrido actual es incompleto por caja —una grafía
       en versales escapa y la misma frase en minúsculas es cazada—, de modo que su verde
       no prueba lo que dice probar. La regla se comprueba sin distinguir caja

E-3.5  el barrido se INCLUYE A SÍ MISMO y a su propia regla: una mutación de la regla que
       la desafile debe dar ROJO

E-3.6  PUBLICA su cobertura: cuántos campos vigentes recorrió. Un barrido que pasa porque
       no leyó nada es el modo de fallo que esto evita
```

**PRUEBA QUE `F6` DEBE SUPERAR:** un cardinal nuevo insertado en un campo vigente **en
versales** debe dar ROJO. Hoy escaparía.

> **Y LO QUE NI `F6` PUEDE HACER CON ÉSTA:** implementar el instrumento y verlo en verde
> **no cierra la clase**. Su sede lo dice sin matices: **sólo un gate independiente
> posterior puede cerrarla**, y barrer no es certificar. `F5` escribe la regla; `F6`
> construye el barrido; **un tercero decide si la clase está cerrada.**

---

## 4 · Trazabilidad, y qué queda vivo después de esto

| especificación | hallazgo que la espera | mitad de `F5` | mitad de `F6` | ¿cerrado? |
|---|---|---|---|---|
| `ESP-1` | el barrido que enmudece | **hecha aquí** | el instrumento | **NO. Vive** |
| `ESP-2` | el extractor que trunca | **hecha aquí** | el instrumento | **NO. Vive** |
| `ESP-3` | la clase de recuentos copiados | **hecha aquí** | el instrumento | **NO, y su cierre NO es de `F6`: es de un gate independiente posterior** |

**Ninguno de los tres cambia de estado en su sede por la existencia de este documento.**
