# Vista — V-014 Pedido confirmado

> Pantalla privada que confirma la compra simulada sólo cuando Ventas informa `PAGADO` para el pedido. Un pedido únicamente `CREADO` continúa en verificación; el correo se procesa por separado.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-014` |
| Nombre | Pedido confirmado |
| Ruta | `/checkout/confirmado/{orderId}` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Jim Segovia |
| Revisor | Fernando José Saire Tello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** confirmar que el pedido existe, conservar su código y elegir entre revisarlo o seguir comprando.
- **Actor principal:** cliente autenticado propietario del pedido/operación.
- **Permiso:** privado.
- **Condición de entrada:** F-026 conserva `externalOrderId` y verifica `PAGADO` del mismo pedido; `PREPARED`, `CREADO` o `SUBMITTED` no permiten mostrar éxito.
- **Resultado esperado:** código, fecha, total, estado pagado y próximos pasos comprensibles, sin exponer documento ni dirección completa.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-027` | [`Mostrar confirmación`](../../funcional/F-027-confirmacion-orden.md) | [`UI F-027`](../F-027-confirmacion-orden.md) | Pedido confirmado, snapshot, estado incierto y acciones. |
| `F-034` | [`Enviar confirmación asíncrona`](../../funcional/F-034-enviar-confirmacion-asincrona.md) | [`UI F-034`](../F-034-enviar-confirmacion-asincrona.md) | Aviso de correo futuro sin promesa de entrega ni bloqueo. |

Contratos consultados: [`API F-027`](../../contrato-api/F-027-confirmacion-orden.md) y [`API F-034`](../../contrato-api/F-034-enviar-confirmacion-asincrona.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| `V-013` después de `SUCCEEDED` | `V-014` | `PAGADO` verificado en Ventas | `orderId` y snapshot permitido. |
| URL propia | `V-014` | Cliente propietario | Sesión; consulta del pedido/operación. |
| “Ver mi pedido” | `V-016` | `orderId` válido | Pedido seleccionado. |
| “Seguir comprando” | `V-005` | Acción explícita | Sesión; carrito anterior ya no se presenta como pendiente. |
| “Verificar pedido” | Misma vista / consulta de operación | Estado `SUBMITTED` | Operación original; nunca una nueva creación. |
| Sesión vencida | `O-003` → `V-001` | `401` | Retorno a esta ruta sólo tras autorizar propiedad. |

## 5. Jerarquía y composición visual

```text
V-014 Pedido confirmado
├── Cabecera de checkout completo
├── Estado principal
│   ├── Icono semántico de éxito
│   ├── “¡Pedido confirmado!”
│   ├── Código copiable
│   └── Fecha y estado PAGADO
├── Resumen corto
│   ├── Artículos/cantidad resumida
│   └── Total confirmado
├── Próximos pasos
│   └── Aviso de correo asíncrono
└── “Ver mi pedido” / “Seguir comprando”
```

El estado de verificación pendiente sustituye el bloque de éxito: usa título, icono y acciones neutrales diferentes; nunca reutiliza el check de confirmación.

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título de éxito | “¡Pedido confirmado!” | — | Sólo `SUCCEEDED` con `orderId` y `PAGADO` verificado. |
| Código | “Pedido {orderId}” | Copiar mediante botón etiquetado | Éxito. |
| Estado | “Pago simulado confirmado” | — | Éxito verificado por Ventas; se aclara que no hubo cargo real. |
| Fecha | Fecha/hora localizada | — | Éxito. |
| Total | Importe y moneda del snapshot de Ventas | — | Éxito. |
| Resumen | Conteo o lista corta autorizada | — | Si contrato lo entrega. |
| Correo | “Te enviaremos una confirmación al correo registrado.” | — | Éxito; email enmascarado sólo si está autorizado. |
| Acción primaria | “Ver mi pedido” | Abrir `V-016` | Éxito. |
| Acción secundaria | “Seguir comprando” | Abrir `V-005` | Éxito. |
| Pendiente | “Estamos preparando o verificando tu pedido” | Consultar operación original | `CREADO`, `SUBMITTED` o respuesta `202`. |

No se muestran documento, dirección completa, contacto, idempotency key, request ID ni estado interno de `NotificationDelivery`.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Consulta autorizada | Skeleton del estado/resumen; sin código ficticio | Esperar | Sí |
| Confirmado | `SUCCEEDED` y pedido `PAGADO` verificado | Éxito, código, fecha, total y acciones | Ver pedido/seguir | Sí |
| Pedido creado pendiente | `CREADO` sin confirmación simulada final | Mensaje neutral, sin check de éxito | Verificar operación original | Sí, variante pendiente |
| Correo pendiente implícito | Pedido confirmado | Mensaje “Te enviaremos…”; no badge técnico | Ninguna; no bloquea | Anotado en confirmado |
| Verificación en curso | Respuesta `202/SUBMITTED` | Mensaje neutral, sin éxito ni nuevo CTA de compra | Verificar de nuevo | Sí |
| Creación fallida recuperable | `409` con salida definida | Mensaje según operación, sin código de pedido | Volver al paso seguro/soporte | Sí |
| Pedido no accesible | No existe o no pertenece al cliente | Estado neutral que no confirma existencia ajena | Volver a pedidos/inicio | Sí |
| Error de consulta | Fallo temporal | No muestra falso éxito ni fallo definitivo | Reintentar | Sí |

Un fallo o retraso del correo nunca cambia `Confirmado` a error ni reemplaza el código del pedido.

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Sesión vencida al consultar | Login y retorno autorizado. |
| `O-010` | Alertas y feedback global | Copia de código o error recuperable | Confirmar/reintentar/cerrar. |
| `C-001` | Correo de confirmación | Pedido exitoso encolado de forma asíncrona | La web no espera su envío; el correo enlaza a `V-016`. |

## 9. Formularios y validación visual

No existen formularios. “Copiar código” es un botón, confirma el resultado sin alterar el pedido y ofrece alternativa manual si el portapapeles no está disponible.

| Control | Regla | Feedback |
|---|---|---|
| Copiar código | Copia sólo el identificador visible | “Código copiado” mediante anuncio accesible. |
| Verificar pedido | Consulta la operación original | Progreso no repetible y resultado en la misma región. |

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Tarjeta/área central con éxito y resumen; acciones primarias visibles sin convertirla en comprobante financiero.
- Código y copiar permanecen juntos; el texto no se trunca.

### Mobile

- **Referencia:** 390 px.
- Orden: estado, código, resumen, correo y acciones apiladas.
- Código puede envolver sin ocultarse y el botón mantiene etiqueta accesible.
- Acciones ocupan ancho disponible y distinguen primaria/secundaria.

### Anchuras intermedias

- Resumen y acciones se apilan antes de reducir la legibilidad del código o total.

## 11. Accesibilidad

- El foco llega al título de éxito, verificación o error tras la navegación.
- El icono complementa texto y no es la única evidencia del estado.
- Código se lee como una unidad comprensible; copiar no exige seleccionar texto.
- Fecha, moneda y total usan formato localizado y etiquetas explícitas.
- El estado pendiente no usa animación infinita como única señal y respeta reducción de movimiento.
- El mensaje del correo no afirma “enviado” y no expone la dirección completa.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-014 / Desktop / Confirmado` | Desktop | Éxito | Código, total, correo y acciones. |
| `V-014 / Mobile / Confirmado` | Mobile | Éxito | Orden apilado. |
| `V-014 / Desktop / Cargando` | Desktop | Skeleton | Sin éxito ficticio. |
| `V-014 / Mobile / Verificación en curso` | Mobile | Pendiente | Acción de verificar. |
| `V-014 / Desktop / Creación fallida` | Desktop | Error recuperable | Salida segura. |
| `V-014 / Mobile / Pedido no accesible` | Mobile | No disponible | Estado neutral. |
| `V-014 / Desktop / Error de consulta` | Desktop | Error temporal | Reintento. |

## 13. Criterios de aceptación visual

- [ ] `UI-V014-001`: Sólo `SUCCEEDED` con `orderId` y `PAGADO` verificado muestra icono/título de pedido confirmado.
- [ ] `UI-V014-008`: `CREADO` no se representa como compra pagada; su salida de verificación depende del contrato homologado con Ventas.
- [ ] `UI-V014-002`: Verificación pendiente es visual y semánticamente distinta y nunca ofrece crear otra compra.
- [ ] `UI-V014-003`: El código es visible, copiable y accesible; sólo pertenece al cliente autenticado.
- [ ] `UI-V014-004`: Documento y dirección completa no aparecen en la confirmación.
- [ ] `UI-V014-005`: El texto del correo promete procesamiento futuro, no entrega inmediata ni estado en tiempo real.
- [ ] `UI-V014-006`: Fallo del correo no cambia el éxito del pedido.
- [ ] `UI-V014-007`: Desktop y mobile ofrecen “Ver mi pedido” y “Seguir comprando” con jerarquía clara.
- [ ] La vista aplica `DS-001` y no se presenta como recibo de un cobro real.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-014-OPEN-01` | Unificar la ruta pública por `orderId` con la consulta técnica actual por `checkoutOperationId`. | Backend + Arquitectura | Antes de implementación; informar diseño | Abierta |
| `V-014-OPEN-02` | Confirmar qué resumen corto de artículos entrega Ventas para esta vista. | Ventas + Producto | Antes del diseño final | Abierta |
| `V-014-OPEN-03` | Confirmar si se muestra correo enmascarado y cuál es su fuente autorizada. | Seguridad + UX | Antes del diseño final | Abierta |
| `V-014-OPEN-04` | Definir salida y soporte para estados `FAILED` sin pedido. | Backend + Producto | Antes del diseño final | Abierta |
| `V-014-OPEN-05` | Confirmar en Ventas el estado `PAGADO`, el snapshot final y la ruta de recuperación antes de actualizar los frames aprobados. | Ventas + Arquitectura + UX | Antes de implementación real | Abierta |
