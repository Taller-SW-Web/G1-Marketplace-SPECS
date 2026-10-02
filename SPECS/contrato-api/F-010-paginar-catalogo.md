# Spec de contrato API — F-010 Paginación

`GET /api/v1/catalog/products?page=0&pageSize=24` valida enteros `page>=0`, `1<=pageSize<=48`; respuesta contiene `data` y `page(number,size,totalElements,totalPages)`. `400 INVALID_PAGE`; BFF conserva criterios y adapta Catálogo bajo `I-01`.

- [ ] **API-CA-F010-01:** Página/tamaño inválidos no se reenvían.
