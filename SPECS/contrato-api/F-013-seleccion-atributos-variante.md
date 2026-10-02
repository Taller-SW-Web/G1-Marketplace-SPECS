# Spec de contrato API — F-013 Seleccionar atributos y variante del producto

| Campo | Valor |
|---|---|
| Versión | `v1` |
| Propietario | BFF Marketplace; adaptador de Catálogo. |
| Autenticación | Pública para producto activo. |

## Endpoint

`GET /api/v1/catalog/products/{slug}/variants`

Respuesta `200`:

```json
{"data":{"productId":"PRD-1","hasVariants":true,"attributes":[{"id":"color","label":"Color","values":[{"id":"black","label":"Negro"}]}],"variants":[{"variantId":"VAR-1","sku":"AERO-42-BLK","status":"ACTIVE","attributes":{"color":"black","size":"42"},"image":{"url":"https://cdn.example.com/aero-black.webp","alt":"Aero X negro"}}]}}
```

El BFF filtra padre/variante no activos y nunca expone stock ni precio. Errores: `400 INVALID_PRODUCT_SLUG`, `404 PRODUCT_NOT_AVAILABLE`, `502 CATALOG_INVALID_RESPONSE`, `503 CATALOG_UNAVAILABLE`, `504 CATALOG_TIMEOUT`.

Reglas: `sku` es obligatorio y único por variante; atributos identificadores son completos; una combinación es única. Agregar atributos opcionales es compatible; cambios incompatibles requieren `v2`. Se propaga `X-Request-Id`.

Integración: BFF → `EXT-OUT-CAT-02`, ruta/auth/payload final pendientes (`I-01` / `OPEN-03`).

- [ ] **API-CA-F013-01:** Una variante activa retorna `variantId` y `sku` distintos.
- [ ] **API-CA-F013-02:** Una respuesta con SKU ausente o combinación duplicada es `502`, no una selección utilizable.
