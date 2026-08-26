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
```

## Cómo se comprueba que todo esto sigue en pie

Diez validadores, todos con `EXIT 0` en el último commit. Desde la raíz del repositorio:

```bash
for v in ads_lint comprobar_contratos comprobar_packs comprobar_referencias \
         comprobar_arranque comprobar_versiones comprobar_recuentos \
         comprobar_integridad comprobar_prompts comprobar_negativos; do
  python3 kernel/operativo/validadores/$v.py || echo "FALLA $v"
done
python3 kernel/operativo/validadores/registro_pruebas.py
python3 kernel/operativo/validadores/comprobar_recuentos.py --generar
git status --short          # tiene que quedar vacío: los generados son deterministas
```

La salida archivada está en `kernel/operativo/pruebas/evidencia/`, un fichero por
validador. El estado real de cada prueba, en
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

**Ninguna bloquea.** Las de `DECISIONES-Y-CONTRADICCIONES.md` §2 siguen con su valor por
defecto implementado. La única con contenido normativo —**O1**, si `ENC` era capacidad
propia— quedó **RESUELTA** por la enmienda E1.

## Siguiente acción exacta

> **La fase de corrección está terminada.** Lo que sigue no es de esta iniciativa: es el
> **piloto en un proyecto real**, y es lo único que puede convertir una prueba de
> `contrato-definido` a `prueba-ejecutada`.

```text
1  INSTALAR       ./tooling/new-project.sh <nombre> wear-os,mobile-app
                  (o web-app, según el proyecto). El comando FUNCIONA y está probado por
                  T148 con los tres packs. Ejecútalo sin argumentos para ver los
                  instalables.

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
