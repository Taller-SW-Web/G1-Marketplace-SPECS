# Spec de componentes React — F-020 Fusionar carrito anónimo al iniciar sesión

> Traducción técnica de las specs vigentes; no es código implementado ni aprobación de un contrato externo pendiente.

## 1. Metadatos y trazabilidad

| Campo | Valor |
|---|---|
| ID funcional | `F-020` |
| Versión / estado | `0.1.0` / En revisión |
| Fecha | 2026-10-02 |
| Funcional | [F-020](../funcional/F-020-fusionar-carrito-anonimo.md) |
| UI funcional | [F-020](../ui/F-020-fusionar-carrito-anonimo.md) |
| Contrato API | [F-020](../contrato-api/F-020-fusionar-carrito-anonimo.md) |
| Entregables visuales | [V-001](../ui/vistas/V-001-inicio-sesion.md), [V-008](../ui/vistas/V-008-carrito.md), [O-007](../ui/overlays/O-007-resultado-fusion-carrito.md) |
| Base transversal | [Arquitectura React](ARQUITECTURA-REACT.md), [DS-001 v0.2.0](../ui/DS-001-sistema-diseno-marketplace.md) |
| Stack | React + TypeScript; Next.js App Router propuesto por arquitectura existente; librería UI pendiente de DS-OPEN-03 |
| Responsables de implementación | Propuesta explícita en [plan F-020](../../plan/funcionalidades/F-020-fusionar-carrito-anonimo.md); no reemplaza el reparto de mockups |
| Iteración objetivo | Sprint 3, sujeto a puertas de entrada y capacidad confirmada |

## 2. Rutas y pantallas

| Ruta / superficie | Acceso | Composición |
|---|---|---|
| `Transición postlogin y aviso /carrito` | Autenticada + cookie anónima válida | `CartMergeCoordinator` + `MergeFailureNotice` + `MergeAdjustmentsDialog` |

Los enlaces de vistas/overlays definen todos los frames y variantes; no crear un nuevo ID V para un estado de la misma pantalla. Desktop se produce primero; mobile sigue dentro del alcance, no se elimina ni se simula reduciendo el desktop.

## 3. Árbol de componentes

```text
Layout de ruta → límite público/privado correspondiente
├── CartMergeCoordinator
├── MergeFailureNotice
└── MergeAdjustmentsDialog
    └── Feedback accesible compartido según estado
```

El contenedor coordina transporte/estado; los componentes presentacionales no llaman servicios externos ni contienen reglas de descuento, stock o autorización.

## 4. Contratos de componentes

| ID / componente | Responsabilidad | Props tipadas (propuesta) | Eventos |
|---|---|---|---|
| `CMP-F020-001` · `CartMergeCoordinator` | Dispara sólo tras autenticación final, no antes de MFA. | `sessionReady: boolean; returnPath?: InternalPath` | onMerged(result); onFailed() |
| `CMP-F020-002` · `MergeFailureNotice` | Dos salidas con sesión activa. | `busy: boolean; canRetry: boolean` | onRetry(); onContinueWithoutMerge() |
| `CMP-F020-003` · `MergeAdjustmentsDialog` | O-007, cantidades/causas sin inventario interno. | `adjustments: MergeAdjustment[]; opened: boolean` | onViewCart(); onClose() |

Los nombres de DTO y drafts son contratos TypeScript de implementación, no nuevos campos de la API. Su estructura se deriva exclusivamente del contrato enlazado; aplicar las convenciones de tipos de [ARQUITECTURA-REACT](ARQUITECTURA-REACT.md#3-tipos-y-contratos). Props con `busy` no habilitan dobles mutaciones. Eventos se invocan una vez y devuelven control al contenedor.

## 5. Estado y flujo de datos

- **Local:** MergeState por sesión; decisión de continuar no muta origen ni declara merged.
- **Compartido:** sólo sesión no sensible, identidad del contexto y contexto transitorio del flujo; no duplicar datos remotos en stores independientes.
- **Remoto / caché:** Después de éxito refrescar cart autenticado y descartar caché anónima. 200 merged:false no suma. Cookie sólo BFF.
- **Flujo específico:** Servidor conserva ambos ante fallo e invalida cookie sólo commit. Frontend no puede comprobar HttpOnly: no fuente se conoce por respuesta; retirar opción de retry sólo por evidencia de origen ausente/expirado, no prometer disponibilidad indefinida.
- Cancelar o ignorar respuestas de identidad/selección anterior. No guardar cuerpos sensibles en devtools, logs o analítica. Los cachés privados se eliminan al cerrar o cambiar de sesión.

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente |
|---|---|---|
| `useAnonymousCartMerge` | Orquestar el flujo descrito; presentación consume estado discriminado y callbacks | Funcional F-020, UI F-020, API F-020 |
| Adaptador tipado | Validar DTO y mapear error público; sin aceptar shape externo no homologado | Contrato API enlazado |
| Validación local | Ayuda inmediata, nunca reemplaza validación ni autorización del servidor | Reglas siguientes |

POST sin body, ningún cartId del cliente. 409 MERGE_IN_PROGRESS no iniciar otra fusión paralela. Reintento seguro por garantía transaccional del BFF.

### Operaciones documentadas

- `POST /api/v1/carts/current/merge-anonymous`

Auth y rutas `/password` se traducen mediante el límite de integración aprobado; no se presupone que ya exista proxy BFF ni CORS habilitado. Rutas `/internal` jamás se consumen desde el navegador. Header, request y response exactos pertenecen al contrato API, no a las props.

## 7. Estados, errores y recuperación

IDLE → MERGING → MERGED | NO_SOURCE | FAILED; FAILED → MERGING o DEFERRED; DEFERRED sólo carrito de cuenta.

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
| `RC-F-020-01` | fusión repetida no suma. |
| `RC-F-020-02` | MFA incompleto no dispara. |
| `RC-F-020-03` | continuar conserva sesión y no fusiona. |
| `RC-F-020-04` | banner de pendientes no revela segundo carrito. |
| Estados UI | Render y transición de cada estado de la sección 7 y de la spec visual relacionada. |
| Transporte | Fixture de éxito, vacío/no aplicable, validación, autorización, conflicto, timeout y fallo externo que realmente correspondan al contrato. |
| Accesibilidad | Teclado/foco, nombre de controles, anuncios y contraste; pruebas automáticas más revisión manual. |

Pruebas de componentes con mocks del contrato Marketplace; pruebas reales del adaptador externo sólo al cerrar la homologación aplicable. Una demo con mocks no acredita integración real.

## 9. Criterios de aceptación técnica

- [ ] `RC-F-020-CONTRATO`: props, callbacks, DTO y operaciones respetan las specs enlazadas sin campos/endpoints inventados.
- [ ] `RC-F-020-ESTADOS`: todos los estados aplicables tienen render, transición, foco y prueba, incluidos vacíos y errores.
- [ ] `RC-F-020-DATOS`: autorización en servidor, caché aislada por sesión y ninguna persistencia de datos externos o secretos prohibidos.
- [ ] `RC-F-020-PRUEBAS`: casos de la sección 8 pasan y quedan evidencias vinculadas a las tareas.
- [ ] `RC-F-020-INTEGRACION`: condiciones de entrada resueltas y prueba de contrato externa aprobada antes de habilitar el flujo real.

## 10. Condiciones pendientes y límites de implementación

I-01; semántica cookie TTL/detección de fuente a documentar con BFF.

Estos pendientes no se resuelven inventando rutas ni comportamiento. El [registro de decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md) separa las soluciones locales propuestas de las confirmaciones externas. Se puede diseñar, construir componentes puros y probar mocks sin activar una integración bloqueada.

