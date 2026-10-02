# Spec funcional — F-007 Buscar productos por texto

| ID | Estado |
|---|---|
| `F-007` | Aprobada; Catálogo condicionado por `I-01`. |

Busca productos activos por texto y muestra resultados paginados. Normaliza espacios, exige 2–120 caracteres; excluye IA/búsqueda administrativa.

- Consulta vacía vuelve a catálogo sin query.
- Resultados usan tarjetas y slugs F-011, nunca productos privados.

- [ ] **CA-F007-01:** Texto menor a dos caracteres no consulta.
