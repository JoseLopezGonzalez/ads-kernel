# CONTRATO · ADAPTADORES

**Qué es.** El contrato derivado del entregable `F6-G` y del corte `V7`, cuya norma es
`11-ARQ` §6 —`docs/evolucion/11-ARQUITECTURA-INTEGRADA.md`, que no viaja al proyecto instalado— y cuya ficha de tipo es
su §3.4. Permite que el runtime trabaje con ejecutores distintos **sin incorporar su estado
interno al estado canónico**.

**Qué NO es.** Conocimiento. `§6.1` es tajante: *«un adaptador TRADUCE; si empieza a contener
reglas de trabajo, se convierte en una segunda copia del kernel»*. Y no declara ningún
NIVEL: `§6.5` hace de `soportado` una conclusión derivada de una prueba de humo ejecutada, no
un campo editable, y por eso **`nivel` no existe como campo**.

---

## 1 · La interfaz, y su versión

`VERSION_DE_CONTRATO = 1`. El runtime la exige y rechaza otra con `AdaptadorIncompatible`.

```python
class Adaptador:
    identificador: str
    version_de_contrato: int
    capacidades: list[str]
    def ficha(self) -> FichaDeAdaptador
    def ejecutar(self, orden, *, efecto, limite_segundos,
                 progreso=None, cancelacion=None) -> dict
```

El resultado declara `estado` —`completado` · `fallido` · `cancelado` · `timeout`—, `codigo`,
`salida`, `detalle`, `reintentable`, `efecto` y `repetido`. La **ficha** declara los trece
campos de `§3.4`: identificador · versión · capacidades · operaciones · límites · timeout ·
cancelación · idempotencia · forma de progreso · resultado · errores · evidencia ·
compatibilidad.

**La selección es por CAPACIDAD DECLARADA**, no por nombre, y el desempate es determinista:
`CapacidadNoSoportada` cuando ninguno la declara.

## 2 · El adaptador local de proceso — real, no simulacro

```text
EJECUTA        un `subprocess` de verdad, en su PROPIO GRUPO de procesos
PROGRESA       cada línea del proceso llama al invocable `progreso`
FALLA          código distinto de cero, distinguido de la muerte abrupta
EXCEDE         al vencer el límite mata el GRUPO: `SIGTERM`, espera, y `SIGKILL` si sigue
               vivo. Se comprueba con `os.kill(pid, 0)` que el hijo Y EL NIETO ya no están
CANCELA        igual de real: mata, no pide por favor
ES IDEMPOTENTE recibo durable por `efecto` en SU espacio de trabajo. Una segunda llamada con
               el mismo `efecto` devuelve `repetido: true` SIN volver a ejecutar
```

> **Por qué el recibo NO vive en el estado canónico.** `g.12` declara **un solo ejecutor** de
> mutaciones canónicas, y es el runtime. El acuse del efecto lo escribe él, en la misma
> transición que el resultado. El recibo del adaptador protege otra cosa —el EFECTO, no el
> ESTADO— y por eso son dos niveles y no una redundancia.
>
> **Por qué el timeout sí usa reloj.** `I-g3` lo prohíbe en lo DURABLE. Un timeout es, por
> definición, tiempo de pared, y vive en el plano operacional: el recibo guarda el efecto, el
> código y la salida, y **ni un solo milisegundo**.

## 3 · Proyecciones, huella y deriva

`§6.2` y `§6.3`. Una proyección se **COMPILA** desde la definición canónica, el kernel
instalado, los packs y el perfil, y lleva estampada la **HUELLA de sus entradas**. El
validador de deriva distingue tres diagnósticos, y distinguirlos importa porque el remedio no
es el mismo:

```text
AL_DIA           la proyección corresponde a sus entradas
EDITADA_A_MANO   el cuerpo no casa con su propio sello. Regla `I5`: derivadas, NO editables
OBSOLETA         el cuerpo casa con su sello, pero las entradas han cambiado
```

**El remedio ante huella rota es RECOMPILAR, no sincronizar.** Y dos proyecciones que dicen
cosas distintas sobre lo mismo se detectan comparándolas, que es el defecto que `CAND-016`
midió: la memoria espejada que divergió 23 contra 32 entradas.

## 4 · Qué demuestra, y dónde

`T191` en [`pruebas/test_adaptadores.py`](pruebas/test_adaptadores.py), y los pasos 7, 8, 17,
18 y 23 de `T193` en
[`pruebas/escenario_e2e_runtime.py`](pruebas/escenario_e2e_runtime.py).

## 5 · Lo que este contrato NO cubre

La **pieza 4** de `§6` —la prueba de humo en sesión nueva— **no está implementada**: exige
abrir un entorno de agente real. Por eso este corte **no declara ningún nivel alcanzado** de
ningún adaptador, y no existe ningún adaptador de proveedor comercial: `§6.5` separa
compatibilidad DECLARADA de capacidad OBSERVADA y de nivel CERTIFICADO, y aquí sólo hay lo
primero. **Nada está CERTIFICADO.**
