# SIS/Conformidad — comprobar que una organización instalada cumple

```yaml ads:metodo
id: SIS/Conformidad
nombre: Conformidad
capacidad: SIS
disparador:
  - "se instala el kernel en un proyecto nuevo"
  - "se audita el corpus de un proyecto en curso"
  - "un cambio grande del kernel operativo exige revalidar"
carga:
  - "el corpus completo del proyecto: kernel operativo, packs instalados y documentación"
  - "el registro de pruebas y su estado real"
preguntas_iniciales:
  - "¿qué pruebas se pueden ejecutar hoy, y cuáles exigen runtime?"
  - "¿hay alguna verdad escrita en dos sitios?"
  - "¿hay documentos que nadie consume?"
pasos:
  - n: 1
    nombre: EJECUTAR VALIDADORES
    modo: lineal
    hace: "Ejecutar ads_lint y comprobar_contratos, y publicar su salida completa."
    produce: "salida de los validadores"
    termina_cuando: "ambos se han ejecutado y su salida está registrada, pase o falle"
    checkpoint: true
  - n: 2
    nombre: COMPROBAR EXTENSIONES
    modo: lineal
    hace: >
      Comprobar que toda capacidad añadida por pack o profile cumple los doce campos, usa
      prefijo de espacio de nombres y no reclama veto en colisión sin arbitraje declarado.
    produce: "veredicto por extensión"
    termina_cuando: "cada extensión instalada tiene veredicto"
    checkpoint: true
  - n: 3
    nombre: BUSCAR DUPLICACIÓN
    modo: divergente
    hace: >
      Buscar la misma verdad escrita en dos ficheros. Se resuelve BORRANDO la copia, nunca
      sincronizando las dos.
    produce: "lista de duplicaciones con cuál sobra"
    termina_cuando: "el barrido termina y cada duplicación tiene propuesta de resolución"
    checkpoint: true
  - n: 4
    nombre: BUSCAR DOCUMENTOS SIN USO
    modo: divergente
    hace: >
      Localizar documentos que ningún método, rol ni gate consume. Un documento sin uso
      operativo es autorreferencia y se propone su retirada a quien lo posee.
    produce: "lista de documentos sin uso"
    termina_cuando: "cada documento del corpus está enlazado desde algún método, rol o gate, o está en la lista"
    checkpoint: true
  - n: 5
    nombre: REGISTRAR ESTADO REAL
    modo: convergente
    hace: >
      Regenerar el registro de pruebas y comprobar que ninguna declara un estado superior al
      que su evidencia sostiene.
    produce: "registro de pruebas regenerado"
    termina_cuando: "el registro es determinista y cada estado corresponde con su evidencia"
    checkpoint: true
  - n: 6
    nombre: INFORMAR Y ENRUTAR
    modo: lineal
    hace: >
      Publicar el informe y crear un item por cada hallazgo, enrutado a la capacidad que
      posee esa capa. SIS no escribe el contenido por ellas.
    produce: "informe y items enrutados"
    termina_cuando: "cada hallazgo tiene item con destinatario"
    checkpoint: true
artefactos:
  - "salida de los validadores"
  - "veredicto por extensión instalada"
  - "lista de duplicaciones y de documentos sin uso"
  - "registro de pruebas regenerado"
  - "informe de conformidad"
puntos_owner:
  - "ninguno: los hallazgos se enrutan a las capacidades competentes"
consultas:
  - "cada capacidad afectada: ¿este documento sigue siendo vuestro y sigue vigente? Responde sí o no"
checkpoints:
  - "tras cada paso"
critica:
  - "¿estoy escribiendo contenido que pertenece a otra capacidad?"
  - "¿he declarado conforme algo cuyos validadores no he ejecutado?"
  - "¿estoy proponiendo sincronizar dos copias en lugar de borrar una?"
gate: gate:sistema-conforme
salida:
  - "informe de conformidad con el estado real"
  - "items enrutados a las capacidades competentes"
devolucion:
  - "a SIS/evolucion, cuando el hallazgo está en el propio kernel operativo"
bloqueo:
  - "los validadores no pueden ejecutarse en el entorno"
cancelacion:
  - "la auditoría se cancela: la salida parcial de los validadores se conserva con su fecha"
aprendizaje:
  - "una duplicación recurrente señala que el mapa de fuente única está mal trazado"
  - "un documento que nadie consume señala una pieza escrita para nadie"
prueba_de_reanudacion: >
  Un agente nuevo reejecuta los validadores: su salida ES el estado. Los hallazgos ya
  enrutados están en sus items, y no se duplican. Es la prueba T121.
```
