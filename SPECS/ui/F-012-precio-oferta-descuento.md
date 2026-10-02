# Spec UI — F-012 Visualizar precio, oferta y descuento vigente

> Define la región comercial de precio de la ficha. Usa `DS-001` y se compone con F-011; no define controles de variante, stock, carrito ni cupón.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID funcional | `F-012` |
| Nombre | Visualizar precio, oferta y descuento vigente |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración externa condicionada por `I-01`. |
| Spec funcional relacionada | `../funcional/F-012-precio-oferta-descuento.md` |
| Sistema de diseño aplicado | `DS-001-sistema-diseno-marketplace.md` v`0.1.0` |
| Prototipo oficial | Pendiente de crear en Figma. |
| Última actualización | `2026-09-27` |

## 2. Pantallas y rutas

| Pantalla | Ruta | Entrada | Salida o destino |
|---|---|---|---|
| Ficha de producto — región de precio | `/productos/{slug}` | Carga de F-011 o cambio futuro de variante. | Se mantiene en la misma ficha. |

## 3. Estructura visual

La región sigue el patrón **Resumen comercial de producto** de `DS-001`.

```text
Resumen descriptivo de F-011
├── Marca y nombre
├── Región F-012: Precio
│   ├── Etiqueta de oferta (si aplica)
│   ├── Precio actual
│   ├── Precio regular de referencia (si aplica)
│   ├── Porcentaje de descuento (si aplica)
│   └── Vigencia de oferta (si aplica)
├── Región futura F-013: variante
└── Regiones futuras F-014 a F-016
```

## 4. Componentes y contenido

| Componente | Contenido | Acción | Visibilidad |
|---|---|---|---|
| `PriceDisplay` | Precio vigente y moneda. | No interactivo. | Precio regular u oferta válida. |
| `SaleBadge` | “Oferta” y porcentaje de descuento. | No interactivo. | Sólo oferta válida. |
| Precio regular de referencia | Importe original con indicación textual de referencia. | No interactivo. | Sólo oferta válida. |
| Vigencia | “Oferta válida hasta …”. | No interactivo. | Sólo si `validUntil` existe. |
| Estado de variante | “Selecciona una opción para ver el precio”. | Dirige visualmente al selector futuro, sin simularlo. | Producto con variantes y sin SKU. |
| Estado no disponible | Mensaje y botón `Reintentar`. | Reintentar precio. | Error o respuesta no comercializable. |
| Skeleton de precio | Bloques neutros de importe y vigencia. | Ninguna. | Cargando. |

## 5. Estados de la interfaz

| Estado | Elementos visibles | Acción |
|---|---|---|
| Cargando | Skeleton; sin importes falsos. | Ninguna. |
| Precio regular | Importe actual y moneda. | Ninguna. |
| Oferta vigente | Importe actual, regular de referencia, badge y vigencia si existe. | Ninguna. |
| Selección requerida | Mensaje claro sin importe. | Esperar selección de F-013. |
| Precio no disponible | Mensaje neutral y Reintentar. | Reintentar F-012. |

## 6. Interacciones y navegación

1. Al obtener un SKU aplicable, la región pasa de carga a precio regular, oferta o no disponible.
2. Al cambiar el SKU desde F-013, se reemplaza la región por skeleton y se consulta el precio de la nueva selección.
3. Al pulsar Reintentar, se repite sólo F-012; la galería y descripción no vuelven a cargarse.
4. Al vencer una oferta durante una actualización, se actualizan conjuntamente importe, referencia, badge y vigencia; no queda un descuento visual huérfano.

## 7. Formularios y validaciones visuales

No hay formulario ni campo editable. Los importes provienen del contrato y no pueden editarse en la ficha.

| Condición | Resultado visual |
|---|---|
| Oferta válida | Precio actual destacado; referencia y descuento acompañantes. |
| Sin oferta | Sólo precio actual; no se muestra “0%” ni precio tachado. |
| Falta SKU de variante | Mensaje de selección requerida; no se muestra precio estimado. |
| Respuesta inválida o fallo | Mensaje de no disponibilidad y Reintentar. |

## 8. Responsive y accesibilidad

- **Desktop/tablet:** se ubica debajo del título en el resumen de la ficha, sin competir con la descripción.
- **Mobile:** se mantiene antes de los selectores futuros y usa líneas separadas para conservar legibilidad de los importes.
- **Lectores de pantalla:** el precio actual se anuncia antes del de referencia; el descuento y fecha se expresan como texto, por ejemplo “Oferta, 15 por ciento de descuento, válida hasta…”.
- **Contraste:** el estado de oferta no depende sólo de verde, rojo, tachado o tamaño; el precio normal de referencia conserva contraste suficiente.
- **Actualización:** cambios de precio se anuncian mediante región `aria-live="polite"` sin mover el foco. Reintentar es un botón con nombre accesible.

## 9. Criterios de aceptación UI

- [ ] **UI-F012-01:** La carga no muestra precio, moneda ni descuento de ejemplo.
- [ ] **UI-F012-02:** Una oferta válida muestra de forma legible precio actual, referencia, descuento y vigencia cuando exista.
- [ ] **UI-F012-03:** Sin oferta, no se renderiza badge, precio tachado ni porcentaje vacío.
- [ ] **UI-F012-04:** Para variantes sin selección, el usuario ve una instrucción clara y no un precio de otra alternativa.
- [ ] **UI-F012-05:** El error de precio permite reintentar sin ocultar la ficha F-011.
- [ ] **UI-F012-06:** El contenido cumple contraste, lectura por tecnologías asistivas y reordenamiento móvil definidos en DS-001.

## 10. Fuentes y decisiones pendientes

- Fuente: `DS-001`, F-011 y `EXT-OUT-PRICE-01` de Productos y Ofertas.
- Pendiente: enlace de prototipo Figma y homologación `I-01` de la consulta externa de precio.
