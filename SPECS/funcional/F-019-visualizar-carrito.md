# Spec funcional — F-019 Visualizar el carrito, totales y estado vacío

| Campo | Valor |
|---|---|
| ID | `F-019` |
| Estado | Aprobada para planificación; precio/disponibilidad condicionados por `I-01`. |

Muestra el carrito activo, sus líneas y subtotal informativo. Incluye estado vacío, detección de cambios de precio/stock y acceso a checkout; excluye cupón, envío, impuestos y total final.

- **RN-F019-01:** El carrito local es fuente de cantidades; nombre, imagen, precio y disponibilidad se refrescan desde los dueños externos.
- **RN-F019-02:** Subtotal es suma de `cantidad × snapshot vigente`; no equivale a total de pedido.
- **RN-F019-03:** Línea sin precio o agotada permanece visible con estado de atención y bloquea avanzar a checkout hasta corregirse.
- **RN-F019-04:** Carrito sin líneas sigue activo y muestra una invitación a explorar catálogo.

Flujo: abrir `/carrito`, identificar sesión/JWT, leer `Cart` y enriquecer líneas; mostrar subtotal y mensajes de variación. Error de enriquecimiento no borra líneas: muestra última información segura marcada como pendiente o permite reintentar.

- [ ] **CA-F019-01:** Carrito vacío no muestra subtotal ni acciones de checkout activas.
- [ ] **CA-F019-02:** Una variación de precio se comunica antes de checkout.
- [ ] **CA-F019-03:** Mostrar carrito no reserva ni consume stock.
