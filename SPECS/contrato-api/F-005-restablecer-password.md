# Spec de contrato API — F-005 Restablecimiento

`POST /api/v1/password/restablecer` con `token`,`nuevaContrasena`; `204`, `401 TOKEN_RECUPERACION_INVALIDO`, `410 TOKEN_RECUPERACION_EXPIRADO`, `422 POLITICA_INCUMPLIDA`. El token transita en el body navegador → Next → BFF → G7; no se persiste en G1 ni aparece en respuestas/logs. Confirmación y UUID nunca se envían a G7. No hay endpoint inventado de validación previa del enlace.

La UI captura el token una vez en memoria y elimina la query y el estado de esa entrada de historial; usa `Referrer-Policy: no-referrer` y no restaura el secreto al recargar. Next omite esa ruta en sus logs de desarrollo. El entorno de hosting también debe omitir/redactar la query del enlace en sus propios logs: esta configuración no se infiere del código local.

Éxito `204` limpia token y contraseñas y ofrece login; no autentica. Si el navegador tenía sesión, intenta el logout protegido y comunica por separado un fallo de ese cierre. G7 es dueño de consumir el token y revocar las sesiones del usuario afectado; su respuesta `204` no incluye UUID y G1 no lo infiere de un dato del cliente. La invalidación observada de access JWT ya emitidos en otros dispositivos debe homologarse con G7; no se promete revocación inmediata por ver un `204` simulado.

El bloque continúa apagado por defecto (`G7_RECOVERY_ENABLED=false`) hasta publicación y prueba de G7. `401/410` eliminan el formulario y ofrecen otro enlace; `422` permite corregir. Un fallo incierto no provoca reenvío automático.

La propuesta de [introspección del BFF](F-002-iniciar-sesion.md#consulta-de-revocación--propuesta-h4-desactivada) permite consultar la vigencia del `jti`/familia mediante G7, sin conocer el UUID desde el reset ni borrar sesiones de otro usuario por un campo del cliente. Está desactivada hasta confirmar cliente/scope/entorno. Las pruebas con proveedor simulado no demuestran que reset G7 esté publicado ni que revoque realmente todas las familias: ese caso sigue pendiente de homologación.

- [ ] **API-CA-F005-01:** Respuesta exitosa no entrega sesión ni token.
