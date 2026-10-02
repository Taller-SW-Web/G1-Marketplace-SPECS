# Spec de contrato API — F-004 Recuperación

`POST /api/v1/password/recuperar` con `correo`; `202` uniforme, `429 DEMASIADAS_SOLICITUDES`. No se almacena token ni correo de recuperación localmente.

- [ ] **API-CA-F004-01:** El resultado público no varía por existencia de cuenta.
