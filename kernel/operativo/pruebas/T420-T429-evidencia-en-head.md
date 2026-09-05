# T420–T429 — el contraste de la evidencia contra `HEAD`: `D-05`

**Qué cierra.** `D-05` del cierre final de `F6`: el canal «la evidencia es la confirmada en
`HEAD`» estaba **implementado y sin un solo sabotaje que lo pusiera rojo**. No por descuido
de quien escribió el catálogo, sino por una incompatibilidad de forma entre el canal y el
banco de pruebas: `comprobar_negativos.py` monta cada mutación sobre una **copia del corpus
sin `.git`**, y `comprobar_evidencia._contrastar_contra_head` abre con

```python
if not os.path.isdir(os.path.join(base, ".git")):
    return "sin repositorio Git en la raíz: el contraste … NO se ha hecho"
```

es decir, en el único banco que teníamos el canal entero se saltaba **por su primera línea**.
Medido: **164 mutaciones del catálogo, CERO sobre este camino**.

**Lo que se hace.** Los ocho ataques se mecanizan sobre un **repositorio Git de verdad** —
`git init`, evidencia escrita, `git add`, `git commit`—, montado por cada caso en su propio
temporal. Nada se simula: hay blob, hay tree, hay commit y hay `HEAD`.

**El control sano va primero y comprueba el banco, no sólo el canal.** `T420` exige que el
montaje sea un repositorio real antes de creerse ningún verde: que `HEAD` resuelva a un
objeto de tipo `commit`, que `HEAD^{tree}` sea un `tree`, que `HEAD:<ruta>` sea un `blob`,
que **el digest de ese blob sea el SHA-1 de `blob <n>\0` + el contenido en disco** —calculado
aquí, no preguntado a Git— y que el árbol de trabajo esté **limpio**. Sin esto, «todo da
verde porque el montaje no existe» explicaría los ocho resultados igual de bien.

## El hueco que mecanizar los ataques encontró, y que estaba abierto

`T425` —vaciar la evidencia entera— **salió rojo la primera vez que se ejecutó, y el rojo era
del canal, no de la prueba**. La comparación de dictámenes estaba guardada por

```python
if not (antes and despues):
    continue
```

de modo que si la versión del árbol de trabajo **no publica ningún veredicto** para el
escenario, no había nada que comparar y el caso pasaba **en verde**. Es la vía más limpia de
retirar un dictamen incómodo: no se edita el veredicto, se deja de emitirlo. Vaciar el
fichero, o reescribirlo para que deje de nombrar al escenario, atravesaba el canal sin ruido.

**Corregido**: que `HEAD` juzgue un escenario y el árbol de trabajo ya no lo juzgue es ahora
un fallo con su propio motivo —«*un escenario que deja de estar juzgado por su propia
evidencia no es un escenario sin novedad: es un dictamen retirado*»—. El caso contrario —que
`HEAD` no lo juzgara— sigue sin ser fallo, porque no hay dictamen anterior del que apartarse,
y de que un escenario cite una evidencia que no lo nombra ya responde el contraste, que lo
cuenta como NO CONTRASTABLE con su estado declarado.

## El noveno ataque, que la auditoría independiente encontró abierto

Los ocho de arriba se cerraron y el auditor probó un noveno de la misma clase: en vez de
**vaciar** el fichero, **borrarlo**. `T425` era rojo; `rm` era **verde**, y ni siquiera se
contaba. Dos gestos con el mismo efecto —el dictamen deja de existir— y veredictos opuestos,
por la guarda `if not os.path.isfile(ruta): continue`. Cerrado en `T429`: si `HEAD` tiene el
blob y el árbol de trabajo no tiene el fichero, es un dictamen retirado y se juzga igual.

**Y el canal era MUDO.** El auditor midió que `r.nota` —donde vive la frase «*el contraste
NO se ha hecho, y no se da por hecho*»— se calculaba y **se descartaba**: `T427` y `T428`
asertaban sobre una cadena que en producción nadie recibía, de modo que sobre el corpus que
`comprobar_negativos` copia sin `.git` la evidencia publicada era **byte a byte
indistinguible** de una corrida donde el canal sí corrió. La decisión que lo descartaba era
correcta en su motivo —la nota entera es volátil y rompería el determinismo de `T158`— y
demasiado ancha en su consecuencia. Ahora se parte en dos: **si el canal se ejerció o no** se
publica siempre, porque depende del árbol y no del reloj; el detalle volátil sigue fuera.

## Lo que estos escenarios NO afirman

El canal juzga el **dictamen**, no los bytes: una regeneración legítima difiere de `HEAD` y
eso **no** es rojo, y `T424` lo mide en positivo, porque un guardián que castiga reforzar una
batería se acaba apagando —y apagado no protege de nada—. Que el contenido de la zona
`EVIDENCIA` no mute sin declararlo lo juzga **`V6-10`** en el verificador de admisión.
Reescribir la historia de Git —`amend`, mover la referencia— lo juzga la **huella** del
kernel; `T427` mide lo que **este** canal hace ante la desaparición de su base de contraste,
que es quedarse sin poder juzgar, y le exige **decirlo** en vez de dar verde callando.

```yaml ads:escenario
id: T420
nombre: El banco del contraste es un repositorio Git de verdad, y se demuestra pieza a pieza
cubre: ["D-05", "control positivo"]
dado:
  - "un repositorio Git creado por la prueba, con la evidencia escrita y confirmada"
cuando: ["se comprueban el commit, el tree, el blob, su digest y la limpieza del arbol"]
entonces:
  - "HEAD resuelve a un objeto commit y HEAD^{tree} a un tree"
  - "el blob de la evidencia existe y su digest es el SHA-1 de la cabecera mas el contenido"
  - "el arbol de trabajo esta limpio y el contraste no publica ningun fallo"
falla_si:
  - "el montaje no es un repositorio real, y entonces los ocho ataques atacan a un decorado"
  - "el control sano da rojo, que haria que todo verde de los ataques no significara nada"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T421
nombre: Un veredicto bueno reescrito como malo en el arbol de trabajo da FALLIDA
cubre: ["D-05", "ataque 1"]
dado: ["una evidencia con seis veredictos buenos confirmada en HEAD"]
cuando: ["el arbol de trabajo se edita para publicar cinco buenos y uno malo"]
entonces: ["el contraste falla nombrando que la evidencia ha cambiado de DICTAMEN"]
falla_si: ["un ok convertido en FAIL pasa sin ser detectado"]
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T422
nombre: Un veredicto malo confirmado que desaparece del disco da FALLIDA
cubre: ["D-05", "ataque 2"]
dado: ["una evidencia con cinco buenos y un malo confirmada en HEAD"]
cuando: ["el arbol de trabajo se edita para publicar seis buenos y ningun malo"]
entonces: ["el contraste falla: el conjunto de veredictos cambio y la cuenta de malos bajo"]
falla_si: ["tapar un rojo confirmado pasa sin ser detectado, que es el ataque que importa"]
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T423
nombre: La evidencia que encoge en silencio da FALLIDA, aunque no cambie de clase de veredicto
cubre: ["D-05", "ataque 3", "cliquet de cobertura"]
dado: ["una evidencia con seis veredictos buenos confirmada en HEAD"]
cuando: ["el arbol de trabajo se edita para publicar uno solo, del mismo tipo"]
entonces: ["el contraste falla diciendo que la evidencia ha ENCOGIDO, con las dos cifras"]
falla_si:
  - "una bateria adelgaza de seis casos a uno sin que nada lo diga"
  - "se compara solo el conjunto de veredictos, que no ve el adelgazamiento"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T424
nombre: Una regeneracion legitima difiere de HEAD y NO da rojo
cubre: ["D-05", "ataque 4", "falso positivo"]
dado: ["una evidencia con seis veredictos buenos confirmada en HEAD"]
cuando: ["se anade un caso que pasa y la evidencia se regenera"]
entonces:
  - "el contraste no publica ningun fallo"
  - "la nota publica que difiere de HEAD sin cambiar ningun dictamen"
falla_si:
  - "reforzar una bateria pone el canal en rojo, que es como se consigue que lo apaguen"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T425
nombre: Vaciar la evidencia entera da FALLIDA, y antes de este escenario NO lo daba
cubre: ["D-05", "ataque 5"]
dado: ["una evidencia con seis veredictos buenos confirmada en HEAD"]
cuando: ["el fichero del arbol de trabajo se deja sin un solo veredicto"]
entonces:
  - "el contraste falla diciendo que HEAD publicaba veredictos y el arbol NO PUBLICA NINGUNO"
falla_si:
  - "la ausencia de veredictos se trata como ausencia de novedad, que era el hueco abierto"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T426
nombre: Renombrar el escenario para que su evidencia deje de nombrarlo da FALLIDA
cubre: ["D-05", "ataque 6"]
dado: ["una evidencia que juzga a T900 con cinco buenos y un malo, confirmada en HEAD"]
cuando: ["el arbol de trabajo publica los mismos veredictos bajo OTRO identificador"]
entonces:
  - "el contraste falla: el dictamen de ese escenario se ha retirado sin ejecucion que lo respalde"
  - "la nota publica ademas que la evidencia difiere de HEAD"
falla_si:
  - "cambiar el identificador basta para que el dictamen deje de compararse"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T427
nombre: Sin repositorio Git el canal no puede juzgar, y lo DICE en vez de dar verde mudo
cubre: ["D-05", "ataque 7"]
dado: ["un repositorio con la evidencia confirmada, al que se le borra el directorio .git"]
cuando: ["se pide el contraste contra HEAD"]
entonces:
  - "no se publica ningun fallo, porque no hay base contra la que juzgar"
  - "la nota dice que el contraste NO se ha hecho y que no se da por hecho"
falla_si:
  - "la ausencia de repositorio se convierte en un verde silencioso, que es EXACTAMENTE la forma del defecto D-05"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T429
nombre: Borrar la evidencia confirmada da FALLIDA igual que vaciarla
cubre: ["D-05", "ataque 9", "auditoria independiente"]
dado: ["una evidencia con cinco buenos y un malo confirmada en HEAD"]
cuando: ["el fichero se BORRA del arbol de trabajo"]
entonces:
  - "el contraste falla diciendo que HEAD la tiene confirmada y el arbol NO la tiene"
  - "la nota cuenta las ausentes, para que el fallo figure tambien en el recuento"
falla_si:
  - "borrar es verde mientras vaciar es rojo: dos gestos con el mismo efecto y veredictos opuestos"
  - "la ausencia del fichero se trata como ausencia de novedad, que era el hueco abierto"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```

```yaml ads:escenario
id: T428
nombre: Una evidencia citada y no confirmada en HEAD se cuenta y se NOMBRA
cubre: ["D-05", "ataque 8"]
dado: ["una evidencia confirmada y otra que existe en disco y no esta en HEAD"]
cuando: ["se pide el contraste contra HEAD con los dos escenarios"]
entonces:
  - "no se publica fallo por la no confirmada, porque no hay contra que contrastarla"
  - "la nota la cuenta y la nombra por su fichero"
falla_si:
  - "un fichero que nadie confirmo pasa sin figurar, que es donde se esconderia una evidencia fabricada"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_integridad_y_evidencia.py"
estado: prueba-superada
evidencia: "evidencia/integridad-evidencia-salida.txt"
```
