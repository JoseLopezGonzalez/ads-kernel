# PACK · wear-os — relojes

> **Un reloj no es un móvil pequeño.** Es el antipatrón central de este pack y el motivo de
> que exista un rol dedicado a impedirlo. El uso dura **segundos**, ocurre **en movimiento**,
> y la pantalla se mira **de un vistazo**, muchas veces sin poder pararse a leer.

**No se ata a gym-wear.** Este pack describe la clase; gym-wear será un perfil posterior que
lo consuma.

```yaml ads:pack
id: wear-os
nombre: Reloj
version: 1.0.0
clase_de_proyecto: >
  Producto cuya superficie principal se ejecuta en un reloj: pantalla mínima, uso de pocos
  segundos, interacción durante el movimiento, batería muy limitada y conectividad que
  depende de un teléfono o de una red que puede no estar.
restricciones:
  - "el uso típico dura entre dos y diez segundos, y ocurre levantando la muñeca"
  - "el usuario puede estar andando, corriendo, conduciendo o con las manos ocupadas"
  - "la pantalla es mínima y el dedo tapa una parte al tocar"
  - "la pantalla entra en estado ambiental y deja de mostrar lo que mostraba"
  - "la batería es el recurso más escaso: cada elemento de la interfaz tiene coste"
  - "la conectividad con el teléfono es intermitente por diseño, no por avería"
  - "la aplicación puede tener que funcionar sin el teléfono cerca"
  - "no hay teclado utilizable: la entrada de texto es la excepción, no la norma"
  - "la corona y los botones físicos son medios de entrada de primera clase"
capacidades_nuevas: []
roles_nuevos: [wear:DIS/lectura-de-un-vistazo, wear:CON/energia-y-estados]
extensiones_de_metodo:
  - "DIS/Evolucion paso 1: comprobar cuántos SEGUNDOS dura el uso previsto de esta superficie"
  - "DIS/Fundacion paso 6: cada dirección se explora directamente en el tamaño del reloj, nunca escalada desde una pantalla grande"
  - "DIS/ValidacionDeUso paso 2: el recorrido se ejecuta EN MOVIMIENTO, no sentado"
  - "DIS/RevisionDeFidelidad paso 5: en reloj real, obligatorio y sin excepción"
  - "CON/Implementacion paso 4: comprobar además el estado ambiental y el comportamiento sin teléfono"
  - "VER/Dosier paso 3: los estados extremos incluyen ambiental, sin teléfono y batería baja"
gates_adicionales: [gate:wear-vistazo, gate:wear-ambiental, gate:wear-consumo]
artefactos:
  - "matriz de relojes reales declarada por el proyecto, con tamaños y forma de pantalla"
  - "grabación del uso completo en reloj real, cronometrada"
  - "captura de cada superficie en estado ambiental"
  - "evidencia del comportamiento sin teléfono cerca"
  - "medición de consumo de la superficie y de sus actualizaciones"
  - "grabación del recorrido con corona y con botones físicos"
herramientas:
  - "relojes físicos de la matriz, con al menos un tamaño pequeño"
  - "grabación de pantalla desde el reloj"
  - "medición de consumo con el reloj desconectado del cargador"
  - "forzado del estado ambiental"
  - "capacidad de alejar el teléfono para probar el comportamiento sin él"
  - "cámara para fotografiar la pantalla a la luz del sol"
matriz_entornos: >
  El proyecto declara la matriz de relojes REALES, con al menos un tamaño pequeño y uno
  grande, y la forma de pantalla si el proyecto soporta más de una. El pack exige evidencia
  en reloj físico: ni emulador ni captura escalada la sustituyen.
pruebas: [T128, T129, T130]
antipatrones:
  - "diseñar el reloj como una reducción de la pantalla del móvil"
  - "poner más de una acción principal en una superficie"
  - "exigir leer un párrafo en una pantalla que se mira dos segundos"
  - "usar texto donde un número grande o un icono bastan"
  - "olvidar el estado ambiental y dejar la superficie en blanco"
  - "suponer que el teléfono está cerca"
  - "actualizar la superficie más de lo necesario y consumir batería en silencio"
  - "pedir entrada de texto"
  - "objetivos táctiles que el dedo tapa por completo al pulsarlos"
  - "vibrar por cosas que no requieren atención inmediata"
no_toca:
  - "los contratos universales del kernel"
  - "la autoridad de ninguna capacidad"
  - "la dirección visual del producto, que es común con el móvil cuando ambos existen"
  - "los dos gates de Diseño: los amplía"
compatible_con: [mobile-app, web-app]
precedencia: >
  Con mobile-app comparte dominio y dirección visual, y su ENTREGA VA COORDINADA: un reloj
  con una versión y un móvil con otra es el estado normal, y ambas deben convivir. Ninguna
  regla de forma del móvil se aplica al reloj. Ver packs/COMPOSICION.md.
```

## Lo que este pack añade, por materia

### El uso de pocos segundos

```text
LA PREGUNTA QUE DEFINE CADA SUPERFICIE:
  ¿cuántos segundos dura el uso previsto, y qué tiene que haber conseguido el usuario
  en ese tiempo?

Si la respuesta no cabe en una frase, la superficie está mal planteada para un reloj.
```

### Lectura de un vistazo

Tiene rol propio: `wear:DIS/lectura-de-un-vistazo`.

```text
[ ] existe UN dato dominante, legible sin enfocar
[ ] hay UNA acción principal por superficie, no dos
[ ] la información secundaria se lee DESPUÉS, si el usuario decide quedarse
[ ] el texto largo se sustituye por número, icono o estado, no se encoge
```

### Pantalla pequeña

```text
· el dedo TAPA parte de la pantalla al tocar: lo que confirma la acción no puede estar debajo
· el contenido llega a los bordes de forma distinta según la FORMA de la pantalla
· la escala tipográfica del móvil NO sirve: se define una propia para el reloj
```

### Interacción durante el movimiento

```text
[ ] las acciones se completan sin precisión fina: nada de arrastres largos ni objetivos pequeños
[ ] toda acción destructiva exige confirmación, o es deshacible
[ ] el recorrido se valida ANDANDO, no sentado en una mesa
```

### Corona y gestos

Medios de entrada **de primera clase**, no atajos:

```text
[ ] la corona recorre lo que sea largo, y su efecto es visible mientras gira
[ ] el botón físico hace lo mismo en todo el producto, sin excepciones por pantalla
[ ] todo gesto tiene alternativa alcanzable
```

### Vibración

```text
SE USA      para lo que requiere atención AHORA, o para acusar recibo de una acción
NO SE USA   para informar de algo que puede esperar
CADA PATRÓN de vibración significa una cosa, y está declarado en la memoria de diseño
```

### Estados ambientales

**La pantalla deja de mostrar lo que mostraba.** Es un estado de la superficie, no un apagado.

```text
[ ] cada superficie declara qué se ve en ambiental
[ ] lo que se ve en ambiental sigue siendo ÚTIL: la información principal, no un logotipo
[ ] volver del ambiental NO reinicia lo que el usuario estaba haciendo
[ ] el ambiental respeta el presupuesto de consumo del pack
```

### Conectividad intermitente

```text
LA INTERMITENCIA ES EL ESTADO NORMAL, no una avería.

[ ] la aplicación dice qué puede hacer sin el teléfono, sin sonar a error
[ ] lo que necesita el teléfono espera o se encola, y el usuario lo sabe
[ ] al reconectar se sincroniza sin pedir nada al usuario
```

### Independencia o sincronización con el móvil

Es una **decisión de producto**, y se declara antes de diseñar:

```text
INDEPENDIENTE   funciona sin el teléfono. Necesita su propia red o sus propios datos.
ACOMPAÑANTE     el teléfono es la fuente. Sin él, el reloj es de sólo lectura, y lo dice.
MIXTO           declara QUÉ funciones son de cada tipo. Sin esa lista, no se diseña.
```

### Consumo de batería

```text
SE MIDE   consumo de la superficie mientras está visible
SE MIDE   consumo del estado ambiental
SE MIDE   frecuencia de actualización y su coste
SE MIDE   coste de cada sensor activado y durante cuánto tiempo está activo
```

Es el pack donde el consumo **es un criterio de diseño**, no una consecuencia: una animación
continua puede ser correcta en una web e inaceptable aquí.

### Sensores y permisos

```text
[ ] cada sensor declara cuándo se enciende y cuándo se apaga
[ ] el sensor denegado tiene camino alternativo, o la función se declara no disponible
[ ] los tres estados de permiso —concedido, denegado, revocado— se resuelven igual que en móvil
```

### Tiles, complications y notificaciones

Cuando la plataforma del proyecto los ofrece, **son superficies con su propio diseño**:

```text
[ ] cada una declara qué muestra y con qué frecuencia se actualiza
[ ] cada una tiene sus estados: sin datos, sin conexión, error
[ ] su actualización respeta el presupuesto de consumo
[ ] llevan a un sitio concreto de la aplicación, no al inicio
```

### Contraste y legibilidad

```text
· se valida A LA LUZ DEL SOL, no sólo en interior
· el contraste mínimo es MÁS EXIGENTE que en pantalla grande, y lo declara el proyecto
· el tamaño mínimo de texto se valida en el reloj más pequeño de la matriz
```

### Pruebas en reloj real

```text
OBLIGATORIO. Sin excepción y sin sustituto.
Ni el emulador ni una captura escalada valen como evidencia en este pack.
El movimiento, el consumo, la legibilidad al sol y el alcance con el dedo sólo existen
en el hardware.
```

### Entrega coordinada móvil–reloj

```text
[ ] las dos versiones pueden convivir: un usuario tendrá una de cada durante un tiempo
[ ] el contrato entre ambas está versionado, y el reloj antiguo con el móvil nuevo funciona
[ ] la reversión de una NO deja a la otra sin poder operar
[ ] la ventana de observación de ENT cubre las dos, no sólo la que se acaba de publicar
```

## Índice del pack

| | |
|---|---|
| roles especializados | [`lectura-de-un-vistazo`](roles/lectura-de-un-vistazo.md) · [`energia-y-estados`](roles/energia-y-estados.md) |
| gates adicionales | [`gates/gates.md`](gates/gates.md) |
| especialización de Diseño | [`diseno/especializacion.md`](diseno/especializacion.md) |
| ejemplos de composición | [`composicion.md`](composicion.md) |
