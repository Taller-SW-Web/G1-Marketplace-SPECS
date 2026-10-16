# Título propuesto

feat(h3): integrar catálogo F-006/F-007 sobre el baseline NestJS

Base manual: **develop**. Rama: `feat/s1-f006-f007-catalogo`.

## Descripción para copiar

Incorpora el catálogo público H3 como CatalogModule sobre el baseline NestJS de develop. Conserva bootstrap, Prisma, health/readiness, CORS, esquema, migraciones, dependencias y configuración de despliegue del baseline; AppModule registra el nuevo módulo. Reemplaza el servidor Node anterior por proveedores/controladores TypeScript y pruebas Jest/Supertest.

Home y búsqueda exponen DTO públicos, validación de query y paginación, errores sanitizados, correlación, proyección de medios permitidos y timeout. El adaptador candidato de Productos mantiene revisión contractual fijada y requiere homologación explícita; MOCK es opt-in, está prohibido en producción y no es fallback de REAL.

Añade CI de pruebas, PostgreSQL 16 temporal para migraciones/readiness, smoke del ejecutable compilado, escaneos y reportes sanitizados con retención de 7 días. El pipeline no despliega.

Validación, hallazgos y límites: [evidencia H3](../evidencias/H3-AUTONOMIA-2026-10-16.md). Guía operativa en `docs/CATALOGO-S1.md`; controles en `docs/CI-H3.md`. Los enlaces relativos de este borrador pertenecen a SPECS: al copiar a GitHub, usar el [documento de evidencia publicado](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/docs/giuliano-elementos-compartidos/plan/evidencias/H3-AUTONOMIA-2026-10-16.md).

Pendientes: integración G6 REAL autorizada, despliegue, DAST staging y revisión de Sebastian/Leonidas. No declara Done ni incorpora funciones posteriores a semana 8.
