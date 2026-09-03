#!/usr/bin/env python3
"""puntero — cómo un entorno abierto SOBRE UNA FUENTE localiza su CONTROL REPO hermano.

Sede: `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` §6.7, sus cuatro reglas, y §6.4, que
hace de esta resolución una de las comprobaciones EXIGIDAS de la prueba de humo en sesión
nueva. Cierra el hallazgo `I.2`: §6.7 remitía a la prueba de humo como la que mide si un
entorno honra el puntero, y aquella prueba no contenía NINGUNA comprobación que abriera el
entorno sobre una fuente. Era una remisión que no llegaba a ninguna parte.

DECISIÓN · esto vive en el ADAPTADOR y no en su prueba
    Alternativas: (a) dejar la resolución dentro del guion de la batería de sesión nueva,
    que es donde nació y donde se ejecutó por primera vez; (b) subirla al paquete de
    adaptadores y que la batería la importe.
    Se elige (b). Con (a) la capacidad existiría SÓLO mientras corre la prueba: ningún
    entorno real podría usarla, y §6.7 quedaría con una regla que nadie implementa mientras
    su prueba pasa en verde. Una prueba que contiene el producto en vez de ejercerlo es
    exactamente lo que `20.0` llama evidencia de consistencia confundida con implementación.

DECISIÓN · los CUATRO desenlaces son CUATRO VALORES, y ninguno se colapsa
    §6.4 los exige «como resultados EXIGIDOS y distintos». `NO_LO_ENCUENTRA` y
    `NO_SE_PUDO_COMPROBAR` son la pareja que más fácilmente se funde, y son cosas opuestas:
    la primera dice que se miró y no estaba; la segunda, que no se pudo mirar. Colapsarlas
    convierte un impedimento de permisos en una ausencia, y entonces el entorno arranca
    creyendo que no hay control repo cuando lo que pasa es que no pudo verlo.

DECISIÓN · la comparación es por IDENTIDAD del remoto, no por su ortografía
    Dos escrituras del mismo remoto —con credenciales y sin ellas, con `.git` y sin él,
    `ssh` y `https`— son el MISMO remoto. Sin normalizar, el descubrimiento falla por una
    diferencia de tecleo, que es literalmente lo que §6.7 regla 4 nombra.

DECISIÓN · el puntero es DATO y nada más
    Si el puntero trajera conocimiento sería una segunda copia del kernel, que es
    `CAND-016`: la memoria espejada que divergió 23 contra 32 entradas. Aquí sólo se leen
    escalares y una lista de componentes.
"""
from __future__ import annotations

import os
import subprocess

# Los CUATRO desenlaces de §6.4. Vocabulario CERRADO.
ENCONTRADO = "LO_ENCUENTRA"
NO_ENCONTRADO = "NO_LO_ENCUENTRA"
NO_SE_PUDO = "NO_SE_PUDO_COMPROBAR"
DOS = "ENCUENTRA_DOS"

DESENLACES = (ENCONTRADO, NO_ENCONTRADO, NO_SE_PUDO, DOS)

# Lo que la ficha del adaptador declara sobre esta capacidad (§3.4). Es una cadena y no una
# lista porque el esquema de la ficha declara campos de texto.
DESENLACES_DECLARADOS = (
    "lee el puntero de la fuente, localiza el control repo hermano por IDENTIDAD del remoto "
    "canónico y devuelve uno de cuatro desenlaces DISTINTOS: "
    + " · ".join(DESENLACES)
    + ". `NO_LO_ENCUENTRA` es ausencia comprobada y `NO_SE_PUDO_COMPROBAR` es impedimento: "
    "no se colapsan"
)

NOMBRE_POR_DEFECTO = ".ads-puntero"
PROFUNDIDAD_POR_DEFECTO = 2

# Git tiene que correr sin la configuración de la máquina y sin poder pedir credenciales:
# un descubrimiento que dependa del `~/.gitconfig` de quien ejecuta no es reproducible.
_ENTORNO_BASE = {
    "LC_ALL": "C",
    "GIT_CONFIG_GLOBAL": os.devnull,
    "GIT_CONFIG_SYSTEM": os.devnull,
    "GIT_TERMINAL_PROMPT": "0",
}


def normalizar_remoto(url):
    """Sin credenciales · con y sin `.git` · `ssh` y `https` EQUIVALENTES."""
    texto = (url or "").strip()
    if not texto:
        return ""
    for prefijo in ("ssh://", "https://", "http://", "git://"):
        if texto.startswith(prefijo):
            texto = texto[len(prefijo):]
            break
    if "@" in texto.split("/", 1)[0]:
        texto = texto.split("@", 1)[1]
    texto = texto.replace(":", "/", 1) if ":" in texto.split("/", 1)[0] else texto
    if texto.endswith(".git"):
        texto = texto[: -len(".git")]
    return texto.rstrip("/").lower()


def leer_puntero(fuente, nombre=NOMBRE_POR_DEFECTO):
    """El puntero de una fuente: DATOS. `None` si no lo hay."""
    ruta = os.path.join(fuente, nombre)
    if not os.path.isfile(ruta):
        return None
    datos = {"componentes": []}
    with open(ruta, encoding="utf-8") as manejador:
        for linea in manejador:
            recorte = linea.strip()
            if not recorte or recorte.startswith("#"):
                continue
            if recorte.startswith("- "):
                datos["componentes"].append(recorte[2:].strip())
                continue
            clave, _, valor = recorte.partition(":")
            clave, valor = clave.strip(), valor.strip()
            if clave == "componentes" and not valor:
                # La cabecera de la lista NO es un escalar vacío: pisarla borraría la lista
                # que las líneas siguientes van a llenar.
                continue
            datos[clave] = valor
    return datos


def _remoto_de(directorio):
    """`(estado, remoto)`, con `estado` en `leido` · `no-es-repo` · `impedido`."""
    try:
        entradas = os.listdir(directorio)
    except PermissionError:
        return "impedido", ""
    except OSError:
        return "no-es-repo", ""
    if ".git" not in entradas:
        return "no-es-repo", ""
    entorno = dict(_ENTORNO_BASE)
    entorno["PATH"] = os.environ.get("PATH", "/usr/bin:/bin")
    entorno["HOME"] = directorio
    proceso = subprocess.run(
        ["git", "-C", directorio, "config", "--get", "remote.origin.url"],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, env=entorno, check=False,
    )
    if proceso.returncode == 128:
        return "impedido", proceso.stderr.decode("utf-8", "replace").strip()
    if proceso.returncode != 0:
        return "no-es-repo", ""
    return "leido", proceso.stdout.decode("utf-8", "replace").strip()


def resolver_control_repo(abierto_en, puntero, *,
                          profundidad_maxima=PROFUNDIDAD_POR_DEFECTO):
    """Los CUATRO desenlaces de §6.7, cada uno con su diagnóstico DISTINTO."""
    buscado = normalizar_remoto((puntero or {}).get("remoto_canonico", ""))
    candidatos = []
    impedidos = []
    directorio = os.path.realpath(abierto_en)
    for _ in range(profundidad_maxima):
        padre = os.path.dirname(directorio)
        if padre == directorio:
            break
        try:
            hermanos = sorted(os.listdir(padre))
        except PermissionError as fallo:
            impedidos.append({"directorio": os.path.basename(padre),
                              "causa": fallo.strerror})
            break
        for nombre in hermanos:
            hermano = os.path.join(padre, nombre)
            if not os.path.isdir(hermano) or os.path.realpath(hermano) == directorio:
                continue
            estado, remoto = _remoto_de(hermano)
            if estado == "impedido":
                impedidos.append({"directorio": nombre, "causa": remoto or "sin permiso"})
                continue
            if estado != "leido":
                continue
            if buscado and normalizar_remoto(remoto) == buscado:
                candidatos.append(hermano)
        directorio = padre
    if len(candidatos) > 1:
        return {"desenlace": DOS,
                "candidatos": [os.path.basename(c) for c in candidatos],
                "diagnostico": ("DOS control repos para el mismo producto: es exactamente "
                                "el defecto que el puntero existe para no crear"),
                "buscado": buscado}
    if len(candidatos) == 1:
        return {"desenlace": ENCONTRADO, "control_repo": candidatos[0],
                "diagnostico": "", "buscado": buscado}
    if impedidos:
        return {"desenlace": NO_SE_PUDO, "impedimentos": impedidos,
                "diagnostico": ("hay directorios que NO SE PUDIERON comprobar: esto no es "
                                "ausencia, es IMPEDIMENTO, y son dos causas distintas"),
                "buscado": buscado}
    return {"desenlace": NO_ENCONTRADO,
            "diagnostico": ("no se encontró ningún hermano con el remoto canónico, y NO "
                            "se adivina"),
            "buscado": buscado}
