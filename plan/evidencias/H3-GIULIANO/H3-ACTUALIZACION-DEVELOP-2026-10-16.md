# H3 — Adaptación al develop actual y preparación de despliegue — 16/10/2026

Solicitado por Giuliano después de revisar las ramas remotas de G1. Implementación asistida por Codex; revisión independiente, despliegue, integración REAL y aceptación pendientes. Alcance hasta semana 8. Se publican únicamente las ramas personales y se mantienen los tres PR en draft hacia develop.

## Bases incorporadas y revisiones

| Repo | Develop incorporado | Revisión publicada | PR |
|---|---|---|---|
| Backend | e6fc7f25e78a8b34316096839f44863f37f5e2c9, incluye carrito del PR #13 | [2095c05](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/2095c0550d0969f81ea2e9bf3dd764f02dd95617) | [#11 draft](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11) |
| Frontend | 843dfde7a4e52e1a836db0eb207d8f9aa3502c28, incluye carrito del PR #5 | [c58f596](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/c58f59619d6f262ea99787f1c710d0fa1e581495) | [#3 draft](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3) |
| SPECS | a8c3a7e21482063d71a083fd950dd8fa418b615c, sin cambios nuevos en develop | Este ajuste documental | [#2 draft](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/2) |

Los commits de aplicación son merges que conservan la historia de develop, sin reescritura ni force-push. No se modifican main/develop. Frontend fija Backend 2095c05 en CI y los controles de historial usan las bases actualizadas.

## Correcciones y compatibilidad

- Backend resuelve conflictos en AppModule y .env.example conservando CartModule, guards RS256, bootstrap y configuración del equipo, e incorporando CatalogModule y sus variables. No sustituye el carrito por la versión anterior de la rama.
- Se restaura `start:prod: node dist/main.js`: Render lo invocaba, pero develop había eliminado ese script. No se altera Render, Prisma, el esquema, las migraciones ni el lockfile Backend.
- Una regresión HTTP comprueba carrito anónimo y catálogo montados en el mismo AppModule con servicios controlados.
- Frontend conserva carrito, estilos, alias Vitest y lockfile de develop, junto con el catálogo, URL/returnTo y placeholder. Se elimina un blanco final heredado de globals.css.
- El proxy cart deja de consultar MOCK_AUTH_URL y de solicitar `/token?user=default`. Reenvía cookies para el carrito anónimo y Authorization sólo si el llamador la proporciona. Conserva Set-Cookie y el 401 del Backend, sin reemplazar una identidad rechazada por una identidad de prueba. No implementa login/sesión G7 ni cambia reglas de negocio del carrito.
- Los DTO, rutas del catálogo y contrato candidato G6 se mantienen. `image:null` sigue mostrando el placeholder. No se añaden filtros H4, precios ficticios ni funcionalidades posteriores.
- Nuevas guías [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/2095c0550d0969f81ea2e9bf3dd764f02dd95617/docs/DESPLIEGUE-H3.md) y [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/c58f59619d6f262ea99787f1c710d0fa1e581495/docs/DESPLIEGUE-H3.md) describen revisión a desplegar, Node, build/arranque, PostgreSQL, CORS, variables del servidor, health y límites. No contienen credenciales.

## Verificación local observada

Windows / Node 22.18.0, dependencias FE instaladas con npm ci, fixtures y servicios controlados; sin llamadas a G6 ni migraciones de entornos externos.

| Suite o control | Resultado |
|---|---|
| Backend build, lint | Aprobados; build genera Prisma Client sin aplicar migraciones |
| Backend Jest unitarias | 42: 38 catálogo/proveedor, 2 health y 2 guard RS256 |
| Backend emisor local Node | 4: JWKS/firma, identidades de prueba, restricción loopback y rechazo en producción |
| Backend HTTP | 29: 14 catálogo/composición AppModule, 9 carrito y 6 health |
| Frontend lint, build, typecheck | Aprobados |
| Frontend componentes/proxy | 33: 29 componentes y 4 Route Handler de carrito |
| Navegador Edge | 17 E2E aprobados contra Next y Backend compilados |
| Smoke test compilado | 7 comprobaciones con catálogo MOCK y readiness DOWN sin BD |
| Smoke production | 4 comprobaciones: destino start:prod, /live 200, /ready 503 sin BD y catálogo 503 UNCONFIGURED sin credenciales |

Total: **125 pruebas**, más **11 comprobaciones smoke**. Incluye regresiones del equipo/baseline, no sólo pruebas escritas por Giuliano. La regresión de proxy comprueba ausencia de petición al emisor de prueba incluso con NODE_ENV=production/MOCK_AUTH_URL configurado, cookie/Set-Cookie, Authorization y 401 preservados, POST/alias y rechazo de rutas arbitrarias.

El smoke production resuelve el destino del script start:prod desde package.json y arranca ese compilado con NODE_ENV=production. Sin configuración REAL conserva 503 y nunca fixtures; no es prueba de conectividad G6 ni de despliegue. CI repite ambos smokes con PostgreSQL 16 desechable y readiness UP.

El next-env.d.ts local se guardó y restauró byte por byte; los bytes del usuario no se incorporan al commit. La versión de ese archivo recibida desde develop se conserva en el índice de la integración. La guía personal de presentación se actualiza al corte de 125 pruebas/11 smokes y permanece ignorada/local, fuera del PR y GitHub.

## CI

- [Backend 2095c05 — run 38975591195](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/38975591195).
- [Frontend c58f596 — run 38975660013](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/38975660013).

Ambos runs terminaron **success** sobre los SHA exactos anteriores. Backend aprobó build/tipado, 42 Jest + 4 Node + 29 HTTP, Prisma validate, migraciones sobre PostgreSQL 16 desechable, ambos smokes con readiness UP y controles de secretos/SAST/SCA/licencias. Frontend aprobó lint, 33 componentes/proxy, 17 E2E en Chromium, typecheck y controles de seguridad. Los controles no equivalen a aceptación humana de moderadas/licencias ni a DAST de staging.

El verificador documental local registró **31 Markdown modificados, 194 destinos locales, 0 ausentes**. Su alcance son los enlaces inline locales del corte; no comprueba URLs externas ni anclas.

## Lo que sigue pendiente

Seleccionar/configurar el entorno con OPS/Andrés, disponer de URL/identidad técnica y contrato G6 homologados, probar web→Next→BFF→Productos real, ejecutar seguridad del entorno autorizado y obtener revisión/aceptación humana. Para usuarios autenticados también corresponde configurar issuer/JWKS del servicio aprobado y completar el contrato de sesión con el bloque de acceso.

El arranque y el carrito anónimo pueden prepararse sin inventar esa autenticación. Ningún /live 200, prueba con mocks o pipeline verde por sí solo cierra H3. Los datos comerciales sintéticos de otros bloques no se presentan como productos reales. Los estados de tareas no pasan a Done con este ajuste.
