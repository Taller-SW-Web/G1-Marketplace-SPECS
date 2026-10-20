# Spec UI — F-016 Agregar ítem al carrito

| Campo | Valor |
|---|---|
| ID | `F-016` |
| Sistema de diseño vigente | `DS-001` v`0.2.0`; aplicación visual pendiente de revisión |
| Ruta | `/productos/{slug}` |

El botón primario “Agregar al carrito” aparece después de F-013/F-014. Sólo agrega con SKU/precio válidos y estado AVAILABLE o STOCK_LOW. Sin selección, agotado, UNDETERMINED, carga o fallo técnico no ejecuta alta; explicar la causa. Error conserva la acción “Reintentar disponibilidad” e indeterminado ofrece “Volver a consultar”, ambas sin mutación del carrito.

| Estado | Interfaz |
|---|---|
| Listo | Botón activo, texto “Agregar al carrito”. |
| Enviando | Botón ocupado y no repetible; conserva texto accesible. |
| Éxito | Toast no intrusivo con cantidad y acciones “Ver carrito” / “Seguir comprando”. |
| Ajustado | Aviso: “Ajustamos la cantidad disponible en tu carrito”. |
| Error | Mensaje claro junto al botón y acción de reintento. |

Teclado activa el botón con Enter/Espacio; cambios se anuncian en `aria-live`; en móvil el botón puede ser fijo si no oculta información ni controles. No muestra totales de checkout.

- [ ] **UI-F016-01:** No se puede ejecutar doble adición por pulsaciones repetidas.
- [ ] **UI-F016-02:** Éxito, ajuste y error son distinguibles sin depender sólo del color.
