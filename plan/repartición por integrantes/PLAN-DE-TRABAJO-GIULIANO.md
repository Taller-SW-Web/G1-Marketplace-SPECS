# Plan de trabajo completo — Giuliano Macchiavello

Fecha de elaboración: 14/10/2026. Propuesta operativa basada en el reparto vigente del PO del 13/10/2026. Este documento organiza el trabajo; no acredita implementación, pruebas, aprobación ni liberación de dependencias. El estado de las tareas sigue exclusivamente en `plan/seguimiento/`.

**Instrucción actualizada de Giuliano para esta sesión:** crear commits y subir las ramas de trabajo de cada repositorio, sin subir a main ni abrir PR; Giuliano los preparará manualmente al terminar. Las referencias posteriores a la política general de PR/commit directo no autorizan esas acciones en esta ejecución. La documentación de elementos comunes está en el [catálogo compartido](../../SPECS/ui/sistema-diseno/ELEMENTOS-COMPARTIDOS.md).

## 1. Objetivo y responsabilidades

Entregar el bloque de búsqueda y navegación del catálogo de punta a punta: frontend, backend propio de Marketplace, integración con Productos, pruebas, revisión y evidencia.

| Funcionalidad | Resultado | Objetivo académico |
|---|---|---|
| F-006 | Inicio público, categorías activas y destacados sólo cuando exista selección homologada | S1 / H3, semanas 7–8 |
| F-007 | Búsqueda pública por texto y resultados mínimos | S1 / H3, semanas 7–8 |
| F-008 | Filtros por categoría, marca y precio; panel mobile | S2 / H4, semanas 9–11 |
| F-009 | Orden por nombre A–Z / Z–A delegado a Productos | S2 / H4, semanas 9–11 |
| F-010 | Paginación consistente con todos los criterios | S2 / H4, semanas 9–11 |

Sebastian es el revisor principal de implementación. Leonidas revisa contratos y adaptadores backend; Andres revisa seguridad cuando corresponda. Giuliano revisa el bloque de detalle de Sebastian y custodia DS-001 y los componentes visuales compartidos.

La ruta crítica de H3 es: **V-005 y búsqueda de V-006 → frontend desplegado → BFF Marketplace desplegado → API real de Productos**. La búsqueda debe funcionar públicamente sin esperar la implementación del login.

El paquete visual histórico también conserva V-001–V-004, O-003, O-004 y C-001, con revisión de Jim. Ese diseño no transfiere a Giuliano la implementación de cuenta, checkout ni correo.

## 2. Punto de partida y fuentes

Los tableros locales consultados registran FE/BE/QA/DOC pendientes e INT bloqueada para F-006–F-010. Esto describe la evidencia documental disponible; no es una auditoría del código ni del estado remoto actual.

Antes de ejecutar, contrastar el avance existente en estos repositorios y aprovechar lo que ya esté implementado:

- [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend).
- [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend).
- Este repositorio SPECS para planificación, contratos y seguimiento. El código de la aplicación se desarrolla en sus repositorios respectivos.

Lectura de referencia:

- [Matriz de responsabilidades](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).
- [Paquete individual de implementación](GIULIANO-MACCHIAVELLO-PEREZ.md).
- [Guía colaborativa](GUIA-DE-TRABAJO-COLABORATIVO.md).
- [Decisiones y bloqueos](../DECISIONES-Y-BLOQUEOS.md).
- [S1](../iteraciones/S01-semanas-07-08.md) y [S2](../iteraciones/S02-semanas-09-11.md).
- [DS-001](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md), [arquitectura React](../../SPECS/componentes-react/ARQUITECTURA-REACT.md) y [DevSecOps/pruebas](../DEVSECOPS-Y-PRUEBAS.md).
- Para cada F-006–F-010: funcional, UI, contrato API, componentes React, plan funcional y seguimiento.
- [V-005](../../SPECS/ui/vistas/V-005-inicio.md), [V-006](../../SPECS/ui/vistas/V-006-catalogo-resultados.md), [O-001](../../SPECS/ui/overlays/O-001-filtros-mobile.md) y [paquete visual de Giuliano](../../SPECS/ui/reparto/PAQUETE-GIULIANO.md).

Aplicar la matriz y las iteraciones vigentes para el calendario. Algunos metadatos React todavía dicen Sprint 2 para F-006/F-007; registrar su alineación documental con S1. Para comportamiento y datos, respetar las specs funcionales y API: V-006 conserva referencias antiguas a relevancia/novedades/precio que deben alinearse con F-009 antes de habilitar opciones. Los checks del paquete visual no reemplazan una verificación actual de frames, enlaces y revisión.

## 3. Secuencia de ejecución y presupuesto

Base oficial del bloque: **13 días persona de 8 horas = 104 horas**. Incluye FE, BE, integración, QA/documentación y revisión directa; excluye esperas externas y trabajo transversal recurrente. La siguiente distribución es una propuesta, no una nueva estimación aprobada ni trece días de calendario consecutivos.

| Orden | Paquete de trabajo | Esfuerzo propuesto | Salida verificable |
|---|---|---:|---|
| 1 | Auditar avance, leer contratos y preparar tareas | 1 día | Alcance y dependencias contrastados |
| 2 | Base FE/BE, tipos, tema y componentes mínimos | 1 día | Arranque y build reproducibles |
| 3 | Implementar F-006 en FE y BE | 2 días | Home usable y API propia probada localmente |
| 4 | Implementar F-007 en FE y BE | 2 días | Búsqueda con estados y validación |
| 5 | Integración real, pruebas y entrega H3 | 2 días | URLs y flujo remoto demostrados |
| 6 | Implementar F-008 | 2 días | Filtros desktop/mobile y validación backend |
| 7 | Implementar F-009 | 1 día | Orden contractual completo |
| 8 | Implementar F-010 | 1 día | Navegación de páginas consistente |
| 9 | Regresión, revisión y evidencia H4 | 1 día | Bloque integrado y revisado |
| **Total** | | **13 días** | |

Semana 7: preparación y FE/BE de F-006/F-007. Semana 8: integración, QA y demo H3. Semana 9: desarrollo FE/BE de filtros, orden y paginación; semana 10: integración con ficha/favoritos y correcciones; semana 11: QA, CI/CD, documentación y demo H4. Las semanas son académicas: mapearlas a fechas con el calendario del curso antes de fijar vencimientos.

Registrar horas reales y disponibilidad con Diego. El paquete visual registra 49 puntos visuales/gobernanza; no convertirlos a días ni asumir que caben íntegramente en las 104 horas del bloque. Jim decide y documenta la secuencia adicional si afecta H3/H4. La reserva del equipo del 20 % no constituye automáticamente una reserva individual.

## 4. Preparación inmediata

- [ ] Revisar ramas, estructura, scripts, dependencias, lockfile y código existente en frontend/backend.
- [ ] Contrastar los pendientes de este documento con commits, PR y pruebas ya existentes.
- [ ] Acordar con Sebastian los archivos compartidos: V-006, ProductCard, DTO y navegación hacia ficha.
- [ ] Confirmar la política real de ramas/permisos con Diego y usar `develop` si está disponible según la guía. Si falta, coordinar su creación.
- [ ] Abrir o vincular issues con los TASK-ID existentes, alcance FE/BE, archivos, revisor, dependencia y prueba de aceptación.
- [ ] Resolver G-STACK: React + TypeScript + Next.js App Router están decididos; seleccionar versiones compatibles y un solo UI kit con aprobación registrada y lockfile. Mantine/Tabler siguen como propuesta.
- [ ] Coordinar G-SHELL con Fernando/Jim: cabecera, navegación mobile, footer, marca y enlaces aprobados.
- [ ] Registrar la versión/SHA del contrato de Productos, ruta, parámetros, autenticación técnica, URL por ambiente y datos autorizados para pruebas de I-01.
- [ ] Obtener y verificar enlaces específicos de frames; el enlace al archivo de Figma no acredita cada pantalla.

## 5. F-006 — Inicio y categorías

Frontend:

- [ ] Implementar `/` con HomePageContainer, CategoryGrid, FeaturedProducts y buscador compartido.
- [ ] Mostrar únicamente categorías activas y tarjetas comerciales completas; navegar por ID de categoría y slug de producto.
- [ ] Cubrir carga por región, contenido, sección vacía, inicio sin contenido y error recuperable.
- [ ] Mantener cabecera/búsqueda operativas ante vacío o error; omitir una sección vacía con su título y espacio.
- [ ] Implementar desktop, mobile y teclado; usar DS-001 sin carruseles automáticos.

Backend propio:

- [ ] Implementar `GET /api/v1/catalog/home` según el contrato Marketplace.
- [ ] Derivar categories/featuredProducts de la proyección autorizada, sin exponer campos administrativos.
- [ ] Admitir arreglos vacíos y error público `503 CATALOG_UNAVAILABLE` cuando corresponda.
- [ ] Aplicar timeout y validar datos/enlaces/medios; distinguir un error de una respuesta vacía válida.
- [ ] Mientras G-FEATURED siga abierta, dejar destacados vacíos u omitir la sección. La curaduría por IDs requiere acuerdo antes de implementarse como capacidad real.

Salida: home local probada; integración REAL sólo cuando I-01 tenga configuración, contrato y pruebas verificadas.

## 6. F-007 — Búsqueda y resultados

Frontend:

- [ ] Implementar SearchBox, SearchResultsHeading y resultados mínimos en `/catalogo`.
- [ ] Separar texto en edición de la consulta aplicada; normalizar espacios y validar 2–120 caracteres.
- [ ] Confirmar con Enter una sola vez; aplicar debounce sólo donde corresponda según la interacción acordada.
- [ ] Guardar criterios aplicados en la URL; consulta vacía elimina `q` y vuelve al catálogo.
- [ ] Reiniciar `page=0` al aplicar búsqueda y conservar filtros/orden compatibles.
- [ ] Cubrir carga, resultados, cero resultados, consulta inválida y error con reintento.
- [ ] Cancelar o ignorar respuestas anteriores para que una búsqueda lenta no reemplace la nueva.
- [ ] Compartir ProductCard/DTO con Sebastian; mantener navegación y favorito como controles separados.

Backend propio:

- [ ] Implementar `GET /api/v1/catalog/products?q={texto}&page=0&pageSize=24`.
- [ ] Repetir la validación en servidor; consulta inválida devuelve `400 INVALID_SEARCH_QUERY` sin llamar a Productos.
- [ ] Adaptar búsqueda pública paginada y proyectar sólo datos comerciales autorizados.
- [ ] Traducir fallos externos a errores públicos seguros; cubrir 401/403/429/5xx y timeout según el contrato, sin inventar códigos de salida.
- [ ] Registrar hash de consulta y diagnóstico sanitizado; mantener token técnico exclusivamente en backend.

Salida: búsqueda FE→BFF probada con fixtures MOCK, seguida de prueba autorizada con Productos REAL.

## 7. Cierre de H3

- [ ] Leonidas revisa adaptador, validaciones, mapeos y contrato.
- [ ] Sebastian revisa PR y estados UI; Giuliano corrige observaciones.
- [ ] Entregar a Andres configuración por ambiente, requisitos de health y build, sin secretos en Git.
- [ ] Comprobar frontend y BFF en URLs públicas y CORS para el origen aprobado.
- [ ] Probar desde la web publicada una búsqueda que llegue a Productos real y verificar la respuesta remota.
- [ ] Ejecutar casos positivos/negativos, vacío/error/timeout, responsive, accesibilidad y QA de seguridad aplicable sobre entornos propios/autorizados.
- [ ] Coordinar smoke con Fernando, verificación con Diego y aceptación con Jim.
- [ ] Vincular commit, PR, contrato/SHA, URLs, comandos/resultados y capturas/logs sanitizados.
- [ ] Aportar el flujo real para que el equipo actualice los diagramas al despliegue; ensayar demo y recuperación con Andres.

Si I-01 no está liberada: continuar componentes, validadores y tests MOCK; registrar el bloqueo con Diego/Jim. No presentar fixture, health aislado o archivo de despliegue como H3 integrado. Los controles de favoritos/auth pendientes se entregan como integración futura explícita, sin dar por completos esos bloques.

## 8. F-008 — Filtros

- [ ] Implementar CatalogFilters y ActiveFilterChips: categoría, marca y rango PEN.
- [ ] Usar IDs activos publicados; combinar criterios con AND y validar importes no negativos y mínimo ≤ máximo.
- [ ] Extender la ruta de productos con `categoryIds`, `brandIds`, `minPrice`, `maxPrice`; rango inválido devuelve `400 INVALID_PRICE_RANGE` y no consulta al proveedor.
- [ ] Homologar maestros y sus mapeos con Productos/Leonidas; no inventar un endpoint BFF de maestros aún pendiente.
- [ ] Desktop: panel lateral. Mobile: integrar la variante catálogo de O-001 diseñada por Sebastian.
- [ ] Separar borrador de filtros aplicados: editar o Limpiar dentro del overlay no cambia URL/resultados hasta Aplicar.
- [ ] Aplicar reinicia página y conserva búsqueda/orden; Cancelar/Escape descartan borrador.
- [ ] Atrapar foco en el modal, bloquear scroll del fondo y restaurar foco al cerrar; al Aplicar, dirigirlo al encabezado según la spec.
- [ ] Cubrir vacío/error, chips removibles y rango inválido; no mostrar conteos previstos sin contrato.

## 9. F-009 — Orden

- [ ] Implementar CatalogSortSelect con “Nombre: A–Z” y “Nombre: Z–A”.
- [ ] Validar `NAME_ASC | NAME_DESC` en el BFF y mapear a `NOMBRE_ASC | NOMBRE_DESC` de Productos.
- [ ] Rechazar otros valores con `400 INVALID_SORT` y no reenviarlos.
- [ ] Homologar orden estable y desempate por identificador; no ordenar solamente las tarjetas de la página actual.
- [ ] Cambiar orden conserva búsqueda/filtros y reinicia página cero.
- [ ] Registrar la alineación de V-006 con F-009: relevancia, novedad y precio permanecen fuera de UI y solicitudes hasta nuevo contrato homologado.

## 10. F-010 — Paginación

- [ ] Implementar CatalogPagination con anterior/siguiente, página actual y total cuando exista.
- [ ] API cero basada; número visible = `page + 1`; tamaño inicial 24 y máximo 48.
- [ ] Validar enteros `page >= 0` y `1 <= pageSize <= 48`; inválidos devuelven `400 INVALID_PAGE` sin llamada externa.
- [ ] Mapear `data` y metadata `number`, `size`, `totalElements`, `totalPages` según el contrato.
- [ ] Conservar query/filtros/orden al paginar; cambiarlos reinicia página cero.
- [ ] Resolver V-006-OPEN-03 con Leonidas/Productos antes de cerrar: página fuera de rango vacía controlada o recuperación contractual a página válida.
- [ ] Deshabilitar anterior en primera y siguiente en última; evitar consultas infinitas y carga del catálogo completo.
- [ ] Anunciar actualización y conservar un foco válido conforme a la spec de la vista.

## 11. Pruebas y cierre H4

| Área | Casos mínimos |
|---|---|
| Home | Categorías/tarjetas activas; incompletas omitidas; ambos arreglos vacíos ofrecen catálogo; error no rompe cabecera |
| Búsqueda | 1 y 121 caracteres rechazados; límites 2/120 aceptados; espacios normalizados; vacía limpia q; cero conserva criterios; respuesta anterior ignorada |
| Filtros | AND correcto; IDs inválidos/inactivos; negativo/rango invertido sin consulta; Aplicar/Limpiar; Cancelar/Escape sin cambio aplicado |
| Orden | Ambos enums mapeados; desconocidos rechazados; estabilidad; página cero; ausencia de orden local parcial |
| Páginas | Primera/última; criterios conservados; reinicio; enteros/límites; URL inválida y fuera de rango sin bucles |
| Resiliencia | Errores externos contractuales, timeout y recuperación; error distinto de cero resultados |
| Seguridad/accesibilidad | Sin secretos/datos privados; XSS e inputs manipulados; CORS; teclado/foco/labels/anuncios/contraste; desktop y mobile |

- [ ] Ejecutar scripts reales de instalación reproducible, build, typecheck, lint y tests FE/BE disponibles en cada repositorio; registrar comando y resultado, sin atribuir ejecuciones a este plan.
- [ ] Vincular cada criterio funcional/UI/API/React a un caso y evidencia; cubrir QA-001 y QA-002.
- [ ] Homologar integración real de F-008–F-010 y regresión de F-006/F-007.
- [ ] Verificar ida a ficha y retorno con Sebastian, preservando criterios/página; integrar controles de favoritos con Diego cuando su contrato esté listo.
- [ ] Documentar OpenAPI BFF versionado y ejemplos de entrada, salida y error.
- [ ] Con Andres/Diego, evidenciar un cambio que recorra build→test→deploy y validar el catálogo en el segundo demo.
- [ ] Corregir hallazgos y obtener revisión independiente; registrar aceptación funcional con Jim.

## 12. Custodia visual y paquete de diseño

Trabajo transversal que debe calendarizarse junto al bloque con Diego/Jim:

- [ ] Mantener tokens DS-001 y su equivalencia con el tema frontend; resolver pendientes de UI kit, logo/activos, tonalidades y publicación.
- [ ] Priorizar componentes necesarios para H3: buscador, botones/campos, ProductCard, header, skeleton, vacío/error y feedback O-010.
- [ ] Revisar diseños V-005/V-006 con Fernando y O-001 con Sebastian; coordinar anchos, columnas y estados accesibles.
- [ ] Registrar variantes, uso, versión y changelog; comunicar cambios a quienes consumen componentes.
- [ ] Revisar UI de detalle de Sebastian en S2 y productos relacionados F-015 en S5.
- [ ] Verificar el paquete propio de diseño: V-001, V-002, V-003, V-004, O-003, O-004 y C-001; completar estados/desktop/mobile y enlaces pendientes.
- [ ] Seguir el orden visual de su paquete: foundations de formularios → login/registro → recuperación/restablecimiento → O-003 → O-004 → C-001.
- [ ] Hacer handoff de diseños de acceso a Jim, O-004 a Leonidas y C-001 a Fernando; coordinar relaciones visuales según el inventario sin alterar autorías históricas.
- [ ] Obtener revisión de Jim para el paquete propio; mantener explícitas las decisiones abiertas de auth, cierre de checkout y correo.

Diseñar V-001–V-004 no agrega F-001–F-005 al bloque de implementación de Giuliano. Diseñar C-001 no agrega el worker/proveedor de correo a su backend.

## 13. Colaboración, Git y evidencia

| Persona | Coordinación concreta |
|---|---|
| Sebastian | Revisión principal; V-006, ProductCard/DTO, ficha/retorno, diseño O-001 y revisión recíproca de detalle |
| Leonidas | Contrato Productos, validaciones, adaptador y política de página fuera de rango |
| Fernando | Diseño V-005/V-006, coherencia visual y smoke H3; handoff C-001 |
| Andres | Entorno, despliegue, CORS, secretos, health y revisión de seguridad aplicable |
| Diego | Tareas/dependencias, integración de favoritos, capacidad real y verificación del hito |
| Jim | Decisiones funcionales/UI kit/shell, aceptación y revisión del paquete visual propio |

Usar ramas cortas por repo/unidad revisable, por ejemplo `feat/s1-f007-resultados` y `feat/s1-f007-bff`, con PR hacia `develop` según política confirmada. Vincular TASK-ID, tests, capturas y revisión independiente. Para SPECS, la política histórica de commit directo a main queda sustituida en esta sesión por commits/publicación exclusivamente en la rama de trabajo. No abrir PR: lo hará Giuliano manualmente al terminar.

Para cada F de 006 a 010, conservar sus seis tareas existentes: `TASK-F00x-FE-001`, `BE-001`, `INT-001`, `QA-001`, `QA-002` y `DOC-001` (en F-010, prefijo `TASK-F010`). Son 30 tareas ya planificadas; no duplicarlas por pantalla, estado o breakpoint. Actualizar los archivos de [seguimiento](../seguimiento/README.md) con evidencia real.

Cada nota individual en el PR o `docs/evidencias/<hito>/` del repo de código incluye: fecha/entorno, F/TASK-ID, specs/versión/frame verificado, decisiones, archivos y autoría manual/IA, comandos/casos/resultados, commit/PR/revisor, URL y respuesta sanitizada, limitaciones y etiqueta MOCK/REAL. Indicar uso de IA y revisión humana; si no se usó, registrarlo.

Hacer check-in diario breve: hecho, siguiente, bloqueo y evidencia. Ante desviación de horas o dependencia externa, avisar a Diego/Jim para resecuenciar con registro.

## 14. Continuidad hasta H6

S3: sostener home/catálogo durante integración de carrito/checkout; revisar cambios de componentes compartidos y ejecutar regresión cuando afecten el bloque. S4: colaborar en QA responsive/accesibilidad y evidencia visual de la integración sin asumir implementación de eventos/pedidos. S5: revisar F-015 y los diseños de recuperación que consumirá Jim; cerrar observaciones del paquete visual y aportar regresión final del catálogo, documentación y explicación individual.

Checklist final del bloque:

- [ ] F-006–F-010 cumplen comportamiento, datos, estados y responsive vigentes.
- [ ] Frontend y BFF están desplegados y la integración REAL con Productos está probada.
- [ ] PR revisados; QA funcional y seguridad aplicable ejecutadas; observaciones corregidas.
- [ ] Evidencias y tareas coherentes con el resultado; ninguna INT se cierra por un fixture.
- [ ] Componentes/DTO entregados a sus consumidores y versión de diseño registrada.
- [ ] Giuliano puede explicar personalmente UI, backend, adaptador, una prueba positiva/negativa y cada dependencia pendiente.

## 15. Primera sesión de trabajo

1. Auditar repositorios y comparar implementación/evidencia existente con el tablero.
2. Leer F-006/F-007 en las cuatro capas y confirmar contrato mínimo I-01.
3. Coordinar archivos/revisión con Sebastian y adaptador con Leonidas; registrar pendientes con Diego/Jim.
4. Preparar ramas/issues asociados a FE/BE de F-006/F-007.
5. Preparar tipos y fixtures fieles al contrato y construir un primer corte de búsqueda UI→BFF con caso válido/inválido.
6. Abrir PR revisable, etiquetar evidencia MOCK o REAL según lo ejecutado y preparar el siguiente paso hacia despliegue real H3.
