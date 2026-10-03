# Spec de componentes React — F-035 Enviar actualización de despacho por correo

> Traducción técnica de las specs vigentes; no es código implementado ni aprobación de un contrato externo pendiente.

## 1. Metadatos y trazabilidad

| Campo | Valor |
|---|---|
| ID funcional | `F-035` |
| Versión / estado | `0.1.0` / En revisión |
| Fecha | 2026-10-02 |
| Funcional | [F-035](../funcional/F-035-enviar-actualizacion-despacho.md) |
| UI funcional | [F-035](../ui/F-035-enviar-actualizacion-despacho.md) |
| Contrato API | [F-035](../contrato-api/F-035-enviar-actualizacion-despacho.md) |
| Entregables visuales | [C-002](../ui/comunicaciones/C-002-correo-actualizacion-despacho.md) |
| Base transversal | [Arquitectura React](ARQUITECTURA-REACT.md), [DS-001 v0.2.0](../ui/DS-001-sistema-diseno-marketplace.md) |
| Stack | React + TypeScript; Next.js App Router propuesto por arquitectura existente; librería UI pendiente de DS-OPEN-03 |
| Responsables de implementación | Propuesta explícita en [plan F-035](../../plan/funcionalidades/F-035-enviar-actualizacion-despacho.md); no reemplaza el reparto de mockups |
| Iteración objetivo | Sprint 5, sujeto a puertas de entrada y capacidad confirmada |

## 2. Rutas y pantallas

| Ruta / superficie | Acceso | Composición |
|---|---|---|
| `No ruta React nueva; correo C-002 enlaza V-017` | Evento interno autorizado/worker | `ShipmentEmailTemplate` |

Los enlaces de vistas/overlays definen todos los frames y variantes; no crear un nuevo ID V para un estado de la misma pantalla. Desktop se produce primero; mobile sigue dentro del alcance, no se elimina ni se simula reduciendo el desktop.

## 3. Árbol de componentes

```text
Servidor / renderer de comunicaciones (sin hidratación)
└── ShipmentEmailTemplate

```

El contenedor coordina transporte/estado; los componentes presentacionales no llaman servicios externos ni contienen reglas de descuento, stock o autorización.

## 4. Contratos de componentes

| ID / componente | Responsabilidad | Props tipadas (propuesta) | Eventos |
|---|---|---|---|
| `CMP-F035-001` · `ShipmentEmailTemplate` | Cambio de estado/fecha estimada y Ver seguimiento, server-only. | `payload: ShipmentEmailPayload; trackingUrl: SafeConfiguredUrl` | — |

Los nombres de DTO y drafts son contratos TypeScript de implementación, no nuevos campos de la API. Su estructura se deriva exclusivamente del contrato enlazado; aplicar las convenciones de tipos de [ARQUITECTURA-REACT](ARQUITECTURA-REACT.md#3-tipos-y-contratos). Props con `busy` no habilitan dobles mutaciones. Eventos se invocan una vez y devuelven control al contenedor.

## 5. Estado y flujo de datos

- **Local:** Sin state interactivo; no conexión browser a event bus ni webhooks.
- **Compartido:** sólo sesión no sensible, identidad del contexto y contexto transitorio del flujo; no duplicar datos remotos en stores independientes.
- **Remoto / caché:** Evento versionado alimenta NotificationDelivery, no cache React ni persistencia de tracking.
- **Flujo específico:** Contrato actual Despacho→Ventas no autoriza Marketplace a consumir. I-05 bloquea integración real; mocks versionados permiten probar composición sin fingir suscripción real.
- Cancelar o ignorar respuestas de identidad/selección anterior. No guardar cuerpos sensibles en devtools, logs o analítica. Los cachés privados se eliminan al cerrar o cambiar de sesión.

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente |
|---|---|---|
| `Sin hook navegador; handler evento y renderer servidor` | Orquestar el flujo descrito; presentación consume estado discriminado y callbacks | Funcional F-035, UI F-035, API F-035 |
| Adaptador tipado | Validar DTO y mapear error público; sin aceptar shape externo no homologado | Contrato API enlazado |
| Validación local | Ayuda inmediata, nunca reemplaza validación ni autorización del servidor | Reglas siguientes |

Sólo shipmentEventId y estados públicos homologados, no inventar eventos desde GET tracking; sin teléfono/coordenadas del repartidor.

### Operaciones documentadas

- Contrato interno propuesto sólo servidor/worker: `POST /internal/v1/notifications/shipment-update`. Bloqueado por I-05; nunca llamada navegador.

Auth y rutas `/password` se traducen mediante el límite de integración aprobado; no se presupone que ya exista proxy BFF ni CORS habilitado. Rutas `/internal` jamás se consumen desde el navegador. Header, request y response exactos pertenecen al contrato API, no a las props.

## 7. Estados, errores y recuperación

EVENT_VALIDATED → RENDERED → QUEUED; evento duplicado reutiliza entrega; fallo envío no cambia despacho.

- **Carga:** no skeleton ni pantalla de espera React. El renderer/worker espera entrada interna autorizada; el email final no tiene estado interactivo de carga.
- **Vacío / no aplicable:** omitir sólo bloques opcionales ausentes, por ejemplo recomendados/fecha estimada. Payload mínimo inválido no genera un correo de éxito ficticio.
- **Error:** resultado técnico interno del renderer/handler; registrar diagnóstico sanitizado y aplicar política del worker, nunca enviar excepciones o secretos en el correo.
- **Éxito:** contenido HTML/texto válido listo para entrega; renderizar no significa enviado ni leído. El worker F-034 conserva estado de entrega.
- **Reintentos:** internos y acotados según eventKey/versión/deduplicación y G-MAIL; no hay CTA de reintento del proveedor en el navegador.

## 8. Accesibilidad, responsive y pruebas previstas

- Aplicar DS-001: etiquetas visibles, orden semántico, foco visible, controles de 44 px, contraste AA y movimiento reducido. No anidar botones de favoritos dentro de enlaces de tarjeta.
- Anunciar progreso/resultado sin duplicar anuncios; error de campo con `aria-describedby`, feedback con `status`/`alert` según severidad.
- Modal/drawer: nombre accesible, foco atrapado cuando modal, cierre permitido según spec y retorno a un elemento existente. Tras eliminar, foco a siguiente elemento/título.
- Probar desktop y, cuando estén listos los frames, mobile con teclado, zoom/reflow y sin depender de hover. Si es correo: HTML/texto legible sin imágenes/scripts, no aplicar roles de app interactiva.

| Caso técnico | Verificación mínima |
|---|---|
| `RC-F-035-01` | evento repetido una entrega lógica. |
| `RC-F-035-02` | email render sin PII. |
| `RC-F-035-03` | enlace exige sesión/ownership. |
| `RC-F-035-04` | fallo correo no revierte estado. |
| Estados UI | Render y transición de cada estado de la sección 7 y de la spec visual relacionada. |
| Transporte | Fixture de éxito, vacío/no aplicable, validación, autorización, conflicto, timeout y fallo externo que realmente correspondan al contrato. |
| Accesibilidad | Teclado/foco, nombre de controles, anuncios y contraste; pruebas automáticas más revisión manual. |

Pruebas de componentes con mocks del contrato Marketplace; pruebas reales del adaptador externo sólo al cerrar la homologación aplicable. Una demo con mocks no acredita integración real.

## 9. Criterios de aceptación técnica

- [ ] `RC-F-035-CONTRATO`: props, callbacks, DTO y operaciones respetan las specs enlazadas sin campos/endpoints inventados.
- [ ] `RC-F-035-ESTADOS`: todos los estados aplicables tienen render, transición, foco y prueba, incluidos vacíos y errores.
- [ ] `RC-F-035-DATOS`: autorización en servidor, caché aislada por sesión y ninguna persistencia de datos externos o secretos prohibidos.
- [ ] `RC-F-035-PRUEBAS`: casos de la sección 8 pasan y quedan evidencias vinculadas a las tareas.
- [ ] `RC-F-035-INTEGRACION`: condiciones de entrada resueltas y prueba de contrato externa aprobada antes de habilitar el flujo real.

## 10. Condiciones pendientes y límites de implementación

I-05/H-05 y F-033/F-034.

Estos pendientes no se resuelven inventando rutas ni comportamiento. El [registro de decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md) separa las soluciones locales propuestas de las confirmaciones externas. Se puede diseñar, construir componentes puros y probar mocks sin activar una integración bloqueada.

