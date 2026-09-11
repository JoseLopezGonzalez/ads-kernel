# T430–T434 — zonas no analizadas declaradas por la instancia: `UP-11`

**Qué cierra.** `exclusiones.yaml` es el sitio donde se declara lo que el validador **no**
analiza, con `motivo` obligatorio, publicación en cada ejecución, y fallo si una entrada
queda huérfana. La disciplina era buena; el problema era **dónde vive**:
`kernel/operativo/validadores/`, es decir, **dentro de la huella que decide si una
instalación es un fork**.

Consecuencia: una instancia que ganaba una zona propia no tenía salida buena.

```text
editar el fichero del kernel   huella DIVERGENTE y `kernel-status.sh` en rojo. Se dispara
                               justo la alarma que la huella existe para dar
no declarar nada               el validador lee como corpus material que no lo es
```

Y ganar una zona propia **no es el caso raro: es el normal**. Un ADS gobierna unas fuentes
y acaba archivando material de esas fuentes: documentos que llegan con enlaces relativos al
árbol de **su** repositorio de origen, apuntando a hermanos que deliberadamente no vinieron.
No son corpus —son evidencia, y la evidencia describe—. Medido en una instancia real: **442
errores** en material archivado, y como el lint es el **primer paso** de su flujo de CI,
éste moría sin llegar a ejecutar el kernel, ni el estado durable, ni los validadores, ni las
pruebas.

**Lo que se hace.** `ads_lint.py` lee además `docs/canonico/exclusiones-de-instancia.yaml`
—fuera de `kernel/`, fuera de la huella— y fusiona sus listas con las del kernel, **con la
misma disciplina**. Los cinco escenarios de abajo se ejercen sobre árboles de laboratorio
de verdad, y **tres de los cinco exigen que el mecanismo se NIEGUE**: es lo único que impide
que la sede de instancia se convierta en una puerta trasera.

```yaml ads:escenario
id: T430
nombre: Sin sede de instancia, un enlace heredado sigue saliendo en rojo
cubre: ["UP-11", "linea base"]
dado:
  - "un arbol con un documento heredado que enlaza a un hermano que no vino"
  - "y ningun docs/canonico/exclusiones-de-instancia.yaml"
cuando:
  - "se ejecuta ads_lint.py contra ese arbol"
entonces:
  - "publica el enlace roto y sale con codigo distinto de cero"
falla_si:
  - "sale en verde: entonces los cuatro escenarios siguientes no demostrarian nada"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/pruebas/prueba_exclusiones_de_instancia.py"
estado: prueba-superada
evidencia: "evidencia/exclusiones-de-instancia-salida.txt"
```

```yaml ads:escenario
id: T431
nombre: Una zona declarada por la instancia se salta de verdad
cubre: ["UP-11"]
dado:
  - "el mismo arbol, y una sede de instancia que declara la zona con su motivo"
cuando:
  - "se ejecuta ads_lint.py contra ese arbol"
entonces:
  - "sale en verde: la zona heredada no se analiza como corpus"
falla_si:
  - "sigue en rojo: la sede de instancia no se lee, y la instancia queda sin salida"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/pruebas/prueba_exclusiones_de_instancia.py"
estado: prueba-superada
evidencia: "evidencia/exclusiones-de-instancia-salida.txt"
```

```yaml ads:escenario
id: T432
nombre: La ejecucion PUBLICA las zonas excluidas, tambien en verde
cubre: ["UP-11", "visibilidad"]
dado:
  - "una sede de instancia con una zona declarada correctamente"
cuando:
  - "se ejecuta ads_lint.py y sale en verde"
entonces:
  - "el resumen nombra la zona excluida y el fichero donde se declaro"
falla_si:
  - "la exclusion solo se ve abriendo el fichero de configuracion: entonces deja de ser una decision y pasa a ser una costumbre"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/pruebas/prueba_exclusiones_de_instancia.py"
estado: prueba-superada
evidencia: "evidencia/exclusiones-de-instancia-salida.txt"
```

```yaml ads:escenario
id: T433
nombre: Una exclusion SIN MOTIVO se rechaza
cubre: ["UP-11", "puerta trasera"]
dado:
  - "una sede de instancia con una entrada que declara ruta y no declara motivo"
cuando:
  - "se ejecuta ads_lint.py"
entonces:
  - "sale en rojo y el mensaje nombra el motivo que falta"
falla_si:
  - "se acepta: una exclusion sin motivo es indistinguible de un descuido, y la sede se convierte en el sitio donde callar lo incomodo"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/pruebas/prueba_exclusiones_de_instancia.py"
estado: prueba-superada
evidencia: "evidencia/exclusiones-de-instancia-salida.txt"
```

```yaml ads:escenario
id: T434
nombre: Una exclusion HUERFANA se rechaza
cubre: ["UP-11", "no se acumulan restos"]
dado:
  - "una sede de instancia que excluye una ruta que ya no existe en el arbol"
cuando:
  - "se ejecuta ads_lint.py"
entonces:
  - "sale en rojo y dice que esa ruta ya no existe"
falla_si:
  - "se acepta: la lista acumula restos, y el resto tapa en silencio la zona que ocupe manana ese mismo nombre"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/pruebas/prueba_exclusiones_de_instancia.py"
estado: prueba-superada
evidencia: "evidencia/exclusiones-de-instancia-salida.txt"
```
