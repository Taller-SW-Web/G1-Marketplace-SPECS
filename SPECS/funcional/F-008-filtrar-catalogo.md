# Spec funcional — F-008 Filtrar catálogo

| ID | Estado |
|---|---|
| `F-008` | Aprobada; Taxonomía/Pricing condicionados por `I-01`. |

Filtra catálogo público por categoría, marca y rango de precio. Combina condiciones AND, permite limpiar y valida rango; excluye stock/filtros administrativos.

- IDs activos, no nombres libres; `minPrice <= maxPrice`, importes no negativos, PEN.
- Aplicar reinicia página y conserva búsqueda/orden.

- [ ] **CA-F008-01:** Rango inválido no consulta catálogo.
