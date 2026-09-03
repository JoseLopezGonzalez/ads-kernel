#!/usr/bin/env python3
"""anfitrion_verificador — la mitad PÚBLICA de la frontera de firma. `O25` §3 y §4.

    anfitrion_verificador.py --firmantes <fichero> verificar <identidad> <firma-hex>
        < mensaje    >  `valida` | `invalida`

**No tiene clave privada, y no puede tenerla**: lo único que lee es el fichero de FIRMANTES
AUTORIZADOS, que contiene claves PÚBLICAS. Ésa es la asimetría que `V6-16` necesita y que un
HMAC no puede dar: quien verifica NO puede firmar.

DECISIÓN · el fichero de firmantes llega por ARGUMENTO de la configuración externa, no por
           variable de entorno ni por convención
    `O25` §3: «la configuración externa de confianza establece la identidad o huella pública
    aceptada» y «el repositorio verificado no puede cambiar por sí mismo qué identidad acepta
    la raíz externa». Una ruta por convención la puede plantar el árbol; una ruta que viaja en
    el campo `orden_de_verificacion` de la configuración externa, no.

DECISIÓN · la respuesta es `valida` o `invalida`, y nunca un tercer valor
    Es el protocolo que `identidad/proveedor.py` ya define y consume. Cualquier otra salida
    —incluida la vacía— la lee ese módulo como NO válida, que es el sentido correcto del
    fallo por omisión.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import firma as modulo_de_firma                                      # noqa: E402
from errores import ErrorDeRaizExterna                               # noqa: E402


def main(argv=None):
    argumentos = list(sys.argv[1:] if argv is None else argv)
    firmantes = None
    while argumentos and argumentos[0] == "--firmantes":
        if len(argumentos) < 2:
            sys.stderr.write("uso: --firmantes <fichero>\n")
            return 2
        firmantes = argumentos[1]
        argumentos = argumentos[2:]
    if len(argumentos) < 3 or argumentos[0] != "verificar":
        sys.stderr.write(
            "uso: anfitrion_verificador.py --firmantes <fichero> verificar <identidad> "
            "<firma-hex>\n"
        )
        return 2
    identidad = argumentos[1]
    try:
        blindada = bytes.fromhex(argumentos[2])
    except ValueError:
        sys.stdout.write("invalida")
        return 0
    if not firmantes or not os.path.isfile(firmantes):
        sys.stderr.write(
            "no esta el fichero de firmantes autorizados que la configuracion externa "
            "declara: sin el no se acepta ninguna identidad\n"
        )
        return 3
    mensaje = sys.stdin.buffer.read()
    try:
        valida, _ = modulo_de_firma.verificar(
            mensaje, blindada, firmantes=firmantes, principal=identidad)
    except ErrorDeRaizExterna as error:
        sys.stderr.write(str(error) + "\n")
        return 3
    sys.stdout.write("valida" if valida else "invalida")
    return 0


if __name__ == "__main__":
    sys.exit(main())
