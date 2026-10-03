# Spec de componentes React — F-033 Generar plantilla de correo

> Traducción técnica de las specs vigentes; no es código implementado ni aprobación de un contrato externo pendiente.

## 1. Metadatos y trazabilidad

| Campo | Valor |
|---|---|
| ID funcional | `F-033` |
| Versión / estado | `0.1.0` / En revisión |
| Fecha | 2026-10-02 |
| Funcional | [F-033](../funcional/F-033-generar-plantilla-correo.md) |
| UI funcional | [F-033](../ui/F-033-generar-plantilla-correo.md) |
| Contrato API | [F-033](../contrato-api/F-033-generar-plantilla-correo.md) |
| Entregables visuales | [C-001](../ui/comunicaciones/C-001-correo-confirmacion-pedido.md), [C-002](../ui/comunicaciones/C-002-correo-actualizacion-despacho.md) |
| Base transversal | [Arquitectura React](ARQUITECTURA-REACT.md), [DS-001 v0.2.0](../ui/DS-001-sistema-diseno-marketplace.md) |
| Stack | React + TypeScript; Next.js App Router propuesto por arquitectura existente; librería UI pendiente de DS-OPEN-03 |
| Responsables de implementación | Propuesta explícita en [plan F-033](../../plan/funcionalidades/F-033-generar-plantilla-correo.md); no reemplaza el reparto de mockups |
| Iteración objetivo | Sprint 5, sujeto a puertas de entrada y capacidad confirmada |

## 2. Rutas y pantallas

| Ruta / superficie | Acceso | Composición |
|---|---|---|
| `No ruta web; renderer de correo sólo servidor` | Contrato interno autenticado, nunca navegador | `TransactionalEmailTemplate` + `EmailOrderSummary` |

Los enlaces de vistas/overlays definen todos los frames y variantes; no crear un nuevo ID V para un estado de la misma pantalla. Desktop se produce primero; mobile sigue dentro del alcance, no se elimina ni se simula reduciendo el desktop.

## 3. Árbol de componentes

```text
Servidor / renderer de comunicaciones (sin hidratación)
├── TransactionalEmailTemplate
└── EmailOrderSummary

```

El contenedor coordina transporte/estado; los componentes presentacionales no llaman servicios externos ni contienen reglas de descuento, stock o autorización.

## 4. Contratos de componentes

| ID / componente | Responsabilidad | Props tipadas (propuesta) | Eventos |
|---|---|---|---|
| `CMP-F033-001` · `TransactionalEmailTemplate` | Propuesta de renderer server-only si se adopta React; HTML/texto semántico. | `payload: EmailTemplatePayload; payloadVersion: string; type: EmailType` | — |
| `CMP-F033-002` · `EmailOrderSummary` | Datos mínimos y CTA de comunicación. | `summary: MinimalOrderEmailDTO; orderUrl: SafeConfiguredUrl` | — |

Los nombres de DTO y drafts son contratos TypeScript de implementación, no nuevos campos de la API. Su estructura se deriva exclusivamente del contrato enlazado; aplicar las convenciones de tipos de [ARQUITECTURA-REACT](ARQUITECTURA-REACT.md#3-tipos-y-contratos). Props con `busy` no habilitan dobles mutaciones. Eventos se invocan una vez y devuelven control al contenedor.

## 5. Estado y flujo de datos

- **Local:** Sin estado React interactivo ni scripts, sin listeners ni hidratación.
- **Compartido:** sólo sesión no sensible, identidad del contexto y contexto transitorio del flujo; no duplicar datos remotos en stores independientes.
- **Remoto / caché:** No query desde browser; entrada interna versionada y snapshot autorizado.
- **Flujo específico:** F-034/F-035 worker invoca renderer interno. React Email u otra librería no elegida: estos componentes expresan anatomía, no obligación de instalar librería ni endpoint público.
- Cancelar o ignorar respuestas de identidad/selección anterior. No guardar cuerpos sensibles en devtools, logs o analítica. Los cachés privados se eliminan al cerrar o cambiar de sesión.

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente |
|---|---|---|
| `No hook cliente; renderEmail(payload) sólo servidor` | Orquestar el flujo descrito; presentación consume estado discriminado y callbacks | Funcional F-033, UI F-033, API F-033 |
| Adaptador tipado | Validar DTO y mapear error público; sin aceptar shape externo no homologado | Contrato API enlazado |
| Validación local | Ayuda inmediata, nunca reemplaza validación ni autorización del servidor | Reglas siguientes |

URLs desde configuración permitida, id opaco, auth exigida al abrir. Sin token,documento/dirección. Escape de texto y alternativa text/plain.

### Operaciones documentadas

- Contrato interno sólo servidor/worker: `POST /internal/v1/notifications/render`. No es una query/mutation React cliente.

Auth y rutas `/password` se traducen mediante el límite de integración aprobado; no se presupone que ya exista proxy BFF ni CORS habilitado. Rutas `/internal` jamás se consumen desde el navegador. Header, request y response exactos pertenecen al contrato API, no a las props.

## 7. Estados, errores y recuperación

VALID_INPUT → RENDERED | RENDER_FAILED; recomendaciones vacías/fallidas omiten sección sin impedir correo.

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
| `RC-F-033-01` | sin imágenes texto/CTA útil. |
| `RC-F-033-02` | HTML escapa contenido malicioso. |
| `RC-F-033-03` | misma versión render semántico igual. |
| `RC-F-033-04` | sin recomendaciones correo válido. |
| `RC-F-033-05` | no JS ni secretos. |
| Estados UI | Render y transición de cada estado de la sección 7 y de la spec visual relacionada. |
| Transporte | Fixture de éxito, vacío/no aplicable, validación, autorización, conflicto, timeout y fallo externo que realmente correspondan al contrato. |
| Accesibilidad | Teclado/foco, nombre de controles, anuncios y contraste; pruebas automáticas más revisión manual. |

Pruebas de componentes con mocks del contrato Marketplace; pruebas reales del adaptador externo sólo al cerrar la homologación aplicable. Una demo con mocks no acredita integración real.

## 9. Criterios de aceptación técnica

- [ ] `RC-F-033-CONTRATO`: props, callbacks, DTO y operaciones respetan las specs enlazadas sin campos/endpoints inventados.
- [ ] `RC-F-033-ESTADOS`: todos los estados aplicables tienen render, transición, foco y prueba, incluidos vacíos y errores.
- [ ] `RC-F-033-DATOS`: autorización en servidor, caché aislada por sesión y ninguna persistencia de datos externos o secretos prohibidos.
- [ ] `RC-F-033-PRUEBAS`: casos de la sección 8 pasan y quedan evidencias vinculadas a las tareas.
- [ ] `RC-F-033-INTEGRACION`: condiciones de entrada resueltas y prueba de contrato externa aprobada antes de habilitar el flujo real.

## 10. Condiciones pendientes y límites de implementación

C-001/C-002, proveedor y motor render por confirmar.

Estos pendientes no se resuelven inventando rutas ni comportamiento. El [registro de decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md) separa las soluciones locales propuestas de las confirmaciones externas. Se puede diseñar, construir componentes puros y probar mocks sin activar una integración bloqueada.

