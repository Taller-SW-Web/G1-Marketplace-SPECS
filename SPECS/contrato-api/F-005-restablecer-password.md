# Spec de contrato API — F-005 Restablecimiento

**Alcance web vigente (decisión PO 26/10):** el enlace del correo y el formulario se procesan en la SPA G7. Este contrato conserva el adaptador BFF G1 para integración y pruebas API; el token del correo no debe entrar en rutas web G1 del recorrido elegido. Véase [alcance Marketplace ↔ Seguridad](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

`POST /api/v1/password/restablecer` con `token`,`nuevaContrasena`; `204`, `401 TOKEN_RECUPERACION_INVALIDO`, `410 TOKEN_RECUPERACION_EXPIRADO`, `422 POLITICA_INCUMPLIDA`. El token transita en el body navegador → Next → BFF → G7; no se persiste en G1 ni aparece en respuestas/logs. Confirmación y UUID nunca se envían a G7. No hay endpoint inventado de validación previa del enlace.

En la alternativa de formulario G1 implementada previamente, la UI capturaba el token en memoria y eliminaba query e historial. Esa alternativa deja de ser el recorrido web objetivo. G7 debe proteger el token en su SPA, historial, referrer y logs; G1 no debe aceptar el enlace con token como entrada del navegador. Si se mantiene la ruta G1 por compatibilidad, no debe registrar ni transmitir la query. La redacción de logs del hosting requiere comprobación propia y no se infiere del código local.

Éxito `204` del BFF no autentica. En el recorrido web elegido, G7 limpia los secretos de su formulario y ofrece volver al login G1 mediante destino fijo permitido; ese retorno aún no está probado. G7 es dueño de consumir el token y revocar las sesiones del usuario afectado; su respuesta `204` no incluye UUID y G1 no lo infiere de un dato del cliente. La invalidación observada de access JWT ya emitidos en otros dispositivos debe homologarse con G7; no se promete revocación inmediata por ver un `204` simulado.

El adaptador G1 permanece apagado por defecto (`G7_RECOVERY_ENABLED=false`), aunque el corte real del 26/10/2026 respondió `recuperacion:true` y permitió `204`, login nuevo `200`, anterior `401` y token usado `401`. No se probó token vencido ni retorno de navegador. G7 presenta los estados `401/410` y permite corregir `422` en su SPA; un fallo incierto no provoca reenvío automático.

La propuesta de [introspección del BFF](F-002-iniciar-sesion.md#consulta-de-revocación--propuesta-h4-desactivada) permite consultar la vigencia del `jti`/familia mediante G7, sin conocer el UUID desde el reset ni borrar sesiones de otro usuario por un campo del cliente. Está desactivada hasta confirmar cliente/scope/entorno. Las pruebas con proveedor simulado no demuestran que reset G7 esté publicado ni que revoque realmente todas las familias: ese caso sigue pendiente de homologación.

- [ ] **API-CA-F005-01:** Respuesta exitosa no entrega sesión ni token.
