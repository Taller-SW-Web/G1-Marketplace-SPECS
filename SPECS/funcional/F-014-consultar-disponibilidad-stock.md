# Spec funcional — F-014 Consultar disponibilidad de stock

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-014` |
| Versión | `0.2.0` |
| Estado | Aprobada para planificación; actualización a cuatro estados alineada con M01 de G6; aprobación G1 e integración pendientes; integración condicionada por `I-01`. |

## 2. Objetivo y alcance

Informa disponibilidad comercial de un SKU en la ficha sin reservar ni consumir inventario. Incluye estados `DISPONIBLE`, `STOCK_BAJO`, `AGOTADO` e `INDETERMINADO`; excluye cantidades exactas, reserva, consumo y validación final de checkout.

## 3. Reglas y comportamiento

- **RN-F014-01:** Inventario es dueño del saldo `(sku, locationId)`; Marketplace no persiste ni descuenta stock.
- **RN-F014-02:** Para el canal público, Productos resuelve una única ruta de abastecimiento ejecutable por SKU. Marketplace no agrega saldos entre puntos de cumplimiento independientes: si Productos no puede resolver una ruta única y verificable, el estado es `INDETERMINADO`. No se exponen almacenes, `onHand` ni `reserved`.
- **RN-F014-03:** Marketplace adapta los estados comerciales publicados por Productos; no calcula umbrales con saldos internos ni presupone acceso a `available`.
- **RN-F014-04:** Consultar no reserva ni garantiza unidades; la venta revalida inventario.
- **RN-F014-06:** La respuesta por estado de un SKU no acredita disponibilidad para la cantidad pedida. Para validar N unidades se requiere una operación comercial `POST /api/v1/inventario/disponibilidad/comercial/verificar` publicada por G6 y aún pendiente de homologación operativa de G1 (`X-P0-03`); la reserva definitiva pertenece a Ventas/Inventario.
- **RN-F014-05:** Sin SKU de variante se espera F-013; un error de stock no se transforma en agotado.

Al resolver un SKU, se consulta disponibilidad. El visitante ve “Disponible”, “Quedan pocas unidades”, “Agotado” o “Disponibilidad por confirmar”. Si cambia variante, se invalida el estado anterior. Error técnico: “No pudimos consultar disponibilidad”, con reintento; la ficha y precio siguen disponibles. `INDETERMINADO` no es un error: se muestra como estado propio, con reintento, sin prometer unidades ni presentarse como agotado.

- [ ] **CA-F014-01:** El SKU agotado no se presenta como seleccionable para añadir al carrito cuando F-016 exista.
- [ ] **CA-F014-02:** Un fallo de Inventario no muestra “Agotado”.
- [ ] **CA-F014-03:** La consulta no modifica `reserved`, `onHand` ni disponibilidad.
- [ ] **CA-F014-04:** `DISPONIBLE` no se interpreta como garantía de N unidades en carrito o checkout.
- [ ] **CA-F014-05:** `INDETERMINADO` se muestra como “Disponibilidad por confirmar”, admite reintento y no se presenta como agotado ni como disponibilidad garantizada.

## 4. Dependencia

Fuente: `SPEC-015` y `EXT-OUT-INV-01`. La decisión de una única ruta de abastecimiento ejecutable resuelve la ausencia de una ubicación elegida por el visitante; debe homologarse con el contrato externo dentro de `I-01`. El cuarto estado (`INDETERMINADO` → `UNDETERMINED`) corresponde al registro bilateral `M-01` y cuenta con conformidad comunicada de G6; F-014 real conserva los permisos, pruebas y aprobación de G1 pendientes.

## Contraste con G6 — 03/11/2026

Fuente: [M01–M03 del acuerdo G1/G6](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/40b566976fb94d924116dcd01d41b3276c2bc9e3/integraciones/ACUERDO_G1_G6_H4_2026-10-20.md). Se adopta la semántica del owner para avanzar diseño y pruebas propias. El código local/MOCK no acredita homologación REAL ni cierra la issue. Se conserva fuente única de cumplimiento; no se suman ubicaciones ni se garantiza cantidad por consultar un estado.
