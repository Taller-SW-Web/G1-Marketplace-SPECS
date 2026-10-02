# Spec funcional — F-040 Registrar evaluación postentrega

| ID | Estado |
|---|---|
| `F-040` | Aprobada para planificación; CSAT condicionado por `I-04`. |

Invita tras pedido `ENTREGADO` a evaluar con Bien/Regular/Mal, motivos contextuales y comentario opcional. Marketplace persiste sólo `PostDeliveryPrompt`; Ventas persiste CSAT.

- Sólo elegible tras tracking/pedido entregado; una vez por pedido.
- Mapeo decidido: Bien→5, Regular→3, Mal→1. Motivos se serializan de forma legible en comentario hasta ampliar contrato.
- Éxito o conflicto duplicado marca prompt `SUBMITTED`; baja calificación no crea reclamo automáticamente.

- [ ] **CA-F040-01:** Pedido no entregado no muestra encuesta.
- [ ] **CA-F040-02:** Respuesta duplicada no se vuelve a enviar.
