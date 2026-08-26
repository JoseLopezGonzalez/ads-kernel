# DIS/RevisionDeFidelidad — lo aprobado frente a lo construido

```yaml ads:metodo
id: DIS/RevisionDeFidelidad
nombre: RevisionDeFidelidad
capacidad: DIS
disparador:
  - "CON entrega una capa que implementa una especificación de DIS"
  - "un item DEF visual alega que lo construido no corresponde a lo aprobado"
carga:
  - "la especificación aprobada con su versión exacta"
  - "el artefacto construido con su commit exacto"
  - "las grabaciones de intención de DIS/movimiento"
  - "la matriz de entornos y los presupuestos del pack instalado"
  - "docs/diseno/03-SISTEMA.md y 10-DEUDA.md"
preguntas_iniciales:
  - "¿qué versión de la especificación se aprobó, y sobre qué commit se construyó?"
  - "¿qué entornos exige la matriz del pack, y hay dispositivo real disponible?"
pasos:
  - n: 1
    nombre: COMPARAR ESTÁTICO
    modo: lineal
    hace: >
      Capturar lo construido en cada entorno de la matriz, a tamaño real y con zoom en las
      juntas, y ponerlo al lado de la intención.
    produce: "comparación estática por entorno"
    termina_cuando: "todos los entornos de la matriz tienen su par de capturas y su diferencia señalada"
    checkpoint: true
  - n: 2
    nombre: COMPARAR ESTADOS
    modo: lineal
    hace: >
      Comparar los cinco estados obligatorios más los propios del componente, en ambas
      columnas, con datos reales.
    produce: "comparación de estados"
    termina_cuando: "todos los estados alcanzables están comparados, y los no alcanzables están declarados como tales"
    checkpoint: true
  - n: 3
    nombre: COMPARAR MOVIMIENTO
    modo: lineal
    hace: >
      Grabar lo construido y medir la duración SOBRE LA GRABACIÓN, no sobre el código.
      Comparar la curva sobre la grabación. Grabar también el estado reducido.
    produce: "comparación de movimiento con duraciones medidas"
    termina_cuando: "cada transición especificada tiene su par de grabaciones y su duración medida"
    checkpoint: true
  - n: 4
    nombre: EXTRAER VALORES
    modo: lineal
    hace: >
      Extraer del artefacto construido los valores realmente usados y compararlos con el
      sistema declarado.
    produce: "tabla de valores construidos frente a sistema declarado"
    termina_cuando: "todo valor usado está localizado dentro o fuera del sistema"
    checkpoint: false
  - n: 5
    nombre: PROBAR EN DISPOSITIVO REAL
    modo: lineal
    hace: >
      Ejecutar en el hardware que el pack exige, declarando dispositivo, versión de sistema
      y condiciones. Un emulador no sustituye a esto cuando el pack lo exige.
    produce: "evidencia en dispositivo real"
    termina_cuando: "existe evidencia en cada dispositivo exigido, o está declarado que no fue posible y por qué"
    checkpoint: true
  - n: 6
    nombre: VEREDICTO
    modo: convergente
    hace: >
      Emitir fiel, fiel con deuda aceptada, o infiel. La deuda sólo cuenta si se acordó
      ANTES de construir distinto: nunca se acepta a posteriori para evitar la devolución.
    produce: "veredicto con su evidencia"
    termina_cuando: "el veredicto está escrito y, si hay deuda, tiene sus cuatro campos"
    checkpoint: true
artefactos:
  - "comparación estática por entorno"
  - "comparación de estados"
  - "comparación de movimiento con duraciones medidas"
  - "tabla de valores construidos frente a sistema"
  - "evidencia en dispositivo real"
  - "veredicto"
puntos_owner:
  - "aceptación de deuda en superficie premium o sobre un patrón aprobado por él"
consultas:
  - "CON: ¿qué evidencia sostiene esta diferencia? Responde con medición, limitación documentada, prototipo fallido o coste medido"
checkpoints:
  - "tras los pasos 1, 2, 3, 5 y 6"
critica:
  - "¿he comparado todos los entornos, o sólo el más cómodo?"
  - "¿he medido las duraciones o las he leído del código?"
  - "¿estoy aceptando como deuda algo que acabo de descubrir?"
gate: gate:excelencia-visual
salida:
  - "artefacto de comparación con veredicto"
  - "deuda registrada cuando se acordó previamente"
devolucion:
  - "a CON, con la comparación completa, cuando el veredicto es infiel"
  - "a DIS/direccion-artistica, cuando CON demuestra imposibilidad con la evidencia exigida"
bloqueo:
  - "no existe especificación versionada contra la que comparar"
  - "el pack exige dispositivo real y no hay ninguno disponible"
cancelacion:
  - "la capa construida se invalida por su propietario antes de terminar la comparación"
aprendizaje:
  - "una simplificación repetida en la misma dimensión señala una especificación que no se puede construir tal como está escrita"
  - "toda deuda aceptada alimenta el ledger y puede promoverse a regla"
prueba_de_reanudacion: >
  Un agente nuevo lee qué entornos y qué estados están ya comparados y continúa por los que
  faltan, sin recapturar. Es la prueba T97.
```
