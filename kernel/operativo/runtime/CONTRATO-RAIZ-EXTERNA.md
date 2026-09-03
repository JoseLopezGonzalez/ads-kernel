# CONTRATO DERIVADO · RAÍZ EXTERNA DE CONFIANZA · `V6-16` · `g.15` · `O25`

**Qué es.** El **tercero** de los tres contratos derivados que
[`(g)` `g.17`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md) nombra. Instancia `g.15`,
la resolución **`O25`** —titularidad, custodia y autoridad administrativa de la identidad— y
el contrato largo de §11.8 de `docs/evolucion/11-ARQUITECTURA-INTEGRADA.md` —material
de la iniciativa, que NO se embarca en un proyecto instalado y por eso se cita por su ruta
y no se enlaza—.

**Dónde vive.** En un **PAQUETE SEPARADO**, [`kernel/operativo/raiz-externa/`](../raiz-externa/),
fuera de `runtime/` a propósito, con su propio instalador, su propio punto ejecutable y su
propio README. §11.8: *«no puede sustituirse por un script alojado ÚNICAMENTE dentro del
mismo repositorio»*.

**Qué NO es.** **No está CERTIFICADA.** `O25` §6 lo dice de sí misma —«no declara implementada
ni certificada la raíz externa»— y `O24` §4 mantiene PesquerApp bloqueada. Lo que este corte
entrega es la implementación ejecutable y su evidencia; certificar es otro acto.

**Contratos hermanos de este corte.**
[`CONTRATO-ARBOLES-ADVERSARIALES.md`](CONTRATO-ARBOLES-ADVERSARIALES.md) ·
[`CONTRATO-CONTENCION.md`](CONTRATO-CONTENCION.md) ·
[`README.md` del paquete externo](../raiz-externa/README.md).

---

## 1 · Las nueve propiedades de `g.15`, y dónde está cada una

```text
SE EJECUTA FUERA          `verificador.py` es un PROCESO propio, en un PAQUETE aparte, que
                          `instalar.py` copia a una instalación FUERA del árbol verificado,
                          con manifiesto de SHA-256 por fichero. El destino se RECHAZA si
                          cae dentro del árbol, por los dos caminos de resolución
IDENTIDAD SIN ESCRITURA   `aislamiento.py` NO lo afirma: lo INTENTA. Ocho escrituras, una a
Y DISTINTA                una, con el mensaje real del sistema en cada intento, más dos
                          controles del control
CONFIGURACIÓN DE FUERA    `identidad/configuracion.py` rechaza la que viva dentro del árbol,
                          y `O25` §3 es su sede: el repositorio verificado NO puede cambiar
                          por sí mismo qué identidad se acepta
ENTRADAS VERIFICADAS      el commit y su `tree` se resuelven con Git y la atestación queda
                          atada a los DOS. Nunca a un nombre de rama
EVIDENCIA FUERA           `--evidencia` se rechaza si cae dentro del árbol verificado, con la
                          misma doble resolución. `g.13` y `g.15`
FALLA CERRADO             sin `ssh-keygen`, sin clave, sin configuración, sin ancla o con una
                          firma que no verifica, NO se emite veredicto favorable
CONDICIONES DECLARADAS    `verificador.py capacidades` las publica, con la versión de OpenSSH
TRAZABLE Y VINCULADA      identidad, huella pública, época y digest de la atestación viajan
                          en el resumen y dentro de lo firmado
PesquerApp BLOQUEADA      y este contrato no la desbloquea
```

## 2 · La firma es ASIMÉTRICA, y por qué eso no es un detalle

`O25` §5: «criptografía estándar y una biblioteca o proveedor mantenido. **No implementará
primitivas criptográficas propias**». Aquí no hay una línea de criptografía: hay una frontera
con `ssh-keygen -Y sign` / `-Y verify` y **Ed25519**.

```text
DESCARTADO · HMAC       es lo que usa el anfitrión de PRUEBAS de `identidad/`, y es
                        SIMÉTRICO: quien verifica puede firmar. Con eso, el veredicto
                        externo lo fabrica cualquiera que pueda comprobarlo, y `V6-16` se
                        cae entero. La propiedad que se persigue es VERIFICAR SIN PODER
                        FIRMAR
DESCARTADO · `gpg`      arrastra anillo con estado propio, agente y caducidades: mucha más
                        superficie de configuración para el mismo resultado
DESCARTADO · `openssl`  obligaría a elegir a mano formato y empaquetado, es decir, a
                        escribir protocolo. `ssh-keygen -Y` trae NAMESPACE y fichero de
                        firmantes autorizados ya definidos, que es el vocabulario que
                        `O25` §3 necesita
```

**Dos programas, dos poderes.** `anfitrion_firmante.py` **sólo firma** y se NIEGA a verificar;
`anfitrion_verificador.py` **sólo verifica** y no tiene clave privada. Juntarlos en un binario
volvería a poner los dos poderes en una sola ruta.

**La dependencia se fija.** La versión de OpenSSH y el algoritmo se registran DENTRO de lo
firmado, y la disponibilidad se comprueba ANTES de correr.

## 3 · La clave privada, y lo que nunca sale

`O25` §2: fuera de todos los repositorios · sin versionar · ausente de estado, diarios,
evidencia, configuración exportada, logs y errores · inaccesible para el runtime y los
agentes · fallo cerrado sin proveedor válido.

```text
NO CRUZA LA FRONTERA    entra el mensaje, sale la firma. El proceso que pide la firma nunca
                        ve la clave, y con un almacén no exportable no puede verla
PERMISOS `0600`         y su directorio `0700`. Una prueba lo mide
EL `stderr` NO SE       ni el del anfitrión de firma ni el de `ssh-keygen`: es la vía por la
PUBLICA                 que un secreto acaba en un log
EFÍMERAS SÓLO EN        `O25` §5, literal: «no constituyen custodia productiva». Las de la
PRUEBAS                 batería se generan fuera de todo repositorio y el directorio entero
                        se destruye en un `addClassCleanup`, pase lo que pase
BARRIDO                 una prueba toma el cuerpo de la clave y lo busca en TODAS las
                        salidas, en la evidencia, en la configuración exportada y en el
                        árbol verificado entero. Y otra comprueba que ese cuerpo SÍ está en
                        la clave, porque si no el barrido no probaría nada
```

## 4 · La independencia, MEDIDA · el orden de preferencia y lo que salió

```text
1 · USUARIO DEL SISTEMA   NO ES POSIBLE en este anfitrión, y se COMPRUEBA en vez de
    DISTINTO              suponerlo: `sudo -n true` responde «a password is required», y no
                          se puede crear un usuario del sistema. Queda REGISTRADO
2 · CONTENEDOR CON        SÍ. `docker run --user 65534:65534 --network none -v <repo>:/repo:ro`
    IDENTIDAD DISTINTA    La identidad del verificador es `65534` y la del runtime `1000`
    Y MONTAJE `ro`
3 · ESPACIO DE NOMBRES    disponible como RESPALDO, con su límite declarado: `unshare -Urm`
    CON MONTAJE `ro`      da el montaje de sólo lectura, y el `root` de dentro se mapea al
                          MISMO usuario del anfitrión, luego NO da identidad distinta
```

**Los OCHO intentos, todos IMPEDIDOS, con el mensaje real:** modificar un fichero · crear uno
· borrar uno · cambiar una ref · alterar la configuración de Git · sustituir la clave pública
aceptada · cambiar la política · **modificar la atestación después de firmarla**. Y **dos
controles del control** en la misma corrida: una escritura en el espacio propio que TIENE que
funcionar, y una lectura del árbol montado que TIENE que funcionar — sin ellas, «todo falló»
tendría una explicación mucho más probable que el aislamiento.

## 5 · `G-A9` · un veredicto falseado desde dentro es DESMENTIDO

```text
EL ÁRBOL PUEDE MENTIR     `estado/operacional/AUTODECLARACION.json` es un fichero suyo, y no
                          tiene ninguna autoridad. Existe para poder desmentirlo
LA RAÍZ EXTERNA JUZGA     sobre el MISMO commit y el MISMO `tree`, desde fuera, con su copia
                          del verificador y con la configuración que el árbol no controla
GANA LA ATESTACIÓN        `VEREDICTO_DESMENTIDO`, y la razón cabe en una línea: el árbol no
                          tiene la clave con que se firma
```

## 6 · Rotación, solapamiento y revocación · `O25` §5

Reutiliza `identidad/rotacion.py`, y ahora con claves **asimétricas de verdad**: la identidad
rotada firma con su propia clave Ed25519 y verifica contra los firmantes autorizados.

```text
ROTACIÓN        la saliente pasa a RETIRADA con su época; la entrante entra ACTIVA
SOLAPAMIENTO    en ÉPOCAS y no en reloj: `I-g3` expulsa el reloj de lo durable, y una firma
                cuya validez dependiera de la hora de la máquina que verifica es la peor
                propiedad posible para una raíz externa
RETIRADA        verifica dentro de su ventana, y deja de hacerlo fuera
REVOCADA        NO verifica nunca, ni dentro del solapamiento
DESCONOCIDA     la configuración externa no la acepta, y el árbol no puede añadirla
TRAZA           con la huella PÚBLICA, y sin una sola clave privada dentro
```

## 7 · Qué demuestra, y dónde

`T192` en [`pruebas/test_identidad.py`](pruebas/test_identidad.py) —el aparato de identidad—
y `T217`–`T220` en [`pruebas/test_raiz_externa.py`](pruebas/test_raiz_externa.py) —el paquete
externo completo: proceso e instalación separados, firma asimétrica real, independencia
ejercida y `G-A9`—. Punto ejecutable: [`../raiz-externa/verificador.py`](../raiz-externa/verificador.py).

## 8 · Lo que FALTA, dicho sin adornarlo

```text
NO HAY PROVEEDOR         `O25` §2 deja la custodia al anfitrión, y aquí la clave es un
PRODUCTIVO DE CLAVES     fichero `0600` fuera de los repositorios. Un HSM, un llavero del
                         sistema o un gestor de secretos entran por la MISMA frontera —la
                         orden externa declarada en la configuración— y no se ha elegido
                         ninguno: elegirlo es despliegue, no contrato

LA IDENTIDAD SIN         se demuestra con contenedor o con espacio de nombres. Un USUARIO DEL
ESCRITURA SE DEMUESTRA   SISTEMA dedicado, que es la opción 1, exige aprovisionamiento del
CON AISLAMIENTO          anfitrión: `sudo` sin contraseña o una cuenta de servicio creada por
                         quien administre la máquina. Queda como REQUISITO DE
                         INFRAESTRUCTURA, no como deuda de este código

NO ESTÁ CERTIFICADA      `O25` §6 y `O24` §3: la suficiencia se demuestra con implementación
                         ejecutable y pruebas reproducibles, y certificar es un acto aparte
                         que este contrato no ejecuta ni presupone
```
