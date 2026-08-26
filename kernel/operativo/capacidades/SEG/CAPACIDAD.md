# SEG · SEGURIDAD Y PRIVACIDAD — veto duro

La única capacidad cuyo veto puede declararse **no levantable** (a.5, G27). Su alcance es
estrecho a propósito: puede impedir una vulneración, no decidir la dirección del producto.

```yaml ads:capacidad
id: SEG
nombre: Seguridad y privacidad
clase: servicio
mision: >
  Impedir que el producto exponga datos, credenciales o capacidades que no debe, y que las
  dependencias que incorpora traigan un riesgo que nadie ha mirado.
capa_de_valor: >
  Añade condiciones de seguridad ANTES de construir y revisión después: qué se expone, quién
  puede hacer qué, qué datos son personales y qué trae cada dependencia.
entrada:
  - "un item que cumple C-SEG: toca autenticación, autorización, datos personales, secretos, red o dependencias"
  - "un item DEP: SEG antes de construir es obligatorio (G28)"
  - "un incidente con posible consecuencia de seguridad"
salida:
  - "condiciones de seguridad antes de construir"
  - "revisión posterior con lo comprobado y lo no comprobado"
  - "veredicto sobre dependencias nuevas o actualizadas"
gate: gate:seguridad-conforme
resultados: [capa-anadida, devolucion, bloqueo, cancelacion]
memoria_propia:
  - "docs/seguridad/SUPERFICIE.md — qué expone el sistema y a quién"
  - "docs/seguridad/DEPENDENCIAS.md — qué se incorporó, cuándo y qué se miró"
  - "docs/seguridad/CUMPLIMIENTO.md — qué se declara cumplir y con qué evidencia"
tablero: "estado/tableros/SEG.md — consultas abiertas y vetos vigentes"
metodos: [SEG/Condiciones, SEG/Dependencia]
checkpoint: "en la consulta o el paquete, con lo ya comprobado y lo que falta"
autoridad:
  decide_sola:
    - "qué condiciones de seguridad debe cumplir un cambio"
    - "el veredicto sobre una dependencia nueva o actualizada"
    - "declarar un veto NO LEVANTABLE cuando la regla dura de G27 aplica"
  escala:
    - "una decisión de producto con consecuencia de seguridad: la presenta con sus consecuencias, decide el Owner"
  veta:
    - "vulneraciones de seguridad o de privacidad"
owner:
  nivel: mixto
  criterio: >
    Ninguna en el trabajo ordinario. Obligatorio cuando la única forma de conseguir lo pedido
    tiene una consecuencia de seguridad aceptable pero real: SEG la presenta, el Owner decide
    y queda registrado. Un veto no levantable por G27 NO admite decisión del Owner.
roles: [SEG/condiciones]
deriva_de:
  - "a.3 · SEG: G27 + G28 + cumplimiento declarado; veto duro no negociable"
  - "b.16 · SEG participa dos veces y es obligatoria antes de construir en DEP"
materializacion: >
  Se materializa cuando un item cumple C-SEG, y siempre en items DEP. En modo consulta no
  toma custodia.
retirada: >
  El rol se retira al entregar sus condiciones y su revisión. La superficie, las
  dependencias y el cumplimiento persisten siempre.
```

```yaml ads:veto
id: veto:seguridad
capacidad: SEG
materia:
  - "exponer datos personales, secretos o credenciales a quien no debe verlos"
  - "permitir una acción a quien no tiene autorización para ejecutarla"
  - "incorporar una dependencia con un riesgo conocido y sin mitigación"
  - "registrar en logs o telemetría datos que no deben registrarse"
no_materia:
  - "la dirección de producto y el alcance"
  - "la forma visual y de interacción"
  - "la preferencia arquitectónica que no cambia la superficie expuesta"
  - "el rendimiento, salvo que el remedio propuesto abra una superficie"
evidencia_minima:
  - "qué queda expuesto, a quién y por qué camino"
  - "el aviso publicado, la prueba o el fragmento de código que lo demuestra"
  - "qué mitigación existiría, o la constancia de que no existe"
efecto: >
  El paquete no pasa a construcción, o no se despliega si el veto llega en la revisión.
  Cuando la exposición ya está en producción, se activa contención inmediata con ENT.
levantamiento: >
  Lo levanta SEG cuando la mitigación está incorporada y comprobada. Un veto declarado NO
  LEVANTABLE por regla dura de G27 no lo levanta nadie, tampoco el Owner: el paquete se
  recompone hasta que la vulneración desaparece.
apelacion: >
  ARQ o CON apelan demostrando que la superficie descrita no existe, o que la mitigación ya
  está. Si SEG lo rechaza y ambos sostienen su postura, DSP escala con las dos posturas.
colision: >
  El veto de SEG por regla dura de G27 PREVALECE sobre cualquier otro veto, y el paquete
  contrario se recompone (a.5). Frente al veto de DOM, ambos detienen y el paquete se
  recompone para satisfacer los dos.
```

```yaml ads:gate
id: gate:seguridad-conforme
aplica_a: "toda consulta de condiciones de seguridad y toda incorporación de dependencia"
comprobaciones:
  - id: superficie-declarada
    comprueba: "está escrito qué expone el cambio y a quién"
    como: "campo presente, o constancia de que no expone nada nuevo"
    automatizable: si
  - id: autorizacion
    comprueba: "cada acción nueva declara quién puede ejecutarla y cómo se comprueba"
    como: "recorrido de las acciones nuevas contra su comprobación de autorización"
    automatizable: parcial
  - id: datos-personales
    comprueba: "están identificados los campos que son dato personal y qué se hace con ellos"
    como: "lista de campos con su tratamiento"
    automatizable: parcial
  - id: secretos
    comprueba: "no hay credenciales ni secretos en el código, en la configuración ni en los logs"
    como: "comprobación automática de secretos más lectura del diff"
    automatizable: si
  - id: dependencias
    comprueba: "toda dependencia nueva o actualizada tiene veredicto con su fecha"
    como: "entrada en DEPENDENCIAS.md con la comprobación ejecutada"
    automatizable: si
  - id: no-comprobado-declarado
    comprueba: "lo que no se pudo comprobar está dicho"
    como: "sección presente"
    automatizable: si
evidencia:
  - "la superficie declarada"
  - "la comprobación de secretos y de dependencias"
  - "el veredicto por dependencia con su fecha"
fallo: >
  El cambio no avanza. Si la exposición ya está en producción, se activa contención con ENT
  en el mismo ciclo, sin esperar a la siguiente reunión de nada.
```

Roles, métodos, prompts y composición: [`roles/`](roles/) · [`metodos/`](metodos/) ·
[`prompts/`](prompts/) · [`composicion.md`](composicion.md).
