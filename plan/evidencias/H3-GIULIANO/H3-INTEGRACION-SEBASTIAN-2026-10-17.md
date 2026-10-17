# Integración de Sebastián en las ramas de Giuliano — H3 — 17/10/2026

Por solicitud de Giuliano se revisan las ramas remotas de Sebastián y se incorporan sus cambios nuevos, conservando el historial mediante merges en las ramas personales. Las revisiones F-011 fusionadas anteriormente en develop ya formaban parte del corte anterior; este registro identifica sólo los avances posteriores y sus ajustes de integración.

## Revisiones

| Repositorio | Rama de Sebastián | Origen incorporado | Merge publicado en la rama de Giuliano |
|---|---|---|---|
| Backend | `feat/h3-f011-f015-detalle-de-producto` | [a35ad431977bb2a7ed4cf04b76ca930341e18815](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/a35ad431977bb2a7ed4cf04b76ca930341e18815) | [1507766823466448737d3b1ed046a669794f8bd6](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/1507766823466448737d3b1ed046a669794f8bd6) |
| Frontend | `feat/h3-f011-f015-detalle-de-producto` | [25778e1a59a2c1e4412324dd72421aa3584e3648](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/25778e1a59a2c1e4412324dd72421aa3584e3648) | [9e5f5af2c0aa8840630b9025f34743018c03c47a](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/9e5f5af2c0aa8840630b9025f34743018c03c47a) |

Destino en ambos repositorios: `feat/s1-f006-f007-catalogo`. Cada merge conserva dos padres: el HEAD previo de Giuliano y la revisión de Sebastián. Se verifica que los orígenes incorporados y develop son ancestros de las ramas resultantes.

Durante la revisión Sebastián publicó una sincronización adicional con develop. También se incorpora: [Backend fdf78ee](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/fdf78ee8c144841980404de68eff5581dd6cbfda) mediante [d448b71](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/d448b71b4a7f1dc06579ea58143986d1a2e29c7e), y [Frontend 7dc0d9f](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/7dc0d9fabbaa6eef66efcb068500dd36f624425e) mediante [88bb0e1](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/88bb0e1f94382ff0365100fdc210650823fe4772). Se verifica que estos últimos merges no cambian ningún archivo respecto de los merges iniciales: sus árboles Git coinciden exactamente. CI Frontend conserva el pin Backend `1507766`, que tiene el mismo contenido que `d448b71`.

No se encontró una rama propia ni un PR de Sebastián en SPECS. La rama `docs/giuliano-elementos-compartidos` actualiza únicamente esta evidencia, su índice y la entrega personal. No se fusionan las ramas de pruebas de Andrés ni se modifica main, develop o las ramas de Sebastián.

## Cambios incorporados y resolución

- **Contrato de errores F-011:** el Backend responde 400/404/503/504 de ficha como `application/problem+json`, con `type`, `title`, `status`, `code`, `instance` y `requestId`. Conserva o genera `X-Request-Id`; los errores de otros módulos conservan su contrato.
- **Bootstrap compartido:** el middleware de correlación se instala en `configureApp`, utilizado por el arranque y las pruebas HTTP. El interceptor de inicio/búsqueda reutiliza el ID validado en lugar de generar otro. Así Next, listado, detalle y adaptador pueden correlacionar la misma solicitud.
- **Filtro de ficha:** el ID devuelto en cabecera coincide siempre con el cuerpo, incluso cuando un controlador se prueba sin middleware.
- **Conflicto textual Frontend:** `src/app/api/catalog/[...path]/route.ts` delega en el nuevo `bff-proxy.ts` de Sebastián. El helper conserva su correlación y errores propios Problem Details y reutiliza `marketplaceApiUrl` de Giuliano para admitir sólo HTTP loopback o Docker explícitamente autorizado, además de HTTPS. Se mantienen rutas completas por slug, query, cancelación, timeout y rechazo de redirecciones.
- **Ficha server-side:** conserva el mismo helper de origen aprobado y el 404 HTTP dentro de Docker.
- **Corrección de alcance en ficha:** el merge inicial incorporó el botón simulado «Agregar al carrito». Tras contrastar UI-F011-09 y la sección 3 de la spec UI F-011, se retira el botón, su confirmación ficticia, estado y estilos exclusivos. La región comercial se omite hasta disponer de la integración correspondiente. No se añaden precio, stock, variantes ni checkout completo; F-016 conserva su responsable y evidencia independiente.
- **Lockfile y suites:** se incorpora la sincronización del lockfile; se conservan todas las suites ya combinadas, el proxy de sesión anónima y el control positivo determinista de seguridad. CI Frontend fija el Backend integrado `1507766`.

## Verificación

Las pruebas locales usan copias de archivos versionados en carpetas temporales, sin `.env` privados, con dependencias ya instaladas, fixtures y repositorios simulados. No se aplican migraciones ni se consulta G6. La compilación de Next en esa copia local quedó impedida por el enlace de dependencias entre discos C: y D:; el build y el navegador del conjunto se verifican en el CI Linux enlazado abajo.

| Comprobación local | Resultado |
|---|---|
| Backend lint/tipado | PASS |
| Backend unitarias | 139 PASS |
| Backend HTTP | 140 PASS |
| Emisor sintético + comprobador G6 | 4 + 5 PASS |
| **Backend total** | **288 PASS** |
| Frontend componentes, detalle y rutas | 185 PASS |
| Frontend servidor | 41 PASS |
| Frontend lint | Sin errores; una advertencia heredada en `OrdersHistory.tsx` |

El CI Linux confirmó además **25 pruebas de navegador aprobadas y 1 omitida** (checkout persistido optativo), build/tipado y **7 comprobaciones Docker aprobadas**. Total consolidado de casos distintos: **539 PASS, 1 omitido**, más las siete comprobaciones Docker. No se suman las repeticiones locales/CI ni el corte anterior de 507 casos.

Las regresiones de integración nuevas comprueban el ID recibido por inicio/listado/detalle, los errores de ficha 404/503/504 dentro del AppModule compartido, el rechazo del HTTP interno no aprobado y el problema de ficha a través del proxy con origen Docker aprobado. Los conteos incluyen suites del equipo y no suman repeticiones.

CI del conjunto: [H3 Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/39016054262), [validación de PR Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/39016057003) y [H3 Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/39016074443), todos **PASS**, incluidos build, tipado, seguridad y Docker.

Los últimos merges, sin cambios de archivos, tienen además estas revalidaciones automáticas sobre sus SHA finales: [H3 Backend final](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/39016322131), [validación de PR Backend final](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/39016324518) y [H3 Frontend final](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/39016322967).

La comprobación Docker pasa de seis a siete casos: readiness de PostgreSQL desechable, inicio/listado/detalle correlacionados, 404 server-side, Problem Details 404 correlacionado a través de Next/BFF y carrito anónimo. CI usa su propio stack y aplica las migraciones del baseline sólo a esa base desechable.

## Conservación y límites

### Alcance parcial de F-011 en H3

El [paquete individual de Sebastián](../../repartición%20por%20integrantes/SEBASTIAN-MALCA-AGUERO.md) incluye en semana 8 abrir una ficha desde una tarjeta, mostrar datos descriptivos y estados mediante BFF MOCK. La funcionalidad completa corresponde a H4/S2, semanas 9–11. Este avance no autoriza controles comerciales que sólo simulen éxito: la [spec UI F-011, sección 3 y UI-F011-09](../../../SPECS/ui/F-011-detalle-producto.md) exige omitir la capacidad no disponible.

La [corrección Frontend 1524fa3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/1524fa303b164bc064f0c740b31cb00f2ac96a9c) mantiene las pruebas existentes de componente y navegador y restaura la expectativa de ausencia de texto/controles de carrito en la ficha. La prueba local focalizada en el checkout Frontend aprobó sus diez casos, sin arrancar Backend ni aplicar migraciones; lint terminó sin errores, con la advertencia heredada de OrdersHistory. El [CI de esta corrección](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/39017167157) verifica el conjunto. Los resultados de integración anteriores conservan sus SHA y no se suman otra vez.

El `.env` privado y el Docker habitual de Giuliano no se reemplazan. `next-env.d.ts` se guardó y restauró byte por byte; se retiró sólo el stash temporal de esta integración. La guía privada de presentación se actualiza y permanece excluida de Git.

Los PR personales [Backend #11](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/11), [Frontend #3](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/3) y [SPECS #2](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/2) conservan destino develop y estado draft. Integrar las ramas no concede revisión humana, aceptación H3, despliegue público ni conexión real con G6.
