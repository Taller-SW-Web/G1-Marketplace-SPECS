# Spec funcional — F-032 Consultar seguimiento de despacho

| Campo | Valor |
|---|---|
| ID | `F-032` |
| Estado | Aprobada para planificación; requiere scope `seguimientos:leer` (`I-06`). |

Permite consultar estado/hitos de despacho de pedido propio. Incluye fecha estimada e incidencias publicables; excluye ubicación en tiempo real, datos del repartidor y modificación.

- **RN-F032-01:** Marketplace verifica propiedad antes de consultar Despacho por `idPedido`.
- **RN-F032-02:** Despacho es dueño de tracking; Marketplace no persiste ni infiere hitos.
- **RN-F032-03:** Sólo estado, hitos, fecha estimada/incidencia genérica; nunca teléfono, coordenadas o repartidor.

- [ ] **CA-F032-01:** Pedido sin despacho muestra estado informativo, no error técnico.
- [ ] **CA-F032-02:** Pedido ajeno no permite seguimiento.
