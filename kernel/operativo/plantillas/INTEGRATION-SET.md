# PLANTILLA — INTEGRATION SET

> Una combinación **exacta** de revisiones de fuentes que ha sido candidata o probada
> conjuntamente. Es la atomicidad **lógica de producto** que Git no ofrece: Git no tiene
> commit físico multi-repositorio, y ADS no finge uno.
>
> Contrato: [`C7`](../contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md) ·
> forma canónica: [`esquemas/integration-set.yaml`](../esquemas/integration-set.yaml) ·
> lo comprueba [`gate:convergencia-de-fuentes`](../contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md).

Vive con su item. Se copia así:

```text
bloque canónico:  ```yaml ads:integration-set

id: IS-<nnn>
item: <ITEM-ID>
estado: candidato | verificado | integrado | parcial | descartado
fuentes:
  - source: <id de SOURCES.toml>
    commit: <SHA>            ← un SHA, nunca una rama: una rama se mueve
    rama: <ref>
    pr: <ref o «ninguno»>
contratos:
  - <contrato transversal>@<versión vigente>
verificacion:
  - ambito: <fuente, integracion, e2e, migracion…>
    resultado: pendiente | pasa | falla | no-aplica
    evidencia: <enlace a la ejecución>
migraciones:
  - <las que intervienen, o «ninguna»>
restaura_a: <IS-anterior, o «primero de su item»>
```

## Las cinco cosas que lo estropean

```text
1  RAMA EN VEZ DE COMMIT     una rama se mueve. Al día siguiente el conjunto ya no
                             describe lo que se probó, y nadie se entera.

2  «VERIFICADO» SIN EVIDENCIA  un resultado `pasa` sin enlace no es una verificación:
                             es una afirmación. El gate lo rechaza.

3  CONFUNDIRLO CON UN RELEASE  un Integration Set puede validarse y no desplegarse
                             nunca. Release es la DECISIÓN de publicar. Son distintos.

4  DECLARARLO `integrado` CON UNA FUENTE FUERA   si una parte se fusionó y otra no, el
                             estado es `parcial`. Llamarlo integrado hace que el sistema
                             informe de un producto que no existe.

5  SIN `restaura_a`          revertir se convierte entonces en arqueología por varios
                             historiales, y nadie la hace bien bajo presión.
```

## Qué debe poder responderse con él, sin reconstruir nada

```text
[ ] ¿qué frontend fue probado con qué backend?
[ ] ¿qué commits componían el candidato?
[ ] ¿qué contratos estaban vigentes?
[ ] ¿qué migraciones intervenían?
[ ] ¿qué CI pasó, y dónde está su salida?
[ ] ¿qué combinación se desplegó?
[ ] ¿qué combinación hay que restaurar si se revierte el producto?
```
