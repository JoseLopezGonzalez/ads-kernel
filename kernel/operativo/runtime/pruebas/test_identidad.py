#!/usr/bin/env python3
"""test_identidad — batería de la IDENTIDAD DE FIRMA EXTERNA. Escenario `T192`.

Instancia `O25` y lo comprueba punto por punto:

    §2  custodia en el ANFITRIÓN, y FALLO CERRADO sin proveedor válido
    §3  la configuración externa establece la identidad aceptada, y el repositorio
        verificado NO puede cambiar por sí mismo cuál es
    §5  rotación, solapamiento EXPLÍCITO, activa · retirada · revocada, rechazo de
        desconocida y de revocada, y trazabilidad SIN revelación de secretos

Y la prueba que las cubre todas a la vez: un MARCADOR SECRETO ÚNICO se inyecta como material
de clave, se ejerce el aparato entero —firmar, verificar, rotar, revocar, fallar— y se
comprueba que el marcador no aparece en NINGUNA salida, ni en el estado, ni en el diario, ni
en la evidencia, ni en la configuración exportada, ni en ningún error.

**FUERA DE ALCANCE, declarado:** un proveedor productivo de claves concreto. `O25` §2 lo deja
al anfitrión y §6 del contrato del macrobloque lo excluye. El anfitrión de estas pruebas usa
HMAC-SHA256 de la biblioteca estándar, que es SIMÉTRICO: quien verifica puede firmar. Una
raíz externa de verdad necesita lo contrario, y eso lo aporta el anfitrión, no este paquete.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import sys
import tempfile
import unittest

RAIZ_RUNTIME = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, RAIZ_RUNTIME)

import estado                                                        # noqa: E402
import identidad                                                     # noqa: E402
from identidad import rotacion                                       # noqa: E402


class _RunnerDeterminista(unittest.TextTestRunner):
    """Igual que el corriente, pero sin la duración en el resumen.

    COPIADO de `tooling/tests/test_workspace.py`, no importado: la salida se PUBLICA como
    evidencia y tiene que ser byte-idéntica entre ejecuciones.
    """

    def run(self, test):
        import io as _io
        buffer = _io.StringIO()
        real, self.stream = self.stream, unittest.runner._WritelnDecorator(buffer)
        try:
            resultado = super().run(test)
        finally:
            self.stream = real
        real.write(re.sub(r"Ran (\d+) tests? in [\d.]+s",
                          r"Ran \1 tests  (duración no registrada: varía por ejecución)",
                          buffer.getvalue()))
        return resultado


# El anfitrión de PRUEBAS. Vive FUERA del árbol verificado, lee la clave de su propio almacén
# —que este proceso nunca abre— y devuelve sólo la firma. Es la frontera de `O25` §2.
ANFITRION = '''#!{interprete}
"""Anfitrión de firma de PRUEBAS. NO es custodia productiva (`O25` §2)."""
import hashlib
import hmac
import os
import sys

almacen = os.environ.get("ADS_ANFITRION_ALMACEN")
if not almacen or not os.path.isfile(almacen):
    sys.stderr.write("el almacen de claves del anfitrion no esta disponible\\n")
    sys.exit(3)
with open(almacen, "rb") as manejador:
    clave = manejador.read()

accion = sys.argv[1] if len(sys.argv) > 1 else ""
nombre = sys.argv[2] if len(sys.argv) > 2 else ""
datos = sys.stdin.buffer.read()
mac = hmac.new(clave + nombre.encode("utf-8"), datos, hashlib.sha256).hexdigest()
if accion == "firmar":
    sys.stdout.write(mac)
elif accion == "verificar":
    esperada = sys.argv[3] if len(sys.argv) > 3 else ""
    sys.stdout.write("valida" if hmac.compare_digest(mac, esperada) else "invalida")
else:
    sys.stderr.write("accion desconocida\\n")
    sys.exit(2)
'''


def huella_publica(clave, nombre):
    """La huella PÚBLICA de una identidad: digest de la clave, nunca la clave."""
    return hashlib.sha256(b"ads.identidad\x00" + clave + nombre.encode("utf-8")).hexdigest()


class BaseDeIdentidad(unittest.TestCase):
    """Un árbol verificado, un almacén de claves FUERA de él, y un anfitrión de firma."""

    MARCADOR = "MARCADOR-SECRETO-UNICO-9f3c1a7e5b2d4086"

    def setUp(self):
        self.directorio = tempfile.mkdtemp(prefix="ads-idn-")
        self.addCleanup(shutil.rmtree, self.directorio, True)
        self.arbol = os.path.join(self.directorio, "arbol")
        self.fuera = os.path.join(self.directorio, "fuera")
        os.makedirs(self.arbol)
        os.makedirs(self.fuera)

        # La clave lleva el MARCADOR dentro. Vive fuera del árbol y este proceso no la lee.
        self.clave = ("clave-de-pruebas-" + self.MARCADOR).encode("utf-8")
        self.almacen_de_claves = os.path.join(self.fuera, "clave.bin")
        with open(self.almacen_de_claves, "wb") as manejador:
            manejador.write(self.clave)
        os.chmod(self.almacen_de_claves, 0o600)
        os.environ["ADS_ANFITRION_ALMACEN"] = self.almacen_de_claves
        self.addCleanup(os.environ.pop, "ADS_ANFITRION_ALMACEN", None)

        self.anfitrion = os.path.join(self.fuera, "anfitrion-de-firma.py")
        with open(self.anfitrion, "w", encoding="utf-8") as manejador:
            manejador.write(ANFITRION.format(interprete=sys.executable))
        os.chmod(self.anfitrion, 0o755)

        self.huella_a = huella_publica(self.clave, "idn-a")
        self.huella_b = huella_publica(self.clave, "idn-b")
        self.configuracion = self._escribir_configuracion(self.fuera)

    def _texto_de_configuracion(self, identidades=None):
        identidades = identidades or (
            "  - id: idn-a\n"
            "    algoritmo: hmac-sha256\n"
            "    huella_publica: " + self.huella_a + "\n"
            "    estado: activa\n"
            "    epoca_de_alta: 1\n"
            "    solapamiento: 2\n"
        )
        return (
            "version: 1\n"
            "autoridad: raiz-externa-de-confianza\n"
            "epoca_vigente: 3\n"
            "orden_de_firma: [" + self.anfitrion + "]\n"
            "identidades:\n" + identidades +
            "ancla:\n"
            "  base: " + ("0" * 40) + "\n"
            "admitidas:\n"
            "  - ruta: docs/canonico/nueva.md\n"
            "    motivo: alta declarada por la autoridad externa\n"
        )

    def _escribir_configuracion(self, carpeta, identidades=None):
        ruta = os.path.join(carpeta, "CONFIANZA.yml")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(self._texto_de_configuracion(identidades))
        return ruta

    def cargar(self):
        return identidad.cargar(self.configuracion, arbol_verificado=self.arbol)


# ===========================================================================
#  `O25` §3 · la configuración vive FUERA, y el árbol no la puede cambiar
# ===========================================================================
class ConfiguracionExterna(BaseDeIdentidad):

    def test_una_configuracion_dentro_del_arbol_se_rechaza(self):
        """T192 · Defecto que previene: que el repositorio decida quién lo verifica."""
        dentro = self._escribir_configuracion(self.arbol)
        with self.assertRaises(identidad.ConfiguracionDentroDelArbol) as capturado:
            identidad.cargar(dentro, arbol_verificado=self.arbol)
        self.assertIn("`O25` §3", str(capturado.exception))

    def test_un_enlace_simbolico_no_la_cuela_dentro(self):
        """T192 · Defecto que previene: meterla dentro con una ruta que no lo parece."""
        objetivo = os.path.join(self.arbol, "config")
        os.makedirs(objetivo)
        dentro = self._escribir_configuracion(objetivo)
        enlace = os.path.join(self.directorio, "atajo")
        os.symlink(objetivo, enlace)
        with self.assertRaises(identidad.ConfiguracionDentroDelArbol):
            identidad.cargar(os.path.join(enlace, "CONFIANZA.yml"),
                             arbol_verificado=self.arbol)
        self.assertTrue(os.path.isfile(dentro))

    def test_manipular_la_configuracion_dentro_del_arbol_no_cambia_el_veredicto(self):
        """T192 · Defecto que previene: `O25` §3, cambiar desde dentro qué identidad se acepta."""
        configuracion = self.cargar()
        antes = configuracion.exportar()
        # El atacante escribe DENTRO del árbol una configuración con otra identidad y otra
        # ancla. La autoridad no cambia: la que manda es la de fuera.
        self._escribir_configuracion(
            self.arbol,
            identidades=("  - id: idn-del-atacante\n"
                         "    algoritmo: hmac-sha256\n"
                         "    huella_publica: " + ("f" * 64) + "\n"
                         "    estado: activa\n"
                         "    epoca_de_alta: 1\n"),
        )
        despues = self.cargar().exportar()
        self.assertEqual(antes, despues)
        self.assertEqual([i["id"] for i in despues["identidades"]], ["idn-a"])

    def test_una_configuracion_sin_identidades_falla_cerrado(self):
        """T192 · Defecto que previene: verificar contra un anillo vacío y decir que sí."""
        ruta = os.path.join(self.fuera, "vacia.yml")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write("version: 1\nautoridad: x\norden_de_firma: [/bin/true]\n"
                            "identidades:\nancla:\n  base: x\n")
        with self.assertRaises(identidad.ConfiguracionInvalida):
            identidad.cargar(ruta, arbol_verificado=self.arbol)

    def test_una_configuracion_con_clave_privada_dentro_se_rechaza_entera(self):
        """T192 · Defecto que previene: `O25` §2, la clave en la configuración."""
        ruta = self._escribir_configuracion(
            self.fuera,
            identidades=("  - id: idn-a\n"
                         "    algoritmo: hmac-sha256\n"
                         "    huella_publica: " + self.huella_a + "\n"
                         "    estado: activa\n"
                         "    epoca_de_alta: 1\n"
                         "    clave_privada: no-deberia-estar-aqui\n"),
        )
        with self.assertRaises(identidad.ConfiguracionInvalida) as capturado:
            identidad.cargar(ruta, arbol_verificado=self.arbol)
        self.assertIn("huella pública", str(capturado.exception))

    def test_la_declaracion_de_admision_viene_de_la_configuracion_externa(self):
        """T192 · Defecto que previene: que el árbol escriba su propia declaración."""
        declaracion = self.cargar().declaracion()
        self.assertEqual(declaracion.autoridad, "raiz-externa-de-confianza")
        self.assertEqual(declaracion.rutas(), ("docs/canonico/nueva.md",))
        self.assertEqual(declaracion.ancla, "0" * 40)


# ===========================================================================
#  `O25` §2 · custodia en el anfitrión, y fallo cerrado
# ===========================================================================
class ProveedorDelegado(BaseDeIdentidad):

    def test_firma_y_verifica_delegando_en_el_anfitrion(self):
        """T192 · Control POSITIVO: el circuito completo, sin que el proceso vea la clave."""
        proveedor = identidad.ProveedorProductivo(self.cargar())
        firma = proveedor.firmar(b"contenido que se firma")
        self.assertTrue(proveedor.verificar(b"contenido que se firma", firma))
        self.assertFalse(proveedor.verificar(b"otro contenido", firma))
        self.assertTrue(proveedor.identidad().startswith("hmac-sha256:idn-a:"))

    def test_reutiliza_la_interfaz_del_motor_y_no_la_duplica(self):
        """T192 · Defecto que previene: una segunda sede de la interfaz de firma."""
        proveedor = identidad.ProveedorProductivo(self.cargar())
        self.assertIsInstance(proveedor, estado.ProveedorDeFirma)

    def test_sin_proveedor_valido_falla_cerrado(self):
        """T192 · Defecto que previene: `O25` §2, una ruta por defecto que firme con nada."""
        with self.assertRaises(identidad.SinProveedorDeIdentidad):
            identidad.ProveedorProductivo(None)
        with self.assertRaises(identidad.SinProveedorDeIdentidad):
            identidad.exigir_proveedor(None)
        with self.assertRaises(identidad.SinProveedorDeIdentidad):
            identidad.exigir_proveedor(object())

    def test_un_anfitrion_que_no_existe_es_fallo_cerrado(self):
        """T192 · Defecto que previene: degradar a una firma local cuando el anfitrión no está."""
        ruta = os.path.join(self.fuera, "sin-anfitrion.yml")
        with open(ruta, "w", encoding="utf-8") as manejador:
            manejador.write(self._texto_de_configuracion().replace(
                self.anfitrion, os.path.join(self.fuera, "no-existe")))
        configuracion = identidad.cargar(ruta, arbol_verificado=self.arbol)
        with self.assertRaises(identidad.SinProveedorDeIdentidad) as capturado:
            identidad.ProveedorProductivo(configuracion)
        self.assertIn("no se firma con nada", str(capturado.exception))

    def test_un_anfitrion_que_falla_no_degrada_a_una_firma_propia(self):
        """T192 · Defecto que previene: evidencia firmada por una autoridad que nadie aceptó."""
        proveedor = identidad.ProveedorProductivo(self.cargar())
        os.environ.pop("ADS_ANFITRION_ALMACEN")
        try:
            with self.assertRaises(identidad.AnfitrionNoResponde) as capturado:
                proveedor.firmar(b"algo")
        finally:
            os.environ["ADS_ANFITRION_ALMACEN"] = self.almacen_de_claves
        self.assertNotIn("clave", str(capturado.exception).lower().split("no se publica")[0])
        self.assertIn("NO se publica", str(capturado.exception))

    def test_el_proveedor_no_publica_su_ruta_absoluta(self):
        """T192 · Defecto que previene: publicar el árbol de directorios de quien ejecuta."""
        proveedor = identidad.ProveedorProductivo(self.cargar())
        texto = json.dumps(proveedor.a_dict(), sort_keys=True, ensure_ascii=False)
        self.assertNotIn(self.directorio, texto)
        self.assertEqual(proveedor.a_dict()["anfitrion"], "anfitrion-de-firma.py")


# ===========================================================================
#  `O25` §5 · rotación, solapamiento, retirada y revocación
# ===========================================================================
class RotacionYSolapamiento(BaseDeIdentidad):

    def _anillo(self):
        return self.cargar().anillo()

    def test_una_identidad_desconocida_se_rechaza(self):
        """T192 · Defecto que previene: aceptar una identidad que la autoridad no declaró."""
        anillo = self._anillo()
        with self.assertRaises(identidad.IdentidadDesconocida) as capturado:
            anillo.exigir_valida("idn-del-atacante", 3)
        self.assertIn("no puede añadirla", str(capturado.exception))

    def test_rotar_retira_la_activa_con_solapamiento_explicito_en_epocas(self):
        """T192 · Control POSITIVO: `O25` §5, la rotación con periodo de solapamiento."""
        anillo = self._anillo()
        nueva = rotacion.Identidad(
            identificador="idn-b", algoritmo="hmac-sha256",
            huella_publica=self.huella_b, estado=rotacion.ACTIVA, epoca_de_alta=1,
        )
        informe = anillo.rotar(nueva=nueva, motivo="rotacion programada", solapamiento=2)
        self.assertEqual(informe["saliente"]["estado"], rotacion.RETIRADA)
        self.assertEqual(informe["entrante"]["estado"], rotacion.ACTIVA)
        self.assertEqual(informe["solapamiento"], 2)
        self.assertEqual(anillo.activa().id, "idn-b")

    def test_una_retirada_verifica_dentro_del_solapamiento_y_no_fuera(self):
        """T192 · Defecto que previene: un solapamiento declarado que no se ejecuta."""
        anillo = self._anillo()
        anillo.rotar(
            nueva=rotacion.Identidad(identificador="idn-b", algoritmo="hmac-sha256",
                                     huella_publica=self.huella_b,
                                     estado=rotacion.ACTIVA, epoca_de_alta=1),
            motivo="rotacion", solapamiento=2,
        )
        retirada = anillo.obtener("idn-a")
        limite = retirada.epoca_de_retirada + retirada.solapamiento
        self.assertIs(anillo.exigir_valida("idn-a", limite), retirada)
        with self.assertRaises(identidad.IdentidadFueraDeSolapamiento) as capturado:
            anillo.exigir_valida("idn-a", limite + 1)
        self.assertIn("verifica hasta la " + str(limite), str(capturado.exception))

    def test_una_revocada_no_verifica_ni_dentro_del_solapamiento(self):
        """T192 · Defecto que previene: honrar el solapamiento de una clave comprometida."""
        anillo = self._anillo()
        anillo.revocar("idn-a", motivo="clave comprometida")
        revocada = anillo.obtener("idn-a")
        with self.assertRaises(identidad.IdentidadRevocada) as capturado:
            anillo.exigir_valida("idn-a", revocada.epoca_de_retirada)
        self.assertIn("su solapamiento no se honra", str(capturado.exception))

    def test_los_tres_estados_y_ninguno_mas(self):
        """T192 · Defecto que previene: un estado inventado que nadie sabe qué significa."""
        self.assertEqual(rotacion.ESTADOS, ("activa", "retirada", "revocada"))
        with self.assertRaises(identidad.ConfiguracionInvalida):
            rotacion.Identidad(identificador="x", algoritmo="a", huella_publica="h",
                               estado="caducada", epoca_de_alta=1)

    def test_una_retirada_sin_epoca_de_retirada_se_rechaza(self):
        """T192 · Defecto que previene: un solapamiento que no se puede medir."""
        with self.assertRaises(identidad.ConfiguracionInvalida) as capturado:
            rotacion.Identidad(identificador="x", algoritmo="a", huella_publica="h",
                               estado=rotacion.RETIRADA, epoca_de_alta=1)
        self.assertIn("solapamiento no se puede medir", str(capturado.exception))

    def test_la_traza_es_completa_y_no_lleva_secretos(self):
        """T192 · Defecto que previene: `O25` §5, trazabilidad que revela material."""
        anillo = self._anillo()
        anillo.rotar(
            nueva=rotacion.Identidad(identificador="idn-b", algoritmo="hmac-sha256",
                                     huella_publica=self.huella_b,
                                     estado=rotacion.ACTIVA, epoca_de_alta=1),
            motivo="rotacion programada", solapamiento=2,
        )
        anillo.revocar("idn-b", motivo="clave comprometida")
        traza = anillo.traza()
        self.assertEqual([apunte["acto"] for apunte in traza],
                         ["rotacion", "alta", "revocacion"])
        texto = json.dumps(traza, sort_keys=True, ensure_ascii=False)
        self.assertNotIn(self.MARCADOR, texto)
        self.assertIn(self.huella_a, texto)


# ===========================================================================
#  LA PRUEBA DE AUSENCIA DE SECRETOS
# ===========================================================================
class AusenciaDeSecretos(BaseDeIdentidad):
    """`O25` §2: la clave no aparece en estado, diarios, evidencia, configuración ni errores."""

    def _ejercer_el_aparato_entero(self):
        """Firma, verifica, atesta, rota, revoca y FALLA. Devuelve todo lo que produjo."""
        producido = []
        configuracion = self.cargar()
        proveedor = identidad.ProveedorProductivo(configuracion)

        producido.append(proveedor.identidad())
        producido.append(json.dumps(proveedor.a_dict(), sort_keys=True, ensure_ascii=False))
        producido.append(json.dumps(configuracion.exportar(), sort_keys=True,
                                    ensure_ascii=False))

        firma = proveedor.firmar(b"contenido que se firma")
        producido.append(firma.hex())
        producido.append(str(proveedor.verificar(b"contenido que se firma", firma)))

        # Un almacén de estado real, atestado con este proveedor. La evidencia va FUERA.
        repo = os.path.join(self.arbol, "control")
        os.makedirs(repo)
        almacen = estado.inicializar(repo)
        try:
            almacen.aplicar(estado.Transicion(
                tipo="alta", base=almacen.revision()["revision_id"],
                operaciones=[estado.Escritura("items/it-1.json", {"titulo": "primero"})],
                autor="runtime-A", motivo="alta de prueba", id="tx-alta-1",
            ))
            destino = os.path.join(self.fuera, "evidencia.json")
            evidencia = estado.atestar(almacen, proveedor, destino)
            producido.append(json.dumps(evidencia, sort_keys=True, ensure_ascii=False))
            informe = estado.verificar_atestacion(destino, proveedor, almacen)
            producido.append(json.dumps(informe, sort_keys=True, ensure_ascii=False))
        finally:
            almacen.cerrar()

        anillo = configuracion.anillo()
        anillo.rotar(
            nueva=rotacion.Identidad(identificador="idn-b", algoritmo="hmac-sha256",
                                     huella_publica=self.huella_b,
                                     estado=rotacion.ACTIVA, epoca_de_alta=1),
            motivo="rotacion programada", solapamiento=2,
        )
        anillo.revocar("idn-b", motivo="clave comprometida")
        producido.append(json.dumps(anillo.a_dict(), sort_keys=True, ensure_ascii=False))

        # Y TODOS los fallos, que es donde un secreto se cuela más fácil.
        fallos = []
        for accion in (
            lambda: anillo.exigir_valida("idn-desconocida", 3),
            lambda: anillo.exigir_valida("idn-b", 9),
            lambda: anillo.exigir_valida("idn-a", 99),
            lambda: proveedor.firmar("no son bytes"),
            lambda: identidad.cargar(self._escribir_configuracion(self.arbol),
                                     arbol_verificado=self.arbol),
        ):
            try:
                accion()
            except identidad.ErrorDeIdentidad as error:
                fallos.append(str(error))
                fallos.append(json.dumps(error.a_dict(), sort_keys=True,
                                         ensure_ascii=False))
        self.assertEqual(len(fallos), 10, "los cinco fallos tienen que haberse producido")
        producido.extend(fallos)

        os.environ.pop("ADS_ANFITRION_ALMACEN")
        try:
            proveedor.firmar(b"algo")
        except identidad.AnfitrionNoResponde as error:
            producido.append(str(error))
        finally:
            os.environ["ADS_ANFITRION_ALMACEN"] = self.almacen_de_claves

        return producido, repo, os.path.join(self.fuera, "evidencia.json")

    def test_el_marcador_no_aparece_en_ninguna_salida(self):
        """T192 · Defecto que previene: `O25` §2, un secreto en un log, un error o la evidencia."""
        producido, repo, evidencia = self._ejercer_el_aparato_entero()
        self.assertGreater(len(producido), 15)
        for indice, texto in enumerate(producido):
            with self.subTest(salida=indice):
                self.assertNotIn(self.MARCADOR, texto)

        # El árbol ENTERO del estado: canónico, diario, reconciliación y operacional.
        revisados = 0
        for carpeta, _, ficheros in os.walk(repo):
            for nombre in ficheros:
                completa = os.path.join(carpeta, nombre)
                with open(completa, "rb") as manejador:
                    crudo = manejador.read()
                revisados += 1
                self.assertNotIn(self.MARCADOR.encode("utf-8"), crudo,
                                 "el marcador aparece en " + nombre)
        self.assertGreater(revisados, 3, "hay estado, diario y registro que revisar")

        with open(evidencia, "rb") as manejador:
            crudo = manejador.read()
        self.assertNotIn(self.MARCADOR.encode("utf-8"), crudo)

    def test_el_marcador_si_esta_en_la_clave_del_anfitrion(self):
        """T192 · Control del CONTROL: si el marcador no estuviera, la prueba no probaría nada."""
        with open(self.almacen_de_claves, "rb") as manejador:
            crudo = manejador.read()
        self.assertIn(self.MARCADOR.encode("utf-8"), crudo)

    def test_la_evidencia_no_puede_escribirse_dentro_del_arbol_verificado(self):
        """T192 · Defecto que previene: `g.13`, certificar un árbol cambiándolo al certificarlo."""
        repo = os.path.join(self.arbol, "control2")
        os.makedirs(repo)
        almacen = estado.inicializar(repo)
        self.addCleanup(almacen.cerrar)
        proveedor = identidad.ProveedorProductivo(self.cargar())
        with self.assertRaises(estado.EvidenciaDentroDelArbol):
            estado.atestar(almacen, proveedor, os.path.join(repo, "evidencia.json"))


if __name__ == "__main__":
    unittest.main(verbosity=2, testRunner=_RunnerDeterminista)
