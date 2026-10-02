# Decisiones y brechas de integración — Fase 2.6

> [!NOTE]
> **Actualización del 28 de septiembre de 2026:** la sección 5 registra la autorización posterior de una línea base física con las seis entidades. Esta decisión reemplaza únicamente las restricciones de las secciones 3 y 4 sobre crear el DDL inicial; no cierra ni habilita las integraciones `I-02`, `I-04` o `I-05`.

## 1. Decisiones refinadas por la revisión cruzada

| Tema | Decisión para el modelo de Marketplace | Evidencia revisada |
| --- | --- | --- |
| Llave de una línea de carrito | La unicidad será `cartId + sku`, no `productVariantId`. `variantId` puede conservarse como referencia visual, pero `sku` es la unidad que usan inventario, cotización y Ventas. | Contrato de Productos y Ofertas, secciones EXT-OUT-CAT-02 y EXT-OUT-INV-01; contrato de Despacho F-01. |
| Direcciones | Seguridad mantiene la dirección. Marketplace la consulta con el token del titular y manda una copia a Ventas al crear el pedido. | OpenAPI de Seguridad: `/usuarios/{id}/direcciones`. |
| Cotización | Despacho calcula cobertura, costo y plazo con distrito y líneas por SKU. | Contrato de Despacho: `POST /api/v1/cotizaciones`. |
| Orden duplicada | Marketplace mantiene `CheckoutOperation` y reutiliza `Idempotency-Key`; no convierte el carrito ni el pago en una orden local. | Decisión SDD de Fase 2.5; requiere homologación de Ventas. |
| CSAT de `F-040` | La calificación, comentario y futuros motivos son propiedad de Ventas y Postventa. Marketplace guarda sólo el estado de presentación UX `PostDeliveryPrompt`. | Contrato de Ventas y Postventa: `POST /api/v2/csat`. |
| Eventos | Marketplace no consume eventos internos sin contrato publicado. Para tracking usa REST; para notificaciones necesita un contrato externo homologado. | Contrato de Despacho: eventos actuales hacia Ventas. |

## 2. Brechas que requieren homologación externa

El detalle ejecutable, los payloads mínimos y los criterios de aceptación se gestiona como material de coordinación fuera del repositorio, en el Almacén de Contexto. Estas brechas no se dan por cerradas hasta que el módulo dueño publique el contrato/configuración y se valide una prueba de contrato.

| ID | Brecha detectada | Funcionalidades afectadas | Resolución requerida |
| --- | --- | --- | --- |
| `I-01` | Productos y Ofertas confirma semántica de catálogo (producto activo, slug, atributos vigentes e imágenes obligatorias), pero las rutas HTTP y autenticación de canal siguen `TBD` bajo `OPEN-03`. | `F-006`–`F-016`, `F-024`, `F-031`, `F-039`. | Solicitud `H-01`: OpenAPI, autorización, filtros, errores y prueba de mapeo. |
| `I-02` | Ventas crea pedidos, pero el contrato actual no declara `Idempotency-Key`. | `F-025`–`F-027`. | Solicitud `H-02`: idempotencia obligatoria y prueba de reintento/concurrencia. |
| `I-03` | Ventas lista pedidos con `clienteId` en query, contrario a la decisión Marketplace de derivar identidad del JWT. | `F-028`, `F-029`. | Solicitud `H-03`: `/pedidos/me` o validación documentada de identidad. |
| `I-04` | CSAT acepta puntuación 1–5 y comentario, pero la propuesta UX usa Bien/Regular/Mal y motivos condicionales; no se exige pedido entregado en el contrato visto. | `F-040`. | `H-04`: mapeo fijado 5/3/1; falta validar entrega y publicar motivos. |
| `I-05` | Despacho publica cambios de estado hacia Ventas, no hacia la notificación de Marketplace. | `F-034`, `F-035`. | Solicitud `H-05`: Ventas reexpone evento/webhook versionado para Marketplace. |
| `I-06` | Despacho requiere los scopes `cotizaciones:calcular` y `seguimientos:leer` para el cliente técnico de Marketplace. | `F-023`, `F-032`. | Solicitud `H-06`: registrar cliente técnico de mínimo privilegio y probar scopes. |

## 3. Criterio para iniciar Fase 3

La base lógica ya permite iniciar la elaboración incremental de specs. No autoriza código todavía.

- Se puede iniciar el piloto `F-011` porque depende de catálogo y variantes, y su contrato puede documentar explícitamente la condición `I-01` sin tocar checkout o eventos.
- `F-022` puede especificarse usando el contrato ya publicado por Seguridad.
- Las specs de checkout, historial, notificaciones y CSAT deberán incluir sus brechas como decisiones de contrato pendientes y no pasar a plan/tareas de implementación hasta cerrarlas.

## 4. Criterio para pasar a modelo físico

Una entidad del modelo lógico se lleva a Prisma únicamente cuando la spec correspondiente esté aprobada. El primer lote físico razonable es `Cart`, `CartItem` y `WishlistItem`; `CheckoutOperation` y `PostDeliveryPrompt` se añaden cuando se hayan cerrado `I-02` y `I-04`, respectivamente.

## 5. Actualización posterior: línea base física

Se autoriza crear y mantener [`04-esquema-inicial-postgresql.sql`](04-esquema-inicial-postgresql.sql) como línea base física ejecutable de las seis entidades locales para desarrollo, revisión y documentación técnica.

Esta autorización:

- reemplaza la indicación de la sección 3 que no autorizaba código y la secuencia de primer lote descrita en la sección 4;
- permite materializar `Cart`, `CartItem`, `WishlistItem`, `CheckoutOperation`, `PostDeliveryPrompt` y `NotificationDelivery` en PostgreSQL 16;
- no declara homologados los contratos externos ni autoriza activar consumidores bloqueados;
- mantiene `I-02`, `I-04` e `I-05` como condiciones obligatorias antes de activar checkout hacia Ventas, CSAT y actualizaciones de despacho, respectivamente;
- exige que cualquier cambio posterior al esquema se implemente mediante una migración incremental y actualice la documentación física.
