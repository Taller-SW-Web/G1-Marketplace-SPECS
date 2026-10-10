# Spec funcional — F-029 Filtrar el historial de pedidos

| Campo | Valor |
|---|---|
| ID | `F-029` |
| Estado | Estado y paginación homologados en H-03; rango de fechas pendiente de contrato externo. |

Permite filtrar el historial propio por estado. El rango de fechas permanece especificado como diseño, pero no se habilita hasta que Ventas publique un contrato equivalente para `/pedidos/me`; excluye búsqueda de otros clientes y filtros administrativos.

- **RN-F029-01:** `from` no puede ser posterior a `to`; fechas se envían ISO y se muestran en zona local.
- **RN-F029-02:** Aplicar filtro reinicia página local a cero (página 1 de Ventas) y conserva ámbito JWT.
- **RN-F029-03:** Cero resultados es válido.

- [ ] **CA-F029-01:** Rango inválido no realiza solicitud.
- [ ] **CA-F029-02:** Restablecer recupera historial sin filtros.
