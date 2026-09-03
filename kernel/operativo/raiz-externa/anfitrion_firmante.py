#!/usr/bin/env python3
"""anfitrion_firmante — el ANFITRIÓN DE FIRMA de la raíz externa. `O25` §2.

Es la mitad PRIVADA de la frontera que `identidad/proveedor.py` define: entra el mensaje por
la entrada estándar, sale la firma en hexadecimal por la salida estándar, y **la clave privada
no cruza en ningún sentido**. El proceso que pide la firma nunca la ve.

    anfitrion_firmante.py firmar <identidad>      < mensaje   > firma en hexadecimal

La clave se localiza por la variable `ADS_ANFITRION_ALMACEN`, que es la que `O25` §2 reserva
al proveedor de secretos del anfitrión y la única que `identidad/proveedor.py` traslada al
proceso externo. Aquí apunta a un fichero de clave Ed25519 con permisos `0600`; en una
instalación productiva apuntaría a lo que el anfitrión ofrezca.

DECISIÓN · este programa se NIEGA a verificar, y no es una omisión
    Alternativas: (a) que el mismo programa firme y verifique; (b) que sólo firme.
    Se elige (b). El sentido entero de `V6-16` es que quien VERIFICA no pueda FIRMAR. Un
    programa que hiciera las dos cosas volvería a juntar los dos poderes en un único binario
    y en una única ruta, y bastaría con poder ejecutarlo para fabricar veredictos. Verificar
    es de `anfitrion_verificador.py`, que sólo tiene claves PÚBLICAS.

DECISIÓN · ni un byte de la clave sale por ninguna salida
    `O25` §2: la clave «no aparecerá en estado, diarios, evidencia, configuración exportada,
    logs o errores». Los diagnósticos de este programa nombran la CAUSA y nunca el material,
    y tampoco publican la ruta absoluta del almacén.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import firma as modulo_de_firma                                      # noqa: E402
from errores import ErrorDeRaizExterna                               # noqa: E402

VARIABLE_DEL_ALMACEN = "ADS_ANFITRION_ALMACEN"


def main(argv=None):
    argumentos = list(sys.argv[1:] if argv is None else argv)
    if not argumentos:
        sys.stderr.write("uso: anfitrion_firmante.py firmar <identidad>\n")
        return 2
    accion = argumentos[0]
    if accion != "firmar":
        # `verificar` NO se atiende aquí, y el código de salida lo dice sin ambigüedad.
        sys.stderr.write(
            "este anfitrion SOLO firma. Verificar es de anfitrion_verificador.py, que no "
            "tiene clave privada\n"
        )
        return 4
    almacen = os.environ.get(VARIABLE_DEL_ALMACEN)
    if not almacen or not os.path.isfile(almacen):
        sys.stderr.write(
            "el almacen de claves del anfitrion no esta disponible: sin proveedor valido "
            "no se firma con nada\n"
        )
        return 3
    mensaje = sys.stdin.buffer.read()
    try:
        blindada = modulo_de_firma.firmar(mensaje, clave_privada=almacen)
    except ErrorDeRaizExterna as error:
        sys.stderr.write(str(error) + "\n")
        return 3
    sys.stdout.write(blindada.hex())
    return 0


if __name__ == "__main__":
    sys.exit(main())
