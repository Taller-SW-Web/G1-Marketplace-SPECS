# Spec de contrato API — F-001 Registro

`POST /api/v1/auth/registro`: `correo`, `contrasena`, `nombres`, `apellidos`, `celular`, `aceptaTerminos:true`, `canalOrigen:"MARKETPLACE"`. `201` devuelve `id` y `estado:PENDIENTE_VERIFICACION`; `400 VALIDACION` informa datos inválidos; `409 CORREO_NO_DISPONIBLE` usa un mensaje neutro; `422 POLITICA_INCUMPLIDA` marca reglas. Marketplace nunca persiste la contraseña.

Según el acuerdo A1 de Seguridad, el correo lleva a su pantalla de verificación. Seguridad configura por ambiente el destino posterior a la verificación exitosa: el `/login` de Marketplace. El registro no acepta una URL de retorno; Marketplace no consume `POST /api/v1/auth/verificar-correo`, no procesa el token del enlace y no asume que la respuesta `201` inicia sesión.

Confirmación del PO de Seguridad del 2026-10-02: Seguridad resuelve los enlaces vencidos o ya usados y ofrece reenvío; el enlace reenviado conserva el `canalOrigen` original. En “enlace ya usado”, la acción “Iniciar sesión” va al `/login` de Marketplace. La redirección usa sólo la URL configurada por Seguridad y nunca transporta el token de verificación. Marketplace no implementa el reenvío ni añade parámetros de retorno al registro.

Fuentes externas consultadas: [SPEC-02, RF-02.8](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/blob/15796e0/specs/SPEC-02-verificacion-correo.md) y [OpenAPI de Seguridad](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/blob/15796e0/specs/openapi.yaml), versión de `main` revisada el 2026-10-02. Los detalles del reenvío, el botón del enlace ya usado y la ausencia del token en la redirección proceden de la confirmación posterior del PO de Seguridad; aún no aparecen explícitos en esas fuentes enlazadas.

- [ ] **API-CA-F001-01:** Canal siempre es `MARKETPLACE`.
- [ ] **API-CA-F001-02:** La petición no incluye URL de destino y la respuesta de registro conserva `PENDIENTE_VERIFICACION`.
- [ ] **API-CA-F001-03:** En cualquier retorno de Seguridad a Marketplace, la URL configurada apunta a `/login` y no contiene el token; el reenvío mantiene el canal original.
