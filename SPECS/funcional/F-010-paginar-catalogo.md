# Spec funcional — F-010 Paginar resultados

| ID | Estado |
|---|---|
| `F-010` | Aprobada; Catálogo condicionado por `I-01`. |

Navega páginas de resultados aplicando query/filtros/orden actuales. Incluye límites, estado sin más páginas y restablecer a primera al cambiar criterios; excluye cargar catálogo completo.

- Página cero basada; tamaño inicial 24, máximo 48.
- Página fuera de rango devuelve resultado vacío controlado/última página según contrato BFF, sin repetir consulta infinita.

- [ ] **CA-F010-01:** Cambio de filtro reinicia a página cero.
