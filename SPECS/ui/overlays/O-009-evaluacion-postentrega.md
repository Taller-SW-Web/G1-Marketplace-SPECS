# Overlay — O-009 Evaluación postentrega

> Invitación no invasiva para evaluar una entrega completada mediante Bien, Regular o Mal, con motivos contextuales y comentario opcional.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-009` |
| Nombre | Evaluación postentrega |
| Tipo | Banner de invitación + modal/formulario |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Diego Espinoza |
| Revisor | Sebastián Malca |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** recoger una evaluación única de un pedido entregado sin interrumpir compra, pago o navegación crítica.
- **Funcionalidad:** `F-040` Registrar evaluación postentrega.
- **Vistas que lo invocan:** [`V-016`](../vistas/V-016-detalle-reordenado.md) y/o [`V-017`](../vistas/V-017-seguimiento.md), sujeto a política final.
- **Spec UI de origen:** [`UI F-040`](../F-040-evaluacion-postentrega.md).

No aparece inmediatamente después del pago o creación del pedido. Una calificación baja no crea un reclamo automáticamente.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Mostrar invitación | Pedido propio `ENTREGADO`, prompt elegible y no respondido/descartado | Banner discreto con Evaluar/Ahora no. |
| Evaluar | Acción del banner o disparador aprobado | Abre formulario modal y enfoca título. |
| Elegir sentimiento | Bien/Regular/Mal | Actualiza motivos contextuales sin borrar comentario. |
| Enviar | Sentimiento válido; motivos según reglas | Envía una sola vez. |
| Ahora no | Acción explícita | Marca prompt `DISMISSED` según política y cierra. |
| Cerrar/Escape | Modal abierto | Equivale a “Ahora no” sólo si la política lo define; de lo contrario cierra sin enviar y conserva elegibilidad. |

## 4. Estructura, contenido y acciones

```text
Invitación
├── “¿Cómo fue la entrega de tu pedido?”
├── “Evaluar”
└── “Ahora no”

Formulario
├── Título y código resumido del pedido
├── Bien / Regular / Mal
├── Motivos contextuales
├── Comentario opcional
├── Enviar evaluación
└── Ahora no / Cerrar
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Contexto | Pedido entregado; no experiencia de pago | Orientar | Primaria |
| Sentimiento | Bien/Regular/Mal | Seleccionar uno | Primaria |
| Motivos | Opciones según sentimiento | Selección múltiple si contrato lo permite | Secundaria |
| Comentario | Texto opcional | Ampliar contexto | Secundaria |
| Enviar | CTA | Registrar | Primaria |
| Ahora no | Acción no destructiva | Posponer/descartar según política | Secundaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Invitación | Pedido elegible | Banner no modal | Sí |
| Sin selección | Formulario abierto | Tres respuestas disponibles; enviar inactivo | Sí |
| Bien | `GOOD` | Motivos positivos aprobados | Sí |
| Regular | `REGULAR` | Motivos neutrales/de mejora | Sí, anotado |
| Mal | `BAD` | Motivos negativos y aclaración de que no crea reclamo | Sí |
| Enviando | POST en curso | CTA ocupado y controles no repetibles | Sí, anotado |
| Enviada | `201` o duplicado `409 CSAT_ALREADY_SUBMITTED` | Agradecimiento y cierre | Sí |
| Ya no elegible | `409 ORDER_NOT_DELIVERED` o estado cambió | Formulario cierra/explica sin guardar éxito | Sí, variante error |
| Error recuperable | Fallo temporal | Selección/comentario se conservan durante la sesión | Reintentar/cerrar | Sí |

## 6. Responsive y accesibilidad

- Banner no tapa navegación, timeline, CTA o información de pedido.
- Desktop usa modal compacto; mobile puede usar bottom sheet alta/pantalla completa con teclado considerado.
- Sentimientos son botones/radios con texto e icono, nunca sólo caras o color.
- Motivos se agrupan con leyenda y se anuncian al cambiar de sentimiento sin mover foco inesperadamente.
- Comentario tiene etiqueta, contador/límite si existe y ayuda “Opcional”.
- Foco inicial en título; trampa de foco; al cerrar vuelve a Evaluar o región del pedido.
- Enviar mueve foco a agradecimiento/error; progreso evita doble envío.
- “Ahora no” es alcanzable y no se presenta como error o rechazo moral.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-009 / Desktop / Invitación` | Desktop | Banner |
| `O-009 / Mobile / Sin selección` | Mobile | Formulario |
| `O-009 / Desktop / Bien` | Desktop | Motivos positivos |
| `O-009 / Mobile / Mal` | Mobile | Motivos negativos |
| `O-009 / Desktop / Enviada` | Desktop | Agradecimiento |
| `O-009 / Mobile / Error recuperable` | Mobile | Reintento |

## 8. Criterios de aceptación visual

- [ ] `UI-O009-001`: Sólo aparece para un pedido propio entregado y como máximo una vez según el estado del prompt.
- [ ] `UI-O009-002`: Nunca aparece inmediatamente después del pago o antes de la entrega.
- [ ] `UI-O009-003`: Bien/Regular/Mal se identifican mediante texto, icono y selección accesible.
- [ ] `UI-O009-004`: Motivos cambian según la respuesta y permanecen opcionales salvo decisión explícita.
- [ ] `UI-O009-005`: Comentario se identifica como opcional y una calificación baja no afirma crear un reclamo.
- [ ] `UI-O009-006`: Duplicado confirmado se trata como ya enviado y no permite repetir.
- [ ] `UI-O009-007`: “Ahora no”, Escape y cerrar siguen una política documental única.
- [ ] El overlay cumple `DS-001`, foco y manejo accesible del teclado.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-009-OPEN-01` | Resolver `I-04`: elegibilidad por ENTREGADO, motivos y adaptación al contrato CSAT de Ventas. | Ventas + Arquitectura | Abierta |
| `O-009-OPEN-02` | Aprobar catálogo de motivos para Bien/Regular/Mal y si alguno será obligatorio. | Producto + UX | Abierta |
| `O-009-OPEN-03` | Definir política de `DISMISSED`, cierre/Escape y si puede volver a invitarse. | Producto | Abierta |
| `O-009-OPEN-04` | Elegir superficies exactas de activación entre `V-016` y `V-017`. | Producto + UX | Abierta |
