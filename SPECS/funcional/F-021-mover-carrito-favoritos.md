# Spec funcional — F-021 Mover un ítem del carrito a favoritos

| Campo | Valor |
|---|---|
| ID | `F-021` |
| Estado | Aprobada para planificación; catálogo condicionado por `I-01`. |

Permite a un cliente autenticado guardar el producto de una línea en favoritos y retirarlo del carrito en una única operación local. Excluye favoritos anónimos y seleccionar una nueva variante.

- **RN-F021-01:** Favorito es de nivel `productId`; la línea mantiene SKU hasta que la operación completa.
- **RN-F021-02:** Se exige sesión. Visitante anónimo recibe inicio de sesión y su línea no cambia.
- **RN-F021-03:** Se crea/reutiliza `WishlistItem(customerId, productId)` y luego se retira el `CartItem` en la misma transacción local.
- **RN-F021-04:** Si producto ya es favorito, se elimina igualmente del carrito con resultado “Ya estaba en favoritos”.

- [ ] **CA-F021-01:** Error al crear favorito conserva la línea.
- [ ] **CA-F021-02:** El resultado no crea duplicados en favoritos.
