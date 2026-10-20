# Spec de contrato API — F-014 Consultar disponibilidad de stock

Versión 0.2.0 · Revisión 2026-10-20 · Alineación documental G1; integración REAL pendiente de I-01/G-G6-COMPAT.

`GET /api/v1/catalog/products/{slug}/availability?sku={sku}` — lectura pública de disponibilidad comercial por SKU.

```json
{"data":{"productId":"PRD-1","sku":"AERO-42-BLK","availability":"STOCK_LOW","checkedAt":"2026-09-27T18:15:00Z"}}
```

`availability` admite exactamente `AVAILABLE`, `STOCK_LOW`, `OUT_OF_STOCK` o `UNDETERMINED`. El mapeo G6→BFF es `DISPONIBLE`→`AVAILABLE`, `STOCK_BAJO`→`STOCK_LOW`, `AGOTADO`→`OUT_OF_STOCK`, `INDETERMINADO`→`UNDETERMINED`. Los cuatro resultados conservan HTTP 200. El BFF no expone cantidades, `locationId`, `onHand` ni `reserved`.

`UNDETERMINED` informa que G6 no puede demostrar una fuente única de cumplimiento realizable; no significa agotado, disponibilidad garantizada ni fallo técnico. G1 no agrega ubicaciones ni inventa contexto de cumplimiento. Un enum desconocido, SKU ausente/duplicado o respuesta no correspondiente al SKU solicitado es `502 INVENTORY_INVALID_RESPONSE`, nunca un estado comercial de reemplazo.

`checkedAt` es el instante UTC de observación del BFF, no una vigencia de reserva ni garantía de cumplimiento de G6.

Errores: `400 INVALID_PRODUCT_SLUG`, `409 PRODUCT_VARIANT_SELECTION_REQUIRED`/`SKU_NOT_BELONG_TO_PRODUCT`, `502 INVENTORY_INVALID_RESPONSE`, `503 INVENTORY_UNAVAILABLE`, `504 INVENTORY_TIMEOUT`.

Consulta segura e idempotente; caché corta máxima 30 s por SKU y canal `MARKETPLACE`, invalidada al cambiar selección. BFF → `GET /api/v1/inventario/disponibilidad/comercial?skus={sku}&canal=MARKETPLACE`: `skus` es la lista CSV contractual (G1 solicita aquí un SKU); comprobar la respuesta y seleccionar sólo el elemento de ese SKU. G6 exige token de servicio con audiencia `api-productos`, cliente `modulo-marketplace` y scope `inventario:disponibilidad:leer`; declaración de contrato no acredita grant. La fuente G6 sigue provisional: homologar configuración, envelope y runtime dentro de `I-01`/`G-G6-COMPAT` antes de activarla.

El GET sólo informa estado comercial; no valida N unidades. La operación candidata `POST /api/v1/inventario/disponibilidad/comercial/verificar` para `sku` + `quantity` tiene homologación y contexto de cumplimiento separados (`G-QUANTITY`/`X-P0-03`); no se sustituye por balances internos ni se inventa `fulfillment_ref` en este GET.

- [ ] **API-CA-F014-01:** Error externo nunca se mapea a `OUT_OF_STOCK`.
- [ ] **API-CA-F014-02:** La respuesta no contiene saldo ni ubicación.
- [ ] **API-CA-F014-03:** HTTP 200 `INDETERMINADO` se preserva como `UNDETERMINED`; fallo de red/503/timeout y enum inválido mantienen sus errores técnicos.
- [ ] **API-CA-F014-04:** Request por SKU/canal y respuesta coinciden; el adaptador no suma ni expone ubicaciones.

Referencia versionada: [OpenAPI G6 0.6.0-rc.1](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/contratos/http/openapi.yaml), operación `consultarDisponibilidadComercial` y schemas `DisponibilidadComercial`/`ConsultaDisponibilidadComercialResponse`.
