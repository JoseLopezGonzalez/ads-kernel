# RAÍZ EXTERNA DE CONFIANZA · paquete separado

**Esto NO es parte del runtime.** Vive fuera de `kernel/operativo/runtime/` a propósito, y
`instalar.py` lo copia a una instalación **fuera del árbol verificado**. Un verificador que
vive donde vive lo verificado no es externo, por muy bien escrito que esté — §11.8, literal.

Sedes: [`(g)` `g.15`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md) ·
[`O25`](../../../docs/owner/ADS-OWNER-RESOLUCIONES.md) ·
§11.8 y §20.1 `V6-16` de `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`.
Contrato derivado: [`CONTRATO-RAIZ-EXTERNA.md`](../runtime/CONTRATO-RAIZ-EXTERNA.md).

---

## Qué hay aquí

```text
verificador.py            PUNTO EJECUTABLE. `capacidades` · `procedencia` · `verificar` ·
                          `comprobar` · `instalacion`. Es un PROCESO aparte, no una función
                          del runtime
instalar.py               PUNTO EJECUTABLE. copia este paquete y las dependencias del
                          verificador a una instalación FUERA del árbol, con manifiesto de
                          SHA-256 por fichero. `--comprobar` · `--procedencia`
anfitrion_firmante.py     PUNTO EJECUTABLE. mitad PRIVADA de la frontera de firma. SÓLO firma
anfitrion_verificador.py  PUNTO EJECUTABLE. mitad PÚBLICA. SÓLO verifica, y no tiene clave
                          privada
firma.py                  módulo. frontera con `ssh-keygen -Y` y Ed25519. NO implementa
                          criptografía
atestacion.py             módulo. la atestación canónica, vinculada al SHA del commit y al
                          `tree`
aislamiento.py            módulo. la DEMOSTRACIÓN de que la identidad no puede escribir: lo
                          intenta
errores.py                módulo. jerarquía tipada propia; no importa la del árbol verificado
```

**La distinción PUNTO EJECUTABLE / módulo no es documental: es MECÁNICA.** `T330` la deriva
del disco con una equivalencia de tres términos, comprobada en los dos sentidos:

```text
lleva `#!`   ⟺   define `if __name__ == "__main__":`   ⟺   lleva el prólogo `E-10`
```

Por eso los cuatro módulos **no llevan línea de intérprete**, y por eso `instalar.py` sólo da
permiso de ejecución a los que la llevan. Es la corrección de `ADJ-B2`: hasta el 2026-09-04
este paquete no tenía **ni una línea de purga** y `T306` cubría cinco ejecutables escritos a
mano —los cinco `ads_*.py`— «y ninguno más». Con un `json.py` homónimo en `PYTHONPATH`,
`verificador.py capacidades` publicaba `{}` con código 0 e `instalar.py` escribía un
manifiesto de tres bytes sobre 41 ficheros instalados, también con código 0.

## Cómo se usa

```bash
# 1 · instalar FUERA del árbol verificado
python3 kernel/operativo/raiz-externa/instalar.py \
        --destino /opt/ads-raiz-externa --arbol /ruta/al/control-repo

# 2 · comprobar que la instalación no se ha tocado
python3 /opt/ads-raiz-externa/raiz-externa/verificador.py instalacion \
        --instalacion /opt/ads-raiz-externa

# 3 · emitir veredicto y ATESTACIÓN FIRMADA, con la evidencia FUERA del árbol
ADS_ANFITRION_ALMACEN=/ruta/fuera/de/todo/repo/clave \
python3 /opt/ads-raiz-externa/raiz-externa/verificador.py verificar \
        --repo /ruta/al/control-repo --base <sha> \
        --configuracion /ruta/fuera/confianza.yml \
        --evidencia /ruta/fuera/atestacion.json

# 4 · comprobar la atestación, SIN poder firmarla
python3 /opt/ads-raiz-externa/raiz-externa/verificador.py comprobar \
        --repo /ruta/al/control-repo \
        --configuracion /ruta/fuera/confianza.yml \
        --evidencia /ruta/fuera/atestacion.json
```

## La configuración externa de confianza

Vive **fuera del árbol verificado** —`identidad/configuracion.py` rechaza la que viva
dentro, por los dos caminos de resolución— y es quien establece la identidad aceptada
(`O25` §3). Su forma:

```yaml
version: 1
autoridad: raiz-externa-de-esta-instalacion
epoca_vigente: 1
orden_de_firma: [/opt/ads-raiz-externa/raiz-externa/anfitrion_firmante.py]
orden_de_verificacion: [/opt/ads-raiz-externa/raiz-externa/anfitrion_verificador.py, --firmantes, /ruta/fuera/allowed_signers]
identidades:
  - id: raiz-externa-1
    algoritmo: ssh-ed25519
    huella_publica: SHA256:...
    estado: activa
    epoca_de_alta: 1
ancla:
  base: <sha de la revisión base>
  digest_del_censo: <digest del censo de zonas>
admitidas: []
```

## La clave privada

`O25` §2: **fuera de todos los repositorios**, sin versionar, ausente de estado, diarios,
evidencia, configuración exportada, logs y errores, y **fallo cerrado sin proveedor válido**.
Este paquete nunca la abre: se la pide al anfitrión por la variable `ADS_ANFITRION_ALMACEN`,
que es la única que `identidad/proveedor.py` traslada al proceso externo.

Las **claves efímeras** que genera `firma.generar_par_efimero` están permitidas **únicamente
en pruebas** y **no constituyen custodia productiva** — `O25` §5, literal.

## Lo que este paquete NO hace

```text
NO ELIGE un proveedor de secretos productivo. `O25` §2 lo deja al anfitrión
NO DECLARA la raíz externa certificada. `O25` §6 lo dice de sí misma
NO DESBLOQUEA PesquerApp. `O24` §4 la mantiene bloqueada
NO SUSTITUYE al verificador interno: lo EJECUTA desde fuera, con otra identidad
```

## `E-17` · CUSTODIA PRODUCTIVA DE CLAVES — deuda EXTERNA, con dueño y con cierre

**Permanece ABIERTA y es EXTERNA.** Este apartado no la resuelve: la REGISTRA, que es lo
único que este paquete puede hacer con ella. Sedes: `O25` §5 y `O26` §4 de
`docs/owner/ADS-OWNER-RESOLUCIONES.md` —material de la iniciativa, que no se embarca en un
proyecto instalado y por eso se cita por su ruta y no se enlaza—.

```text
PROPIETARIO          el OWNER. `O25` §3 le reserva la autoridad para aprovisionar,
                     autorizar, rotar, revocar, recuperar y sustituir la identidad «mediante
                     un canal administrativo externo y auditable». No es una decisión de
                     este código y no se toma aquí

MECANISMO PREVISTO   un proveedor de secretos del ANFITRIÓN —HSM, llavero del sistema o
                     gestor de secretos— que entre por la MISMA frontera que ya existe: la
                     orden externa declarada en `orden_de_firma` de la configuración de
                     confianza, con la clave alcanzada por `ADS_ANFITRION_ALMACEN`. El
                     paquete no cambia: cambia quién responde detrás de esa orden.
                     `O25` §2 lo deja explícitamente al anfitrión y dice que «será diferente
                     por instalación y entorno»

CONDICIÓN DE CIERRE  `E-17` se cierra cuando el Owner designa un proveedor productivo
                     concreto y una instalación real firma con él: identidad aceptada por el
                     anillo externo, clave que NUNCA cruza la frontera, y rotación,
                     solapamiento, retirada y revocación ejercidas contra ese proveedor. La
                     evidencia de cierre es una atestación emitida y comprobada con la clave
                     custodiada por él, NO por un fichero de pruebas

NO LA SATISFACE      una CLAVE EFÍMERA DE PRUEBAS. `O25` §5 es literal —«las claves efímeras
                     están permitidas únicamente en pruebas y no constituyen custodia
                     productiva»— y `O26` §4 lo repite cerrando la puerta de atrás: «aunque
                     esté fuera de los repositorios y tenga permisos `0600`, NO constituye
                     custodia productiva». Las claves de `firma.generar_par_efimero` son
                     exactamente eso y se destruyen al terminar la batería

QUÉ NO BLOQUEA       la certificación TÉCNICA de lo que este paquete implementa: la
                     propiedad que se demuestra es la frontera, no el custodio detrás de
                     ella

QUÉ SÍ BLOQUEA       cualquier afirmación de CUSTODIA PRODUCTIVA. Ninguna salida de este
                     paquete la afirma, y una prueba lo barre: `T309` en
                     `../runtime/pruebas/test_integridad_y_evidencia.py`
```

## `E-18` · LO QUE ESTE ANFITRIÓN PUEDE EJERCER, Y LO QUE NO

**Permanece como LIMITACIÓN DE ANFITRIÓN**, y su alcance no se adivina: se mide en cada
ejecución y se publica. Lo que sigue es lo MEDIDO en el anfitrión de esta corrección, y vale
para él: **ninguna afirmación aquí es universal.**

```text
IDENTIDAD DISTINTA     SÍ, por CONTENEDOR. `aislamiento.capacidades()` lo sonda y lo elige:
POR CONTENEDOR         `docker` responde y la imagen declarada está en local, la identidad
                       de dentro es `65534` y la del runtime `1000`, y el repositorio se
                       monta en SÓLO LECTURA. Es la demostración transitoria que `O26` §3
                       acepta, con sus dos CONTROLES POSITIVOS: la escritura en el espacio
                       propio del contenedor TIENE que funcionar y la lectura del árbol
                       montado TIENE que funcionar

USUARIO DEL SISTEMA    NO. Se COMPRUEBA en vez de suponerlo: `sudo -n true` responde que
DISTINTO               hace falta contraseña, y no se puede crear una cuenta de servicio.
                       Es REQUISITO DE INFRAESTRUCTURA, no deuda de este código

`cgroup v2`            PRESENTE y NO EJERCITABLE. Está montado (`cgroup2 on /sys/fs/cgroup`)
                       y publica controladores, y `systemd` delega un subárbol con
                       `cgroup.kill`; pero el envoltorio REAL del backend —escribir el PID en
                       `cgroup.procs` del subgrupo— falla con `EIO`. La sonda lo declara NO
                       DISPONIBLE con ese motivo, y por tanto NO SE CUENTA COMO EJERCIDO. No
                       produce un falso rojo: la política se sirve con otro backend fuerte

CERTIFICACIÓN          LIMITADA AL BACKEND EJERCIDO. Lo que este anfitrión ejerce se publica
LIMITADA               en `contencion.capacidades()` y se comprueba en `T309`; lo que no
                       ejerce se declara con su motivo y no se presenta como demostrado
```
