# Spec de contrato API — F-028 Historial

`GET /api/v1/orders/me?page=0&pageSize=10` requiere JWT. El BFF adapta `page` local desde 0 a `GET /api/v1/pedidos/me?page=1&pageSize=10` de Ventas (página inicial 1, máximo 50) con scope `ventas:pedidos:leer`; la identidad proviene de `sub`/`customerId` del JWT.

`200`: `{"data":[{"orderId":"PED-1","state":"PAGADO","total":{"amount":355,"currency":"PEN"},"createdAt":"2026-09-27T18:30:00Z"}],"page":{"number":0,"size":10,"totalElements":1,"totalPages":1}}`.

El BFF deriva el titular del JWT y adapta la respuesta de Ventas (`items`, `total`, `page`, `pageSize`); no expone/acepta `clienteId`. El contrato H-03 está publicado; quedan implementación y prueba de autorización/paginación (`I-03`).

- [ ] **API-CA-F028-01:** Un parámetro cliente no altera el ámbito.
- [ ] **API-CA-F028-02:** La primera página local consulta la página 1 externa; lista vacía de Ventas se presenta como lista vacía, no error.
