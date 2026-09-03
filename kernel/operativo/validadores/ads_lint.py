#!/usr/bin/env python3
"""ads_lint — validador estructural del kernel operativo ADS.

Comprueba, sobre kernel/operativo/ y packs/:
  1. que todo bloque canónico ```yaml ads:<tipo> tenga un esquema y lo cumpla
  2. unicidad de identificadores
  3. resolución de toda referencia (`ref`) a otro artefacto canónico
  4. resolución de todo enlace relativo de Markdown
  5. ausencia de vocabulario prohibido, con exenciones ACOTADAS por rango o por línea
  6. las reglas específicas de validadores/reglas.yaml

Uso:
  python3 kernel/operativo/validadores/ads_lint.py [--json] [--raiz DIR] [--solo PATRON]
Salida: 0 si no hay errores, 1 si los hay.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys

try:
    import yaml
except ImportError:  # pragma: no cover
    print("ads_lint requiere PyYAML: pip install pyyaml", file=sys.stderr)
    sys.exit(2)

BLOQUE = re.compile(r"^```yaml\s+ads:([a-z-]+)\s*$")
FIN_BLOQUE = re.compile(r"^```\s*$")
ENLACE_MD = re.compile(r"\[[^\]]*\]\(([^)\s]+)(?:\s+\"[^\"]*\")?\)")
# Exenciones ACOTADAS. La versión anterior era por FICHERO COMPLETO: bastaba un comentario
# en la cabecera para que todo el documento quedara fuera de la comprobación de
# vocabulario. Diecinueve de los ciento ochenta y ocho ficheros del corpus estaban exentos
# —los seis de diseño, cuatro de los cinco contratos, el circuito de entrada—, es decir,
# justo donde la condición comprobable más importa (hallazgo A-27). Ahora se exime un
# RANGO, y el rango declara su motivo.
#
#   <!-- ads-lint-ignore-next-line: <motivo> -->
#   <!-- ads-lint-ignore-start: <motivo> -->  …  <!-- ads-lint-ignore-end -->
INICIO_EXENCION = re.compile(r"<!--\s*ads-lint-ignore-start:\s*(.+?)\s*-->")
FIN_EXENCION = re.compile(r"<!--\s*ads-lint-ignore-end\s*-->")
EXENCION_LINEA = re.compile(r"<!--\s*ads-lint-ignore-next-line:\s*(.+?)\s*-->")
EXENCION_ENLACES = "ads-lint: permitir-enlaces-rotos"

VOCABULARIO_PROHIBIDO = [
    "si aplica", "si procede", "cuando corresponda", "cuando proceda",
    "según el contexto", "segun el contexto", "según convenga", "segun convenga",
    "el agente decidirá", "el agente decidira", "a criterio del agente",
    "a juicio del agente", "el agente valorará", "el agente valorara",
    "se hará una revisión adecuada", "se hara una revision adecuada",
    "revisión adecuada", "revision adecuada", "revisión apropiada", "revision apropiada",
    "lo que sea razonable", "en la medida de lo posible", "idealmente",
    "preferiblemente", "si fuera necesario", "en su caso",
]


# ===========================================================================
#  `F-07` · la AUTORIDAD de cada documento de `docs/owner/`, DERIVADA
# ===========================================================================
#  SEDE ÚNICA de la fórmula, y los dos consumidores la IMPORTAN en vez de reescribirla
#  (`V6-19`): este validador —que ya recorre `docs/owner/`— y `comprobar_contratos.py`,
#  que publica el resultado como prueba numerada.
#
#  El VALOR no lo elige `F6`: sale de la clase que `docs/canonico/FUENTES-CANONICAS.yml`
#  asigna a cada ruta, que es material canónico y no se toca aquí.
DIRECTORIO_DEL_OWNER = "docs/owner"
AUTORIDAD_POR_CLASE = {
    "AUTORIDAD_SUPERIOR": "aprobada",
    "NO_APLICABLE_A_IMPLEMENTACION": "trabajo",
}
AUTORIDADES_ADMITIDAS = ("aprobada", "trabajo")


def clases_canonicas_de_zona(raiz):
    """Las clases que el registro canónico asigna, por patrón. No se escriben aquí."""
    ruta = os.path.join(raiz, "docs/canonico/FUENTES-CANONICAS.yml")
    if not os.path.exists(ruta):
        return None
    with open(ruta, encoding="utf-8") as fh:
        datos = yaml.safe_load(fh) or {}
    zonas = []
    for entrada in (datos.get("zonas") or datos.get("zonas_del_universo") or []):
        if isinstance(entrada, dict) and entrada.get("patron") and entrada.get("clase"):
            zonas.append((re.compile(entrada["patron"]), entrada["clase"]))
    return zonas


def autoridad_de_los_documentos_del_owner(raiz):
    """Devuelve (declaraciones, problemas). Un problema es un ROJO, no un aviso.

    Falla si: un fichero de `docs/owner/` no tiene autoridad declarada · una declaración
    apunta a un fichero que no existe · el valor no es uno de los dos admitidos · o el
    valor declarado NO coincide con el que la clase canónica de la ruta deriva. Lo último
    es lo que impide que esta lista se convierta en una segunda verdad editable.
    """
    problemas = []
    # DÓNDE APLICA. La sede del Owner vive en el repositorio del kernel y **no viaja** al
    # proyecto instalado; `exclusiones.yaml` sí viaja. El marcador de «aquí vive la sede» no
    # es la presencia del propio directorio —que sería circular: borrarlo apagaría la
    # comprobación— sino la del registro canónico de zonas, que es de donde se DERIVA el
    # valor. Con registro y sin directorio, es un ROJO; sin registro, la comprobación no
    # tiene sujeto y se declara inaplicable.
    registro = os.path.join(raiz, "docs/canonico/FUENTES-CANONICAS.yml")
    if not os.path.exists(registro):
        return {}, []
    if not os.path.isdir(os.path.join(raiz, DIRECTORIO_DEL_OWNER)):
        return {}, [f"existe `docs/canonico/FUENTES-CANONICAS.yml`, que clasifica "
                    f"`{DIRECTORIO_DEL_OWNER}/`, y el directorio NO existe"]
    ruta_excl = os.path.join(raiz, "kernel/operativo/validadores/exclusiones.yaml")
    if not os.path.exists(ruta_excl):
        return {}, ["no existe `validadores/exclusiones.yaml`: sin él `F-07` no se comprueba"]
    with open(ruta_excl, encoding="utf-8") as fh:
        datos = yaml.safe_load(fh) or {}
    declaradas = datos.get("autoridad_de_documentos_del_owner")
    if not declaradas:
        return {}, ["`exclusiones.yaml` no declara `autoridad_de_documentos_del_owner`: "
                    "la distinción aprobada/trabajo de `docs/owner/` volvería a estar sólo "
                    "en prosa (`11-ARQ` §19 `F-07`)"]

    zonas = clases_canonicas_de_zona(raiz)
    directorio = os.path.join(raiz, DIRECTORIO_DEL_OWNER)
    en_disco = sorted(f"{DIRECTORIO_DEL_OWNER}/{n}" for n in os.listdir(directorio)
                      if n.endswith(".md")) if os.path.isdir(directorio) else []

    declaracion = {}
    for entrada in declaradas:
        if not isinstance(entrada, dict) or not entrada.get("ruta") or not entrada.get("motivo"):
            problemas.append("una declaración de autoridad sin `ruta` o sin `motivo`: "
                             "una exención sin motivo escrito no es una exención")
            continue
        rel, valor = entrada["ruta"], entrada.get("autoridad")
        if valor not in AUTORIDADES_ADMITIDAS:
            problemas.append(f"{rel}: `autoridad: {valor}` no es uno de los dos valores "
                             f"declarados {list(AUTORIDADES_ADMITIDAS)}")
            continue
        if not os.path.exists(os.path.join(raiz, rel)):
            problemas.append(f"{rel}: se le declara autoridad y el fichero no existe")
            continue
        if zonas is not None:
            clase = next((c for patron, c in zonas if patron.search(rel)), None)
            if clase is None:
                problemas.append(f"{rel}: ninguna zona de `FUENTES-CANONICAS.yml` la "
                                 f"clasifica, y sin clase la autoridad no se deriva")
            elif AUTORIDAD_POR_CLASE.get(clase) != valor:
                problemas.append(
                    f"{rel}: declara `autoridad: {valor}` y su clase canónica `{clase}` "
                    f"deriva `{AUTORIDAD_POR_CLASE.get(clase)}`. El valor no se escribe: "
                    f"se deriva de `docs/canonico/FUENTES-CANONICAS.yml`")
        declaracion[rel] = valor

    for rel in en_disco:
        if rel not in declaracion:
            problemas.append(f"{rel}: vive en `{DIRECTORIO_DEL_OWNER}/` y NO declara su "
                             f"autoridad. Un documento del Owner sin `aprobada|trabajo` "
                             f"declarado pasa por omisión, que es lo que `F-07` cierra")
    return declaracion, problemas


class Hallazgo:
    def __init__(self, nivel, fichero, linea, regla, mensaje):
        self.nivel, self.fichero, self.linea = nivel, fichero, linea
        self.regla, self.mensaje = regla, mensaje

    def __str__(self):
        pos = f"{self.fichero}:{self.linea}" if self.linea else self.fichero
        return f"{self.nivel.upper():7} {pos}  [{self.regla}] {self.mensaje}"

    def a_dict(self):
        return {"nivel": self.nivel, "fichero": self.fichero, "linea": self.linea,
                "regla": self.regla, "mensaje": self.mensaje}


class Lint:
    def __init__(self, raiz, ambitos, ambitos_texto=None):
        self.raiz = os.path.abspath(raiz)
        self.ambitos = ambitos
        # Ámbito de ENLACES y VOCABULARIO. Por defecto el repositorio entero: la portada,
        # START_HERE y docs/ quedaban fuera, y por eso el hallazgo A-12 —tres versiones
        # para el mismo artefacto en el README— no lo veía ningún validador.
        self.ambitos_texto = ambitos_texto if ambitos_texto is not None else ["."]
        self.exentos_vocabulario = []
        self.no_analizados = []
        self.no_embarcados = []
        self.enlaces_aguas_arriba = 0
        self.hallazgos = []
        self.esquemas = {}
        self.bloques = []          # (tipo, datos, fichero, linea)
        self.ids = {}              # id -> (tipo, fichero)
        self.refs = []             # (id_referido, tipo_esperado, fichero, linea, campo)
        self.reglas = {}

    # ---------------------------------------------------------------- utilidades
    def err(self, f, l, regla, msg):
        self.hallazgos.append(Hallazgo("error", self.rel(f), l, regla, msg))

    def avi(self, f, l, regla, msg):
        self.hallazgos.append(Hallazgo("aviso", self.rel(f), l, regla, msg))

    def rel(self, f):
        return os.path.relpath(f, self.raiz) if os.path.isabs(f) else f

    def cargar_exclusiones(self):
        ruta = os.path.join(self.raiz, "kernel/operativo/validadores/exclusiones.yaml")
        if not os.path.exists(ruta):
            return
        with open(ruta, encoding="utf-8") as fh:
            datos = yaml.safe_load(fh) or {}
        self.exentos_vocabulario = [i["ruta"] for i in (datos.get("vocabulario_exento") or [])
                                    if isinstance(i, dict) and i.get("ruta")]
        self.no_analizados = [i["ruta"] for i in (datos.get("no_analizados") or [])
                              if isinstance(i, dict) and i.get("ruta")]
        # La frontera del proyecto instalado. Ver el bloque de exclusiones.yaml: sólo se
        # activa donde la ruta declarada NO existe, que es el proyecto instalado y nunca
        # este repositorio.
        self.no_embarcados = [i["ruta"] for i in (datos.get("enlaces_no_embarcados") or [])
                              if isinstance(i, dict) and i.get("ruta") and i.get("motivo")]

    def _resolver_listas_del_esquema(self, datos, ruta):
        """`variantes_desde: <clave>` se resuelve contra la RAÍZ del esquema.

        Por qué no un ancla YAML. `runtime/ciclo/corpus.py` analiza estos mismos ficheros
        con un analizador propio de biblioteca estándar —el runtime VIAJA y no puede
        depender de PyYAML—, y ese subconjunto **no admite anclas, alias ni etiquetas**.
        Un `&ancla` aquí deja el esquema legible para el validador e ILEGIBLE para el
        runtime, que es la peor de las dos verdades: la que sólo se descubre ejecutando.
        Con `variantes_desde` la lista sigue teniendo UNA sede en el fichero y el
        subconjunto se respeta.
        """
        def recorrer(nodo):
            if isinstance(nodo, dict):
                clave = nodo.get("variantes_desde")
                if isinstance(clave, str):
                    lista = datos.get(clave)
                    if not isinstance(lista, list):
                        self.err(ruta, None, "esquema",
                                 f"`variantes_desde: {clave}` y el esquema no declara esa "
                                 f"lista en su raíz")
                    else:
                        nodo["variantes"] = list(lista)
                for valor in nodo.values():
                    recorrer(valor)
            elif isinstance(nodo, list):
                for valor in nodo:
                    recorrer(valor)
        recorrer(datos.get("campos") or {})

    def _excluido(self, ruta, lista):
        rel = os.path.relpath(ruta, self.raiz).replace(os.sep, "/")
        return any(rel == x or rel.startswith(x.rstrip("/") + "/") for x in lista)

    def ficheros_texto(self, ext):
        vistos = set()
        for ambito in self.ambitos_texto:
            base = os.path.join(self.raiz, ambito)
            for dirpath, dirnames, filenames in os.walk(base):
                dirnames[:] = [d for d in dirnames
                               if d not in (".git", "__pycache__") and not d.startswith("legacy-")]
                for nombre in sorted(filenames):
                    if not nombre.endswith(ext):
                        continue
                    ruta = os.path.join(dirpath, nombre)
                    if self._excluido(ruta, self.no_analizados):
                        continue
                    if ruta not in vistos:
                        vistos.add(ruta)
                        yield ruta

    def ficheros(self, ext):
        for ambito in self.ambitos:
            base = os.path.join(self.raiz, ambito)
            for dirpath, dirnames, filenames in os.walk(base):
                dirnames[:] = [d for d in dirnames
                               if d not in (".git", "__pycache__") and not d.startswith("legacy-")]
                for nombre in sorted(filenames):
                    if nombre.endswith(ext):
                        yield os.path.join(dirpath, nombre)

    # ---------------------------------------------------------------- carga
    def cargar_esquemas(self):
        dir_esq = os.path.join(self.raiz, "kernel/operativo/esquemas")
        for nombre in sorted(os.listdir(dir_esq)):
            if not nombre.endswith(".yaml"):
                continue
            ruta = os.path.join(dir_esq, nombre)
            with open(ruta, encoding="utf-8") as fh:
                try:
                    datos = yaml.safe_load(fh)
                except yaml.YAMLError as exc:
                    self.err(ruta, None, "yaml", f"esquema ilegible: {exc}")
                    continue
            if not isinstance(datos, dict) or datos.get("kind") != "esquema":
                self.err(ruta, None, "esquema", "un fichero de esquemas debe declarar kind: esquema")
                continue
            self._resolver_listas_del_esquema(datos, ruta)
            self.esquemas[datos["esquema"]] = datos
        ruta_reglas = os.path.join(self.raiz, "kernel/operativo/validadores/reglas.yaml")
        if os.path.exists(ruta_reglas):
            with open(ruta_reglas, encoding="utf-8") as fh:
                self.reglas = yaml.safe_load(fh) or {}

    def cargar_bloques(self):
        for ruta in self.ficheros(".md"):
            with open(ruta, encoding="utf-8") as fh:
                lineas = fh.readlines()
            i = 0
            while i < len(lineas):
                m = BLOQUE.match(lineas[i].rstrip("\n"))
                if not m:
                    i += 1
                    continue
                tipo, inicio, cuerpo = m.group(1), i + 1, []
                i += 1
                while i < len(lineas) and not FIN_BLOQUE.match(lineas[i].rstrip("\n")):
                    cuerpo.append(lineas[i])
                    i += 1
                if i >= len(lineas):
                    self.err(ruta, inicio, "bloque", "bloque canónico sin cierre ```")
                    break
                try:
                    datos = yaml.safe_load("".join(cuerpo))
                except yaml.YAMLError as exc:
                    self.err(ruta, inicio, "yaml", f"bloque ads:{tipo} ilegible: {exc}")
                    i += 1
                    continue
                if not isinstance(datos, dict):
                    self.err(ruta, inicio, "bloque", f"el bloque ads:{tipo} no es un mapa")
                    i += 1
                    continue
                self.bloques.append((tipo, datos, ruta, inicio))
                i += 1

    # ---------------------------------------------------------------- esquema
    def validar_ref_tipada(self, valor, spec, ruta, linea, camino, padre):
        """Una `ref` con SUFIJO DE VARIANTE tipado. Es el remedio exacto de `F-02`.

        `11-ARQ` §19, fila `F-02`, fija el vocabulario y lo fija entero: (1) la capacidad
        base es una de las QUINCE y sólo una de las quince; (2) admite un sufijo
        `:<variante>` OPCIONAL y TIPADO, y las variantes declaradas son las que la fila
        enumera; (3) **`/` NO es válido** —es lo que hoy admite un MÉTODO donde va una
        capacidad, y es la raíz de `F-01`/`PN-14`—; (4) `capacidad_productora` usa la MISMA
        referencia; (5) **`OWNER` NO es una capacidad**: se separa como AUTORIDAD, en su
        propio campo.

        `autoridades` declara los tokens que NO son capacidad y que exigen el campo de
        autoridad hermano. `derivable_con` declara el campo hermano que autoriza —y sólo
        entonces— una formulación DERIVADA en prosa, que es lo que `b.16` hace en `DIR`
        cuando la capacidad productora la fija el encargo y no la tabla. Sin ese hermano,
        la prosa NO entra: sin él, cualquier cadena valdría y el tipado no tiparía nada.
        """
        padre = padre or {}
        if "/" in valor:
            return self.err(ruta, linea, "metodo-donde-va-capacidad",
                            f"{camino}: '{valor}' nombra un MÉTODO donde va una CAPACIDAD. "
                            f"`/` no es separador de variante (11-ARQ §19 `F-02` punto 3). "
                            f"Una ruta nombra capacidades; qué método se ejecuta lo calcula "
                            f"la escala de novedad (`E4.3`)")
        # `F-02` punto 5 dice MOVER, no duplicar: una AUTORIDAD ya no cabe en el campo de
        # capacidad EN NINGUNA FORMA, ni siquiera acompañada de su campo hermano. La
        # tolerancia anterior dejaba `OWNER` viviendo en los dos sitios, que es exactamente
        # el estado que el hallazgo existe para retirar.
        prohibidos = spec.get("prohibidos") or []
        if valor in prohibidos:
            return self.err(ruta, linea, "autoridad-en-campo-de-capacidad",
                            f"{camino}: '{valor}' es una AUTORIDAD y no una de las quince "
                            f"capacidades. `F-02` punto 5 manda MOVERLA a su campo propio "
                            f"`autoridad_productora`, no declararla en los dos")
        derivable = spec.get("derivable_con")
        if derivable and padre.get(derivable):
            if len(valor.strip()) < 15:
                self.err(ruta, linea, "derivacion-telegrafica",
                         f"{camino}: la capacidad productora se declara DERIVADA y su "
                         f"formulación no dice de qué se deriva")
            return None
        m = re.fullmatch(r"([A-Z]{3})(?::([a-z]+))?", valor)
        if not m:
            return self.err(ruta, linea, "capacidad-no-tipada",
                            f"{camino}: '{valor}' no es una referencia de capacidad. "
                            f"Forma admitida: `<CAP>` o `<CAP>:<variante>` con la variante "
                            f"declarada en el esquema; una autoridad va en su campo propio "
                            f"y una derivación se declara con `{derivable}`")
        if m.group(2) is not None and valor not in (spec.get("variantes") or []):
            self.err(ruta, linea, "variante-no-declarada",
                     f"{camino}: la variante '{valor}' no está declarada. Declaradas: "
                     f"{spec.get('variantes')}. Una variante sin declarar es texto libre "
                     f"donde el esquema promete un tipo")
        self.refs.append((m.group(1), spec.get("ref_a"), ruta, linea, camino))
        return None

    def validar_valor(self, valor, spec, ruta, linea, camino, tipo_padre, padre=None):
        tipo = spec.get("tipo", "texto")
        if tipo == "texto":
            if not isinstance(valor, str):
                return self.err(ruta, linea, "tipo", f"{camino}: se esperaba texto")
            if "min" in spec and len(valor.strip()) < spec["min"]:
                self.err(ruta, linea, "min", f"{camino}: texto demasiado corto "
                                             f"({len(valor.strip())} < {spec['min']}); un campo operativo vacío o telegráfico no es ejecutable")
            if "patron" in spec and not re.fullmatch(spec["patron"], valor):
                self.err(ruta, linea, "patron", f"{camino}: '{valor}' no casa con {spec['patron']}")
        elif tipo == "entero":
            if not isinstance(valor, int) or isinstance(valor, bool):
                return self.err(ruta, linea, "tipo", f"{camino}: se esperaba entero")
            if "min" in spec and valor < spec["min"]:
                self.err(ruta, linea, "min", f"{camino}: {valor} < {spec['min']}")
        elif tipo == "numero":
            if isinstance(valor, bool) or not isinstance(valor, (int, float)):
                return self.err(ruta, linea, "tipo", f"{camino}: se esperaba número")
            if "min" in spec and valor < spec["min"]:
                self.err(ruta, linea, "min", f"{camino}: {valor} < {spec['min']}")
        elif tipo == "booleano":
            if not isinstance(valor, bool):
                self.err(ruta, linea, "tipo", f"{camino}: se esperaba true/false")
        elif tipo == "enum":
            valores = spec.get("valores", [])
            if valor not in valores:
                self.err(ruta, linea, "enum", f"{camino}: '{valor}' no está en {valores}")
        elif tipo == "ref":
            if not isinstance(valor, str):
                return self.err(ruta, linea, "tipo", f"{camino}: una ref debe ser texto")
            if "variantes" in spec or "prohibidos" in spec:
                return self.validar_ref_tipada(valor, spec, ruta, linea, camino, padre)
            self.refs.append((valor, spec.get("ref_a"), ruta, linea, camino))
        elif tipo == "lista":
            if not isinstance(valor, list):
                return self.err(ruta, linea, "tipo", f"{camino}: se esperaba lista")
            if "min" in spec and len(valor) < spec["min"]:
                self.err(ruta, linea, "min", f"{camino}: {len(valor)} elementos < {spec['min']}")
            de = spec.get("de", "texto")
            for n, elem in enumerate(valor):
                sub = dict(spec)
                sub.pop("min", None)
                sub["tipo"] = de
                self.validar_valor(elem, sub, ruta, linea, f"{camino}[{n}]", tipo_padre, padre)
        elif tipo == "objeto":
            if not isinstance(valor, dict):
                return self.err(ruta, linea, "tipo", f"{camino}: se esperaba objeto")
            for req in spec.get("obligatorios", []):
                if req not in valor or valor[req] is None:
                    self.err(ruta, linea, "obligatorio",
                             f"{camino}.{req}: campo obligatorio no declarado. "
                             f"Si la respuesta es «ninguno», decláralo vacío de forma explícita")
            # EXACTAMENTE UNO de cada grupo. Ni cero —la capa quedaría sin quien la
            # produzca— ni dos —que es la duplicación que `F-02` retira—.
            for grupo in spec.get("obligatorios_alternativos", []):
                puestos = [c for c in grupo if valor.get(c) is not None]
                if len(puestos) != 1:
                    self.err(ruta, linea, "obligatorio-alternativo",
                             f"{camino}: de [{', '.join(grupo)}] tiene que declararse "
                             f"EXACTAMENTE UNO, y se han declarado {len(puestos)}"
                             + (f" ({', '.join(puestos)})" if puestos else ""))
            for clave, sub in (spec.get("campos") or {}).items():
                if clave in valor and valor[clave] is not None:
                    self.validar_valor(valor[clave], sub, ruta, linea, f"{camino}.{clave}",
                                       tipo_padre, valor)
        else:
            self.err(ruta, linea, "esquema", f"{camino}: tipo desconocido '{tipo}'")

    def validar_bloques(self):
        for tipo, datos, ruta, linea in self.bloques:
            esquema = self.esquemas.get(tipo)
            if not esquema:
                self.err(ruta, linea, "esquema", f"no existe esquema para ads:{tipo}")
                continue
            for req in esquema.get("obligatorios", []):
                if req not in datos or datos[req] is None:
                    self.err(ruta, linea, "obligatorio",
                             f"ads:{tipo} no declara '{req}' (obligatorio en esquemas/{tipo}.yaml). "
                             f"Si la respuesta es «ninguno», decláralo vacío de forma explícita")
            for clave, spec in (esquema.get("campos") or {}).items():
                if clave in datos and datos[clave] is not None:
                    self.validar_valor(datos[clave], spec, ruta, linea, clave, tipo, datos)
            desconocidos = set(datos) - set(esquema.get("campos") or {}) - {"kind"}
            for extra in sorted(desconocidos):
                self.avi(ruta, linea, "campo-extra",
                         f"ads:{tipo} declara '{extra}', que el esquema no conoce")
            ident = datos.get("id")
            if isinstance(ident, str):
                if ident in self.ids:
                    otro_tipo, otro_f = self.ids[ident]
                    self.err(ruta, linea, "id-duplicado",
                             f"'{ident}' ya está declarado como ads:{otro_tipo} en {self.rel(otro_f)}")
                else:
                    self.ids[ident] = (tipo, ruta)

    def validar_refs(self):
        for ident, tipo_esperado, ruta, linea, campo in self.refs:
            if ident not in self.ids:
                self.err(ruta, linea, "ref-rota",
                         f"{campo}: '{ident}' no está declarado en ningún bloque canónico")
                continue
            tipo_real = self.ids[ident][0]
            if tipo_esperado and tipo_real != tipo_esperado:
                self.err(ruta, linea, "ref-tipo",
                         f"{campo}: '{ident}' es ads:{tipo_real}, se esperaba ads:{tipo_esperado}")

    # ---------------------------------------------------------------- texto
    def lineas_exentas(self, texto):
        """Qué líneas quedan fuera, por rango o por marca de línea siguiente.

        Devuelve (exentas, huerfanas): las huérfanas son marcas de fin sin inicio o
        rangos sin cerrar, que son un defecto por sí mismos: una exención abierta se
        convierte en una exención de fichero completo por descuido.
        """
        exentas, problemas = set(), []
        abierto_en = None
        for n, linea in enumerate(texto.splitlines(), 1):
            if INICIO_EXENCION.search(linea):
                if abierto_en:
                    problemas.append((n, "exención abierta dentro de otra ya abierta"))
                abierto_en = n
                exentas.add(n)
                continue
            if FIN_EXENCION.search(linea):
                if not abierto_en:
                    problemas.append((n, "cierre de exención sin inicio"))
                abierto_en = None
                exentas.add(n)
                continue
            if abierto_en:
                exentas.add(n)
            if EXENCION_LINEA.search(linea):
                exentas.add(n)
                exentas.add(n + 1)
        if abierto_en:
            problemas.append((abierto_en, "exención abierta y nunca cerrada"))
        return exentas, problemas

    def validar_vocabulario(self):
        for ruta in self.ficheros_texto(".md"):
            if self._excluido(ruta, self.exentos_vocabulario):
                continue
            with open(ruta, encoding="utf-8") as fh:
                texto = fh.read()
            exentas, problemas = self.lineas_exentas(texto)
            for linea_n, motivo in problemas:
                self.err(ruta, linea_n, "exencion", f"{motivo}: una exención sin cerrar "
                                                    f"exime el resto del fichero por descuido")
            bajo = texto.lower()
            for linea_n, linea in enumerate(bajo.splitlines(), 1):
                if linea_n in exentas:
                    continue
                for frase in VOCABULARIO_PROHIBIDO:
                    if frase in linea:
                        self.err(ruta, linea_n, "vocabulario",
                                 f"expresión prohibida «{frase}»: escribe la condición comprobable")

    def validar_enlaces(self):
        for ruta in self.ficheros_texto(".md"):
            with open(ruta, encoding="utf-8") as fh:
                texto = fh.read()
            if EXENCION_ENLACES in texto:
                continue
            base = os.path.dirname(ruta)
            dentro_de_bloque = False
            for linea_n, linea in enumerate(texto.splitlines(), 1):
                if linea.lstrip().startswith("```"):
                    dentro_de_bloque = not dentro_de_bloque
                    continue
                # un enlace dentro de un bloque cercado es una ilustración, no una
                # referencia: se muestra tal cual y no tiene por qué resolver
                if dentro_de_bloque:
                    continue
                for destino in ENLACE_MD.findall(linea):
                    if destino.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    limpio = destino.split("#")[0]
                    if not limpio:
                        continue
                    absoluto = os.path.normpath(os.path.join(base, limpio))
                    if os.path.exists(absoluto):
                        continue
                    rel_destino = os.path.relpath(absoluto, self.raiz).replace(os.sep, "/")
                    if rel_destino in self.no_embarcados:
                        # Material que se queda AGUAS ARRIBA por decisión declarada, con su
                        # motivo escrito. No es un descuido, y se cuenta para que se vea.
                        self.enlaces_aguas_arriba += 1
                        continue
                    self.err(ruta, linea_n, "enlace-roto", f"no existe: {destino}")

    # ---------------------------------------------------------------- reglas
    def validar_reglas(self):
        for regla in self.reglas.get("reglas", []):
            rid = regla.get("id", "sin-id")
            tipo = regla.get("aplica_a")
            objetivo = [b for b in self.bloques if b[0] == tipo]
            minimo = regla.get("minimo")
            if minimo is not None and len(objetivo) < minimo:
                self.err(os.path.join(self.raiz, "kernel/operativo"), None, rid,
                         f"{regla.get('mensaje', 'faltan bloques')} ({len(objetivo)} < {minimo})")
            campo_no_vacio = regla.get("campo_no_vacio")
            if campo_no_vacio:
                for _, datos, ruta, linea in objetivo:
                    if not datos.get(campo_no_vacio):
                        self.err(ruta, linea, rid, regla.get("mensaje", f"'{campo_no_vacio}' vacío"))
            requiere_texto = regla.get("campo_contiene")
            if requiere_texto:
                campo, sub = requiere_texto["campo"], requiere_texto["texto"]
                for _, datos, ruta, linea in objetivo:
                    valor = json.dumps(datos.get(campo, ""), ensure_ascii=False).lower()
                    if sub.lower() not in valor:
                        self.err(ruta, linea, rid, regla.get("mensaje", "condición no cumplida"))

    # ---------------------------------------------------------------- ejecución
    def ejecutar(self):
        self.cargar_exclusiones()
        self.cargar_esquemas()
        self.cargar_bloques()
        self.validar_bloques()
        self.validar_refs()
        self.validar_vocabulario()
        self.validar_enlaces()
        self.validar_reglas()
        self.validar_autoridad_del_owner()
        return self.hallazgos

    # ------------------------------------------------------------- F-07
    def validar_autoridad_del_owner(self):
        """`F-07`. La fórmula vive arriba y aquí SÓLO se consume (`V6-19`)."""
        _decl, problemas = autoridad_de_los_documentos_del_owner(self.raiz)
        destino = os.path.join(self.raiz, "kernel/operativo/validadores/exclusiones.yaml")
        for problema in problemas:
            self.err(destino, None, "autoridad-del-owner", problema)


def main():
    ap = argparse.ArgumentParser(description="validador estructural del kernel operativo ADS")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    ap.add_argument("--ambito", action="append", default=None,
                    help="subdirectorio a analizar (repetible). Por defecto kernel/operativo y packs")
    args = ap.parse_args()
    ambitos = args.ambito or ["kernel/operativo", "packs"]
    # los bloques canónicos viven en kernel/operativo y packs; los ENLACES y el
    # VOCABULARIO se comprueban en TODO el repositorio (hallazgo A-28)
    lint = Lint(args.raiz, ambitos, ambitos_texto=(args.ambito or ["."]))
    hallazgos = lint.ejecutar()
    errores = [h for h in hallazgos if h.nivel == "error"]
    avisos = [h for h in hallazgos if h.nivel == "aviso"]
    if args.json:
        print(json.dumps({
            "bloques": len(lint.bloques), "ids": len(lint.ids),
            "errores": len(errores), "avisos": len(avisos),
            "hallazgos": [h.a_dict() for h in hallazgos]}, ensure_ascii=False, indent=2))
    else:
        for h in hallazgos:
            print(h)
        print(f"\nbloques canónicos: {len(lint.bloques)} · identificadores: {len(lint.ids)}"
              f" · errores: {len(errores)} · avisos: {len(avisos)}"
              f" · enlaces a material no embarcado: {lint.enlaces_aguas_arriba}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
