# CONTRATO DERIVADO · RAÍZ EXTERNA DE CONFIANZA · IDENTIDAD Y FIRMA

**Qué es.** El **tercero** de los tres contratos derivados que
[`(g)` `g.17`](../../../docs/rediseno/g-ESTADO-DURABLE-APROBADA.md) nombra. Instancia `g.15`
y la resolución **`O25`**, que fija titularidad, custodia y autoridad administrativa de la
identidad criptográfica.

**Qué NO es.** **No es la raíz externa COMPLETA**, y no se presenta como tal. `O25` §6 lo
dice de sí misma: la resolución *«no declara implementada ni certificada la raíz externa»*.
Aquí está el contrato y su parte ejecutable; falta que se ejecute con un proveedor
productivo del anfitrión.

---

## 1 · Lo que `O25` fija, y esto instancia

```text
TITULARIDAD   la identidad es de la RAÍZ EXTERNA de cada instalación. No del repositorio
              verificado, ni del control repo, ni del kernel, ni del runtime, ni de un
              agente. La autoridad administrativa es del Owner

CUSTODIA      una identidad de servicio dedicada del verificador externo, con un proveedor
              de secretos del anfitrión. Fuera de todos los repositorios · sin versionar ·
              ausente de estado, diarios, evidencia, configuración exportada, logs y
              errores · inaccesible para el runtime y para los agentes · no exportable
              cuando el proveedor lo permita · distinta por instalación y entorno

FALLO CERRADO sin proveedor válido no se firma. No hay ruta por defecto que firme con nada
```

## 2 · El proveedor productivo DELEGA, y no toca la clave

`ProveedorProductivo` extiende la interfaz de firma que **ya existe** en el motor —no la
duplica— y delega en una orden del anfitrión declarada en la configuración externa. El
proceso **nunca abre la clave privada**. Sin proveedor válido o con el anfitrión mudo:
`SinProveedorDeIdentidad` o `AnfitrionNoResponde`, **sin degradar** a una firma propia. El
`stderr` del anfitrión **no se publica**: es la vía por la que un secreto se escapa a un log.

**No se implementa criptografía propia.** `O25` §5 lo prohíbe, y aquí sólo se usan primitivas
de la biblioteca estándar mantenida.

## 3 · La configuración de confianza vive FUERA del árbol

Es la propiedad que impide que el repositorio decida quién lo verifica, y `g.15` la exige:
*«recibe DESDE FUERA su configuración y su política de admisión: su autoridad NO puede
depender del árbol que verifica»*.

```text
· una ruta de configuración DENTRO del árbol verificado se rechaza: ConfiguracionDentroDelArbol
· también por enlace simbólico, porque si no la comprobación sería una formalidad
· manipular la configuración dentro del árbol NO cambia el veredicto, y se demuestra
  comparando la exportación byte a byte antes y después
```

## 4 · Estados de identidad y rotación

```text
ACTIVA     firma y verifica
RETIRADA   NO firma; verifica sólo DENTRO del solapamiento declarado
REVOCADA   no firma y no verifica, ni siquiera dentro del solapamiento

el SOLAPAMIENTO se mide en ÉPOCAS, no en reloj: una retirada verifica en el límite y falla
en el límite más uno. Una identidad desconocida es IdentidadDesconocida, y una revocada es
IdentidadRevocada. La traza de aprovisionamiento y rotación se conserva SIN revelar secretos
```

## 5 · Qué demuestra, y dónde

`T192` en [`pruebas/test_identidad.py`](pruebas/test_identidad.py), con la **prueba de
ausencia de secretos**: se inyecta un marcador único en la clave, se ejerce todo el aparato
—firmar, verificar, atestar, verificar la atestación, rotar, revocar y fallar— y se comprueba
que el marcador **no aparece** en ninguna salida, ni en el árbol de estado, ni en el diario,
ni en la evidencia, ni en la configuración exportada; con su control del control, que
confirma que el marcador **sí** está en la clave.

## 6 · Lo que FALTA para que la raíz externa esté completa, dicho sin adornarlo

```text
· un PROVEEDOR PRODUCTIVO del anfitrión. El de pruebas usa un MAC SIMÉTRICO, y eso
  significa que quien verifica podría firmar: una raíz externa real necesita firma
  ASIMÉTRICA del anfitrión. Está escrito también en el código
· EJECUCIÓN REAL FUERA del árbol verificado con una identidad que no pueda escribir en él.
  Se demuestra la PROPIEDAD —proceso aparte, cwd fuera, árbol sin permiso de escritura—,
  no el despliegue
· `V6-16` sigue NO IMPLEMENTADO, y no se declara cerrado
```

**Las claves efímeras siguen permitidas ÚNICAMENTE en pruebas y no son custodia productiva**,
como `O25` §5 dice. **Nada de esto está CERTIFICADO.**
