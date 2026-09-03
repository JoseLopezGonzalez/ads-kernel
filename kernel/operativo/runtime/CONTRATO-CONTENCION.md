# CONTRATO DERIVADO · CONTENCIÓN DE PROCESOS · `FD-5`

**Qué instancia.** La deuda `FD-5` sobre el adaptador local: `adaptadores/proceso.py` declara
—y MIDE— que «un descendiente que hace `setsid` ESCAPA» a `os.killpg`, y remite la contención
a «otro corte». Éste es ese corte.

**Qué NO es.** No retira el backend simple ni lo disfraza. Lo conserva con su **nivel de
aislamiento explícitamente inferior**, declarado en la ficha, en el resultado y en el error
que se levanta cuando la política pide más.

**Contratos hermanos de este corte.**
[`CONTRATO-ARBOLES-ADVERSARIALES.md`](CONTRATO-ARBOLES-ADVERSARIALES.md) ·
[`CONTRATO-RAIZ-EXTERNA.md`](CONTRATO-RAIZ-EXTERNA.md) ·
[`CONTRATO-ADAPTADOR.md`](CONTRATO-ADAPTADOR.md), cuyo límite declarado cierra este paquete.

---

## 1 · El vocabulario, CERRADO. Dos niveles, y no hay tercero

```text
grupo-de-procesos    `killpg`. Muere todo el que siga en el GRUPO. Quien se sale del grupo,
                     sobrevive. Es lo que hay hoy en `adaptadores/proceso.py`, y se DECLARA
arbol-de-procesos    el contenedor de recursos se lleva TODO lo que hay dentro. `setsid` no
                     saca a nadie de un espacio de nombres de PID, de un cgroup, de un
                     ámbito de `systemd` ni de un contenedor
```

Backends: `cgroup-v2` · `espacio-de-nombres-de-pid` · `systemd-scope` · `contenedor` · `simple`.
Errores tipados: `CONTENCION_FUERTE_NO_DISPONIBLE` · `BACKEND_NO_DISPONIBLE` ·
`NIVEL_DESCONOCIDO` · `TAREA_INVALIDA` · `GRUPO_NO_CANCELADO`.

## 2 · Decisiones técnicas, con sus alternativas descartadas

```text
LA DETECCIÓN EJERCE      frente a comprobar que el binario existe, o que el directorio se
LA CAPACIDAD             puede crear. Se midió en un anfitrión real: `cgroup2` unificado,
                         delegación bajo `user@<uid>.service` y `mkdir` correcto — y la
                         MIGRACIÓN de un proceso a `cgroup.procs` devuelve **EIO**. Con una
                         sonda superficial el aparato habría elegido un backend incapaz de
                         contener y lo habría llamado FUERTE. La sonda y el backend
                         comparten el MISMO envoltorio, `GUION_DE_MIGRACION`: una sonda que
                         ejerciera otra vía no detectaría nada

SE PIDE UN NIVEL,        frente a pedir un backend concreto. Quien escribe una política no
NO UN BACKEND            quiere «cgroups»: quiere que la descendencia no escape. Pedir el
                         nivel hace que otro anfitrión cumpla la política con otro mecanismo,
                         y que uno que no pueda cumplirla lo DIGA en vez de aparentarlo.
                         Pedir un backend concreto se conserva para diagnóstico y pruebas

LA DEGRADACIÓN ES UNA    frente a registrar un aviso y seguir. Un aviso lo lee quien opera y
EXCEPCIÓN, NO UN AVISO   lo ignora quien ataca; y sobre todo, el resultado de una ejecución
                         degradada es indistinguible del de una contenida cuando nadie lee
                         el aviso. Con la excepción, la ausencia de contención fuerte NO
                         produce ejecución

EL ORDEN DE              frente a una cadena de `if/elif`. Un orden implícito en el flujo de
PREFERENCIA ES UN DATO   control no se puede publicar, y entonces «se eligió el mejor
                         disponible» es una afirmación que nadie puede contrastar

MATAR AL PID 1 DEL       frente a enumerar los procesos del espacio y señalarlos uno a uno.
ESPACIO                  Cuando el PID 1 de un espacio muere, el núcleo manda `SIGKILL` a
                         todos los demás: es la semántica del mecanismo, no una convención
                         de este código, y no tiene carrera. Enumerar siempre deja una
                         ventana en la que aparece un proceso nuevo

EL ÁMBITO DE `systemd`   frente a señalar al `systemd-run`. `systemctl --user stop
SE PARA POR SU UNIDAD    <unidad>.scope` actúa sobre el cgroup del ámbito, que es el
                         contenedor real; una señal al lanzador deja vivo el ámbito

`cgroup.kill` LLEVA      antes de matar, el backend comprueba que su propio PID no está en
GUARDA                   el subgrupo. Escribir en el `cgroup.kill` equivocado mata a quien
                         lo escribe, y una guarda que se comprueba es barata

LA TAREA LLEVA UNA       dentro de un espacio de nombres de PID los procesos se ven como 1,
MARCA ÚNICA              2, 3 y no pueden publicar su PID del anfitrión. Sin marca, «murió»
                         sería una creencia; con ella, el anfitrión localiza cada generación
                         por `/proc/<pid>/cmdline` y la comprueba con `os.kill(pid, 0)`

EL BACKEND DE            no descarga imágenes: una prueba cuya contención dependiera de la
CONTENEDOR CORRE SIN RED red no mediría la contención. La imagen se elige entre las que YA
                         están en local, y el contenedor va con `--network none`
```

## 3 · Lo que se demuestra, y con qué pareja

```text
CON EL BACKEND FUERTE    hijo, nieto y bisnieto —los TRES con `setsid`— y NINGUNO sobrevive
                         a la cancelación ni al timeout. Comprobado por PID
CON EL BACKEND SIMPLE    el que se salió del grupo SOBREVIVE, y la prueba lo exige
```

**Esa pareja es el contrato.** Si las dos pruebas dieran lo mismo, una de las dos estaría mal
escrita, y el débil se podría presentar como fuerte sin que nada lo denunciara.

## 4 · Qué demuestra, y dónde

`T214`–`T216` en [`pruebas/test_contencion.py`](pruebas/test_contencion.py), con procesos
REALES y con la detección ejercida sobre el anfitrión que ejecuta la batería.

## 5 · Lo que este contrato NO alcanza

```text
NO SE ENCHUFA SOLO AL    `adaptadores/proceso.py` **no se ha modificado**: sigue con su
ADAPTADOR LOCAL          `killpg` y su límite declarado. Enchufar este paquete como backend
                         del adaptador quedó APLICADA en la integración: el adaptador local
                         acepta `politica_de_contencion`, y su ficha declara el nivel REAL
                         —`grupo-de-procesos` sin política, `arbol-de-procesos` con ella—.
                         Medido a través del adaptador: con `killpg`, tres de cuatro
                         descendientes SOBREVIVEN a la cancelación; con contención, cero de
                         cinco

NO GOBIERNA RECURSOS     contener no es limitar. Memoria, CPU y E/S se pueden limitar con el
                         mismo `cgroup v2` y NO se hace aquí: exigiría una política de
                         recursos que ninguna sede ha fijado

NO CIERRA `FD-5` EN UN   la contención fuerte depende del ANFITRIÓN. En uno que no ofrezca
ANFITRIÓN CUALQUIERA     ninguno de los cuatro mecanismos, lo que queda demostrado es la
                         DETECCIÓN y el FALLO CERRADO, y este contrato lo dice en vez de
                         prometer un aislamiento que ese anfitrión no puede dar
```
