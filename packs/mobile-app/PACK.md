# PACK · mobile-app — aplicaciones móviles

El dispositivo es de otro, va en su bolsillo, se interrumpe constantemente y tiene batería
finita. **No se ata a ninguna tecnología**: las tecnologías pertenecen al PROFILE del
proyecto o a una extensión específica, nunca al pack universal de la clase.

```yaml ads:pack
id: mobile-app
nombre: Aplicación móvil
version: 1.0.0
clase_de_proyecto: >
  Producto cuya superficie principal se ejecuta en un dispositivo móvil personal, con
  entrada táctil, pantalla pequeña, batería finita, conectividad variable y un sistema
  operativo que puede detener la aplicación en cualquier momento.
restricciones:
  - "el sistema operativo puede suspender o terminar la aplicación en cualquier momento"
  - "la interacción es táctil: no hay puntero preciso ni estado de hover"
  - "el teclado ocupa media pantalla cuando aparece"
  - "los permisos los concede el usuario, puede negarlos y puede revocarlos después"
  - "la conectividad va y viene, y a veces está pero no sirve"
  - "la batería es finita y el usuario nota lo que la consume"
  - "el uso es interrumpido: llamadas, notificaciones, cambiar de aplicación y volver"
  - "el tamaño de pantalla y la densidad varían mucho entre dispositivos reales"
capacidades_nuevas: []
roles_nuevos: [mob:DIS/interaccion-tactil, mob:CON/ciclo-de-vida]
extensiones_de_metodo:
  - "DIS/Evolucion paso 1: comprobar además si la superficie recibe el teclado, que cambia la composición a la mitad"
  - "DIS/ValidacionDeUso paso 2: el recorrido se hace SIEMPRE en dispositivo real, no en emulador"
  - "DIS/RevisionDeFidelidad paso 5: la prueba en dispositivo real es OBLIGATORIA, sin excepción"
  - "CON/Implementacion paso 4: comprobar además el comportamiento con permiso denegado y revocado"
  - "VER/Dosier paso 3: los estados extremos incluyen sin conexión, sin permiso y tras suspensión"
  - "ENT/Despliegue: la distribución pasa por una tienda con sus tiempos, y eso condiciona la reversión"
gates_adicionales: [gate:mob-dispositivo-real, gate:mob-ciclo-y-permisos, gate:mob-consumo]
artefactos:
  - "matriz de dispositivos reales declarada por el proyecto"
  - "grabación en dispositivo real de cada recorrido principal"
  - "capturas con el teclado abierto en las superficies que lo reciben"
  - "evidencia del comportamiento con permiso denegado y con permiso revocado"
  - "evidencia del retorno tras suspensión larga"
  - "medición de consumo en las operaciones declaradas costosas"
herramientas:
  - "dispositivos físicos de la matriz, al menos uno de gama baja"
  - "grabación de pantalla desde el dispositivo"
  - "forzado de suspensión y terminación por el sistema"
  - "medición de consumo con el dispositivo desconectado de la corriente"
  - "simulación de red degradada y de ausencia de conexión"
  - "lector de pantalla de la plataforma para la comprobación de accesibilidad"
matriz_entornos: >
  El proyecto declara la matriz de dispositivos REALES: al menos uno de gama baja y uno
  reciente, con sus versiones de sistema. El pack exige que la evidencia se recoja en
  hardware real y que el emulador NO sustituya a la prueba en dispositivo.
propiedades_medibles:
  - id: objetivo-tactil-minimo
    nombre: tamaño mínimo del objetivo táctil
    unidad: dp
    direccion: minimo
    valor: 44
    fija_el_profile: false
    motivo: >
      Es propiedad del medio táctil con pulgar sobre pantalla de teléfono. El proyecto puede
      exigir más; no puede exigir menos.
  - id: contraste-minimo
    nombre: relación de contraste mínima del texto
    unidad: ratio
    direccion: minimo
    fija_el_profile: true
    motivo: >
      El umbral depende del nivel de accesibilidad declarado por el proyecto; el pack fija
      QUÉ se mide y en qué entornos.
pruebas: [T125, T126, T127]
antipatrones:
  - "validar en emulador lo que se ejecutará en un dispositivo de gama baja"
  - "diseñar el camino feliz y no el permiso denegado"
  - "perder lo escrito cuando el sistema suspende la aplicación"
  - "objetivos táctiles pequeños o pegados al borde donde vive el pulgar"
  - "diseñar como si el teclado no ocupara media pantalla"
  - "asumir que hay conexión porque el icono dice que la hay"
  - "consumir batería en segundo plano sin que el usuario pueda saberlo"
  - "gestos que no tienen equivalente alcanzable de otra forma"
no_toca:
  - "los contratos universales del kernel"
  - "la autoridad de ninguna capacidad"
  - "la elección de tecnología: pertenece al PROFILE o a una extensión específica"
  - "los dos gates de Diseño: los amplía"
compatible_con: [web-app, wear-os]
precedencia: >
  Con web-app comparte dominio y dirección visual, no matriz ni presupuestos. Con wear-os
  es la pieza central y su entrega va COORDINADA con la del reloj. Ver packs/COMPOSICION.md.
```

## Lo que este pack añade, por materia

### Navegación

```text
[ ] el gesto de volver del sistema hace lo que el usuario espera, siempre
[ ] la profundidad de navegación es alcanzable con una mano
[ ] volver a la aplicación tras una interrupción deja al usuario DONDE ESTABA
```

### Gestos

```text
TODO GESTO tiene un camino alternativo alcanzable. Un gesto es un atajo, nunca la única vía.
TODO GESTO se descubre: o es convencional en la plataforma, o la interfaz lo enseña.
NINGÚN GESTO destruye sin poder deshacerse.
```

### Tamaños de pantalla y orientación

```text
El tamaño NO es un conjunto de dispositivos: es un rango con densidades distintas.
Se comprueba en el más pequeño de la matriz y en uno grande, con datos reales.
La orientación: o se soporta y se diseña, o se bloquea y se declara por qué.
```

### Teclado

Ocupa **media pantalla** y aparece encima de lo que el usuario está mirando.

```text
[ ] el campo enfocado sigue siendo visible con el teclado abierto
[ ] la acción de confirmar es alcanzable sin cerrar el teclado
[ ] el tipo de teclado corresponde al campo: número, correo, texto
[ ] cerrar el teclado NO pierde lo escrito
```

### Permisos

**Tres estados, y los tres se diseñan**: concedido, denegado, revocado después.

```text
[ ] se pide el permiso CUANDO se necesita, explicando para qué, no al abrir
[ ] denegado: la aplicación sigue siendo útil, y se dice qué no funcionará
[ ] revocado después: la aplicación se entera y se recupera, sin romperse
[ ] existe un camino para reconsiderar, sin instrucciones de sistema operativo en un texto
```

### Cámara y sensores

```text
[ ] cada sensor declara qué se hace con el dato y durante cuánto tiempo se conserva  ← SEG
[ ] el sensor no disponible o denegado tiene camino alternativo o mensaje útil
[ ] la captura se puede repetir: nadie acierta a la primera
```

### Conectividad y offline

```text
CONECTADO      el caso fácil, y el único que se prueba si nadie lo impide
SIN CONEXIÓN   qué se puede seguir haciendo, y qué queda pendiente de sincronizar
CONEXIÓN MALA  peor que sin conexión: parece que hay red y las operaciones no terminan
VUELVE         se sincroniza, y se dice qué pasó con lo que quedó pendiente

Lo escrito por el usuario NO SE PIERDE en ninguno de los cuatro.
```

### Ciclo de vida

Es la materia que más fallos silenciosos produce, y por eso tiene rol propio:
`mob:CON/ciclo-de-vida`.

```text
[ ] la aplicación suspendida y reanudada vuelve al mismo estado
[ ] la aplicación TERMINADA por el sistema y reabierta no pierde lo escrito
[ ] una operación en curso al suspender: termina, se reanuda o se declara perdida — nunca queda a medias en silencio
[ ] volver desde una notificación lleva al sitio correcto
```

### Rendimiento y consumo

```text
SE MIDE   tiempo hasta la primera pantalla utilizable, EN EL DISPOSITIVO MÁS LENTO de la matriz
SE MIDE   fluidez de las transiciones en ese mismo dispositivo
SE MIDE   consumo de las operaciones declaradas costosas
SE MIDE   trabajo en segundo plano: qué hace, cuándo y con qué coste
```

### Accesibilidad táctil

```text
[ ] los objetivos táctiles alcanzan el tamaño mínimo declarado por el proyecto
[ ] no hay objetivos pegados entre sí donde el error es sistemático
[ ] la superficie funciona con el texto ampliado del sistema
[ ] la superficie funciona con el lector de pantalla de la plataforma
[ ] la superficie funciona con el movimiento reducido activado
```

### Notificaciones

```text
[ ] cada notificación dice qué ha pasado y lleva a un sitio concreto
[ ] el usuario puede desactivarlas por tipo, no todo o nada
[ ] no se usan para reclamar atención sin que haya ocurrido nada
```

### Distribución

```text
La tienda impone tiempos que el equipo no controla.
Eso cambia la REVERSIÓN: revertir no es desplegar la versión anterior, es publicar una
nueva. ENT lo declara en su procedimiento ANTES de la primera publicación.
```

### Pruebas en dispositivo real

```text
OBLIGATORIO en la revisión de fidelidad y en la validación de uso.
El emulador vale para construir. NO vale como evidencia.
Un movimiento aprobado en emulador puede dar tirones en el dispositivo del Owner, y ahí
es donde se juzgará el producto.
```

## Índice del pack

| | |
|---|---|
| roles especializados | [`interaccion-tactil`](roles/interaccion-tactil.md) · [`ciclo-de-vida`](roles/ciclo-de-vida.md) |
| gates adicionales | [`gates/gates.md`](gates/gates.md) |
| especialización de Diseño | [`diseno/especializacion.md`](diseno/especializacion.md) |
| ejemplos de composición | [`composicion.md`](composicion.md) |
