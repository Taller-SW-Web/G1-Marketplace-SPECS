# Spec funcional — F-001 Registrar cliente

| ID | Estado |
|---|---|
| `F-001` | Aprobada para planificación; Seguridad es dueño. |

Autorregistro de cliente desde Marketplace: correo, contraseña, nombres, apellidos, celular, términos y `canalOrigen=MARKETPLACE`. No crea cuenta/contraseña local ni inicia sesión automáticamente.

- Correo repetido recibe mensaje neutro para no enumerar cuentas.
- Contraseña sigue política publicada por Seguridad; validación final externa.
- Registro requiere verificación por correo antes de asumir cuenta activa.

- [ ] **CA-F001-01:** Datos válidos envían un único registro a Seguridad.
- [ ] **CA-F001-02:** Correo repetido no confirma existencia.
