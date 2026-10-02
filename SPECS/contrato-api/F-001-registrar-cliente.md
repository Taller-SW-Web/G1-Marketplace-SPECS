# Spec de contrato API — F-001 Registro

`POST /api/v1/auth/registro`: `correo`, `contrasena`, `nombres`, `apellidos`, `celular`, `aceptaTerminos:true`, `canalOrigen:"MARKETPLACE"`. `201` devuelve `id` y `estado:PENDIENTE_VERIFICACION`; `400 VALIDACION` informa datos inválidos; `409 CORREO_NO_DISPONIBLE` usa un mensaje neutro; `422 POLITICA_INCUMPLIDA` marca reglas. Marketplace nunca persiste la contraseña.

Según el acuerdo A1 de Seguridad, el correo lleva a su pantalla de verificación. Seguridad configura por ambiente el destino posterior a la verificación exitosa: el `/login` de Marketplace. El registro no acepta una URL de retorno; Marketplace no consume `POST /api/v1/auth/verificar-correo`, no procesa el token del enlace y no asume que la respuesta `201` inicia sesión.

Fuentes externas consultadas: [SPEC-02, RF-02.8](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/blob/15796e0/specs/SPEC-02-verificacion-correo.md) y [OpenAPI de Seguridad](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/blob/15796e0/specs/openapi.yaml), versión de `main` revisada el 2026-10-02. Queda por confirmar con Seguridad que la redirección final no incluya el token de verificación ni datos sensibles.

- [ ] **API-CA-F001-01:** Canal siempre es `MARKETPLACE`.
- [ ] **API-CA-F001-02:** La petición no incluye URL de destino y la respuesta de registro conserva `PENDIENTE_VERIFICACION`.
