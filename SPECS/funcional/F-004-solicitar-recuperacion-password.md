# Spec funcional — F-004 Solicitar recuperación de contraseña

| ID | Estado |
|---|---|
| `F-004` | Aprobada para planificación; Seguridad es dueño. |

Solicita enlace de recuperación por correo. Incluye validar formato y respuesta uniforme; excluye confirmar existencia de cuenta o modificar contraseña.

- Seguridad responde `202` exista o no correo con latencia equivalente.
- Límite de solicitudes muestra espera neutral.

- [ ] **CA-F004-01:** Correo inexistente recibe misma confirmación pública.
