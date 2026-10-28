# Spec funcional — F-005 Restablecer contraseña

| ID | Estado |
|---|---|
| `F-005` | Aprobada para planificación; Seguridad es dueño. |

La SPA de G7 fija la contraseña nueva usando el token de un solo uso del enlace. G1 verifica el retorno al login de Marketplace conforme a la [decisión del PO para F-004/F-005](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md). Incluye política vigente y confirmación; excluye conservar token en G1 o iniciar sesión automáticamente.

- Token inválido/vencido/ya usado no revela cuenta y requiere solicitar nuevo enlace.
- Éxito revoca sesiones anteriores según Seguridad.

- [ ] **CA-F005-01:** Token usado no puede modificar contraseña de nuevo.
- [ ] **CA-F005-02:** Tras el resultado G7, el canal Marketplace vuelve al login G1 mediante destino fijo permitido, sin sesión implícita ni redirección arbitraria.
