# Spec de contrato API — F-033 Plantilla

Contrato interno `POST /internal/v1/notifications/render`: `{"type":"ORDER_CONFIRMATION","eventKey":"ORD-1:CREATED","orderId":"PED-1","payloadVersion":"v1"}`. Retorna asunto, HTML/texto y metadatos, sin destinatario. Requiere servicio.

Render determinista por `type + eventKey + payloadVersion`; recomendados opcionales. No se expone al navegador ni guarda HTML como entidad de dominio.

- [ ] **API-CA-F033-01:** Misma entrada/version produce contenido semánticamente igual.
