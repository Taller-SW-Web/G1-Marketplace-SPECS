# Vista — V-013 Creación de la orden

> Pantalla autenticada para completar únicamente los datos de contacto faltantes y enviar una operación preparada a Ventas de forma idempotente.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-013` |
| Nombre | Creación de la orden |
| Ruta | `/checkout/confirmacion` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Jim Segovia |
| Revisor | Fernando José Saire Tello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** revisar la preparación y crear un pedido una sola vez, completando sólo el contacto que Ventas aún necesita.
- **Actor principal:** cliente autenticado propietario de una `CheckoutOperation PREPARED`.
- **Permiso:** privado.
- **Condiciones de entrada:** operación preparada desde `V-012`, todavía no enviada con éxito a Ventas.
- **Resultado esperado:** pedido único en Ventas y navegación a `V-014`, o estado de verificación cuando el resultado sea incierto.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-026` | [`Crear orden en Ventas`](../../funcional/F-026-crear-orden-ventas.md) | [`UI F-026`](../F-026-crear-orden-ventas.md) | Contacto faltante, envío idempotente y resultado cierto/incierto. |

Contrato consultado: [`API F-026`](../../contrato-api/F-026-crear-orden-ventas.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| `V-012` → continuar | `V-013` | Operación `PREPARED` | `checkoutOperationId` y resumen transitorio. |
| “Volver” | `V-012` | Antes de enviar y operación aún preparada | Operación; no duplica preparación. |
| Orden creada | `V-014` | `SUCCEEDED` con `orderId` | Sólo ID de pedido y resumen permitido. |
| Resultado pendiente | Misma `V-013` | `SUBMITTED`/`ORDER_CREATION_PENDING` | Operación original para consultar; no genera una nueva. |
| Operación no preparada | `V-012` o `V-011` | `409 OPERATION_NOT_PREPARED` | Retorno seguro según estado vigente. |
| Sesión vencida | `O-003` → `V-001` | `401` | Después de login se consulta la operación existente antes de permitir acción. |
| Cerrar sesión | `O-004` | Acción durante envío/preparación | Nunca interrumpe silenciosamente un envío; confirma y luego consulta estado. |

## 5. Jerarquía y composición visual

```text
V-013 Creación de la orden
├── Cabecera de checkout + progreso
├── Encabezado “Confirma y crea tu pedido”
├── Resumen final de sólo lectura
│   ├── Líneas e importes revalidados
│   ├── Dirección resumida
│   └── Pago simulado preparado
├── Datos de contacto faltantes, condicional
│   ├── Nombre completo
│   ├── Tipo/número de documento
│   ├── Teléfono
│   └── Correo
├── Aviso: aún no existe pedido
└── Acción “Crear pedido”
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Resumen | Representación final permitida | Primaria | Sólo lectura; no expone dirección/documento completos innecesariamente. |
| Contacto | Sólo campos faltantes | Primaria | Datos ya resueltos no se vuelven a solicitar ni muestran como editables. |
| Aviso | Creación única | Primaria | Explica que el siguiente envío registrará el pedido, sin prometer cobro real. |
| CTA | “Crear pedido” | Primaria | Una activación; bloqueado mientras se envía o verifica. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Confirma y crea tu pedido” | — | Estado listo. |
| Resumen | Artículos, importes, entrega y simulación preparada | Revisar | Siempre antes del envío. |
| Nombre completo | Dato requerido por Ventas | Capturar | Falta en perfil autorizado. |
| Tipo documento | DNI/RUC/CE/PASAPORTE | Seleccionar | Documento faltante. |
| Número documento | Según tipo | Capturar | Documento faltante. |
| Teléfono | Contacto de la orden | Capturar | Falta en perfil autorizado. |
| Correo | Contacto/notificación | Capturar | Falta en perfil autorizado. |
| CTA | “Crear pedido” | Enviar operación una vez | Datos válidos y estado `PREPARED`. |
| Progreso | “Estamos registrando tu pedido” | Informar | `SUBMITTED` en curso. |
| Verificación | “Estamos verificando tu pedido” | Consultar la operación existente | Resultado incierto. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Listo sin campos | Perfil aporta todo | Resumen y CTA | Crear pedido | Sí |
| Listo con campos faltantes | Contacto incompleto | Sólo campos necesarios y CTA | Completar | Sí |
| Validación local | Formato/incompletitud | Errores junto al campo; resto permanece | Corregir | Sí |
| Enviando | POST iniciado | CTA no repetible, controles bloqueados, mensaje de progreso | Esperar | Sí |
| Éxito | `201 SUCCEEDED` | Transición a `V-014`; no se repite CTA | Ver pedido confirmado | Se diseña en `V-014` |
| Resultado incierto | `409 ORDER_CREATION_PENDING` o estado `SUBMITTED` | Mensaje neutral; no icono de fracaso/éxito; sin nuevo envío | Verificar operación | Sí |
| Contacto rechazado | `400 CONTACT_VALIDATION_ERROR` | Sólo campos inválidos marcados | Corregir | Sí |
| Operación no preparada | `409 OPERATION_NOT_PREPARED` | Explicación y retorno al paso correcto | Revisar preparación | Sí |
| Conflicto idempotente | `409 IDEMPOTENCY_KEY_REUSED` | Error general; no muestra clave | Recuperar estado/iniciar flujo seguro | Sí, variante |
| Ventas no disponible | `503` | No se asume que no existe pedido; estado según operación local | Verificar/reintentar sólo cuando sea seguro | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Sesión vencida | Login y consulta de operación antes de habilitar CTA. |
| `O-004` | Confirmación de cierre durante checkout | Intento de logout, especialmente durante `SUBMITTED` | Cancelar o cerrar tras explicar verificación pendiente. |
| `O-010` | Alertas y feedback global | Error o transición que no pertenece a un campo | Verificar, volver o cerrar. |

`C-001` todavía no se dispara desde esta vista como garantía visual; corresponde a la orden confirmada y se procesa de forma asíncrona.

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Nombre completo | Texto | Condicional | Reglas de Ventas, no sólo espacios | “Ingresa el nombre completo” | Default/foco/error |
| Tipo de documento | Select/radio | Condicional | DNI, RUC, CE o PASAPORTE | “Selecciona el tipo” | Default/foco/error |
| Número de documento | Texto | Condicional | Regla dependiente del tipo, sin revelar validaciones internas | Ayuda específica por tipo | Default/foco/error |
| Teléfono | Teléfono | Condicional | Formato aceptado por Ventas | Ejemplo aprobado | Default/foco/error |
| Correo | Email | Condicional | Formato válido | “Ingresa un correo válido” | Default/foco/error |

Los datos son transitorios para crear la orden; la interfaz no afirma que actualizará el perfil. No existe campo editable de cliente, operación o idempotencia.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Resumen y contacto pueden usar dos columnas, con CTA asociado al bloque de confirmación.
- Campos condicionales mantienen orden y anchura coherentes; documento agrupa tipo y número sin perder ayudas.

### Mobile

- **Referencia:** 390 px.
- Orden: título, resumen, aviso, campos faltantes y CTA.
- Tipo/número se apilan si no mantienen ancho útil.
- En estado enviando/verificando, el mensaje permanece visible y no se sustituye por un spinner aislado.

### Anchuras intermedias

- El resumen pasa encima del formulario al dejar de funcionar en columnas.
- El CTA no queda fijo si tapa errores o el estado incierto.

## 11. Accesibilidad

- El formulario sólo incluye campos faltantes, con explicación previa para evitar incertidumbre.
- Tipo y número de documento se agrupan semánticamente; errores se asocian al campo correspondiente.
- El CTA anuncia estado ocupado y no desaparece sin una confirmación/estado visible.
- Al fallar validación, el foco llega al primer error; al pasar a verificación, al título del estado.
- “Resultado incierto” no depende de un icono de advertencia y no invita a crear otra compra.
- Datos sensibles se enmascaran en el resumen y no se anuncian fuera del contexto necesario.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-013 / Desktop / Listo sin campos` | Desktop | Principal | Resumen y CTA. |
| `V-013 / Mobile / Campos faltantes` | Mobile | Formulario | Todos los tipos de campo. |
| `V-013 / Desktop / Validación` | Desktop | Error local | Documento/contacto inválido. |
| `V-013 / Mobile / Enviando` | Mobile | Progreso | CTA bloqueado y mensaje. |
| `V-013 / Desktop / Resultado incierto` | Desktop | Pendiente | Verificación sin reenvío. |
| `V-013 / Mobile / Operación no preparada` | Mobile | Conflicto | Retorno al paso correcto. |
| `V-013 / Desktop / Ventas no disponible` | Desktop | Error/pendiente | Recuperación segura. |

## 13. Criterios de aceptación visual

- [ ] `UI-V013-001`: Sólo se solicitan los campos que faltan según el perfil autorizado y los requisitos de Ventas.
- [ ] `UI-V013-002`: “Crear pedido” no puede activarse dos veces ni reaparecer como una compra nueva durante `SUBMITTED`.
- [ ] `UI-V013-003`: Resultado incierto se presenta como verificación pendiente, no como fallo ni éxito.
- [ ] `UI-V013-004`: Los datos de contacto no se presentan como actualización del perfil local.
- [ ] `UI-V013-005`: Errores validables preservan campos correctos y llevan el foco al primer error.
- [ ] `UI-V013-006`: No se muestran idempotency keys, request IDs, tokens ni errores internos.
- [ ] Desktop y mobile aplican `DS-001` y distinguen creación de orden de pago preparado/confirmación final.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-013-OPEN-01` | Resolver `I-02`: idempotencia explícita y respuesta repetida de `POST /pedidos` en Ventas. | Ventas + Arquitectura | Antes de implementación; informar diseño | Abierta |
| `V-013-OPEN-02` | Confirmar reglas exactas de DNI, RUC, CE y PASAPORTE aceptadas por Ventas. | Ventas + UX | Antes del diseño final | Abierta |
| `V-013-OPEN-03` | Definir frecuencia, duración y salida del estado “Estamos verificando tu pedido”. | Backend + Producto | Antes del diseño final | Abierta |
| `V-013-OPEN-04` | Confirmar qué datos de perfil llegan autorizados para decidir los campos faltantes. | Seguridad + Ventas | Antes del diseño final | Abierta |
