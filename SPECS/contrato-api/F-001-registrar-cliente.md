# Spec de contrato API — F-001 Registro

`POST /api/v1/auth/registro`: `correo`, `contrasena`, `nombres`, `apellidos`, `celular`, `aceptaTerminos:true`, `canalOrigen:"MARKETPLACE"`. `201/202` confirma proceso; `409 CORREO_NO_DISPONIBLE` es neutro; `422 POLITICA_INCUMPLIDA` marca reglas. Nunca se registra contraseña.

- [ ] **API-CA-F001-01:** Canal siempre es `MARKETPLACE`.
