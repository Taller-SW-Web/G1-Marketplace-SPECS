# Spec funcional — F-004 Solicitar recuperación de contraseña

| ID | Estado |
|---|---|
| `F-004` | Aprobada para planificación; Seguridad es dueño. |

Desde Marketplace se inicia el recorrido en la SPA de G7, conforme a la [decisión del PO para F-004/F-005](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md). Seguridad solicita el enlace por correo; G1 mantiene la entrada y comprueba la integración/retorno. Incluye validar formato y respuesta uniforme; excluye confirmar existencia de cuenta o modificar contraseña.

- Seguridad responde `202` exista o no correo con latencia equivalente.
- Límite de solicitudes muestra espera neutral.

- [ ] **CA-F004-01:** Correo inexistente recibe misma confirmación pública.
- [ ] **CA-F004-02:** La entrada desde login G1 abre recuperación G7 mediante destino confiable; el correo abre el restablecimiento G7 y ninguna URL de recuperación con token entra en G1.
