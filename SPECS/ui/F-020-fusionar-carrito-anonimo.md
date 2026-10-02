# Spec UI — F-020 Fusionar carrito anónimo al iniciar sesión

Tras inicio de sesión, la fusión es automática y no bloquea la pantalla más de lo necesario. Se muestra mensaje `aria-live`: “Actualizamos tu carrito” y, si aplica, un resumen de SKU/cantidad ajustados. No se solicitan decisiones para resolver duplicados: la regla de suma y máximo es determinista.

Si falla, la sesión permanece iniciada y se comunica “No pudimos combinar tus carritos”. Se ofrecen **Reintentar** y **Continuar sin combinar**. La segunda acción permite seguir hacia el destino interno previsto o, si no existe, al inicio; no presenta los artículos anónimos como parte del carrito de la cuenta. Se explica que el carrito invitado no se combinó, sin afirmar que sus productos se perdieron. Al llegar a `/carrito`, se muestra sólo el carrito autenticado con un aviso de fusión pendiente y la opción de reintentar mientras el carrito anónimo siga disponible. Los cambios de una fusión exitosa se resaltan una vez sin depender sólo de color.

- [ ] **UI-F020-01:** No existe doble carrito visible tras inicio de sesión.
- [ ] **UI-F020-02:** Los ajustes explican la causa sin revelar inventario interno.
- [ ] **UI-F020-03:** El error ofrece ambas salidas; continuar no se interpreta visualmente como fusión exitosa ni deja al usuario atrapado en la pantalla de acceso.
