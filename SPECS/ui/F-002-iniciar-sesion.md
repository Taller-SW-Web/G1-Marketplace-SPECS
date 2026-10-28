# Spec UI — F-002 Login

Ruta `/login`: correo, contraseña, recuperación, CTA y MFA sólo al recibir desafío. CTA no repetible; éxito vuelve a ruta protegida/inicio; error genérico accesible.

La acción de recuperación abre la SPA G7 mediante destino confiable según la [decisión PO F-004/F-005](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md); no presenta el formulario G1 anterior como recorrido objetivo.

- [ ] **UI-F002-01:** MFA no se muestra sin desafío válido.
