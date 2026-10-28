# Spec de contrato API — F-010 Paginación

`GET /api/v1/catalog/products?page=0&pageSize=24` valida enteros `page>=0`, `1<=pageSize<=48`; respuesta contiene `data` y `page(number,size,totalElements,totalPages)`. `400 INVALID_PAGE`; BFF conserva criterios y adapta Catálogo bajo `I-01`.

- [ ] **API-CA-F010-01:** Página/tamaño inválidos no se reenvían.

## Corte implementado H4 — 26/10/2026, en revisión

El BFF conserva la API cero basada y adapta a `pagina=page+1`, `tamanio=pageSize` de G6. Valida enteros seguros, tamaño 1–48 e índice máximo operativo de 1 000 000 antes de consultar. Rechaza metadatos incoherentes y tarjetas duplicadas; el frontend valida también la relación entre tamaño, total, páginas y cantidad recibida.

Decisión técnica implementada y registrada en `V-006-OPEN-03` (28/10/2026): una página numéricamente válida fuera del total conserva la respuesta vacía y sus criterios. La UI ofrece «Volver a la primera página», conserva búsqueda/filtros/orden y no inicia ciclos de reintento automático. No muestra controles para avanzar más allá del total. La alternativa de comportamiento queda resuelta en V-006; la revisión final de contrato/UI y el cierre de la funcionalidad conservan sus dependencias de aceptación/despliegue.

Cambiar búsqueda/filtro/orden vuelve a primera página; navegar páginas conserva los criterios. El número visible es `page+1`. Evidencia local en [corte H4](../../plan/evidencias/H4-GIULIANO-2026-10-26.md); paginación REAL desplegada y revisión independiente pendientes.


Alineación del 28/10/2026: [errores, metadatos y límites comunes de catálogo H4](CATALOGO-H4-ERRORES-Y-METADATOS.md). La distinción pública de timeout usa 503/CATALOG_TIMEOUT; otras indisponibilidades conservan 503/CATALOG_UNAVAILABLE. Home/filtros rechazan query. No implica aceptación ni liberación de I-01.
