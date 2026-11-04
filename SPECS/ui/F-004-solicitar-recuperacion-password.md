# Spec UI — F-004 Recuperación

En el canal Marketplace, el acceso «¿Olvidaste tu contraseña?» del login conduce a `/recuperar-contrasena` de la SPA G7 mediante destino confiable. Allí G7 presenta correo, CTA, confirmación neutral y espera/reintento por límite. La ruta homónima de G1, si se conserva por compatibilidad, no presenta un formulario alternativo ni recibe tokens. Véase la [decisión del PO](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

- [ ] **UI-F004-01:** No confirma cuenta registrada.
- [ ] **UI-F004-02:** Desde G1 se identifica con claridad la salida a G7 y se puede volver a Marketplace; el destino no procede de una URL arbitraria.
