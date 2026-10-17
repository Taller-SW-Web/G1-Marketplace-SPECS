# Integración de develop — Giuliano — H3 — 17/10/2026

Por solicitud de Giuliano, se incorporan los avances publicados de develop en las tres ramas personales, conservando el historial. No se modifica main/develop ni se amplía el bloque propio más allá de F-006/F-007. Los incrementos de otros integrantes llegan desde la base compartida y conservan su ownership.

## Revisiones integradas

| Repositorio | Rama personal | HEAD previo | develop incorporado |
|---|---|---|---|
| Backend | `feat/s1-f006-f007-catalogo` | `962a259d67c08ad430ee64c0b5b24ff18db13cbd` | `62f077dfa948186ab95fd650428eafce2273153f` |
| Frontend | `feat/s1-f006-f007-catalogo` | `d73b5760d359dfe17bbdac423db968d74d282d84` | `0b0ed1c8c3449442e5611ddb321b80c73b1c0fc8` |
| SPECS | `docs/giuliano-elementos-compartidos` | `5f0d4ad27ef8fa0dfc39b13bf47e57269667587b` | `4cb6e971305d3c16d68b391178fa93de8964d49c` |

## Decisiones de resolución

- Backend adopta el validador de entorno y el bootstrap de develop. Se conserva `CatalogModule` junto a `ProductDetailModule`, Auth, Cart, Wishlist, Orders, Checkout, Health y Prisma; se elimina la copia antigua del validador.
- Se combinan las variables de ejemplo, scripts y documentación de ambos lados. La preparación G6 y `start:prod` siguen disponibles. `npm test` conserva las suites de la base y añade el comprobador G6; CI evita repetir la misma suite HTTP.
- El proxy de catálogo conserva las rutas de colección y detalle por slug, y emplea el helper de origen aprobado para Docker. La comprobación server-side de ficha usa ese mismo helper, manteniendo el 404 real dentro de la red de contenedores.
- El proxy de carrito mantiene cookies y Authorization explícito. No solicita una identidad MOCK por defecto ni reemplaza una identidad rechazada. Esto conserva la corrección ya documentada de la rama de Giuliano; el Backend sigue autorizando la operación.
- Vitest incluye componentes, pruebas de detalle, rutas propias y la suite separada de servidor. Playwright recupera las pruebas de catálogo que develop excluía mientras el catálogo estaba en otro PR; conserva detalle y checkout del baseline. Las pruebas optativas de favoritos conservan sus configuraciones explícitas.
- DS-001 conserva las referencias de Figma y la decisión kit-neutral de Checkout incorporada en develop. No cambia tokens ni aprueba un kit global.

Se añaden regresiones de colección/detalle con identidad coincidente, rutas de proxy por slug y 404 server-side en Docker. Las comprobaciones de Docker pasan de cuatro a seis al incorporar identidad del detalle y respuesta 404 de página.

## Verificación del resultado

| Validación | Resultado |
|---|---|
| Backend build, tipado y Prisma validate | PASS |
| Backend unitarias | 129 PASS |
| Backend HTTP | 129 PASS |
| Backend emisor de prueba + comprobador G6 | 4 + 5 PASS |
| **Backend total** | **267 PASS** |
| Frontend componentes, detalle y rutas | 174 PASS |
| Frontend servidor | 41 PASS |
| Frontend build y tipado | PASS |
| Frontend lint | Sin errores; una advertencia heredada de OrdersHistory |
| Chromium contra el stack Docker temporal | 25 PASS, 1 omitido (checkout persistido optativo) |
| **Casos automatizados distintos** | **507 PASS, 1 omitido** |
| Comprobaciones adicionales del stack Docker | 6 PASS |

Las pruebas se ejecutaron en imágenes Linux temporales con dependencias de los lockfiles integrados y datos sintéticos. El navegador utilizó un proxy de loopback hacia el contenedor para conservar el contexto seguro requerido por Web Crypto, sin desactivar TLS ni modificar el checkout. Se actualizaron las expectativas antiguas que exigían enlaces de cuenta/favoritos deshabilitados, porque develop ya incorpora sus rutas activas.

El proyecto temporal `g1-h3-merge-20261017` usa los puertos 3300/10300 y un PostgreSQL propio. No carga el `.env` privado y no reemplaza el stack habitual. Se ejercitan las migraciones del baseline únicamente en esa base desechable. Las suites unitarias/HTTP emplean dobles controlados y no escriben en una BD del equipo.

Los conteos incluyen regresiones de otros integrantes y no suman repeticiones. Las pruebas de integración externas siguen separadas de las suites locales con fixtures; no se activa G6 REAL con este merge.

Backend publicado: [merge f258574](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/f25857469f1ff05dacb506773b3889ce4afc6273). Pasaron [H3 Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/39013739390) y [validación de PR Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/39013741760), con sus controles de seguridad, arranque y contrato.

Frontend publicado: [merge 9696bd1](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/9696bd1a58e5cce786849b5e480d3df970bce803). El CI de esta rama fija el Backend integrado anterior y conserva las suites de servidor. Sus resultados se consultan en los checks del PR #3.

## Archivos privados y límites

Los cambios locales de `next-env.d.ts` se guardan antes del merge y se restauran después de las pruebas. El `.env` de Backend no se versiona ni se reemplaza. La preparación personal de presentación se actualiza con esta integración y permanece excluida de Git.

Los PR existentes de [Backend #11](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11), [Frontend #3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3) y [SPECS #2](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/2) permanecen draft. La integración de ramas no acredita aceptación humana, despliegue público ni llamada real a G6.
