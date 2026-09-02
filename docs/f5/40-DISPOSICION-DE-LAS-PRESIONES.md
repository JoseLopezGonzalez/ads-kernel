# 40 · DISPOSICIÓN DE LAS PRESIONES NORMATIVAS · el acta de `A1`

**Una fila por presión vigente, con su disposición, el acto que la cierra y su prueba.**
Ésta es la sede que hace `A1` comprobable **por barrido y no por lectura**.

> **QUÉ ES.** Un artefacto **DERIVADO**. No cierra ninguna presión por sí mismo: cada fila
> cita el ACTO que la cierra, y ese acto vive en `O23`, en una enmienda aprobada o en la
> sección `(g)`. **No crea autoridad.**
>
> **EL CENSO NO SE ESCRIBE: SE DERIVA.** El control `F14` de [`validar-f5.py`](validar-f5.py)
> deriva las presiones vigentes del árbol y exige que TODAS tengan fila aquí con disposición
> y acto. Si la sede crece, el control se pone rojo.

```bash
# el censo VIGENTE, de su sede única
grep '^## `PN-' docs/evolucion/11-ARQUITECTURA-INTEGRADA.md | grep -vc 'RETIRADA\|FUSIONADA'
# las filas de esta acta
grep -cE '^\| `PN-[0-9]+` \|' docs/f5/40-DISPOSICION-DE-LAS-PRESIONES.md
```

---

## 1 · El acta

**Ninguna presión queda RETIRADA. Las diecisiete quedan RESUELTAS**, cada una con su acto.

| presión | disposición | acto que la cierra | artefacto | prueba posterior |
|---|---|---|---|---|
| `PN-1` | **RESUELTA** | `O23` §2 | [`(g)`](../rediseno/g-ESTADO-DURABLE-APROBADA.md) entera · [`E3`](../rediseno/a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md) `E3.3 bis` | `(g)` existe y su Anexo cubre las materias reservadas; `a.11` deja de declarar el diario PENDIENTE |
| `PN-2` | **RESUELTA** | `O23` §6 | [`E3`](../rediseno/a-ENMIENDA-E3-ARRANQUE-Y-POLITICA.md) `E3.2` | `b.15.1` declara la tercera vía con sus cuatro condiciones |
| `PN-3` | **RESUELTA** | `O23` §6 | `E3` `E3.3` | `a.11` nombra `G03` y declara su ajuste ACOTADO |
| `PN-6` | **RESUELTA** | `O23` §10 | la ratificación de `B-05`, registrada en `O23` | la confirmación existe con fecha y autoridad |
| `PN-7` | **RESUELTA** | `O23` §10 | [`E6`](../rediseno/a-ENMIENDA-E6-REANUDACION.md) `E6.1` | `b.14` distingue PUBLICADO de ESPECULATIVO |
| `PN-8` | **RESUELTA** | `O23` §7 | [`E4`](../rediseno/a-ENMIENDA-E4-COMPOSICION-DE-RUTAS.md) `E4.1` | la fila `AUD` declara `VER` `C-VER`, y `C-VER` está definido en el vocabulario |
| `PN-9` | **RESUELTA** | `O23` §10 | la ratificación de `B-05` | la confirmación existe; no se reinstaura la presión retirada |
| `PN-10` | **RESUELTA** | `O23` §10 | la ratificación de `B-05`, que la nombra expresamente | la lectura del estado durable de la iniciativa queda fijada |
| `PN-11` | **RESUELTA** | `O16` fijó la sede · `O23` §2 la materializa | `(g)` `g.14` | `(g)` tiene apartado de gobierno Git del control repo; `C7` intacto |
| `PN-12` | **RESUELTA** | `O23` §9 | la declaración de derivación mecánica | el mapa documental no se escribe a mano |
| `PN-13` | **RESUELTA** | `O23` §7 | `E4` `E4.2` | las filas `SIS` e `INV` admiten `DOM`, `SEG` y `DIS` con condición declarada |
| `PN-14` | **RESUELTA** | `O23` §7 | `E4` `E4.3` | ninguna tabla de participación de `(a)` ni `(b)` nombra un método donde va una capacidad |
| `PN-15` | **RESUELTA** | `O23` §5 | `E3` `E3.1` | **una fila por cada** `G20`, `G21`, `G22`, `G23`, con su disposición |
| `PN-16` | **RESUELTA, no retirada** | `O23` §8 | la declaración de grafía canónica | manda la grafía de la fuente aprobada; `(b)` **no se enmienda** |
| `PN-17` | **RESUELTA** | `O23` §4 | `(g)` `g.9` | el registro auxiliar existe como norma, separado del estado y del diario |
| `PN-18` | **RESUELTA, no retirada** | `O23` §8 | la misma declaración de grafía | ídem, para el segundo identificador |
| `PN-19` | **RESUELTA, no retirada** | `O23` §3 | `(g)` `g.15` | el contrato que dependía de ella deja de estar bloqueado, **sin que ningún otro campo cambie** |

**Y las dos que NO son vigentes, dichas para que el censo cuadre:**

```text
PN-4   RETIRADA en su día, con motivo escrito. Su sede la declaraba «reinstaurable por F5
       si el Owner lo prefiere». `O23` §10 aprueba la retirada de `B-05`: NO se reinstaura,
       y decirlo es parte del acto
PN-5   FUSIONADA en `PN-3`, y se cierra con ella
```

## 2 · Cómo se activaron las condiciones de reversión

**Cinco presiones declaraban que, con cierta respuesta, quedarían RESUELTAS en vez de
retiradas. Se dice cuáles se activaron y cuáles no, porque invocar la que no toca sería
fabricar una cobertura que no se tiene.**

```text
ACTIVADAS, y su supuesto es literalmente lo que el Owner decidió

  PN-16 y PN-18   el Owner eligió la grafía de la FUENTE APROBADA, que es el supuesto
                  exacto de su cláusula: quedan RESUELTAS en vez de retiradas, y (b) no
                  se enmienda
  PN-19           el gobierno del verificador externo cabe entero en (g) y su contrato
                  derivado, SIN tocar el contrato de fuentes, E2 ni la constitución
  PN-15           las cuatro reglas se CONSERVAN y el circuito nuevo se SUBORDINA

NO ACTIVADAS, y se dice para no invocar una cobertura que no se tiene

  PN-11           su cláusula era declarar el control repo FUERA del gobierno Git
                  normativo. NO es lo que se hizo: se resuelve por su materia mínima
  PN-12 · PN-13   sus cláusulas describían la OTRA salida, que no se eligió
  PN-14
  PN-17           SU CLÁUSULA NO SE ACTIVA. Describe la salida «el caso queda fuera del
                  predicado a propósito», y el Owner eligió otra. Queda RESUELTA por su
                  MATERIA MÍNIMA —declarar qué significa registrar y quién es su
                  productor—, y NO por su cláusula de reversión
```

## 3 · Lo que esta acta NO afirma

```text
NO AFIRMA   que ninguna de las diecisiete esté IMPLEMENTADA. Ninguna lo está: F5 emite
            norma, y construir es F6
NO AFIRMA   que ningún hallazgo vivo esté superado
NO AFIRMA   que F5 esté cerrada. Sólo se cierra por acto posterior y expreso del Owner
NO CIERRA   ninguna presión por sí misma: cada fila CITA el acto que la cierra
```
