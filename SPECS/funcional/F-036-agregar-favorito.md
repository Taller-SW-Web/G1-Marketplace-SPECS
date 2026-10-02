# Spec funcional — F-036 Agregar producto a favoritos

| ID | Estado |
|---|---|
| `F-036` | Aprobada; Catálogo condicionado por `I-01`. |

Guarda un producto activo para cliente autenticado. Favorito es `productId`, no SKU; operación idempotente por `customerId + productId`. Sin sesión, redirige a login sin crear favorito anónimo.

- [ ] **CA-F036-01:** Repetir guardado no duplica fila.
- [ ] **CA-F036-02:** Producto inactivo no se guarda.
