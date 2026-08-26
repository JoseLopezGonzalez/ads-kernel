# PACK · web-app — aplicaciones web

El entorno es **el navegador de otro**: no controlas su versión, su tamaño, su red, sus
extensiones ni su configuración de accesibilidad. Todo lo que este pack añade sale de ahí.

```yaml ads:pack
id: web-app
nombre: Aplicación web
version: 1.0.0
clase_de_proyecto: >
  Producto cuya superficie principal se ejecuta en un navegador que el equipo no controla,
  con entrada de teclado y puntero, tamaños de ventana variables y red no garantizada.
restricciones:
  - "el navegador y su versión los elige el usuario: la matriz de navegadores es del proyecto, no del equipo"
  - "el tamaño de la ventana es continuo, no un conjunto de dispositivos"
  - "la red puede ser lenta, intermitente o estar caída a mitad de una operación"
  - "el usuario puede tener el texto ampliado, el contraste aumentado o el movimiento reducido"
  - "el usuario puede abrir dos pestañas de la misma aplicación y operar en las dos"
  - "el historial del navegador es parte de la navegación: atrás y adelante deben funcionar"
  - "el contenido puede imprimirse o exportarse, y eso es otra superficie"
capacidades_nuevas: []
roles_nuevos: [web:DIS/densidad-y-tablas, web:CON/estados-de-red]
extensiones_de_metodo:
  - "DIS/Evolucion paso 1: comprobar además si la superficie tiene tabla o formulario, que tienen sus propios patrones"
  - "DIS/ValidacionDeUso paso 2: el recorrido por medio de entrada incluye SIEMPRE teclado solo, sin puntero"
  - "VER/Dosier paso 2: la regresión visual se ejecuta en cada navegador de la matriz declarada"
  - "VER/Dosier paso 4: las mediciones incluyen los presupuestos de rendimiento percibido de este pack"
  - "ENT/Despliegue paso 2: las señales incluyen errores de cliente por versión de navegador"
gates_adicionales: [gate:web-accesibilidad, gate:web-rendimiento-percibido, gate:web-estados-de-red]
artefactos:
  - "matriz de navegadores y tamaños declarada por el proyecto"
  - "capturas de cada superficie en cada navegador y en los tamaños extremos de la matriz"
  - "grabación del recorrido completo con teclado solo"
  - "medición de los presupuestos de rendimiento percibido"
  - "captura de la superficie de impresión o exportación, cuando existe"
herramientas:
  - "navegador automatizable para captura y recorrido"
  - "comprobación automática de accesibilidad"
  - "medición de rendimiento en el navegador"
  - "simulación de red lenta e intermitente"
matriz_entornos: >
  El proyecto declara la matriz: qué navegadores, qué versiones mínimas y qué tamaños. El
  pack exige que existan al menos dos motores distintos y dos tamaños extremos —el más
  estrecho soportado y uno amplio—, y que toda captura de evidencia cubra la matriz entera.
propiedades_medibles:
  - id: objetivo-tactil-minimo
    nombre: tamaño mínimo del objetivo táctil
    unidad: dp
    direccion: minimo
    valor: 24
    fija_el_profile: false
    motivo: >
      Una web puede usarse con puntero preciso, y por eso su suelo es menor que el de un
      medio exclusivamente táctil. Sigue siendo un suelo: por debajo, el error de pulsación
      deja de ser accidental y pasa a ser sistemático.
  - id: contraste-minimo
    nombre: relación de contraste mínima del texto
    unidad: ratio
    direccion: minimo
    fija_el_profile: true
    motivo: >
      Lo fija el nivel de accesibilidad que el proyecto declare exigible; el pack fija que
      se mide y con qué herramienta.
pruebas: [T122, T123, T124]
antipatrones:
  - "diseñar para tres tamaños fijos y llamarlo responsive: el tamaño es continuo"
  - "resolver la adaptación quitando funciones en pantallas estrechas"
  - "formularios que pierden lo escrito al fallar el envío"
  - "tablas que truncan sin dar acceso al valor completo"
  - "estados de carga que saltan y desplazan el contenido ya leído"
  - "acciones que sólo se alcanzan con puntero"
  - "romper el botón atrás del navegador"
  - "medir el rendimiento sólo en la máquina de desarrollo, con red local"
no_toca:
  - "los contratos universales de rol, método, gate y handoff del kernel"
  - "la autoridad de ninguna capacidad del kernel"
  - "los dos gates de Diseño: los amplía con gates adicionales, no los sustituye"
  - "la elección de tecnología: pertenece al PROFILE del proyecto"
compatible_con: [mobile-app, wear-os]
precedencia: >
  Cuando convive con mobile-app, cada pack gobierna su propia superficie y ninguno impone su
  matriz al otro. Lo compartido —modelo de dominio, contratos, criterios de éxito— pertenece
  al kernel y a las capacidades, no a los packs. Ver packs/COMPOSICION.md.
```

## Lo que este pack añade, por materia

### Responsive: el tamaño es continuo

```text
PROHIBIDO   diseñar para tres tamaños de dispositivo
OBLIGATORIO declarar los puntos de adaptación por CONTENIDO: dónde la composición deja de
            funcionar, no dónde cambia un dispositivo de moda

Se comprueba: la superficie funciona en el tamaño MÁS ESTRECHO soportado y en uno amplio,
y en el punto intermedio donde la composición cambia.
```

### Navegadores

Al menos **dos motores distintos** en la matriz. La regresión visual se ejecuta en todos, y
las diferencias aceptadas se declaran; no se descubren en producción.

### Teclado y ratón

```text
TODO recorrido principal se completa CON TECLADO SOLO. Sin excepción.
El foco es visible SIEMPRE, y su orden sigue el orden de lectura.
Ninguna acción existe sólo al pasar el puntero por encima.
```

### Estados de red

Cinco, y los cinco se diseñan:

```text
lenta          la espera se comunica y el usuario sabe cuánto falta o qué está pasando
intermitente   la operación se recupera o dice qué hacer; no se queda a medias en silencio
caída          se puede seguir leyendo lo que ya está, y se dice qué no funcionará
falla a mitad  lo escrito NO SE PIERDE
vuelve         lo que quedó pendiente se reconcilia, o se dice que hay que repetirlo
```

### Formularios

```text
[ ] lo escrito sobrevive a un error de envío
[ ] los errores se muestran junto al campo y en un resumen alcanzable con teclado
[ ] la validación no impide escribir: corrige al terminar el campo, no en cada tecla
[ ] los campos declaran su formato ANTES de que el usuario se equivoque
[ ] un formulario largo se puede abandonar y retomar, o dice expresamente que no
```

### Tablas y densidad

Es la superficie donde más se nota la diferencia entre un producto trabajado y uno genérico,
y por eso tiene rol propio: `web:DIS/densidad-y-tablas`.

```text
[ ] una línea de datos domina la fila; el resto se atenúa hasta que se necesita
[ ] el nombre más largo real NO se trunca sin dar acceso al valor completo
[ ] la ordenación y el filtro dicen qué está aplicado, y se pueden quitar
[ ] el vacío, el uno y el máximo están resueltos con datos reales
[ ] la cabecera sigue siendo legible al desplazar, o se declara por qué no
```

### Navegación

```text
[ ] el botón atrás del navegador funciona y hace lo que el usuario espera
[ ] la dirección refleja el estado: se puede compartir y recargar sin perderlo
[ ] dos pestañas de la misma aplicación no se corrompen entre sí
```

### Rendimiento percibido

El pack fija **qué se mide**; el PROFILE fija el umbral cuando depende del producto.

```text
SE MIDE   tiempo hasta la primera respuesta visible tras una acción
SE MIDE   tiempo hasta que la superficie principal es utilizable
SE MIDE   desplazamiento del contenido ya leído durante la carga: debe ser cero
SE MIDE   respuesta a la interacción durante una operación en curso
```

### Escritorio y móvil

Son **la misma aplicación en tamaños distintos**, no dos productos. Lo que cambia es
composición, densidad y navegación. Lo que **no** cambia es el alcance: si una función sobra
en móvil, sospecha que sobra en escritorio, y dilo.

### Despliegue y observación

```text
[ ] el despliegue no deja a un usuario con una versión a medias entre dos pestañas
[ ] las señales incluyen errores de cliente agrupados POR VERSIÓN DE NAVEGADOR
[ ] existe forma de volver a la versión anterior sin esperar a un nuevo despliegue
```

## Índice del pack

| | |
|---|---|
| roles especializados | [`densidad-y-tablas`](roles/densidad-y-tablas.md) · [`estados-de-red`](roles/estados-de-red.md) |
| gates adicionales | [`gates/gates.md`](gates/gates.md) |
| especialización de Diseño | [`diseno/especializacion.md`](diseno/especializacion.md) |
| ejemplos de composición | [`composicion.md`](composicion.md) |
