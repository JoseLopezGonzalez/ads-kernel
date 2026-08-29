# Verificación mecánica de la corrección del GATE DE CIERRE

**Qué es.** La batería que comprueba, sobre el árbol y no sobre lo que el texto afirma de
sí mismo, que las correcciones `I-01`–`I-28` del
[`18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md`](../18-GATE-DE-CIERRE-INDEPENDIENTE-F4C.md) —más
la fila `A7`, que es una de las diez FALLIDAS y no lleva número `I-nn`— están hechas.

**Qué NO es.** No es un gate, y no certifica nada. La escribió quien aplicó la corrección,
que es exactamente lo que `F4c` lleva diez tandas sin poder aceptar como prueba. Su valor es
otro: **hace refutable** cada afirmación de la tanda. Si alguien cambia el texto de forma que
una corrección se pierda, esto lo dice.

```bash
python3 docs/evolucion/verificacion/comprobar-correccion-gate-de-cierre.py
```

Sale con código `0` si las treinta están en verde, y con `1` si alguna falla.

> **Portabilidad.** La batería deriva su raíz de `__file__` —tres niveles por encima de
> `docs/evolucion/verificacion/`— y **de nada más**. No usa el cwd y no codifica la ruta de
> ninguna máquina. La versión anterior tomaba el directorio del propio script y, al no
> encontrar `docs` allí, caía a `/home/jose/ads-kernel`: en cualquier otro clon o worktree
> comprobaba **el repositorio del autor en vez del que tenía delante**, y daba verde sobre un
> árbol que nadie estaba mirando. Si la estructura esperada no aparece bajo la raíz derivada,
> **falla con diagnóstico y código 2** en vez de adivinar.
>
> Comprobado **30/30 desde la raíz, desde `/tmp` por ruta absoluta y desde un worktree con
> ruta arbitraria**.

## Por qué estas treinta, y por qué así

Cada comprobación **DERIVA** su resultado del árbol. Ninguna cifra de este documento ni del
checkpoint se compara contra otra escrita a mano: los recuentos se extraen de las filas, los
censos de un barrido, y las cabeceras de su propia enumeración. **La lección de la tanda
anterior es exactamente ésta**: sus «30 comprobaciones, 30 en verde» incluían cuatro que no
debían estarlo —el predicado, la vía de cada participante, los doce campos y las once
presiones—, y ninguna se había ejecutado.

| | qué comprueba | de qué hallazgo sale |
|---|---|---|
| `G-01` | cero `estado/cuarentena/` **vigente**: toda mención que queda declara su retirada, comprobado por párrafo y no por línea | `I-01` |
| `G-02` | `.ads/run/quarantine/` clasificado en §2.4, listado en §2.3, con su ciclo —crear antes de restaurar, verificar por hash, eliminar tras el commit del incidente—, el bloqueo de `SEG` y la aceptación de pérdida del Owner | `I-01` |
| `G-03` | `estado/deriva/` con sus **siete** piezas: árbol, excepción de ruta, `.gitignore`, reconstrucción, creación, retirada y prueba | `I-02` |
| `G-04` | predicado `abierta(tx)` **único**: ninguna sede fuera de §2.6.1 lo redeclara, y se enumeran las que lo citan | `I-03` · `I-09` |
| `G-05` | cero reglas de `#intentos` / `agotado` **vigentes** en la capa B | `I-03` |
| `G-06` | la capa B declara **dos** terminales, no uno | `I-03` |
| `G-07` | cero atribuciones «`PLT` para cada source change» | `I-04` |
| `G-08` | §8.0, §8.1, §8.2, §8.3, §8.4 y §18 citan `C7` operación a operación | `I-04` |
| `G-09` | §18 lleva el gate de `INS-5`, su salida y los tres productores de `O12` | `I-07` |
| `G-10` | **seis** extensiones de ficha en §5.2, §16 y §17, con las seis capacidades | `I-06` |
| `G-11` · `G-11b` | `D67` **idéntica byte a byte** a la de `7e99388`, y `D1`–`D86` intactas. **Las dos fallan CERRADO sin Git** (`Q-01`) | `I-16` · `Q-01` |
| `G-12` | `PN-14` presente, con sus campos, **y sin enmienda redactada** | `F-01` |
| `G-13` | el censo de presiones, derivado de sus cabeceras menos las marcadas, **y el barrido de `PN-15` sobre el material APROBADO** —(a), (b) y `E2`—, derivado fichero a fichero | `I-11` · `P-06` |
| `G-14` | `F-01` reclasificado, con `requiere_f5` y `requiere_f6` | `F-01` |
| `G-15` | `<CAP>:revision` derivado por las CUATRO vías con un **lector estructurado** —indentación y escalares, no expresiones regulares sobre prosa—, **procedencia conservada**, **ancla normalizada**, conjunto vigilado **derivado de las fichas**, y reparto por vía, anclas y censo de fixtures contrastados contra la proyección publicada | `I-08` · `Q-02` · `Q-03` · `Q-05` · `Q-09` · `Q-10` · `Q-11` · `Q-12` |
| `G-16` · `G-16b` | 43 filas, 43 ids distintos, un estado primario cada uno, ninguno compuesto; `A11` absorbido y `A14` excluido. Las trece condiciones `C-L` se contrastan **dentro del bloque VIGENTE**, que está delimitado, y `C-L.3` tiene que nombrar `D104` | matriz · `Q-14` |
| `G-17` · `G-17b` | el recuento publicado **coincide con el derivado**, los atributos secundarios también, y **la matriz de los 24 hallazgos del documento 21** trae sus ids una sola vez, con severidad adjudicada y sin declarar SUPERADO ninguno | matriz |
| `G-18` | vallas Markdown balanceadas en los cuatro ficheros tocados | higiene |
| `G-19` | cero párrafos largos duplicados | higiene |
| `G-20` | `D1`–`D95` sin hueco y sin repetir | trazabilidad |
| `G-21` | `O1`–`O16` intactas frente a `7e99388` | trazabilidad |
| `G-22` | los documentos **15, 16, 17 y 18** no se han tocado | inmutabilidad |
| `G-23` | lo normativo intacto; del kernel sólo cambia la **excepción NOMBRADA**; el **conjunto de ficheros del kernel** se compara contra la revisión base —rastreados o no— y el catálogo de procesos ocupa **UNA sede**; y el punto de entrada del checkpoint **remite** en vez de copiar | alcance · `Q-04` · `M-04` · `R-02` |
| `G-24` | las catorce fuentes y las quince fichas **se LEEN**, y son **exactamente ésas** | cobertura |
| `G-25` | los cuatro macrocircuitos declaran sus **catorce** campos | `I-21` |
| `G-26` | la tabla adversarial tiene tantas filas como ids distintos; la fila que barre **todas** las ventanas cubre las derivadas y nombra la última; los **RANGOS** de presiones terminan en la última vigente; y el censo de presiones se contrasta **también sobre el checkpoint** | higiene · `P-01` · `Q-07` · `P-05` |
| `G-27` | la regla 1 de §2.6.10 usa «los cinco **CAMPOS**» | `A7` |

> **`G-23` y `G-24`, corregidas.** `G-23` afirmaba «`kernel/operativo/` intacto» y excluía en
> bloque todo `pruebas/evidencia/`. Dejó de ser cierta en `1b588ac`, que corrigió
> `comprobar_negativos.py` —para hacer `N158g` independiente del orden del runner— y reancló
> `.upstream-hash`, porque la huella cubre el código de los validadores. Ahora comprueba lo
> exacto: lo normativo intacto, el kernel operativo **sustantivo** intacto, y como únicas
> excepciones `comprobar_negativos.py`, `.upstream-hash` y la evidencia derivada. **Sin
> exclusiones amplias**, y comparando la base contra el **árbol de trabajo** y no contra
> `HEAD`: comparar dos commits dejaba pasar cualquier edición sin confirmar, y una
> comprobación que no ve el árbol que se le pone delante no protege nada.
>
> `G-24` decía «existen y son legibles» y comprobaba `os.path.exists` más `len(fichas) == 15`.
> Con eso, una ficha sustituida por otra, renombrada o ilegible pasaba en verde, y quince
> directorios cualesquiera contaban como el catálogo. Ahora **compara los quince nombres**
> —`APR ARQ CON DIS DOM DSP ENC ENT INV PLT PRD SEG SIS USO VER`— y **abre en UTF-8** las
> catorce fuentes y las quince fichas.

## Lo que esta batería NO comprueba, y se dice

```text
NO EJECUTA NADA DEL         no hay runtime, no hay esquema de `evento`, no hay validador
PROTOCOLO                   del diario y no hay un solo fichero bajo `estado/`. Todo lo que
                            comprueba es TEXTO contra TEXTO, y un contrato coherente no es
                            un sistema que funcione

NO SUSTITUYE AL GATE        no juzga si la arquitectura es SUFICIENTE PARA F5. Comprueba que
                            lo que la tanda dice haber corregido está corregido, que es
                            mucho menos

NO CUBRE EL CORPUS          las catorce fuentes y las quince fichas se comprueban por
                            LECTURA de cada fichero en UTF-8 y por comparación de NOMBRES
                            (`G-24`), no por su contenido. Que un gate posterior los
                            LEA sigue siendo su condición mínima, y ninguna comprobación
                            mecánica la sustituye
```

## Lo que la corrección posterior al GATE DE CIERRE CON MANIFIESTOS añadió

El gate del documento 21 **refutó tres veces esta batería**, y las tres refutaciones están
reproducidas y cerradas:

```text
Q-01  sin `.git` y con D12, D40 y D80 reescritas, `G-11b` decía «ninguna difiere» sobre
      ochenta y seis filas que no había mirado. Hoy falla CERRADO
Q-04  un árbol con `01-PROCESOS-BIS.md` —copia íntegra del catálogo— y un
      `C8-SEGUNDA-SEDE.md` que declara por escrito contradecir a `C4` daba **30/30 EN
      VERDE**: `git diff --name-only` no ve ficheros nuevos sin rastrear. Hoy `G-23`
      compara el CONJUNTO del kernel contra la revisión base y falla nombrando las dos
      causas
Q-05  una línea con aspecto de campo dentro de la prosa de un `criterio_de_satisfaccion`
      entraba en la derivación. Hoy el troceado lee INDENTACIÓN y ESCALARES DE BLOQUE, y
      el fallo NOMBRA el campo que la contiene en vez de acusar a la proyección
```

Y siguen fallando, como deben, las cuatro refutaciones prescritas `R1`–`R4`. **Nada de
esto certifica la batería**: la escribió quien aplicó la corrección, y eso es exactamente
lo que este expediente no acepta como prueba.
