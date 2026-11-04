# Spec funcional — F-030 Visualizar detalle de pedido

| Campo | Valor |
|---|---|
| ID | `F-030` |
| Estado | Proyección local minimizada implementada; integración/pruebas de `I-03` pendientes. |

Muestra detalle de un pedido propio: líneas históricas, importes, estado, dirección resumida e historial de estados. Excluye modificar pedido, seguimiento de Despacho (F-032) y datos de pago sensibles.

La respuesta de G5 consultada publica el total del pedido y el precio unitario/cantidad por línea, pero no un desglose autoritativo de subtotal, descuentos y costo de envío. Hasta que G5 publique esos importes o Producto apruebe una derivación, la implementación presenta total y líneas históricas; no calcula ni inventa componentes del desglose visual de V-016.

La proyección de entrega conserva sólo distrito/provincia/departamento, correo parcialmente enmascarado, últimos tres dígitos del teléfono y fecha estimada. Omite calle, referencia, documento e identificadores de contacto.

- **RN-F030-01:** Ventas autoriza propiedad; Marketplace no usa `orderId` como permiso suficiente.
- **RN-F030-02:** Se presentan snapshots históricos, no información vigente de catálogo.
- **RN-F030-03:** Dirección y contacto se minimizan; no se expone documento ni tarjeta.

- [ ] **CA-F030-01:** Pedido ajeno responde no disponible sin filtrar existencia.
- [ ] **CA-F030-02:** El detalle conserva precios históricos aunque catálogo cambie.
