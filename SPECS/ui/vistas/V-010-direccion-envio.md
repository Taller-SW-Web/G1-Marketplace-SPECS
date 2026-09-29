# Vista — V-010 Dirección de envío

> Primer tramo del checkout autenticado para seleccionar una dirección propia guardada o registrar una nueva antes de cotizar el envío.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-010` |
| Nombre | Dirección de envío |
| Ruta | `/checkout/direccion` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Jim Segovia |
| Revisor | Leonidas Garcia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** elegir una dirección propia o registrar una nueva para continuar el checkout.
- **Actor principal:** cliente autenticado con carrito válido y no vacío.
- **Permiso:** privado; no existe checkout de invitado en el alcance inicial.
- **Condiciones de entrada:** sesión activa y carrito comprable desde `V-008`.
- **Resultado esperado:** `addressId` válido seleccionado y navegación a `V-011`; Marketplace no guarda una copia permanente de la dirección.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-022` | [`Capturar o seleccionar dirección`](../../funcional/F-022-seleccionar-direccion-envio.md) | [`UI F-022`](../F-022-seleccionar-direccion-envio.md) | Direcciones propias, registro, selección y validación. |

Contrato consultado: [`API F-022`](../../contrato-api/F-022-seleccionar-direccion-envio.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| `V-008` → “Iniciar checkout” | `V-010` | Sesión y carrito válidos | Carrito/version vigente. |
| Acceso sin sesión | `O-003` → `V-001` | Sesión ausente o vencida | Retorno seguro a checkout después de validar nuevamente el carrito. |
| “Volver al carrito” | `V-008` | Acción explícita | Carrito; dirección temporal puede descartarse tras advertencia si corresponde. |
| “Continuar” | `V-011` | Dirección propia seleccionada o creada | `addressId` y copia transitoria necesaria para cotizar. |
| Cerrar sesión durante checkout | `O-004` | Acción explícita | No se cierra hasta confirmar; luego se descarta contexto sensible. |

Si el carrito queda vacío o no comprable, la vista informa el cambio y dirige a `V-008`; no permite avanzar con una dirección aislada.

## 5. Jerarquía y composición visual

```text
V-010 Dirección de envío
├── Cabecera de checkout
│   ├── Logo/salida segura
│   └── Indicador de progreso
├── Encabezado “¿Dónde entregamos tu pedido?”
├── Contenido principal
│   ├── Direcciones guardadas
│   │   └── AddressCard + radio × N
│   ├── Acción “Agregar nueva dirección”
│   └── Formulario de nueva dirección, condicional
├── Resumen compacto del carrito
└── Acciones “Volver al carrito” / “Continuar al resumen”
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Progreso | Dirección → Resumen → Pago → Confirmación | Secundaria | Paso actual textual; no permite saltar a pasos incompletos. |
| Direcciones | Tarjetas seleccionables | Primaria | Sólo direcciones del titular; una selección a la vez. |
| Nueva dirección | Formulario | Primaria | Se abre cuando no hay direcciones o por acción explícita. |
| Resumen compacto | Cantidad de artículos y acceso de revisión | Secundaria | No introduce cálculo de envío, cupón o total de `V-011`. |
| Navegación | Volver / continuar | Primaria | Continuar sólo con dirección confirmada. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “¿Dónde entregamos tu pedido?” | — | Siempre. |
| AddressCard | Etiqueta, calle, distrito/provincia/departamento y teléfono enmascarado | Seleccionar | Existen direcciones guardadas. |
| Nueva dirección | “Agregar nueva dirección” | Mostrar formulario | Siempre, salvo formulario ya abierto. |
| Etiqueta | Nombre de referencia, por ejemplo “Casa” | Capturar | Formulario. |
| Calle/avenida | Dirección principal | Capturar | Formulario. |
| Departamento/provincia/distrito | Ubicación administrativa | Seleccionar o capturar según contrato UI aprobado | Formulario. |
| Referencia | Ayuda para encontrar el lugar | Capturar | Opcional. |
| Teléfono | Contacto para entrega | Capturar | Formulario. |
| Guardar/usar | “Guardar y usar esta dirección” | Crear dirección y seleccionarla | Formulario válido. |
| Continuar | “Continuar al resumen” | Abrir `V-011` | Dirección seleccionada. |

Editar o eliminar direcciones existentes no está incluido en F-022 y no debe aparecer como acción funcional sin una spec adicional.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Consulta de direcciones | Skeleton de tarjetas; continuar inactivo | Esperar | Sí |
| Con direcciones | Lista propia disponible | Tarjetas, selección y nueva dirección | Seleccionar/continuar | Sí |
| Sin direcciones | Arreglo vacío | Explicación y formulario abierto | Registrar | Sí |
| Nueva dirección | Acción explícita | Formulario y cancelar/guardar | Completar/cancelar | Sí |
| Validación local | Campos inválidos o incompletos | Errores asociados; datos válidos permanecen | Corregir | Sí |
| Guardando dirección | POST en curso | Formulario ocupado y CTA no repetible | Esperar | Sí |
| Dirección creada | Respuesta `201` | Nueva tarjeta seleccionada; formulario se cierra | Continuar | Sí, transición anotada |
| Error de dirección | `400` | Campos específicos marcados; datos permanecen | Corregir | Sí |
| Servicio no disponible | `503` en lista o creación | Mensaje; formulario/datos preservados | Reintentar/volver | Sí |
| Sesión vencida | `401` | No se muestran direcciones; acceso requerido | Iniciar sesión | Se diseña con `O-003` |
| Carrito inválido | Carrito vacío/no comprable al revalidar | Aviso de atención y avance bloqueado | Volver a `V-008` | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida con retorno | Sesión ausente o vencida | Login y revalidación antes de regresar. |
| `O-004` | Confirmación de cierre durante checkout | El cliente intenta cerrar sesión | Cancelar conserva la vista; confirmar descarta checkout y vuelve al inicio. |
| `O-010` | Alertas y feedback global | Error no asociado a un campo o cambio del carrito | Reintentar o volver al carrito. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla visible | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Dirección guardada | Radio | Sí, alternativa al formulario | Debe pertenecer al titular | “Selecciona una dirección” | Default/seleccionada |
| Etiqueta | Texto | Según contrato final | Nombre breve para reconocerla | Ejemplo “Casa” | Default/foco/error |
| Calle/avenida | Texto | Sí | No sólo espacios; límites del contrato | “Ingresa la dirección” | Default/foco/error |
| Departamento | Selector/texto | Sí | Valor admitido por Seguridad | “Selecciona el departamento” | Default/foco/error |
| Provincia | Selector/texto | Sí | Coherente con departamento | “Selecciona la provincia” | Default/foco/error |
| Distrito | Selector/texto | Sí | Coherente con provincia | “Selecciona el distrito” | Default/foco/error |
| Referencia | Texto | No | Límite del contrato; no recopilar datos innecesarios | “Opcional” | Default/foco/error |
| Teléfono | Teléfono | Sí | Formato aceptado por Seguridad | Ayuda con formato | Default/foco/error |

No existe un campo `userId` o `customerId`. La identidad siempre proviene de la sesión.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Contenido de dirección y resumen compacto pueden usar dos columnas, priorizando el formulario.
- Tarjetas en lista o grilla con radio, etiqueta y datos esenciales legibles.
- Formulario puede agrupar ubicación en columnas sólo si ayudas/errores conservan espacio suficiente.

### Mobile

- **Referencia:** 390 px.
- Progreso compacto con texto del paso actual; no depender sólo de círculos numerados.
- Tarjetas y campos en una columna; teléfono enmascarado permanece legible.
- Resumen compacto y acciones aparecen después del formulario/selección.
- El teclado no oculta error ni CTA; continuar no queda fijo si tapa campos.

### Anchuras intermedias

- El resumen pasa debajo del contenido cuando reduce el ancho útil del formulario.
- Campos de ubicación se apilan antes de truncar etiquetas o mensajes.

## 11. Accesibilidad

- Direcciones agrupadas en `fieldset` con leyenda; toda la tarjeta puede activar el radio sin duplicar focos.
- El lector anuncia etiqueta, dirección resumida y teléfono enmascarado de la seleccionada.
- Mostrar el formulario mueve el foco a su título; cancelar devuelve foco a “Agregar nueva dirección”.
- Etiquetas, ayudas y errores están asociados mediante descripción.
- Al guardar, el CTA evita doble envío; al completar, se anuncia la nueva dirección seleccionada.
- El paso actual del checkout se expresa con texto y `aria-current` apropiado.
- Datos personales no aparecen en títulos de página, URLs, toasts globales o registros visuales innecesarios.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-010 / Desktop / Con direcciones` | Desktop | Principal | Tarjetas, selección y resumen. |
| `V-010 / Mobile / Con direcciones` | Mobile | Principal | Flujo apilado. |
| `V-010 / Desktop / Sin direcciones` | Desktop | Vacío | Formulario abierto. |
| `V-010 / Mobile / Nueva dirección` | Mobile | Formulario | Campos y acciones. |
| `V-010 / Desktop / Validación` | Desktop | Error local | Errores por campo. |
| `V-010 / Mobile / Guardando` | Mobile | Progreso | CTA no repetible. |
| `V-010 / Desktop / Servicio no disponible` | Desktop | Error | Datos preservados y reintento. |
| `V-010 / Mobile / Carrito inválido` | Mobile | Conflicto | Retorno a `V-008`. |

## 13. Criterios de aceptación visual

- [ ] `UI-V010-001`: Sólo se muestran y seleccionan direcciones del titular autenticado.
- [ ] `UI-V010-002`: Sin direcciones, el formulario aparece con una explicación y no como error.
- [ ] `UI-V010-003`: Referencia es opcional; los demás datos exigidos por F-022 se validan sin borrar valores correctos.
- [ ] `UI-V010-004`: El teléfono de las tarjetas está enmascarado y los datos visibles se limitan a elegir la entrega.
- [ ] `UI-V010-005`: Continuar sólo está disponible con una dirección confirmada y un carrito todavía comprable.
- [ ] `UI-V010-006`: Crear una dirección no acepta identidad manipulable ni la persiste en Marketplace.
- [ ] `UI-V010-007`: Sesión vencida y cierre voluntario protegen los datos y conservan/descartan el contexto según la decisión del usuario.
- [ ] Desktop y mobile aplican `DS-001`, foco, errores y objetivos táctiles accesibles.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-010-OPEN-01` | Confirmar obligatoriedad y límites exactos de `label` y los demás campos en el contrato de Seguridad. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-010-OPEN-02` | Confirmar fuente y controles para departamento, provincia y distrito: maestros encadenados o texto validado. | Seguridad + UX | Antes del diseño final | Abierta |
| `V-010-OPEN-03` | Aprobar anatomía y nombres del indicador de progreso compartido por `V-010` a `V-014`. | UX/UI | Antes del diseño final | Abierta |
| `V-010-OPEN-04` | Definir cuánto resumen del carrito se muestra sin duplicar `V-011`. | Producto + UX | Antes del diseño final | Abierta |
