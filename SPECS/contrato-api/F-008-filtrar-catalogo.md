# Spec de contrato API — F-008 Filtros

Extiende `GET /api/v1/catalog/products` con `categoryIds`,`brandIds`,`minPrice`,`maxPrice`; `400 INVALID_PRICE_RANGE`. BFF obtiene maestros activos y delega filtro/precio a dueños; externo `I-01`.

- [ ] **API-CA-F008-01:** IDs inactivos no se presentan como opciones.
