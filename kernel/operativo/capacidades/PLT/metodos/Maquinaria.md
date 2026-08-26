# PLT/Maquinaria — construir lo que desbloquea

```yaml ads:metodo
id: PLT/Maquinaria
nombre: Maquinaria
capacidad: PLT
disparador:
  - "una capacidad declara un bloqueo de maquinaria, nombrando qué la desbloquearía"
  - "DSP despacha un item del backlog de PLT"
carga:
  - "el bloqueo declarado y qué lo desbloquearía"
  - "docs/plataforma/ENTORNOS.md y AISLAMIENTO.md"
  - "la matriz de entornos del pack instalado"
preguntas_iniciales:
  - "¿qué operación concreta no puede hacer hoy quien declaró el bloqueo?"
  - "¿lo que pide es maquinaria, o es otra cosa?"
  - "¿cuántos agentes van a usar esto a la vez?"
pasos:
  - n: 1
    nombre: CONFIRMAR EL BLOQUEO
    modo: convergente
    hace: >
      Comprobar que lo que se pide es una carencia de maquinaria y no otra cosa, y escribir
      qué operación concreta quedará desbloqueada.
    produce: "operación desbloqueada declarada"
    termina_cuando: "está escrita la operación que hoy no se puede hacer y mañana sí"
    checkpoint: true
  - n: 2
    nombre: MONTAR
    modo: lineal
    hace: "Construir la pieza, escribiendo el procedimiento a la vez que se ejecuta."
    produce: "pieza montada y procedimiento escrito"
    termina_cuando: "la pieza funciona y el procedimiento está escrito"
    checkpoint: true
  - n: 3
    nombre: PROBAR DESDE CERO
    modo: lineal
    hace: >
      Ejecutar el procedimiento desde cero en un sitio distinto del que se montó. Lo que
      sólo funciona donde se construyó no desbloquea a nadie.
    produce: "resultado de la reproducción"
    termina_cuando: "el montaje desde cero funciona siguiendo sólo lo escrito"
    checkpoint: true
  - n: 4
    nombre: AISLAR
    modo: convergente
    hace: >
      Si varios agentes van a usarla a la vez, declarar cómo se aíslan y comprobarlo con dos
      usos simultáneos.
    produce: "estrategia de aislamiento comprobada"
    termina_cuando: "dos usos simultáneos no se interfieren, o consta que el uso es exclusivo"
    checkpoint: true
  - n: 5
    nombre: CONFIRMAR
    modo: convergente
    hace: "Pedir a quien declaró el bloqueo que ejecute la operación y lo confirme."
    produce: "confirmación de desbloqueo"
    termina_cuando: "quien lo pidió ha ejecutado la operación con éxito"
    checkpoint: true
artefactos:
  - "operación desbloqueada declarada"
  - "pieza montada y procedimiento"
  - "resultado de la reproducción desde cero"
  - "estrategia de aislamiento"
  - "confirmación de desbloqueo"
puntos_owner:
  - "ninguno"
consultas:
  - "la capacidad bloqueada: ¿esta pieza te desbloquea? Ejecuta la operación y responde sí o no"
  - "ENT: ¿qué señales necesitas para tu ventana de observación? Responde con la lista"
checkpoints:
  - "tras los pasos 1, 2, 3, 4 y 5"
critica:
  - "¿esto desbloquea algo concreto, o es una mejora que nadie pidió?"
  - "¿funciona en otro sitio, o sólo donde lo monté?"
  - "¿he comprobado el aislamiento con dos usos a la vez?"
gate: gate:maquinaria-disponible
salida:
  - "maquinaria funcionando, documentada y confirmada"
devolucion:
  - "a quien declaró el bloqueo, cuando lo que pide no es maquinaria"
bloqueo:
  - "el recurso necesario excede lo autorizado"
cancelacion:
  - "la capacidad bloqueada encuentra otro camino: se registra qué se montó y qué quedó a medias"
aprendizaje:
  - "un bloqueo de maquinaria que se repite señala una carencia estructural, no un item"
  - "todo procedimiento de montaje que falló al reproducirse se corrige y se registra"
prueba_de_reanudacion: >
  Un agente nuevo lee qué piezas están montadas y sigue el procedimiento escrito para
  continuar. Si el procedimiento no está escrito, la pieza se considera no entregada. Es la
  prueba T116.
```
