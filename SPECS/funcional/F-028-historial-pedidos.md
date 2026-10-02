# Spec funcional — F-028 Consultar historial de pedidos

| Campo | Valor |
|---|---|
| ID | `F-028` |
| Estado | Aprobada para planificación; integración bloqueada por `I-03`. |

Permite al cliente autenticado ver su lista paginada de pedidos, estado, fecha y total. Ventas es la fuente de verdad; Marketplace no replica el historial.

- **RN-F028-01:** Identidad se deriva del JWT; no se acepta `clienteId` del navegador.
- **RN-F028-02:** Sólo se muestran pedidos propios y el resumen mínimo; detalle corresponde a F-030.
- **RN-F028-03:** Paginación/orden provienen de Ventas; lista vacía es válida.

- [ ] **CA-F028-01:** Un usuario no puede enumerar pedidos de otro.
- [ ] **CA-F028-02:** Lista vacía ofrece acceso a catálogo.

Ventas hoy exige `clienteId` en query; se requiere `/me` o validación estricta contra JWT (`I-03`).
