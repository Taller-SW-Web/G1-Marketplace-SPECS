# Spec funcional — F-023 Calcular y mostrar resumen de compra y envío

| Campo | Valor |
|---|---|
| ID | `F-023` |
| Estado | Aprobada para planificación; requiere scopes de Despacho e `I-01` para precios/promociones. |

Calcula una cotización temporal a partir de líneas válidas y dirección seleccionada: subtotal revalidado, promociones automáticas, costo/plazo de envío y total estimado. Excluye cupón manual (`F-024`), pago y creación de orden.

- **RN-F023-01:** Despacho cotiza con destino y `{sku,cantidad}`; Marketplace usa cliente técnico con `cotizaciones:calcular`.
- **RN-F023-02:** Precio/promoción/stock se revalidan con sus dueños; cotización no reserva stock, precio ni capacidad de despacho.
- **RN-F023-03:** Resumen indica vigencia y es estimado hasta F-025/F-026.
- **RN-F023-04:** Sin cobertura o línea inválida bloquea continuar y señala qué corregir.

- [ ] **CA-F023-01:** Cambiar dirección o carrito invalida la cotización previa.
- [ ] **CA-F023-02:** Costo/plazo provienen de Despacho, no de cálculo local.
- [ ] **CA-F023-03:** Error de cotización no se presenta como envío gratis.
