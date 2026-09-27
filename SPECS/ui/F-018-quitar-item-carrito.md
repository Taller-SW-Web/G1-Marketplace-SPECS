# Spec UI — F-018 Quitar un ítem del carrito

Cada línea de `/carrito` tiene botón “Quitar {producto}”. Al activarlo se elimina optimistamente sólo tras conservar opción “Deshacer” durante 5 segundos; si el servidor rechaza, la línea se restaura y se anuncia el error.

No se usa confirmación modal para una única línea, salvo que el carrito incluya datos no guardados futuros. Si queda vacío, F-019 presenta su estado vacío. Botón accesible, foco tras quitar pasa a la siguiente línea o al título del carrito.

- [ ] **UI-F018-01:** Eliminar es reversible durante la ventana visual sin crear una segunda línea.
- [ ] **UI-F018-02:** El foco nunca queda en un elemento retirado del DOM.
