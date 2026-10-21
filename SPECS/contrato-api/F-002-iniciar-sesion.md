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

### Consulta de revocación — propuesta H4 desactivada

Fuente adicional: G7 backend develop `813b809`. El BFF prepara `G7_INTROSPECTION_ENABLED=false`, sujeto a revisión, cliente técnico propio y despliegue confirmado. Al activarlo, la validación criptográfica RS256/issuer/tipo/sub precede a la introspección del guard compartido; también se revalida la sesión pública en recarga/refresh. Los endpoints públicos de login/MFA/registro/recuperación y logout conservan sus reglas propias.

Sólo el BFF obtiene `POST /auth/token` por formulario `grant_type=client_credentials`, `client_id`, `client_secret`, `scope=tokens:introspeccion`. Credenciales `G7_SERVICE_CLIENT_ID`/`G7_SERVICE_CLIENT_SECRET` en gestor privado; audiencia/concesión G7 `api-seguridad` confirmadas antes de activar. Se valida `Bearer`, expiración acotada y scope de respuesta; el token técnico permanece en memoria del servidor hasta antes de vencer y su solicitud concurrente se comparte. No es una sesión de usuario ni se entrega al navegador. Rotar credenciales requiere reiniciar las instancias.

`POST /auth/introspeccion`, Bearer de servicio y JSON `{token:accessTokenDelTitular}`, exige `activo` booleano. Si activo, `sub` debe coincidir con el JWT ya verificado, `tipo=acceso`, roles/permisos tipados y `exp` vigente. No se almacenan decisiones activas entre requests. `activo:false` produce rechazo genérico `401`, sin reenviar el motivo de cuenta; la lectura de sesión elimina su contenedor/cookie revocados. JWT inválido se rechaza antes de pedir credenciales técnicas.

Fallo/timeout, scope insuficiente o respuesta incompatible producen `503`, sin fallback a autorización offline ni reintento de la misma solicitud. Un fallo transitorio al consultar una sesión todavía válida no confirma revocación ni elimina su refresh; la identidad no se devuelve y una lectura posterior puede recuperarse. Una respuesta incierta de refresh de usuario conserva su regla anterior de invalidación sin replay. Logout sigue disponible para invalidar localmente aun si G7 no responde. La disponibilidad/latencia y revocación efectiva tras reset deben probarse en el entorno conjunto antes de activar.

- [ ] Implementación y pruebas con proveedor simulado firmante.
- [ ] G7 REAL: cuentas A/B, entorno, revisión desplegada y pruebas positivas/negativas/timeout.
- [ ] Prueba web + API en despliegues G1 y revisión independiente.

Registro/verificación y recuperación/restablecimiento dependen de publicación de sus bloques G7. Este diseño no acredita disponibilidad ni cierre de INT.
