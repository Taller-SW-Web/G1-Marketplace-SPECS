# Vista — V-011 Resumen, envío y beneficio

> Pantalla autenticada para revisar líneas, dirección, cotización temporal de envío y beneficio promocional antes de preparar el pago simulado.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-011` |
| Nombre | Resumen, envío y beneficio |
| Ruta | `/checkout/resumen` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Jim Segovia |
| Revisor | Fernando José Saire Tello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** comprender el monto estimado, plazo de entrega y beneficio aplicable, y corregir dirección o carrito antes de continuar.
- **Actor principal:** cliente autenticado con dirección seleccionada y carrito válido.
- **Permiso:** privado.
- **Condiciones de entrada:** `addressId`, versión de carrito y sesión vigentes desde `V-010`.
- **Resultado esperado:** `quoteId` temporal vigente —con beneficio seleccionado si aplica— y navegación consciente a `V-012`; la cotización no reserva stock, precio ni despacho.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-023` | [`Calcular resumen y envío`](../../funcional/F-023-calcular-resumen-envio.md) | [`UI F-023`](../F-023-calcular-resumen-envio.md) | Líneas, subtotal, envío, plazo, total estimado y vigencia. |
| `F-024` | [`Validar cupón o promoción`](../../funcional/F-024-validar-aplicar-cupon-promocion.md) | [`UI F-024`](../F-024-validar-aplicar-cupon-promocion.md) | Promoción automática, cupón, recálculo y retiro. |

Contratos consultados: [`API F-023`](../../contrato-api/F-023-calcular-resumen-envio.md) y [`API F-024`](../../contrato-api/F-024-validar-aplicar-cupon-promocion.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| `V-010` → continuar | `V-011` | Dirección propia confirmada | `addressId` y carrito/version. |
| “Editar dirección” | `V-010` | Acción explícita | Carrito; cambiar dirección invalida cotización. |
| “Editar carrito” | `V-008` | Acción explícita | Sesión; cualquier cambio invalida cotización/beneficio. |
| “Continuar al pago simulado” | `V-012` | Cotización vigente y sin atención | `quoteId` opaco y beneficio seleccionado. |
| Sesión vencida | `O-003` → `V-001` | `401` | Retorno condicionado a revalidar dirección, carrito y cotización. |
| Cerrar sesión | `O-004` | Acción durante checkout | Cancelar conserva; confirmar descarta contexto. |

El código de cupón no debe incorporarse en la URL, analítica visible ni logs. La ruta por sí sola no reconstruye una cotización vencida.

## 5. Jerarquía y composición visual

```text
V-011 Resumen, envío y beneficio
├── Cabecera de checkout + progreso
├── Encabezado “Revisa tu pedido”
├── Contenido principal
│   ├── Lista resumida de líneas
│   ├── Dirección de entrega + Editar
│   ├── Plazo de entrega estimado
│   ├── Promociones automáticas
│   ├── Cupón manual
│   └── Avisos de cambios/atención
├── Resumen económico
│   ├── Subtotal
│   ├── Descuento seleccionado
│   ├── Envío
│   ├── Total estimado
│   └── Vigencia
└── Volver / Continuar al pago simulado
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Líneas | Producto, variante, cantidad y precio revalidado | Primaria | Sólo revisión; edición vuelve a `V-008`. |
| Dirección | Resumen mínimo de entrega | Primaria | Editar vuelve a `V-010` e invalida quote. |
| Cotización | Envío, plazo, importes y vigencia | Primaria | Todo monto proviene de servicios dueños; no inventar cero. |
| Beneficios | Automáticos y cupón | Secundaria | Se distinguen; sólo el elegido afecta el total. |
| Total | “Total estimado” | Primaria | No se presenta como cargo ni total definitivo. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Revisa tu pedido” | — | Siempre. |
| Línea | Nombre, variante, cantidad, unitario/subtotal | Editar carrito | Cotización válida o atención. |
| Dirección | Dirección resumida y teléfono enmascarado | Editar dirección | Dirección seleccionada. |
| Plazo | “Entrega estimada en {n} días” | — | Despacho lo devuelve. |
| Subtotal | Importe revalidado | — | Cotización válida. |
| Descuento automático | Nombre comprensible e importe | — | Beneficio automático elegido. |
| Cupón | “Código de cupón” | Ingresar/aplicar | Cotización vigente. |
| Cupón aplicado | Código parcialmente oculto, ahorro y “Quitar” | Recalcular sin cupón | Cupón elegido. |
| Envío | Importe o “Envío gratis” | — | Sólo costo válido; “gratis” sólo si Despacho devuelve cero. |
| Total | “Total estimado” | — | Cotización válida. |
| Vigencia | “Cotización válida hasta…” o explicación equivalente | Recalcular al vencer | Siempre que exista quote. |
| CTA | “Continuar al pago simulado” | Abrir `V-012` | Quote vigente y sin atención. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Calculando | Entrada/cambio que invalida quote | Skeleton de importes y texto “Calculando tu envío”; sin montos ficticios | Esperar | Sí |
| Cotizado sin cupón | `200` de F-023 | Desglose, plazo, vigencia y campo cupón | Continuar/aplicar | Sí |
| Cotizado con promoción automática | Beneficio automático | Bloque identificado y descuento en desglose | Continuar/aplicar cupón si está permitido | Sí |
| Validando cupón | Solicitud F-024 | Campo y botón ocupados; desglose vigente distinguible | Esperar | Sí |
| Cupón aplicado | Beneficio seleccionado | Código parcialmente visible, ahorro, nuevo quote y Quitar | Continuar/quitar | Sí |
| Cupón no aplicable | `422` | Mensaje neutral junto al campo; quote anterior sigue comprensible | Corregir/continuar sin cupón | Sí |
| Cupón inválido | `400` | Error de formato asociado al campo | Corregir | Sí |
| Cotización vencida | `409 QUOTE_EXPIRED` o tiempo alcanzado | Montos marcados no vigentes; CTA bloqueado | Recalcular | Sí |
| Carrito cambió | `409 CART_CHANGED` | Línea/cambio identificado si está disponible; quote invalidado | Volver al carrito/recalcular | Sí |
| Línea no disponible | `409 LINE_NOT_AVAILABLE` | Atención sobre línea y avance bloqueado | Corregir en `V-008` | Sí |
| Sin cobertura | `409 NO_SHIPPING_COVERAGE` | No se muestra envío cero; explicación y edición de dirección | Editar `V-010` | Sí |
| Error de cotización | `503` u otro fallo | No se inventan importes; criterios preservados | Reintentar | Sí |
| Error de beneficios | Servicio de promociones falla | Cotización base permanece si sigue vigente; no se inventa descuento | Reintentar/continuar según regla aprobada | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Sesión ausente/vencida | Login y revalidación completa del checkout. |
| `O-004` | Confirmar cierre de sesión | Cerrar sesión durante checkout | Cancelar o descartar flujo. |
| `O-010` | Alertas y feedback global | Cambio global de carrito/quote o error no asociado al cupón | Recalcular, volver o cerrar. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Código de cupón | Texto | No | Formato y longitud del contrato; normalización sólo para consulta | No revelar límites/estado de otros clientes | Default/foco/error/aplicado |

Aplicar no consume el cupón. Quitar sólo solicita una nueva cotización sin ese código; no “devuelve” un uso porque aún no existe consumo.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Contenido de líneas/dirección/beneficios y resumen económico en dos columnas.
- El resumen puede ser sticky con límites; nunca oculta vigencia, errores o pie.
- Etiquetas e importes se alinean sin depender sólo de posición para comunicar signo/descuento.

### Mobile

- **Referencia:** 390 px.
- Orden: líneas, dirección, plazo, beneficios, desglose, vigencia y CTA.
- Resumen no se separa del contexto; total estimado y vigencia aparecen antes del CTA.
- Campo y botón de cupón se apilan si no conservan ancho/objetivo táctil.
- CTA no queda fijo si tapa mensajes de atención.

### Anchuras intermedias

- El resumen pasa debajo del contenido cuando su columna comprime las líneas o etiquetas.
- Importes usan formato consistente y no se truncan.

## 11. Accesibilidad

- El desglose usa pares etiqueta–importe con lectura ordenada; descuento expresa el signo y el motivo.
- “Total estimado” y vigencia se anuncian juntos; no se anuncia como cobro.
- El resultado de cotización/beneficio usa `aria-live="polite"` sin desplazar el foco.
- Errores del cupón se asocian al campo; cambios generales llegan a un resumen de atención.
- “Envío gratis” incluye texto, no sólo importe `0` o color.
- Al vencer, el CTA queda no disponible con explicación y foco accesible en “Recalcular”.
- Los enlaces Editar indican destino y consecuencia cuando invalidan cotización.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-011 / Desktop / Cotizado` | Desktop | Principal | Dos columnas y desglose. |
| `V-011 / Mobile / Cotizado` | Mobile | Principal | Orden apilado. |
| `V-011 / Desktop / Calculando` | Desktop | Skeleton | Sin importes. |
| `V-011 / Mobile / Promoción automática` | Mobile | Beneficio | Diferencia con cupón. |
| `V-011 / Desktop / Cupón aplicado` | Desktop | Éxito | Código parcial, ahorro, quitar. |
| `V-011 / Mobile / Cupón no aplicable` | Mobile | Error de campo | Quote conservado. |
| `V-011 / Desktop / Cotización vencida` | Desktop | Conflicto | Recalcular y CTA bloqueado. |
| `V-011 / Mobile / Sin cobertura` | Mobile | Atención | Editar dirección. |
| `V-011 / Desktop / Línea no disponible` | Desktop | Atención | Editar carrito. |
| `V-011 / Mobile / Error de cotización` | Mobile | Error | Reintento sin montos ficticios. |

## 13. Criterios de aceptación visual

- [ ] `UI-V011-001`: Cada importe tiene etiqueta y el total se denomina siempre “estimado”.
- [ ] `UI-V011-002`: Envío gratis sólo aparece cuando Despacho entrega un costo cero válido; los errores nunca se presentan como cero.
- [ ] `UI-V011-003`: Cambiar dirección o carrito invalida visualmente la cotización y obliga a recalcular.
- [ ] `UI-V011-004`: Promoción automática y cupón manual son distinguibles; sólo el beneficio seleccionado afecta el desglose.
- [ ] `UI-V011-005`: Validar/quitar un cupón no afirma consumo o restitución.
- [ ] `UI-V011-006`: Cotización vencida, sin cobertura y línea no disponible bloquean avance y ofrecen la corrección adecuada.
- [ ] `UI-V011-007`: Desktop y mobile muestran vigencia antes del CTA y no ocultan cambios revalidados.
- [ ] La vista aplica `DS-001` y reutiliza `OrderSummary`, alertas y formularios aprobados.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-011-OPEN-01` | Homologar scopes y contrato de cotización con Despacho, Pricing, Promociones e Inventario. | Backend + módulos dueños | Antes de implementación; informar diseño | Abierta |
| `V-011-OPEN-02` | Resolver `OPEN-11`/`OPEN-12`: formato, combinabilidad y datos de elegibilidad del cupón. | Promociones + Arquitectura | Antes del diseño final | Abierta |
| `V-011-OPEN-03` | Definir presentación de vigencia: fecha/hora, mensaje relativo o ambos, sin depender de contador. | Producto + UX | Antes del diseño final | Abierta |
| `V-011-OPEN-04` | Confirmar si fallo de Promociones permite continuar con cotización base o bloquea el paso. | Producto + Backend | Antes del diseño final | Abierta |
