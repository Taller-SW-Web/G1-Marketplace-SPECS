# Spec funcional — F-012 Visualizar precio, oferta y descuento vigente

> Documento de comportamiento para la región comercial de precio dentro de la ficha. El precio autoritativo pertenece a Pricing del módulo Productos y Ofertas; Marketplace sólo lo consulta y presenta.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-012` |
| Nombre | Visualizar precio, oferta y descuento vigente |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración externa condicionada por `I-01`. |
| Última actualización | `2026-09-27` |
| Especificaciones relacionadas | `F-011`, `F-013` y contrato/UI `F-012`. |

## 2. Objetivo y alcance

### Objetivo

Permitir que el visitante conozca el precio comercial vigente de un SKU en el canal Marketplace, incluyendo una oferta activa y su descuento cuando correspondan, sin inducir a error sobre el precio final de checkout.

### Incluye

- Consulta de precio regular y precio de oferta vigente por `sku`, canal `MARKETPLACE` y momento de consulta.
- Presentación de importe, moneda, oferta activa, descuento porcentual calculado y vigencia visible cuando tenga fecha de fin.
- Estado informativo cuando el producto requiere seleccionar una variante antes de resolver su SKU.
- Estados de carga, precio no disponible y actualización de la región de precio.

### No incluye

- Elegir talla, color u otro atributo; corresponde a `F-013`.
- Stock, reserva o elegibilidad de compra; corresponde a `F-014` y `F-016`.
- Promociones de cesta, cupones, envío, impuestos, total o precio final del pedido; corresponden a `F-023`–`F-025`.
- Crear, modificar, programar o auditar precios u ofertas.

## 3. Actores y permisos

| Actor | Permisos en esta funcionalidad |
|---|---|
| Visitante o cliente autenticado | Consultar y visualizar precio público vigente. |
| Pricing de Productos y Ofertas | Determinar precio regular, oferta, moneda, vigencia y versión. |
| Marketplace BFF | Adaptar y exponer una representación pública, sin calcular ni persistir precios. |

No se requiere sesión para esta lectura comercial.

## 4. Conceptos y datos involucrados

| Concepto | Descripción | Datos relevantes | Dueño |
|---|---|---|---|
| SKU | Identidad comercial que recibe precio. | `sku` | Catálogo de Productos y Ofertas |
| Precio regular | Importe normal vigente. | `regularAmount`, `currency` | Pricing |
| Precio de oferta | Importe reducido opcional vigente. | `saleAmount` | Pricing |
| Vigencia | Intervalo temporal de la cotización. | `validFrom`, `validUntil` | Pricing |
| Versión de precio | Referencia técnica para detectar cambio. | `priceVersion` | Pricing |

`variantId` no reemplaza a `sku`. Para un producto simple se usa su SKU vendible; para uno con variantes, F-013 proporciona el SKU de la alternativa elegida.

## 5. Reglas de negocio

- **RN-F012-01 — Fuente autoritativa:** Marketplace no calcula ni guarda un precio vigente; consume la respuesta de Pricing para SKU, canal y momento consultado.
- **RN-F012-02 — Oferta válida:** sólo se presenta oferta cuando `saleAmount` existe, es positivo, es menor que `regularAmount` y la vigencia incluye el momento de respuesta. La ausencia de oferta no equivale a cero.
- **RN-F012-03 — Descuento:** se muestra `round((regularAmount - saleAmount) / regularAmount × 100)` sólo junto a una oferta válida. No se inventa ni redondea un precio de oferta.
- **RN-F012-04 — Moneda y formato:** se muestra el código ISO recibido y se formatea con configuración `es-PE`. La moneda inicial esperada es `PEN`; una moneda no soportada se muestra con su código ISO sin suponer conversión.
- **RN-F012-05 — Variante requerida:** si el producto posee variantes y todavía no hay `sku` seleccionado, no se muestra un importe potencialmente incorrecto; se indica que debe seleccionarse una opción.
- **RN-F012-06 — Vigencia:** si `validUntil` existe, se comunica la fecha/hora en zona `America/Lima`. Al expirar o recibirse una versión nueva, se reemplaza la oferta por la respuesta vigente.
- **RN-F012-07 — Límite comercial:** el importe de esta ficha es informativo. Cupones, promociones de varias líneas, envío y validaciones posteriores pueden modificar el total final; el precio se revalida en checkout.

## 6. Comportamiento funcional

### Precondiciones

- La ficha descriptiva `F-011` está disponible con un producto comercial activo.
- Existe un SKU resoluble: automáticamente para producto simple o desde la selección futura de `F-013`.
- Marketplace puede consultar Pricing o una caché técnica aún vigente.

### Flujo principal

1. La ficha obtiene o recibe el `sku` aplicable y solicita su precio vigente para `MARKETPLACE` al momento actual.
2. Pricing responde precio regular, moneda, oferta opcional, vigencia y versión.
3. Marketplace valida la respuesta y presenta el precio regular o, si existe una oferta válida, el precio de oferta destacado, el regular como referencia y el descuento.
4. Si la oferta tiene fin, se comunica su vigencia. La siguiente consulta usa la respuesta vigente, no un valor calculado localmente.

### Flujos alternativos y errores

| ID | Situación | Comportamiento esperado |
|---|---|---|
| ALT-F012-01 | Producto con variantes sin SKU elegido. | Se presenta “Selecciona una opción para ver el precio”; no se consulta ni muestra precio de otra variante. |
| ALT-F012-02 | Sólo existe precio regular válido. | Se muestra un único importe; no se reserva espacio para descuento u oferta. |
| ALT-F012-03 | La oferta expira mientras la ficha sigue abierta. | En la próxima actualización o reintento, se reemplaza por el precio vigente; no se garantiza el importe anterior. |
| ERR-F012-01 | Pricing no responde o expira el tiempo de espera. | Se muestra “Precio no disponible por el momento” con Reintentar; F-011 permanece accesible. |
| ERR-F012-02 | Respuesta con moneda, importes o vigencia inválidos. | No se muestra un importe parcial; se registra el incidente y se presenta el estado recuperable. |
| ERR-F012-03 | SKU no tiene precio comercial vigente o dejó de ser elegible. | Se muestra “Precio no disponible”; no se traduce en precio cero ni disponibilidad de compra. |

### Estados

| Estado | Cuándo aplica | Transiciones permitidas |
|---|---|---|
| `WAITING_FOR_VARIANT` | Falta SKU de un producto con variantes. | `LOADING` al recibir SKU. |
| `LOADING` | Se consulta o actualiza el precio. | `REGULAR`, `SALE`, `UNAVAILABLE`. |
| `REGULAR` | Hay precio regular vigente sin oferta válida. | `LOADING`. |
| `SALE` | Hay oferta válida. | `LOADING`, `REGULAR` al expirar. |
| `UNAVAILABLE` | Falló o no existe una respuesta comercial válida. | `LOADING` al reintentar. |

## 7. Validaciones

| Campo o condición | Regla | Resultado |
|---|---|---|
| `sku` | No vacío y corresponde al producto/variante elegible. | Si no se puede resolver, se usa `WAITING_FOR_VARIANT` o `UNAVAILABLE`. |
| `regularAmount` | Número decimal mayor que cero. | Respuesta inválida si no cumple. |
| `saleAmount` | Nulo o decimal mayor que cero y menor que el regular. | Si es inválido, se rechaza la respuesta completa. |
| `currency` | Código ISO 4217 de tres letras. | Respuesta inválida si no cumple. |
| Vigencia | `validFrom` no posterior a `validUntil`; oferta sólo vigente en el momento consultado. | Oferta inválida no se presenta. |

## 8. Criterios de aceptación

- [ ] **CA-F012-01:** Un SKU simple con precio regular válido presenta el importe y moneda sin promoción ficticia.
- [ ] **CA-F012-02:** Un SKU con oferta vigente presenta importe de oferta, regular de referencia y descuento calculado según RN-F012-03.
- [ ] **CA-F012-03:** Una oferta ausente, vencida o con importe no menor al regular no se presenta como descuento.
- [ ] **CA-F012-04:** Un producto con variantes sin selección no muestra el precio de una variante arbitraria.
- [ ] **CA-F012-05:** Un error de Pricing no oculta la información descriptiva de F-011 y permite reintentar sólo esta consulta.
- [ ] **CA-F012-06:** La ficha no promete que este importe incluya cupón, envío ni total de checkout.

## 9. Restricciones y requisitos de calidad

- **Rendimiento:** objetivo p95 de la región de precio ≤ 1.5 s bajo integración normal; su carga no bloquea F-011.
- **Accesibilidad:** el precio actual, referencia, descuento y vigencia se anuncian en texto; no dependen sólo de tachado o color.
- **Seguridad y observabilidad:** no se exponen reglas internas de Pricing. Registrar `requestId`, `sku` pseudotécnico, `priceVersion`, origen y latencia, nunca tokens.
- **Caché:** puede usarse caché técnica de corta duración dentro de la vigencia recibida; no debe servir una oferta más allá de `validUntil`.

## 10. Dependencias e integraciones

| Dependencia | Motivo | Estado |
|---|---|---|
| Productos y Ofertas — Pricing | Precio regular/oferta, moneda y vigencia por SKU y canal. | Semántica `EXT-OUT-PRICE-01` documentada; ruta/auth final pendiente en `I-01` / `OPEN-03`. |
| F-011 | Resuelve el producto y conserva la ficha visible. | Aprobada. |
| F-013 | Entrega el SKU de una variante seleccionada. | Aprobada para planificación; requiere la misma homologación externa `I-01` para integración real. |

## 11. Fuentes y decisiones pendientes

- Fuente: `Contrato_Api.md`, `EXT-OUT-PRICE-01`; Pricing es dueño de precio regular/oferta, moneda y vigencias.
- Fuente: `Modelo_Conceptual.md`, responsabilidad de Pricing.
- Pendiente `I-01` / `OPEN-03`: homologar ruta de consulta corriente por SKU/canal, autenticación servicio-a-servicio, errores y OpenAPI de Productos y Ofertas antes de implementación integrada.
