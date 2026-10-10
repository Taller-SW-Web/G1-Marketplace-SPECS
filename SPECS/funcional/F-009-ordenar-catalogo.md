# Spec funcional — F-009 Ordenar resultados

| ID | Estado |
|---|---|
| `F-009` | Ajustada al ordenamiento publicado por Productos; integración condicionada por `I-01`. |

Ordena resultados por nombre de producto mediante el contrato publicado por Productos. Excluye ordenar localmente una página incompleta.

- Valores habilitados: `NAME_ASC` y `NAME_DESC`, que el BFF adapta a `NOMBRE_ASC` y `NOMBRE_DESC` del proveedor.
- `RELEVANCE`, `NEWEST`, `PRICE_ASC` y `PRICE_DESC` quedan fuera del selector y de las solicitudes reales hasta que Productos publique y se homologue una regla de ordenamiento a nivel de producto. En particular, el precio de un SKU no se extrapola a un producto con varias variantes.
- Cambio conserva query/filtros y reinicia página.

- [ ] **CA-F009-01:** Orden desconocido no llega al proveedor.
- [ ] **CA-F009-02:** La UI y el BFF no ofrecen ni envían opciones aún no publicadas por Productos.
