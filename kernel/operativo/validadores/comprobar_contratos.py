#!/usr/bin/env python3
"""comprobar_contratos — pruebas de conformidad ESTRUCTURALES, ejecutables hoy.

A diferencia de ads_lint (que valida forma), esto comprueba propiedades del contenido
que las secciones (a) y (b) y los contratos C1-C5 declaran obligatorias, y que NO
necesitan runtime para verificarse.

Cada comprobación corresponde a una prueba numerada. La salida dice, por prueba,
SUPERADA o FALLIDA, con el detalle de cada fallo.

Uso:
  python3 kernel/operativo/validadores/comprobar_contratos.py [--json] [--prueba T86]
"""
from __future__ import annotations

# ---------------------------------------------------------------------------
#  `G-03` · AISLAMIENTO DE ARRANQUE · lo PRIMERO que hace este punto
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-05, sobre esta zona. Con seis líneas de
#  veneno en un `sitecustomize.py` alcanzable desde `PYTHONPATH`:
#
#      $ cat veneno/sitecustomize.py
#        import hashlib; hashlib.sha256 = lambda *a, **k: _Falso()   # digest 0000…
#      $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/huella.py
#        0000000000000000                     ← la huella FORJADA sobre un árbol mutado
#      $ PYTHONPATH=veneno python3.12 kernel/operativo/validadores/comprobar_integridad.py
#        T150  SUPERADA · EXIT=0              ← VERDE sobre un árbol MUTADO
#
#  El prólogo `E-10` de abajo purga `sys.path` en su primera sentencia, y eso llega TARDE:
#  `site.py` importa `sitecustomize` mientras el intérprete arranca, antes de que la primera
#  línea de este módulo exista. Lo que cambia no es un módulo —`hashlib` es el bueno— sino
#  un atributo suyo, y el control del control de `E-10`, que mira la procedencia de `os`, no
#  lo ve. Con la guarda, este punto se reejecuta con `-I -S -E` y `sitecustomize` no llega a
#  importarse: medido en la tabla de los doce ataques de `T380`-`T399`.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      La misma disciplina que `E-10` sigue debajo y que `T330` comprueba: lo que protege
#      está fijado y es idéntico en todos los puntos —`T380` lo exige con su digest—, y lo
#      que se lee dice qué se midió en ESTA sede. Un recital común mentiría en la mitad de
#      las sedes; un mecanismo por sede derivaría, y el que derive de menos es el que nadie
#      mira.
#
#  DECISIÓN · la guarda va ANTES del prólogo `E-10`, y no lo sustituye
#      Alternativas: (a) sustituir `E-10` por la guarda; (b) dejar `E-10` y añadir la
#      guarda encima.
#      Se elige (b). Cierran cosas distintas: `E-10` retira del `sys.path` lo que mete el
#      lanzador —y sigue haciendo falta cuando el punto se IMPORTA, donde la guarda no
#      reejecuta—; `G-03` impide que `sitecustomize` llegue siquiera a ejecutarse. Quitar
#      `E-10` reabriría la contaminación de la ruta en el caso importado.
import os as _os_g03
import sys as _sys_g03

# LA GUARDA NO DEJA RASTRO EN EL ÁRBOL QUE JUZGA. Medido: al importar la guarda, Python
# escribía `validadores/__pycache__/aislamiento_de_arranque…pyc` en el árbol, y
# `comprobar_arranque.py` empezó a publicar «el proyecto arrastra `__pycache__`» sobre
# proyectos recién creados. Se desactiva la escritura de bytecode DURANTE la guarda y se
# devuelve al estado que tenía: lo que el punto importe después sigue cacheándose como
# siempre, y no se paga rendimiento por una comprobación que corre una vez.
_G03_BYTECODE = _sys_g03.dont_write_bytecode
_sys_g03.dont_write_bytecode = True
_G03_PROPIA = _os_g03.path.dirname(_os_g03.path.realpath(__file__))
_G03_SEDE = ""
_G03_RAIZ = _G03_PROPIA
while not _G03_SEDE:
    for _G03_CANDIDATA in (_G03_PROPIA,
                           _os_g03.path.join(_G03_RAIZ, "kernel", "operativo",
                                             "validadores")):
        if _os_g03.path.isfile(_os_g03.path.join(_G03_CANDIDATA,
                                                 "aislamiento_de_arranque.py")):
            _G03_SEDE = _G03_CANDIDATA
            break
    else:
        _G03_PADRE = _os_g03.path.dirname(_G03_RAIZ)
        if _G03_PADRE == _G03_RAIZ:
            _sys_g03.stderr.write(
                "[PROCEDENCIA_NO_FIABLE] no hay `aislamiento_de_arranque.py` ni junto a "
                "este punto ejecutable ni en el `kernel/operativo/validadores/` de ning\u00fan "
                "ancestro suyo: no se puede decidir si el arranque est\u00e1 aislado, y no se "
                "sigue\n")
            raise SystemExit(5)
        _G03_RAIZ = _G03_PADRE
_sys_g03.path.insert(0, _G03_SEDE)
import aislamiento_de_arranque as _aislamiento_g03                    # noqa: E402

AISLAMIENTO = _aislamiento_g03.exigir(__file__, __name__)
_sys_g03.dont_write_bytecode = _G03_BYTECODE

# `-I` deja FUERA de `sys.path` el directorio del guión —es lo que impide que un homónimo
# vecino se cuele— y los puntos que importan módulos hermanos lo necesitan. Se reintroduce
# por RUTA DERIVADA DE `__file__`, que no la escribe el lanzador.
if _G03_PROPIA not in _sys_g03.path:
    _sys_g03.path.insert(0, _G03_PROPIA)

# ---------------------------------------------------------------------------
#  `E-10` · PROCEDENCIA · la ruta de importación se PURGA ANTES de importar nada
# ---------------------------------------------------------------------------
#  HECHO REPRODUCIDO ANTES DE CORREGIR, el 2026-09-04, sobre `validadores/huella.py` —el
#  instrumento que produce el número que se publica como línea base— y con seis líneas de
#  veneno: un `hashlib.py` homónimo cuyo `sha256()` devuelve siempre el digest esperado.
#
#      $ echo "# CODIGO INYECTADO" >> mutado/kernel/operativo/validadores/ads_lint.py
#      $ cd mutado && python3.12 …/huella.py                     → 8b38fb4f4b07300c
#      $ python3.12 …/comprobar_integridad.py                    → T150 FALLIDA  EXIT=1
#      $ PYTHONPATH=veneno python3.12 …/huella.py                → bc59513f7182130a
#      $ PYTHONPATH=veneno python3.12 …/comprobar_integridad.py  → T150 SUPERADA EXIT=0
#
#  `T150` es la prueba que dice «la huella detecta su edición», y bajo veneno certificaba en
#  VERDE un árbol editado. La causa: la zona `validadores/` estaba ENTERA fuera del
#  inventario de `T306`, de modo que `E-10` —declarado «CERRADO POR INVENTARIO MECÁNICO»—
#  seguía vivo justo en el aparato que produce la evidencia de la certificación.
#
#  DECISIÓN · el MECANISMO se copia byte a byte; el recital, no
#      Alternativas: (a) importar la purga de un módulo común; (b) copiar el prólogo entero
#      —recital incluido— desde `ads_runtime.py`; (c) copiar el MECANISMO byte a byte y
#      escribir el recital de esta sede.
#      Se elige (c). Con (a) la guardia dependería de un `import`, que es exactamente lo que
#      está protegiendo: una guardia que necesita importar ya ha perdido. Con (b) el recital
#      mentiría, porque el hecho reproducido allí no es el de aquí. Con (c) `T330` exige
#      —y comprueba— que el MECANISMO sea IDÉNTICO byte a byte en todos los puntos
#      ejecutables del árbol (digest `aa219465a6dd6a04`, 1 869 bytes), mientras cada sede
#      dice qué se midió en ella. Lo que protege es el mecanismo; lo que se lee, el recital.
#
#  DECISIÓN · se retira lo que viene del LANZADOR, y no «todo lo que no reconozco»
#      Una lista blanca de directorios del intérprete se rompería en cada instalación
#      distinta y convertiría un fallo de entorno en un fallo del aparato. Lo que `E-10`
#      nombra es concreto: `PYTHONPATH` y el `cwd`. Se retiran ésos, se cuenta cuántos, y el
#      recuento queda en `RETIRADAS_DE_LA_RUTA`.
import sys as _sys
import os as _os

_RAIZ_DEL_APARATO = _os.path.dirname(_os.path.abspath(__file__))


def _entradas_del_lanzador():
    """Lo que el LANZADOR puede meter en la ruta de importación: `PYTHONPATH` y el `cwd`."""
    sospechosas = set()
    for entrada in (_os.environ.get("PYTHONPATH") or "").split(_os.pathsep):
        if entrada:
            sospechosas.add(_os.path.realpath(entrada))
    try:
        sospechosas.add(_os.path.realpath(_os.getcwd()))
    except OSError:
        # Un `cwd` borrado bajo los pies no es motivo para no purgar el resto.
        pass
    return sospechosas


def _purgar_la_ruta_de_importacion():
    """Retira de `sys.path` lo que venga del lanzador. Devuelve cuántas entradas retiró."""
    del_lanzador = _entradas_del_lanzador()
    propia = _os.path.realpath(_RAIZ_DEL_APARATO)
    conservadas, retiradas = [], []
    for entrada in _sys.path:
        try:
            real = _os.path.realpath(entrada or _os.getcwd())
        except OSError:
            conservadas.append(entrada)
            continue
        if real != propia and real in del_lanzador:
            retiradas.append(real)
        else:
            conservadas.append(entrada)
    _sys.path[:] = conservadas
    return retiradas


RETIRADAS_DE_LA_RUTA = _purgar_la_ruta_de_importacion()

# CONTROL DEL CONTROL de la purga: `os` se usa para poder purgar, así que si `os` mismo
# viniera del lanzador la purga no probaría nada. No hay forma honesta de seguir: se dice y
# se sale con el código de PROCEDENCIA.
if _os.path.realpath(_os.path.dirname(_os.__file__ or ".")) in _entradas_del_lanzador():
    _sys.stderr.write(
        "[PROCEDENCIA_NO_FIABLE] el módulo `os` procede de la ruta de importación del "
        "lanzador: este punto ejecutable no puede garantizar de dónde salen sus módulos y "
        "NO ejecuta\n")
    raise SystemExit(5)


import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))


def fijar_raiz(nueva):
    """Permite ejecutar las pruebas contra una COPIA del corpus.

    Lo usa `comprobar_negativos.py` para introducir una infracción deliberada en un
    directorio temporal y demostrar que la prueba falla. El corpus real nunca se toca.
    """
    global RAIZ
    RAIZ = os.path.abspath(nueva)

# Marcas comerciales que NO pueden aparecer como requisito en kernel ni packs (K0.8, C2).
# Expresiones regulares, no subcadenas: «llama» es un verbo corriente en castellano y
# «cómo llama el Owner a esto» no es una marca. Se exige la forma en que la marca aparece
# de verdad cuando alguien la usa como requisito.
MARCAS = [
    r"\bclaude\b", r"\banthropic\b", r"\bopenai\b", r"\bgpt-?[0-9]", r"\bchatgpt\b",
    r"\bcodex\b", r"\bgemini\b", r"\bcopilot\b", r"\bllama[ -][0-9]", r"\bllama\.cpp\b",
    r"\bmistral\b", r"\bcohere\b", r"\bollama\b", r"\bbedrock\b", r"\bvertex ai\b",
]
# Ficheros donde nombrar una marca es legítimo: hablan del adaptador o de la prohibición.
EXENTOS_MARCA = {
    # Habla del adaptador y de la prohibición: nombrar la marca es su materia.
    "kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md",
    # Contiene la INFRACCIÓN DELIBERADA con la que se demuestra que esta misma prueba
    # falla cuando debe fallar (mutación N92). Sin la marca dentro, el negativo no
    # existiría, y una prueba que sólo se ha visto pasar no está verificada.
    "kernel/operativo/validadores/comprobar_negativos.py",
}


class Resultado:
    def __init__(self, pid, nombre):
        self.id, self.nombre, self.fallos = pid, nombre, []

    @property
    def superada(self):
        return not self.fallos

    def fallo(self, msg):
        self.fallos.append(msg)


def cargar():
    lint = Lint(RAIZ, ["kernel/operativo", "packs"])
    lint.cargar_esquemas()
    lint.cargar_bloques()
    porTipo = {}
    for tipo, datos, ruta, linea in lint.bloques:
        porTipo.setdefault(tipo, []).append((datos, ruta, linea))
    return porTipo


def t86_autoridad_subconjunto(b):
    r = Resultado("T86", "Ningún rol veta lo que su capacidad no veta")
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    for datos, ruta, _ in b.get("rol", []):
        cap = caps.get(datos.get("capacidad"))
        if not cap:
            r.fallo(f"{datos.get('id')}: su capacidad '{datos.get('capacidad')}' no tiene ficha")
            continue
        veta_rol = datos.get("autoridad", {}).get("veta") or []
        veta_cap = cap.get("autoridad", {}).get("veta") or []
        if veta_rol and not veta_cap:
            r.fallo(f"{datos['id']}: veta {veta_rol} pero {cap['id']} no declara veto alguno")
        if datos.get("veto") and not veta_cap:
            r.fallo(f"{datos['id']}: declara contrato de veto y {cap['id']} no veta nada")
    return r


def t87_independencia_gana(b):
    r = Resultado("T87", "Ninguna composición permite combinar dos roles que ella declara independientes")
    for datos, ruta, _ in b.get("composicion", []):
        prohibidos = set()
        for indep in datos.get("independientes") or []:
            sujeto = indep.get("rol")
            for objeto in indep.get("de") or []:
                if isinstance(objeto, str) and re.fullmatch(r"([a-z0-9-]+:)?[A-Z]{3}/[a-z0-9-]+", objeto):
                    prohibidos.add(frozenset((sujeto, objeto)))
        for comb in datos.get("combinables") or []:
            roles = comb.get("roles") or []
            for i, a in enumerate(roles):
                for bb in roles[i + 1:]:
                    if frozenset((a, bb)) in prohibidos:
                        r.fallo(f"{datos['id']}: combina '{a}' con '{bb}', "
                                f"y la misma composición los declara independientes")
    return r


def t88_prompt_existe(b):
    r = Resultado("T88", "Todo rol apunta a un prompt operativo que existe")
    for datos, ruta, _ in b.get("rol", []):
        prompt = datos.get("prompt")
        if not prompt:
            r.fallo(f"{datos.get('id')}: sin prompt declarado")
            continue
        # el prompt puede vivir en su propio fichero, o como sección del contrato
        fichero = prompt.split("#")[0]
        ancla = prompt.split("#")[1] if "#" in prompt else None
        ruta_prompt = os.path.join(RAIZ, fichero)
        if not os.path.exists(ruta_prompt):
            r.fallo(f"{datos['id']}: el prompt declarado no existe → {fichero}")
            continue
        if ancla:
            with open(ruta_prompt, encoding="utf-8") as fh:
                cuerpo = fh.read().lower()
            if f"## {ancla.replace('-', ' ')}" not in cuerpo and f"## {ancla}" not in cuerpo:
                r.fallo(f"{datos['id']}: el prompt apunta a la sección '#{ancla}', que no existe en {fichero}")
    return r


# T01-T74 están definidas en las secciones (a) y (b) aprobadas: son referencias válidas
# aunque no existan como bloque ads:escenario en este corpus.
HEREDADAS = {f"T{n:02d}" for n in range(1, 75)}


def t89_reanudacion_con_prueba(b):
    r = Resultado("T89", "Toda prueba de reanudación cita un escenario que existe")
    ids = {d.get("id") for d, _, _ in b.get("escenario", [])} | HEREDADAS
    for datos, ruta, _ in b.get("metodo", []):
        texto = datos.get("prueba_de_reanudacion", "")
        citadas = set(re.findall(r"\bT\d{2,3}\b", texto))
        if not citadas:
            r.fallo(f"{datos.get('id')}: su prueba de reanudación no cita ningún escenario numerado")
            continue
        for t in citadas:
            if t not in ids:
                r.fallo(f"{datos['id']}: cita {t}, que no está declarada como ads:escenario "
                        f"ni pertenece a T01-T74 de las secciones aprobadas")
    return r


def t90_roles_coherentes(b):
    r = Resultado("T90", "Capacidades, roles y métodos se referencian mutuamente sin huérfanos")
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    roles = {d["id"]: d for d, _, _ in b.get("rol", [])}
    for cid, cap in caps.items():
        for rid in cap.get("roles", []):
            if rid not in roles:
                r.fallo(f"{cid}: declara el rol {rid}, que no tiene contrato")
            elif roles[rid].get("capacidad") != cid:
                r.fallo(f"{cid}: declara {rid}, pero ese rol dice pertenecer a {roles[rid].get('capacidad')}")
    for rid, rol in roles.items():
        cid = rol.get("capacidad")
        # Los roles de pack se ADJUNTAN a la capacidad al materializar (packs/00-QUE-ES-UN-PACK):
        # la capacidad del kernel no los conoce y no puede listarlos.
        if ":" in rid:
            continue
        if cid in caps and rid not in caps[cid].get("roles", []):
            r.fallo(f"{rid}: dice pertenecer a {cid}, que no lo lista entre sus roles")

    # A-15: ENC/Critica existía, se usaba y se probaba, y su capacidad no lo declaraba.
    # Era el único caso del corpus, y nada lo habría vuelto a detectar.
    metodos = {d["id"]: d for d, _, _ in b.get("metodo", [])}
    for cid, cap in caps.items():
        for mid in cap.get("metodos", []):
            if mid not in metodos:
                r.fallo(f"{cid}: declara el método {mid}, que no tiene contrato")
            elif metodos[mid].get("capacidad") != cid:
                r.fallo(f"{cid}: declara {mid}, que dice pertenecer a "
                        f"{metodos[mid].get('capacidad')}")
    for mid, met in metodos.items():
        cid = met.get("capacidad")
        if ":" in mid:
            continue
        if cid in caps and mid not in caps[cid].get("metodos", []):
            r.fallo(f"{mid}: dice pertenecer a {cid}, que no lo lista entre sus métodos. "
                    f"La ficha de la capacidad es la fuente única: un método que no está "
                    f"en ella no lo encuentra nadie")
    return r


def t91_metodos_con_gate_y_pasos(b):
    r = Resultado("T91", "Todo paso de todo método declara cuándo termina")
    for datos, ruta, _ in b.get("metodo", []):
        for paso in datos.get("pasos", []):
            if not paso.get("termina_cuando"):
                r.fallo(f"{datos.get('id')} paso {paso.get('n')}: sin `termina_cuando`")
            if paso.get("hace", "").strip().lower().startswith(("valorar si", "decidir si conviene")):
                r.fallo(f"{datos.get('id')} paso {paso.get('n')}: el paso delega el criterio en vez de escribirlo")
    return r


def t92_sin_marca(_b):
    r = Resultado("T92", "Ni un contrato, ni un esquema, ni un validador exige una marca")
    for ambito in ("kernel/operativo", "packs"):
        for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, ambito)):
            dirnames[:] = [d for d in dirnames if not d.startswith("legacy-") and d != "__pycache__"]
            for nombre in filenames:
                if not nombre.endswith((".md", ".yaml", ".yml", ".py")):
                    continue
                ruta = os.path.join(dirpath, nombre)
                rel = os.path.relpath(ruta, RAIZ)
                if rel in EXENTOS_MARCA:
                    continue
                with open(ruta, encoding="utf-8") as fh:
                    bajo = fh.read().lower()
                for patron in MARCAS:
                    hallado = re.search(patron, bajo)
                    if hallado:
                        r.fallo(f"{rel}: nombra «{hallado.group(0)}»; el contrato canónico es neutral de proveedor")
    return r


def t134_sin_documentos_para_nadie(b):
    """Un documento que ningún otro enlaza y cuyos bloques nadie cita existe para nadie.

    Es el hallazgo que la revisión adversarial busca bajo el nombre de
    «autorreferencia sin producto», y aquí queda comprobado de forma permanente.
    """
    r = Resultado("T134", "Ningún documento del corpus existe para nadie")
    corpus = {}
    for ambito in ("kernel/operativo", "packs"):
        for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, ambito)):
            dirnames[:] = [d for d in dirnames
                           if d not in ("__pycache__",) and not d.startswith("legacy-")]
            for nombre in filenames:
                if nombre.endswith((".md", ".py", ".yaml")):
                    ruta = os.path.join(dirpath, nombre)
                    with open(ruta, encoding="utf-8") as fh:
                        corpus[os.path.abspath(ruta)] = fh.read()

    ids_por_fichero = {}
    for _, datos, ruta, _ in [(t, d, f, l) for t, d, f, l in
                              [(tt, dd, ff, ll) for tt in b for dd, ff, ll in b[tt]]]:
        ids_por_fichero.setdefault(os.path.abspath(ruta), []).append(datos.get("id"))

    for ruta, _ in corpus.items():
        if not ruta.endswith(".md"):
            continue
        base = os.path.basename(ruta)
        otros = {k: v for k, v in corpus.items() if k != ruta}
        entrante = any(base in txt for txt in otros.values())
        citado = any(i and any(i in txt for txt in otros.values())
                     for i in ids_por_fichero.get(ruta, []))
        if not entrante and not citado:
            r.fallo(f"{os.path.relpath(ruta, RAIZ)}: nadie lo enlaza y nadie cita sus bloques")
    return r


def t135_composicion_respeta_el_contrato(b):
    """Ninguna composición combina dos roles que el CONTRATO de uno declara independientes.

    T87 comprueba la coherencia interna de cada composición. Esto comprueba algo distinto
    y más fuerte: que ninguna composición rebaje lo que el contrato del rol exige.
    """
    r = Resultado("T135", "Ninguna composición rebaja la independencia que exige un contrato")
    roles = {d["id"]: d for d, _, _ in b.get("rol", [])}
    for datos, ruta, _ in b.get("composicion", []):
        for comb in datos.get("combinables") or []:
            pareja = comb.get("roles") or []
            for i, a in enumerate(pareja):
                for bb in pareja[i + 1:]:
                    for uno, otro in ((a, bb), (bb, a)):
                        rol = roles.get(uno)
                        if not rol:
                            continue
                        ind = rol.get("independencia") or {}
                        if not ind.get("requiere_independencia"):
                            continue
                        if otro in (ind.get("de") or []):
                            r.fallo(f"{datos['id']}: combina '{uno}' con '{otro}', y el "
                                    f"contrato de {uno} exige independencia de él")
    return r


# ---------------------------------------------------------------------------
# Pruebas añadidas en la corrección post-auditoría. Cada una nombra su hallazgo.
# ---------------------------------------------------------------------------

CODIGO_CAP = re.compile(r"\b([A-Z]{3})\b")


def t136_vetos_no_se_arbitran(b):
    """A-06 · a.5: dos vetos incompatibles NO se arbitran entre las capacidades.

    Escalan al Owner con ambas materias. La ÚNICA excepción es un veto declarado
    no levantable por regla dura del kernel (G27). Por tanto:
      · un veto LEVANTABLE nunca puede aparecer como el que prevalece;
      · toda cláusula de colisión debe declarar el escalado al Owner.
    """
    r = Resultado("T136", "Ningún veto arbitra a otro veto levantable: ambos detienen y escalan")
    vetos = {d["id"]: d for d, _, _ in b.get("veto", [])}
    por_capacidad = {d.get("capacidad"): d for d in vetos.values()}
    for vid, datos in vetos.items():
        colision = (datos.get("colision") or "")
        # (a) nadie declara que prevalece un veto levantable
        for m in re.finditer(r"(?i)\bprevalece[nr]?\s+(?:el\s+veto\s+de\s+)?([A-Z]{3})\b", colision):
            otro = por_capacidad.get(m.group(1))
            if otro is None:
                continue
            if otro.get("levantable") == "si":
                r.fallo(f"{vid}: declara que prevalece {m.group(1)}, cuyo veto es LEVANTABLE. "
                        f"a.5 sólo admite prevalencia de un veto no levantable por regla dura")
        # (b) el propio veto, si es levantable, no puede reclamar prevalencia para sí
        if datos.get("levantable") == "si":
            propio = datos.get("capacidad", "")
            if re.search(r"(?i)prevalece\s+" + re.escape(propio) + r"\b", colision):
                r.fallo(f"{vid}: es levantable y se declara prevaleciente sobre otro veto")
        # (c) toda colisión declara el escalado al Owner
        if not re.search(r"(?i)escala\w*\s+al\s+owner", colision):
            r.fallo(f"{vid}: su cláusula de colisión no declara el escalado al Owner (a.5)")
    return r


def t137_dsp_no_cancela_por_contenido(b):
    """A-23 · b.7: DSP NUNCA posee por sí mismo la autoridad semántica para cancelar."""
    r = Resultado("T137", "DSP no declara autoridad semántica sobre ninguna cancelación")
    for datos, ruta, _ in b.get("rol", []) + b.get("capacidad", []):
        cap = datos.get("capacidad") or datos.get("id")
        if cap != "DSP":
            continue
        aut = datos.get("autoridad", {}) or {}
        decide = list(aut.get("decide") or []) + list(aut.get("decide_sola") or [])
        for item in decide:
            if re.search(r"(?i)cancela", str(item)):
                r.fallo(f"{datos.get('id')}: DECIDE «{str(item)[:70]}». "
                        f"b.7: la cancelación se propone y se ejecuta, nunca se decide desde DSP")
    return r


VARIABLES_NOVEDAD = ("superficie_construida", "memoria_vigente", "dir_sustituye",
                     "patron_cubre", "premium_o_nuevo")
EJES_VISUALES = ("personalidad", "intencion", "jerarquia", "sistema", "actualidad",
                 "respuesta", "acabado", "fidelidad", "alma")


def _evaluar_condicion(expr, entorno):
    """Evalúa una condición booleana SIN ejecutar código arbitrario.

    Sólo se admiten nombres de variable declarados, `and`, `or`, `not` y paréntesis. Una
    condición que no encaje en eso no es comprobable, y por tanto no es una condición.
    """
    import ast

    def visitar(nodo):
        if isinstance(nodo, ast.Expression):
            return visitar(nodo.body)
        if isinstance(nodo, ast.BoolOp):
            valores = [visitar(v) for v in nodo.values]
            return all(valores) if isinstance(nodo.op, ast.And) else any(valores)
        if isinstance(nodo, ast.UnaryOp) and isinstance(nodo.op, ast.Not):
            return not visitar(nodo.operand)
        if isinstance(nodo, ast.Name):
            if nodo.id not in entorno:
                raise ValueError(f"variable no declarada: {nodo.id}")
            return entorno[nodo.id]
        if isinstance(nodo, ast.Constant) and isinstance(nodo.value, bool):
            return nodo.value
        raise ValueError(f"expresión no admitida: {ast.dump(nodo)[:60]}")

    return visitar(ast.parse(expr, mode="eval"))


def t138_escala_total_y_alcanzable(b):
    """A-07 · la escala de novedad cubre todos los casos y ningún nivel es inalcanzable.

    La versión anterior preguntaba en N4 «¿no existe memoria de diseño?», que es cierto
    también para un producto construido sin dirección escrita. Como N4 se evaluaba antes,
    N3 no se alcanzaba nunca y un brownfield recibía el método de fundación.
    """
    r = Resultado("T138", "La escala de novedad es total y sus cinco niveles son alcanzables")
    niveles = sorted((d for d, _, _ in b.get("nivel-novedad", [])),
                     key=lambda d: d.get("orden", 0))
    if len(niveles) != 5:
        r.fallo(f"se declaran {len(niveles)} niveles y la escala tiene cinco")
        return r
    ordenes = [n["orden"] for n in niveles]
    if len(set(ordenes)) != len(ordenes):
        r.fallo(f"dos niveles comparten orden de evaluación: {ordenes}")

    alcanzados, sin_nivel = {}, []
    for combo in range(2 ** len(VARIABLES_NOVEDAD)):
        entorno = {v: bool(combo >> i & 1) for i, v in enumerate(VARIABLES_NOVEDAD)}
        elegido = None
        for nivel in niveles:
            try:
                cierto = _evaluar_condicion(nivel["condicion_formal"], entorno)
            except ValueError as exc:
                r.fallo(f"{nivel['id']}: condición no comprobable — {exc}")
                return r
            if cierto:
                elegido = nivel["id"]
                break
        if elegido is None:
            sin_nivel.append(entorno)
        else:
            alcanzados.setdefault(elegido, []).append(entorno)

    if sin_nivel:
        muestra = ", ".join(k for k, v in sin_nivel[0].items() if v) or "(todas falsas)"
        r.fallo(f"{len(sin_nivel)} combinaciones no producen NINGÚN nivel. "
                f"Ejemplo: {muestra}. La escala no es total")
    for nivel in niveles:
        if nivel["id"] not in alcanzados:
            r.fallo(f"{nivel['id']} ({nivel['nombre']}) es INALCANZABLE: ninguna de las "
                    f"{2 ** len(VARIABLES_NOVEDAD)} combinaciones lo produce. Su método "
                    f"{nivel['metodo']} no se elige nunca")
    return r


def t139_ningun_nivel_omite_un_gate(b):
    """A-08 · ningún nivel de novedad omite un gate obligatorio de Diseño."""
    r = Resultado("T139", "Ningún nivel de novedad omite un gate: lo que cambia es la evidencia reutilizable")
    niveles = {d["id"]: d for d, _, _ in b.get("nivel-novedad", [])}
    if not niveles:
        r.fallo("no hay ningún bloque ads:nivel-novedad declarado")
        return r
    for nid, nivel in sorted(niveles.items()):
        for gate in ("gate:usabilidad", "gate:excelencia-visual"):
            if gate not in (nivel.get("gates_obligatorios") or []):
                r.fallo(f"{nid}: no declara {gate} como obligatorio. Un nivel pequeño "
                        f"explora menos; no verifica menos")
        reut = set(nivel.get("ejes_reutilizables") or [])
        nunca = set(nivel.get("ejes_nunca_reutilizables") or [])
        if reut & nunca:
            r.fallo(f"{nid}: {sorted(reut & nunca)} está a la vez en reutilizables y en "
                    f"nunca reutilizables")
        if reut | nunca != set(EJES_VISUALES):
            faltan = set(EJES_VISUALES) - (reut | nunca)
            sobran = (reut | nunca) - set(EJES_VISUALES)
            if faltan:
                r.fallo(f"{nid}: los ejes {sorted(faltan)} no se declaran ni reutilizables "
                        f"ni propios: quedarían sin régimen")
            if sobran:
                r.fallo(f"{nid}: declara ejes que la rúbrica no tiene: {sorted(sobran)}")
        for imprescindible in ("acabado", "fidelidad"):
            if imprescindible in reut:
                r.fallo(f"{nid}: declara `{imprescindible}` reutilizable, y depende de esta "
                        f"aplicación concreta: nunca se hereda de un patrón")
        if reut and not (nivel.get("evidencia_de_vigencia") or []):
            r.fallo(f"{nid}: reutiliza ejes y no declara qué evidencia demuestra que el "
                    f"patrón previo sigue siendo aplicable")
        # las estaciones de los dos gates son la 8 y la 9 del ciclo de calidad
        estaciones = set(nivel.get("estaciones") or [])
        for est, nombre in ((8, "validación de uso · gate:usabilidad"),
                            (9, "validación visual · gate:excelencia-visual")):
            if est not in estaciones:
                r.fallo(f"{nid}: su lista de estaciones omite la {est} ({nombre}), y declara "
                        f"ese gate obligatorio")

    # la tabla de 04-CICLO se DERIVA de estos bloques: se comprueba que coincide
    ruta = os.path.join(RAIZ, "kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md")
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as fh:
            texto = fh.read()
        for nid, nivel in sorted(niveles.items()):
            m = re.search(rf"^{nid}\s+(.+)$", texto, re.M)
            if not m:
                r.fallo(f"04-CICLO-DE-CALIDAD.md no declara las estaciones de {nid}")
                continue
            linea = m.group(1)
            if "las trece" in linea:
                declaradas = set(range(1, 14))
            else:
                declaradas = {int(x) for x in re.findall(r"\b(\d+)\b", linea.split("(")[0])}
            if declaradas != set(nivel.get("estaciones") or []):
                r.fallo(f"{nid}: 04-CICLO declara {sorted(declaradas)} y su bloque canónico "
                        f"declara {sorted(nivel.get('estaciones') or [])}. Dos fuentes para "
                        f"la misma verdad")
    return r


def t144_usabilidad_tiene_portador_en_con(b):
    """A-13 · gate:usabilidad dice aplicarse a las capas de CON, y nada lo vinculaba."""
    r = Resultado("T144", "El gate de usabilidad tiene portador computable en Construcción")
    gates = {d["id"]: d for d, _, _ in b.get("gate", [])}
    usab = gates.get("gate:usabilidad")
    impl = gates.get("gate:implementacion-completa")
    if not usab or not impl:
        r.fallo("falta gate:usabilidad o gate:implementacion-completa")
        return r
    if "CON" not in (usab.get("aplica_a") or ""):
        return r      # si deja de aplicarse a CON, no hay nada que vincular
    ids = {c.get("id") for c in impl.get("comprobaciones") or []}
    textos = " ".join(str(c.get("comprueba", "")) + str(c.get("como", ""))
                      for c in impl.get("comprobaciones") or [])
    if "superficie-usable" not in ids:
        r.fallo("gate:implementacion-completa no comprueba la usabilidad de lo construido, "
                "y gate:usabilidad declara aplicarse a las capas de CON")
    if "gate:usabilidad" not in textos:
        r.fallo("la comprobación de superficie usable no cita gate:usabilidad: el vínculo "
                "no es rastreable")
    if "validacion-de-uso" not in textos:
        r.fallo("no se declara QUIÉN juzga la evidencia de usabilidad de lo construido: "
                "sin eso, la juzga quien la produjo")
    return r


def t140_obligaciones_y_cierre(b):
    """A-09 · el aparato central de (b) tiene portador operativo.

    Antes de esto, las palabras `obligación_satisfecha`, `obligación_retirada` y
    `obligación_huérfana` no aparecían una sola vez en el corpus operativo, y no existía
    ningún gate de cierre: cerrar todos los paquetes de un item cerraba un item cuyo
    resultado nunca existió, y nada lo impedía.
    """
    r = Resultado("T140", "Las obligaciones del proceso existen y el cierre las comprueba")
    procesos = {d["id"]: d for d, _, _ in b.get("proceso", [])}
    if len(procesos) != 10:
        r.fallo(f"se declaran {len(procesos)} procesos y b.16 deriva diez rutas")
    for pid, proc in sorted(procesos.items()):
        obligs = proc.get("obligatorias") or []
        if not obligs:
            r.fallo(f"{pid}: sin obligaciones. Un proceso sin obligación no puede cerrar mal")
        vistos = set()
        for o in obligs:
            oid = o.get("id")
            if oid in vistos:
                r.fallo(f"{pid}: dos obligaciones con el mismo id '{oid}'")
            vistos.add(oid)
            autoridad = str(o.get("autoridad_de_retirada", ""))
            if re.search(r"\bDSP\b", autoridad):
                r.fallo(f"{pid}/{oid}: declara a DSP como autoridad de retirada. Retirar es "
                        f"autoridad semántica, y b.5 y b.9 dicen que DSP no la tiene")
        for c in proc.get("condicionales") or []:
            cond = str(c.get("condicion", "")).strip().lower()
            if cond in ("si aplica", "si procede", "cuando corresponda", ""):
                r.fallo(f"{pid}/{c.get('capacidad')}: condición no comprobable «{cond}»")

    gates = {d["id"]: d for d, _, _ in b.get("gate", [])}
    cierre = gates.get("gate:cierre-de-item")
    if not cierre:
        r.fallo("no existe gate:cierre-de-item: las cinco condiciones de b.10 no las "
                "comprueba nadie")
        return r
    ids = {c.get("id") for c in cierre.get("comprobaciones") or []}
    for exigida in ("terminacion", "obligaciones-resueltas", "vigencia", "integracion",
                    "aprendizaje"):
        if exigida not in ids:
            r.fallo(f"gate:cierre-de-item no comprueba '{exigida}', que es una de las cinco "
                    f"condiciones de cierre de b.10")
    texto = json.dumps(cierre, ensure_ascii=False).lower()
    for concepto in ("huérfana", "retirada", "satisfecha", "invalidada"):
        if concepto not in texto:
            r.fallo(f"gate:cierre-de-item no menciona '{concepto}': el vocabulario de b.3 "
                    f"tiene que ser el suyo")
    plantilla = os.path.join(RAIZ, "kernel/operativo/plantillas/CIERRE.md")
    if not os.path.exists(plantilla):
        r.fallo("no existe la plantilla de informe de cierre que separa satisfechas de retiradas")
    else:
        with open(plantilla, encoding="utf-8") as fh:
            cuerpo = fh.read().upper()
        for cifra in ("OBLIGACIONES SATISFECHAS", "OBLIGACIONES RETIRADAS"):
            if cifra not in cuerpo:
                r.fallo(f"la plantilla de cierre no reporta '{cifra}' por separado")
    return r


# Los umbrales YA APROBADOS. Esta prueba no los fija: comprueba que el corpus no los
# reinventa ni los deja a la memoria del agente.
FRENOS = {
    "devolucion": ("2", "a.7 · FRENO 1"),
    "ciclo": ("3", "a.7 · FRENO 2"),
    "racha": ("2", "a.7 · FRENO 3"),
    "recomposici": ("3", "b.9 · MAX_RECOMPOSICIONES_SIN_AVANCE"),
}


def t141_frenos_con_ejecutor(b):
    """A-10 · los frenos de a.7 y b.9 tienen quien los cuente, los detenga y los escale."""
    r = Resultado("T141", "Los frenos tienen ejecutor operativo, no sólo prosa")
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    roles = {d["id"]: d for d, _, _ in b.get("rol", [])}
    metodos = {d["id"]: d for d, _, _ in b.get("metodo", [])}
    dsp = caps.get("DSP")
    if not dsp:
        r.fallo("no existe la ficha de DSP")
        return r
    if "DSP/supervision" not in (dsp.get("roles") or []):
        r.fallo("DSP no declara el rol que ejecuta su cuarta función, la Supervisión de a.3")
    if "DSP/Supervision" not in (dsp.get("metodos") or []):
        r.fallo("DSP no declara el método de supervisión: los frenos quedarían en prosa")

    metodo = metodos.get("DSP/Supervision")
    if not metodo:
        r.fallo("no existe el método DSP/Supervision")
    else:
        cuerpo = json.dumps(metodo, ensure_ascii=False).lower()
        for freno in FRENOS:
            if freno not in cuerpo:
                r.fallo(f"DSP/Supervision no cuenta el freno de {freno}")
        for paso in metodo.get("pasos", []):
            if not paso.get("termina_cuando"):
                r.fallo(f"DSP/Supervision paso {paso.get('n')}: sin condición de salida")

    rol = roles.get("DSP/supervision")
    if not rol:
        r.fallo("no existe el contrato del rol DSP/supervision")
    else:
        ind = rol.get("independencia") or {}
        if not ind.get("requiere_independencia"):
            r.fallo("DSP/supervision no exige independencia de DSP/enrutamiento: quien "
                    "recompone contaría sus propias recomposiciones")
        elif "DSP/enrutamiento" not in (ind.get("de_quien") or []):
            r.fallo("DSP/supervision exige independencia pero no de DSP/enrutamiento")
        limites = " ".join(rol.get("limites") or []).lower()
        if "prioridad" not in limites:
            r.fallo("DSP/supervision no declara que NO toca la prioridad: b.12 lo prohíbe "
                    "expresamente y es el error más fácil ante una inanición")

    gate = {d["id"]: d for d, _, _ in b.get("gate", [])}.get("gate:despacho-coherente")
    if not gate:
        r.fallo("no existe gate:despacho-coherente")
        return r
    ids = {c.get("id") for c in gate.get("comprobaciones") or []}
    for exigida in ("frenos-evaluados", "freno-disparado-con-dos-posturas",
                    "inanicion-visible-sin-tocar-prioridad"):
        if exigida not in ids:
            r.fallo(f"gate:despacho-coherente no comprueba '{exigida}': un despacho podría "
                    f"cerrar su gate sin haber evaluado un solo freno")

    # los umbrales son los aprobados: no se inventan números nuevos
    ruta = os.path.join(RAIZ, "kernel/operativo/capacidades/DSP/prompts/supervision.md")
    if os.path.exists(ruta):
        with open(ruta, encoding="utf-8") as fh:
            prompt = fh.read()
        for freno, (valor, fuente) in FRENOS.items():
            if not re.search(rf"(?i){freno}[^=≥\n]*[=≥]\s*{valor}\b", prompt):
                r.fallo(f"el prompt de supervisión no fija el umbral de {freno} en {valor} "
                        f"({fuente}): un umbral que el agente recuerda de memoria se ajusta solo")
    return r


# Los once estados de paquete de b.2. El corpus no puede usar un vocabulario paralelo.
ESTADOS_B2 = {"propuesto", "listo", "en-curso", "esperando-capacidad",
              "esperando-dependencia", "esperando-owner", "esperando-externo",
              "bloqueado", "devuelto", "cerrado", "cancelado"}


def t142_encuadre_expresa_sus_estados(_b):
    """A-11 · el encuadre puede declarar todo estado que sus propios documentos le exigen.

    `esperando-owner` lo exigían 04-INCERTIDUMBRE y el campo `bloqueo` de ENC/Escucha, y el
    enum del esquema no podía expresarlo. A la vez tenía `aparcado-por-owner`, que b.2
    excluye expresamente de los estados de paquete.
    """
    import yaml as _yaml
    r = Resultado("T142", "El encuadre expresa todos los estados que sus métodos le exigen")
    ruta = os.path.join(RAIZ, "kernel/operativo/esquemas/encuadre.yaml")
    if not os.path.exists(ruta):
        r.fallo("no existe esquemas/encuadre.yaml")
        return r
    with open(ruta, encoding="utf-8") as fh:
        esquema = _yaml.safe_load(fh)
    campos = esquema.get("campos") or {}
    if "estado_paquete" not in (esquema.get("obligatorios") or []):
        r.fallo("el encuadre no declara `estado_paquete`: sin él no puede expresar los "
                "estados de b.2 que sus propios documentos le exigen")
        return r
    valores = set((campos.get("estado_paquete") or {}).get("valores") or [])
    faltan = ESTADOS_B2 - valores
    if faltan:
        r.fallo(f"`estado_paquete` no admite {sorted(faltan)}, que son estados de b.2")
    sobran = valores - ESTADOS_B2
    if sobran:
        r.fallo(f"`estado_paquete` admite {sorted(sobran)}, que no son estados de b.2: "
                f"un vocabulario paralelo sin reconciliar")
    madurez = set((campos.get("estado") or {}).get("valores") or [])
    for prohibido in ("aparcado", "aparcado-por-owner"):
        if prohibido in madurez or prohibido in valores:
            r.fallo(f"'{prohibido}' figura como estado. b.2 es explícita: aparcado NO es un "
                    f"estado de paquete, es una bandera global del item")

    # todo estado citado por los documentos de ENC tiene que ser declarable
    for rel in ("kernel/operativo/entrada/04-INCERTIDUMBRE-Y-CONFIRMACION.md",
                "kernel/operativo/capacidades/ENC/metodos/Escucha.md"):
        f = os.path.join(RAIZ, rel)
        if not os.path.exists(f):
            continue
        with open(f, encoding="utf-8") as fh:
            texto = fh.read()
        for estado in ESTADOS_B2:
            if re.search(rf"`?{re.escape(estado)}`?", texto) and estado not in valores:
                r.fallo(f"{rel} exige el estado `{estado}` y el esquema no lo admite")
    return r


def t145_critica_de_encuadre_no_se_evapora(b):
    """A-14 · la crítica obligatoria no desaparece porque la conversación baje el grado."""
    import yaml as _yaml
    r = Resultado("T145", "La crítica de encuadre exigible no se evapora al bajar la incertidumbre")
    ruta = os.path.join(RAIZ, "kernel/operativo/esquemas/encuadre.yaml")
    with open(ruta, encoding="utf-8") as fh:
        esquema = _yaml.safe_load(fh)
    inc = ((esquema.get("campos") or {}).get("incertidumbre") or {})
    if "grado_inicial" not in (inc.get("obligatorios") or []):
        r.fallo("el encuadre no persiste `grado_inicial`: sin él, una incertidumbre alta que "
                "baja tras conversar hace desaparecer la crítica que ya era obligatoria")

    gate = {d["id"]: d for d, _, _ in b.get("gate", [])}.get("gate:encuadre-listo")
    if not gate:
        r.fallo("no existe gate:encuadre-listo")
        return r
    critica = next((c for c in gate.get("comprobaciones") or []
                    if c.get("id") == "critica-cuando-corresponde"), None)
    if not critica:
        r.fallo("gate:encuadre-listo no comprueba la crítica de encuadre")
        return r
    texto = (str(critica.get("comprueba", "")) + " " + str(critica.get("como", ""))).lower()
    if "grado_inicial" not in texto.replace("_inicial", "_INICIAL").lower() and \
            "inicial" not in texto:
        r.fallo("la comprobación se apoya en el grado FINAL: un encuadre que empieza alto y "
                "baja tras conversar pasaría sin el dictamen que su composición exigía")
    if "materializ" not in texto:
        r.fallo("la comprobación no mira si la composición materializó ENC/critica-de-encuadre: "
                "un rol materializado cuyo dictamen no se exige es un rol decorativo")

    comp = next((d for d, _, _ in b.get("composicion", [])
                 if d.get("id") == "composicion:enc-alta-incertidumbre"), None)
    if comp and "no se retira" not in (comp.get("reduccion") or "").lower():
        r.fallo("composicion:enc-alta-incertidumbre no declara que la crítica NO se retira "
                "al bajar el grado")
    return r


VACIAS = set("""el la los las un una unos unas de del al a y o u que se su sus lo en con
por para sin sobre entre no ni es son ser esta este esa ese cuando donde como cual cada
todo toda todos todas mas menos ya si segun tras hasta desde le les nos me te""".split())


def _palabras(texto):
    import unicodedata
    t = unicodedata.normalize("NFD", str(texto).lower())
    t = "".join(c for c in t if unicodedata.category(c) != "Mn")
    return {w for w in re.findall(r"[a-z0-9-]{3,}", t) if w not in VACIAS}


def _parecido(a, b_):
    if not a or not b_:
        return 0.0
    return len(a & b_) / len(a | b_)


def t146_autoridad_de_decision(b):
    """A-18 · lo que T86 no comprobaba: la autoridad de DECISIÓN de un rol.

    C1 fija tres reglas y sólo la del veto estaba implementada. Ésta cubre las otras dos
    en lo que es mecánicamente comprobable:

      · un rol NO PUEDE decidir lo que su capacidad ESCALA
      · un rol NO PUEDE decidir la materia declarada por OTRA capacidad
      · un rol que decide algo pertenece a una capacidad que decide algo

    LO QUE NO COMPRUEBA, y se dice para no repetir el defecto de T131: la contención
    SEMÁNTICA fina. Que `DIS/critica-visual` decida «el nivel de cada eje de la rúbrica» y
    que `DIS` declare «qué dirección visual se elige» son compatibles sin compartir una
    palabra, y ninguna medida de texto puede decidir eso. Esa lectura es de la revisión
    humana; aquí se atrapan las tres formas groseras.
    """
    r = Resultado("T146", "Ningún rol decide lo que su capacidad escala ni lo que decide otra")
    caps = {d["id"]: d for d, _, _ in b.get("capacidad", [])}
    materia_ajena = {}
    for cid, cap in caps.items():
        for item in (cap.get("autoridad", {}).get("decide_sola") or []):
            materia_ajena.setdefault(cid, []).append(_palabras(item))

    for datos, _ruta, _l in b.get("rol", []):
        cid = datos.get("capacidad")
        cap = caps.get(cid)
        if not cap:
            continue
        decide = datos.get("autoridad", {}).get("decide") or []
        if decide and not (cap.get("autoridad", {}).get("decide_sola") or []):
            r.fallo(f"{datos['id']}: decide {len(decide)} cosas y {cid} no declara "
                    f"`decide_sola`: un rol no puede decidir donde su capacidad no decide")
        escala = [_palabras(x) for x in (cap.get("autoridad", {}).get("escala") or [])]
        for item in decide:
            w = _palabras(item)
            for e in escala:
                if _parecido(w, e) >= 0.6:
                    r.fallo(f"{datos['id']}: DECIDE «{str(item)[:60]}», y {cid} declara eso "
                            f"mismo en `escala`. C1: un rol no decide lo que su capacidad escala")
                    break
            for otro_id, materias in materia_ajena.items():
                if otro_id == cid:
                    continue
                for m in materias:
                    if _parecido(w, m) >= 0.6:
                        r.fallo(f"{datos['id']}: DECIDE «{str(item)[:60]}», que es materia "
                                f"declarada por {otro_id}. Autoridad de otra capacidad")
                        break
    return r


# ===========================================================================
#  LOS HALLAZGOS EXTERNOS CON PROPIETARIO Y FASE `F6` — `11-ARQ` §19 · `F6-H`
# ===========================================================================
#  Cada una de estas pruebas cierra UNA fila de la tabla «Lo que esta fase NO puede
#  corregir». No comprueban que el texto esté escrito: comprueban la PROPIEDAD, de modo
#  que reintroducir el defecto las pone en rojo. Los sabotajes están en
#  `comprobar_negativos.py`, y se ejecutan sobre una copia del árbol.

# Las CINCO entregas que `11-ARQ` §8.0 declara, en su bloque «`SIS` y `PLT`, dicho aparte».
# Viajan como DATO porque `11-ARQ` NO viaja al proyecto instalado —la misma decisión que se
# tomó con la tabla de §18—, y la prueba las CONTRASTA contra el documento cuando existe.
ENTREGAS_DE_8_0 = [("SIS", "PLT"), ("SIS", "CON"), ("SIS", "VER"),
                   ("CON", "ENT"), ("ENT", "VER")]
SEDE_DE_8_0 = "docs/evolucion/11-ARQUITECTURA-INTEGRADA.md"


def t240_capacidad_tipada_sin_metodos(b):
    """`F-02` y la mitad de `F6` de `F-01`."""
    r = Resultado("T240", "Ninguna tabla de participación nombra un método donde va una capacidad")
    quince = {d.get("id") for d, _r, _l in b.get("capacidad", [])}
    esquema = os.path.join(RAIZ, "kernel/operativo/esquemas/proceso.yaml")
    with open(esquema, encoding="utf-8") as fh:
        import yaml as _y
        decl = _y.safe_load(fh)
    campos = ((decl.get("campos") or {}).get("obligatorias") or {}).get("campos") or {}
    spec = campos.get("capacidad_productora") or {}
    if spec.get("tipo") != "ref" or spec.get("ref_a") != "capacidad":
        r.fallo("`proceso.yaml` no tipa `capacidad_productora` como `ref_a: capacidad`: "
                "sin tipar, nada impide que vuelva a entrar un método donde va una "
                "capacidad (`11-ARQ` §19 `F-02` punto 1)")
    # `F-02` punto 5, en su forma MOVIDA: `OWNER` está PROHIBIDO en el campo de capacidad,
    # tiene su propio campo de autoridad, y el esquema exige EXACTAMENTE UNO de los dos.
    obligatorias = (decl.get("campos") or {}).get("obligatorias") or {}
    if "OWNER" not in (spec.get("prohibidos") or []):
        r.fallo("`proceso.yaml` no PROHÍBE `OWNER` en `capacidad_productora`: tolerarlo "
                "junto a su campo hermano deja la duplicación que `F-02` punto 5 retira")
    if "capacidad_productora" in (obligatorias.get("obligatorios") or []):
        r.fallo("`proceso.yaml` mantiene `capacidad_productora` como obligatoria "
                "INCONDICIONAL, lo que obliga a conservar `OWNER` en el campo de capacidad "
                "(`F-02` punto 5)")
    alternativos = [set(g) for g in (obligatorias.get("obligatorios_alternativos") or [])]
    if {"capacidad_productora", "autoridad_productora"} not in alternativos:
        r.fallo("`proceso.yaml` no declara `capacidad_productora` y `autoridad_productora` "
                "como obligatorias ALTERNATIVAS: sin eso, una obligación puede quedarse sin "
                "ninguna de las dos y su capa sin quien la produzca (`F-02` punto 5)")
    autoridad = ((obligatorias.get("campos") or {}).get("autoridad_productora") or {})
    if autoridad.get("valores") != ["OWNER"]:
        r.fallo("`proceso.yaml` no tipa `autoridad_productora` como el enum cerrado "
                "`[OWNER]`: una autoridad sin conjunto declarado es texto libre")
    # Las variantes se declaran UNA vez en la raíz del esquema y los campos apuntan a ella
    # con `variantes_desde`; el ancla YAML no es una opción, porque el analizador stdlib del
    # runtime no admite anclas. Aquí se resuelve contra la misma raíz.
    if spec.get("variantes"):
        variantes = set(spec["variantes"])
    elif spec.get("variantes_desde"):
        declaradas = decl.get(spec["variantes_desde"])
        if not isinstance(declaradas, list):
            r.fallo(f"`proceso.yaml` apunta a `{spec['variantes_desde']}` y el esquema no "
                    f"declara esa lista: el sufijo de variante quedaría sin tipar")
            declaradas = []
        variantes = set(declaradas)
    else:
        r.fallo("`proceso.yaml` no declara el conjunto de variantes admitidas: un sufijo "
                "sin conjunto declarado es texto libre (`F-02` punto 2)")
        variantes = set()
    cond = ((decl.get("campos") or {}).get("condicionales") or {}).get("campos") or {}
    if (cond.get("capacidad") or {}).get("ref_a") != "capacidad":
        r.fallo("`proceso.yaml` no tipa `condicionales.capacidad` como `ref_a: capacidad` "
                "(`F-02` punto 4: la MISMA referencia)")

    for datos, ruta, _l in b.get("proceso", []):
        origen = os.path.relpath(ruta, RAIZ)
        campos_vistos = []
        for obligacion in (datos.get("obligatorias") or []):
            campos_vistos.append((f"{datos.get('id')}·{obligacion.get('id')}",
                                  obligacion.get("capacidad_productora"),
                                  obligacion))
        for condicional in (datos.get("condicionales") or []):
            campos_vistos.append((f"{datos.get('id')}·condicional",
                                  condicional.get("capacidad"), None))
        # `F-02` punto 5 manda MOVER `OWNER`, no duplicarlo: exactamente una de las dos
        # claves. Sin esta comprobación la fila se podía «cerrar» dejando el token viejo
        # en el campo de capacidad y añadiendo el nuevo al lado, que es como estaba.
        for obligacion in (datos.get("obligatorias") or []):
            puestas = [c for c in ("capacidad_productora", "autoridad_productora")
                       if obligacion.get(c) is not None]
            if len(puestas) != 1:
                r.fallo(f"{origen}: {datos.get('id')}·{obligacion.get('id')} declara "
                        f"{len(puestas)} de [capacidad_productora, autoridad_productora] "
                        f"({', '.join(puestas) or 'ninguna'}); `F-02` punto 5 exige "
                        f"EXACTAMENTE UNA, y declarar las dos es la duplicación que el "
                        f"hallazgo retira")
            if obligacion.get("capacidad_productora") == "OWNER":
                r.fallo(f"{origen}: {datos.get('id')}·{obligacion.get('id')} sigue "
                        f"nombrando `OWNER` en el campo de CAPACIDAD; su sede es "
                        f"`autoridad_productora` (`F-02` punto 5)")

        for donde, valor, obligacion in campos_vistos:
            if not isinstance(valor, str):
                continue
            if "/" in valor:
                r.fallo(f"{origen}: {donde} nombra `{valor}`, que es un MÉTODO donde va "
                        f"una CAPACIDAD. `E4.3` lo sustituyó en la fuente aprobada; el "
                        f"derivado no puede seguir diciéndolo (`F-01`)")
                continue
            if valor == "OWNER":
                # Ya denunciado arriba: aquí sólo se evita medirlo como capacidad.
                continue
            if obligacion is not None and obligacion.get("capacidad_productora_derivada"):
                continue
            base = valor.split(":", 1)[0]
            if base not in quince:
                r.fallo(f"{origen}: {donde} declara `{valor}`, y `{base}` no es una de las "
                        f"quince capacidades")
            elif ":" in valor and valor not in variantes:
                r.fallo(f"{origen}: {donde} usa la variante `{valor}`, que el esquema no "
                        f"declara. Una variante sin declarar no está tipada (`F-02` punto 2)")
    return r


def t241_dis_a_ver_anclado_al_ciclo(b):
    """`F-06`."""
    r = Resultado("T241", "La entrega de DIS a VER está anclada a una estación del ciclo de calidad")
    ciclo = os.path.join(RAIZ, "kernel/operativo/diseno/04-CICLO-DE-CALIDAD.md")
    estaciones = set()
    if os.path.exists(ciclo):
        with open(ciclo, encoding="utf-8") as fh:
            estaciones = {int(n) for n in re.findall(r"^\s*(\d{1,2})\s{2}[A-ZÁÉÍÓÚÑ]",
                                                    fh.read(), re.M)}
    if not estaciones:
        r.fallo("no se derivan las estaciones del ciclo de calidad: sin ellas, «anclado a "
                "una estación» no es comprobable")
    handoff = next((d for d, _r, _l in b.get("handoff", [])
                    if d.get("id") == "handoff:dis-a-ver"), None)
    if handoff is None:
        r.fallo("no existe `handoff:dis-a-ver`")
        return r
    cuando = str(handoff.get("cuando") or "")
    citadas = {int(n) for n in re.findall(r"estaci[oó]n\s+(\d{1,2})", cuando, re.I)}
    if not citadas:
        r.fallo("el `cuando` de `handoff:dis-a-ver` no nombra ninguna estación del ciclo: "
                "«DIS cierra su capa» no dice CUÁNDO, y el gate visual tiene DOS pasadas "
                "(`11-ARQ` §19 `F-06`)")
    for n in citadas - estaciones:
        r.fallo(f"el `cuando` de `handoff:dis-a-ver` cita la estación {n}, que el ciclo de "
                f"calidad no declara")
    entrega = " ".join(handoff.get("entrega") or [])
    for dictamen, palabra in (("excelencia visual", "pasada"), ("usabilidad", "estación")):
        trozo = next((x for x in (handoff.get("entrega") or []) if dictamen in x), None)
        if trozo is None:
            r.fallo(f"la entrega no incluye el dictamen de {dictamen}")
        elif palabra not in trozo.lower() and "estaci" not in trozo.lower():
            r.fallo(f"la entrega del dictamen de {dictamen} no dice de qué PASADA procede "
                    f"el dictamen (`F-06`, segunda mitad del remedio)")
    if "fidelidad" not in entrega.lower():
        r.fallo("la entrega no nombra el eje `fidelidad`, que es el único que separa las "
                "dos pasadas y el que obliga a anclar el `cuando`")
    return r


def t242_autoridad_de_los_documentos_del_owner(_b):
    """`F-07`. La fórmula vive en `ads_lint`; aquí SÓLO se consume (`V6-19`)."""
    r = Resultado("T242", "Todo documento de docs/owner/ declara su autoridad, y no la elige: la deriva")
    from ads_lint import autoridad_de_los_documentos_del_owner   # noqa: PLC0415
    declaracion, problemas = autoridad_de_los_documentos_del_owner(RAIZ)
    for problema in problemas:
        r.fallo(problema)
    # Sin registro canónico de zonas esto es un proyecto instalado y la sede del Owner no
    # viaja: la comprobación no tiene sujeto. Donde sí lo tiene, no declarar nada es rojo.
    if os.path.exists(os.path.join(RAIZ, "docs/canonico/FUENTES-CANONICAS.yml")) \
            and not problemas and not declaracion:
        r.fallo("no se declaró la autoridad de ningún documento del Owner")
    return r


def t243_entregas_de_8_0_materializadas(b):
    """`F-05` (i)."""
    r = Resultado("T243", "Las cinco entregas que 11-ARQ §8.0 declara existen como instancias en circuitos/")
    instancias = {}
    for datos, ruta, _l in b.get("handoff", []):
        if "/circuitos/" in ruta.replace(os.sep, "/"):
            instancias[(datos.get("de"), datos.get("a"))] = datos
    for de, a in ENTREGAS_DE_8_0:
        datos = instancias.get((de, a))
        if datos is None:
            r.fallo(f"`11-ARQ` §8.0 declara qué viaja de {de} a {a} y `circuitos/` no tiene "
                    f"la instancia: la composición no se bloquea, la ENTREGA sí (`F-05` i)")
            continue
        for campo in ("cuando", "entrega", "comprueba_al_recibir", "rechaza_si",
                      "devolucion", "checkpoint"):
            if not datos.get(campo):
                r.fallo(f"handoff {de}→{a}: `{campo}` vacío; `C5` lo exige")
    # CONTRASTE contra el documento, cuando el documento está presente.
    sede = os.path.join(RAIZ, SEDE_DE_8_0)
    if os.path.exists(sede):
        with open(sede, encoding="utf-8") as fh:
            declaradas = set(re.findall(r"QU[EÉ] VIAJA DE ([A-Z]{3}) A ([A-Z]{3})", fh.read()))
        if declaradas and declaradas != set(ENTREGAS_DE_8_0):
            r.fallo(f"§8.0 declara {sorted(declaradas)} y el kernel lleva "
                    f"{sorted(ENTREGAS_DE_8_0)}: el dato derivado dejó de coincidir con su "
                    f"documento")
    return r


def t244_grado_inicial_coincide_con_el_paso_5(b):
    """`F-04`."""
    r = Resultado("T244", "El grado inicial del escenario coincide con el grado que midió su paso 5")
    ruta = os.path.join(RAIZ, "kernel/operativo/entrada/05-ESCENARIOS.md")
    if not os.path.exists(ruta):
        r.fallo("no existe `entrada/05-ESCENARIOS.md`")
        return r
    with open(ruta, encoding="utf-8") as fh:
        texto = fh.read()
    medidos = re.findall(r"GRADO GLOBAL\s*=\s*([A-ZÁ]+)", texto)
    if not medidos:
        r.fallo("el escenario ya no publica el GRADO GLOBAL que midió su paso de "
                "incertidumbre: sin él no hay nada con lo que contrastar `grado_inicial`")
        return r
    encuadres = [d for d, ru, _l in b.get("encuadre", []) if os.path.abspath(ru) == ruta]
    if not encuadres:
        r.fallo("el fichero de escenarios no contiene ningún bloque `ads:encuadre`")
        return r
    medido = medidos[0].lower()
    for datos in encuadres:
        inc = datos.get("incertidumbre") or {}
        inicial = inc.get("grado_inicial")
        if inicial != medido:
            r.fallo(f"{datos.get('id')}: el paso 5 midió GRADO GLOBAL = {medidos[0]} y el "
                    f"encuadre persiste `grado_inicial: {inicial}`. Con esa divergencia la "
                    f"crítica independiente que el grado de entrada hace OBLIGATORIA "
                    f"desaparece al bajar el grado (`11-ARQ` §19 `F-04`)")
        if not inc.get("grado"):
            r.fallo(f"{datos.get('id')}: el encuadre no conserva `grado` junto a "
                    f"`grado_inicial`; `F-04` exige los DOS")
    return r


PRUEBAS = [t86_autoridad_subconjunto, t87_independencia_gana, t88_prompt_existe,
           t89_reanudacion_con_prueba, t90_roles_coherentes, t91_metodos_con_gate_y_pasos,
           t92_sin_marca, t135_composicion_respeta_el_contrato,
           t136_vetos_no_se_arbitran, t137_dsp_no_cancela_por_contenido,
           t138_escala_total_y_alcanzable, t139_ningun_nivel_omite_un_gate,
           t144_usabilidad_tiene_portador_en_con,
           t140_obligaciones_y_cierre, t141_frenos_con_ejecutor,
           t142_encuadre_expresa_sus_estados,
           t145_critica_de_encuadre_no_se_evapora, t146_autoridad_de_decision,
           t240_capacidad_tipada_sin_metodos, t241_dis_a_ver_anclado_al_ciclo,
           t242_autoridad_de_los_documentos_del_owner,
           t243_entregas_de_8_0_materializadas,
           t244_grado_inicial_coincide_con_el_paso_5]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--prueba", default=None)
    ap.add_argument("--raiz", default=None, help="ejecutar contra otra copia del corpus")
    args = ap.parse_args()
    if args.raiz:
        fijar_raiz(args.raiz)
    b = cargar()
    resultados = [f(b) for f in PRUEBAS]
    if args.prueba:
        resultados = [r for r in resultados if r.id == args.prueba]
    if args.json:
        print(json.dumps([{"id": r.id, "nombre": r.nombre,
                           "estado": "prueba-superada" if r.superada else "prueba-fallida",
                           "fallos": r.fallos} for r in resultados], ensure_ascii=False, indent=2))
    else:
        for r in resultados:
            estado = "SUPERADA" if r.superada else "FALLIDA "
            print(f"{r.id}  {estado}  {r.nombre}")
            for f in r.fallos:
                print(f"          · {f}")
        fallidas = [r for r in resultados if not r.superada]
        print(f"\n{len(resultados) - len(fallidas)} superadas · {len(fallidas)} fallidas")
    return 1 if any(not r.superada for r in resultados) else 0


if __name__ == "__main__":
    sys.exit(main())
