# CONTRATO · VERIFICADOR DE ADMISIÓN

**Qué es.** El contrato derivado del entregable `F6-A`, cuyos puntos son las filas
`V6-01`…`V6-19` de `11-ARQ` §20.1 —`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, que no viaja al proyecto instalado—.
Este corte construye `V2`, `V3`, `V4` y `V5` del plan.

**Qué NO es.** No es la batería interna del corpus. `§20.0` lo separa a propósito: la batería
comprueba la CONSISTENCIA del corpus; esto juzga si una MUTACIÓN es admisible. Un verde de la
primera no dice nada de lo segundo.

---

## 1 · Qué cubre cada corte, y qué queda fuera

```text
V2 · lectura Git segura       V6-01 V6-02 V6-03 V6-04      lectura.py · censo.py
V3 · admisión por MUTACIÓN    V6-05 V6-06 V6-07 V6-08 V6-09 mutacion.py
V4 · auto-inclusión           V6-10 V6-11 V6-12            perimetro.py · censo.py
V5 · matriz adversarial       V6-13 V6-14 V6-17 V6-18 V6-19 matriz.py · formulas.py

FUERA DE ESTE CORTE, y se declara en vez de fingirse:
V6-15  los ÁRBOLES ADVERSARIALES derivados de las cabeceras de los gates. Su conjunto se
       DERIVA con el comando de §20.5, y ese derivador no es de este corte
V6-16  la RAÍZ EXTERNA productiva. Se demuestra la PROPIEDAD —el verificador corre desde
       fuera del árbol y con el árbol sin permiso de escritura—, no el despliegue
```

Todo veredicto publica su lista `fuera_de_alcance`, de modo que nadie pueda leer un verde
como si cubriera los diecinueve puntos.

## 2 · El canal único de lectura · `V6-01`–`V6-04`

Toda lista de rutas se lee con **`-z`** y decodificación **estricta**. Una lectura con un
separador que una ruta puede contener es `LecturaInsegura` **antes** de invocar nada. Salida
truncada, no decodificable o con estructura ajena → **ROJO nombrando la causa**, nunca una
lista vacía con éxito.

**El censo de lecturas se DERIVA del código con `ast`**, no con `grep` y no a mano: una
invocación de Git escrita fuera del canal aparece en el censo y da ROJO. Es lo que impide
una vía paralela oculta.

## 3 · Se juzga la MUTACIÓN, no la existencia · `V6-05`–`V6-09`

```text
· un fichero PREEXISTENTE mutado se juzga igual que uno nuevo. Existir en la base NO exime
· las seis letras `A M D T R C`, y `R`/`C` por SUS DOS PUNTAS: un renombrado con destino
  admitido y origen no admitido da ROJO
· cada comprobación DECLARA contra qué estado juzga —revisión base, `HEAD`, índice o árbol
  de trabajo— y la declarada es la usada. Una mutación visible sólo en el índice, o sólo
  sin rastrear, SE VE
· confirmar NO exime: el mismo ataque da ROJO antes y después del commit
```

## 4 · El censo de zonas, y la deuda `S1-02` · `V6-10`

**Es el punto central de este corte.** El censo de ZONAS se **deriva** del registro canónico
de fuentes y del árbol, y **cada zona lleva una condición de CONTENIDO declarada y
ejecutada**. Una zona sin condición **da ROJO**: no pasa por omisión.

> **Qué era `S1-02`, y por qué «añadir la raíz» no lo cerraba.** El universo gobernado
> derivaba el eje equivocado: derivaba QUÉ CONJUNTO se examina —lo que aparece y lo que
> desaparece respecto de la revisión base— y no QUÉ PROPIEDAD se examina —la existencia en
> vez del CONTENIDO—. Un fichero que ya existía en la base **no era ampliación dijera lo que
> dijera hoy**, y los tres inventarios de contenido que había no alcanzaban a la **RAÍZ del
> repositorio**. El ataque medido: reescribir `START_HERE.md` con una sentencia que se
> declaraba superior a la sede del Owner, confirmarlo, y ver `git status` vacío y
> **38/38 en verde**.
>
> **Se demuestra en los dos sentidos, y ésa es la evidencia.** La regla anterior se
> REPRODUCE dentro de la batería, con su procedencia escrita, y sobre el mismo árbol atacado
> da **VERDE**; la de este contrato da **ROJO**. Con su control positivo —el árbol sin
> ataque da verde con las dos— y con el control del control —la regla anterior sí ve una
> ampliación, luego no es la constante verde—. Y el remedio se comprueba sobre el **eje** y
> no sobre la zona: el mismo ataque en cuatro zonas de clases distintas, ninguna nombrada en
> ninguna regla.

## 5 · El instrumento se incluye a sí mismo · `V6-11` · `V6-12`

Una mutación del propio verificador o de su política da **ROJO aunque vaya declarada**: la
declaración la escribe quien opera, y si bastara para eximirse, cambiar la regla y aprobarse
con ella serían el mismo acto. Cero rutas del instrumento exentas.

La **sede del Owner** conserva su contrato append-only contrastado contra el **COMMIT DE
NACIMIENTO** y no contra `HEAD`: añadir una resolución es legítimo, alterar una letra de lo
publicado da ROJO **aunque esté confirmado**, y también cuando un commit posterior la
blanquea.

## 6 · La matriz y las fórmulas · `V6-13` · `V6-14` · `V6-17` · `V6-18` · `V6-19`

```text
SEIS FORMAS de nombre y contenido, y SEIS letras de mutación, cada una con fixture
positivo y negativo. Un control que no puede ponerse rojo no es evidencia

SIN ANCLA EXTERNA el veredicto es INDETERMINADO, nunca VERDE: `V6-17` prohíbe sostener la
integridad de un árbol con un digest que ese mismo árbol calcula

falsos_verdes = 0 y falsos_rojos = 0, MEDIDOS y PUBLICADOS por la matriz

UNA SOLA SEDE por fórmula compartida, con censo DERIVADO del código: una segunda definición
aparece y da ROJO aunque hoy coincida. Y si la importación de la sede falla, el instrumento
NO EMITE: no calcula con una suya
```

## 7 · Qué demuestra, y dónde

`T188`, `T189` y `T190` en [`pruebas/test_admision.py`](pruebas/test_admision.py), sobre
árboles Git **reales** con forma de corpus, y los pasos 21 y 22 de `T193` en
[`pruebas/escenario_e2e_runtime.py`](pruebas/escenario_e2e_runtime.py). Punto ejecutable:
[`ads_admision.py`](ads_admision.py).

**Nada de esto está CERTIFICADO**, y `V6-18` medido en verde **no** es el criterio `B2` de
`F6`: ése exige la suite entera, incluidos los puntos que este corte declara fuera.
