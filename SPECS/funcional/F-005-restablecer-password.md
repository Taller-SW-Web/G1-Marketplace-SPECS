# Spec funcional — F-005 Restablecer contraseña

| ID | Estado |
|---|---|
| `F-005` | Aprobada para planificación; Seguridad es dueño. |

Fija contraseña nueva usando token de un solo uso del enlace. Incluye política vigente y confirmación; excluye conservar token o iniciar sesión automáticamente.

- Token inválido/vencido/ya usado no revela cuenta y requiere solicitar nuevo enlace.
- Éxito revoca sesiones anteriores según Seguridad.

- [ ] **CA-F005-01:** Token usado no puede modificar contraseña de nuevo.
