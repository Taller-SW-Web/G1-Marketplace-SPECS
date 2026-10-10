# Spec funcional — F-016 Agregar ítem al carrito

| Campo | Valor |
|---|---|
| ID | `F-016` |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración de catálogo/stock condicionada por `I-01`. |

Permite a un visitante o cliente agregar un SKU vendible al carrito activo. Incluye crear o recuperar el carrito, agregar una unidad o sumar sobre una línea existente y refrescar su snapshot informativo. Excluye reserva, pago, cupón y favoritos.

- **RN-F016-01:** La línea se identifica por `cartId + sku`; nunca por `variantId`.
- **RN-F016-02:** Antes de persistir, Marketplace confirma que el SKU es comercialmente elegible y que el estado comercial no sea `AGOTADO`. Esto no prueba disponibilidad para N unidades ni reserva inventario (`X-P0-03`).
- **RN-F016-03:** Si el SKU ya existe, incrementa su cantidad de forma atómica hasta el máximo local permitido. Sólo ajusta a un máximo de stock cuando Productos devuelva una cantidad permitida mediante contrato cuantitativo homologado; el estado por SKU no permite inferirla.
- **RN-F016-04:** El carrito puede ser anónimo mediante cookie segura o autenticado; sólo una identidad es dueña del carrito activo.
- **RN-F016-05:** Precio es snapshot informativo y se revalida después; no garantiza checkout.

Flujo: usuario elige variante si aplica, F-014 informa estado comercial, pulsa “Agregar al carrito”, BFF valida SKU/precio y reglas que el proveedor realmente publica, crea o actualiza `CartItem` y devuelve carrito actualizado. La cantidad del carrito es intención de compra, no reserva. Stock insuficiente para N unidades sólo puede afirmarse con una operación cuantitativa homologada o con la reserva autoritativa posterior. Un fallo confirmado no crea una línea parcial.

- [ ] **CA-F016-01:** Agregar un SKU nuevo crea una única línea con cantidad uno.
- [ ] **CA-F016-02:** Repetir el mismo SKU no duplica la línea; respeta el límite local y no inventa un máximo disponible externo.
- [ ] **CA-F016-03:** Agregar no descuenta ni reserva stock.
- [ ] **CA-F016-04:** El error externo deja el carrito local sin mutación.

Fuentes: modelo lógico, F-012–F-014 y contratos Productos y Ofertas. Pendiente `I-01` para consulta final de SKU, precio y disponibilidad.
