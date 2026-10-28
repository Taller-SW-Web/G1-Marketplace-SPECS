# Spec de contrato API — F-004 Recuperación

**Alcance web vigente (decisión PO 26/10):** el formulario del navegador pertenece a G7. Este contrato conserva el adaptador BFF G1 ya implementado para integración y pruebas API; no define la ruta visual elegida. Véase [alcance Marketplace ↔ Seguridad](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

`POST /api/v1/password/recuperar` con `correo`; `202` uniforme, `429 DEMASIADAS_SOLICITUDES`. El BFF acepta sólo el `202` contratado, sin consulta previa de cuentas. Next proyecta `{accepted:true}` uniforme al navegador. No se almacena token ni correo de recuperación localmente.

Si G7 devuelve `Retry-After` en segundos, G1 conserva un valor entero acotado en `retryAfterSeconds`; el proxy web también publica la cabecera. La UI conserva el correo y bloquea el botón durante ese intervalo, sin reintento automático. Si no hay intervalo válido, informa espera y permite reintento manual sin inventar duración.

`G7_RECOVERY_ENABLED=false` es el valor por defecto del adaptador G1. En el corte real del 26/10/2026 la capacidad pública G1 respondió `recuperacion:true` y una solicitud API web G1 devolvió `202` con correo recibido. Esto acredita ese caso de integración, sin probar por sí solo la entrada desde G1 a la SPA G7, el retorno ni todos los negativos. No inferir la configuración de otro despliegue a partir de ese corte.

- [ ] **API-CA-F004-01:** El resultado público no varía por existencia de cuenta.
