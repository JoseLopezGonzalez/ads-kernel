# T159–T170 — un producto no es un repositorio

Conformidad de la [enmienda E2](../../../docs/rediseno/a-ENMIENDA-E2-MULTIREPO.md) y de los
contratos [`C6`](../contratos/C6-PRODUCTO-FUENTES-Y-WORKSPACE.md) y
[`C7`](../contratos/C7-GOBIERNO-GIT-MULTI-SOURCE.md).

**Tres validadores distintos**, y la distinción importa:

```text
comprobar_fuentes.py         T159 · T160 · T161 — el ADS Project es VÁLIDO, sin disco
tooling/tests/test_workspace.py  T162..T167 — el workspace se MATERIALIZA, con repos
                             Git locales temporales. Sin red, sin GitHub.
comprobar_arranque.py        T168 — el arranque produce la topología correcta
```

Los que exigen runtime o juicio humano quedan en `contrato-definido`, y lo dicen.

```yaml ads:escenario
id: T159
nombre: La plantilla de SOURCES.toml es válida y arranca sin fuentes
cubre: [C6 fuente única de la composición, E2.0]
dado:
  - "kernel/operativo/plantillas/SOURCES.toml, que new-project.sh copia a cada proyecto"
cuando:
  - "se analiza con el mismo analizador que usa workspace.py"
entonces:
  - "el schema y el layout están soportados"
  - "no declara ninguna fuente: un producto nuevo todavía no tiene código"
falla_si:
  - "la plantilla trae fuentes de ejemplo activas, que un proyecto heredaría como reales"
  - "el TOML no es analizable"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_fuentes.py
estado: prueba-superada
evidencia: evidencia/fuentes-salida.txt
```

```yaml ads:escenario
id: T160
nombre: El manifiesto de un ADS Project, cuando existe, es válido sin tocar el disco
cubre: [C6 validación estática frente a disponibilidad, "§62"]
dado:
  - "un repositorio que puede ser un ADS Project instalado o el propio kernel"
cuando:
  - "se valida su SOURCES.toml sin exigir que ninguna fuente esté clonada"
entonces:
  - "el repositorio del kernel se supera por ausencia justificada: es el upstream, no un control repo"
  - "un ADS Project instalado valida ids, rutas, remotos y componentes"
falla_si:
  - "la validación estática exige acceso a repositorios privados para pasar en CI"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_fuentes.py
estado: prueba-superada
evidencia: evidencia/fuentes-salida.txt
```

```yaml ads:escenario
id: T161
nombre: El corpus no conserva la equivalencia proyecto igual a repositorio
cubre: [E2.0, E2.1, E2.4, 78 qué debe cambiar en el corpus]
dado:
  - "las formulaciones del modelo anterior que la enmienda E2 retira"
  - "los ficheros donde SÍ pueden citarse, porque declaran su derogación"
cuando:
  - "se recorre el repositorio entero buscándolas"
entonces:
  - "ninguna aparece fuera de donde se declara que quedó retirada"
falla_si:
  - "un documento sigue enseñando a copiar ADS dentro del repositorio de código"
  - "un documento sigue afirmando que una tarea equivale a una rama"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_fuentes.py
estado: prueba-superada
evidencia: evidencia/fuentes-salida.txt
```

```yaml ads:escenario
id: T162
nombre: Una fuente ya clonada se reutiliza y no se vuelve a clonar
cubre: [C6 materialización, "§12.1", CA-3]
dado:
  - "un workspace con ads/ y una fuente ya clonada en su ruta declarada"
  - "un fichero local sin confirmar dentro de esa fuente"
cuando:
  - "se ejecuta workspace init"
entonces:
  - "la acción registrada es reutilizada, no clonada"
  - "el fichero local sigue existiendo"
falla_si:
  - "se vuelve a clonar encima y el trabajo local desaparece"
ejecucion: validador-estructural
validador: tooling/tests/test_workspace.py
estado: prueba-superada
evidencia: evidencia/workspace-salida.txt
```

```yaml ads:escenario
id: T163
nombre: Un directorio ocupado por otro repositorio produce error y no se destruye
cubre: [C6 lo que la materialización nunca hace, "§63", CA-5, CA-6]
dado:
  - "una fuente declarada con un remoto, y en su ruta un repositorio Git DISTINTO"
cuando:
  - "se ejecuta workspace check y después workspace init"
entonces:
  - "ambos terminan con error, nombrando el remoto declarado y el encontrado"
  - "el repositorio equivocado sigue intacto en disco"
falla_si:
  - "se cambia el remoto automáticamente"
  - "se borra o se sobrescribe el directorio"
ejecucion: validador-estructural
validador: tooling/tests/test_workspace.py
estado: prueba-superada
evidencia: evidencia/workspace-salida.txt
```

```yaml ads:escenario
id: T164
nombre: Ninguna ruta del manifiesto escapa del workspace
cubre: [C6 identidad frente a materialización, "§11.2"]
dado:
  - "manifiestos con path absoluto, con path que sube con dos puntos, y con la ruta reservada ads"
cuando:
  - "se validan"
entonces:
  - "los tres son ERROR, cada uno nombrando su motivo"
falla_si:
  - "una ruta relativa con dos puntos permite escribir fuera del workspace"
  - "una fuente técnica puede ocupar la ruta del repositorio de control"
ejecucion: validador-estructural
validador: tooling/tests/test_workspace.py
estado: prueba-superada
evidencia: evidencia/workspace-salida.txt
```

```yaml ads:escenario
id: T165
nombre: La identidad de una fuente no depende de la forma de su URL
cubre: [C6 identidad, 39 normalización de remotes, N9]
dado:
  - "la misma fuente escrita como HTTPS, como scp de SSH y como URL ssh explícita"
cuando:
  - "se normalizan las tres"
entonces:
  - "las tres producen la misma identidad"
  - "dos repositorios distintos siguen produciendo identidades distintas"
falla_si:
  - "clonar con SSH un remoto declarado con HTTPS hace fallar la comprobación"
  - "la normalización iguala repositorios que no lo son"
ejecucion: validador-estructural
validador: tooling/tests/test_workspace.py
estado: prueba-superada
evidencia: evidencia/workspace-salida.txt
```

```yaml ads:escenario
id: T166
nombre: Un componente puede vivir dentro de una fuente, y dos componentes compartirla
cubre: [C6 los tres conceptos, "§9", "§10", CA-7, CA-8, N7]
dado:
  - "una sola fuente y dos componentes que apuntan a rutas distintas dentro de ella"
cuando:
  - "se valida el manifiesto"
entonces:
  - "es válido, y los dos componentes quedan declarados sobre la misma fuente"
  - "un componente cuya ruta sale de su fuente es ERROR"
falla_si:
  - "el modelo impone un componente por repositorio y no admite monorepo"
ejecucion: validador-estructural
validador: tooling/tests/test_workspace.py
estado: prueba-superada
evidencia: evidencia/workspace-salida.txt
```

```yaml ads:escenario
id: T167
nombre: Una fuente ausente no bloquea el trabajo que no la necesita
cubre: [C6 alcance mínimo, 63 source ausente, E2.2 regla 5]
dado:
  - "dos fuentes declaradas y sólo una materializada"
cuando:
  - "se consulta el estado del workspace"
entonces:
  - "la ausente se informa como INFO, no como ERROR"
  - "la orden termina con código cero"
falla_si:
  - "una fuente que nadie necesita todavía impide operar sobre las demás"
ejecucion: validador-estructural
validador: tooling/tests/test_workspace.py
estado: prueba-superada
evidencia: evidencia/workspace-salida.txt
```

```yaml ads:escenario
id: T168
nombre: El arranque crea un workspace con el control repo dentro, en la rama que documenta, y el workspace no es un repositorio
cubre: [C6 topología, "§45", "§46", CA-1, CA-9]
dado:
  - "el comando de arranque documentado, con cada pack y con la combinación real"
  - "la configuración global y de sistema de Git VACÍA, que es donde aparece el defecto"
cuando:
  - "se ejecuta sobre una copia temporal del repositorio"
entonces:
  - "existe workspace/ads con su propio .git, su SOURCES.toml y el kernel instalado"
  - "el control repo nace en la rama que el propio script y START_HERE.md documentan al publicar"
  - "esa rama tiene commit inicial, no sólo un HEAD simbólico"
  - "el workspace NO es un repositorio Git, ni lo es ningún antecesor suyo"
  - "el workspace contiene el control repo y nada más"
  - "workspace check pasa dentro del proyecto creado y no declara ninguna fuente"
falla_si:
  - "el workspace se inicializa como repositorio y las fuentes quedarían anidadas"
  - "el proyecto nace con fuentes de ejemplo que nadie declaró"
  - "se documenta `git push -u origin main` y `git init` deja la rama en `master`"
  - "la rama creada y la documentada dejan de ser la misma sin que nada lo diga"
ejecucion: validador-estructural
validador: kernel/operativo/validadores/comprobar_arranque.py
estado: prueba-superada
evidencia: evidencia/arranque-salida.txt
```

```yaml ads:escenario
id: T169
nombre: Un item que atraviesa dos fuentes no cierra con una sin integrar
cubre: [E2.6, C7 integración parcial, gate:convergencia-de-fuentes, "§30"]
dado:
  - "un item cuyos paquetes escribieron en frontend y en backend"
  - "el PR de frontend fusionado y el de backend sin fusionar"
cuando:
  - "se intenta cerrar el item"
entonces:
  - "el estado del producto es integración parcial, no terminado"
  - "gate:convergencia-de-fuentes falla por la comprobación sin-integracion-parcial"
  - "ENT decide entre continuar la convergencia, compensar o revertir"
falla_si:
  - "fusionar el PR de una fuente basta para declarar el item cerrado"
ejecucion: requiere-runtime
estado: contrato-definido
```

```yaml ads:escenario
id: T170
nombre: Un agente nuevo reanuda un trabajo multi-fuente sin abrir ningún repositorio para adivinar
cubre: [E2.3, C7 recuperación, "§34", "§35", CA-12]
dado:
  - "un paquete interrumpido que escribió en dos fuentes"
  - "su checkpoint, con las revisiones de cada fuente y el contrato vigente"
cuando:
  - "un agente distinto retoma el trabajo"
entonces:
  - "sabe qué fuentes tocó, en qué rama y en qué revisión, sin inspeccionar los repositorios"
  - "el based_on referencia las revisiones y no copia contenido de otra fuente"
falla_si:
  - "hay que abrir cada repositorio para deducir en qué estado quedó el trabajo"
  - "el checkpoint copia contenido de otra fuente en vez de referenciarlo"
ejecucion: guion-manual
estado: contrato-definido
```
