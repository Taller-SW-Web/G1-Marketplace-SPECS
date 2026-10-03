# Arquitectura y contratos transversales de componentes React

Versión 0.1.0 · En revisión · 2026-10-02. Diseño técnico, no implementación existente.

## 1. Alcance y precedencia

Cubre F-001–F-040, 17 vistas, 10 overlays y 2 correos. Las funcionalidades siguen siendo la unidad SDD; una vista compone varias funcionalidades. F-033–F-035 no justifican rutas públicas ni llamadas desde el navegador a notificaciones.

Orden de autoridad: funcional para comportamiento, API para operaciones/datos, UI funcional y V/O/C para composición/estados, DS-001 v0.2.0 para tokens, esta carpeta para estructura React. Ante conflicto registrar decisión en [plan](../../plan/DECISIONES-Y-BLOQUEOS.md), no modificar silenciosamente comportamiento.

DS-001 v0.2.0 reemplaza los tokens 0.1.0 aún citados por algunas specs. Mantine/Tabler es dirección preliminar, no migración aprobada. No instalar ni fijar Mantine 9.6.2 sólo porque figure en la guía: validar disponibilidad/compatibilidad y aprobar DS-OPEN-03 al preparar el frontend. No mezclar dos UI kits.

Frontend y backend locales sólo contienen README; no hay package.json, aplicación ni pruebas ejecutables verificadas. Next.js App Router/React/TypeScript, TanStack Query, formularios tipados y NestJS/Prisma son diseños de partida, no afirmación de código instalado. Se seleccionan versiones/lockfile al implementar el Sprint 1.

## 2. Separación por capas y organización propuesta

```text
src/app/                       rutas y layouts, no reglas de microservicios
src/features/auth/             acceso/registro/recuperación
src/features/catalog/          listado y ficha, regiones independientes
src/features/cart/             carrito y coordinación de fusión
src/features/wishlist/         favoritos a nivel producto
src/features/checkout/         dirección/quote/preparación/orden
src/features/orders/           historial/detalle/seguimiento/postentrega
src/shared/ui/                 wrappers de UI kit y compuestos compartidos
src/shared/api/                cliente, DTO, validación y errores públicos
src/shared/session/            estado no sensible, límites privados y limpieza
src/theme/                     equivalencia con tokens DS-001
tests/                         componentes, integración contrato, E2E y seguridad
backend/notifications/         ubicación conceptual en repo backend, NO dentro de bundle web
```

Estas rutas son una propuesta para los repos de código; no se crean en el repo de specs. Componentes server-only no se importan desde módulos cliente. Evitar serializar sesiones, direcciones o contacto en HTML público o props de una caché compartida.

## 3. Tipos y contratos

- `Money = {amount: number; currency: string}` donde el API lo define; precisión y cálculo comercial son responsabilidad del BFF. Formatear es-PE, no recomputar descuentos o total.
- `QueryState<T>`: unión discriminada loading / ready(data) / empty / error(publicError); no combinar error con éxito inventado. Empty sólo corresponde donde el contrato admite colección vacía.
- `QueryStatus`: estado de transporte idle/loading/success/error; no reemplaza el estado de dominio de la sección 7 de cada spec. `PreparationState`, `MergeState`, `QuoteValidity` y `TrackingQueryState` son uniones específicas de esos estados, no enums nuevos de la API.
- `MutationState<T>`: idle / pending / succeeded(result) / failed(error) / uncertain cuando existe resultado incierto; incertidumbre no es fracaso confirmado.
- `SessionState`: anonymous / authenticating / mfa-required / authenticated / expired. Sólo authenticated habilita datos privados; no incluir refresh/access token en props presentacionales.
- `OperationState`: PREPARING, PREPARED, SUBMITTED, SUCCEEDED, FAILED, como backend; no confundir PREPARED con pedido.
- `AvailabilityState`: espera / carga / AVAILABLE / STOCK_LOW / OUT_OF_STOCK / error. Sólo el enum recibido define disponibilidad; error no significa agotado.
- `Sentiment`: GOOD, REGULAR, BAD; el BFF adapta a 5,3,1; `PromptState` refleja ELIGIBLE/SHOWN/DISMISSED/SUBMITTED sólo cuando hay respuesta de servidor.
- `InternalPath`: ruta relativa del Marketplace validada con allowlist; rechazar destinos absolutos, protocol-relative, esquemas y codificaciones evasivas. No confiar en returnPath/redirectUrl recibidos.
- `PublicError`: código reconocido, mensaje público y errores de campos permitidos. requestId permanece diagnóstico sin mostrarlo como copy.
- Cada `...DTO` de las specs es la proyección definida en su API: no inventar campos ausentes. Cada `...Draft` contiene campos de formulario descritos en UI. Tipar callbacks y validar runtime en el límite HTTP; nunca `any` como contrato final.
- Extensiones de DTO, política de contraseña, MFA, maestros de dirección, resúmenes o prompt que no están en API siguen bloqueadas por su decisión correspondiente.

## 4. Estado, consultas y coherencia

Servidor es autoridad; TanStack Query propuesto conserva remoto, contexto/store conserva sesión no sensible y selección transitoria, estado local conserva drafts. No mantener simultáneamente carrito completo en Zustand y query como fuentes independientes.

Claves privadas incluyen ámbito de sesión estable no secreto; no incluir tokens, teléfono, contraseña o documento en claves. Cambio de cuenta/logout cancela requests y destruye cachés privados, drafts, operaciones visibles y comentarios. No persistir esas cachés con plugins de storage.

Criterios de catálogo/historial aplicados van a URL; drafts no. page es cero basado y número visual humano. Todas las claves incluyen criterios completos. Abort/cancel o secuencia de request evita respuesta fuera de orden.

Precio/stock/variantes/descripción de ficha tienen consultas independientes. Precio no se sirve más allá de vigencia; stock cache máximo 30 s; el precio informativo nunca autoriza venta definitiva.

Mutaciones de carrito serializan por versión y reconcilian snapshot confirmado. Cambios de carrito/dirección/beneficio invalidan quote y preparación. No seguir mostrando una quote vigente de otra combinación.

## 5. Seguridad del límite de sesión y microservicios

La protección de ruta React es UX, no autorización. BFF valida JWT, ownership, inputs y scopes, deriva titular, rechaza IDs de cliente manipulados. Sólo APIs autorizadas entre microservicios; nunca Prisma en navegador ni acceso a DB ajena.

- Cookie anónima de F-016: HttpOnly/Secure/SameSite=Lax la administra BFF; JS no la lee.
- Transporte de access/refresh, refresh y MFA: contrato abreviado F-002/003 no fija estrategia completa. Registrar G-AUTH, evaluar BFF/cookie protegida o mecanismo homologado antes de implementar. No crear token de servicio en navegador ni guardar secretos en localStorage.
- Direcciones: BFF de F-022 utiliza token del titular ante Seguridad, no token técnico; sólo memoria temporal web. Sin copia en DB Marketplace.
- Despacho: token técnico cotizaciones:calcular/seguimientos:leer sólo backend. Scopes mínimos, sin sustituir por token del titular.
- Registro: canal fijo MARKETPLACE; verificación/reenvío/enlace vencido o usado en Seguridad; URL /login configurada por ambiente, sin token. Recuperación de contraseña es flujo distinto, F-005 sí recibe token efímero.
- HTTPS, origen CORS explícito, CSP, protección CSRF si cookie autentica mutaciones, prevención XSS/open redirect y redacción de secretos/PII. Política concreta y pruebas en [DevSecOps](../../plan/DEVSECOPS-Y-PRUEBAS.md).
- Medios/catalogo y email: lista permitida de URLs, escape/sanitización; no contenido ejecutable. Backend valida SSRF si proxy/media o fetch externo.
- Ningún dato de tarjeta/CVV; no real cobro ni promesas Pago 100% seguro. Documentos/contacto sólo transitorios hacia Ventas.

## 6. Componentes reutilizables y contrato de composición

| Componente | Props / eventos principales | Contrato de uso |
|---|---|---|
| AppShell / CommercialHeader | sessionState, navItems permitidos; onSearch/onLogin/onLogout | Marca, búsqueda, catálogo, cuenta, favoritos/carrito según DS. Sin enlaces ficticios. |
| CheckoutHeader / CheckoutProgress | currentStep, completedSteps, orderSucceeded | Propuesta previa de Jim: sólo logo + Dirección/Resumen/Pago/Confirmación, sin perfil ni pago seguro. Sin saltar pasos; V-013 confirmación activa, V-014 completo sólo SUCCEEDED. Cierre visual G-SHELL pendiente antes de pixel final. |
| CommercialFooter / CheckoutFooter | approvedLinks, brandAsset, legalText | Anatomía definitiva no formalizada en UI; no crear páginas de ayuda/legal ni enlaces rotos. Propuesta oscura requiere logo inverso aprobado. No tratar pendiente como implementación concluida. |
| ProductCard | DTO público, favoriteState privado separado; onFavorite | Enlace de producto y botón corazón no anidados. Skeleton/error local, sin carrito rápido no especificado. |
| ProductGallery / GalleryViewer | medios, índice, opened; onSelect/onClose | F-011/O-002, finitos, fallback y foco. |
| CartLine / QuantityStepper | línea y versión confirmadas, draft, busy; onCommit/onRemove/onMove | F-017–021, cantidades absolutas, ninguna reserva. |
| OrderSummary | variante cart/quote/confirmed y DTO correspondiente | No reutilizar subtotal de carrito como total de checkout; cada variante conserva etiquetas/origen. |
| EmptyState / InlineError / RegionSkeleton | mensaje, recovery, busy | Vacío no oculta error; reintento sólo región afectada. |
| AccessibleDialog / Drawer | opened,title,closePolicy,triggerRef | Modal traps focus, Escape sólo seguro, foco restituido; O-001 a O-009. |
| FeedbackRegion / UndoFeedback | type,message,action?,timerPolicy | O-010 y O-006; no robar foco ni prometer deshacer sin contrato. |
| OrderTimeline / ShipmentTimeline | hitos publicados,estado,fechas | Snapshots respectivos, no inferencia ni mapa en tiempo real. |

Los wrappers encapsulan UI kit; los nombres anteriores son contratos semánticos, no nombres de librería obligatorios. Un compuesto compartido tiene una única implementación y pruebas de contrato de variantes.

### Feedback transversal O-010

[O-010 Alertas y feedback](../ui/overlays/O-010-alertas-feedback-global.md) se consume desde todas las funcionalidades que requieran feedback no asociado a campo. `FeedbackRegion` recibe `{id, severity, message, placement, action?, dismissible}`; `severity` es info/success/warning/error, `placement` inline/toast/banner. Los textos provienen del mapeo público, no de mensajes crudos del proveedor. `onAction(id)` invoca recuperación específica; `onDismiss(id)` retira sólo ese aviso. Nunca reemplaza un error de campo ni decide autorización.

El contenedor coordina la cola por identidad y deduplica mensajes de una misma operación, no eventos distintos. Estado visible/action-pending/dismissed; CTA de recuperación no repetible. `status` para información no urgente, `alert` para error que exige atención, sin anuncio simultáneo duplicado. No robar foco, no cubrir CTA/footer/controles, ni representar error permanente sólo mediante toast efímero. Timer/cierre según la spec del overlay y accesibilidad; no aplicar la ventana de Deshacer indiscriminadamente.

Pruebas comunes: aviso repetido de la misma operación no duplica anuncio; acción dispara una recuperación; mensaje no contiene token/PII; cambio de cuenta vacía feedback sensible; desktop/mobile no ocultan controles y cierre mantiene foco válido. QA de cada función que lo use cubre su copy y callback, y la regresión transversal verifica el compuesto.

## 7. Matriz de layouts

| Familia | Vistas | Layout |
|---|---|---|
| Acceso | V-001–V-004 | Marca/formulario, ayuda y retorno seguro según cada V |
| Comercial | V-005–V-009 | Navegación comercial y footer por aprobar |
| Checkout | V-010–V-014 | CheckoutHeader compartido, 4 etapas, footer simplificado por aprobar |
| Cuenta/pedidos | V-015–V-017 | Navegación comercial autenticada, datos privados y retorno |
| Correo | C-001/C-002 | Renderer HTML/texto servidor, sin app shell ni scripts |

Móvil sigue la composición UI, no copia desktop escalada. Checkout desktop primero por petición de Jim; no cerrar entrega responsive mientras falten mobile/estados. No reducir alcance por el orden de producción.

## 8. Recuperación y acciones no idempotentes

- Login exitoso + merge fallido conserva sesión, ofrece dos salidas y nunca expone dos carritos. Continuar sin combinar sólo cambia navegación, no llama API nueva.
- GET puede reintentar de forma acotada; POST login/registro/proveedor no tienen retry automático genérico.
- POST agregar/reordenar pueden incrementar cantidades; unicidad de SKU no es idempotencia de cantidad. Timeout exige reconciliar y respetar garantía antes de reenviar.
- DELETE idempotente puede releer; deshacer requiere restauración aprobada, espera DELETE y revalida. Carrito no dispone de endpoint undo definido.
- Idempotencia checkout de preparación y creación necesita cerrar ámbito/fingerprint; no usar misma clave con payload distinto, ni generar otra cuando pedido puede existir.
- Outbox de correo se registra atómicamente con la transición local de CheckoutOperation a SUCCEEDED cuando corresponda. Esa transacción no incluye la base de Ventas ni el proveedor de correo: reconciliar fallo entre respuesta externa y commit local, y deduplicar entrega. La unicidad de NotificationDelivery no garantiza por sí sola ausencia de dos envíos si el proveedor aceptó uno y su respuesta se perdió; G-MAIL debe definir idempotencia o reconciliación del proveedor.
- Confirmación orderId versus operación operationId es brecha real, G-CONFIRM. No pasar orderId al GET de operaciones.
- No polling ilimitado ni endpoints nuevos de lookup/validación/prompt supuestos. Hasta que el contrato permita recuperación tras reload, bloquear esa capacidad real y describir salida segura sin crear pedido duplicado.

## 9. Entregabilidad y pruebas

Unitarias de transformaciones/validadores; componentes/estado/foco con fixtures API; integración BFF/DB/adaptadores; E2E de flujos verticales; seguridad positiva/negativa; responsive/a11y y revisión manual; correo HTML/texto sin recursos externos.

Las specs definen los casos; [plan y seguimiento](../../plan/README.md) define ejecución, responsables propuestos, dependencias y evidencias. Ninguna checklist React está marcada como implementada por crear estos documentos.

