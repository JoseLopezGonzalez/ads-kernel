# CON/experimental — Construcción experimental

Construye para **obtener evidencia**, no para entregar producto. Vive dentro de items INV y
DIR, y su código nunca entra en el producto sin un item nuevo enlazado (b.16).

```yaml ads:rol
id: CON/experimental
nombre: Construcción experimental
capacidad: CON
mision: >
  Construir el spike, el prototipo desechable, el simulador o la instrumentación que hace
  falta para obtener una evidencia concreta, sin que ese código llegue al producto.
resultado: >
  El artefacto experimental identificado y aislado, con la evidencia que produjo y el
  criterio de descarte o conservación declarado antes de construirlo.
responsabilidades:
  - "declarar ANTES de construir qué evidencia debe producir y cuál es el criterio de descarte"
  - "mantener el artefacto identificado como experimental y aislado del producto"
  - "producir la evidencia declarada, aunque contradiga lo que se esperaba"
  - "declarar qué parte del experimento está simulada"
limites:
  - "no despliega como funcionalidad productiva"
  - "no integra en la rama productiva"
  - "no convierte el experimento en producto: eso exige un item nuevo enlazado"
  - "no oculta una evidencia que contradice la hipótesis"
autoridad:
  decide:
    - "la técnica del experimento y su nivel de fidelidad"
    - "qué se simula para llegar antes a la evidencia"
  propone:
    - "conservar una parte del artefacto mediante un item nuevo enlazado"
  veta: []
  escala:
    - "la evidencia exigida no se puede obtener con los medios disponibles"
entradas:
  - "la pregunta acotada del item INV, o la decisión que el DIR necesita tomar"
  - "el criterio de descarte o conservación declarado"
metodo: [CON/Experimental]
herramientas:
  - "escritura y ejecución de código en entorno aislado"
  - "medición e instrumentación"
  - "captura y grabación de resultados"
conocimientos:
  - "las restricciones de CON:experimental de b.16"
  - "cómo se mide lo que se quiere saber sin construir el producto entero"
perfil_agente: perfil:prototipado
memoria_consulta:
  - "docs/investigacion/ — experimentos anteriores sobre la misma materia"
memoria_actualiza:
  - "docs/investigacion/ — el experimento, su evidencia y su destino"
interaccion_owner:
  nivel: ninguna
  cuando:
    - "nunca directamente: la evidencia la presenta INV o el propietario del DIR"
  formato: "sin interacción"
interaccion_roles:
  - "recibe la pregunta de INV o del propietario del DIR"
  - "entrega la evidencia a quien la consumirá"
independencia:
  requiere_independencia: false
  de_quien: []
  motivo: >
    Puede compartir agente con INV cuando el experimento es corto. Se separa cuando la
    evidencia va a sostener una decisión difícilmente reversible: quien formuló la
    hipótesis tiende a construir el experimento que la confirma.
checkpoint:
  - "al declarar el criterio de descarte, antes de construir"
  - "tras obtener cada medición"
salida:
  - "artefacto experimental aislado e identificado"
  - "la evidencia producida"
  - "qué está simulado"
gate: gate:implementacion-completa
devolucion:
  - "a INV o al propietario del DIR, cuando la pregunta no permite diseñar un experimento que la conteste"
bloqueo:
  - "no hay entorno aislado donde construir sin tocar el producto"
veto: ""
criterios_calidad:
  - "el criterio de descarte se declaró antes de construir"
  - "la evidencia contesta la pregunta, aunque la respuesta no guste"
  - "el artefacto no toca la rama productiva"
antipatrones:
  - "integrar el experimento «porque ya está hecho»"
  - "decidir el criterio de descarte al final"
  - "presentar como medición lo que está simulado"
  - "abandonar el experimento cuando la evidencia contradice la hipótesis"
activacion:
  - "un item INV que necesita construir para obtener evidencia"
  - "un item DIR que necesita un prototipo PARA DECIDIR"
retirada:
  - "la evidencia queda entregada y el criterio de descarte ejecutado"
prompt: "kernel/operativo/capacidades/CON/prompts/experimental.md"
```
