# Spec UI — F-001 Registro

Ruta `/registro`: nombre, apellido, correo, celular, contraseña, confirmación y términos. Medidor usa política actual; mensajes no revelan correo existente. La solicitud aceptada indica que el enlace del correo abre la pantalla de Seguridad y que, tras verificar correctamente, el usuario regresará al `/login` de Marketplace para iniciar sesión. No hay pantalla de verificación de correo propia del Marketplace ni sesión automática.

- [ ] **UI-F001-01:** Password tiene etiquetas, ayuda y mostrar/ocultar accesible.
- [ ] **UI-F001-02:** El mensaje posterior al registro distingue solicitud aceptada de cuenta verificada y no invita a iniciar sesión como si la cuenta ya estuviera activa.
