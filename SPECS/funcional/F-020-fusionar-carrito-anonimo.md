# Spec funcional — F-020 Fusionar carrito anónimo al iniciar sesión

| Campo | Valor |
|---|---|
| ID | `F-020` |
| Estado | Aprobada para planificación; revalidación externa condicionada por `I-01`. |

Al iniciar sesión, combina el carrito anónimo del navegador con el carrito activo del cliente. Incluye suma por SKU, ajuste por límite y trazabilidad; excluye fusionar favoritos o crear una segunda cuenta.

- **RN-F020-01:** La fusión ocurre una vez por carrito anónimo y es transaccional; origen pasa a `MERGED` con `mergedIntoCartId`.
- **RN-F020-02:** Líneas con mismo SKU se suman; se revalidan precio y disponibilidad y se ajustan al máximo confirmado, informando cada ajuste.
- **RN-F020-03:** Si el cliente no tiene carrito, el anónimo se reasigna sólo tras crear el carrito autenticado; nunca queda con dos dueños.
- **RN-F020-04:** Fallo previo al commit conserva ambos carritos. Reintentar no duplica cantidades.
- **RN-F020-05:** Ante una fusión fallida, el cliente puede reintentar o continuar con la sesión iniciada sin combinar. Continuar no ejecuta la fusión, no elimina el carrito anónimo y sólo deja operativo y visible el carrito autenticado; los artículos anónimos no se consideran parte de éste.

- [ ] **CA-F020-01:** Una fusión repetida no vuelve a sumar el carrito origen.
- [ ] **CA-F020-02:** Sólo el carrito autenticado final acepta mutaciones posteriores.
- [ ] **CA-F020-03:** Un ajuste por stock queda visible al cliente.
- [ ] **CA-F020-04:** Continuar sin combinar permite navegar con la sesión iniciada, sin sumar artículos anónimos ni presentarlos como parte del carrito autenticado.
