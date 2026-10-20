# Spec funcional — F-014 Consultar disponibilidad de stock

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-014` |
| Versión | `0.2.0` · revisión 2026-10-20 |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |

## 2. Objetivo y alcance

Informa disponibilidad comercial de un SKU en la ficha sin reservar ni consumir inventario. Incluye estados G6 `DISPONIBLE`, `STOCK_BAJO`, `AGOTADO` e `INDETERMINADO`, adaptados por el BFF a `AVAILABLE`, `STOCK_LOW`, `OUT_OF_STOCK` y `UNDETERMINED`; excluye cantidades exactas, reserva, consumo y validación final de checkout.

## 3. Reglas y comportamiento

- **RN-F014-01:** Inventario es dueño del saldo `(sku, locationId)`; Marketplace no persiste ni descuenta stock.
- **RN-F014-02:** G6 resuelve una única fuente de cumplimiento elegible y realizable por contexto, conforme a D-INV-01/DEC-F-005. Marketplace no suma saldos de ubicaciones independientes ni resuelve un almacén. Mapeo ausente, ambiguo o no ejecutable produce `INDETERMINADO`; no se exponen almacenes, `onHand` ni `reserved`.
- **RN-F014-03:** Marketplace adapta los estados comerciales publicados por Productos; no calcula umbrales con saldos internos ni presupone acceso a `available`.
- **RN-F014-04:** Consultar no reserva ni garantiza unidades; la venta revalida inventario.
- **RN-F014-06:** La respuesta por estado de un SKU no acredita disponibilidad para la cantidad pedida. Para validar N unidades se requiere la operación comercial candidata `sku` + `quantity`, aún pendiente de homologación/configuración/prueba (`G-QUANTITY`/`X-P0-03`); la reserva definitiva pertenece a Ventas/Inventario.
- **RN-F014-05:** Sin SKU de variante se espera F-013; un error de stock no se transforma en agotado.
- **RN-F014-07:** `INDETERMINADO` es un resultado comercial válido HTTP 200, distinto de `AGOTADO` y de error/timeout del proveedor. No acredita disponibilidad ni cantidad; mientras persista, la ficha no habilita Agregar al carrito y permite volver a consultar. Una respuesta técnica inválida no se convierte en `INDETERMINADO`.

Al resolver un SKU, se consulta disponibilidad. El visitante ve “Disponible”, “Quedan pocas unidades”, “Agotado” o “Disponibilidad por confirmar”. El último ofrece volver a consultar y conserva ficha/precio sin afirmar posibilidad de compra. Si cambia variante, se invalida el estado anterior. Un fallo técnico muestra “No pudimos consultar disponibilidad”, con reintento; la ficha y precio siguen disponibles.

- [ ] **CA-F014-01:** El SKU agotado no se presenta como seleccionable para añadir al carrito cuando F-016 exista.
- [ ] **CA-F014-02:** Un fallo de Inventario no muestra “Agotado”.
- [ ] **CA-F014-03:** La consulta no modifica `reserved`, `onHand` ni disponibilidad.
- [ ] **CA-F014-04:** `DISPONIBLE` no se interpreta como garantía de N unidades en carrito o checkout.
- [ ] **CA-F014-05:** Los cuatro estados G6 se mapean de forma exhaustiva, incluido HTTP 200 `INDETERMINADO` → `UNDETERMINED`; un estado desconocido es respuesta inválida.
- [ ] **CA-F014-06:** Falta de fuente de cumplimiento realizable no se resuelve sumando ubicaciones; se conserva el resultado comercial indeterminado y se bloquea el CTA hasta nueva respuesta válida.

## 4. Dependencia

Fuentes: `SPEC-015`, `EXT-OUT-INV-01`, [OpenAPI G6 0.6.0-rc.1](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/contratos/http/openapi.yaml) y [DEC-F-005](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/arquitectura/decisiones/REGISTRO_DEC_F.md). La revisión alinea la documentación G1; conformidad bilateral, grant, implementación del proveedor y prueba REAL siguen dentro de `I-01`/`G-G6-COMPAT`.
