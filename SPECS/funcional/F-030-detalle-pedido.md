# Spec funcional — F-030 Visualizar detalle de pedido

| Campo | Valor |
|---|---|
| ID | `F-030` |
| Estado | Aprobada para planificación; depende de `I-03`. |

Muestra detalle de un pedido propio: líneas históricas, importes, estado, dirección resumida e historial de estados. Excluye modificar pedido, seguimiento de Despacho (F-032) y datos de pago sensibles.

- **RN-F030-01:** Ventas autoriza propiedad; Marketplace no usa `orderId` como permiso suficiente.
- **RN-F030-02:** Se presentan snapshots históricos, no información vigente de catálogo.
- **RN-F030-03:** Dirección y contacto se minimizan; no se expone documento ni tarjeta.

- [ ] **CA-F030-01:** Pedido ajeno responde no disponible sin filtrar existencia.
- [ ] **CA-F030-02:** El detalle conserva precios históricos aunque catálogo cambie.
