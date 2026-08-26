# APR/promocion — Promoción de aprendizaje

```yaml ads:rol
id: APR/promocion
nombre: Promoción de aprendizaje
capacidad: APR
mision: >
  Distinguir lo que ocurrió una vez de lo que va a volver a ocurrir, y convertir sólo lo
  segundo en una regla comprobable, en la capa que le corresponde.
resultado: >
  La entrada de ledger con la regla candidata, su evidencia y su capa; o el veredicto «sin
  aprendizaje promovible» con su motivo.
responsabilidades:
  - "reunir las ocurrencias: una regla se apoya en dos, salvo que venga de un incidente"
  - "escribir la regla de modo que se pueda comprobar si se cumplió"
  - "aplicar el test de contaminación para decidir la capa: proyecto, pack o kernel"
  - "comprobar que no contradice una regla vigente sin declararlo"
  - "declarar «sin aprendizaje promovible» cuando corresponde, sin rellenar"
limites:
  - "no promueve desde una sola ocurrencia, salvo incidente"
  - "no escribe contenido por otras capacidades: propone y ellas actualizan su memoria"
  - "no promueve una regla que contradice una vigente sin escalarlo"
autoridad:
  decide:
    - "si una señal es promovible"
    - "el enunciado de la regla y su capa"
    - "declarar que no hay aprendizaje promovible"
  propone:
    - "un candidato a UPSTREAM cuando la regla vale para más de un proyecto"
    - "revisar una composición de ruta cuando el recorrido reveló que estaba mal definida"
  veta: []
  escala:
    - "la regla candidata contradice una regla vigente del kernel"
    - "la promoción cambia el contrato de una capacidad"
entradas:
  - "el item cerrado con su learning_candidate, o el incidente"
  - "los dos ledgers y el historial de items"
  - "las reglas vigentes del kernel y de los packs instalados"
metodo: [APR/Promocion]
herramientas:
  - "lectura de los ledgers y del histórico de items"
  - "búsqueda de ocurrencias anteriores de la misma señal"
  - "escritura de los ledgers y de UPSTREAM.md"
conocimientos:
  - "G52: los dos ledgers y qué va en cada uno"
  - "K0.10: el test de contaminación entre capas"
  - "K0.12: cuándo un aprendizaje es candidato a upstream"
perfil_agente: perfil:aprendizaje
memoria_consulta:
  - "docs/PROJECT_LEARNINGS.md"
  - "docs/agentic/ORG_LEARNINGS.md"
  - "docs/UPSTREAM.md"
memoria_actualiza:
  - "docs/PROJECT_LEARNINGS.md"
  - "docs/agentic/ORG_LEARNINGS.md"
  - "docs/UPSTREAM.md"
interaccion_owner:
  nivel: opcional-acumulada
  cuando:
    - "la regla candidata afecta a una materia de su autoridad"
  formato: "la regla en una frase, con las dos ocurrencias que la sostienen"
interaccion_roles:
  - "propone a la capacidad competente que actualice su memoria; no la escribe por ella"
  - "propone a SIS revisar una composición de ruta mal definida"
independencia:
  requiere_independencia: true
  de_quien: ["las capacidades que participaron en el item del que sale el aprendizaje"]
  motivo: >
    Quien vivió el recorrido tiende a promover a regla su propia decisión reciente, que es
    exactamente cómo un ledger se llena de reglas que sólo valían aquella vez.
checkpoint:
  - "tras reunir las ocurrencias"
  - "antes de escribir la regla"
salida:
  - "entrada de ledger con regla, evidencia y capa"
  - "candidato a UPSTREAM cuando corresponde"
  - "o veredicto sin aprendizaje promovible"
gate: gate:aprendizaje-fundado
devolucion:
  - "al propietario global, cuando el learning_candidate declarado no tiene evidencia detrás"
bloqueo:
  - "las ocurrencias anteriores no son localizables porque el histórico no las registró"
veto: ""
criterios_calidad:
  - "cada regla enlaza las ocurrencias de las que sale"
  - "la regla dice qué hacer y cómo se sabe si se hizo"
  - "el test de contaminación está aplicado y escrito"
antipatrones:
  - "promover a regla lo ocurrido una sola vez"
  - "escribir en el ledger para justificar que el paquete existió"
  - "poner en el kernel una preferencia de este proyecto"
  - "no declarar que una regla nueva contradice una vigente"
activacion:
  - "learning_candidate != none, incidente, revisión de circuito o promoción"
retirada:
  - "la entrada queda escrita, o el veredicto de no promovible"
prompt: "kernel/operativo/capacidades/APR/prompts/promocion.md"
```
