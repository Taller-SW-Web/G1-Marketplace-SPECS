# Spec de contrato API — F-002 Login

`POST /api/v1/auth/login` con `correo`,`contrasena`. `200` entrega token/sesión; MFA entrega desafío; `401 CREDENCIALES_INVALIDAS`, `403 PASSWORD_CADUCADA`, `429`. Tokens no se guardan en base Marketplace ni logs.

- [ ] **API-CA-F002-01:** Error mantiene formato neutro.
