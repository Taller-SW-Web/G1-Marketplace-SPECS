# Adaptación visual de Inicio y Catálogo a Figma — H3

Fecha de cierre de esta adaptación: 15/10/2026. Autoría asistida por Codex; comprobaciones automáticas y revisión de capturas por el agente. Revisión humana pendiente. Clasificación de las pruebas: **MOCK**.

Giuliano solicitó actualizar el diseño según Figma, conservando el límite previo de semana 8/H3. Se implementó la composición aplicable de V-005/V-006; no se incorporaron funciones H4 ni se modificaron Backend, DTO, tokens o contratos HTTP.

## Referencias y código publicado

- [Mockups — página Inicio, catálogo y producto](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-3).
- [V-005](../../../SPECS/ui/vistas/V-005-inicio.md): principal desktop `274:111`, mobile `274:293`; estados de carga `294:720`, vacío `294:827` y error `294:911`.
- [V-006](../../../SPECS/ui/vistas/V-006-catalogo-resultados.md): catálogo desktop `339:881`, mobile `339:1026`, resultados mobile `360:1734`; carga `351:1188`, vacío `351:1338` y error `351:1565`.
- Frontend, rama [feat/s1-f006-f007-catalogo](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/tree/feat/s1-f006-f007-catalogo): [cambio visual `9f39e0c`](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/9f39e0c58ace011a0c910c27bcc43e46a80d8108) y [conservación de exports `3a5a20b`](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/3a5a20bf776c3cf3e9be9d4dfcdfa71dfaf42b0c).
- [Guía de adaptación del Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/s1-f006-f007-catalogo/docs/FIGMA-H3.md) y [guía de elementos compartidos](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/s1-f006-f007-catalogo/docs/ELEMENTOS-COMPARTIDOS.md), versión documental 0.2.1.

Se consultó contexto detallado y capturas mediante Figma; no se escribió en el archivo de diseño. La [comparación inicial](H3-COMPARACION-FIGMA-2026-10-14.md) conserva el estado anterior del commit `241401c`.

## Cambios aplicados

| Área | Resultado |
|---|---|
| Cabecera | Logo y recorte del mockup, etiqueta de búsqueda visible, iconos exactos y navegación por categorías recibidas. Se elimina la franja promocional anterior. |
| Hero | Bloque oscuro integrado, fotografía editorial exacta, textos y CTA de Figma. Contenedor de 1320 px a viewport de 1440; fotografía en slot de 580 × 386,67 px y composición apilada en móvil. |
| Categorías | Tarjetas ilustradas, 4 posiciones por fila en escritorio y 2 en móvil, mostrando sólo categorías existentes. Ilustración semántica y exports distintos para desktop/mobile. |
| Catálogo | Encabezado, descripción, criterios, tarjetas y resumen de rango. Grilla de 3 columnas a 1440 px, 2 en tablet y 1 a 390 px; tarjeta móvil de 358 px. |
| Navegación lateral | Enlaces H3 a una categoría existente; no contiene los filtros múltiples, precio ni orden de H4. |
| Estados | Inicio cargando/vacío/error y listado con skeleton, vacío e icono de recuperación; se reutilizan las APIs de componentes compartidos. |
| Pie | Marca, distribución y copyright del mockup. Los destinos informativos pendientes permanecen deshabilitados. |

Se conservan Button, TextField, EmptyState, Skeleton y LoadingState. ErrorState añade `home?: boolean` como prop opcional; CategoryNavigation y CategoryArtwork se ubican en el módulo de catálogo. No se instalaron dependencias.

## Recursos y comprobación

Los 19 recursos de Figma están en `public/figma/`: fotografía editorial, logo, ilustraciones desktop/mobile e iconos. Se descargaron con `curl -L` desde los exports del contexto y se conservaron sin editar. El manifiesto registra archivo, nodo, dimensiones y SHA-256; se verificaron los 19 archivos locales y los bytes comprometidos en Git contra esos hashes. `.gitattributes` evita la conversión de saltos de línea de los SVG al clonar en Windows. No quedan URLs temporales de Figma en el código.

| Verificación ejecutada | Resultado |
|---|---|
| Frontend `npm run typecheck` | Pasó; el build final también completó TypeScript |
| Frontend `npm run lint` | Pasó en la versión final |
| Frontend `npm run test:components` | 10 pruebas pasaron |
| Frontend `npm run test:e2e` | Build de producción y 16 pruebas de Edge pasaron en la ejecución final |
| Geometría y recursos | Inicio a 1440/390/320 px, proporciones de ilustraciones/fotografía, recursos visibles cargados, ausencia de overflow, grilla desktop/mobile y separación entre icono y texto de búsqueda |
| Contratos y regresiones H3 | Búsqueda, límites, escape de texto, criterios en URL, cancelación, paginación básica, error/reintento y vacío conservados |
| Integridad documental | Enlaces locales y `git diff --check` comprobados antes de publicar SPECS |

Se revisaron las capturas nuevas `figma-inicio-1440.png`, `figma-inicio-390.png`, `figma-catalogo-1440.png`, `catalogo-mobile.png`, `figma-inicio-cargando-390.png`, `figma-inicio-vacio-390.png`, `figma-inicio-error-390.png`, `figma-catalogo-vacio-1280.png` y `figma-catalogo-error-1280.png`, bajo `Frontend/test-results/`. Son artefactos locales ignorados por Git. La inspección detectó y corrigió dimensiones del hero/buscador y un solapamiento del icono de búsqueda móvil; la captura final y una aserción de geometría verifican su corrección.

No se realizó una superposición de píxeles ni se revisaron todos los 34 estados enlazados como aceptación visual. Se verificó el corte implementado, no el resto de pantallas del proyecto.

## Diferencias conservadas por alcance o datos

- El BFF mock mantiene tres categorías, 32 productos sintéticos y destacados vacíos. No se cambia su contenido por los ejemplos del mockup; G-FEATURED sigue pendiente y la sección vacía se omite.
- Las imágenes de producto siguen siendo dinámicas. El DTO H3 no proporciona precios, stock ni nombres comerciales de marca; no se inventan para completar la tarjeta de Figma.
- Cuenta, favoritos y carrito se representan con controles deshabilitados y nombres accesibles, sin simular sesión, contadores ni operaciones. Ayuda y políticas también esperan destinos confirmados.
- No se añaden filtros múltiples, orden «Novedades», modal, ficha ni receptor de retorno. La ficha continúa en el bloque de Sebastian.
- La aceptación humana, G-SHELL/G-STACK, los acuerdos de datos, la integración real con G6 y el despliegue siguen pendientes según la [evidencia H3](H3-GIULIANO-CATALOGO-2026-10-14.md).

La adaptación visual H3 está implementada y publicada en su rama. No se declara identidad completa con datos/controles fuera de alcance ni cierre de H3. Main permanece sin cambios y los PR quedan a cargo de Giuliano.
