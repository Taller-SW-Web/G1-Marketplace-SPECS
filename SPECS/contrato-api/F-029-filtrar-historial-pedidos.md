# Spec de contrato API — F-029 Filtros de historial

Extiende `GET /api/v1/orders/me` con `state`, `from`, `to`, `page` y `pageSize`. `state` acepta los estados publicados de Ventas; `from/to` son ISO 8601 y máximo un año de intervalo por solicitud. `400 INVALID_DATE_RANGE` evita consulta externa. La identidad sigue derivada del JWT y depende de `I-03`.

- [ ] **API-CA-F029-01:** Un rango invertido devuelve `400` sin llamar a Ventas.
