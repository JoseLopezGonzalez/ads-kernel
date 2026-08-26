# LA DECISIÓN MULTI-REPO — qué cambia, y la contradicción que no puedo resolver

El 2026-08-26, con F2 ya escrita, el Owner incorporó dos documentos al repositorio. Uno
declara una arquitectura **aprobada para implementación**. El otro declara esa misma
materia **abierta y bloqueada para implementación**. Este documento registra ambos, mide su
efecto sobre el trabajo hecho, y **no elige entre ellos**.

## Los dos documentos

| | estado que se declara a sí mismo | sobre la materialización multi-repo |
|---|---|---|
| [`ADS-ARQUITECTURA-MULTIREPO-APROBADA.md`](../../ADS-ARQUITECTURA-MULTIREPO-APROBADA.md) | *«APROBADO PARA IMPLEMENTACIÓN»* · *«La decisión de arquitectura descrita aquí está tomada y debe implementarse»* | la **cierra**: `D1`–`D10`, con repositorio ADS de control, workspace de repos hermanos, `SOURCES.toml`, sin submodules |
| [`ADS-IDEAS-PENDIENTES-MULTIREPO.md`](../../ADS-IDEAS-PENDIENTES-MULTIREPO.md) | *«documento de trabajo del Owner»* · *«no autoriza a implementar automáticamente»* | la **abre**: §12 *«CUESTIÓN ABIERTA CRÍTICA … NO IMPLEMENTAR TODAVÍA»*, §15 *«ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO»* |

## La contradicción, con las dos posturas escritas

Es el formato que exige el freno 1 de [`a.7`](../rediseno/a-CAPACIDADES-APROBADA.md):
ninguna parte cede en silencio.

```text
POSTURA A — la arquitectura sustituye a la cuestión abierta
  El §12 de IDEAS enumera veintiocho preguntas. ARQUITECTURA las responde una a una:
  dónde vive el PROFILE, dónde el estado, si hay repositorio de control, si se usan
  submodules, cómo trabaja un package que toca dos repos, qué pasa si un repo está
  inaccesible, cómo se versiona la composición. El §13 de IDEAS pide comparar diez
  alternativas; el §106 de ARQUITECTURA cierra D1–D10 sobre esas mismas alternativas.
  Lectura: IDEAS planteó la pregunta y ARQUITECTURA es su respuesta.

POSTURA B — la cuestión sigue abierta
  Los dos ficheros se guardaron con sesenta y ocho segundos de diferencia, y el que
  declara la materia ABIERTA se guardó DESPUÉS. Su tabla de estado del §15 no dice
  «resuelta»: dice «ABIERTA — NO IMPLEMENTAR SIN DISEÑO PREVIO». Un documento de
  trabajo que se entrega junto a la decisión y sigue marcando el punto como abierto
  puede estar señalando que la decisión no está cerrada, o que se cerró y la tabla no
  se actualizó.

QUÉ NO PUEDE HACERSE
  Elegir por probabilidad. La postura A es más verosímil y sigue siendo una inferencia
  sobre la intención del Owner en la materia de mayor alcance de toda la evolución:
  ARQUITECTURA ordena reescribir START_HERE, new-project.sh, las plantillas, KERNEL.md,
  cuatro capacidades y —en su §79— las secciones (a) y (b) APROBADAS.

QUÉ SE HACE
  Registrar, no implementar. La materia pertenece al Owner por autoridad, no por
  cortesía: es una contradicción normativa que el sistema no puede resolver por sí solo,
  que es exactamente el caso que la directiva reserva para él en su último párrafo.
```

### RESUELTA por el Owner el 2026-08-26

Se planteó y se cerró en el mismo día. La resolución, literal:

> `ADS-IDEAS-PENDIENTES-MULTIREPO.md` conserva ideas generales y cuestiones todavía
> abiertas. `ADS-ARQUITECTURA-MULTIREPO-APROBADA.md` contiene la decisión definitiva del
> Owner sobre la arquitectura multi-repositorio. **Para todo lo relacionado con la
> materialización multi-repo, el segundo documento resuelve y sustituye el bloqueo y las
> cuestiones abiertas del primero.** No interpretes el resto de ideas pendientes del primer
> documento como autorización automática para implementarlas.

```text
VIGENTE      ARQUITECTURA, en todo lo relativo a materialización multi-repo. Es la POSTURA A.
SUPERADO     el §12 y la fila de materialización del §15 de IDEAS.
SIGUE VIVO   el resto de IDEAS —auditoría de simplificación, actualización de ADS en
             proyectos instalados, unidad superior a task/package, dossier vivo, contratos
             compartidos, integración global— como ideas, NO como autorización.
```

## Qué cambia en F2 si la postura A es la correcta

Medido, no supuesto: los seis problemas de [`06-CONTRASTE.md`](06-CONTRASTE.md) contra lo
que `ARQUITECTURA` decide.

| | problema registrado en F2 | efecto de la decisión aprobada |
|---|---|---|
| **P-01** | el adaptador está nombrado en una regla y no tiene contrato | **redirigido, no resuelto.** `D10` decide el modelo —*«adapters sobre un contrato de filesystem/Git»*— y `I10` prohíbe que una integración de proveedor sea requisito del kernel. Sigue sin existir el tipo, el propietario y el gate; ahora se sabe sobre qué contrato apoyarlos |
| **P-02** | ADS no tiene posición para el conocimiento traído de fuera | **intacto.** `ARQUITECTURA` gobierna repositorios de código propios, no conocimiento de terceros |
| **P-03** | no hay estado de calidad persistente por área del producto | **intacto en su pregunta, y con sujeto nuevo.** El documento introduce el **componente lógico** (`N6`, `N7`), que es un candidato natural a ser ese sujeto. No lo decide |
| **P-04** | `G29` gobierna Git en 1.3.0 y la línea 2.0 no lo recogió | **resuelto en su dirección.** El §31 revisa `G29` expresamente y sustituye `item → branch → PR` por `item/package → 0..N source changes → Integration Set`. El §33 exige trazabilidad de source changes y el §27 define el Integration Set. Es la respuesta al 8.3 de la directiva. **Queda como implementación, no como pregunta** |
| **P-05** | sin evidencia independiente no puede demostrarse si falta capa entre PACK y PROFILE | **intacto y deferido.** `ARQUITECTURA` reparte el conocimiento entre control repo y sources; no dice nada sobre conocimiento reutilizable entre productos distintos |
| **P-06** | la deriva entre núcleo neutral y adaptadores no la ve nadie | **reforzado.** El §111 —regla de no duplicación— y `I1` —una única fuente de verdad para la composición— van en la misma dirección, y siguen sin validador que las compruebe |

**Dos de seis se mueven. Cuatro siguen igual.** La decisión multi-repo es grande y
ortogonal a la mayor parte de lo que el contraste encontró.

## Lo que la decisión aprobada exige y F2 no había previsto

```text
ENMIENDA A MATERIAL APROBADO   el §79 lista docs/rediseno/a-CAPACIDADES-APROBADA.md y
                               b-RECORRIDO-APROBADA.md entre los ficheros a revisar, y el
                               §80 toca la premisa de a.9: «el estado operativo ES los
                               ficheros del repo». Con varios repos, «el repo» deja de ser
                               una expresión unívoca.
                               → es una ENMIENDA, con el precedente de E1: numerada,
                                 aprobada explícitamente, conservando el texto anterior.
                                 La regla 1 de 03-INVARIANTES no admite otra vía.

CATORCE PRINCIPIOS NUEVOS      N1–N14 del §97 son normativa que hoy no existe en ninguna
                               capa.

DIEZ INVARIANTES NUEVOS        I1–I10 del §98 conviven con los seis de a.9 y usan la misma
                               numeración para cosas distintas. Dos juegos de «I1» en el
                               mismo sistema es el defecto que kernel/VERSIONES.md ya
                               documentó para las versiones.

DIECISIETE CRITERIOS           CA-1 a CA-17 del §99 son, en vocabulario ADS, un gate con
DE ACEPTACIÓN                  diecisiete comprobaciones. Encajan sin deformarse.
```

## Tercera ocurrencia de un defecto ya registrado

Los dos documentos entraron al repositorio y **los mismos dos validadores volvieron a
rechazarlos**: seis expresiones de vocabulario y `T147` declarándolos *«existe para
nadie»*. Es la tercera vez, con el mismo mecanismo y el mismo remedio manual.

```text
P-07 · ADS no tiene sitio declarado para material normativo en voz del Owner

  OCURRENCIAS   ADS-NEXT-OWNER-BRIEF.md y su prompt (X5, F0)
                ADS-ARQUITECTURA-MULTIREPO-APROBADA.md y ADS-IDEAS-PENDIENTES (aquí)

  QUÉ FALLA     un documento del Owner no es corpus operativo y no puede reescribirse
                para cumplir la regla de condición comprobable: reescribirlo sería
                reescribir la orden. Hoy la única salida es una exención manual en
                exclusiones.yaml, una por fichero, cada vez.

  Y ADEMÁS      quedan en la raíz del repositorio, que el README no describe como sitio
                de nada. La convención existente —docs/rediseno/ para lo normativo,
                docs/evolucion/ para la evolución— no se aplicó, y moverlos es una
                decisión del Owner, no una limpieza.

  NO SE RESUELVE AQUÍ   un tipo canónico para «documento del Owner» es diseño, y el
                        diseño está detenido hasta que se resuelva la contradicción.
```

## Qué pasa con F3

**Sustituida por el mandato de implementación.** El Owner ordenó el 2026-08-26 implementar
`ARQUITECTURA` íntegramente, y prohibió expresamente reabrir investigación sobre lo que ese
documento ya cerró. La síntesis de los candidatos de PesquerApp no se cancela: se reanuda
cuando el mandato esté cumplido, y su material sigue intacto en
[`05-CANDIDATOS.md`](05-CANDIDATOS.md) y [`06-CONTRASTE.md`](06-CONTRASTE.md).

Los cuatro problemas que la decisión no toca —**P-02**, **P-03**, **P-05** y **P-06**—
siguen registrados y sin resolver. **P-04** pasa de pregunta a implementación. **P-01**
queda redirigido por `D10`. **P-07** es nuevo y sigue abierto.
