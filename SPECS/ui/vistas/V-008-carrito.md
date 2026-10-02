# Vista — V-008 Carrito

> Pantalla para revisar el carrito activo, modificar cantidades, quitar líneas, mover productos a favoritos y comenzar el checkout cuando todas las líneas son comprables.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-008` |
| Nombre | Carrito |
| Ruta | `/carrito` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Sebastián Malca |
| Revisor | Diego Espinoza |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** revisar los productos que desea comprar, corregir cantidades o líneas y avanzar al checkout con un carrito válido.
- **Actor principal:** visitante con carrito anónimo o cliente autenticado con carrito activo.
- **Permiso:** lectura y gestión para ambos; mover a favoritos y avanzar al checkout requieren sesión.
- **Condición de entrada:** icono de carrito, `O-005`, reordenado o URL directa.
- **Resultado esperado:** carrito coherente y sin líneas de atención antes de abrir `V-010`; visualizar no reserva ni consume inventario.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-017` | [`Cambiar cantidad`](../../funcional/F-017-cambiar-cantidad-item-carrito.md) | [`UI F-017`](../F-017-cambiar-cantidad-item-carrito.md) | `QuantityStepper`, ajuste por máximo y conflicto. |
| `F-018` | [`Quitar ítem`](../../funcional/F-018-quitar-item-carrito.md) | [`UI F-018`](../F-018-quitar-item-carrito.md) | Eliminación idempotente, foco y deshacer. |
| `F-019` | [`Visualizar carrito`](../../funcional/F-019-visualizar-carrito.md) | [`UI F-019`](../F-019-visualizar-carrito.md) | Líneas, subtotal, atención, vacío y checkout. |
| `F-020` | [`Fusionar carrito`](../../funcional/F-020-fusionar-carrito-anonimo.md) | [`UI F-020`](../F-020-fusionar-carrito-anonimo.md) | Resultado de fusión al volver del login. |
| `F-021` | [`Mover a favoritos`](../../funcional/F-021-mover-carrito-favoritos.md) | [`UI F-021`](../F-021-mover-carrito-favoritos.md) | Guardar producto y retirar línea de forma atómica. |

Se consultaron los contratos API `F-017` a `F-021` de `SPECS/contrato-api/`.

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto conservado |
|---|---|---|---|
| Cabecera o `O-005` | `V-008` | Existe o no carrito | Sesión/cookie y versión del carrito. |
| Nombre o imagen de línea | `V-007` | Producto aún disponible | Carrito y retorno a `V-008`. |
| “Explorar productos” | `V-006` | Carrito vacío o decisión del usuario | Carrito activo aunque esté vacío. |
| “Iniciar checkout” | `V-010` | Sesión activa y todas las líneas válidas | Carrito/version vigente. |
| Checkout sin sesión | `O-003` → `V-001` | Visitante pulsa CTA | Retorno a `V-008` e intención de checkout. |
| “Mover a favoritos” sin sesión | `O-003` → `V-001` | Visitante solicita acción protegida | SKU/línea e intención; no se modifica antes de autenticar. |
| Login exitoso | `V-008` | Existía carrito anónimo | Carrito final fusionado o error recuperable de F-020. |

## 5. Jerarquía y composición visual

```text
V-008 Carrito
├── Cabecera global
├── Encabezado “Tu carrito” + cantidad de líneas/unidades
├── Avisos de fusión o cambios
├── Contenido
│   ├── Lista semántica de CartLine
│   │   ├── Imagen, nombre y variante
│   │   ├── Precio unitario/snapshot
│   │   ├── QuantityStepper
│   │   ├── Subtotal de línea
│   │   ├── Estado de atención
│   │   ├── Quitar
│   │   └── Mover a favoritos
│   └── OrderSummary
│       ├── Subtotal informativo
│       ├── Nota de envío/descuentos
│       └── “Iniciar checkout”
└── Estado vacío, cuando corresponda
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Lista | Una `CartLine` por SKU | Primaria | Actualizaciones locales por línea; no bloquea otras líneas salvo conflicto global. |
| Cantidad | Disminuir, campo y aumentar | Primaria | Reemplazo absoluto 1–99; disminuir se deshabilita en 1. |
| Atención | Precio cambiado, sin precio, agotado o datos pendientes | Primaria | Se anuncia antes del resumen y bloquea checkout hasta corregir. |
| Acciones de línea | Quitar / mover a favoritos | Secundaria | No comparten el mismo resultado; ambas conservan foco correctamente. |
| Resumen | Subtotal y CTA | Primaria | No muestra cupón, envío, impuestos ni total final. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Tu carrito” | — | Siempre. |
| Línea | Imagen, nombre, variante/SKU comprensible | Abrir `V-007` | Línea existente. |
| Precio | Precio unitario vigente o snapshot marcado | — | Disponible; nunca precio ficticio. |
| Cantidad | Valor confirmado | Aumentar/disminuir/editar | Línea comprable o ajustable. |
| Quitar | “Quitar {producto}” | Eliminar línea | Siempre por línea. |
| Mover | “Mover a favoritos” | F-021 o autenticar | Por línea; operación sólo con sesión. |
| Atención | Motivo comprensible | Reintentar, quitar o volver a producto | Línea no comprable/incompleta. |
| Subtotal | Suma de cantidades × precio vigente | — | Todas las líneas tienen precio. |
| Nota | “No incluye envío ni descuentos” | — | Con subtotal. |
| CTA | “Iniciar checkout” | Abrir `V-010` o autenticar | Carrito con líneas válidas. |
| Vacío | “Tu carrito está vacío” | Abrir catálogo | Sin líneas. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Lectura/enriquecimiento inicial | Skeleton de líneas y resumen; sin importes falsos | Esperar | Sí |
| Válido anónimo | Líneas comprables, sin sesión | Lista/subtotal; CTA requiere autenticación | Iniciar sesión/seguir editando | Sí |
| Válido autenticado | Líneas comprables y sesión | Lista/subtotal; checkout activo | Abrir `V-010` | Sí |
| Vacío | `items: []` | Mensaje e invitación; sin resumen ni CTA activo | Explorar catálogo | Sí |
| Atención | Una o más líneas sin precio, agotadas o pendientes | Línea identificada; subtotal puede ser nulo; CTA bloqueado con explicación | Corregir/quitar/reintentar | Sí |
| Actualizando cantidad | `PATCH` en curso | Sólo línea ocupada; valor solicitado distinguible del confirmado | Esperar | Sí, variante de línea |
| Cantidad ajustada | Límite de stock | Valor confirmado y aviso del máximo sin saldo interno | Aceptar/editar/quitar | Sí |
| Error de cantidad | Validación, conflicto o proveedor | Se restaura valor confirmado; mensaje y reintento | Reintentar/actualizar | Sí |
| Quitando | Eliminación solicitada | Línea retirada visualmente y `O-006` disponible | Deshacer | Sí, con overlay |
| Eliminación rechazada | Servidor no confirma | Línea restaurada y error anunciado | Reintentar | Sí |
| Moviendo a favoritos | Operación autenticada en curso | Línea ocupada; no se retira todavía como éxito definitivo | Esperar | Sí, variante |
| Movido/ya favorito | Transacción confirmada | Línea retirada; mensaje correspondiente | Ver favoritos/continuar | Sí, con feedback |
| Error al mover | Favorito o catálogo falla | Línea permanece y mensaje de reintento | Reintentar | Sí |
| Fusionando | Regreso de login con carrito anónimo | Mensaje “Actualizando tu carrito”; no aparecen dos carritos | Esperar | Sí |
| Fusión ajustada | Cantidades limitadas | `O-007` resume ajustes; líneas resaltadas una vez | Revisar | Se diseña en `O-007` |
| Fusión fallida | Error antes del commit | Sesión activa, mensaje y reintento; no se afirma pérdida | Reintentar | Sí |
| Error de carga | No hay representación coherente | Mensaje general; no se borra visualmente por asumir vacío | Reintentar/explorar | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Checkout o mover a favoritos sin sesión | Login conserva carrito e intención; cancelar mantiene `V-008`. |
| `O-006` | Deshacer eliminación | Una línea fue retirada | Deshacer dentro de 5 segundos o cerrar/expirar. |
| `O-007` | Resultado de fusión | Fusión con ajustes o información relevante | Cerrar y revisar líneas; no solicita resolver duplicados. |
| `O-010` | Alertas y feedback global | Conflicto o error no contenido en una línea | Reintentar/actualizar. |

## 9. Formularios y validación visual

| Campo/control | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Cantidad | Entero/stepper | Sí | 1–99 y no mayor al máximo confirmado | Ajuste o error junto a la línea | Default/foco/ocupado/ajustado/error |

Cantidad cero nunca elimina: en 1, disminuir queda deshabilitado y la acción “Quitar” permanece separada. Cambiar cantidad envía un valor absoluto, no un incremento relativo.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Lista a la izquierda y `OrderSummary` a la derecha con ancho estable.
- El resumen puede permanecer visible dentro de su columna sólo si no tapa pie, avisos ni controles.
- Cada línea alinea imagen, identidad, cantidad, precio y acciones sin depender de hover.

### Mobile

- **Referencia:** 390 px.
- Línea apilada: imagen/identidad, variante, precio, cantidad y acciones.
- Resumen aparece después de todas las líneas; no se fija un CTA que oculte controles o mensajes.
- Acciones “Quitar” y “Mover” conservan objetivos separados y etiquetas completas.

### Anchuras intermedias

- El resumen pasa debajo de la lista cuando ambas columnas dejan de conservar ancho legible.
- Precios y cantidades no se truncan; las acciones pueden pasar a una fila propia.

## 11. Accesibilidad

- El carrito es una lista semántica; cada línea tiene encabezado con nombre del producto.
- El stepper tiene etiqueta “Cantidad de {producto}”, botones de 44 px y valor editable por teclado.
- Cambios de cantidad/subtotal se anuncian sin mover foco; valor solicitado y confirmado se distinguen.
- Tras quitar, el foco pasa a la siguiente línea, anterior o título del carrito; nunca queda en un nodo eliminado.
- `O-006` es alcanzable sin robar permanentemente el foco y anuncia el tiempo disponible sin exigir leer un contador animado.
- Una línea de atención se anuncia antes del CTA y no depende sólo de color.
- El CTA deshabilitado tiene explicación visible/asociada.
- Importes indican moneda y contexto; subtotal no se anuncia como total final.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-008 / Desktop / Válido autenticado` | Desktop | Principal | Lista + resumen en dos columnas. |
| `V-008 / Mobile / Válido anónimo` | Mobile | Principal | CTA interceptado por acceso. |
| `V-008 / Desktop / Cargando` | Desktop | Skeleton | Líneas y resumen. |
| `V-008 / Mobile / Vacío` | Mobile | Vacío | Una salida al catálogo. |
| `V-008 / Desktop / Atención` | Desktop | No comprable | Línea marcada, subtotal/checkout bloqueados. |
| `V-008 / Mobile / Cantidad actualizando` | Mobile | Progreso local | Stepper ocupado. |
| `V-008 / Desktop / Cantidad ajustada` | Desktop | Límite | Solicitado vs confirmado. |
| `V-008 / Mobile / Error de cantidad` | Mobile | Error local | Valor restaurado y reintento. |
| `V-008 / Desktop / Moviendo a favoritos` | Desktop | Progreso | Línea conservada hasta confirmación. |
| `V-008 / Mobile / Fusión fallida` | Mobile | Error recuperable | Sesión activa y reintento. |
| `V-008 / Desktop / Error de carga` | Desktop | Error total | Reintento sin falso vacío. |

Los overlays `O-003`, `O-006` y `O-007` se diseñan en sus propias specs.

## 13. Criterios de aceptación visual

- [ ] `UI-V008-001`: Carrito vacío no muestra subtotal ni acción de checkout activa.
- [ ] `UI-V008-002`: Subtotal se identifica como informativo y excluye envío/descuentos; nunca se presenta como total final.
- [ ] `UI-V008-003`: Una línea sin precio o agotada permanece visible, explica el problema y bloquea checkout hasta corregirse.
- [ ] `UI-V008-004`: Cantidad admite 1–99, usa reemplazo absoluto y nunca convierte cero en eliminación.
- [ ] `UI-V008-005`: Quitar permite deshacer, restaura la línea si falla y mantiene el foco en un elemento existente.
- [ ] `UI-V008-006`: Mover a favoritos no retira la línea hasta confirmar ambas mutaciones y autentica antes de cambiar el carrito.
- [ ] `UI-V008-007`: Tras login existe un único carrito visible; ajustes y fallos de fusión son comprensibles.
- [ ] `UI-V008-008`: Desktop y mobile mantienen controles accesibles y el resumen no oculta líneas ni avisos.
- [ ] La vista aplica `DS-001`, `CartLine`, `QuantityStepper` y `OrderSummary`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-008-OPEN-01` | Definir la operación técnica que materializa “Deshacer” después del `DELETE` y su comportamiento ante cambios de stock/precio. | Backend + UX | Antes del diseño final | Abierta |
| `V-008-OPEN-02` | Confirmar si el resumen desktop será sticky y sus límites de desplazamiento. | UX/UI | Antes del diseño final | Abierta |
| `V-008-OPEN-03` | Definir el copy y la recuperación para cada valor de `attention` devuelto por el carrito. | Backend + UX | Antes del diseño final | Abierta |
| `V-008-OPEN-04` | Homologar consultas externas de precio/disponibilidad usadas para enriquecer líneas (`I-01`). | Backend + módulos dueños | Antes de implementación; informar diseño | Abierta |
