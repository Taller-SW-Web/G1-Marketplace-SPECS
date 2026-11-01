# Spec de contrato API — F-004 Recuperación

`POST /api/v1/password/recuperar` con `correo`; `202` uniforme, `429 DEMASIADAS_SOLICITUDES`. El BFF acepta sólo el `202` contratado, sin consulta previa de cuentas. Next proyecta `{accepted:true}` uniforme al navegador. No se almacena token ni correo de recuperación localmente.

Si G7 devuelve `Retry-After` en segundos, G1 conserva un valor entero acotado en `retryAfterSeconds`; el proxy web también publica la cabecera. La UI conserva el correo y bloquea el botón durante ese intervalo, sin reintento automático. Si no hay intervalo válido, informa espera y permite reintento manual sin inventar duración.

H4: `G7_RECOVERY_ENABLED=false` por defecto. El contrato publicado permite avanzar con dobles; no se declara envío de correo REAL hasta publicación y prueba conjunta del bloque G7.

- [ ] **API-CA-F004-01:** El resultado público no varía por existencia de cuenta.
