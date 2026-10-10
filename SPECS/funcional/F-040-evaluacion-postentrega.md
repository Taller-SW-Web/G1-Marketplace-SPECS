# Spec funcional — F-040 Registrar evaluación postentrega

| ID | Estado |
|---|---|
| `F-040` | Contrato CSAT H-04 publicado; implementación y pruebas de `I-04` pendientes. |

Invita tras pedido `ENTREGADO` a evaluar con Bien/Regular/Mal, motivos contextuales y comentario opcional. Marketplace persiste sólo `PostDeliveryPrompt`; Ventas persiste CSAT.

- Sólo elegible tras tracking/pedido entregado; una vez por pedido.
- Mapeo decidido: Bien→5, Regular→3, Mal→1. Motivos se serializan de forma legible en comentario hasta ampliar contrato.
- Ventas valida pedido propio contra el JWT, estado `ENTREGADO` y unicidad de la evaluación; pedido no entregado produce `422 ORDER_NOT_DELIVERED` y duplicado `409 CSAT_ALREADY_SUBMITTED`.
- Éxito o conflicto duplicado marca prompt `SUBMITTED`; baja calificación no crea reclamo automáticamente.

- [ ] **CA-F040-01:** Pedido no entregado no muestra encuesta.
- [ ] **CA-F040-02:** Respuesta duplicada no se vuelve a enviar.
