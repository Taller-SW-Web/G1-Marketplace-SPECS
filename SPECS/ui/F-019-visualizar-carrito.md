# Spec UI — F-019 Visualizar el carrito, totales y estado vacío

Ruta `/carrito`, patrón `CartLine` y `OrderSummary` de DS-001.

```text
Carrito
├── Lista de CartLine (imagen, nombre, variante, precio, cantidad, quitar/mover)
├── Mensajes de cambios o no disponibilidad
└── Resumen: subtotal informativo + Iniciar checkout
```

| Estado | Interfaz |
|---|---|
| Cargando | Skeleton de líneas y resumen. |
| Con líneas válidas | Lista, subtotal y acción checkout. |
| Atención | Línea marcada, explicación y checkout deshabilitado hasta corrección. |
| Vacío | Ilustración, “Tu carrito está vacío” y enlace a catálogo. |
| Error | Datos locales preservados, aviso y Reintentar. |

El subtotal incluye etiqueta “No incluye envío ni descuentos”. La lista es semántica; cada línea tiene encabezado y controles accesibles. En móvil, resumen queda después de líneas y no fija un CTA que oculte controles.

- [ ] **UI-F019-01:** Estado vacío ofrece una única salida clara sin contenedor de resumen vacío.
- [ ] **UI-F019-02:** Una línea no comprable se anuncia antes del botón checkout.
