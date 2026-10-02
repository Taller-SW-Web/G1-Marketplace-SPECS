# Spec UI — F-016 Agregar ítem al carrito

| Campo | Valor |
|---|---|
| ID | `F-016` |
| Sistema de diseño | `DS-001` v`0.1.0` |
| Ruta | `/productos/{slug}` |

El botón primario “Agregar al carrito” aparece después de F-013/F-014. Está deshabilitado con explicación si falta seleccionar variante o el SKU está agotado; no se deshabilita por fallo de consulta, sino que muestra “Reintentar disponibilidad”.

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
