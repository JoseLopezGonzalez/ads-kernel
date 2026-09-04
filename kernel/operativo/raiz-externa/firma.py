"""firma — la FIRMA ASIMÉTRICA de la raíz externa, delegada en `ssh-keygen -Y`. `O25` §5.

`O25` §5: «`F6` utilizará criptografía estándar y una biblioteca o proveedor mantenido. **No
implementará primitivas criptográficas propias.**» Aquí no hay ni una línea de criptografía:
hay una FRONTERA con la herramienta estándar del anfitrión.

DECISIÓN · `ssh-keygen -Y sign` / `-Y verify` con **Ed25519**, y no HMAC
    Alternativas: (a) HMAC-SHA256 de `hmac`, que es lo que usa el anfitrión de PRUEBAS de
    `identidad/`; (b) `gpg`; (c) `openssl`; (d) `ssh-keygen -Y`.
    Se elige (d), y (a) queda EXPRESAMENTE DESCARTADA para la raíz externa: **HMAC es
    simétrico, luego quien verifica puede firmar**. Con eso, el veredicto externo lo puede
    fabricar cualquiera que pueda comprobarlo, y toda la demostración de `V6-16` se cae: la
    propiedad que se persigue es «verificar SIN poder firmar».
    Frente a (b), `gpg` arrastra un anillo de claves con estado propio, agente y caducidades,
    y su superficie de configuración es mucho mayor para el mismo resultado. Frente a (c),
    `openssl` obligaría a elegir formato de codificación y de empaquetado a mano —es decir, a
    escribir protocolo—; `ssh-keygen -Y` trae un formato firmado con NAMESPACE y un fichero
    de firmantes autorizados ya definidos, que es exactamente el vocabulario que `O25` §3
    necesita: «la configuración externa de confianza establece la identidad o huella pública
    aceptada».

DECISIÓN · la firma viaja en HEXADECIMAL sobre el protocolo que `identidad/` ya define
    `identidad/proveedor.py` habla con el anfitrión así: entra el mensaje por la entrada
    estándar, sale la firma en hexadecimal por la salida estándar. La firma de `ssh-keygen`
    es texto blindado (`-----BEGIN SSH SIGNATURE-----`). Se transporta codificando ESE TEXTO
    en hexadecimal, sin tocar un byte de su contenido.
    Alternativas: (a) cambiar el protocolo de `identidad/proveedor.py` para admitir texto;
    (b) codificar el texto blindado.
    Se elige (b). (a) obligaría a tocar un módulo que ya está construido y probado, para
    ganar legibilidad en un valor que nadie lee a mano.

DECISIÓN · el fichero de firmantes se construye QUITANDO el comentario de la clave pública
    Un `.pub` de OpenSSH es `<tipo> <base64> <comentario>`, y un `allowed_signers` es
    `<principal> <tipo> <base64>`. Pegar la línea entera hace que el comentario se lea como
    una OPCIÓN del firmante y `ssh-keygen` responda «bad options: unknown key option». Se
    construye campo a campo, y una prueba comprueba que el fichero resultante verifica.

DECISIÓN · la disponibilidad se COMPRUEBA antes de correr, y su ausencia es FALLO CERRADO
    `O25` §2 termina con «la ausencia de un proveedor válido provoca fallo cerrado». Aquí eso
    significa que si `ssh-keygen` no está, o no soporta `-Y`, o la clave no está donde la
    configuración dice, **no se emite veredicto favorable**: se levanta el error tipado.

DECISIÓN · la versión de OpenSSH y el algoritmo se REGISTRAN en la evidencia
    Una dependencia externa sin versión registrada no es reproducible. `capacidades()`
    publica la versión que `ssh -V` declara y el algoritmo usado, y la atestación los lleva
    dentro de lo que se firma.
"""

# ---------------------------------------------------------------------------
#  ADVERTENCIA DE FORMA · este módulo NO lleva línea de intérprete, y es deliberado.
#
#  `ADJ-B2` obligó a que los puntos ejecutables de la raíz externa se INVENTARÍEN de forma
#  mecánica en vez de por una lista escrita a mano —una lista escrita a mano fue exactamente lo
#  que dejó a este paquete fuera del alcance de `T306`—. El criterio derivado es una
#  equivalencia de tres términos que `T330` comprueba sobre el disco:
#
#      lleva `#!`   ⟺   define `if __name__ == "__main__":`   ⟺   lleva el prólogo `E-10`
#
#  Un módulo que se importa y no se ejecuta no cumple los dos últimos, así que tampoco puede
#  llevar el primero: una línea de intérprete en un módulo lo presenta como ejecutable, y a un
#  ejecutable esta equivalencia le exige la purga. Se retira la línea, y con ella la ambigüedad.
# ---------------------------------------------------------------------------

from __future__ import annotations

import os
import re
import shutil
import subprocess

from errores import (
    ClaveNoDisponible,
    FirmaNoVerificada,
    ProveedorDeFirmaAusente,
)

ALGORITMO = "ssh-ed25519"
TIPO_DE_CLAVE = "ed25519"
ESPACIO_DE_NOMBRES = "ads-atestacion-de-raiz-externa"
LIMITE_DE_ESPERA = 60.0

_PATRON_DE_VERSION = re.compile(r"OpenSSH_[0-9][^ ,]*")


def _entorno():
    """Entorno construido ENTERO. `ssh-keygen -Y` no necesita nada de la sesión."""
    return {
        "PATH": os.environ.get("PATH", "/usr/bin:/bin"),
        "LC_ALL": "C",
        "LANG": "C",
        "TZ": "UTC",
        "HOME": os.environ.get("ADS_RAIZ_EXTERNA_HOME", "/nonexistent"),
        # Sin agente y sin `askpass`: una clave con frase de paso NO se desbloquea
        # interactivamente en una raíz externa. Si hiciera falta, es fallo cerrado.
        "SSH_ASKPASS": "/bin/false",
        "SSH_ASKPASS_REQUIRE": "never",
        "DISPLAY": "",
    }


def _correr(orden, entrada=None):
    try:
        return subprocess.run(
            orden, input=entrada, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
            env=_entorno(), timeout=LIMITE_DE_ESPERA, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise ProveedorDeFirmaAusente(
            "no se pudo invocar la herramienta de firma del anfitrión: "
            + type(exc).__name__
        ) from exc


def version_de_openssh():
    """La versión que el anfitrión declara. Se REGISTRA en la evidencia, no se interpreta."""
    if shutil.which("ssh") is None:
        return None
    proceso = _correr(["ssh", "-V"])
    texto = (proceso.stderr or proceso.stdout).decode("utf-8", "replace")
    casado = _PATRON_DE_VERSION.search(texto)
    return casado.group(0) if casado else None


def soporta_firma_de_ficheros():
    """¿Este `ssh-keygen` conoce `-Y`? Se pregunta a la herramienta, no a la versión."""
    if shutil.which("ssh-keygen") is None:
        return False
    proceso = _correr(["ssh-keygen", "-Y"])
    texto = (proceso.stderr or proceso.stdout).decode("utf-8", "replace")
    # Sin operación, `-Y` se queja de que le falta el argumento. Que se queje de ESO —y no
    # de que la opción no exista— es la prueba de que la conoce.
    return "requires an argument -- Y" in texto or "Y" in texto and "usage:" in texto


def capacidades():
    """Lo que este anfitrión ofrece para firmar. Sin esto no se emite veredicto favorable."""
    version = version_de_openssh()
    tiene = shutil.which("ssh-keygen") is not None
    soporta = soporta_firma_de_ficheros() if tiene else False
    return {
        "herramienta": "ssh-keygen",
        "presente": tiene,
        "version_de_openssh": version,
        "soporta_firma_de_ficheros": soporta,
        "algoritmo": ALGORITMO,
        "espacio_de_nombres": ESPACIO_DE_NOMBRES,
        "simetrica": False,
        "motivo_de_asimetria": (
            "quien verifica NO puede firmar: el verificador sólo tiene el fichero de "
            "firmantes autorizados, que contiene claves PÚBLICAS"
        ),
        "disponible": bool(tiene and soporta),
    }


def exigir_proveedor():
    """`O25` §2: sin proveedor válido, FALLO CERRADO. No hay ruta por defecto que firme."""
    informe = capacidades()
    if not informe["disponible"]:
        raise ProveedorDeFirmaAusente(
            "el anfitrión no ofrece `ssh-keygen` con firma de ficheros (`-Y`): sin "
            "proveedor válido NO se emite veredicto favorable"
        )
    return informe


# ---------------------------------------------------------------------------
#  claves y firmantes autorizados
# ---------------------------------------------------------------------------
def generar_par_efimero(directorio, nombre, *, comentario="ads-raiz-externa"):
    """Genera un par Ed25519 EFÍMERO fuera de todo repositorio. `O25` §5, sólo en pruebas.

    `-N ''` y entrada estándar cerrada: sin las dos cosas, `ssh-keygen` pide la frase de paso
    por el terminal y el proceso se queda colgado para siempre.
    """
    exigir_proveedor()
    os.makedirs(directorio, exist_ok=True)
    privada = os.path.join(directorio, nombre)
    for residuo in (privada, privada + ".pub"):
        if os.path.exists(residuo):
            os.remove(residuo)
    proceso = subprocess.run(
        ["ssh-keygen", "-t", TIPO_DE_CLAVE, "-f", privada, "-N", "", "-C", comentario,
         "-q"],
        stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        env=_entorno(), timeout=LIMITE_DE_ESPERA, check=False,
    )
    if proceso.returncode != 0 or not os.path.isfile(privada):
        raise ProveedorDeFirmaAusente(
            "no se pudo generar el par de claves efímero (código "
            + str(proceso.returncode) + "). Su salida de error NO se publica"
        )
    os.chmod(privada, 0o600)
    return privada, privada + ".pub"


def huella_publica(ruta_publica):
    """La huella `SHA256:` de una clave pública. Es lo que la configuración externa ancla."""
    proceso = _correr(["ssh-keygen", "-l", "-f", ruta_publica])
    if proceso.returncode != 0:
        raise ClaveNoDisponible(
            "no se pudo leer la huella de una clave pública",
            ruta=os.path.basename(ruta_publica))
    partes = proceso.stdout.decode("ascii", "replace").split()
    for parte in partes:
        if parte.startswith("SHA256:"):
            return parte
    raise ClaveNoDisponible("la salida de `ssh-keygen -l` no trae huella `SHA256:`")


def linea_de_firmante(principal, ruta_publica):
    """`<principal> <tipo> <base64>`. SIN el comentario del `.pub`, que no es una opción."""
    with open(ruta_publica, encoding="ascii") as manejador:
        campos = manejador.read().split()
    if len(campos) < 2:
        raise ClaveNoDisponible(
            "la clave pública no tiene la forma `<tipo> <base64> [comentario]`",
            ruta=os.path.basename(ruta_publica))
    return principal + " " + campos[0] + " " + campos[1] + "\n"


def escribir_firmantes(ruta, entradas):
    """Escribe el fichero de firmantes autorizados. `entradas` es `[(principal, .pub)]`."""
    cuerpo = "".join(linea_de_firmante(principal, publica)
                     for principal, publica in entradas)
    directorio = os.path.dirname(os.path.abspath(ruta))
    os.makedirs(directorio, exist_ok=True)
    with open(ruta, "w", encoding="ascii") as manejador:
        manejador.write(cuerpo)
    os.chmod(ruta, 0o644)
    return ruta


# ---------------------------------------------------------------------------
#  firmar y verificar
# ---------------------------------------------------------------------------
def firmar(mensaje, *, clave_privada, espacio_de_nombres=ESPACIO_DE_NOMBRES):
    """Firma `mensaje` (bytes) y devuelve el texto blindado de la firma, en bytes."""
    exigir_proveedor()
    if not os.path.isfile(clave_privada):
        raise ClaveNoDisponible(
            "la clave privada declarada por la configuración externa no está donde dice: "
            "sin clave NO se firma, y no se firma con otra cosa",
            ruta=os.path.basename(clave_privada))
    proceso = _correr(
        ["ssh-keygen", "-Y", "sign", "-f", clave_privada, "-n", espacio_de_nombres, "-"],
        entrada=mensaje,
    )
    if proceso.returncode != 0 or not proceso.stdout:
        # El `stderr` NO se publica: puede llevar la ruta de la clave o material del
        # anfitrión, y `O25` §2 prohíbe que eso aparezca en un error.
        raise ProveedorDeFirmaAusente(
            "el anfitrión no produjo firma (código " + str(proceso.returncode)
            + "). Su salida de error NO se publica, por si llevara material sensible"
        )
    return proceso.stdout


def verificar(mensaje, firma, *, firmantes, principal,
              espacio_de_nombres=ESPACIO_DE_NOMBRES):
    """Verifica la firma de `mensaje`. Devuelve `(bool, diagnóstico)`. NUNCA lanza por falso."""
    exigir_proveedor()
    if not os.path.isfile(firmantes):
        raise ClaveNoDisponible(
            "no está el fichero de firmantes autorizados: sin él no se puede aceptar "
            "ninguna identidad, y el fallo es CERRADO",
            ruta=os.path.basename(firmantes))
    import tempfile
    temporal = tempfile.mkdtemp(prefix="ads-firma-")
    ruta_de_firma = os.path.join(temporal, "atestacion.sig")
    try:
        with open(ruta_de_firma, "wb") as manejador:
            manejador.write(firma)
        proceso = _correr(
            ["ssh-keygen", "-Y", "verify", "-f", firmantes, "-I", principal,
             "-n", espacio_de_nombres, "-s", ruta_de_firma],
            entrada=mensaje,
        )
    finally:
        shutil.rmtree(temporal, ignore_errors=True)
    diagnostico = (proceso.stderr or proceso.stdout).decode("utf-8", "replace").strip()
    return proceso.returncode == 0, diagnostico


def exigir_firma_valida(mensaje, firma, *, firmantes, principal,
                        espacio_de_nombres=ESPACIO_DE_NOMBRES):
    """La forma de fallo CERRADO: una firma que no verifica NO produce veredicto."""
    valida, diagnostico = verificar(mensaje, firma, firmantes=firmantes,
                                    principal=principal,
                                    espacio_de_nombres=espacio_de_nombres)
    if not valida:
        raise FirmaNoVerificada(
            "la atestación NO verifica contra los firmantes autorizados: " + diagnostico
        )
    return True
