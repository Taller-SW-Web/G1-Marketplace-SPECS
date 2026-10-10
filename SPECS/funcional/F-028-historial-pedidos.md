# Spec funcional — F-028 Consultar historial de pedidos

| Campo | Valor |
|---|---|
| ID | `F-028` |
| Estado | Contrato de historial propio H-03 publicado; integración y pruebas de `I-03` pendientes. |

Permite al cliente autenticado ver su lista paginada de pedidos, estado, fecha y total. Ventas es la fuente de verdad; Marketplace no replica el historial.

- **RN-F028-01:** Identidad se deriva del JWT; no se acepta `clienteId` del navegador.
- **RN-F028-02:** Sólo se muestran pedidos propios y el resumen mínimo; detalle corresponde a F-030.
- **RN-F028-03:** Paginación/orden provienen de Ventas; lista vacía es válida.

- [ ] **CA-F028-01:** Un usuario no puede enumerar pedidos de otro.
- [ ] **CA-F028-02:** Lista vacía ofrece acceso a catálogo.

Ventas publicó `GET /api/v1/pedidos/me` con identidad del JWT, `page` desde 1 y lista vacía `200`. El endpoint con `clienteId` queda sólo para backoffice; Marketplace usa `/me` y comprueba autorización en integración.
