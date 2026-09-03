# T240–T248 — los hallazgos EXTERNOS y la deuda declarada con fase `F6`

**Qué cierran.** La entrega `F6-H` del plan de implementación de `F5`-`F6`: *«los hallazgos EXTERNOS
con propietario y fase `F6`, que tocan kernel, esquemas, circuitos y pruebas»*. Su sede es
la tabla «Lo que esta fase NO puede corregir, con su propietario y su fase» de `11-ARQ` §19,
y su censo lo publica `06-DEUDA-Y-LIMITACIONES-VIGENTES.md` §7. **Ninguno de los dos
documentos se enlaza desde aquí**: son historia del kernel y no viajan al proyecto
instalado, y un enlace roto en el proyecto instalado es el defecto que `E5` destapó.

**Una prueba por fila, y ninguna comprueba que el texto esté escrito: comprueban la
PROPIEDAD**, de modo que reintroducir el defecto las pone en rojo.

> **Todas llevan prueba negativa, y son SABOTAJES ejecutados.** Cada una tiene al menos una
> infracción deliberada en
> [`../validadores/comprobar_negativos.py`](../validadores/comprobar_negativos.py), que se
> aplica sobre una COPIA temporal del repositorio —el corpus real no se toca— y exige que la
> prueba señalada FALLE, y que falle **por el motivo esperado**. CATORCE infracciones
> para siete pruebas: `N240`, `N240b`, `N240c`, `N240d`, `N240e`, `N241`, `N241b`, `N242`,
> `N242b`, `N242c`, `N243`, `N244`, `N245` y `N246`. `T247` y `T248` llevan el suyo aparte:
> el sabotaje que desenchufa la política de contención del adaptador, ejecutado sobre una
> copia, deja las dos en rojo.

**`T247` y `T248` no son de §19: son de `FD-5`**, la deuda que `06-DEUDA` §10 bis
registra con propietario `PLT` y fase `F6`. Están aquí porque cierran la misma clase
de laguna: una deuda cerrada en el paquete y abierta en el sitio donde está escrita.

**Qué NO cierran.** `F-08` no está aquí: su fase es `F5` y su propietario es el Owner, y
`O23` §10 ya emitió su nota de vigencia. `F-03` y `F-09` no existen en la tabla.

```yaml ads:escenario
id: T240
nombre: Ninguna tabla de participación nombra un método donde va una capacidad
cubre: ["F-01", "F-02", "PN-14", "E4.3", "esquemas/proceso.yaml"]
dado:
  - "el esquema de proceso tipa capacidad y capacidad_productora como ref_a capacidad"
  - "las variantes admitidas están declaradas una a una en el esquema"
cuando: ["se recorren los diez bloques ads:proceso y el esquema que los gobierna"]
entonces:
  - "ninguna capacidad ni capacidad productora contiene una barra"
  - "toda base es una de las quince capacidades declaradas"
  - "toda variante con sufijo está en el conjunto que el esquema declara"
  - "OWNER se declara en su campo de autoridad propio y no como capacidad"
falla_si:
  - "vuelve a aparecer DIS/Reconstruccion o cualquier otro método donde va una capacidad"
  - "el esquema deja de tipar el campo y admite texto libre"
  - "entra una variante que el esquema no declara"
  - "OWNER viaja como si fuera una de las quince"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T241
nombre: La entrega de DIS a VER está anclada a una estación del ciclo de calidad
cubre: ["F-06", "diseno/04-CICLO-DE-CALIDAD", "02-RUBRICAS las dos pasadas", "handoff:dis-a-ver"]
dado:
  - "el ciclo de calidad declara sus estaciones y el gate visual tiene DOS pasadas"
  - "el eje fidelidad no tiene nivel hasta que hay construcción que comparar"
cuando: ["se lee el cuando y la entrega de handoff:dis-a-ver"]
entonces:
  - "el cuando nombra una estación que el ciclo de calidad declara"
  - "la entrega dice de qué pasada procede el dictamen visual y de qué estación el de usabilidad"
falla_si:
  - "el cuando vuelve a decir sólo que DIS cierra su capa"
  - "el cuando cita una estación que el ciclo no tiene"
  - "el dictamen se entrega sin decir de qué pasada procede"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T242
nombre: Todo documento del Owner declara su autoridad y no la elige, la deriva
cubre: ["F-07", "O10", "V6-12", "FUENTES-CANONICAS.yml", "exclusiones.yaml"]
dado:
  - "docs/owner/ contiene material aprobado y material de trabajo, y hasta ahora la distinción vivía sólo en prosa"
  - "el registro canónico de zonas clasifica cada ruta, y de esa clase se deriva la autoridad"
cuando: ["se recorre el directorio del Owner y se contrasta cada declaración con su clase canónica"]
entonces:
  - "todo fichero de docs/owner/ tiene autoridad declarada, con su motivo escrito"
  - "el valor declarado coincide con el que la clase canónica deriva"
  - "ninguna declaración apunta a un fichero que no existe"
falla_si:
  - "un documento del Owner pasa por omisión, sin autoridad declarada"
  - "alguien escribe una autoridad distinta de la que su clase canónica deriva"
  - "la declaración desaparece y la distinción vuelve a estar sólo en prosa"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T243
nombre: Las cinco entregas que 11-ARQ 8.0 declara existen como instancias en circuitos
cubre: ["F-05", "11-ARQ 8.0", "C5", "circuitos/entregas-de-8-0.md"]
dado:
  - "11-ARQ 8.0 declara qué viaja de SIS a PLT, de SIS a CON, de SIS a VER, de CON a ENT y de ENT a VER"
  - "el documento no viaja al proyecto instalado, y por eso el conjunto se lleva como dato derivado"
cuando: ["se recorren las instancias de handoff declaradas en circuitos/"]
entonces:
  - "cada una de las cinco entregas tiene su instancia con los campos que C5 exige"
  - "el dato derivado sigue coincidiendo con el documento cuando el documento está presente"
falla_si:
  - "desaparece una de las cinco instancias"
  - "una instancia deja vacío un campo que C5 exige"
  - "el documento declara un conjunto distinto del que el kernel lleva"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T244
nombre: El grado inicial del escenario coincide con el grado que midió su paso 5
cubre: ["F-04", "T75", "A-14", "entrada/04-INCERTIDUMBRE-Y-CONFIRMACION"]
dado:
  - "el paso de incertidumbre del escenario publica un GRADO GLOBAL medido eje a eje"
  - "el encuadre resultante persiste grado y grado_inicial"
cuando: ["se contrasta el grado inicial persistido con el grado global que midió el paso 5"]
entonces:
  - "grado_inicial es el grado con el que la expresión entró, no el que tiene al final"
  - "grado se conserva junto a grado_inicial"
falla_si:
  - "grado_inicial difiere del grado global del paso 5"
  - "el escenario deja de publicar el grado global que midió"
  - "el encuadre pierde grado o grado_inicial"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_contratos.py"
estado: prueba-superada
evidencia: "evidencia/contratos-salida.txt"
```

```yaml ads:escenario
id: T245
nombre: Ninguna cabecera afirma una correspondencia uno a uno entre formas y clases
cubre: ["F-10", "A-24", "entrada/03-FORMAS", "entrada/01-TAXONOMIA"]
dado:
  - "las formas de conversación y las clases de expresión se derivan del corpus y son cifras distintas"
  - "la misma aposición es CIERTA cuando se predica de las clases de entrada"
cuando: ["se busca la aposición y se mira de qué se predica la frase que la contiene"]
entonces:
  - "ninguna frase que hable de formas de conversación afirma una por clase de expresión"
  - "la frase que DESMIENTE la aposición no se cuenta como infracción"
  - "la regla se apaga sola si algún día los dos cardinales coinciden"
falla_si:
  - "una cabecera vuelve a afirmar catorce formas, una por clase de expresión"
  - "la comprobación se apoya en un cardinal escrito a mano en vez de derivarlo"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T246
nombre: La cabecera de los escenarios enumera las pruebas que el fichero contiene
cubre: ["F-11", "A-24", "entrada/05-ESCENARIOS", "pruebas/T081-T085-reanudacion-ENC"]
dado:
  - "el fichero de escenarios contiene sus pruebas como bloques con identificador"
  - "la cabecera puede citarlas por rangos, y un rango cita todo lo que hay entre sus extremos"
cuando: ["se expanden los rangos de la cabecera y se contrastan con los identificadores del fichero"]
entonces:
  - "la cabecera no nombra ninguna prueba que el fichero no contenga"
  - "el fichero no contiene ninguna prueba que la cabecera calle"
  - "lo que la cabecera declara que vive en otro fichero no está aquí"
falla_si:
  - "la cabecera vuelve a afirmar un rango que el fichero no contiene"
  - "el fichero gana una prueba y la cabecera no la enumera"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_recuentos.py"
estado: prueba-superada
evidencia: "evidencia/recuentos-salida.txt"
```

```yaml ads:escenario
id: T247
nombre: El bisnieto con setsid no escapa al adaptador con política de contención
cubre: ["FD-5", "CONTRATO-ADAPTADOR 2", "CONTRATO-CONTENCION", "T215"]
dado:
  - "el adaptador de proceso local recibe una politica_de_contencion de nivel arbol-de-procesos"
  - "la tarea engendra hijo, nieto y bisnieto, y los tres hacen setsid"
cuando: ["la tarea entra por AdaptadorDeProcesoLocal.ejecutar y vence su límite"]
entonces:
  - "el resultado declara el nivel de aislamiento MEDIDO y el backend que lo dio"
  - "ninguna de las tres generaciones sobrevive, con CADA backend fuerte disponible en el anfitrión"
  - "donde el anfitrión no ofrece contención fuerte, la prueba lo declara en vez de pasar por no mirar"
falla_si:
  - "el adaptador deja de enchufar la política y vuelve a contener sólo por grupo de procesos"
  - "una generación sobrevive al vencimiento con política fuerte"
  - "se prueba un solo backend y se declara la clase entera"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_adaptadores.py"
estado: prueba-superada
evidencia: "evidencia/adaptadores-salida.txt"
```

```yaml ads:escenario
id: T248
nombre: Sin backend fuerte el adaptador no ejecuta y falla cerrado
cubre: ["FD-5", "CONTRATO-CONTENCION", "T216"]
dado:
  - "una política que exige arbol-de-procesos y un anfitrión sin ningún backend fuerte"
cuando: ["se pide al adaptador ejecutar una orden que dejaría un testigo en disco"]
entonces:
  - "la elección levanta ContencionFuerteNoDisponible y no devuelve el backend simple"
  - "el adaptador no llega a lanzar nada y el testigo no existe"
falla_si:
  - "la ausencia de contención fuerte produce ejecución con nivel inferior"
  - "la degradación se resuelve con un aviso en vez de con una excepción"
ejecucion: requiere-runtime
validador: "kernel/operativo/runtime/pruebas/test_adaptadores.py"
estado: prueba-superada
evidencia: "evidencia/adaptadores-salida.txt"
```
