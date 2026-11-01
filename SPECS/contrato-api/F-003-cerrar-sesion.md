# Spec de contrato API — F-003 Logout

`POST /api/v1/auth/logout` desde el mismo origen, sin tokens en body. El BFF invalida la sesión compartida y borra cookies de sesión/desafío. Intenta `POST /auth/logout` de G7 con el refresh del servidor. Es idempotente.

`200 {authenticated:false,remoteRevocationPending:boolean}`: la sesión local está cerrada; si G7 falla, la UI comunica que no pudo confirmar revocación remota. No se afirma revocación inmediata de JWT emitidos. Si no puede invalidar la sesión persistida, devuelve `503` y permite reintentar; no anuncia cierre confirmado. No se registra el refresh ni se copia al navegador.

La UI limpia el estado privado de favoritos y vuelve al inicio. Durante checkout solicita confirmación de salida. Recargar y usar otra pestaña deben comprobar la sesión; cambiar usuario invalida cachés.

- [ ] Repetir logout es seguro.
- [ ] Timeout G7 no conserva sesión local y se informa con precisión.
- [ ] Usuario B nunca recibe datos cacheados de A.
- [ ] Prueba REAL y despliegue con revisión de Andrés pendientes.
