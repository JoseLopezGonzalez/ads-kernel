# CHECKPOINT — kernel operativo y sus correcciones

> Registro persistente y reanudable. **Se actualiza al cerrar cada bloque de trabajo.**
> Basta decir «Continúa» en un chat nuevo: la siguiente acción exacta está al final.
>
> **Ninguna cifra de este documento se escribe a mano.** Las derivadas viven en
> [`RECUENTOS-generado.md`](../../kernel/operativo/pruebas/RECUENTOS-generado.md) y
> [`REGISTRO-generado.md`](../../kernel/operativo/pruebas/REGISTRO-generado.md), y T151
> falla si algún documento afirma otra. La versión anterior de este checkpoint quedó
> desactualizada respecto al commit que declaraba terminado —incumpliendo la regla 3 de
> a.10, que es suya— y fue el hallazgo **A-32**.

```text
iniciativa   contenido operativo del kernel 2.0, y sus correcciones post-auditoría
rama         claude/kernel-operativo-correcciones-post-auditoria
base         origin/main @ f5cf2bb
normativo    (a) y (b) APROBADAS · enmienda E1 APROBADA el 2026-08-26
alcance      contratos, esquemas, plantillas, roles, prompts, métodos, circuitos,
             obligaciones, cierre, frenos, gates, validadores, pruebas y packs
fuera        runtime · dispatcher · gym-wear · PesquerApp · pack ERP · (c) a (i)
```

## Estado

```text
LOS SEIS PASOS ESTÁN IMPLEMENTADOS, Y AUDITADOS POR UN LECTOR INDEPENDIENTE.

BLOQUE 0   esquemas, validadores e índice          TERMINADO
BLOQUE 1   circuito Owner → item (paso 1)          TERMINADO
BLOQUE 2   contrato equipo/rol/agente/método       TERMINADO
BLOQUE 3   sistema de excelencia de Diseño         TERMINADO
BLOQUE 4   equipo de Diseño materializado          TERMINADO
BLOQUE 5   demás capacidades                       TERMINADO
BLOQUE 6   packs web-app · mobile-app · wear-os    TERMINADO
REVISIÓN   adversarial del propio equipo           TERMINADA, con su límite declarado
AUDITORÍA  independiente, lector externo           TERMINADA · 33 hallazgos
CORRECCIÓN de los 33 hallazgos                     TERMINADA · 32 corregidos, 1 deuda

FUERA DE ALCANCE, sin empezar:
runtime · dispatcher · gym-wear · PesquerApp · pack ERP · secciones (c) a (i)
```

## Lo que la auditoría cambió, y hay que saber antes de tocar nada

```text
1  ENC es la DECIMOQUINTA capacidad base, por la enmienda E1, y NO es equipo permanente:
   se materializa bajo demanda. Los permanentes siguen siendo DOS, DSP y SIS.

2  Los dos gates de Diseño son obligatorios en los CINCO niveles de novedad. Lo que
   cambia entre niveles es cuánta evidencia se REUTILIZA del patrón vigente, y qué
   demuestra esa vigencia. `acabado` y `fidelidad` no se heredan nunca.

3  El nivel de novedad se CALCULA con cinco variables y condiciones formales. No se
   elige. T138 comprueba sobre las 32 combinaciones que la escala es total y que los
   cinco niveles son alcanzables — N3 no lo era.

4  Las OBLIGACIONES del proceso existen: `recorrido/`, con los diez procesos canónicos y
   `gate:cierre-de-item`. Un item con una obligación huérfana NO cierra.

5  Los frenos tienen ejecutor: `DSP/supervision`, independiente de quien recompone.

6  DSP PROPONE cancelaciones; nunca las decide. Dos vetos incompatibles NO se arbitran:
   escalan al Owner.

7  NINGUNA cifra se escribe a mano. Se derivan y T151 lo comprueba.

8  Cada prueba nueva lleva su INFRACCIÓN DELIBERADA. Un validador que sólo se ha visto
   pasar no está verificado: fue el modo de fallo de T131 y T134.

9  La EVIDENCIA la publica un runner, no un bucle de shell, y T158 comprueba que respalda
   lo que el informe afirma. Ocho de diez evidencias de la entrega anterior estaban
   corruptas y nada lo detectó.
```

## Cómo se comprueba que todo esto sigue en pie

**Una sola orden**, desde la raíz del repositorio:

```bash
python3 kernel/operativo/validadores/registrar_evidencia.py
git status --short          # tiene que quedar vacío: los generados son deterministas
```

El runner regenera los artefactos derivados, ejecuta **todos los componentes declarados
`tipo: validador`** en su manifiesto —[`validadores.yaml`](../../kernel/operativo/validadores/validadores.yaml),
que es su única sede— por su ruta completa terminada en `.py`, captura stdout, stderr y
código por separado, y publica la evidencia **sólo** si el código fue cero. Termina con
código distinto de cero si algo falla.

> **CUÁNTOS SON NO SE ESCRIBE AQUÍ, y es la regla 7 de arriba aplicada a este documento.**
> Esta línea decía «los **once** validadores» cuando el manifiesto ya declaraba más, en el
> fichero cuya cabecera promete que ninguna cifra se escribe a mano: es `Q-15` del
> documento 22. El censo se DERIVA, y éste es el comando:
>
> ```bash
> grep -c 'tipo: validador' kernel/operativo/validadores/validadores.yaml
> ```
>
> El resumen que el propio runner imprime al terminar —`N/M validadores en verde`— es la
> otra sede derivada, y manda sobre cualquier prosa. **Una cifra copiada envejece sola; una
> remisión no.**

> **Y una advertencia que el gate del documento 22 obliga a dejar escrita** (`P-27`≡`Q-08`).
> `git status --short` queda vacío **sólo si la evidencia derivada se republica en el MISMO
> commit que cambia el corpus**. Añadir o quitar un documento mueve los recuentos que
> `fuentes-salida.txt` y `negativos-salida.txt` publican, y el árbol queda sucio hasta que se
> vuelve a correr el runner. Y `T147` falla mientras exista un documento al que no llegue
> ningún enlace por ruta: **todo lo que `C-L.5` obliga a publicar —manifiestos de gate,
> addenda y corrigenda— se enlaza desde
> [`docs/evolucion/00-INDICE.md`](../evolucion/00-INDICE.md) en el mismo commit que lo crea.**
> No se arregla con `exclusiones.yaml`: una exclusión apaga la comprobación en vez de
> cumplirla.

> **No archives evidencia a mano.** La entrega anterior lo hizo con un bucle de shell que
> omitía la extensión `.py` y redirigía el error del intérprete dentro del fichero: ocho de
> diez evidencias quedaron con «python3: can't open file» mientras el informe afirmaba
> «todos EXIT 0». Que lo publicado respalde lo que se afirma lo comprueba ahora **T158**.

La salida vive en `kernel/operativo/pruebas/evidencia/`, un fichero por validador con su
cabecera de procedencia. El estado real de cada prueba, en
[`REGISTRO.md`](../../kernel/operativo/pruebas/REGISTRO.md) y su tabla generada.

## Dónde está cada cosa

| | |
|---|---|
| especificación normativa | [`a-CAPACIDADES-APROBADA.md`](a-CAPACIDADES-APROBADA.md) · [`b-RECORRIDO-APROBADA.md`](b-RECORRIDO-APROBADA.md) · [`a-ENMIENDA-E1-ENC.md`](a-ENMIENDA-E1-ENC.md) |
| contenido operativo | [`kernel/operativo/00-INDICE.md`](../../kernel/operativo/00-INDICE.md) |
| decisiones y contradicciones | [`DECISIONES-Y-CONTRADICCIONES.md`](DECISIONES-Y-CONTRADICCIONES.md) |
| revisión del propio equipo | [`REVISION-ADVERSARIAL.md`](REVISION-ADVERSARIAL.md) |
| auditoría independiente | [`AUDITORIA-INDEPENDIENTE-LOCAL.md`](AUDITORIA-INDEPENDIENTE-LOCAL.md) |
| matriz de correcciones | [`CORRECCIONES-POST-AUDITORIA.md`](CORRECCIONES-POST-AUDITORIA.md) |
| política de versiones | [`kernel/VERSIONES.md`](../../kernel/VERSIONES.md) |

## Decisiones pendientes del Owner

**Ninguna bloquea a ESTA iniciativa.** Las de `DECISIONES-Y-CONTRADICCIONES.md` §2 siguen
con su valor por defecto implementado. La única con contenido normativo —**O1**, si `ENC` era
capacidad propia— quedó **RESUELTA** por la enmienda E1.

> **Las resoluciones posteriores del Owner NO se listan aquí: se REMITEN.** `O7` en adelante
> —incluida **`O17`**, del 2026-08-30, que fija que el nivel ESTRUCTURAL lo produce cada
> macrocircuito al arrancar— pertenecen a la iniciativa **ADS NEXT**, viven en §2 de
> [`DECISIONES-Y-CONTRADICCIONES.md`](DECISIONES-Y-CONTRADICCIONES.md) y su registro
> reanudable es [`docs/evolucion/CHECKPOINT-ADS-NEXT.md`](../evolucion/CHECKPOINT-ADS-NEXT.md).
> **Cuántas son se deriva de sus FILAS, no de una lista copiada aquí**, con
> `grep -cE '^\| *\*{0,2}`?O[0-9]+`?\*{0,2} *\|' docs/rediseno/DECISIONES-Y-CONTRADICCIONES.md`. Ninguna de ellas autoriza
> iniciar `F5`, `F6` ni la adopción de PesquerApp.

## Siguiente acción exacta

> **La fase de corrección está terminada.** Lo que sigue no es de esta iniciativa: es el
> **piloto en un proyecto real**, y es lo único que puede convertir una prueba de
> `contrato-definido` a `prueba-ejecutada`.

```text
1  INSTALAR       ./tooling/new-project.sh <nombre> wear-os,mobile-app
                  (o web-app, según el proyecto). T148 ejecuta EXACTAMENTE esa orden
                  combinada, además de los tres packs por separado, y comprueba que ambos
                  packs quedan instalados, que no se cuela ninguno más, que ningún fichero
                  se sobrescribe entre packs, que la composición P1 es computable y que
                  declara qué queda pendiente del PROFILE. Ejecútalo sin argumentos para
                  ver los instalables.

2  COMPROBAR      dentro del proyecto creado, ads_lint tiene que salir en verde. Si hay
                  enlaces rotos, falta algo por copiar y es un defecto del tooling.

3  PROFILE        rellenar PROFILE.md, y añadir lo que la composición de packs exige:
                    · matriz de relojes y de dispositivos reales
                    · el arbitraje de todo conflicto de materia entre los packs
                    · los valores que P1 resolvió — véanlos con
                      `python3 kernel/operativo/validadores/composicion_packs.py`
                    · la decisión de independencia del reloj: autónomo, acompañante o mixto

4  PRIMER ITEM    NO empezar por una pantalla. Empezar por una FRASE del Owner, entrando
                  por ENC con el prompt de ENC/interlocutor cargado tal cual.

5  PRIMER ANCLAJE ENC/anclaje devolverá qué existe y qué no. El nivel de novedad lo
                  CALCULA la escala con sus cinco variables: no lo decidas por
                  anticipado. Un proyecto con interfaz real probablemente sea N3, pero
                  decide la evidencia.

6  QUÉ VIGILAR    el escenario A de entrada/05-ESCENARIOS es ese recorrido, y ahora
                  declara sus CUATRO salidas posibles según el anclaje. Si el sistema
                  produce en su lugar una tarea de estilos, el kernel ha fallado en su
                  primer uso real: se registra como aprendizaje, no se corrige a mano.

7  QUÉ SE GANA    la primera ejecución convertirá varias pruebas de `contrato-definido` a
                  `prueba-ejecutada`. Ese cambio de estado, con su evidencia, es el
                  resultado más valioso del piloto — más que la aplicación.
```

**No se empieza el runtime.** El piloto se ejecuta con agentes siguiendo los métodos a
mano; lo que el runtime tendrá que automatizar se descubre haciéndolo, y ése es el material
del que nacerán los items `SIS` de la siguiente iteración.
