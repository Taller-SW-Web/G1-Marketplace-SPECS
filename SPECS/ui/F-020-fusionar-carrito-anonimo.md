# Spec UI — F-020 Fusionar carrito anónimo al iniciar sesión

Tras inicio de sesión, la fusión es automática y no bloquea la pantalla más de lo necesario. Se muestra mensaje `aria-live`: “Actualizamos tu carrito” y, si aplica, un resumen de SKU/cantidad ajustados. No se solicitan decisiones para resolver duplicados: la regla de suma y máximo es determinista.

Si falla, sesión permanece iniciada y se comunica “No pudimos actualizar tu carrito. Reintentar”; no se afirma que productos se perdieron. En `/carrito`, los cambios se resaltan una vez sin depender sólo de color.

- [ ] **UI-F020-01:** No existe doble carrito visible tras inicio de sesión.
- [ ] **UI-F020-02:** Los ajustes explican la causa sin revelar inventario interno.
