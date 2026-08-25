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

import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(__file__))
from ads_lint import Lint  # noqa: E402

RAIZ = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))

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
    "kernel/operativo/contratos/C2-AGENTES-Y-MODELOS.md",
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
    r = Resultado("T86", "La autoridad de un rol no excede la de su capacidad")
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
    r = Resultado("T87", "Ningún rol declarado independiente aparece como combinable")
    for datos, ruta, _ in b.get("composicion", []):
        combinables = " · ".join(datos.get("combinables") or [])
        for indep in datos.get("independientes") or []:
            roles_indep = re.findall(r"[a-z0-9-]+:[A-Z]{3}/[a-z0-9-]+|[A-Z]{3}/[a-z0-9-]+", indep)
            for rol in roles_indep:
                if rol in combinables:
                    r.fallo(f"{datos['id']}: '{rol}' aparece a la vez en combinables y en independientes")
    return r


def t88_prompt_existe(b):
    r = Resultado("T88", "Todo rol apunta a un prompt operativo que existe")
    for datos, ruta, _ in b.get("rol", []):
        prompt = datos.get("prompt")
        if not prompt:
            r.fallo(f"{datos.get('id')}: sin prompt declarado")
            continue
        if not os.path.exists(os.path.join(RAIZ, prompt)):
            r.fallo(f"{datos['id']}: el prompt declarado no existe → {prompt}")
    return r


def t89_reanudacion_con_prueba(b):
    r = Resultado("T89", "Toda prueba de reanudación cita un escenario que existe")
    ids = {d.get("id") for d, _, _ in b.get("escenario", [])}
    for datos, ruta, _ in b.get("metodo", []):
        texto = datos.get("prueba_de_reanudacion", "")
        citadas = set(re.findall(r"\bT\d{2,3}\b", texto))
        if not citadas:
            r.fallo(f"{datos.get('id')}: su prueba de reanudación no cita ningún escenario numerado")
            continue
        for t in citadas:
            if t not in ids:
                r.fallo(f"{datos['id']}: cita {t}, que no está declarada como ads:escenario")
    return r


def t90_roles_coherentes(b):
    r = Resultado("T90", "Capacidades y roles se referencian mutuamente sin huérfanos")
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
        if cid in caps and rid not in caps[cid].get("roles", []):
            r.fallo(f"{rid}: dice pertenecer a {cid}, que no lo lista entre sus roles")
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
    r = Resultado("T92", "Ningún contrato del kernel ni de un pack exige una marca concreta")
    for ambito in ("kernel/operativo", "packs"):
        for dirpath, dirnames, filenames in os.walk(os.path.join(RAIZ, ambito)):
            dirnames[:] = [d for d in dirnames if not d.startswith("legacy-") and d != "__pycache__"]
            for nombre in filenames:
                if not nombre.endswith(".md"):
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


PRUEBAS = [t86_autoridad_subconjunto, t87_independencia_gana, t88_prompt_existe,
           t89_reanudacion_con_prueba, t90_roles_coherentes, t91_metodos_con_gate_y_pasos,
           t92_sin_marca]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--prueba", default=None)
    args = ap.parse_args()
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
