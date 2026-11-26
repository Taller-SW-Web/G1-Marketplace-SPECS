# Evidencia de avance local — Giuliano — F-006/F-007

Fecha: 14/10/2026. Fuente: trabajo ejecutado en los checkouts locales Frontend y Backend. Clasificación: **MOCK**, con adaptador candidato probado mediante respuestas sintéticas. No se ejecutó una llamada real a G6 ni un despliegue. Revisión humana y aceptación pendientes. Los commits de trabajo se publican en sus ramas; Giuliano preparará los PR manualmente al terminar.

**Actualización de política por instrucción de Giuliano:** crear commits y subir las ramas de trabajo de cada repositorio, sin subir a main ni abrir PR. SPECS usa `docs/giuliano-elementos-compartidos`; Frontend y Backend usan sus ramas de catálogo. Giuliano preparará los PR manualmente al terminar. La revisión independiente queda pendiente sobre las ramas publicadas.

## Repositorios y autoría

| Repositorio | Rama de trabajo | Base |
|---|---|---|
| G1-Marketplace-Frontend | `feat/s1-f006-f007-catalogo` | `main`, `030f657` |
| G1-Marketplace-Backend | `feat/s1-f006-f007-catalogo` | `origin/develop`, `d98b01c` |

El frontend no publicaba develop en las referencias locales; Diego debe coordinar la base de integración antes del PR. No se modificó la historia ni se creó develop. La rama backend `origin/chore/s1-base-despliegue` fue inspeccionada para identificar solapamiento en servidor/CORS/health; no se fusionó automáticamente.

### Publicación de ramas por instrucción de Giuliano

Frontend y Backend se publicaron mediante push explícito a sus ramas de trabajo; se verificó que el SHA remoto coincide con el commit y que main no cambió durante la publicación. La documentación de SPECS se publica en su propia rama. No se abren PR: Giuliano los preparará manualmente al terminar. Publicar código en GitHub no acredita despliegue ni libera I-01/H3.

| Repositorio | Rama | Commit del corte |
|---|---|---|
| Frontend | [feat/s1-f006-f007-catalogo](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/tree/feat/s1-f006-f007-catalogo) | [0f0e6dc](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/0f0e6dc5cc26cd6b196b13fe1da4bf3f2f134f13) |
| Backend | [feat/s1-f006-f007-catalogo](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/tree/feat/s1-f006-f007-catalogo) | [3357609](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/3357609c4d44235722fc63b9cbebc9ec67d7febd) |
| SPECS | [docs/giuliano-elementos-compartidos](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/tree/docs/giuliano-elementos-compartidos) | Esta nota y el inventario compartido se versionan en la misma rama |

IA utilizada: Codex, para inspeccionar las fuentes, preparar y escribir el corte de catálogo, ejecutar verificaciones y corregir fallos. Modelo exacto no identificado en esta nota. El encargo fue comenzar la parte de Giuliano desde la carpeta Proyecto según su matriz y plan. Código, pruebas, estilos, configuración y documentación de este corte fueron generados con asistencia de IA. Las comprobaciones automáticas de esta nota fueron ejecutadas por el agente; Giuliano y los revisores aún deben leer, comprender, corregir y aprobar los cambios. No se atribuye revisión humana al código generado.

## Fuentes y decisiones

- [Responsabilidades](../../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), [paquete individual](../../repartici%C3%B3n%20por%20integrantes/GIULIANO-MACCHIAVELLO-PEREZ.md) y [plan de trabajo](../../repartici%C3%B3n%20por%20integrantes/PLAN-DE-TRABAJO-GIULIANO.md).
- Funcional/UI/API/React F-006/F-007, V-005/V-006, DS-001 v0.2.0, arquitectura React y guía colaborativa.
- [OpenAPI G6](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/contratos/http/openapi.yaml): candidato `0.6.0-rc.1`, blob SHA `f64bfe9a097b2a0f74c2600988305443d92f640e`, consultado por conexión GitHub.
- [Alineación Marketplace G6](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/integraciones/ALINEACION_MARKETPLACE.md): faltan conformidad bilateral, ambiente, credenciales y grants. El primer corte separa catálogo de Pricing/Inventario.
- React + TypeScript + Next.js App Router; versiones npm verificadas y lockfile generado. UI kit pendiente: se implementó HTML/CSS con tokens desacoplados, sin aprobar Mantine/shadcn.
- Figma: en el corte inicial no se verificaron frames específicos. La [comparación posterior con Mockups](H3-COMPARACION-FIGMA-2026-10-14.md) registra ahora enlaces exactos y diferencias visibles; no certifica fidelidad ni aprobación visual.
- DTO mínimo descriptivo sin precio/stock/nombre de marca. Es una adaptación parcial del corte G6 que necesita revisión con Leonidas/Jim frente a las tarjetas comerciales completas de G1.

## Archivos y alcance

Frontend: `src/app`, `src/features/catalog`, `src/shared/ui`, `src/theme/tokens.css`, logo oficial recibido, SVG sintéticos de demostración, configuración Next/TypeScript/ESLint/Playwright, lockfile, tests y `docs/CATALOGO-S1.md`.

Backend: `src/app.js`, `src/catalog`, refactor de `src/server.js`, `test/catalog.test.js`, script `npm test`, configuración de ejemplo y `docs/CATALOGO-S1.md`. Se conserva Prisma y la comprobación real de BD en health; no se ejecutaron migraciones ni se copiaron datos de Productos.

Implementado localmente: inicio, categorías, buscador, validación de consulta, resultados, carga, vacío, error/reintento, criterios en URL, cancelación de respuestas anteriores y paginación básica. Proxy Next→BFF, validación runtime, proyección pública, CORS explícito y errores seguros.

## Verificación ejecutada

Entorno: Windows/PowerShell, Node.js `v22.18.0`, npm `11.13.0`.

| Comando / verificación | Resultado observado | Clasificación |
|---|---|---|
| Backend `npm test` (`node --test`) | 34 pruebas pasaron; incluye validación, HTTP local, mapeo 0→1, datos públicos, timeout HTTP efectivo, rechazo de revisión contractual distinta, 401/403/429/5xx y medios permitidos | MOCK |
| Backend `npm ci --offline=false --no-fund` | Instalación desde lockfile; auditoría de instalación sin vulnerabilidades reportadas | Local |
| Backend `npm run build` | Prisma Client generado correctamente; no aplica migraciones | Local |
| Frontend `npm run typecheck` | Pasó | Local |
| Frontend `npm run lint` | Pasó tras corregir hooks y sustituir configuración vulnerable | Local |
| Frontend `npm run build` | Build de producción exitoso: `/`, `/catalogo`, proxy y 404 | Local |
| Frontend instalación/auditoría | Cero vulnerabilidades reportadas tras sustituir eslint-config-next por reglas ESLint/TypeScript/React | Local |
| Frontend `npm run test:e2e` | Build de producción exitoso y 13 pruebas de Edge pasaron: búsqueda, límites sin request, error/reintento, foco/páginas, respuesta anterior, responsive, escape de texto, home vacío y payload inválido | MOCK |

La primera ejecución de navegador detectó cinco fallos: selector de nombre accesible, selección ambigua del anunciador de Next, interceptación de error y doble efecto en desarrollo. Se corrigieron los selectores/interceptación y se pasó a ejecución contra build de producción. La ejecución posterior de 11 casos pasó; tras revisar omisión de categorías vacías e IDs internos se añadieron dos casos y la ejecución final de 13 pasó. No se cuentan los fallos iniciales como pruebas aprobadas.

Revisión visual realizada por el agente sobre capturas de inicio desktop y catálogo mobile. Artefactos locales ignorados en Git: `G1-Marketplace-Frontend/test-results/inicio-desktop.png`, `test-results/catalogo-mobile.png` y `playwright-report/index.html`. No representan un frame aprobado ni una revisión humana.

## Incremento de componentes compartidos — 14/10/2026

Archivos nuevos del frontend: `src/shared/ui/Button.tsx`, `TextField.tsx`, `EmptyState.tsx`, `Skeleton.tsx`, `tests/components/` y `vitest.config.mts`. Integraciones: SearchBox, Feedback, Home y Catalog; estilos/tokens y configuración de pruebas/documentación actualizados. Asistencia de Codex y revisión humana pendientes en los mismos términos de la sección de autoría.

Commit del incremento: [119b117](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/119b117c18294d3128f5caf55858f16a1d80aee8), publicado en la misma rama de Frontend. La tabla anterior conserva los commits del corte inicial. No se modifica main ni se abre PR.

Verificación ejecutada tras el incremento:

- `npm run typecheck` y `npm run lint`: pasan.
- `npm run test:components`: **10 pruebas pasan**; submit explícito, loading/disabled sin clicks repetidos, refs, variantes, IDs/labels, asociación de hint/error, callbacks, vacío y anuncio de carga.
- `npm run test:e2e`: build de producción exitoso y **13 pruebas pasan**, con recorrido MOCK web→Next→BFF y verificación responsive/foco.
- Instalación de dependencias: auditoría sin vulnerabilidades reportadas. Vitest 5.0.4, Happy DOM 21.0.1 y Testing Library React 16.3.3 compatibles con el Node 22.18 instalado.

Los mensajes/acciones del dominio permanecen en los contenedores; los componentes no simulan integración, precio, stock ni autorización. El backend no cambia y no se repiten sus pruebas por este incremento. Las 34 pruebas anteriores pertenecen al corte inicial.

## Pendientes para cierre

Se incorporó el [catálogo de elementos compartidos](../../../SPECS/ui/sistema-diseno/ELEMENTOS-COMPARTIDOS.md), su changelog y las guías de uso en ambos repositorios de código. Esta entrega documental inventaría componentes/estilos reales y pendientes; no agrega implementación ni cambia los resultados de pruebas de la tabla anterior.

- Revisión de Sebastian; revisión técnica de Leonidas y de seguridad/despliegue con Andres cuando corresponda.
- Ambiente, token técnico `catalogo:leer`, configuración autorizada, medios y homologación I-01; prueba real y URLs públicas.
- Concordancia del primer corte descriptivo con las specs de tarjeta y decisiones visuales G-SHELL/G-STACK.
- Handoff de enlaces `/productos/{slug}` y `returnTo` a Sebastian. La ficha F-011 aún no está implementada en el frontend local.
- Favoritos/login/carrito de sus responsables, sin controles simulados en este corte.
- Scans SAST/DAST y revisión QA-002 conforme al plan; pruebas negativas locales y auditoría de dependencias no sustituyen todos esos controles.
- Revisor, explicación individual de Giuliano y aceptación de Jim. Los commits se registran abajo; los PR los preparará Giuliano manualmente al terminar.

INT continúa bloqueada. Ninguna funcionalidad, hito ni tarea se marca terminada por este avance.
