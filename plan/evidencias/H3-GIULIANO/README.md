# Evidencias de Giuliano — H3, semanas 7–8

Este documento es el punto de entrada a las evidencias del catálogo y búsqueda, F-006/F-007. Reúne la prueba manual de Giuliano y enlaza los registros técnicos anteriores, que conservan las versiones y resultados de cada avance.

## Prueba manual del 16/10/2026

| Dato | Registro |
|---|---|
| Responsable de la prueba y capturas | Giuliano Macchiavello |
| Entorno | Docker local del equipo; Frontend Next, Backend Nest y PostgreSQL |
| Datos del catálogo | **MOCK**, identificados en la interfaz como catálogo de demostración |
| URL de acceso | http://localhost:3000 |
| Navegador | Microsoft Edge; las capturas muestran zoom de navegador de 90 % |
| Escritorio | Capturas de pantalla de 1920 × 1080; esas medidas incluyen la interfaz del navegador |
| Móvil | Emulación Pixel 5 en DevTools, viewport configurado en 393 × 851; no es una prueba en dispositivo físico |
| Referencias actuales de código/configuración | Backend [9a410af](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/9a410af4342696441f076d20a72a706663f3a18d) y Frontend [d73b576](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/d73b5760d359dfe17bbdac423db968d74d282d84) |

Las revisiones identifican las ramas con las que se preparó el entorno; las imágenes no incluyen un identificador de compilación. La [evidencia Docker](H3-DOCKER-2026-10-16.md) registra la construcción, arranque, configuración privada y comprobaciones técnicas.

### Recorridos y capturas

| Caso | Acción / ruta | Resultado visible | Captura |
|---|---|---|---|
| F-006 · Inicio en escritorio | Abrir `/` | Cabecera, buscador, hero, acceso al catálogo, categorías Running/Entrenamiento/Aire libre y aviso de demostración | [inicio.png](capturas/inicio.png) |
| F-006 · Inicio en móvil | Abrir `/` con emulación móvil | Cabecera y buscador adaptados; hero, texto, botón e imagen apilados en el área capturada | [inicio-mobile.png](capturas/inicio-mobile.png) |
| F-007 · Búsqueda en escritorio | Buscar `zapatillas`, `/catalogo?q=zapatillas` | Consulta en campo, título, chip y URL; contador de **8 productos**, tarjetas y aviso MOCK | [busqueda-resultados.png](capturas/busqueda-resultados.png) |
| F-007 · Búsqueda en móvil | Buscar `zapatillas` con emulación móvil | Misma consulta y contador de **8 productos**; composición en una columna y primera tarjeta visible | [busqueda-resultados-mobile.png](capturas/busqueda-resultados-mobile.png) |
| F-007 · Vacío en escritorio | Buscar un texto sin coincidencias | **0 productos**, mensaje «No encontramos productos con estos criterios», acciones «Limpiar búsqueda» y «Ver catálogo completo» | [busqueda-sin-resultados.png](capturas/busqueda-sin-resultados.png) |
| F-007 · Vacío en móvil | Buscar `asdasda` con emulación móvil | Consulta conservada, **0 productos**, aviso MOCK e inicio del mensaje de vacío; su parte inferior queda fuera de la captura | [busqueda-sin-resultados-mobile.png](capturas/busqueda-sin-resultados-mobile.png) |

Giuliano reportó que, durante su recorrido manual, no encontró errores de navegación en el alcance de H3. Las seis imágenes respaldan los estados visibles de la tabla; no constituyen seis pruebas automatizadas nuevas. No se adjuntan consola ni trazas de red de ese recorrido.

### Observaciones para etapas posteriores

Durante la revisión se reportaron estos comportamientos y se mantuvieron sin cambios por indicación de Giuliano de limitar el trabajo a semana 8:

| Observación | Requisito y etapa |
|---|---|
| Cambiar categoría elimina la búsqueda actual | [F-008](../../../SPECS/funcional/F-008-filtrar-catalogo.md) exige conservar búsqueda/orden al aplicar filtros; H4/S2, semanas 9–11 |
| Cambiar cantidades o eliminar líneas del carrito sólo modifica la pantalla; al volver se recuperan los datos guardados anteriores | [F-017](../../../SPECS/funcional/F-017-cambiar-cantidad-item-carrito.md) y [F-018](../../../SPECS/funcional/F-018-quitar-item-carrito.md), bloque de Andrés; S3, semanas 12–13 |
| Checkout completo no operativo | F-022–F-027, bloque de Leonidas; S3, semanas 12–13. Su incremento individual de H3 es un resumen MOCK sin pago |

Alcance y asignaciones: [plan de implementación](../../PLAN-IMPLEMENTACION.md) y [responsabilidades punta a punta](../../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estos pendientes no amplían F-006/F-007 ni se declaran resueltos en este registro.

### Pendientes del cierre

La evidencia corresponde al entorno local con datos MOCK. Quedan la prueba autorizada web → BFF → G6 con datos reales, revisión independiente y aceptación. El responsable del hito debe registrar la modalidad Docker acordada frente al requisito original de nube/URL pública. Las capturas no cambian el estado de las tareas ni acreditan por sí solas el cierre de H3.

## Documentos para consultar

| Documento | Uso |
|---|---|
| [Entrega y trazabilidad H3](../../entrega/H3-GIULIANO.md) | Guion, responsabilidades, implementación y pendientes |
| [Entorno Docker](H3-DOCKER-2026-10-16.md) | Arranque local, servicios, configuración y validaciones actuales |
| [Imagen opcional](H3-IMAGEN-OPCIONAL-2026-10-16.md) | Contrato nullable, placeholder y pruebas del adaptador |
| [Preparación G6, 17/10](H3-PREPARACION-G6-2026-10-17.md) | Ensayo HTTP de contrato, activación Docker REAL y comprobación futura del BFF; integración externa pendiente |
| [Integración develop, 17/10](H3-INTEGRACION-DEVELOP-2026-10-17.md) | Resolución de conflictos, conservación de módulos del equipo y regresión de catálogo/detalle/Docker |
| [Integración de Sebastián, 17/10](H3-INTEGRACION-SEBASTIAN-2026-10-17.md) | Problem Details, correlación compartida, proxy Docker combinado y ficha H3 sin controles comerciales simulados |

## Historial técnico conservado

Estos documentos registran cortes anteriores. Sus commits, conteos y referencias de entorno describen la fecha de cada registro; para la prueba manual actual usar la sección anterior y la evidencia Docker. Se conservan para respaldar revisiones, decisiones y enlaces desde specs/seguimiento, sin exigir releerlos todos para la presentación.

| Registro | Contenido |
|---|---|
| [Catálogo inicial, 14/10](H3-GIULIANO-CATALOGO-2026-10-14.md) | Primer corte F-006/F-007 y componentes compartidos |
| [Comparación Figma, 14/10](H3-COMPARACION-FIGMA-2026-10-14.md) | Referencias visuales y alcance de los mockups |
| [Adaptación Figma, 15/10](H3-ADAPTACION-FIGMA-2026-10-15.md) | Cambios visuales y comprobaciones |
| [Auditoría de bases, 15/10](H3-AUDITORIA-BASELINES-2026-10-15.md) | Diferencias entre ramas y bases compartidas |
| [Adaptación NestJS, 15/10](H3-ADAPTACION-BASELINE-NESTJS-2026-10-15.md) | Integración con el baseline de Backend |
| [Automatización, 16/10](H3-AUTONOMIA-2026-10-16.md) | Pruebas, CI y límites del corte documentado |
| [Reportes sanitizados](H3-AUTONOMIA-2026-10-16/README.md) | Copias de resultados e inventarios de ese corte |
| [Actualización a develop, 16/10](H3-ACTUALIZACION-DEVELOP-2026-10-16.md) | Compatibilidad con los avances compartidos |
