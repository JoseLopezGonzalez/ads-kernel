#!/usr/bin/env python3
"""mutacion — admisión por MUTACIÓN. Corte `V3` · `V6-05` a `V6-09`.

Los cinco puntos, con su criterio literal de §20.1:

  `V6-05`  se juzga la MUTACIÓN, no la mera existencia.
           Cierre: **cero** rutas gobernadas exentas por preexistencia.
  `V6-06`  `A M D T R C`, y `R`/`C` por sus DOS puntas.
           Cierre: las seis letras cubiertas; `R` y `C` por sus dos puntas.
  `V6-07`  cada comprobación DECLARA contra qué estado juzga, y la declarada es la usada.
           Cierre: base · `HEAD` · índice · árbol de trabajo, declarados y usados.
  `V6-08`  confirmar NO exime.
           Cierre: **cero** comprobaciones cuyo veredicto mejore al confirmar.
  `V6-09`  ficheros NUEVOS y PREEXISTENTES, las dos clases con guarda.
           Cierre: **cero** rutas gobernadas sin guarda por su antigüedad.

DECISIÓN · cuatro lecturas declaradas, y no una sola contra `HEAD`
    Alternativas: (a) `git diff <base>` y ya; (b) `git status`; (c) las cuatro referencias.
    Se elige (c). Con (a) una mutación que vive sólo en el índice —`git add` sin commit— no
    aparece, y una sin rastrear tampoco. Con (b) se ve el trabajo sucio pero se pierde todo
    lo ya CONFIRMADO desde la base, que es el vector de `S1-02`: el ataque commitea y
    `porcelain` queda VACÍO. Las cuatro juntas cubren el cuadrado entero, y cada fila del
    resultado dice de cuál viene: `V6-07` exige que la referencia declarada sea la usada, y
    aquí la declara la propia lectura que la produjo.

DECISIÓN · `R` y `C` producen DOS filas, no una
    Alternativas: (a) una fila con `origen` y `destino`; (b) dos filas, una por punta.
    Se elige (b) para el JUICIO, conservando (a) en la lectura. `V6-06` dice literalmente
    que «un renombrado con destino admitido y origen NO admitido da ROJO»: si el juicio
    recibe una sola fila, la regla tiene que acordarse de mirar las dos puntas, y olvidarlo
    es un falso verde silencioso. Con dos filas la punta de origen es una mutación de pleno
    derecho y ninguna regla puede saltársela por descuido.

DECISIÓN · la preexistencia NO exime, y por eso la base entra en la diferencia
    El defecto medido `S1-02` es exactamente éste: `_ampliaciones = (disco ∪ publicado) −
    base_gobernada` deja fuera todo lo que YA EXISTÍA en la base, «diga lo que diga hoy».
    Aquí la primera lectura es `diff <base> HEAD`, que es la que hace visible la MUTACIÓN
    de un fichero preexistente. La existencia en la base no es una exención: es sólo el
    punto desde el que se mide.
"""
from __future__ import annotations

from .errores import EstructuraAjena
from .lectura import LETRAS

# Las cuatro referencias del `V6-07`, con la lectura que las produce. La tabla es DATO: una
# comprobación no puede declarar una referencia y usar otra porque no elige la lectura.
LECTURAS_DECLARADAS = (
    {"referencia": "base",
     "que_compara": "la revisión base contra `HEAD`",
     "ve": "todo lo ya CONFIRMADO desde la base, incluida la mutación de un preexistente"},
    {"referencia": "HEAD",
     "que_compara": "`HEAD` contra el ÍNDICE",
     "ve": "lo preparado con `git add` y todavía sin confirmar"},
    {"referencia": "indice",
     "que_compara": "el ÍNDICE contra el árbol de trabajo",
     "ve": "lo modificado en disco y aún sin preparar"},
    {"referencia": "trabajo",
     "que_compara": "el árbol de trabajo contra lo versionado",
     "ve": "lo que no rastrea nadie"},
)


class Mutacion:
    """Una mutación juzgable: su letra, su ruta, su punta y su referencia DECLARADA."""

    __slots__ = ("letra", "ruta", "punta", "referencia", "similitud", "pareja")

    def __init__(self, letra, ruta, *, referencia, punta="destino", similitud=None,
                 pareja=None):
        if letra not in LETRAS:
            raise EstructuraAjena(
                "letra de mutación fuera del vocabulario `A M D T R C`: " + str(letra)
            )
        self.letra = letra
        self.ruta = ruta
        self.punta = punta
        self.referencia = referencia
        self.similitud = similitud
        self.pareja = pareja

    def clave(self):
        return (self.ruta, self.letra, self.punta, self.referencia)

    def a_dict(self):
        salida = {"letra": self.letra, "ruta": self.ruta, "punta": self.punta,
                  "referencia": self.referencia}
        if self.similitud:
            salida["similitud"] = self.similitud
        if self.pareja:
            salida["pareja"] = self.pareja
        return salida

    def __repr__(self):
        return "Mutacion(" + self.letra + " " + self.ruta + " @" + self.referencia + ")"


def _filas_a_mutaciones(filas):
    salida = []
    for fila in filas:
        letra = fila["letra"]
        if letra not in LETRAS:
            # `U` (sin fusionar), `X` (desconocido) y `B` (roto) no son del vocabulario de
            # `V6-06`. No se ignoran: se convierten en estructura ajena, porque un árbol con
            # un conflicto sin resolver no es un árbol sobre el que emitir veredicto.
            raise EstructuraAjena(
                "el árbol trae una mutación en estado `" + letra + "`, que no es una de "
                "las seis letras juzgables. No se emite veredicto sobre un árbol así"
            )
        if letra in ("R", "C"):
            salida.append(Mutacion(letra, fila["ruta"], referencia=fila["referencia"],
                                   punta="destino", similitud=fila["similitud"],
                                   pareja=fila["origen"]))
            # La punta de ORIGEN. En un renombrado ES un borrado de pleno derecho, y se
            # emite con la letra `D` porque eso es lo que le pasa a esa ruta. En una copia
            # el origen no cambia, pero SIGUE siendo una punta que hay que admitir: admitir
            # una copia es admitir que ese contenido se duplica DESDE esa ruta, y `V6-06`
            # dice literalmente que `R` y `C` se juzgan por sus DOS puntas. Conserva la
            # letra `C` para que la evidencia diga de qué punta habla.
            salida.append(Mutacion("D" if letra == "R" else "C", fila["origen"],
                                   referencia=fila["referencia"], punta="origen",
                                   similitud=fila["similitud"], pareja=fila["ruta"]))
            continue
        salida.append(Mutacion(letra, fila["ruta"], referencia=fila["referencia"]))
    return salida


def derivar(canal_de_lectura, base):
    """Las mutaciones del árbol respecto de `base`, por las CUATRO referencias declaradas.

    El orden del resultado es determinista: por ruta, letra, punta y referencia. La
    evidencia se publica, y un orden que dependiera de Git cambiaría entre ejecuciones.
    """
    mutaciones = []

    # 1 · base → HEAD. La que hace visible el ataque YA CONFIRMADO (`V6-08`).
    mutaciones.extend(_filas_a_mutaciones(
        canal_de_lectura.diferencia(base, "HEAD", referencia="base")
    ))
    # 2 · HEAD → índice. La mutación que vive sólo en el índice (`V6-07`).
    mutaciones.extend(_filas_a_mutaciones(
        canal_de_lectura.diferencia("--cached", referencia="HEAD")
    ))
    # 3 · índice → árbol de trabajo.
    mutaciones.extend(_filas_a_mutaciones(
        canal_de_lectura.diferencia(referencia="indice")
    ))
    # 4 · sin rastrear. Git no le pone letra: se le pone `A`, que es lo que es.
    for ruta in canal_de_lectura.rutas_sin_rastrear():
        mutaciones.append(Mutacion("A", ruta, referencia="trabajo"))

    vistas = set()
    unicas = []
    for mutacion in mutaciones:
        if mutacion.clave() in vistas:
            continue
        vistas.add(mutacion.clave())
        unicas.append(mutacion)
    unicas.sort(key=lambda m: (m.ruta, m.letra, m.punta, m.referencia))
    return unicas


def preexistentes(canal_de_lectura, base):
    """Conjunto de rutas que YA existían en la base. Se usa para CLASIFICAR, no para eximir."""
    return set(canal_de_lectura.rutas_del_arbol(base))


def clasificar(mutaciones, base_conocida):
    """Marca cada mutación como `nueva` o `preexistente`. `V6-09`: las dos con guarda."""
    salida = []
    for mutacion in mutaciones:
        entrada = mutacion.a_dict()
        entrada["clase"] = "preexistente" if mutacion.ruta in base_conocida else "nueva"
        salida.append(entrada)
    return salida


def cobertura_de_letras(mutaciones):
    """Qué letras del vocabulario aparecen. La matriz lo publica; nadie lo escribe a mano."""
    presentes = {mutacion.letra for mutacion in mutaciones}
    return {letra: (letra in presentes) for letra in LETRAS}
