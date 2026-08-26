# T122–T133 — conformidad de los packs

Las pruebas que los tres packs declaran, más las de composición entre ellos. Su estado real
está en [`REGISTRO-generado.md`](REGISTRO-generado.md).

> Ninguna está ejecutada: todas exigen un proyecto real con superficie construida, y varias
> exigen hardware físico que esta iteración no tiene.

```yaml ads:escenario
id: T122
nombre: Toda la matriz de navegadores tiene evidencia
cubre: ["web-app", "gate:web-accesibilidad", "VER/Dosier"]
dado: ["un proyecto web con dos motores y dos tamaños extremos declarados"]
cuando: ["una superficie llega a verificación"]
entonces: ["existe captura de esa superficie en cada motor y en los dos tamaños extremos"]
falla_si: ["la evidencia cubre un solo motor, o sólo un tamaño"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T123
nombre: El recorrido completo se hace con teclado solo
cubre: ["web-app", "gate:web-accesibilidad"]
dado: ["una superficie web con acciones"]
cuando: ["se ejecuta el recorrido principal usando únicamente el teclado"]
entonces: ["todas las acciones se completan y el foco es visible en cada parada"]
falla_si: ["alguna acción sólo se alcanza con puntero, o el foco desaparece en algún punto"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T124
nombre: Lo escrito sobrevive a un fallo de red
cubre: ["web-app", "gate:web-estados-de-red", "web:CON/estados-de-red"]
dado: ["un formulario largo con datos escritos por el usuario"]
cuando: ["se corta la red y se intenta enviar"]
entonces: ["lo escrito sigue disponible al restaurarse la red, sin que el usuario lo repita"]
falla_si: ["se pierde lo escrito", "se reintenta una operación no idempotente sin consultar a DOM"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T125
nombre: El emulador no sustituye al dispositivo real
cubre: ["mobile-app", "gate:mob-dispositivo-real"]
dado: ["una superficie móvil con transiciones especificadas"]
cuando: ["se recoge la evidencia de fidelidad y de validación"]
entonces: ["toda la evidencia declara el dispositivo físico donde se obtuvo, incluido el más lento de la matriz"]
falla_si: ["alguna pieza de evidencia procede de un emulador"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T126
nombre: La terminación forzada no pierde el trabajo del usuario
cubre: ["mobile-app", "gate:mob-ciclo-y-permisos", "mob:CON/ciclo-de-vida"]
dado: ["una aplicación móvil con estado de trabajo del usuario"]
cuando: ["el sistema termina la aplicación y el usuario la reabre"]
entonces: ["lo escrito sigue ahí y el usuario vuelve donde estaba"]
falla_si: ["se pierde lo escrito", "la prueba se hizo cerrando la aplicación en vez de forzando la terminación"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T127
nombre: Los tres estados de cada permiso están resueltos
cubre: ["mobile-app", "gate:mob-ciclo-y-permisos"]
dado: ["una aplicación que pide al menos un permiso"]
cuando: ["se recorre con el permiso concedido, denegado y revocado después"]
entonces: ["en los tres casos la aplicación es utilizable y dice qué no funcionará"]
falla_si: ["sólo está resuelto el caso concedido", "la aplicación se rompe al revocarse el permiso"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T128
nombre: La superficie del reloj se entiende en el tiempo declarado
cubre: ["wear-os", "gate:wear-vistazo", "wear:DIS/lectura-de-un-vistazo"]
dado: ["una superficie de reloj que declara cuántos segundos dura su uso"]
cuando: ["alguien que no la conoce la usa en reloj real, andando"]
entonces: ["consigue lo declarado dentro del tiempo declarado"]
falla_si: ["tarda más del tiempo declarado", "la validación se hizo sentado o en emulador"]
ejecucion: requiere-juicio-humano
estado: contrato-definido
```

```yaml ads:escenario
id: T129
nombre: Volver del ambiental no reinicia el trabajo
cubre: ["wear-os", "gate:wear-ambiental", "wear:CON/energia-y-estados"]
dado: ["una tarea en curso en el reloj"]
cuando: ["el usuario baja la muñeca, la pantalla entra en ambiental y vuelve"]
entonces: ["la tarea sigue donde estaba y el ambiental mostró la información principal"]
falla_si: ["la tarea se reinicia", "el ambiental sólo mostraba un elemento decorativo"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T130
nombre: El consumo se mide sin cargador y en reloj real
cubre: ["wear-os", "gate:wear-consumo"]
dado: ["una aplicación de reloj con actualizaciones o sensores"]
cuando: ["se mide su consumo"]
entonces: ["la medición se hizo en reloj físico desconectado del cargador, y está registrada"]
falla_si: ["se midió con el reloj cargando", "se midió en emulador", "algún sensor quedó fuera de su ciclo declarado"]
ejecucion: guion-manual
estado: contrato-definido
```

```yaml ads:escenario
id: T131
nombre: Lo más restrictivo gana entre dos packs
cubre: ["packs/COMPOSICION", "precedencia P1", "T18"]
dado: ["dos packs instalados que fijan valores distintos para la misma propiedad medible"]
cuando: ["SIS ejecuta la detección de conflictos"]
entonces: ["se aplica el valor más restrictivo y queda registrado cuál ganó y por qué"]
falla_si: ["se aplica el menos restrictivo", "el conflicto no queda registrado"]
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_packs.py"
estado: prueba-superada
evidencia: "evidencia/T131-T132-salida.txt"
```

```yaml ads:escenario
id: T132
nombre: Un rol de pack no reclama autoridad de un rol del kernel
cubre: ["packs/00-QUE-ES-UN-PACK", "T18", "C1"]
dado: ["un pack que aporta roles especializados"]
cuando: ["se instala y se comprueba su conformidad"]
entonces:
  - "todo rol de pack usa prefijo de espacio de nombres"
  - "ningún rol de pack reclama autoridad que un rol del kernel ya tiene"
  - "ningún gate de pack sustituye a uno del kernel: se suma"
falla_si:
  - "un rol de pack sin prefijo"
  - "un rol de pack que decide lo que decide un rol del kernel"
  - "un gate de pack que rebaja una comprobación del kernel"
ejecucion: validador-estructural
validador: "kernel/operativo/validadores/comprobar_packs.py"
estado: prueba-superada
evidencia: "evidencia/T131-T132-salida.txt"
```

```yaml ads:escenario
id: T133
nombre: La entrega móvil-reloj admite versiones distintas conviviendo
cubre: ["wear-os", "mobile-app", "packs/COMPOSICION"]
dado: ["un producto con aplicación móvil y aplicación de reloj"]
cuando: ["se publica una versión nueva de una de las dos"]
entonces:
  - "el reloj con la versión anterior y el móvil con la nueva siguen funcionando"
  - "la ventana de observación de ENT cubre las dos aplicaciones"
falla_si:
  - "una versión deja a la otra sin poder operar"
  - "revertir una obliga a revertir la otra sin que estuviera previsto"
ejecucion: guion-manual
estado: contrato-definido
```
