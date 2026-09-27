# Spec de contrato API — F-012 Visualizar precio, oferta y descuento vigente

> Contrato de lectura entre el frontend y el BFF Marketplace. El BFF adapta Pricing de Productos y Ofertas y no convierte precio, oferta ni vigencia en datos propios.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID funcional | `F-012` |
| Versión del contrato | `v1` |
| Estado | Aprobada para planificación; integración externa condicionada por `I-01`. |
| Spec funcional relacionada | `../funcional/F-012-precio-oferta-descuento.md` |
| Spec UI relacionada | `../ui/F-012-precio-oferta-descuento.md` |
| Última actualización | `2026-09-27` |

## 2. Propósito y límites

| Campo | Valor |
|---|---|
| Servicio propietario | Backend Marketplace (BFF/adaptador). |
| Consumidor | Frontend Marketplace. |
| Base URL | `/api/v1`. |
| Autenticación | No requerida para la lectura pública de un producto activo. |
| Formato | `application/json`; errores `application/problem+json`. |
| Fuente externa | Pricing, Productos y Ofertas, `EXT-OUT-PRICE-01`. |

El contrato devuelve el precio de un SKU aplicable a la ficha. Excluye cupón, promociones de cesta, envío, impuestos, stock, carrito y total de pedido.

## 3. Endpoints

| ID | Método | Ruta | Propósito | Autorización |
|---|---|---|---|---|
| `API-F012-001` | `GET` | `/catalog/products/{slug}/price` | Consultar precio vigente para el producto y, si aplica, el SKU seleccionado. | Pública; producto comercial activo. |

## 4. Detalle de endpoint

### API-F012-001 — Obtener precio vigente de ficha

**Método y ruta:** `GET /api/v1/catalog/products/{slug}/price?sku={sku-opcional}`

**Headers:**

```text
Accept: application/json
X-Request-Id: <UUID opcional>
```

**Parámetros:**

| Nombre | Ubicación | Tipo | Obligatorio | Regla |
|---|---|---|---:|---|
| `slug` | path | string | Sí | Mismo formato canónico de F-011. |
| `sku` | query | string | No | Obligatorio si el producto posee variantes; si se envía debe pertenecer al producto activo. |

**Respuesta `200 OK`:**

```json
{
  "data": {
    "productId": "PRD-9f419c42",
    "sku": "AERO-X-42-BLK",
    "price": {
      "regularAmount": 200.00,
      "saleAmount": 170.00,
      "currency": "PEN",
      "discountPercent": 15,
      "validFrom": "2026-09-01T00:00:00Z",
      "validUntil": "2026-10-01T00:00:00Z",
      "priceVersion": 8
    }
  },
  "meta": {
    "channel": "MARKETPLACE",
    "retrievedAt": "2026-09-27T18:15:00Z"
  }
}
```

`saleAmount`, `discountPercent` y `validUntil` pueden ser `null`. `discountPercent` lo calcula el BFF sólo como representación de los importes autoritativos; no es una regla independiente de Pricing.

**Errores:**

| HTTP | Código | Cuándo ocurre |
|---:|---|---|
| 400 | `INVALID_PRODUCT_SLUG` | Slug inválido. |
| 404 | `PRODUCT_NOT_AVAILABLE` | Producto inexistente o no elegible. |
| 409 | `PRODUCT_VARIANT_SELECTION_REQUIRED` | Producto con variantes sin `sku`. |
| 409 | `SKU_NOT_BELONG_TO_PRODUCT` | SKU no corresponde al producto o no es elegible. |
| 422 | `PRICE_NOT_AVAILABLE` | No existe un precio comercial vigente para el SKU/canal. |
| 502 | `PRICING_INVALID_RESPONSE` | Pricing devolvió importes, moneda o vigencia inválidos. |
| 503 | `PRICING_UNAVAILABLE` | No se obtuvo una respuesta utilizable. |
| 504 | `PRICING_TIMEOUT` | Se agotó el tiempo de espera. |

Los errores usan Problem Details con `code`, `status`, `instance` y `requestId`; no incluyen reglas internas de Pricing.

## 5. Reglas del contrato

- `regularAmount` es decimal positivo y obligatorio. `saleAmount` es nulo o decimal positivo menor que el regular.
- `currency` es ISO 4217. No hay conversión de moneda en Marketplace.
- La representación se consulta con `channel=MARKETPLACE` y tiempo actual del BFF; el frontend no controla el parámetro temporal.
- Si hay oferta, `validFrom <= retrievedAt < validUntil` cuando existe fin. El BFF no sirve caché más allá de `validUntil`.
- La respuesta puede tener `Cache-Control: public, max-age=30, stale-while-revalidate=30`, limitada siempre por la vigencia más cercana.
- `GET` es seguro e idempotente. Agregar campos opcionales es compatible en `v1`; romper campos requiere `v2`.

## 6. Integraciones y eventos

| Integración | Dirección | Datos intercambiados | Sincronía | Estado |
|---|---|---|---|---|
| Frontend → BFF Marketplace | Entrada | `slug`, `sku` opcional, `X-Request-Id`. | REST. | Definida aquí. |
| BFF → Pricing | Salida | `sku`, canal `MARKETPLACE`, momento actual; recibe importes, moneda, vigencia y versión. | REST. | Semántica documentada; ruta/auth/OpenAPI pendientes por `I-01` / `OPEN-03`. |

`pricing.price.changed` puede invalidar caché en el futuro, pero no es requisito de este contrato mientras no exista homologación de consumo del evento.

## 7. Seguridad y observabilidad

- Sólo expone precios de productos comerciales activos; no devuelve costos internos, reglas de prioridad ni condiciones administrativas.
- El BFF valida relación `slug`–`sku` antes de consultar Pricing y propaga/genera `X-Request-Id`.
- Registra `requestId`, hash técnico de SKU, `priceVersion`, resultado y latencia. No registra tokens ni cuerpos completos externos.
- Aplica timeout, circuito de fallo y caché acotada en el adaptador; no reintenta indefinidamente una lectura del visitante.

## 8. Criterios de aceptación del contrato

- [ ] **API-CA-F012-01:** Un producto simple con precio regular válido responde `200` con importe positivo, moneda y versión, sin datos de cupón o stock.
- [ ] **API-CA-F012-02:** Una oferta válida responde `saleAmount`, descuento derivado y vigencia; sin oferta esos campos son `null`.
- [ ] **API-CA-F012-03:** Un producto con variantes sin SKU responde `409 PRODUCT_VARIANT_SELECTION_REQUIRED` y no devuelve precio arbitrario.
- [ ] **API-CA-F012-04:** Una respuesta externa con oferta inválida, moneda inválida o importe no positivo no llega al frontend y resulta en `502`.
- [ ] **API-CA-F012-05:** Antes de integrar, Productos y Ofertas homologa ruta corriente, canal, autorización de servicio y esquema OpenAPI de `EXT-OUT-PRICE-01` (`I-01` / `OPEN-03`).
