# Spec de contrato API — F-003 Logout

`POST /api/v1/auth/logout` con refresh token protegido; `204` tanto para revocación efectiva como token ya inválido. Cliente limpia sesión. No body ni log de secreto.

- [ ] **API-CA-F003-01:** Repetir logout es seguro.
