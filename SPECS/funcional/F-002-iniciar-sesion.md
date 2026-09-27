# Spec funcional — F-002 Iniciar sesión

| ID | Estado |
|---|---|
| `F-002` | Aprobada para planificación; Seguridad es dueño. |

Autentica cliente y establece sesión Marketplace. Incluye correo/contraseña, MFA y fusión F-020; excluye validar contraseñas localmente o persistir refresh token como dato de dominio.

- Error de credenciales es genérico.
- MFA no inicia sesión hasta verificación.
- Éxito dispara F-020 si existe carrito anónimo.

- [ ] **CA-F002-01:** Inicio válido fusiona carrito cuando aplica.
- [ ] **CA-F002-02:** Error no distingue correo/contraseña.
