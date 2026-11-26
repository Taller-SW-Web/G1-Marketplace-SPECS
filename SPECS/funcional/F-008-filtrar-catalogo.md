# Spec funcional — F-008 Filtrar catálogo

| ID | Estado |
|---|---|
| `F-008` | Aprobada; Taxonomía/Pricing condicionados por `I-01`. |

Filtra catálogo público por categoría, marca y rango de precio. Combina condiciones AND, permite limpiar y valida rango; excluye stock/filtros administrativos.

- IDs activos, no nombres libres; `minPrice <= maxPrice`, importes no negativos, PEN.
- Aplicar reinicia página y conserva búsqueda/orden.

- [ ] **CA-F008-01:** Rango inválido no consulta catálogo.


Corte H4 alineado el 28/10/2026: selección única de categoría y única de marca, AND entre dimensiones; precio conserva su validación. No se acepta CSV ni IDs repetidos. Multiselección queda fuera hasta contrato compatible. Aplicar confirma borrador y reinicia página; cancelar conserva criterios. La disponibilidad REAL de marcas/precio y la aceptación independiente se registran aparte.
