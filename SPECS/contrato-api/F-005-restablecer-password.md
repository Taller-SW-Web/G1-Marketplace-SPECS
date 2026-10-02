# Spec de contrato API — F-005 Restablecimiento

`POST /api/v1/password/restablecer` con `token`,`nuevaContrasena`; `204`, `401 TOKEN_RECUPERACION_INVALIDO`, `410 TOKEN_RECUPERACION_EXPIRADO`, `422 POLITICA_INCUMPLIDA`. Token sólo viaja a Seguridad y se omite de logs.

- [ ] **API-CA-F005-01:** Respuesta exitosa no entrega sesión ni token.
