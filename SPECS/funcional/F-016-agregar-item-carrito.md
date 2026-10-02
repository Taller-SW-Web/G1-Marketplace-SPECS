# Spec funcional — F-016 Agregar ítem al carrito

| Campo | Valor |
|---|---|
| ID | `F-016` |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración de catálogo/stock condicionada por `I-01`. |

Permite a un visitante o cliente agregar un SKU vendible al carrito activo. Incluye crear o recuperar el carrito, agregar una unidad o sumar sobre una línea existente y refrescar su snapshot informativo. Excluye reserva, pago, cupón y favoritos.

- **RN-F016-01:** La línea se identifica por `cartId + sku`; nunca por `variantId`.
- **RN-F016-02:** Antes de persistir, Marketplace confirma que el SKU es comercialmente elegible y con disponibilidad distinta de agotado. No reserva inventario.
- **RN-F016-03:** Si el SKU ya existe, incrementa su cantidad de forma atómica; si supera el máximo disponible confirmado, conserva el máximo y comunica el ajuste.
- **RN-F016-04:** El carrito puede ser anónimo mediante cookie segura o autenticado; sólo una identidad es dueña del carrito activo.
- **RN-F016-05:** Precio es snapshot informativo y se revalida después; no garantiza checkout.

Flujo: usuario elige variante si aplica, F-014 confirma disponibilidad, pulsa “Agregar al carrito”, BFF valida SKU/precio/stock, crea o actualiza `CartItem` y devuelve carrito actualizado. Fallos: SKU inactivo/no disponible, stock insuficiente, conflicto concurrente o proveedor no disponible; ninguno crea una línea parcial.

- [ ] **CA-F016-01:** Agregar un SKU nuevo crea una única línea con cantidad uno.
- [ ] **CA-F016-02:** Repetir el mismo SKU no duplica la línea; incrementa cantidad conforme al límite confirmado.
- [ ] **CA-F016-03:** Agregar no descuenta ni reserva stock.
- [ ] **CA-F016-04:** El error externo deja el carrito local sin mutación.

Fuentes: modelo lógico, F-012–F-014 y contratos Productos y Ofertas. Pendiente `I-01` para consulta final de SKU, precio y disponibilidad.
