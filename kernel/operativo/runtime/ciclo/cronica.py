"""cronica — la SECUENCIA de lo que pasó en la oficina, derivada del diario durable.

No hay un registro aparte que alguien mantenga: cada toma, latido, entrega, handoff,
dictamen, devolución, bloqueo, reoferta y cierre es una transacción del motor con su
`autor` (la instancia), su `clase` y su `motivo`, y el diario las conserva en el orden en
que se confirmaron. La crónica las lee y las cuenta en ese orden. Dos lecturas del mismo
diario producen la misma crónica.
"""
from __future__ import annotations

import re

CLASES_DE_LA_OFICINA = (
    "runtime.lease.", "runtime.paquete.", "runtime.efecto.", "ciclo.entrega", "ciclo.handoff",
    "ciclo.gate", "ciclo.dictamen", "ciclo.cierre", "ciclo.plan", "ciclo.equipos", "ciclo.correccion",
    "ciclo.checkpoint", "checkpoint", "runtime.checkpoint",
)

_PAQUETE = re.compile(r"\b(pq-[0-9a-f]{6,})\b")
_ITEM = re.compile(r"\b(enc-[a-z0-9-]+|it-[a-z0-9-]+)\b")


def _objetos(evento):
    salida = []
    for operacion in evento.get("operaciones") or []:
        ruta = str(operacion.get("ruta") or operacion.get("logica") or "")
        if ruta:
            salida.append(ruta)
    return salida


def derivar(almacen, *, item=None, paquetes=None):
    """Las filas de la crónica: secuencia, autor, clase, motivo, paquete e item (si se deducen)."""
    filas = []
    items_por_paquete = {}
    for ruta in almacen.listar("paquetes"):
        objeto = almacen.leer(ruta)
        if objeto:
            items_por_paquete[objeto["id"]] = objeto.get("item")
    for evento in almacen.diario():
        # el diario guarda TRES fases por transacción (abierta, preparada, confirmada); un
        # suceso de la oficina es la transacción CONFIRMADA, y sólo ésa. Contar las tres
        # triplicaba cada fila (medido en el cuarto dogfood: 492 rachas de tres iguales)
        tipo = str(evento.get("tipo") or "")
        if tipo and tipo != "transicion.confirmada":
            continue
        clase = str(evento.get("clase") or "")
        if not any(clase.startswith(prefijo) for prefijo in CLASES_DE_LA_OFICINA):
            continue
        motivo = str(evento.get("motivo") or "")
        objetos = _objetos(evento)
        texto = motivo + " " + " ".join(objetos)
        paquete = None
        casa = _PAQUETE.search(texto)
        if casa:
            paquete = casa.group(1)
        item_de = items_por_paquete.get(paquete) if paquete else None
        if item_de is None:
            casa = _ITEM.search(texto)
            item_de = casa.group(1) if casa else None
        if item and item_de != item:
            continue
        if paquetes and paquete not in paquetes:
            continue
        filas.append({
            "secuencia": evento.get("secuencia"),
            "transaccion": str(evento.get("transaccion") or ""),
            "autor": str(evento.get("autor") or ""),
            "clase": clase,
            "motivo": motivo,
            "paquete": paquete,
            "item": item_de,
            "objetos": objetos,
        })
    return filas


def como_texto(filas):
    lineas = ["CRÓNICA DE LA OFICINA · " + str(len(filas)) + " sucesos, en el orden del diario",
              "=" * 78,
              "%-6s %-16s %-30s %-16s %s" % ("seq", "quién", "qué", "paquete", "motivo")]
    for fila in filas:
        lineas.append("%-6s %-16s %-30s %-16s %s" % (
            fila["secuencia"], fila["autor"][:16], fila["clase"][:30], (fila["paquete"] or "")[:16],
            fila["motivo"][:110]))
    return "\n".join(lineas)


def por_trabajador(filas):
    """Qué tomó, entregó y devolvió cada instancia, en orden."""
    salida = {}
    for fila in filas:
        salida.setdefault(fila["autor"], []).append(
            {"secuencia": fila["secuencia"], "clase": fila["clase"], "paquete": fila["paquete"], "item": fila["item"]})
    return salida
