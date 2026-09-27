# Spec UI — F-021 Mover un ítem del carrito a favoritos

Cada `CartLine` ofrece enlace/botón “Mover a favoritos” sólo con sesión. Sin sesión, abre inicio de sesión con retorno a `/carrito`, sin ejecutar mutación. Éxito retira la línea y anuncia “Guardado en favoritos”; si ya existía, “Ya estaba en favoritos”. Error conserva línea y muestra reintento.

- [ ] **UI-F021-01:** Acción y resultado son accesibles por teclado y lector de pantalla.
- [ ] **UI-F021-02:** La interfaz no indica éxito hasta confirmar ambas mutaciones locales.
