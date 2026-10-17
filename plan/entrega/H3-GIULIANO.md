# Entrega de Giuliano — H3, semanas 7–8

> **Entorno actual solicitado por Giuliano: Docker local del equipo; Render queda fuera de este paso.** Consultar la [evidencia Docker](../evidencias/H3-GIULIANO/H3-DOCKER-2026-10-16.md). Las referencias anteriores de nube se conservan como contexto; el cambio no acredita cierre H3.

Corte 16/10/2026. Alcance: F-006 inicio/categorías y F-007 búsqueda pública, con componentes compartidos. Implementación asistida por Codex; revisión humana y aceptación pendientes. Las pruebas usan **MOCK**. Ningún recorrido local acredita integración real con Productos.

**Actualización 17/10/2026:** [preparación de conexión G6](../evidencias/H3-GIULIANO/H3-PREPARACION-G6-2026-10-17.md) y [nueva integración de develop](../evidencias/H3-GIULIANO/H3-INTEGRACION-DEVELOP-2026-10-17.md). Estos registros identifican las bases y validaciones actuales; las cifras y guiones anteriores conservan su fecha.

**Actualización posterior del 17/10:** [integración de las correcciones nuevas de Sebastián](../evidencias/H3-GIULIANO/H3-INTEGRACION-SEBASTIAN-2026-10-17.md), con Problem Details de ficha, correlación compartida y conservación del acceso Docker. Tras contrastar la spec F-011 se retira el botón simulado de carrito y su confirmación ficticia; la ficha conserva el avance descriptivo MOCK de semana 8, sin declarar F-016 integrado.

La [evidencia manual de Giuliano](../evidencias/H3-GIULIANO/README.md) reúne seis capturas de Inicio, búsqueda con resultados y vacío en escritorio y emulación móvil, además del índice del historial técnico. El recorrido se hizo en Docker local con catálogo MOCK.

## Qué está preparado

Frontend conserva el diseño H3 obtenido de [Mockups Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-3), navegación por categorías, búsqueda, URL compartible, validación, vacío, carga, error/reintento y paginación básica. Los enlaces a cada ventana están en las specs UI. Backend incorpora el catálogo como módulo del baseline NestJS de develop, con validación, proyección pública, errores seguros y adaptador candidato para Productos.

El [inventario de elementos compartidos](../../SPECS/ui/sistema-diseno/ELEMENTOS-COMPARTIDOS.md) enlaza las guías de imports/props en los dos repositorios. El [corte técnico de NestJS](../evidencias/H3-GIULIANO/H3-ADAPTACION-BASELINE-NESTJS-2026-10-15.md) explica la compatibilidad con el baseline. La [evidencia de automatización](../evidencias/H3-GIULIANO/H3-AUTONOMIA-2026-10-16.md) registra resultados y límites actuales.

## Demostración local

Usar Node 22.18.0 y los tres checkouts existentes, con Backend y Frontend como carpetas hermanas. No sobreescribir un .env propio ni activar REAL sin homologación.

Terminal Backend, desde su carpeta:

```powershell
npm ci
$env:NODE_ENV = 'development'
$env:CATALOG_SOURCE = 'mock'
$env:DATABASE_URL = 'postgresql://test:test@127.0.0.1:1/h3_demo?schema=public'
$env:PORT = '10000'
$env:CORS_ORIGINS = 'http://127.0.0.1:3000'
npm run build
npm run start:prod
```

Terminal Frontend, desde su carpeta:

```powershell
npm ci
$env:MARKETPLACE_API_URL = 'http://127.0.0.1:10000'
npm run dev
```

Abrir **http://127.0.0.1:3000**. Un navegador sin extensiones de traducción evita el problema de hidratación ya identificado. La URL sintética de BD no representa una credencial real; readiness da 503 porque no hay PostgreSQL. `/live` y el catálogo MOCK funcionan: no se falsea la salud de la BD.

Guion de 5–7 minutos:

1. Mostrar inicio y aviso MOCK. Explicar que destacados permanece vacío hasta resolver G-FEATURED.
2. Abrir Running y comprobar la categoría en la URL; quitar el criterio y volver al catálogo.
3. Buscar `running`, pulsar Enter, recargar y comprobar que conserva q. Limpiar la búsqueda.
4. Probar un carácter y 121: aparece validación antes de consultar. Buscar un texto sin coincidencias: muestra vacío y permite limpiar.
5. Mostrar paginación desde el catálogo sin categoría; comprobar foco y URL. Reducir viewport a 390 y 320 px.
6. Detener Backend, volver a consultar y mostrar error/reintento conservando el texto. Reiniciar Backend y reintentar.
7. Mostrar las pruebas y la evidencia enlazada. Aclarar que ficha, cuenta, favoritos, carrito y datos comerciales completos requieren sus contratos/bloques.

No presentar los fixtures ni la ausencia de precio/stock como datos reales. El clic de una tarjeta conserva slug y returnTo, pero la ficha pertenece a Sebastian y no forma parte de este demo cerrado.

## Explicación técnica que debes preparar

| Pregunta | Respuesta respaldada por el código |
|---|---|
| ¿Cómo viaja una búsqueda? | SearchBox normaliza la URL; el contenedor consulta `/api/catalog/products` en Next; el proxy servidor llama al BFF Nest `/api/v1/catalog/products`; CatalogService usa el proveedor seleccionado. El navegador no recibe el token de Productos. |
| ¿Qué evita que una respuesta vieja reemplace la nueva? | Cancelación del fetch y protección del estado por consulta vigente, cubierta por el caso `slow old response cannot overwrite new query`. |
| ¿Cómo distingues vacío de error? | Un DTO válido con cero elementos es éxito; fallos técnicos/proveedor o DTO inválido producen error recuperable. REAL nunca cae silenciosamente a MOCK. |
| ¿Qué protege el BFF? | Rechazo de query inválida/duplicada/desconocida antes del proveedor; DTO público; imágenes HTTPS con allowlist; timeout y redirecciones rechazadas; requestId y hash de q sin texto en logs. |
| ¿Qué se adaptó a develop? | CatalogModule se añade a AppModule; usa ConfigService y las pruebas Jest/SWC del baseline. Se conservan bootstrap, Prisma, health/readiness y comportamiento CORS. |
| ¿Por qué no está cerrado H3? | Falta demostrar web→BFF→Productos real en entorno autorizado, despliegue acordado, revisión independiente y aceptación. Fixtures y CI no sustituyen esas pruebas. |

Este material permite ensayar; no acredita que Giuliano ya haya explicado o defendido el código.

## Trazabilidad del corte

| Tarea | Implementación | Verificación reproducible / límite |
|---|---|---|
| TASK-F006-FE-001 | FE `src/features/catalog/Home.tsx`, CategoryNavigation/CategoryArtwork y ProductCard según composición vigente | `tests/catalog.spec.ts`: home, categorías, home vacío; `tests/figma-h3.spec.ts`: composición/carga/error |
| TASK-F006-BE-001 | BE `src/catalog/provider.ts`, fixtures, CatalogModule/Controller/Service | `src/catalog/catalog.spec.ts`: sólo categorías activas y destacados vacíos; `test/catalog.e2e-spec.ts`: DTO/cabeceras |
| TASK-F007-FE-001 | FE SearchBox, contenedor de catálogo y lógica de consulta | `tests/catalog.spec.ts`: q 1/121, normalización/URL/limpiar, vacío/error, carrera, foco/paginación, responsive y XSS como texto |
| TASK-F007-BE-001 | BE query/provider y proyección pública | Unitarias de límites, parámetros desconocidos/duplicados, mapeo G6, timeout HTTP real contra servidor local; HTTP contra AppModule con proveedor sintético |
| TASK-F006/F007-QA-001 | Pruebas anteriores + `tests/components/shared-ui.test.tsx` | Ejecución MOCK; QA REAL sigue pendiente |
| TASK-F006/F007-QA-002 | Reglas SAST locales, Gitleaks, npm audit/inventario y negativos HTTP/navegador | Alcance y hallazgos en la evidencia; DAST staging y aceptación de riesgo pendientes |
| TASK-F006/F007-DOC-001 | Specs UI enlazadas a Figma, inventario compartido, operación, esta guía y borradores de PR | Revisión humana y evidencia REAL pendientes |

## PR y bases de integración

Por indicación posterior de Giuliano se abrieron [Backend PR #11](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11) y [Frontend PR #3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3), ambos hacia develop. También solicitó abrir el PR de este paquete SPECS hacia develop. Los textos [Backend](PR-BACKEND.md), [Frontend](PR-FRONTEND.md) y [SPECS](PR-SPECS.md) se conservan como referencia; abrir un PR no acredita aprobación, merge ni cierre H3.

| Repositorio | Rama de Giuliano | Base de integración |
|---|---|---|
| Backend | feat/s1-f006-f007-catalogo | **develop**, baseline NestJS autorizado |
| Frontend | feat/s1-f006-f007-catalogo | **develop**, creada desde main 0f47537 por indicación de Giuliano |
| SPECS | docs/giuliano-elementos-compartidos | **develop**, creada desde main a8c3a7e para el PR solicitado |

Los workflows se activan al push a tus ramas o por ejecución manual sobre ellas. No despliegan ni crean PR. Si después cambia la base compartida, revisar el diff, incorporar el baseline en la rama individual y repetir los controles antes de pedir revisión.

## Corte actualizado: adaptación a develop y despliegue

Se incorporan Backend/develop e6fc7f2 y Frontend/develop 843dfde en las ramas personales, conservando el carrito del equipo. Publicados Backend **2095c05** y Frontend **c58f596**, con start:prod restaurado, proxy de carrito sin identidad de prueba automática y **125 pruebas + 11 comprobaciones smoke** locales aprobadas. [Evidencia actual, guías y límites](../evidencias/H3-GIULIANO/H3-ACTUALIZACION-DEVELOP-2026-10-16.md). Las cifras anteriores describen sus cortes históricos.

Backend #11, Frontend #3 y SPECS #2 continúan en draft hacia develop. El catálogo sin credenciales devuelve 503 en producción; arrancar el servidor no acredita integración REAL ni cierre H3. No se despliega ni se cambian main/develop.

## Lo que requiere coordinación para cerrar

| Pendiente | Participación necesaria | Evidencia de salida |
|---|---|---|
| I-01 / Productos | G6 y Leonidas: confirmar revisión contractual, origen, token por canal seguro, medios permitidos y permisos de prueba | Prueba autorizada web→BFF→Productos, paginación, errores y timeout; requestId y logs sanitizados; registrar revisión exacta |
| G-FEATURED y campos comerciales | Productos y responsables funcionales: fuente/criterio y DTO de precio/marca/stock si se exigen al corte | Decisión enlazada y contrato; no completar campos con supuestos |
| Entorno de demostración | Coordinación OPS/Andrés: destino FE/BFF, CORS, BD y variables de servidor | URLs propias, readiness real, prueba REAL y DAST baseline autorizado; rollback acordado |
| Revisión independiente | Sebastian; Leonidas para NestJS/contrato; responsables QA/seguridad del plan | Comentarios resueltos, riesgos aceptados por humanos y aprobación enlazada |
| Riesgos de dependencias y licencias | Responsable de arquitectura/seguridad | Revisión del inventario y de las moderadas heredadas; resolución o aceptación con dueño/fecha |
| Cierre H3 | Giuliano y responsables de aceptación | Demo, trazabilidad completa, evidencia REAL y revisión; actualizar estados sólo al cumplir DoD |

No hace falta desarrollar semanas posteriores a la 8 para avanzar este corte. No se cambian políticas del equipo ni se asumen aprobaciones ajenas.
