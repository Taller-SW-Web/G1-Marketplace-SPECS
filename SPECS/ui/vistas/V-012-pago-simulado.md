# Vista — V-012 Pago simulado

> Pantalla autenticada para confirmar explícitamente una simulación de pago y ejecutar la última revalidación antes de crear la orden. No solicita tarjeta ni realiza un cobro real.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-012` |
| Nombre | Pago simulado |
| Ruta | `/checkout/pago` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Jim Segovia |
| Revisor | Leonidas Garcia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** revisar el resumen vigente, comprender que no habrá un cargo real y autorizar la preparación simulada del checkout.
- **Actor principal:** cliente autenticado con cotización vigente.
- **Permiso:** privado.
- **Condiciones de entrada:** `quoteId`, versión de carrito, dirección y beneficio aún válidos desde `V-011`.
- **Resultado esperado:** una única `CheckoutOperation` en estado `PREPARED`; todavía no existe pedido, cobro, consumo de cupón ni descuento de stock.

> [!IMPORTANT]
> El wireframe histórico que solicitaba número de tarjeta, titular, vencimiento y CVV quedó reemplazado por F-025. Esos campos y cualquier iconografía que sugiera un pago real están fuera del diseño vigente.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-025` | [`Simular pago y revalidar stock`](../../funcional/F-025-simular-pago-revalidar-stock.md) | [`UI F-025`](../F-025-simular-pago-revalidar-stock.md) | Confirmación explícita, revalidación, idempotencia y estado preparado. |

Contrato consultado: [`API F-025`](../../contrato-api/F-025-simular-pago-revalidar-stock.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| `V-011` → continuar | `V-012` | Cotización vigente | `quoteId`, cartVersion, dirección y beneficio. |
| “Volver al resumen” | `V-011` | Antes de preparar o revisión requerida | Checkout; cotización se revalida si venció. |
| “Corregir carrito” | `V-008` | Stock/línea cambió | Sesión y carrito actual; preparación no creada. |
| Preparación aprobada → “Continuar” | `V-013` | `PREPARED` confirmado | `checkoutOperationId` opaco. |
| Sesión vencida | `O-003` → `V-001` | `401` | El regreso exige revalidar el flujo; no conserva una confirmación secreta. |
| Cerrar sesión | `O-004` | Acción durante checkout | Cancelar conserva; confirmar descarta contexto. |

La `Idempotency-Key` se administra técnicamente y no aparece como campo, texto, URL o dato copiable.

## 5. Jerarquía y composición visual

```text
V-012 Pago simulado
├── Cabecera de checkout + progreso
├── Encabezado “Pago simulado”
├── Aviso destacado
│   ├── “Este entorno no realiza cobros reales”
│   └── Explicación de la revalidación
├── Resumen vigente
│   ├── Dirección resumida
│   ├── Líneas
│   ├── Beneficio
│   ├── Envío
│   └── Total estimado
├── Confirmación explícita
│   └── Checkbox no preseleccionado
├── Volver / “Confirmar pago simulado”
└── Resultado preparado + CTA separado a V-013
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Aviso | Naturaleza simulada | Primaria | Visible antes de la confirmación y del CTA; no se reduce a una nota legal. |
| Resumen | Cotización vigente | Primaria | Sólo lectura; editar vuelve a `V-011`. |
| Confirmación | Checkbox explícito | Primaria | No preseleccionado; declara que se comprende la simulación. |
| CTA de preparación | Confirmar pago simulado | Primaria | Habilitado sólo con confirmación y contexto vigente. |
| Resultado | Pago simulado aprobado | Primaria | Diferencia preparación de creación del pedido y ofrece CTA separado. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Pago simulado” | — | Siempre. |
| Aviso | “No se realizará ningún cobro real ni se solicitarán datos de tarjeta.” | — | Antes y durante preparación. |
| Ayuda | “Volveremos a validar precios, promociones, envío y disponibilidad.” | — | Estado listo. |
| Resumen | Dirección, líneas, descuentos, envío y total estimado | Volver a revisar | Contexto vigente. |
| Checkbox | “Entiendo que este pago es una simulación.” | Confirmar intención | Listo; nunca marcado por defecto. |
| CTA | “Confirmar pago simulado” | Crear/reutilizar preparación idempotente | Checkbox marcado y no procesando. |
| Preparado | “Pago simulado aprobado” | Informar que aún falta crear pedido | `PREPARED`. |
| CTA siguiente | “Continuar a crear pedido” | Abrir `V-013` | Sólo `PREPARED`. |

No se muestran marcas de tarjeta, candados asociados a cobro, teclado numérico financiero, número de tarjeta, vencimiento, titular, CVV ni mensajes de “cargo”.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Listo | Quote vigente | Aviso, resumen, checkbox y CTA inicialmente inactivo | Confirmar | Sí |
| Confirmado localmente | Checkbox marcado | CTA habilitado; ningún cobro iniciado | Enviar/desmarcar | Anotado en principal |
| Procesando | POST de preparación | CTA bloqueado, progreso y navegación destructiva desaconsejada | Esperar | Sí |
| Preparado | Respuesta `201` o repetición idempotente equivalente | Confirmación diferenciada y CTA separado | Continuar a `V-013` | Sí |
| Confirmación ausente | `400 SIMULATION_NOT_CONFIRMED` | Error asociado al checkbox | Marcar y reenviar | Sí |
| Cotización vencida | `409 QUOTE_EXPIRED` | Resumen marcado no vigente; preparación no creada | Volver a `V-011` y recalcular | Sí |
| Revisión requerida | `409 REVALIDATION_CHANGED` | Lista de categorías de cambio sin datos técnicos | Volver a `V-011` | Sí |
| Stock no disponible | `409 STOCK_NOT_AVAILABLE` | Producto afectado cuando sea seguro; preparación no creada | Corregir en `V-008` | Sí |
| Conflicto de idempotencia | `409 IDEMPOTENCY_KEY_REUSED` | Error general sin exponer la clave | Recuperar estado/reiniciar intento seguro | Sí, variante de error |
| Revalidación no disponible | `503` | Mensaje neutral; no afirma rechazo ni aprobación | Reintentar con la misma operación segura | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Sesión vencida | Login seguido de revalidación completa, no retorno ciego a procesar. |
| `O-004` | Confirmar cierre de sesión | Cierre durante checkout | Cancelar o descartar flujo. |
| `O-010` | Alertas y feedback global | Estado incierto o error no asociado al checkbox | Reintentar, revisar o volver. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Confirmación de simulación | Checkbox | Sí | Debe marcarse deliberadamente | “Confirma que comprendes que no habrá un cobro real” | Default/foco/error/seleccionado |

No existen otros campos. El resumen es de sólo lectura y cualquier corrección vuelve al paso correspondiente.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Aviso y confirmación ocupan la región principal; resumen en columna complementaria o inferior.
- El CTA permanece próximo al checkbox y no se confunde con el CTA posterior de creación de pedido.

### Mobile

- **Referencia:** 390 px.
- Orden: aviso, resumen, confirmación y CTA.
- Total estimado y naturaleza simulada son visibles antes del CTA.
- Checkbox conserva área táctil suficiente y etiqueta completa.
- CTA no se fija si oculta el aviso o los cambios de revalidación.

### Anchuras intermedias

- Resumen pasa debajo del aviso cuando las dos columnas reducen legibilidad.
- Ningún importe o texto de simulación se trunca.

## 11. Accesibilidad

- El aviso se expresa en texto directo; no depende de icono, color o tooltip.
- Checkbox y explicación forman una etiqueta comprensible y no vienen seleccionados.
- Procesando usa estado ocupado y anuncio moderado; el CTA evita doble activación.
- El foco llega al encabezado del resultado preparado o del error/revisión requerida.
- Cambios de revalidación se presentan como lista y enlazan a la corrección apropiada.
- “Preparado” y “pedido creado” nunca comparten icono, título o texto que los vuelva indistinguibles.
- Movimiento/progreso respeta preferencias de reducción.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-012 / Desktop / Listo` | Desktop | Principal | Aviso, resumen, checkbox. |
| `V-012 / Mobile / Listo` | Mobile | Principal | Orden apilado. |
| `V-012 / Desktop / Procesando` | Desktop | Progreso | CTA no repetible. |
| `V-012 / Mobile / Preparado` | Mobile | Éxito intermedio | CTA separado a `V-013`. |
| `V-012 / Desktop / Cotización vencida` | Desktop | Revisión | Volver a resumen. |
| `V-012 / Mobile / Stock no disponible` | Mobile | Atención | Corregir carrito. |
| `V-012 / Desktop / Revalidación cambió` | Desktop | Conflicto | Lista de cambios. |
| `V-012 / Mobile / Error recuperable` | Mobile | Error | Reintento seguro. |

## 13. Criterios de aceptación visual

- [ ] `UI-V012-001`: Ningún frame contiene campos, marcas o iconografía que sugieran tarjeta o cobro real.
- [ ] `UI-V012-002`: El aviso de simulación aparece antes del checkbox y del CTA en desktop y mobile.
- [ ] `UI-V012-003`: El checkbox no está preseleccionado y el CTA no puede repetirse durante el procesamiento.
- [ ] `UI-V012-004`: Cotización vencida, cambios de revalidación y stock no disponible no dejan una operación preparada.
- [ ] `UI-V012-005`: “Pago simulado aprobado” se distingue de “Pedido creado” y conduce mediante una acción separada a `V-013`.
- [ ] `UI-V012-006`: Reintentar conserva la idempotencia sin mostrar claves o identificadores técnicos.
- [ ] La vista aplica `DS-001`, foco, contraste y reducción de movimiento.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-012-OPEN-01` | Definir vigencia y recuperación de una `CheckoutOperation PREPARED` si el usuario recarga o abandona la ruta. | Backend + Producto | Antes del diseño final | Abierta |
| `V-012-OPEN-02` | Definir el detalle seguro que se mostrará para `REVALIDATION_CHANGED` y `STOCK_NOT_AVAILABLE`. | Backend + UX | Antes del diseño final | Abierta |
| `V-012-OPEN-03` | Confirmar copy institucional para explicar el pago simulado en la entrega académica. | Producto + UX | Antes del diseño final | Abierta |
| `V-012-OPEN-04` | Homologar integraciones de revalidación `I-01` y dependencia de creación posterior `I-02`. | Arquitectura + módulos dueños | Antes de implementación; informar diseño | Abierta |
