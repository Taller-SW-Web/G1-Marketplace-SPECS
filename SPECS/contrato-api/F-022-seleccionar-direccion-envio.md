# Spec de contrato API — F-022 Dirección de envío

`GET /api/v1/checkout/delivery-addresses` y `POST /api/v1/checkout/delivery-addresses`, ambos requieren JWT.

POST:
```json
{"label":"Casa","street":"Av. Lima 123","district":"Miraflores","province":"Lima","department":"Lima","reference":"Dpto. 402","phone":"999999999"}
```

Respuesta `201`: `{"data":{"addressId":"ADR-1","label":"Casa", "...":"campos públicos necesarios"}}`. Errores: `400 ADDRESS_VALIDATION_ERROR`, `401 UNAUTHENTICATED`, `503 ADDRESS_SERVICE_UNAVAILABLE`.

El BFF extrae el titular del JWT y adapta Seguridad; no acepta `customerId` en request, no guarda dirección en Marketplace y nunca registra cuerpo completo en logs. La lista usa sólo datos necesarios para elección.

- [ ] **API-CA-F022-01:** Un token sólo recibe direcciones de su titular.
