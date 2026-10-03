# Spec de componentes React — F-028 Consultar historial de pedidos

> Traducción técnica de las specs vigentes; no es código implementado ni aprobación de un contrato externo pendiente.

## 1. Metadatos y trazabilidad

| Campo | Valor |
|---|---|
| ID funcional | `F-028` |
| Versión / estado | `0.1.0` / En revisión |
| Fecha | 2026-10-02 |
| Funcional | [F-028](../funcional/F-028-historial-pedidos.md) |
| UI funcional | [F-028](../ui/F-028-historial-pedidos.md) |
| Contrato API | [F-028](../contrato-api/F-028-historial-pedidos.md) |
| Entregables visuales | [V-015](../ui/vistas/V-015-historial-pedidos.md) |
| Base transversal | [Arquitectura React](ARQUITECTURA-REACT.md), [DS-001 v0.2.0](../ui/DS-001-sistema-diseno-marketplace.md) |
| Stack | React + TypeScript; Next.js App Router propuesto por arquitectura existente; librería UI pendiente de DS-OPEN-03 |
| Responsables de implementación | Propuesta explícita en [plan F-028](../../plan/funcionalidades/F-028-historial-pedidos.md); no reemplaza el reparto de mockups |
| Iteración objetivo | Sprint 5, sujeto a puertas de entrada y capacidad confirmada |

## 2. Rutas y pantallas

| Ruta / superficie | Acceso | Composición |
|---|---|---|
| `/mis-pedidos` | JWT del titular | `OrdersHistoryContainer` + `OrderList` |

Los enlaces de vistas/overlays definen todos los frames y variantes; no crear un nuevo ID V para un estado de la misma pantalla. Desktop se produce primero; mobile sigue dentro del alcance, no se elimina ni se simula reduciendo el desktop.

## 3. Árbol de componentes

```text
Layout de ruta → límite público/privado correspondiente
├── OrdersHistoryContainer
└── OrderList
    └── Feedback accesible compartido según estado
```

El contenedor coordina transporte/estado; los componentes presentacionales no llaman servicios externos ni contienen reglas de descuento, stock o autorización.

## 4. Contratos de componentes

| ID / componente | Responsabilidad | Props tipadas (propuesta) | Eventos |
|---|---|---|---|
| `CMP-F028-001` · `OrdersHistoryContainer` | Sólo historial propio. | `page: PageMeta; orders: OrderSummaryDTO[]; status: QueryStatus` | onPageChange(page); onRetry() |
| `CMP-F028-002` · `OrderList` | Tabla desktop/cards mobile con códigos/fechas/total/estado. | `orders: OrderSummaryDTO[]` | onOpenOrder(orderId) |

Los nombres de DTO y drafts son contratos TypeScript de implementación, no nuevos campos de la API. Su estructura se deriva exclusivamente del contrato enlazado; aplicar las convenciones de tipos de [ARQUITECTURA-REACT](ARQUITECTURA-REACT.md#3-tipos-y-contratos). Props con `busy` no habilitan dobles mutaciones. Eventos se invocan una vez y devuelven control al contenedor.

## 5. Estado y flujo de datos

- **Local:** Foco/paginación aplicada; filtros F-029.
- **Compartido:** sólo sesión no sensible, identidad del contexto y contexto transitorio del flujo; no duplicar datos remotos en stores independientes.
- **Remoto / caché:** ['orders','me',sessionScope,{page,pageSize,state,from,to}]; sin clienteId en URL/request; limpiar en cambio identidad.
- **Flujo específico:** GET BFF /orders/me deriva usuario JWT, backend autoriza contra Ventas. Lista enlaza detalle por orderId opaco.
- Cancelar o ignorar respuestas de identidad/selección anterior. No guardar cuerpos sensibles en devtools, logs o analítica. Los cachés privados se eliminan al cerrar o cambiar de sesión.

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente |
|---|---|---|
| `useMyOrders` | Orquestar el flujo descrito; presentación consume estado discriminado y callbacks | Funcional F-028, UI F-028, API F-028 |
| Adaptador tipado | Validar DTO y mapear error público; sin aceptar shape externo no homologado | Contrato API enlazado |
| Validación local | Ayuda inmediata, nunca reemplaza validación ni autorización del servidor | Reglas siguientes |

page0/pageSize10 inicial; sólo meta de Ventas, no orden local. Error no equivale sin pedidos.

### Operaciones documentadas

- `GET /api/v1/orders/me?page=0&pageSize=10`

Auth y rutas `/password` se traducen mediante el límite de integración aprobado; no se presupone que ya exista proxy BFF ni CORS habilitado. Rutas `/internal` jamás se consumen desde el navegador. Header, request y response exactos pertenecen al contrato API, no a las props.

## 7. Estados, errores y recuperación

LOADING → LIST | EMPTY | FILTER_EMPTY | ERROR;401 oculta datos y ofrece login seguro.

- **Carga:** skeleton de la región que consulta, o progreso local de mutación; nunca datos o importes de ejemplo.
- **Vacío / no aplicable:** sólo ante respuesta válida o condición explícita; errores nunca se convierten en colección vacía, precio cero o stock agotado.
- **Error:** mensaje público y recuperación específica del flujo; errores de campo se asocian a su control. Conservar valores no sensibles cuando sea seguro.
- **Éxito:** se deriva de la respuesta confirmada y actualiza sólo los recursos indicados; no usar navegación, color o cierre del modal como prueba de persistencia.
- **Reintentos:** lecturas acotadas/manuales; mutaciones no se repiten automáticamente si el contrato no garantiza idempotencia. `401` limpia datos privados y ofrece retorno interno seguro.

## 8. Accesibilidad, responsive y pruebas previstas

- Aplicar DS-001: etiquetas visibles, orden semántico, foco visible, controles de 44 px, contraste AA y movimiento reducido. No anidar botones de favoritos dentro de enlaces de tarjeta.
- Anunciar progreso/resultado sin duplicar anuncios; error de campo con `aria-describedby`, feedback con `status`/`alert` según severidad.
- Modal/drawer: nombre accesible, foco atrapado cuando modal, cierre permitido según spec y retorno a un elemento existente. Tras eliminar, foco a siguiente elemento/título.
- Probar desktop y, cuando estén listos los frames, mobile con teclado, zoom/reflow y sin depender de hover. Si es correo: HTML/texto legible sin imágenes/scripts, no aplicar roles de app interactiva.

| Caso técnico | Verificación mínima |
|---|---|
| `RC-F-028-01` | request no clienteId. |
| `RC-F-028-02` | vacío catálogo. |
| `RC-F-028-03` | 401 retira lista previa. |
| `RC-F-028-04` | meta pagina y conserva filtros. |
| Estados UI | Render y transición de cada estado de la sección 7 y de la spec visual relacionada. |
| Transporte | Fixture de éxito, vacío/no aplicable, validación, autorización, conflicto, timeout y fallo externo que realmente correspondan al contrato. |
| Accesibilidad | Teclado/foco, nombre de controles, anuncios y contraste; pruebas automáticas más revisión manual. |

Pruebas de componentes con mocks del contrato Marketplace; pruebas reales del adaptador externo sólo al cerrar la homologación aplicable. Una demo con mocks no acredita integración real.

## 9. Criterios de aceptación técnica

- [ ] `RC-F-028-CONTRATO`: props, callbacks, DTO y operaciones respetan las specs enlazadas sin campos/endpoints inventados.
- [ ] `RC-F-028-ESTADOS`: todos los estados aplicables tienen render, transición, foco y prueba, incluidos vacíos y errores.
- [ ] `RC-F-028-DATOS`: autorización en servidor, caché aislada por sesión y ninguna persistencia de datos externos o secretos prohibidos.
- [ ] `RC-F-028-PRUEBAS`: casos de la sección 8 pasan y quedan evidencias vinculadas a las tareas.
- [ ] `RC-F-028-INTEGRACION`: condiciones de entrada resueltas y prueba de contrato externa aprobada antes de habilitar el flujo real.

## 10. Condiciones pendientes y límites de implementación

I-03, estados publicados Ventas y política fuera de rango.

Estos pendientes no se resuelven inventando rutas ni comportamiento. El [registro de decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md) separa las soluciones locales propuestas de las confirmaciones externas. Se puede diseñar, construir componentes puros y probar mocks sin activar una integración bloqueada.

