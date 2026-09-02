# BORRADOR · `B-04` · La vía normativa del trabajo que nace por política

```text
ESTADO-DEL-BORRADOR: NO_APROBADO
PENDIENTE-DECISION-DEL-OWNER: D-05
ENTREGABLE: F5-A
PRESIONES: PN-2 · PN-3
FILAS DE LA MATRIZ: F5-OB-05 · F5-OB-06
```

> **ESTO NO ES NORMA Y NO ESTÁ APROBADO.**

---

## 1 · Qué está decidido y qué falta

**Decidido por el Owner:** las auditorías se abren **por política** —por evento, riesgo,
recurrencia y caducidad—, y **una única decisión declara alcance, prioridad, presupuesto,
umbrales y revocación**. Detectar e inventariar es automático y **no crea trabajo**.

**Lo que falta:** la **vía**. La especificación de recorrido declara que el trabajo nace de
una entrada del Owner o de un desbloqueador **dentro del alcance ya autorizado**. Una
política de recurrencia es una **tercera vía** que la taxonomía no contempla. Y la regla
constitucional que limita la ejecución desatendida **no está ajustada** a lo que esa política
autoriza.

**Las dos presiones son la misma pregunta por dos caminos**, y por eso se aplican en un solo
acto. Una tercera presión quedó **fusionada** en la segunda por esta misma razón.

## 2 · Esqueleto de la enmienda

<!-- ads-lint-ignore-start: marcadores estructurales de decisión pendiente -->

```text
SI D-05 = A · reconocer la tercera vía            ← recomendada

  PARTE 1 · sobre la especificación de RECORRIDO
    AMPLÍA la taxonomía de entrada: la POLÍTICA DE RECURRENCIA APROBADA es fuente de
    trabajo, con su alcance, su presupuesto, sus umbrales, su caducidad y su revocación
    declarados. Fuera de esos límites NO crea trabajo.
    PRECISA que detectar e inventariar sigue SIN crear trabajo.

  PARTE 2 · sobre la lista de efecto sobre el kernel, en (a)
    AJUSTA la regla de ejecución desatendida AL ALCANCE EXACTO que la política autoriza,
    CONSERVANDO EL RESTO. La regla NO queda levantada en bloque: sólo lo que la política
    declara.

SI D-05 = B · no ampliar la taxonomía
  se declara que la política opera DENTRO del alcance ya autorizado, sin tercera vía y
  sin tocar la regla constitucional. Este borrador registra que esa lectura choca con lo
  que la sede afirma, y que el problema reaparecería en F6.
```

<!-- ads-lint-ignore-end -->

## 3 · Trazabilidad

| presión | fila | decisión | qué desbloquea |
|---|---|---|---|
| `PN-2` | `F5-OB-05` | `D-05` | el paso de APERTURA automática del sistema de cobertura |
| `PN-3` | `F5-OB-06` | `D-05` | la ejecución desatendida acotada, sin levantar la regla en bloque |

**Prueba prevista:** que la vía esté declarada en la especificación de recorrido, y que la
lista de efecto sobre el kernel nombre la regla y declare su disposición.
