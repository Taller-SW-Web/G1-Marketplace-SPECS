# Spec de contrato API — F-008 Filtros

Extiende `GET /api/v1/catalog/products` con `categoryIds`,`brandIds`,`minPrice`,`maxPrice`; `400 INVALID_PRICE_RANGE`. BFF obtiene maestros activos y delega filtro/precio a dueños; externo `I-01`.

## Propuesta implementada H4 — 26/10/2026, en revisión

El OpenAPI de G6 `0.6.0-rc.1`, blob `f64bfe9a097b2a0f74c2600988305443d92f640e`, publica `categoriaId`, `marcaId`, `precioMin` y `precioMax`. G1 mantiene las claves históricas `categoryIds`/`brandIds` con **un ID por dimensión** y combinación AND. CSV, duplicados, IDs vacíos y criterios administrativos se rechazan con 400 antes del proveedor. Multiselección requiere ampliar/homologar el contrato; no se filtra localmente una página parcial.

Importes PEN no negativos, hasta dos decimales y rango mínimo ≤ máximo; formato/rango inválido devuelve `400 INVALID_PRICE_RANGE`. G1 adapta a los nombres del proveedor, conserva búsqueda/orden y reinicia a página cero cuando cambia un filtro. El precio se filtra en G6; no se inventa un precio de tarjeta a partir de un SKU.

### Maestros públicos de filtros

`GET /api/v1/catalog/filters` es una operación **aditiva de Marketplace**, implementada para revisión; no introduce una ruta de G6. No requiere sesión del comprador ni acepta parámetros. Usa las lecturas publicadas `/api/v1/categorias` y `/api/v1/marcas` con identidad técnica server-only según la configuración autorizada.

```json
{
  "categories": [{ "categoryId": "categoria-publica", "name": "Nombre público" }],
  "brands": [{ "brandId": "marca-publica", "name": "Nombre público" }]
}
```

Sólo expone IDs/nombres de maestros activos; arreglos vacíos son válidos si el proveedor responde válidamente. Un fallo de cualquiera de las lecturas produce `503 CATALOG_UNAVAILABLE`, con reintento de filtros separado de los productos. No afecta `home`. Query no permitida: `400 INVALID_PARAMETERS`. Mantiene `Cache-Control: no-store`, `X-Request-Id` y `X-Catalog-Source`.

`422 CATEGORIA_INVALIDA/MARCA_INVALIDA` del proveedor se traduce a `400 INVALID_FILTER`; no se exponen cuerpos privados. El resto de errores/timeout conserva error seguro de catálogo. El proxy Next permite únicamente la ruta exacta `filters`, además de las rutas ya existentes.

La implementación y las pruebas locales no acreditan aprobación de API, grants, disponibilidad de marcas ni integración completa. Evidencia y límites en [corte H4 de Giuliano](../../plan/evidencias/H4-GIULIANO-2026-10-26.md).

- [ ] **API-CA-F008-01:** IDs inactivos no se presentan como opciones.
