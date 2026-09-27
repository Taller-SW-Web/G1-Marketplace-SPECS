# Spec funcional — F-031 Reordenar una compra anterior

| Campo | Valor |
|---|---|
| ID | `F-031` |
| Estado | Aprobada para planificación; catálogo/stock condicionados por `I-01`. |

Permite copiar líneas elegibles de un pedido propio al carrito actual. Incluye revalidar SKU, precio y stock, sumar por SKU y reportar ajustes; excluye recrear dirección, cupón, precio histórico o pedido automático.

- **RN-F031-01:** Sólo se reordena un pedido autorizado de F-030.
- **RN-F031-02:** Cada SKU se valida como activo, comprable y disponible; precio histórico no se reutiliza.
- **RN-F031-03:** Líneas válidas se combinan por SKU; no elegibles se reportan sin abortar las demás.
- **RN-F031-04:** Reordenar no crea orden, reserva stock ni consume cupón.

- [ ] **CA-F031-01:** Pedido ajeno no añade ítems.
- [ ] **CA-F031-02:** SKU retirado se excluye con explicación.
