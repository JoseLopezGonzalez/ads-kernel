# mobile-app — ejemplos de composición de equipo

## Caso 1 · pantalla nueva con captura de cámara

```text
La escala devuelve N2 → composicion:dis-feature-visual

ROLES DEL KERNEL          los nueve de dis-feature-visual
ROLES DEL PACK            mob:DIS/interaccion-tactil · mob:CON/ciclo-de-vida
CONSULTA OBLIGATORIA      SEG: qué se hace con la imagen y cuánto se conserva
INDEPENDENCIA             DIS/validacion-de-uso de mob:DIS/interaccion-tactil
GATES                     los dos del kernel + gate:mob-dispositivo-real +
                          gate:mob-ciclo-y-permisos
EVIDENCIA                 grabación en el dispositivo más lento · los tres estados del
                          permiso de cámara · terminación forzada durante la captura
```

## Caso 2 · sincronización en segundo plano

```text
Sin superficie nueva: la escala devuelve N0 para diseño

ROLES DEL KERNEL          ARQ/encaje · CON/implementacion · VER/dosier · DOM/modelo
ROL DEL PACK              mob:CON/ciclo-de-vida
CONSULTA OBLIGATORIA      DOM: ¿la sincronización es idempotente? Sin esa respuesta no se reintenta
GATES                     gate:implementacion-completa + gate:mob-consumo
EVIDENCIA                 consumo medido en dispositivo desconectado de la corriente
OWNER                     si el consumo es inherente al alcance: reducir la frecuencia es
                          decisión suya, no de construcción
```

## Caso 3 · corrección de un objetivo táctil demasiado pequeño

```text
Es un DEF → composicion:dis-bug-visual

ROLES                     DIS/revision-de-fidelidad
ROL DEL PACK              mob:DIS/interaccion-tactil, sólo si la corrección exige recomponer
GATES                     gate:excelencia-visual + gate:mob-dispositivo-real
CLAVE                     se comprueba en el dispositivo MÁS GRANDE de la matriz, que es
                          donde el alcance con el pulgar falla
```
