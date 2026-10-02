# Spec de contrato API — F-006 Inicio

`GET /api/v1/catalog/home` público: `categories[]` y `featuredProducts[]` con id/nombre/slug/imagen/tarjeta comercial. BFF filtra activos; `200` admite arreglos vacíos, `503 CATALOG_UNAVAILABLE`; externo pendiente `I-01`.

- [ ] **API-CA-F006-01:** No devuelve datos administrativos.
