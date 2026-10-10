# Spec funcional — F-014 Consultar disponibilidad de stock

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-014` |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |

## 2. Objetivo y alcance

Informa disponibilidad comercial de un SKU en la ficha sin reservar ni consumir inventario. Incluye estados `DISPONIBLE`, `STOCK_BAJO` y `AGOTADO`; excluye cantidades exactas, reserva, consumo y validación final de checkout.

## 3. Reglas y comportamiento

- **RN-F014-01:** Inventario es dueño del saldo `(sku, locationId)`; Marketplace no persiste ni descuenta stock.
- **RN-F014-02:** Para el canal público se usa una proyección comercial agregada por SKU sobre ubicaciones elegibles. No se exponen almacenes, `onHand` ni `reserved`.
- **RN-F014-03:** Marketplace adapta los estados comerciales publicados por Productos; no calcula umbrales con saldos internos ni presupone acceso a `available`.
- **RN-F014-04:** Consultar no reserva ni garantiza unidades; la venta revalida inventario.
- **RN-F014-06:** La respuesta por estado de un SKU no acredita disponibilidad para la cantidad pedida. Para validar N unidades se requiere una operación comercial `sku` + `quantity` aún no publicada/homologada (`X-P0-03`); la reserva definitiva pertenece a Ventas/Inventario.
- **RN-F014-05:** Sin SKU de variante se espera F-013; un error de stock no se transforma en agotado.

Al resolver un SKU, se consulta disponibilidad. El visitante ve “Disponible”, “Quedan pocas unidades” o “Agotado”. Si cambia variante, se invalida el estado anterior. Error: “No pudimos consultar disponibilidad”, con reintento; la ficha y precio siguen disponibles.

- [ ] **CA-F014-01:** El SKU agotado no se presenta como seleccionable para añadir al carrito cuando F-016 exista.
- [ ] **CA-F014-02:** Un fallo de Inventario no muestra “Agotado”.
- [ ] **CA-F014-03:** La consulta no modifica `reserved`, `onHand` ni disponibilidad.
- [ ] **CA-F014-04:** `DISPONIBLE` no se interpreta como garantía de N unidades en carrito o checkout.

## 4. Dependencia

Fuente: `SPEC-015` y `EXT-OUT-INV-01`. La decisión de proyección agregada resuelve la ausencia de una ubicación elegida por el visitante; debe homologarse con el contrato externo dentro de `I-01`.
