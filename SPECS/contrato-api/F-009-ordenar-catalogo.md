# Spec de contrato API — F-009 Ordenamiento

`GET /api/v1/catalog/products?sort=NAME_ASC` valida el enum público `NAME_ASC | NAME_DESC` y adapta respectivamente a `NOMBRE_ASC | NOMBRE_DESC` de `GET /api/v1/productos?canal=MARKETPLACE` de Productos. No se ordena localmente una página incompleta. `400 INVALID_SORT` para otros valores; la respuesta incluye sort aplicado y página. La prueba del adaptador y los grants siguen bajo `I-01`.

- [ ] **API-CA-F009-01:** Empates tienen orden estable por identificador.
- [ ] **API-CA-F009-02:** `PRICE_ASC`, `PRICE_DESC`, `NEWEST` y `RELEVANCE` no se transmiten al proveedor ni se aceptan como valores habilitados mientras no exista contrato canónico homologado.
