# Spec de contrato API — F-015 Visualizar productos relacionados

`GET /api/v1/catalog/products/{slug}/recommendations` — lectura pública del BFF Marketplace.

```json
{"data":[{"productId":"PRD-REC-1","slug":"medias-runner","name":"Medias Runner","image":{"url":"https://cdn.example.com/medias.webp","alt":"Medias Runner"},"type":"CROSS_SELL","price":{"amount":89.90,"currency":"PEN"},"presentationOrder":1}],"meta":{"sourceProductId":"PRD-1"}}
```

`type` admite `CROSS_SELL` o `UPSELL`; precio puede ser `null`. Se devuelve un máximo de 8 tarjetas completas, activas y deduplicadas. El BFF consulta `EXT-OUT-REC-01` y enriquece con Catálogo; candidatos no enriquecibles se omiten. `200` con arreglo vacío es válido. Errores técnicos se degradan a arreglo vacío para esta región no crítica y se registran con `X-Request-Id`; no se exponen errores externos al visitante.

Integración y contrato externo siguen pendientes (`I-01` / `OPEN-03`), incluido request exacto, auth y consulta batch de catálogo.

- [ ] **API-CA-F015-01:** La salida no contiene duplicados ni el producto origen.
- [ ] **API-CA-F015-02:** Una recomendación sin slug/nombre/imagen comercial válida no llega al frontend.
