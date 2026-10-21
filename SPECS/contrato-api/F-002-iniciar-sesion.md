# Spec de contrato API — F-002 Login

## Transporte H4 — propuesta implementada para revisión

Fuente: respuesta G1 a G7 del 20/10 y contrato G7 v1.1.0, revisión documental `1b034d2b1db0a19bb5c12c1c5426c797f47864b5`. Responsable Jim; revisor Andrés. Contacto técnico G7: David Morales Brenis; contrato y scopes: Sergio.

El navegador consume el proxy de Next en el mismo origen. El BFF consume G7 v1. Los access/refresh/challenge tokens no se entregan al navegador ni se registran en logs. No se usan localStorage ni sessionStorage para credenciales. La cookie `__Host-g1_session` es opaca, HttpOnly, Secure, SameSite=Lax, Path=/, sin Domain. Sólo desarrollo local permite `g1_session` sin Secure.

Se sustituye la prohibición anterior de toda persistencia: el BFF conserva exclusivamente una sesión temporal compartida en PostgreSQL con identificador hasheado, tokens G7 cifrados con AES-256-GCM y vencimiento. No crea cuentas ni contraseñas locales. La clave de cifrado es un secreto externo a la base. El refresh se serializa con bloqueo de fila y un marcador confirmado antes de llamar a G7; un reinicio no permite repetir el token anterior. Ante respuesta incierta se invalida la sesión sin reintentar el refresh de un solo uso. La sesión dura como máximo siete días desde el login; renovar no extiende ese límite. Purgar filas vencidas forma parte de operación.

## Endpoints G1

- `POST /api/v1/auth/login`, JSON `{correo,contrasena}`: `200` con sesión pública o `{mfaRequerido:true,canal:"EMAIL",expiraEn}` y cookie de desafío opaco. No hay sesión autenticada antes de verificar OTP.
- `POST /api/v1/auth/otp/solicitar`, sin datos de identidad: usa el desafío del servidor y pide EMAIL a G7. Devuelve destino enmascarado y tiempos. Reenvío no prolonga el desafío.
- `POST /api/v1/auth/otp/verificar`, JSON `{codigo}`: verifica con G7 y establece una sesión nueva, invalidando el desafío.
- `GET /api/v1/auth/session`: proyección pública `{authenticated,user?,scope}`; nunca tokens. Puede renovar el access token dentro del límite de sesión.
- `POST /api/v1/auth/refresh`: sin refresh token en body; usa el servidor y devuelve sesión pública.

Login: `401 CREDENCIALES_INVALIDAS` neutro; `403 PASSWORD_CADUCADA`; `429 RATE_LIMITED`. MFA conserva códigos homologados sin reenviar mensajes arbitrarios. Fallo de proveedor/configuración: `503 AUTH_UNAVAILABLE`. Mutaciones con cookie requieren Origin exacto configurado. El proxy rechaza origen externo y parámetros no esperados. Retorno tras login: sólo rutas locales permitidas, sin URLs externas ni rutas auth/API.

Favoritos demuestra autenticación y separación por UUID central G7. La API directa con Bearer continúa disponible; el cliente no elige el UUID dueño. Credenciales de servicio de Productos son independientes y permanecen en BFF.

## Evidencia y gates

- [ ] Implementación y pruebas con proveedor simulado firmante.
- [ ] G7 REAL: cuentas A/B, entorno, revisión desplegada y pruebas positivas/negativas/timeout.
- [ ] Prueba web + API en despliegues G1 y revisión independiente.

Registro/verificación y recuperación/restablecimiento dependen de publicación de sus bloques G7. Este diseño no acredita disponibilidad ni cierre de INT.
