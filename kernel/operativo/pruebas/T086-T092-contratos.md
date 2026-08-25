# T86–T92 — conformidad estructural de los contratos

Siete propiedades que los contratos C1–C5 declaran obligatorias y que **no necesitan
runtime** para comprobarse. Por eso son las primeras pruebas del sistema que llegan a
**PRUEBA SUPERADA** con evidencia real.

```bash
python3 kernel/operativo/validadores/comprobar_contratos.py
```

Salida registrada: [`evidencia/T086-T092-salida.txt`](evidencia/T086-T092-salida.txt).

> **Lo que estas siete pruebas NO demuestran.** Que los contratos son *coherentes*, no que
> el sistema *funciona*. Un rol puede tener sus veintiocho campos perfectamente declarados
> y aun así producir mal trabajo. La conformidad estructural es condición necesaria, nunca
> suficiente.

```yaml ads:escenario
id: T86
nombre: La autoridad de un rol no excede la de su capacidad
cubre: ["C1", "a.1 AUTORIDAD", "autoridad silenciosa"]
dado: ["el catálogo de capacidades y todos los contratos de rol instalados"]
cuando: ["se comparan las listas de veto de cada rol con las de su capacidad"]
entonces:
  - "ningún rol veta una materia que su capacidad no veta"
  - "ningún rol declara contrato de veto si su capacidad no tiene ninguno"
falla_si:
  - "un rol reclama veto que su capacidad no posee"
  - "un rol pertenece a una capacidad sin ficha"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T86"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```

```yaml ads:escenario
id: T87
nombre: La independencia gana siempre a la combinación
cubre: ["C4 paso 5", "C2 combinaciones prohibidas", "G13"]
dado: ["todas las composiciones declaradas de todas las capacidades"]
cuando: ["se cruzan las listas combinables e independientes de cada composición"]
entonces: ["ningún rol aparece en las dos listas de la misma composición"]
falla_si: ["una composición permite combinar dos roles que ella misma declara independientes"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T87"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```

```yaml ads:escenario
id: T88
nombre: Todo rol es materializable porque su prompt existe
cubre: ["C1 campo prompt", "regla R02", "C4 prohibiciones"]
dado: ["todos los contratos de rol"]
cuando: ["se resuelve la ruta declarada en el campo prompt de cada uno"]
entonces: ["el fichero existe en el repositorio"]
falla_si: ["un rol declara un prompt inexistente, o no declara ninguno"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T88"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```

```yaml ads:escenario
id: T89
nombre: Ninguna reanudación se declara posible sin prueba que la respalde
cubre: ["C3 regla 7", "regla R03", "a.10"]
dado: ["todos los métodos declarados"]
cuando: ["se extraen los identificadores de prueba citados en prueba_de_reanudacion"]
entonces: ["cada uno corresponde a un ads:escenario declarado"]
falla_si:
  - "un método afirma ser reanudable sin citar prueba"
  - "un método cita una prueba que no existe"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T89"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```

```yaml ads:escenario
id: T90
nombre: Capacidades y roles se referencian mutuamente sin huérfanos
cubre: ["a.1", "C1", "C4"]
dado: ["el catálogo completo de capacidades y roles"]
cuando: ["se cruzan las listas de roles de cada capacidad con el campo capacidad de cada rol"]
entonces:
  - "toda capacidad lista roles que existen y que dicen pertenecerle"
  - "todo rol pertenece a una capacidad que lo lista"
falla_si: ["existe un rol huérfano, o una capacidad que lista un rol inexistente"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T90"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```

```yaml ads:escenario
id: T91
nombre: Ningún paso de ningún método dura lo que el agente decida
cubre: ["C3 regla 1", "esquemas/metodo.yaml"]
dado: ["todos los métodos declarados"]
cuando: ["se recorre cada paso de cada método"]
entonces:
  - "todo paso declara termina_cuando"
  - "ningún paso delega el criterio en lugar de escribirlo"
falla_si: ["un paso carece de condición de salida comprobable"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T91"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```

```yaml ads:escenario
id: T92
nombre: El kernel es portable porque ningún contrato exige una marca
cubre: ["K0.8", "C2 regla de portabilidad"]
dado: ["todo el contenido de kernel/operativo y packs, excluido el legado 1.3.0"]
cuando: ["se busca cualquier nombre comercial de proveedor o de modelo"]
entonces:
  - "no aparece ninguno como requisito"
  - "la única excepción declarada es C2, que habla precisamente del adaptador"
falla_si: ["un rol, método, gate o pack exige un proveedor o modelo concreto"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T92"
estado: prueba-superada
evidencia: "evidencia/T086-T092-salida.txt"
```
