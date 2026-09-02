# BORRADOR · `B-02` · La norma habilitante de la RAÍZ EXTERNA DE CONFIANZA

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-02
ENTREGABLE: F5-D
PRESION: PN-19
FILA DE LA MATRIZ: F5-OB-03
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.** El CONTENIDO de abajo **sí** está ratificado por
> el Owner en su sede canónica; lo que **no** está decidido es **en qué sede vive**. Este
> fichero no crea esa sede y no la elige.

---

## 1 · Lo que el Owner YA resolvió, y que aquí NO se vuelve a preguntar

```text
· el verificador externo es OBLIGATORIO en F6
· el ejecutor externo NO PUEDE COMPARTIR la identidad de escritura del runtime
· la alternativa de retirar la garantía quedó RECHAZADA EXPRESAMENTE
· las TRES condiciones obligatorias: antes de la primera adopción permanente, antes de
  declarar ADS operativo, y antes de certificar cualquier adaptador
· el reparto: sistema define · plataforma construye y opera · verificación produce el
  dosier · seguridad gobierna credenciales y bloqueo · el Owner acepta o rechaza, y esa
  autoridad es INDELEGABLE
```

**Nada de esa lista es una elección.** Es autoridad vigente, y este borrador la cita sin
ampliarla.

## 2 · Los tres extremos que la norma habilitante tiene que fijar

**Son la condición exacta de desbloqueo del único contrato de `F6` que está bloqueado.**

```text
(i)    la IDENTIDAD DE ESCRITURA separada del runtime, CON SU TITULAR
(ii)   DÓNDE vive la evidencia y la atestación, fuera del árbol comprobado
(iii)  QUIÉN la custodia
```

Emitida esa sede, el contrato pasa a construible **sin tocar ninguno de sus campos**.

**Y un extremo añadido que el contrato técnico exige y ninguna sede aprobada contempla:** la
protección de las referencias remotas del control repo, con el forzado **prohibido y
detectado**.

> **AVISO OPERATIVO, no arquitectónico, y se declara porque nadie lo ha registrado.** El
> contrato técnico exige commits firmados o equivalente verificable por un tercero. Eso
> implica que el Owner posea y custodie una clave de firma. No consta en ninguna resolución.

## 3 · Esqueleto del texto, por sede

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

```text
SI `D-02` = A · dentro de (g) y su contrato derivado          ← recomendada
     g.N.1  identidad técnica de verificación separada, con titular declarado
     g.N.2  ubicación de la evidencia y la atestación, fuera del árbol comprobado
     g.N.3  custodia: quién la conserva y bajo qué autoridad
     g.N.4  protección de referencias remotas; forzado prohibido Y DETECTADO
     g.N.5  separación de poderes: ningún actor modifica a la vez corpus, batería y
            resultado
     → el contrato derivado del control repo lo materializa F6. (a), (b), E2, el contrato
       de fuentes y la constitución quedan INTACTOS

SI `D-02` = B · ampliar el contrato de fuentes
     → exige ENMIENDA de material aprobado, y exige además revisar expresamente la
       resolución que dice que ese contrato NO CAMBIA. Este borrador NO la redacta:
       revisar una resolución vigente es acto del Owner

SI `D-02` = C · sede nueva propia
     → exige declarar la sede, su autoridad, su relación de precedencia con (g) y con el
       contrato de fuentes, y aplicarle la prueba que el corpus exige a toda sede nueva
```

<!-- ads-lint-ignore-end -->

## 4 · Trazabilidad

| presión | fila | decisión | qué desbloquea |
|---|---|---|---|
| `PN-19` | `F5-OB-03` | `D-02` | el único contrato de `F6` bloqueado por dependencia, su corte vertical, y por la cadena que el Owner fijó, la adopción real |

**Prueba prevista:** que el contrato pase a construible sin que ningún otro campo de su fila
cambie; y la prueba negativa que la presión fija — falsear un veredicto desde dentro del
árbol y exigir que la atestación externa lo detecte.

> **Y lo que este borrador NO hace:** no implementa nada, no construye la raíz externa, no
> declara superada la deuda que la espera, y no desbloquea la primera adopción real. Todo
> eso es `F6`, y `F6` NO está iniciada.
