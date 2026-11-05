# Auditoría de baselines y ramas de Giuliano — 15/10/2026

Instrucción de Giuliano: adaptar sus tres ramas a la base compartida, sin modificar main/develop para acomodar el trabajo individual. Se mantiene H3, sin crear PR ni incorporar módulos ajenos.

Fuentes: `git fetch --prune origin` en los tres repositorios, historias y árboles de las referencias remotas, archivos del baseline y metadatos del PR de arquitectura. Se usan `origin/main` y `origin/develop`, no los main locales que todavía apuntan a cortes anteriores.

## Estado remoto encontrado

| Repositorio | main remoto | develop remoto | Situación de la rama individual |
|---|---|---|---|
| Frontend | `0f47537ee12c25194817f7682be84500a62dde1c` | No existe en los refs publicados | El PR #1 ya incorporó los commits de catálogo/Figma. Su árbol es idéntico al de la rama individual anterior `3a5a20b`; sólo faltaba el commit de merge. |
| Backend | `d98b01c9aa2c04f614699df78ef4070b34803472` | `ed9582e55da30007620d5740f9e4c80d41d5ad8b` | La rama individual `f095de1` sigue basada en main. El baseline NestJS está integrado únicamente en develop. |
| SPECS | `a8c3a7e21482063d71a083fd950dd8fa418b615c` | No existe en los refs publicados | main ya es ancestro de la rama individual; no hay commits nuevos de main que incorporar. La rama conservaba cinco commits propios antes de esta nota. |

En esta consulta no se encontraron tres nuevos baselines incorporados en main. El cambio nuevo de arquitectura está en Backend/develop. Las ramas ajenas de ficha, checkout e historial se identificaron para contexto; no se fusionaron en las ramas de Giuliano.

## Frontend: alineación realizada

Se avanzó `feat/s1-f006-f007-catalogo` por fast-forward de `3a5a20b` a `0f47537`, y se publicó únicamente esa rama. No se generó un commit de código ni se reescribió el historial.

Se comprobó igualdad de árboles antes de la operación y que el SHA de main remoto no cambiara durante la publicación. No fue necesario repetir las pruebas de aplicación porque no cambió ningún archivo del árbol comprometido; los resultados anteriores están en la [evidencia de adaptación Figma](H3-ADAPTACION-FIGMA-2026-10-15.md).

El `next-env.d.ts` local generado por `next dev` estaba modificado antes de comenzar. Se conservó exactamente, verificando su SHA-256 antes y después; no se incluyó en ningún commit ni se restauró sobre el trabajo del usuario.

## Backend: cambios del baseline NestJS

El [PR #9](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/9), de Leonidas, se fusionó en **develop** mediante `ed9582e`; el commit de implementación es `487ffa0`. Git y los metadatos de GitHub coinciden sobre la base y el estado fusionado. El diff respecto de main afecta 24 archivos, con 9486 inserciones y 145 eliminaciones, principalmente por dependencias y lockfile.

| Área | Baseline compartido | Impacto sobre nuestro catálogo |
|---|---|---|
| Arranque | Elimina `src/server.js`; introduce `src/main.ts`, AppModule y módulos NestJS | El catálogo debe incorporarse como módulo/controlador/servicio; no restaurar el servidor `node:http` como arranque principal. |
| Lenguaje y build | TypeScript, Node 22, compilación a `dist/main.js` y dependencias NestJS | Conservar scripts y lockfile del baseline; adaptar imports, tipos y pruebas del catálogo. |
| Configuración | Valida PORT y exige DATABASE_URL PostgreSQL al arrancar | El arranque de pruebas web debe aportar configuración local explícita. No hace falta modificar esquemas ni ejecutar migraciones para portar lectura de catálogo. |
| CORS | `CORS_ORIGINS` admite varios orígenes y deshabilita concesiones si está vacío | Reemplazar el uso del `CORS_ORIGIN` singular de nuestro handler y respetar la configuración compartida. |
| Salud | Conserva `/` y `/health`; añade `/ready` y `/live` | Mantener HealthModule/PrismaService y su ciclo de vida. Catálogo no debe sustituir health/readiness. |
| Calidad | Jest/SWC, pruebas unitarias y Supertest e2e | Adaptar o integrar los 34 casos de catálogo sin perder validación, errores seguros, timeout, mock explícito y aislamiento del proveedor. |
| Render | Compila TypeScript, arranca `dist/main.js`, conserva migraciones de despliegue y usa `/live` | Respetar el blueprint y coordinar orígenes reales antes de promover a main. No desplegar automáticamente desde esta adaptación. |
| Persistencia | Sin cambios en Prisma schema, migraciones ni SQL | No copiar datos de Productos ni crear cambios de BD para adaptar el catálogo. |

También deben revisarse `playwright.config.ts` y las guías de Frontend: actualmente lanzan `node ../G1-Marketplace-Backend/src/server.js`, que no existe en el baseline NestJS. Los DTO públicos y las rutas `/api/v1/catalog/home|products` se pueden conservar durante la migración; cambiar el framework no autoriza cambios de contrato ni funciones H4.

El README del baseline conserva referencias históricas de roles y stack; estas no sustituyen la matriz punta a punta vigente ni justifican añadir bibliotecas al Frontend sin decisión del equipo.

**Decisión confirmada:** Giuliano eligió «Usar develop con el baseline NestJS». La [adaptación posterior](H3-ADAPTACION-BASELINE-NESTJS-2026-10-15.md) registra la integración y las pruebas. La tabla de esta auditoría conserva el estado encontrado antes de migrar; Backend se adapta a develop sin modificar esa rama compartida.

Los resultados de build, pruebas y staging descritos en el PR #9 son evidencia del autor del baseline, no ejecuciones nuevas realizadas por esta auditoría.

## SPECS y publicación

SPECS no necesita resolver divergencias con main en el estado consultado. Se incorpora esta auditoría únicamente a `docs/giuliano-elementos-compartidos`, conservando la documentación H3 propia y el historial normativo existente.

No se modifican main/develop, no se promueven baselines ni se crean PR. Sólo se adopta el baseline compartido autorizado; no se fusionan ramas funcionales de compañeros. Las verificaciones documentales y de Git no acreditan integración real con Productos ni cierre de H3.
