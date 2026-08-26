# T86–T92 — conformidad estructural de los contratos

Siete propiedades que los contratos C1–C5 declaran obligatorias y que **no necesitan
runtime** para comprobarse. Por eso son las primeras pruebas del sistema que llegan a
**PRUEBA SUPERADA** con evidencia real.

```bash
python3 kernel/operativo/validadores/comprobar_contratos.py
```

Salida registrada: [`evidencia/contratos-salida.txt`](evidencia/contratos-salida.txt).

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
evidencia: "evidencia/contratos-salida.txt"
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
evidencia: "evidencia/contratos-salida.txt"
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
evidencia: "evidencia/contratos-salida.txt"
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
evidencia: "evidencia/contratos-salida.txt"
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
evidencia: "evidencia/contratos-salida.txt"
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
evidencia: "evidencia/contratos-salida.txt"
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
evidencia: "evidencia/contratos-salida.txt"
```

---

## T134 — añadida por la revisión adversarial

La revisión adversarial del conjunto encontró **siete documentos que nadie enlazaba y cuyos
bloques nadie citaba**: existían para nadie. Se corrigió la navegación, y la comprobación
quedó como prueba permanente para que el hallazgo no pueda repetirse en silencio.

> **T134 quedó sustituida por T147.** Decidía que un documento tenía enlace entrante
> buscando su NOMBRE BASE como subcadena en cualquier otro fichero. Como el corpus da a
> propósito el mismo nombre a los ficheros homólogos de cada capacidad, una sola mención
> satisfacía a todos: 119 de 188 documentos quedaban exentos sin declararlo (hallazgo
> **A-05**). Su sustituta construye el grafo por RUTA NORMALIZADA y vive en
> [`T136-T152-post-auditoria.md`](T136-T152-post-auditoria.md).


---

## T135 — añadida por la revisión adversarial

La revisión encontró cuatro roles que juzgan trabajo ajeno y cuyo contrato no exige
independencia, cubiertos en cambio por sus composiciones. Eso es correcto —**el contrato
fija el mínimo y la composición puede exigir más**— pero nada comprobaba la dirección
contraria: que ninguna composición **rebajara** lo que un contrato exige. Ahora sí.

```yaml ads:escenario
id: T135
nombre: Ninguna composición rebaja la independencia que exige un contrato
cubre: ["C1 independencia", "C4 paso 5", "G13"]
dado: ["todos los contratos de rol y todas las composiciones del corpus"]
cuando: ["se cruza cada pareja declarada combinable con la independencia exigida por cada contrato"]
entonces: ["ninguna composición combina dos roles que un contrato declara independientes"]
falla_si: ["una composición permite compartir agente entre un rol y otro del que su contrato exige independencia"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py --prueba T135"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```
