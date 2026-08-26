#!/usr/bin/env python3
"""ads_lint — validador estructural del kernel operativo ADS.

Comprueba, sobre kernel/operativo/ y packs/:
  1. que todo bloque canónico ```yaml ads:<tipo> tenga un esquema y lo cumpla
  2. unicidad de identificadores
  3. resolución de toda referencia (`ref`) a otro artefacto canónico
  4. resolución de todo enlace relativo de Markdown
  5. ausencia de vocabulario prohibido
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
EXENCION = "ads-lint: permitir-vocabulario-prohibido"
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
    def __init__(self, raiz, ambitos):
        self.raiz = os.path.abspath(raiz)
        self.ambitos = ambitos
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
    def validar_valor(self, valor, spec, ruta, linea, camino, tipo_padre):
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
                self.validar_valor(elem, sub, ruta, linea, f"{camino}[{n}]", tipo_padre)
        elif tipo == "objeto":
            if not isinstance(valor, dict):
                return self.err(ruta, linea, "tipo", f"{camino}: se esperaba objeto")
            for req in spec.get("obligatorios", []):
                if req not in valor or valor[req] is None:
                    self.err(ruta, linea, "obligatorio",
                             f"{camino}.{req}: campo obligatorio no declarado. "
                             f"Si la respuesta es «ninguno», decláralo vacío de forma explícita")
            for clave, sub in (spec.get("campos") or {}).items():
                if clave in valor and valor[clave] is not None:
                    self.validar_valor(valor[clave], sub, ruta, linea, f"{camino}.{clave}", tipo_padre)
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
                    self.validar_valor(datos[clave], spec, ruta, linea, clave, tipo)
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
    def validar_vocabulario(self):
        for ruta in self.ficheros(".md"):
            with open(ruta, encoding="utf-8") as fh:
                texto = fh.read()
            if EXENCION in texto:
                continue
            bajo = texto.lower()
            for linea_n, linea in enumerate(bajo.splitlines(), 1):
                for frase in VOCABULARIO_PROHIBIDO:
                    if frase in linea:
                        self.err(ruta, linea_n, "vocabulario",
                                 f"expresión prohibida «{frase}»: escribe la condición comprobable")

    def validar_enlaces(self):
        for ruta in self.ficheros(".md"):
            with open(ruta, encoding="utf-8") as fh:
                texto = fh.read()
            if EXENCION_ENLACES in texto:
                continue
            base = os.path.dirname(ruta)
            for linea_n, linea in enumerate(texto.splitlines(), 1):
                for destino in ENLACE_MD.findall(linea):
                    if destino.startswith(("http://", "https://", "#", "mailto:")):
                        continue
                    limpio = destino.split("#")[0]
                    if not limpio:
                        continue
                    if not os.path.exists(os.path.normpath(os.path.join(base, limpio))):
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
        self.cargar_esquemas()
        self.cargar_bloques()
        self.validar_bloques()
        self.validar_refs()
        self.validar_vocabulario()
        self.validar_enlaces()
        self.validar_reglas()
        return self.hallazgos


def main():
    ap = argparse.ArgumentParser(description="validador estructural del kernel operativo ADS")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--raiz", default=os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    ap.add_argument("--ambito", action="append", default=None,
                    help="subdirectorio a analizar (repetible). Por defecto kernel/operativo y packs")
    args = ap.parse_args()
    ambitos = args.ambito or ["kernel/operativo", "packs"]
    lint = Lint(args.raiz, ambitos)
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
              f" · errores: {len(errores)} · avisos: {len(avisos)}")
    return 1 if errores else 0


if __name__ == "__main__":
    sys.exit(main())
