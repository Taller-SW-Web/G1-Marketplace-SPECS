# Spec UI — F-005 Restablecimiento

El correo de G7 abre `/restablecer-contrasena?token=...` **en la SPA G7**, que presenta contraseña nueva, confirmación, reglas y errores. El token no se muestra ni persiste en G1. El éxito ofrece el login de Marketplace mediante destino fijo permitido por G7, sin sesión implícita; enlace vencido permite solicitar recuperación G7. El retorno aún requiere implementación y prueba real según la [decisión del PO](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

- [ ] **UI-F005-01:** Diferencia política incumplida de enlace vencido sin exponer secreto.
- [ ] **UI-F005-02:** El retorno G7 → login G1 funciona en navegador sin incorporar token ni credenciales al destino.
