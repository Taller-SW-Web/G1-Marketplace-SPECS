# Spec de contrato API — F-022 Dirección de envío

`GET /api/v1/checkout/delivery-addresses` y `POST /api/v1/checkout/delivery-addresses`, ambos requieren JWT.

GET devuelve `200` con `{"data":[]}` o una lista de direcciones propias dentro de `data`.

POST:
```json
{"label":"Casa","street":"Av. Lima 123","district":"Miraflores","province":"Lima","department":"Lima","reference":"Dpto. 402","phone":"999999999"}
```

POST devuelve `201` con una sola dirección dentro de `data`. Cada dirección incluye `addressId`, `street`, `district`, `province` y `department`. Incluye `label` y `reference` si G7 los devuelve. Errores: `400 ADDRESS_VALIDATION_ERROR`, `401 UNAUTHENTICATED`, `503 ADDRESS_SERVICE_UNAVAILABLE`.

G7 no define teléfono en su esquema de dirección. El BFF valida `phone` como parte del formulario, lo excluye de la llamada a G7 y no lo devuelve. El contacto del pedido se rige por su propio contrato. La homologación REAL y la resolución definitiva del dato siguen en G-ADDRESS.

El BFF extrae el titular del JWT y adapta Seguridad; no acepta `customerId` en request, no guarda dirección en Marketplace y nunca registra cuerpo completo en logs. La lista usa sólo datos necesarios para elección.

- [ ] **API-CA-F022-01:** Un token sólo recibe direcciones de su titular.
