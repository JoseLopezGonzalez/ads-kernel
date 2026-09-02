# ENMIENDA `E6` a la SECCIÓN (b) — la reanudación distingue lo PUBLICADO de lo ESPECULATIVO

```text
identificador   E6
enmienda a      docs/rediseno/b-RECORRIDO-APROBADA.md
fecha           2026-09-02
autoridad       Owner
motivo          el paso 2 de b.14 dice «completar o revertir» sin distinguir qué se puede
                revertir; revertir estado YA PUBLICADO no es un desenlace legítimo, y el
                texto vigente no lo excluye
origen          docs/owner/ADS-OWNER-RESOLUCIONES.md · O23 §10, que aprueba las cuatro
                lecturas del borrador B-05
                docs/evolucion/11-ARQUITECTURA-INTEGRADA.md · §16 PN-7
estado          APROBADA
```

> **Qué es este documento.** La sección `(b)` permanece **íntegra y sin reescribir**. Esta
> enmienda PRECISA un desenlace que su texto vigente dejaba abierto por omisión.
>
> **Lo que esta enmienda NO hace:** no añade un tercer desenlace —**no lo hay**—, no cambia
> el orden de los siete pasos de la reanudación, y no toca la disposición del estado
> durable, que es materia de la sección `(g)`.

---

## `E6.0` — La decisión

**El paso 2 de `b.14` distingue lo PUBLICADO de lo ESPECULATIVO.** Ésta es la lectura que el
Owner ratifica, y **no hay un tercer desenlace normativo**.

## `E6.1` — El texto que PRECISA

### Texto de `(b)` `b.14`, paso 2 · VERIFICAR

```text
DICE           · ¿hay transiciones multiarchivo incompletas? → completar o revertir (a.9)

PASA A REGIR   · ¿hay transiciones multiarchivo incompletas?
                 → COMPLETAR, o REVERTIR LAS ESCRITURAS ESPECULATIVAS a su revisión base,
                   registrar el incidente y escalar — SIN autorizar en ningún caso la
                   reversión de estado ya PUBLICADO (a.9)
```

## `E6.2` — Por qué la distinción es normativa y no una precisión de estilo

```text
LO ESPECULATIVO   es local y todavía no es verdad para nadie más. Revertirlo a su revisión
                  base no destruye ninguna afirmación que otro haya podido leer

LO PUBLICADO      ya es verdad para otros. Revertirlo automáticamente destruiría una
                  afirmación sobre la que alguien pudo actuar, y ninguna reanudación tiene
                  autoridad para eso

Y NO HAY TERCER   o se completa, o se revierte lo especulativo y se escala. La reanudación
DESENLACE         NO decide por su cuenta sobre lo publicado: lo escala
```

**Concordancia con la sección `(g)`, y se dice para que no se lean como dos reglas:** `g.8`
fija las dos ramas de la recuperación —COMPLETAR y MARCAR— y declara que **lo publicado no se
restaura nunca de forma automática** y que **la reversión está acotada a lo especulativo
local**. Esta enmienda es la misma regla vista desde el recorrido, y **no crea una segunda
sede**: la disposición vive en `(g)`, y `b.14` la aplica.

## `E6.3` — Impacto

```text
SOBRE (b)     el paso 2 de b.14 gana la distinción. Los siete pasos, su orden y sus tres
              reglas posteriores NO cambian
SOBRE (a)     ninguno. `a.9` ya prohíbe inventar estado, y esta enmienda no la toca
SOBRE (g)     ninguno. `g.8` ya lo fija, y esta enmienda REMITE en vez de reformular
SOBRE F6      el runtime que implemente la reanudación tiene que distinguir los dos casos.
              ES TRABAJO DE F6, y no está construido
```

## `E6.4` — Trazabilidad

| presión | qué resuelve | apartado |
|---|---|---|
| `PN-7` | el desenlace del paso 2 de `b.14`, sin autorizar la reversión de lo publicado | `E6.1` |

**Prueba posterior:** que `b.14` distinga PUBLICADO de ESPECULATIVO, y que no exista un
tercer desenlace normativo en ninguna sede.
