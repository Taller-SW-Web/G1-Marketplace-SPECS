# Spec de contrato API — F-009 Ordenamiento

`GET /api/v1/catalog/products?sort=NAME_ASC` admite sólo `NAME_ASC | NAME_DESC`; adapta a `NOMBRE_ASC | NOMBRE_DESC` de G6. Un valor distinto devuelve `400 INVALID_SORT` antes del proveedor. No se ordena localmente una página incompleta.

La respuesta incluye `data`, `page` y **`sort`**: `NAME_ASC`, `NAME_DESC` o `null`. El campo identifica el criterio explícito delegado al proveedor; `null` significa que se conserva su orden predeterminado, sin inventar uno. Lo devuelve tanto REAL como MOCK. El cliente tolera temporalmente el DTO previo sin ese campo durante el despliegue aditivo, pero valida el enum cuando está presente. El OpenAPI G1 0.2.0 lo exige a la nueva versión Backend.

## Estabilidad y frontera externa

El criterio objetivo de desempate es identificador estable. MOCK lo implementa antes de paginar. Las pruebas MOCK y la reproducción manual sin duplicados no demuestran una garantía contractual global de G6: ese desempate permanece bajo I-01/G-SORT hasta confirmación del proveedor y revisión externa. No se añade un segundo sort no publicado ni se reordena sólo una página en G1.

- [ ] **API-CA-F009-01:** Empates tienen orden estable por identificador; pendiente confirmación/ensayo externo.
- [ ] **API-CA-F009-02:** `PRICE_ASC`, `PRICE_DESC`, `NEWEST` y `RELEVANCE` no se transmiten ni se habilitan sin homologación.

[Errores y metadatos comunes](CATALOGO-H4-ERRORES-Y-METADATOS.md). Integración autenticada y despliegue conservan sus gates; la corrección del DTO no constituye aprobación de F-009.
