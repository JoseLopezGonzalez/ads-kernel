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
verificador.py            PUNTO EJECUTABLE. `capacidades` · `verificar` · `comprobar` ·
                          `instalacion`. Es un PROCESO aparte, no una función del runtime
instalar.py               copia este paquete y las dependencias del verificador a una
                          instalación FUERA del árbol, con manifiesto de SHA-256 por fichero
firma.py                  frontera con `ssh-keygen -Y` y Ed25519. NO implementa criptografía
atestacion.py             la atestación canónica, vinculada al SHA del commit y al `tree`
aislamiento.py            la DEMOSTRACIÓN de que la identidad no puede escribir: lo intenta
anfitrion_firmante.py     mitad PRIVADA de la frontera de firma. SÓLO firma
anfitrion_verificador.py  mitad PÚBLICA. SÓLO verifica, y no tiene clave privada
errores.py                jerarquía tipada propia; no importa la del árbol verificado
```

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
