# Selección de Home y preparación del histórico de más vendidos

## Regla confirmada por Giuliano a partir del mensaje de Jim — 03/11/2026

**Prioridad:** destacados definidos → históricos más vendidos → aleatorios sólo cuando todavía no hay historial. Esto sustituye la selección exclusivamente editorial propuesta en el corte anterior. La confirmación de la prioridad y de la métrica no certifica revisión de código, contrato aceptado por el proveedor ni despliegue.

Giuliano eligió documentar como criterio de históricos las **unidades vendidas del canal MARKETPLACE, en todo el historial, con pago confirmado, descontando devoluciones confirmadas**. Se agrupan por producto, no por variante/SKU. La fuente autorizada y su contrato siguen pendientes de homologación; no se calculó un ranking con datos de compradores o importes administrativos.

La alternativa se evalúa al quedar vacía la selección anterior. Una selección definida parcialmente elegible se conserva sin rellenarla con otras fuentes. Si hay historial pero ninguno de sus productos es publicable, la sección puede quedar vacía: no se afirma que no haya historial. Un fallo o ausencia de la fuente de ventas es indisponibilidad técnica y no habilita aleatorios.

## Fuente y contrato por concretar

En la revisión del [contrato G5](https://github.com/Taller-SW-Web/G5-Ventas-Postventas/blob/HEAD/specs/api/api-ventas.md), versión declarada 1.8.0, no se encontró un ranking por producto. Su operación `/api/v1/pedidos/kpis` requiere `ADMIN_VENTAS` y agrega importes por día/canal: no satisface esta necesidad. `/pedidos/me` es historial propio, no ranking global. No se creará una consulta administrativa desde Home ni se expondrán pedidos, compradores, importes, tokens o scopes internos.

Preparación en Backend: puerto de servidor `CATALOG_HOME_SOURCES.salesRanking(signal, requestId)` con `{ hasHistory: boolean, orderedProductIds: string[] }`. La lista está ordenada por ventas, agrupada por producto, sin duplicados y con un máximo técnico de cien candidatos; G1 toma las primeras ocho posiciones y revalida datos/elegibilidad con G6. No se inventó una URL, scope o credencial de G5. El módulo no conecta aún una fuente real: ésta y el adaptador HTTP/eventos/snapshot autorizado se acuerdan con su responsable.

Para homologar ese adaptador se debe fijar con Ventas qué estados prueban pago confirmado, cómo se resta una devolución confirmada, cómo se resuelve SKU a producto y cómo se garantiza un agregado completo del canal MARKETPLACE. El orden por empate puede ser estable por ID como propuesta técnica, pendiente de compatibilizar con la fuente. Una fuente parcial o fallida no puede retornar `hasHistory: false`.

`hasHistory: false` significa que se comprobó ausencia de historial de ventas aplicable; una lista vacía porque los productos vendidos no son publicables conserva `hasHistory: true`. El contrato debe precisar el caso de devoluciones que dejan unidades netas en cero sin borrar la existencia de ventas históricas. No hay una retención temporal elegida: el criterio solicitado usa todo el historial disponible autorizado.

## Comportamiento preparado

Destacados definidos mantienen orden y omiten ausencias comerciales confirmadas. Si no queda ninguno, se consulta el ranking. Sólo cuando la fuente confirma ausencia de historial se realiza un sorteo sin reemplazo sobre posiciones del catálogo completo declarado por G6, con páginas ordenadas y lecturas acotadas. No se completa una selección parcial mezclando fuentes. Si existe historial pero no hay tarjetas elegibles, puede quedar vacío sin pasar a aleatorio.

La muestra se recalcula por nueva lectura de Home. Hay límite técnico de ocho tarjetas, tres lecturas paralelas y un deadline compartido. Los cambios observables del listado se rechazan; la API no ofrece un snapshot global entre llamadas y no se presume esa garantía. La propuesta no introduce caché de catálogo ni persistencia de hechos de Productos en G1.

Los flags predeterminados permanecen desactivados. La confirmación de Giuliano resuelve la prioridad y el criterio que se pide; no significa que G5 ya acepte o publique el agregado, que haya grants, que un revisor apruebe el código o que se haya desplegado. Las issues conservan DoD y estado abierto. No se enviaron solicitudes de revisión, por instrucción de Giuliano.
