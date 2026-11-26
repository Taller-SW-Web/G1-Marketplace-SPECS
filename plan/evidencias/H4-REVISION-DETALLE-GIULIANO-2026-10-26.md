# Revisión técnica preliminar del detalle — Giuliano

26/10/2026. Bloque de Sebastian: F-011–F-015. Esta revisión de fuentes y regresión no equivale a aprobación humana, revisión de todas las PR vigentes ni aceptación REAL de las cinco funciones.

Fuentes: rama local `feat/giuliano-hito4` de FE/BE, basada en `develop` e integrada con `main`. Archivo BE `src/catalog/product-detail.service.ts`, contrato/validador `product-detail.dto.ts` y FE `src/features/catalog/components/ProductDetailContainer.tsx`/tipos relacionados.

| Función | Hallazgo | Tratamiento requerido / evidencia de aceptación |
|---|---|---|
| F-011 Ficha | `ProductDetailService.getBySlug` conserva fixtures en MOCK; en REAL devuelve 503 y mantiene el TODO de integración. Las pruebas locales de galería, proxy, DTO y detalle pasan dentro de las suites ejecutadas | Sebastian completa adaptador REAL por contrato, demuestra slug→detalle, ausente/no elegible/error y despliegue; Giuliano revisa navegación/retorno desde catálogo |
| F-012 Precio/oferta | DTO v1 declara precio fuera de su corte; las tarjetas actuales no inventan importes | Revisar la ampliación de contrato/implementación que aporte Sebastian, vigencias/moneda/fuente y evidencia REAL |
| F-013 SKU | DTO v1 también excluye SKU/variante. El corte observado no acredita selección REAL y handoff | Probar simple/variantes, selección inválida y distinción productId/variantId/SKU con Andres |
| F-014 Disponibilidad | El corte de ficha no acredita estados comerciales REAL ni cantidad N | Resolver G-G6-COMPAT, probar los estados acordados y fuente realizable; no inferir cantidad desde disponibilidad |
| F-015 Relacionados | El corte v1 no demuestra la integración de relacionados | Revisar candidatos/enriquecimiento, máximo/dedupe/exclusión del origen y degradación al recibir implementación/contrato |

Punto positivo de integración local: `catalog.e2e-spec.ts` comprueba listado→ficha con identidad de producto/slug/nombre conservada en MOCK. El catálogo devuelve enlace con `returnTo` y mantiene acciones de favorito separadas del enlace. No se extrapola esa regresión a Productos REAL.

Aporte de Giuliano preparado: controles de catálogo y navegación, mapeos de filtros/orden/página, contrato de maestros y casos para consumer tests API-002. Revisión visual definitiva de V-006/O-001 y biblioteca DS-001 permanece pendiente. Si Giuliano coimplementa cambios de detalle, debe intervenir otro revisor independiente según la matriz.

No se modificó el código del detalle ni se aprobaron PR o tareas ajenas. Esta nota sirve para el handoff de revisión; no atribuye ejecución de F-012–F-015 por ausencia de campos en un corte v1.
