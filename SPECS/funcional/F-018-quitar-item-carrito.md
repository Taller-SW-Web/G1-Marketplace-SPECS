# Spec funcional — F-018 Quitar un ítem del carrito

| Campo | Valor |
|---|---|
| ID | `F-018` |
| Estado | Aprobada para planificación. |

Permite retirar una línea del carrito activo. Incluye eliminación idempotente, actualización de versión y estado vacío; excluye mover a favoritos (`F-021`), reserva e inventario.

- **RN-F018-01:** Quitar elimina sólo `CartItem` del `sku` indicado y aumenta `Cart.version`.
- **RN-F018-02:** No consulta ni modifica stock, precio o Catálogo.
- **RN-F018-03:** Repetir la misma eliminación tiene resultado final seguro: línea ausente.
- **RN-F018-04:** Si era la última línea, el carrito sigue `ACTIVE` y F-019 muestra vacío.

- [ ] **CA-F018-01:** Quitar una línea no afecta otras líneas.
- [ ] **CA-F018-02:** Un reintento no produce error visible ni altera inventario.
