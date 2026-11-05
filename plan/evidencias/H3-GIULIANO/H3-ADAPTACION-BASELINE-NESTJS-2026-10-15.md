# Adaptación de las ramas H3 al baseline compartido — 15/10/2026

Giuliano confirmó usar **Backend/develop con NestJS** tras la [auditoría de baselines](H3-AUDITORIA-BASELINES-2026-10-15.md). Se adapta su catálogo a esa arquitectura, sin modificar main/develop para acomodar el servidor anterior. Se mantiene H3 y la política de publicar únicamente las ramas individuales, sin abrir PR.

Autoría asistida por Codex. Comprobaciones ejecutadas por el agente; revisión humana de Sebastian/Leonidas y aceptación del equipo pendientes. Clasificación de los recorridos: **MOCK**, sin llamada real a G6 ni despliegue.

## Bases y commits publicados

| Repositorio | Base compartida adoptada | Rama individual y cambio |
|---|---|---|
| Backend | develop `ed9582e55da30007620d5740f9e4c80d41d5ad8b`, baseline de Leonidas integrado por PR #9 | `feat/s1-f006-f007-catalogo`: [055ec99](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/055ec995ddd6719551c5ebf1a50abd841093dc27) |
| Frontend | main `0f47537ee12c25194817f7682be84500a62dde1c` | `feat/s1-f006-f007-catalogo`: [0f352fd](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/0f352fd3eca5ae8ce379c88153d65671808858a3) |
| SPECS | main `a8c3a7e21482063d71a083fd950dd8fa418b615c`, sin baseline nuevo que incorporar | `docs/giuliano-elementos-compartidos`: esta evidencia, actualización de auditoría, inventario y guías |

Backend incorpora develop mediante un commit de integración sobre la rama existente; no requiere force push ni reescribe los commits publicados. Se comprobó que develop es ancestro del nuevo HEAD. Frontend conserva main como base y sólo modifica el arranque de pruebas y la guía de ejecución. SPECS conserva su base y registra la adaptación.

## Qué se conserva del baseline

Se verificó igualdad contra develop de package.json y package-lock.json, src/main.ts, módulos de health y Prisma, filtro global 404, configuraciones TypeScript/Jest/SWC/Nest/Node, render.yaml, .gitignore, esquema/migraciones Prisma y database/db.sql. El README conserva todo el contenido del baseline y añade al final las referencias del catálogo.

No se cambian dependencias, arranque, validación obligatoria de DATABASE_URL, CORS_ORIGINS, ciclo de vida de Prisma ni health/readiness. AppModule sólo añade el import y registro de CatalogModule. El diff frente a develop afecta 17 archivos, con 926 inserciones y sin eliminaciones; no resta archivos del baseline.

La fusión detectó conflicto en .env.example y en la eliminación de src/server.js; se conservaron la configuración y eliminación del baseline. También se corrigió la fusión automática de package.json, que habría repetido la clave test y restaurado node --test: el archivo final es idéntico al baseline y usa Jest.

## Catálogo adaptado

- CatalogModule registra CatalogController, CatalogService, proveedor por CATALOG_PROVIDER, interceptor y filtro locales. ConfigService selecciona MOCK/REAL/UNCONFIGURED.
- Se portaron errors, query, fixtures y provider a TypeScript. Se eliminaron src/app.js, src/server.js y los helpers JavaScript anteriores; no existe un segundo servidor de aplicación.
- Se conservan `/api/v1/catalog/home|products`, DTO, normalización, rechazo de parámetros inválidos/duplicados, paginación básica, proyección pública, correlación, logs saneados, timeout, revisión contractual fijada y prohibición de MOCK en producción.
- El interceptor genera requestId y cabeceras del catálogo; el filtro local devuelve problem+json. Ninguno reemplaza filtros o controles de otros módulos.
- CORS adopta el comportamiento de develop: concede cabeceras sólo a orígenes configurados; no reinstala el HTTP 403 por origen del handler previo. No representa autenticación. Las rutas inexistentes conservan el 404 `{error: "Ruta no encontrada"}` del baseline.
- No se inventan precios, stock, marca comercial ni destacados. No se añaden filtros múltiples, orden visual, ficha ni funciones posteriores a semana 8.

La composición se implementó con los patrones oficiales de [controladores](https://docs.nestjs.com/controllers), [proveedores por token](https://docs.nestjs.com/fundamentals/custom-providers) y [filtros de excepciones](https://docs.nestjs.com/exception-filters), adaptados a los componentes y configuración del baseline.

## Verificaciones ejecutadas

| Comando / comprobación | Resultado observado |
|---|---|
| Backend npm ci | Instalación del lockfile del baseline, sin actualizar paquetes |
| Backend npm run build | Prisma Client generado y compilación a dist/main.js; también se compiló desde Playwright |
| Backend npm run lint | Tipado de código y pruebas pasó en la versión final |
| Backend npm test -- --coverage=false | 34 pruebas pasaron: 32 de catálogo/proveedor y las 2 unitarias de health del baseline |
| Backend npm run test:e2e | 19 pruebas pasaron: 13 de catálogo/AppModule compuesto y las 6 HTTP de health del baseline |
| Backend npm run prisma:validate | Esquema válido con URL sintética; no se conectó ni se ejecutaron migraciones |
| Backend npm audit --omit=dev | 0 vulnerabilidades de producción reportadas |
| Frontend npm run lint / typecheck | Pasaron |
| Frontend npm run test:components | 10 pruebas pasaron |
| Frontend npm run test:e2e | Build de producción y 16 pruebas de Edge pasaron contra el Backend NestJS compilado |
| Git y documentación | Archivos protegidos del baseline idénticos, package.json sin claves duplicadas, conflictos resueltos, diff y enlaces locales verificados |

La primera compilación detectó un estrechamiento de tipo pendiente para el orden permitido; se corrigió sin ampliar valores válidos. La primera ejecución Jest detectó tres fallos al portar pruebas: dos por clasificación de DOMException/AbortError entre contextos y uno por comparación de prototipos de DTO procedentes de Response.json. Se conservó el diagnóstico por nombre seguro y se usó comparación estructural de Jest para el DTO, manteniendo los datos esperados. Las ejecuciones finales anteriores pasaron; no se cuentan los fallos iniciales como pruebas aprobadas.

La instalación completa reportó 19 vulnerabilidades moderadas de herramientas de desarrollo que ya están en el lockfile del baseline. Se registran para revisión del responsable de arquitectura; no se aplicó audit fix/force ni se cambió la base para resolverlas por cuenta del catálogo. El resultado de producción anterior se comprobó mediante auditoría nueva.

Playwright ahora usa los scripts build/start:prod del Backend, con CATALOG_SOURCE=mock, NODE_ENV=test, CORS_ORIGINS explícito y DATABASE_URL PostgreSQL sintético a un puerto sin BD. Se verifica el arranque real compilado, no un reemplazo del servidor. El catálogo funciona aunque readiness indique BD no disponible; no se falsea health. Los servidores de prueba se detienen al finalizar.

El next-env.d.ts local de Frontend, ya modificado por next dev antes del trabajo, se guardó y restituyó exactamente tras las pruebas; se verificó su SHA-256 y no se incluyó en el commit. Las pruebas de esta evidencia usaron los tipos generados por el build.

## Handoff y límites

Las guías [Backend/CATALOGO-S1.md](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s1-f006-f007-catalogo/docs/CATALOGO-S1.md), [Backend/ELEMENTOS-COMPARTIDOS.md](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s1-f006-f007-catalogo/docs/ELEMENTOS-COMPARTIDOS.md) y [Frontend/CATALOGO-S1.md](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/s1-f006-f007-catalogo/docs/CATALOGO-S1.md) describen los comandos actuales y la migración de imports internos. El inventario central pasa a versión documental 0.2.2, sin cambiar DS-001 ni las props de componentes React.

Main/develop se verificaron sin cambios durante la publicación de ambas ramas de código. No se incorporaron ramas funcionales ajenas, no se promovió el baseline a main ni se abrió PR. I-01, credenciales/configuración real, despliegue, revisión humana y aceptación H3 siguen pendientes; la adaptación técnica no los cierra.
