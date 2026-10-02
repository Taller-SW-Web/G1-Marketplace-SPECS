# Spec funcional — F-009 Ordenar resultados

| ID | Estado |
|---|---|
| `F-009` | Aprobada; Catálogo/Pricing condicionados por `I-01`. |

Ordena resultados: relevancia por defecto cuando existe búsqueda, novedades, precio ascendente/descendente. Excluye orden local de lista incompleta.

- Valor permitido: `RELEVANCE`, `NEWEST`, `PRICE_ASC`, `PRICE_DESC`.
- Cambio conserva query/filtros y reinicia página.

- [ ] **CA-F009-01:** Orden desconocido no llega al proveedor.
