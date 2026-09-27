# Spec funcional — F-013 Seleccionar atributos y variante del producto

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-013` |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |
| Relacionadas | F-011, F-012 y F-014. |

## 2. Objetivo y alcance

Permite elegir una combinación comercial, como talla y color, para resolver su `sku` vendible dentro de la ficha. Incluye atributos identificadores, imagen propia de variante y cambio de selección. Excluye precio (`F-012`), stock (`F-014`), carrito y creación administrativa de variantes.

## 3. Reglas y comportamiento

- **RN-F013-01:** `variantId` es interno a Catálogo; el resultado interoperable es siempre `sku`.
- **RN-F013-02:** Marketplace expone sólo variantes comercialmente activas con padre activo. No muestra borradores o inactivas.
- **RN-F013-03:** La selección es válida sólo si corresponde a una combinación existente; cambiar un atributo invalida elecciones incompatibles y exige una combinación válida.
- **RN-F013-04:** Stock no determina qué variante existe ni se replica en Catálogo. F-014 decide su disponibilidad visual; una variante agotada no se confunde con inexistente.
- **RN-F013-05:** Un producto simple usa su SKU base y no presenta selector.

Flujo: al cargar una ficha variable, Marketplace consulta variantes activas; presenta sus atributos; el visitante elige valores; el BFF resuelve una única variante y comunica su `sku` a F-012 y F-014. Si no quedan variantes activas, se presenta producto no disponible, sin exponer estados internos.

| Situación | Resultado |
|---|---|
| Combinación no existente | Valor no seleccionable o mensaje “Esta combinación no está disponible”. |
| Imagen de variante no carga | Se conserva la selección; F-011 aplica respaldo de imagen. |
| Catálogo no responde/contrato inválido | Error recuperable de variantes; no se inventa SKU. |

## 4. Validaciones y aceptación

| Condición | Regla |
|---|---|
| Atributos | Cada atributo identificador tiene un único valor activo seleccionado. |
| Variante | Debe devolver `variantId`, `sku` no vacío, atributos y estado activo. |
| Imagen | Es opcional para el render de selección; si existe debe ser HTTPS permitida. |

- [ ] **CA-F013-01:** Una combinación activa resuelve exactamente un `sku` y actualiza F-012/F-014.
- [ ] **CA-F013-02:** Una combinación inválida no permite continuar con un SKU de otra combinación.
- [ ] **CA-F013-03:** Variantes inactivas o borrador no se exponen al visitante.
- [ ] **CA-F013-04:** El selector no muestra precio, stock ni carrito como parte de su responsabilidad.

## 5. Dependencias y decisiones

Fuente: `SPEC-004` y `EXT-OUT-CAT-02` de Productos y Ofertas. La ruta, auth de canal y OpenAPI externos siguen pendientes en `I-01` / `OPEN-03`.
