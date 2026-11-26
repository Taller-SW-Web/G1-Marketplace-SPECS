# Preparación de integración G6 — Giuliano — H3

Fecha: 17/10/2026. Alcance: F-006/F-007 hasta semana 8. Este registro describe trabajo preparatorio, no cierre ni aceptación de integración REAL.

## Fuentes revisadas

| Fuente | Revisión |
|---|---|
| [Contrato HTTP G6](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/contratos/http/openapi.yaml) | OpenAPI candidato `0.6.0-rc.1`; blob `f64bfe9a097b2a0f74c2600988305443d92f640e` |
| [Alineación Marketplace](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/integraciones/ALINEACION_MARKETPLACE.md) | Rutas, mapeo, identidad propuesta y dependencias |
| Backend G6 | `9866ff26a8ff542b802ae39775db2e0326c623fb` |
| Prueba pública | 17/10/2026 01:25 Lima: categorías y productos devolvieron 503 Caddy indicando Gateway no desplegado; sin token y con TLS verificado |

## Trabajo preparado

- Prueba HTTP reproducible de `CatalogModule` y su adaptador contra un proveedor local de contrato. No sustituye `fetch` ni la factory del proveedor y no lee el `.env` real.
- Override Docker explícito para activar REAL cuando exista configuración autorizada, conservando MOCK como modo habitual.
- Comando de comprobación de nuestro BFF o proxy Next: exige REAL y distingue errores, falta de datos y lecturas positivas; no recibe ni imprime la credencial de G6.
- Guía operativa con rutas, variables privadas, mapeos, condiciones de token/renovación y evidencia requerida. [Guía Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/962a259d67c08ad430ee64c0b5b24ff18db13cbd/docs/INTEGRACION-G6-H3.md).

Implementación publicada en la rama de Giuliano `feat/s1-f006-f007-catalogo`, commit [962a259](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/962a259d67c08ad430ee64c0b5b24ff18db13cbd). No se modifica main/develop ni se abre otro PR. La guía personal de presentación y el `.env` permanecen fuera de Git.

Las rutas son `GET /api/v1/categorias` y `GET /api/v1/productos?canal=MARKETPLACE`. El detalle por slug pertenece al bloque de Sebastian y no se implementa en este cambio. La paginación traduce `page=0` a `pagina=1`; imágenes omitidas/vacías conservan `image:null`.

## Validación

| Validación local | Resultado |
|---|---|
| Tipado `npm run lint` | PASS |
| Unitarias Backend existentes | 42 PASS |
| Emisor local de identidad, regresión existente | 4 PASS |
| Comprobador G6 | 5 PASS nuevos |
| HTTP Backend existente | 29 PASS |
| HTTP BFF → proveedor local de contrato G6 | 14 PASS nuevos; incluye ejecución real del CLI contra el BFF |
| **Total de casos distintos Backend** | **94 PASS; 19 nuevos** |
| Build TypeScript y generación Prisma Client | PASS; sin migraciones |
| Esquema Prisma | PASS |
| Compose base y override | PASS: ambas configuraciones se resuelven y sólo cambia `CATALOG_SOURCE` de mock a real |

El total no incluye Frontend ni suma las repeticiones de suites. Las pruebas usan datos sintéticos y un token estático local; no acreditan firma G7, grants, elegibilidad real ni despliegue de G6. No se envían secretos a servicios externos. La comprobación Compose se hizo capturando sus valores en memoria y publicando únicamente el resultado; el entorno Docker en ejecución no se modificó.

## Pendientes externos

G6 debe desplegar y conectar Gateway/servicios y resolver su política autoritativa de elegibilidad: en la revisión consultada se inyecta `PendingCommercialEligibility`, que devuelve 503. G6/G7 deben confirmar credenciales, permisos, audiencia e identidad, incluida la relación de `sub` con la allowlist y el mecanismo de renovación. El equipo debe registrar homologación y probar la web → BFF → G6 con productos elegibles y trazas correlacionadas.

La guía personal de presentación se ensaya bajo la suposición solicitada de cierre y aceptación completos; esa suposición no modifica el estado de este registro, los PR ni los gates del plan.
