# Propuesta H4 — sesión temporal del BFF

Fecha: 21/10/2026. Responsable Jim Segovia; revisión Andrés Morales pendiente. Complemento propuesto de F-002/F-003 en [SPECS #9](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/9). Implementado para prueba local en [BE #229](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/229); sin aprobación ni despliegue inferidos. La línea base SQL de seis tablas permanece identificada como tal.

## Alcance de la excepción propuesta

G7 mantiene cuentas, contraseñas, roles, MFA y recuperación como autoridad. El BFF guarda un contenedor temporal cifrado de sesión/desafío para que el navegador utilice sólo una cookie opaca. No añade una tabla de clientes ni réplicas maestras. Se propone sustituir la exclusión absoluta de sesiones/tokens del modelo inicial por esta excepción limitada, sujeta a aprobación arquitectónica.

El contenedor incluye los tokens necesarios de G7 y la proyección mínima de usuario que ya contiene la sesión; todo dentro del cifrado. Contraseñas y tokens/enlaces de recuperación no se persisten en G1. No se crean FK hacia G7.

## Tabla propuesta `auth_sessions`

Fuente física: [migración BE 20261021000100_auth_sessions](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/068fbf9cec95304a405b5af0921cd8b24e4079d9/prisma/migrations/20261021000100_auth_sessions/migration.sql) y `AuthSession` Prisma de esa revisión.

| Columna | Tipo | Regla / contenido |
|---|---|---|
| `id` | `char(64)` PK | SHA-256 de identificador aleatorio de 32 bytes; cookie original no se guarda |
| `encrypted` | `text NOT NULL` | AES-256-GCM: nonce aleatorio de 12 bytes, tag de 16 y ciphertext, codificados base64; AAD vinculado al id |
| `expires_at` | `timestamptz(6) NOT NULL` | TTL absoluto: sesión máximo siete días desde login; desafío máximo cinco minutos |
| `created_at` | `timestamptz(6) NOT NULL DEFAULT CURRENT_TIMESTAMP` | Auditoría temporal mínima, sin identidad en claro |

Índice `auth_sessions_expiry_idx(expires_at)`. No FK a carrito/cliente/proveedor. La clave AES tiene 32 bytes y se custodia fuera de DB y del frontend; no forma parte del esquema ni de la evidencia. Cambiarla invalida contenedores existentes.

## Concurrencia y revocación

Bloqueo de fila para cambios; antes de llamar al refresh de un uso se confirma un marcador `refreshing` cifrado. Otra instancia espera; un marcador vencido por caída o una respuesta incierta invalida sesión y no reproduce el token. Un logout concurrente no puede resucitar la fila al terminar refresh.

Logout elimina la sesión local antes de pedir revocación G7. `200 authenticated:false` confirma cierre local; un fallo G7 se comunica con `remoteRevocationPending`. Fallo al invalidar DB devuelve error y no confirma cierre. No se promete revocación inmediata de JWT ya emitidos por terceros.

## Operación y evidencia

Purgar filas vencidas con mantenimiento acordado; una fila vencida no autoriza aunque todavía no se haya eliminado. Definir custodia/rotación de clave, permisos mínimos, respaldo cifrado y retención de backups con revisión de arquitectura/operación. No registrar cookies, payload descifrado, cuerpos de login ni tokens.

Pruebas PostgreSQL desechable: cifrado manipulado, expiración, rotación concurrente, caída/timeout sin replay, logout y separación A/B. [Evidencia BE](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s2-f002-f003-g7/docs/evidencias/H4/jim-segovia/F001-F005-cuenta.md). El uso de `db push` local valida el esquema actual, no la cadena de despliegue: G-DB sigue abierto por el índice duplicado de la migración heredada. Aplicar esta migración requiere revisión y resolución previa de ese gate; no reparar una base compartida a ciegas.

## Pendientes de aprobación

- Decisión arquitectónica de esta excepción de almacenamiento y política operativa de claves/TTL/purga/backups.
- Despliegue G1/G7, cuentas A/B y prueba REAL web/API.
- Semántica observada de revocación entre dispositivos después de reset; G7 no devuelve UUID en `204` y G1 no lo infiere del cliente.
- Revisión independiente; el contenedor temporal no libera G-AUTH ni certifica seguridad completa.
