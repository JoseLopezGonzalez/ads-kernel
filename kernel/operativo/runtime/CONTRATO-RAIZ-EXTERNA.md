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
                          atada a los DOS. Nunca a un nombre de rama. Las DOS MITADES se
                          rechazan POR SEPARADO y tienen prueba independiente capaz de
                          fallar: `E-07`, corregido el 2026-09-04. Antes, la única prueba del
                          vínculo confirmaba un commit nuevo —que cambia commit Y tree a la
                          vez— y las dos mitades levantaban el mismo error, de modo que
                          sabotear cualquiera de las dos dejaba la batería en 38/38 VERDE
EVIDENCIA FUERA           `--evidencia` se rechaza si cae dentro del árbol verificado, con la
                          misma doble resolución. `g.13` y `g.15`
FALLA CERRADO             sin `ssh-keygen`, sin clave, sin configuración, sin ancla o con una
                          firma que no verifica, NO se emite veredicto favorable
CONDICIONES DECLARADAS    `verificador.py capacidades` las publica, con la versión de OpenSSH
TRAZABLE Y VINCULADA      identidad, huella pública, época y digest de la atestación viajan
                          en el resumen y dentro de lo firmado
PesquerApp BLOQUEADA      y este contrato no la desbloquea
ENTORNO CONTAMINADO       los NUEVE puntos ejecutables del árbol —los cinco `ads_*.py` y los
FALLA CERRADO             cuatro de este paquete— purgan la ruta de importación ANTES de
`E-10` · `ADJ-B2`         importar nada, comprueban de dónde salió cada módulo y NO emiten
                          nada si no lo pueden demostrar. `O26` §1, condición 8, corregido
                          el 2026-09-04
```

### 1 bis · `E-10` en la raíz externa, y por qué el inventario se DERIVA

**Lo reproducido, y no se atenúa.** Hasta el 2026-09-04 este paquete no tenía **ni una línea
de purga**, y era la única pieza que `O26` §1 juzga. Con un `json.py` homónimo en
`PYTHONPATH` y desde un `cwd` ajeno:

```text
verificador.py capacidades           → {}          EXIT=0     (sano: las nueve condiciones)
instalar.py --destino … --arbol …    → {}          EXIT=0     manifiesto 3 BYTES (sano: 6734)
                                                              y 41 ficheros instalados igual
… --comprobar sobre esa instalación  → KeyError: 'ficheros'   EXIT=1 y cuatro rutas del
                                                              anfitrión en la traza
```

**Los cuatro puntos ejecutables de este paquete**, con lo que cada uno hace ahora:

```text
verificador.py             purga · exige procedencia de la INSTALACIÓN · publica la
                           procedencia en `capacidades` y en la orden `procedencia` · se
                           niega a publicar el vacío como éxito
instalar.py                purga · exige procedencia · construye APARTE y publica por
                           renombrado, de modo que no queda una instalación a medias ·
                           valida la forma del manifiesto y rechaza el truncado TIPADO
anfitrion_firmante.py      purga · exige procedencia antes de tocar la clave
anfitrion_verificador.py   purga · exige procedencia antes de responder `valida`/`invalida`
```

**El inventario no se escribe: se DERIVA.** Una lista escrita a mano fue exactamente lo que
dejó este paquete fuera del alcance de `T306`, y volvería a quedarse corta. El criterio es
una equivalencia de tres términos, comprobada en los dos sentidos sobre el disco por `T330`:

```text
lleva `#!`   ⟺   define `if __name__ == "__main__":`   ⟺   lleva el prólogo `E-10`
```

Por eso los módulos de biblioteca de este paquete —`errores`, `firma`, `atestacion`,
`aislamiento`— **no llevan línea de intérprete**: llevarla los presentaría como ejecutables,
y a un ejecutable la equivalencia le exige la purga. El prólogo es **el mismo, byte a byte,
en los nueve puntos del árbol**, y `T330` lo verifica por digest: se COPIA, no se importa,
porque una guardia que necesita importar para poder purgar ya ha perdido.

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

## 6 bis · El ORDEN de la verificación, y cuándo se puede escribir evidencia

**La evidencia sólo se escribe DESPUÉS de completar los SIETE pasos, en este orden** —`E-07`,
2026-09-04—. Escribir antes de terminar deja un fichero que dice «verificado» sobre una
verificación que no llegó a su final, y un lector externo no puede distinguirlo de uno bueno:

```text
1 firma                 verifica criptográficamente, o no se sigue
2 clave aceptada        la huella pública está en la configuración EXTERNA
3 época                 la clave estaba vigente para la época declarada, ni retirada ni
                        revocada
4 commit                el SHA del commit casa con el atestado
5 tree                  el `tree` de ESE commit casa con el atestado. Separado del 4: es
                        la otra mitad de `E-07`
6 política              la política externa admite lo atestado
7 identidad del emisor  quién firmó, contrastado contra la configuración externa
```

Interrumpir en cualquiera de los siete deja el fichero de evidencia SIN escribir, y eso se
prueba paso a paso.

## 7 · Qué demuestra, y dónde

`T192` en [`pruebas/test_identidad.py`](pruebas/test_identidad.py) —el aparato de identidad—
y `T217`–`T220` en [`pruebas/test_raiz_externa.py`](pruebas/test_raiz_externa.py) —el paquete
externo completo: proceso e instalación separados, firma asimétrica real, independencia
ejercida y `G-A9`—. Punto ejecutable: [`../raiz-externa/verificador.py`](../raiz-externa/verificador.py).

`T330`–`T337` en
[`pruebas/test_integridad_y_evidencia.py`](pruebas/test_integridad_y_evidencia.py) —el
inventario derivado, el entorno contaminado, el manifiesto truncado, la instalación que no
se hace a medias, el repositorio ajeno que no aporta el código que lo verifica, los
argumentos obligatorios ausentes, el control del control de la purga y el fallo cerrado por
procedencia—. Los sabotajes que las ponen en rojo son `N330` y `N333` del catálogo negativo
del runtime.

## 8 · Lo que FALTA, dicho sin adornarlo

```text
NO HAY PROVEEDOR         `O25` §2 deja la custodia al anfitrión, y aquí la clave es un
PRODUCTIVO DE CLAVES     fichero `0600` fuera de los repositorios. Un HSM, un llavero del
`E-17`                   sistema o un gestor de secretos entran por la MISMA frontera —la
                         orden externa declarada en la configuración— y no se ha elegido
                         ninguno: elegirlo es despliegue, no contrato.
                         **Y se dice sin atenuarlo, porque `O26` §4 lo dice literalmente:
                         una clave efímera de pruebas, AUNQUE esté fuera de los repositorios
                         y tenga permisos `0600`, NO constituye custodia productiva.**
                         PROPIETARIO: el Owner (`O25` §3, autoridad administrativa).
                         MECANISMO PREVISTO: un proveedor de secretos del anfitrión entrando
                         por la frontera ya construida.
                         CONDICIÓN DE CIERRE: una instalación real que firme contra ese
                         proveedor, con rotación y revocación EJERCIDAS contra él.
                         Mientras tanto, NINGUNA salida de este paquete puede afirmar
                         custodia productiva, y hay una prueba que lo barre

LA IDENTIDAD SIN         se demuestra con contenedor o con espacio de nombres. Un USUARIO DEL
ESCRITURA SE DEMUESTRA   SISTEMA dedicado, que es la opción 1, exige aprovisionamiento del
CON AISLAMIENTO          anfitrión: `sudo` sin contraseña o una cuenta de servicio creada por
                         quien administre la máquina. Queda como REQUISITO DE
                         INFRAESTRUCTURA, no como deuda de este código

NO ESTÁ CERTIFICADA      `O25` §6 y `O24` §3: la suficiencia se demuestra con implementación
                         ejecutable y pruebas reproducibles, y certificar es un acto aparte
                         que este contrato no ejecuta ni presupone
```
