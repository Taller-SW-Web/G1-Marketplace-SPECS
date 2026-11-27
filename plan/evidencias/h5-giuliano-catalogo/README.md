# H5 · Catálogo F-006 a F-010 · Matriz de integración y QA

Retest del 26/11/2026. Frontend `073b3b0` y Backend `5810045`. La [matriz HTTP](matriz-http-mock.json) registra **24 PASS, 0 FAIL, 0 BLOCKED y 1 INCONCLUSIVE** en Next → BFF **MOCK local**. El único caso inconcluso es F009-observed-ties porque el fixture carece de homónimos. La suite de Backend sí cubre el criterio de desempate con datos específicos. [Frontend probado](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/073b3b0a10fac0ba9df324aa02f14ac40523f08d) · [Backend probado](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/581004571d1dd62e22842526c33dd584037cc61e)

| Función | Integración local | QA funcional | QA de seguridad | Criterio del corte publicado |
| --- | --- | --- | --- | --- |
| **F-006 Inicio** | [BE #45][be45] · Home y destacados observados con datos simulados. | [FE #28][fe28] · Categorías, destacados, carga, vacío y error recuperable. | [BE #46][be46] · Consulta en Home rechazada y proyección pública validada. | Inicio REAL en Vercel mostró las diez categorías. El arreglo de destacados llegó vacío en la prueba. Ranking G5 fuera de H5 por decisión del PO. |
| **F-007 Búsqueda** | [BE #49][be49] · Caso positivo, vacío y longitudes inválidas en MOCK. | [FE #30][fe30] · Búsqueda y texto, vacío, timeout y reintento con los criterios conservados. | [BE #50][be50] · Límites, rechazo de parámetros fuera del contrato y proyección pública. | Resultado positivo y vacío en Render. El positivo también pasó en Vercel. Queda registrar el timeout autorizado del entorno. |
| **F-008 Filtros** | [BE #53][be53] · Maestros, categoría, combinación, rango PEN y negativos HTTP. | [FE #32][fe32] · Filtros activos, recuperación y conservación de criterios. | [BE #54][be54] · Validación de filtros inválidos y reglas de exposición. | Maestros y tres rangos de precio en Render. Categoría, marca y rango 0–45 PEN juntos en Vercel móvil. |
| **F-009 Orden** | [BE #57][be57] · Nombre ascendente y descendente por HTTP. Homónimos inconclusos en el fixture. | [FE #34][fe34] · Orden global entre páginas y conservación de filtros. | [BE #58][be58] · Orden inválido rechazado. Suites de Backend prueban desempate. | Homónimos en ASC y DESC por Render. DESC en la vista móvil de Vercel. |
| **F-010 Paginación** | [BE #61][be61] · Primera, siguiente, última y fuera de rango en MOCK. | [FE #36][fe36] · Recuperación al cambiar página y conservación de filtros. | [BE #62][be62] · Límites inválidos de página y tamaño rechazados. La matriz verifica IDs y total. | Sin duplicados entre página 1 y 2 y fuera de rango correcto en Render. Ambas páginas renderizaron el producto esperado en Vercel. |

**Pruebas locales adicionales:** 15 del runner, 91 de Backend y 76 de Frontend, todas aprobadas. Las pruebas unitarias y el recorrido HTTP son evidencias de capas distintas.

## Retest en Render

El 26/11 a las 18:13–18:14 Lima, **11 de 11 lecturas públicas** del BFF de Render devolvieron HTTP 200 con fuente `REAL`. El [registro del retest](retest-real-render.json) conserva hora UTC, resultado y `x-request-id` por caso.

| Caso | Resultado REAL |
| --- | --- |
| Inicio y maestros | Inicio respondió con categorías y el arreglo de destacados. Maestros devolvió categorías y marcas. |
| Búsqueda | Los dos homónimos sintéticos aparecieron en la consulta. La búsqueda de control devolvió cero resultados. |
| Precio | PEN 0–100 y 0–60 incluyeron los dos productos. El rango 0–45 devolvió solo `g6-qa-marketplace-ord-001`. |
| Orden | ASC y DESC conservaron el desempate ascendente por `productId` entre los homónimos. |
| Paginación | Tamaño 1. Páginas 1 y 2 con un ID distinto cada una, total 2. Página 3 vacía, total 2. |

El [503 histórico en BE #53][diag] queda como antecedente. El [retest previo del BFF local contra G7/G6][real-local] aporta nueve lecturas reales anteriores. Las lecturas públicas nuevas acreditan el BFF durante esa ventana. El historial de Render identifica el deploy `dep-dc4b7u3l550s738o8jd0` con SHA `f17896d7ee24876ffd33db1bb7dd91d65623ed37`, activo desde las 22:35:30 UTC y durante el retest. [Ficha del deploy](https://dashboard.render.com/web/srv-db05v0navr4c73e9mnug/deploys/dep-dc4b7u3l550s738o8jd0) · [Commit desplegado](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/f17896d7ee24876ffd33db1bb7dd91d65623ed37)

### Validación de fallos

A las 22:59 Lima se verificaron cinco lecturas negativas sobre el Render público. Cada una devolvió HTTP 400, el código esperado y un ID de solicitud que coincide entre cabecera y cuerpo. [Registro por caso](validacion-parametros-render.json)

| Función | Entrada | Código |
| --- | --- | --- |
| F-006 | Parámetro `q` en Inicio | `INVALID_PARAMETERS` |
| F-007 | Búsqueda de 121 caracteres | `INVALID_SEARCH_QUERY` |
| F-008 | Precio mínimo superior al máximo | `INVALID_PRICE_RANGE` |
| F-009 | Orden fuera del contrato | `INVALID_SORT` |
| F-010 | Página negativa | `INVALID_PAGE` |

El BFF local pasó nueve pruebas HTTP en el mismo código base que Render. Las cuatro nuevas ejercitan 503 en Inicio, filtros y búsqueda, además de agotar el plazo de 100 ms del adaptador real de catálogo con transporte G6 simulado. Verifican respuesta pública correlacionada, recuperación al reintentar y ausencia del cuerpo interno del proveedor. En Chrome las pruebas verifican mensajes diferentes para timeout e indisponibilidad, conservación de la búsqueda y retorno del foco. [Suite de Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/29528af0cecde2fe160f931e15cd32d456ba08de/test/catalog-public-read-only.e2e-spec.ts) · [Evidencia de Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/h5-overlays-carrito/docs/evidencias/H5/UX-013-014-estados/README.md)

Queda provocar de forma autorizada el 503 o timeout de G6 en un entorno integrado y registrar la aceptación por tarea. A las 22:59 Lima, Inicio volvió a entregar 10 categorías y cero destacados en Render y Vercel. [Retest de destacados](retest-destacados.json)

## Retest de catálogo en Vercel

Entre las 18:16:36 y las 18:18:34 Lima se recorrieron Inicio y Catálogo públicos en Chrome. Las cinco respuestas del proxy Next fueron HTTP 200 con fuente `REAL`. El orden, la paginación y la combinación de filtros se probaron abriendo las URL con los criterios correspondientes y comprobando las tarjetas visibles. [Trazas de navegador](retest-real-vercel.json)

| Recorrido | Evidencia |
| --- | --- |
| Escritorio, ASC, página 1, tamaño 1. Solo aparece `ord-002`. | [Captura](vercel-desktop-p1.png) |
| Escritorio, ASC, página 2, tamaño 1. Solo aparece `ord-001`. | [Captura](vercel-desktop-p2.png) |
| Móvil, DESC, tamaño 2. Aparecen `ord-002` y `ord-001` en ese orden. | [Captura](vercel-mobile-desc.png) |
| Inicio en escritorio. El proxy devolvió 10 categorías y cero destacados. Se vieron los enlaces de categorías. | [Captura](vercel-desktop-inicio.png) |
| Móvil con categoría, marca y rango PEN 0–45 a la vez. Solo aparece `ord-001`. | [Captura](vercel-mobile-filtros.png) |

## Reproducción local

Con Frontend y Backend en carpetas hermanas `G1-Marketplace-Frontend` y `G1-Marketplace-Backend`, instalar y compilar ambos antes de ejecutar el runner desde Frontend.

```bash
npm run demo:catalogo:h4 -- --skip-build --check --matrix --featured
```

El runner levanta ambos servicios en loopback y guarda el resultado en `.local-security/catalog-h4-demo.json`. Los casos están versionados en [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/tree/581004571d1dd62e22842526c33dd584037cc61e/scripts/catalog-h4/cases).

[be45]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/45
[be46]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/46
[be49]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/49
[be50]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/50
[be53]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53
[be54]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/54
[be57]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/57
[be58]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/58
[be61]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/61
[be62]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/62
[fe28]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/28
[fe30]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/30
[fe32]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/32
[fe34]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/34
[fe36]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/36
[diag]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53#issuecomment-7202936915
[real-local]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53#issuecomment-7202778407
