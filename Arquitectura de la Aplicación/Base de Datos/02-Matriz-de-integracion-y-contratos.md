# Matriz de integración y contratos — Marketplace

## 1. Regla de lectura

Esta matriz refleja lo encontrado el 27 de septiembre de 2026 en los repositorios de los módulos dueños. `Confirmado` significa que existe una ruta y payload documentados; `Semántico/TBD` significa que existe la intención y el esquema mínimo, pero aún no un OpenAPI/ruta definitiva; `Pendiente` requiere acuerdo entre equipos antes de implementar.

| Módulo dueño | Datos que Marketplace necesita | Interfaz encontrada | Identificadores | Estado y decisión para Marketplace |
| --- | --- | --- | --- | --- |
| Seguridad y Usuarios | Registro, login, recuperación, identidad y direcciones del cliente. | `POST /auth/registro`, `/auth/login`, `/password/recuperar`, `/password/restablecer`, `GET/POST /usuarios/{id}/direcciones`. | UUID de usuario y `addressId`. | **Confirmado.** La interfaz de direcciones permite acceso con token del titular. Marketplace no necesita una tabla de direcciones. |
| Productos y Ofertas | Catálogo, categorías, marcas, variantes, precios, stock, promociones, cupón y recomendados. | Contrato semántico EXT-OUT-CAT/PRICE/PROMO/COUPON/INV/REC. Varias rutas están `TBD`. | `productId`, `variantId`, `sku`. | **Semántico/TBD.** Usar `sku` como llave de carrito e integración; no implementar endpoint final hasta homologar OpenAPI. |
| Despacho y Entrega | Cobertura, costo/plazo de envío y seguimiento. | `POST /api/v1/cotizaciones`, `GET /api/v1/seguimientos/pedidos/{idPedido}`. | `sku`, `idPedido`. | **Confirmado.** Marketplace requiere token de servicio con `cotizaciones:calcular` y `seguimientos:leer`. |
| Ventas y Postventa | Crear pedido, historial, detalle, reorder y CSAT. | `POST /api/v1/pedidos`, `GET /api/v1/pedidos`, `GET /api/v1/pedidos/{pedidoId}`, `POST /api/v2/csat`. | `pedidoId`, `clienteId`, `sku`. | **Parcial.** Las rutas existen, pero historial, idempotencia y CSAT requieren ajustes descritos en el documento 03. |

## 2. Matriz por necesidad funcional

| Funcionalidades Marketplace | Operación externa | Datos que salen de Marketplace | Datos que regresan | Estado |
| --- | --- | --- | --- | --- |
| `F-001`–`F-005` | Seguridad: registro, login, recuperación y restablecimiento. | Datos de formulario; `canalOrigen=MARKETPLACE` en registro. | Estado de cuenta, token/sesión o resultado neutro. | Confirmado. |
| `F-006`–`F-015` | Productos y Ofertas: catálogo, variantes, precio, stock y recomendados. | Filtros, `productId`, `sku`, canal. | Productos activos, atributos, variantes, precios, disponibilidad, recomendaciones. | Semántico/TBD. |
| `F-016`–`F-021` | Productos y Ofertas: revalidación de SKU y precio. | `sku`, cantidad. | Disponibilidad, precio vigente. | Semántico/TBD. Persistencia de carrito/favoritos es local. |
| `F-022` | Seguridad: consultar/registrar dirección del titular. | Token de usuario y referencia de usuario. | Dirección con distrito, provincia, departamento, referencia y `addressId`. | Confirmado; no se replica localmente. |
| `F-023` | Despacho: cotización exacta; Productos y Ofertas: precios/promociones. | Destino y líneas `{sku, cantidad}`. | Cobertura, costo, moneda PEN, plazo y fecha estimada. | Despacho confirmado; precio/promoción semántico/TBD. |
| `F-024` | Productos y Ofertas: validación sin consumo de cupón. | Código, cliente si aplica, canal y líneas. | Validez, motivo, descuento, total. | Semántico/TBD. |
| `F-025`–`F-027` | Productos y Ofertas revalida; Ventas crea pedido. | SKU, cantidad, snapshot de precio/cupón, copia de dirección, cotización, clave de idempotencia. | Disponibilidad final, `pedidoId`, estado de creación. | Parcial; falta homologar idempotencia con Ventas. |
| `F-028`–`F-031` | Ventas y Postventa: historial, detalle y recompra. | JWT del cliente, filtros y `pedidoId`. | Pedidos propios, líneas históricas y estado. | Parcial; se debe reemplazar `clienteId` como query por identidad desde JWT. |
| `F-032` | Despacho: seguimiento por pedido. | `idPedido`. | Estado, hitos, fecha estimada e incidencias. | Confirmado. |
| `F-033`–`F-035` | Ventas y Despacho como emisores de cambios; proveedor de correo. | Según evento homologado. | Evento `OrderCreated` o actualización de despacho. | Pendiente de homologar una interfaz de eventos consumible por el servicio de notificaciones de Marketplace. |
| `F-040` | Ventas y Postventa: CSAT. | `pedidoId`, identidad autenticada y respuesta UX. | Confirmación de encuesta aceptada o ya existente. | Parcial; payload actual no contiene motivos ni la condición de pedido entregado. |

## 3. Contratos confirmados que condicionan el modelo

### 3.1 Cotización de envío

Despacho recibe `destino.distrito` y, para una cotización exacta, líneas por `{sku, cantidad}`. Devuelve cobertura, costo, moneda, plazo y fecha estimada. La cotización no crea pedido ni reserva stock. Por tanto Marketplace no guarda una entidad `ShippingRate`: la cotización se consulta de nuevo cuando sea necesario y se manda a Ventas sólo como dato de la orden aprobada.

### 3.2 Dirección del cliente

Seguridad publica direcciones con `id`, `departamento`, `provincia`, `distrito`, `direccion`, `referencia` y `esPredeterminada`. Marketplace consulta o registra la dirección en Seguridad usando el token del usuario; para la orden se transmite una copia de los campos de entrega a Ventas, sin asumir que `addressId` exista allí.

### 3.3 Producto y variante

Productos y Ofertas diferencia `variantId` de `sku`: el primero es identidad interna de Catálogo y el segundo es identidad comercial para precio, stock, cotización y Ventas. Esto respalda el modelo `CartItem(cartId, sku)` y evita tratar el `variantId` como un ID universal.

### 3.4 Seguimiento

Marketplace consulta a Despacho exclusivamente por `idPedido`. El evento de cambio de despacho actualmente se entrega de Despacho a Ventas y Postventa; Marketplace no debe asumir acceso directo a la base de datos ni a eventos internos de Despacho.

## 4. Seguridad y minimización de datos

- Las llamadas del navegador a Seguridad usan el token del titular; Marketplace no intercambia ni persiste contraseñas.
- Las llamadas servidor a servidor a Despacho requieren token de servicio y los scopes publicados por Despacho.
- Las direcciones, tarjetas, CVV, tokens JWT, respuestas completas de proveedores y documentos de identidad no se almacenan en la base local de Marketplace.
- Las referencias externas no llevan FK física; su vigencia se verifica mediante su API dueña.
