#!/usr/bin/env python3
"""perimetro — auto-inclusión, condiciones de ZONA y veredicto. Corte `V4` · `V6-10` a `V6-12`,
más `V6-17`.

**ÉSTE ES EL MÓDULO QUE CIERRA `S1-02`**, y conviene decir con precisión qué era el defecto,
porque el remedio equivocado es más tentador que el bueno.

    LO QUE FALLABA (`docs/evolucion/28-SEPTIMO-GATE-DE-CERTIFICACION-F4C.md` §3.2 y §3.6)
    El universo gobernado se derivaba como `_ampliaciones = (disco ∪ publicado) − base`.
    Eso cubre la APARICIÓN y la DESAPARICIÓN de ficheros: la TOPOLOGÍA. No cubre su
    CONTENIDO. Un fichero que ya existía en la revisión base «no es ampliación diga lo que
    diga hoy», y la RAÍZ del repositorio no estaba en ningún inventario de contenido. Con
    eso, `START_HERE.md` se reescribió entero con una sentencia que se declaraba superior a
    la sede del Owner, se confirmó, `git status --porcelain` quedó VACÍO y la batería dio
    **38/38 comprobaciones en verde**. La segunda instancia (§3.6) ni siquiera tocó la raíz:
    reescribió el contenido de `kernel/operativo/pruebas/evidencia/fuentes-salida.txt`, un
    fichero YA enumerado, y volvió a dar **38/38**.

    LO QUE **NO** LO CIERRA, y por qué no se hace
    Buscar palabras —«PREVALECE», «SENTENCIA», «AUTORIZADA»— cierra una instancia y deja la
    clase abierta: el atacante siguiente escribe otra frase. Añadir «la raíz» a un inventario
    de contenido cierra otra instancia y deja la clase abierta: la §3.6 no toca la raíz. El
    eje equivocado era EXISTENCIA en vez de CONTENIDO, y el remedio tiene que ser sobre el
    eje, no sobre la zona.

    LO QUE SÍ LO CIERRA, y es `V6-10` literal
    **Toda ZONA del censo derivado tiene una condición de CONTENIDO declarada y ejecutada, y
    una zona sin condición da ROJO en vez de pasar por omisión.** El censo de zonas se DERIVA
    de `docs/canonico/FUENTES-CANONICAS.yml` y del árbol; una ruta que ninguna zona clasifica
    no «pasa»: es `SIN_ZONA`, y es ROJO.

DECISIÓN · la condición de una zona se declara por CLASE y no fichero a fichero
    Alternativas: (a) un inventario de ficheros con su condición; (b) una condición por clase
    de zona.
    Se elige (b). Un inventario escrito a mano CADUCA —es el defecto que el propio corpus
    documenta tres veces, `Q-04`, `T-03` y `A2`— y un fichero nuevo entra sin condición y
    pasa. La clase la asigna el registro canónico por PATRÓN, de modo que un directorio nuevo
    hereda su condición sin que nadie escriba una línea, y un directorio que ningún patrón
    cubre da ROJO en vez de colarse.

DECISIÓN · `EVIDENCIA` e `HISTORICA` tienen contenido INMUTABLE, no «declarable»
    Es lo que cierra la segunda instancia de `S1-02` sin nombrarla. Una salida publicada por
    el runner canónico y un pack retirado por trazabilidad no se «modifican con permiso»: si
    su contenido cambia, dejan de ser lo que dicen ser. Una declaración de admisión NO puede
    levantar esta condición, y por eso `admitida` no se consulta para estas dos clases.

DECISIÓN · el instrumento no puede cambiar y certificarse en la misma pasada
    Alternativas: (a) permitir mutar el verificador si la mutación va declarada; (b) que toda
    mutación del instrumento sea ROJO en la pasada que la contiene.
    Se elige (b). Con (a) la declaración de admisión —que la escribe quien opera— basta para
    cambiar la regla y aprobarse con la regla nueva en el mismo acto: el instrumento se
    saldría de su alcance por la puerta de la declaración, que es exactamente lo que `V6-11`
    prohíbe. Con (b) cambiar el verificador exige una pasada aparte, juzgada por el
    verificador ANTERIOR y desde la raíz externa, que es lo que `g.15` ya obliga. El coste
    —dos pasadas para tocar el instrumento— es el precio de que no haya rutas exentas.

DECISIÓN · `V6-17`: el veredicto NO se sostiene sobre un digest del propio árbol
    Un `cid` recalculado sobre el árbol SIEMPRE cuadra con el árbol, porque lo calcula el
    árbol. Aquí el ancla la aporta la DECLARACIÓN, que llega de fuera. Sin ancla externa el
    veredicto no es VERDE: es `INDETERMINADO`, y se dice por qué.
"""
from __future__ import annotations

import re

from .errores import (
    InstrumentoAlterado,
    MutacionNoDeclarada,
    SedeDelOwnerAlterada,
    SinAnclaExterna,
    ZonaSinCondicion,
)
from .formulas import digest_de_contenido

# ===========================================================================
#  Las CONDICIONES DE CONTENIDO, por clase de zona. Ninguna clase sin condición.
# ===========================================================================
DECLARADA = "contenido-declarado"
INMUTABLE = "contenido-inmutable"
APPEND_ONLY = "append-only-contra-el-nacimiento"
INSTRUMENTO = "instrumento-inmutable-en-la-pasada"

CONDICIONES_DE_ZONA = {
    "AUTORIDAD_SUPERIOR": {
        "condicion": APPEND_ONLY,
        "motivo": "material aprobado y sede del Owner: se amplía, no se reescribe",
    },
    "CANONICA_OPERATIVA": {
        "condicion": DECLARADA,
        "motivo": "corpus canónico vigente: toda mutación de contenido va declarada",
    },
    "CONTRATO_O_ESQUEMA_TECNICO": {
        "condicion": DECLARADA,
        "motivo": "contratos, esquemas y código: toda mutación de contenido va declarada",
    },
    "DERIVADA": {
        "condicion": DECLARADA,
        "motivo": (
            "proyecciones y puertas de entrada. Es la clase de `README.md` y de "
            "`START_HERE.md`, y es donde `S1-02` §3.2 entró: derivada NO significa exenta"
        ),
    },
    "EVIDENCIA": {
        "condicion": INMUTABLE,
        "motivo": (
            "salidas publicadas y documentos de gate. Es la clase de "
            "`kernel/operativo/pruebas/evidencia/`, por donde entró `S1-02` §3.6"
        ),
    },
    "HISTORICA": {
        "condicion": INMUTABLE,
        "motivo": "conservado por trazabilidad: si cambia, deja de ser el testimonio",
    },
    "NO_APLICABLE_A_IMPLEMENTACION": {
        "condicion": DECLARADA,
        "motivo": "material de trabajo: no autoriza a implementar, pero sí se gobierna",
    },
}

# La sede APPEND-ONLY que `V6-12` nombra, y su fuente. Se contrasta contra el COMMIT DE
# NACIMIENTO y no contra `HEAD`: contra `HEAD` la comprobación es una tautología.
SEDE_DEL_OWNER = "docs/owner/ADS-OWNER-RESOLUCIONES.md"

# Letras cuyo efecto es una mutación de CONTENIDO de una ruta que sobrevive.
LETRAS_DE_CONTENIDO = ("M", "T", "C")
LETRAS_DE_TOPOLOGIA = ("A", "D", "R")


class Zona:
    """Una zona del censo derivado: su patrón, su clase y su condición de contenido."""

    __slots__ = ("patron", "clase", "motivo_de_zona", "condicion", "motivo_de_condicion",
                 "_compilado")

    def __init__(self, patron, clase, motivo_de_zona):
        self.patron = patron
        self.clase = clase
        self.motivo_de_zona = motivo_de_zona
        declarada = CONDICIONES_DE_ZONA.get(clase)
        self.condicion = declarada["condicion"] if declarada else None
        self.motivo_de_condicion = declarada["motivo"] if declarada else None
        self._compilado = re.compile(patron)

    def casa(self, ruta):
        return bool(self._compilado.search(ruta))

    def a_dict(self):
        return {
            "patron": self.patron,
            "clase": self.clase,
            "condicion": self.condicion,
            "motivo": self.motivo_de_condicion,
            "declarada": self.condicion is not None,
        }


class Declaracion:
    """La DECLARACIÓN DE ADMISIÓN. Llega de FUERA del árbol; el árbol no la escribe.

    Contiene el ancla externa —`V6-17`—, las mutaciones admitidas con su motivo, y la
    autoridad que las declara. Un árbol que pudiera escribir su propia declaración decidiría
    quién lo verifica, que es lo que `O25` §3 y `g.15` prohíben.
    """

    def __init__(self, *, ancla=None, autoridad="", admitidas=(), digest_del_censo=None):
        self.ancla = ancla
        self.autoridad = autoridad
        self.digest_del_censo = digest_del_censo
        self._admitidas = {}
        for entrada in admitidas:
            ruta = entrada["ruta"] if isinstance(entrada, dict) else entrada
            motivo = entrada.get("motivo", "") if isinstance(entrada, dict) else ""
            self._admitidas[ruta] = motivo

    def admite(self, ruta):
        return ruta in self._admitidas

    def motivo(self, ruta):
        return self._admitidas.get(ruta, "")

    def rutas(self):
        return tuple(sorted(self._admitidas))

    def a_dict(self):
        return {
            "ancla": self.ancla,
            "autoridad": self.autoridad,
            "admitidas": [{"ruta": r, "motivo": self._admitidas[r]} for r in self.rutas()],
            "digest_del_censo": self.digest_del_censo,
        }


class Hallazgo:
    """Un motivo de ROJO, con el punto de §20.1 que lo exige y la ruta que lo produce."""

    __slots__ = ("punto", "codigo", "ruta", "zona", "causa")

    def __init__(self, punto, codigo, ruta, zona, causa):
        self.punto = punto
        self.codigo = codigo
        self.ruta = ruta
        self.zona = zona
        self.causa = causa

    def a_dict(self):
        return {"punto": self.punto, "codigo": self.codigo, "ruta": self.ruta,
                "zona": self.zona, "causa": self.causa}

    def __repr__(self):
        return "Hallazgo(" + self.punto + " " + self.codigo + " " + self.ruta + ")"


class Veredicto:
    """El resultado del verificador. `VERDE`, `ROJO` o `INDETERMINADO`, y nunca otra cosa."""

    def __init__(self, color, hallazgos, informe):
        self.color = color
        self.hallazgos = list(hallazgos)
        self.informe = dict(informe)

    @property
    def ok(self):
        return self.color == "VERDE"

    def a_dict(self):
        salida = dict(self.informe)
        salida["color"] = self.color
        salida["hallazgos"] = [hallazgo.a_dict() for hallazgo in self.hallazgos]
        return salida

    def __repr__(self):
        return "Veredicto(" + self.color + ", " + str(len(self.hallazgos)) + " hallazgos)"


class Perimetro:
    """Cruza el censo de zonas con las mutaciones y emite el veredicto."""

    def __init__(self, zonas, *, prefijos_de_instrumento=()):
        self.zonas = list(zonas)
        self.prefijos_de_instrumento = tuple(prefijos_de_instrumento)

    # -- clasificación -----------------------------------------------------
    def zona_de(self, ruta):
        """La PRIMERA zona cuyo patrón casa. El orden del registro es normativo."""
        for zona in self.zonas:
            if zona.casa(ruta):
                return zona
        return None

    def es_instrumento(self, ruta):
        return any(ruta.startswith(prefijo) for prefijo in self.prefijos_de_instrumento)

    # -- el censo de zonas, con su condición --------------------------------
    def censo(self, rutas_del_arbol):
        """`V6-10`: cada zona, su condición y CUÁNTAS rutas cubre. Derivado, no escrito."""
        filas = []
        cubiertas = {}
        for zona in self.zonas:
            cubiertas[zona.patron] = 0
        sin_zona = []
        for ruta in sorted(rutas_del_arbol):
            zona = self.zona_de(ruta)
            if zona is None:
                sin_zona.append(ruta)
                continue
            cubiertas[zona.patron] += 1
        for zona in self.zonas:
            fila = zona.a_dict()
            fila["rutas"] = cubiertas[zona.patron]
            filas.append(fila)
        return {
            "zonas": filas,
            "sin_condicion": [f["patron"] for f in filas if not f["declarada"]],
            "sin_zona": sin_zona,
            "ok": not [f for f in filas if not f["declarada"]] and not sin_zona,
        }

    # -- el juicio ---------------------------------------------------------
    def juzgar(self, mutaciones, declaracion, *, contenidos=None, nacimiento=None):
        """Aplica a cada mutación la condición de CONTENIDO de su zona.

        `contenidos` es `{ruta: (bytes_en_la_base, bytes_ahora)}` y sólo hace falta para la
        condición append-only. `nacimiento` es el contenido de la sede del Owner en su
        COMMIT DE NACIMIENTO, que es contra lo que `V6-12` obliga a contrastar.
        """
        hallazgos = []
        for mutacion in mutaciones:
            ruta = mutacion.ruta
            zona = self.zona_de(ruta)

            # `V6-11` · el instrumento se incluye a sí mismo, y va PRIMERO: ninguna otra
            # regla puede llegar antes y eximirlo.
            if self.es_instrumento(ruta):
                hallazgos.append(Hallazgo(
                    "V6-11", InstrumentoAlterado.CODIGO, ruta,
                    zona.clase if zona else "(sin zona)",
                    "el propio verificador o su política mutan en la pasada que juzgan "
                    "(letra " + mutacion.letra + ", punta " + mutacion.punta
                    + ", referencia " + mutacion.referencia + "). Cambiar el instrumento "
                    "exige una pasada aparte, juzgada por el instrumento anterior",
                ))
                continue

            # `V6-10` · una ruta que ninguna zona clasifica NO pasa por omisión.
            if zona is None:
                hallazgos.append(Hallazgo(
                    "V6-10", ZonaSinCondicion.CODIGO, ruta, "(sin zona)",
                    "ninguna zona del censo derivado clasifica esta ruta, luego no tiene "
                    "condición de contenido declarada. Una zona sin condición da ROJO",
                ))
                continue
            if zona.condicion is None:
                hallazgos.append(Hallazgo(
                    "V6-10", ZonaSinCondicion.CODIGO, ruta, zona.clase,
                    "la clase `" + zona.clase + "` no declara condición de CONTENIDO. No "
                    "pasa por omisión",
                ))
                continue

            # `V6-12` · la sede del Owner, contra el NACIMIENTO y no contra `HEAD`.
            if ruta == SEDE_DEL_OWNER or zona.condicion == APPEND_ONLY:
                fallo = self._juzgar_append_only(
                    mutacion, zona, contenidos or {}, nacimiento
                )
                if fallo is not None:
                    hallazgos.append(fallo)
                continue

            if zona.condicion == INMUTABLE:
                hallazgos.append(Hallazgo(
                    "V6-10", MutacionNoDeclarada.CODIGO, ruta, zona.clase,
                    "la zona `" + zona.clase + "` tiene contenido INMUTABLE ("
                    + zona.motivo_de_condicion + ") y ha mutado con la letra "
                    + mutacion.letra + " contra la referencia " + mutacion.referencia
                    + ". Ninguna declaración de admisión levanta esta condición",
                ))
                continue

            if zona.condicion == DECLARADA and not declaracion.admite(ruta):
                punto = "V6-05" if mutacion.letra in LETRAS_DE_CONTENIDO else "V6-09"
                hallazgos.append(Hallazgo(
                    punto, MutacionNoDeclarada.CODIGO, ruta, zona.clase,
                    "mutación de CONTENIDO no declarada: letra " + mutacion.letra
                    + ", punta " + mutacion.punta + ", referencia " + mutacion.referencia
                    + ". La zona `" + zona.clase + "` exige declaración y existir en la "
                    "revisión base NO exime",
                ))
        return hallazgos

    def _juzgar_append_only(self, mutacion, zona, contenidos, nacimiento):
        """`V6-12`: añadir es legítimo; alterar una letra de lo publicado es ROJO."""
        ruta = mutacion.ruta
        if mutacion.letra in ("D", "R"):
            return Hallazgo(
                "V6-12", SedeDelOwnerAlterada.CODIGO, ruta, zona.clase,
                "una sede APPEND-ONLY no se borra ni se renombra (letra "
                + mutacion.letra + ")",
            )
        anterior = nacimiento if ruta == SEDE_DEL_OWNER and nacimiento is not None else None
        if anterior is None:
            par = contenidos.get(ruta)
            anterior = par[0] if par else None
        par = contenidos.get(ruta)
        actual = par[1] if par else None
        if anterior is None or actual is None:
            return Hallazgo(
                "V6-12", SedeDelOwnerAlterada.CODIGO, ruta, zona.clase,
                "no se pudo contrastar la sede APPEND-ONLY contra su commit de "
                "NACIMIENTO. Sin ese contraste no se emite verde",
            )
        if actual.startswith(anterior):
            return None
        return Hallazgo(
            "V6-12", SedeDelOwnerAlterada.CODIGO, ruta, zona.clase,
            "el contenido publicado en el commit de NACIMIENTO ya no es un prefijo exacto "
            "del contenido actual: se ha alterado lo publicado, y confirmar no exime",
        )


def exigir_ancla_externa(declaracion, cid_interno):
    """`V6-17`: sin ancla que venga de FUERA, el veredicto no puede ser verde."""
    if not declaracion.ancla:
        raise SinAnclaExterna(
            "la declaración no trae ancla externa. Un digest calculado por el propio árbol "
            "siempre cuadra con el árbol, y no prueba su integridad: el veredicto queda "
            "INDETERMINADO",
        )
    if declaracion.ancla != cid_interno:
        return False
    return True


def digest_del_censo(zonas):
    """Digest del censo de zonas, para que la configuración externa pueda ANCLARLO."""
    cuerpo = "\n".join(
        zona.patron + "\t" + zona.clase + "\t" + str(zona.condicion)
        for zona in zonas
    )
    return digest_de_contenido(cuerpo)
