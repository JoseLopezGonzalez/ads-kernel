# PLANTILLA — ENCUADRE

Se copia, se rellena y vive en el paquete de `ENC`. Cómo se llena cada campo sin
inventarlo: [`ENC/Formulacion`](../capacidades/ENC/metodos/Formulacion.md).

> **Lo que el Owner lee es la prosa. Lo que el sistema consume es el bloque.** Los dos
> dicen lo mismo; si divergen, es un defecto y se corrige el bloque *y* la prosa.

---

## <título humano del encuadre>

**Lo que dijiste**

> «<cita literal, sin corregir>» — <fecha>

**Lo que he entendido**

<interpretación en dos o tres frases, en lenguaje del Owner>

**Lo que existiría cuando esto termine**

<resultado perseguido, una frase>

**Lo que sabremos para darlo por hecho**

- <evidencia de cierre 1>
- <evidencia de cierre 2>

**Lo que no sé todavía**

- <duda abierta 1>

**Lo que estoy dando por supuesto**

- <suposición 1>

**Lo que ya existe y toca esto**

- <hallazgo del anclaje, con su ruta>

---

```yaml ads:encuadre
id: ENC-000
expresion_literal:
  - fecha: "2026-08-25"
    texto: "<las palabras exactas del Owner, sin editar>"
    canal: "chat"
interpretacion: >
  <qué se ha entendido, separado de lo que el Owner dijo. Si sustituyó a una
  interpretación anterior, la anterior queda enlazada, no borrada>
resultado_perseguido: "<qué existirá cuando esto termine, sin usar mejorar/optimizar/revisar como único verbo>"
problema_observado: "<qué ocurre hoy que no debería, con un caso concreto>"
motivo: "<por qué importa: a quién afecta y con qué consecuencia>"
situacion_actual: "<qué hay hoy, según el anclaje, no según la impresión>"
expectativas:
  - "<qué espera el Owner que pase>"
restricciones:
  - "<qué no se puede tocar, cambiar ni romper>"
referencias:
  - "<enlace, captura o ejemplo aportado, con su fecha>"
decisiones_previas:
  - "<decisión vigente que condiciona esto, con enlace>"
suposiciones:
  - "<lo que la interpretación necesita y el Owner no confirmó>"
dudas_abiertas:
  - "<lo que sigue sin respuesta y no se ha escondido en la interpretación>"
evidencia_de_cierre:
  - "<qué se mira, dónde, y qué resultado cuenta como cierre — comprobable por un tercero>"
incertidumbre:
  grado: media
  ejes: ["resultado perseguido: baja", "problema: baja", "alcance: media", "restricciones: baja", "criterio de terminado: media"]
  motivo: "<por qué ese grado, derivado de los ejes>"
nivel_owner: opcional-acumulada
vinculos:
  - "<item, decisión o patrón con el que se relaciona>"
anclaje:
  ya_implementado:
    - "<qué existe, con ruta exacta>"
  decisiones_que_gobiernan:
    - "<decisión o ADR vigente>"
  aprendizajes:
    - "<entrada del ledger que aplica>"
  duplica: []
  no_existe_y_se_creia:
    - "<qué se daba por construido y no está>"
clasificacion:
  naturaleza: entrada:candidato
  tipo_propuesto: FEA
  motivo: "<por qué ese tipo, citando el RESULTADO PERSEGUIDO y no las capacidades previstas>"
estado: listo-para-dsp
```

---

## Errores que esta plantilla existe para impedir

```text
literal reescrita              se corrigió la frase del Owner «para que quedara mejor»
interpretación disfrazada      una suposición escrita como si fuera un hecho observado
evidencia no comprobable       «que quede bien», «que sea más rápido» sin medida ni testigo
duda escondida                 lo que no se sabe, redactado con firmeza
anclaje vacío por comodidad    no_existe_y_se_creia sin traza que lo sostenga
nivel de Owner por prudencia   marcado obligatorio sin citar la fila de a.8 que aplica
tipo por capacidades           «esto es DIS porque lo hará Diseño» en vez de por resultado
```
