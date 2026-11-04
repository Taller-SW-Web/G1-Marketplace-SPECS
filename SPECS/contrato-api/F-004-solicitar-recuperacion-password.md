# Spec de contrato API — F-004 Recuperación

**Alcance web vigente (decisión PO 26/10):** el formulario del navegador pertenece a G7. Este contrato conserva el adaptador BFF G1 ya implementado para integración y pruebas API; no define la ruta visual elegida. Véase [alcance Marketplace ↔ Seguridad](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

`POST /api/v1/password/recuperar` con `correo`; `202` uniforme, `429 DEMASIADAS_SOLICITUDES`. El BFF acepta sólo el `202` contratado, sin consulta previa de cuentas. Next proyecta `{accepted:true}` uniforme al navegador. No se almacena token ni correo de recuperación localmente.

**Alineación API informada el 01/11:** el backend G7 desplegado en `2c8fe58039f94ae871efd3781c126335f670667a` acepta `canalOrigen` en la solicitud de recuperación y usa `WEB` si falta. El navegador G1 sigue enviando sólo `correo` al BFF; el BFF debe fijar `canalOrigen: MARKETPLACE` en su cuerpo servidor → G7 y rechazar cualquier canal o URL de retorno suministrado por el navegador ([BE PR #252](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/252), abierta). Este campo de la API BFF → G7 **no** es un parámetro en la URL de entrada G1 FE → SPA G7 ni define el mecanismo de retorno de la SPA. La prueba conjunta del canal y el SHA frontend G7 desplegado siguen pendientes.

Si G7 devuelve `Retry-After` en segundos, G1 conserva un valor entero acotado en `retryAfterSeconds`; el proxy web también publica la cabecera. La UI conserva el correo y bloquea el botón durante ese intervalo, sin reintento automático. Si no hay intervalo válido, informa espera y permite reintento manual sin inventar duración.

`G7_RECOVERY_ENABLED=false` es el valor por defecto del adaptador G1. En el corte real del 26/10/2026 la capacidad pública G1 respondió `recuperacion:true` y una solicitud API web G1 devolvió `202` con correo recibido. Esto acredita ese caso de integración, sin probar por sí solo la entrada desde G1 a la SPA G7, el retorno ni todos los negativos. No inferir la configuración de otro despliegue a partir de ese corte.

- [ ] **API-CA-F004-01:** El resultado público no varía por existencia de cuenta.
