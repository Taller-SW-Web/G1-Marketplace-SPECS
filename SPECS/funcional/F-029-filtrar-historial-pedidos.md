# Spec funcional — F-029 Filtrar el historial de pedidos

| Campo | Valor |
|---|---|
| ID | `F-029` |
| Estado | Aprobada para planificación; depende de `I-03`. |

Permite filtrar el historial propio por estado y rango de fechas. Incluye validación de rango y restablecer; excluye búsqueda de otros clientes y filtros administrativos.

- **RN-F029-01:** `from` no puede ser posterior a `to`; fechas se envían ISO y se muestran en zona local.
- **RN-F029-02:** Aplicar filtro reinicia página a cero y conserva ámbito JWT.
- **RN-F029-03:** Cero resultados es válido.

- [ ] **CA-F029-01:** Rango inválido no realiza solicitud.
- [ ] **CA-F029-02:** Restablecer recupera historial sin filtros.
