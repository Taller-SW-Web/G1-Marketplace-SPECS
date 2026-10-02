# Spec funcional — F-001 Registrar cliente

| ID | Estado |
|---|---|
| `F-001` | Aprobada para planificación; Seguridad es dueño. |

Autorregistro de cliente desde Marketplace: correo, contraseña, nombres, apellidos, celular, términos y `canalOrigen=MARKETPLACE`. No crea cuenta/contraseña local ni inicia sesión automáticamente.

- Correo repetido recibe mensaje neutro para no enumerar cuentas.
- Contraseña sigue política publicada por Seguridad; validación final externa.
- La respuesta de registro deja la cuenta en `PENDIENTE_VERIFICACION`; no se asume activa ni se inicia sesión.
- El enlace del correo abre la pantalla de verificación de Seguridad. Tras verificar correctamente, Seguridad redirige a la ruta `/login` de Marketplace configurada en su servicio; los enlaces vencidos o ya usados se atienden en Seguridad.
- Si el enlace vence, Seguridad ofrece solicitar uno nuevo y conserva el `canalOrigen=MARKETPLACE` del registro. Si el enlace ya fue usado, su acción “Iniciar sesión” dirige al `/login` de Marketplace. Ninguna de esas pantallas pertenece a Marketplace.
- Marketplace no envía una URL de destino en el registro, no recibe ni procesa el token de verificación y no ofrece una segunda pantalla de verificación de correo.

- [ ] **CA-F001-01:** Datos válidos envían un único registro a Seguridad.
- [ ] **CA-F001-02:** Correo repetido no confirma existencia.
- [ ] **CA-F001-03:** El registro usa `canalOrigen=MARKETPLACE` y no incluye una URL de retorno enviada por el cliente.
- [ ] **CA-F001-04:** La confirmación explica que el usuario debe verificar su correo antes de iniciar sesión; Marketplace no interpreta el enlace de verificación.
- [ ] **CA-F001-05:** El reenvío gestionado por Seguridad conserva el canal `MARKETPLACE`; los retornos hacia `/login` usan la URL configurada y no contienen el token de verificación.
