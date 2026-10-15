# Comparación visual H3 con Figma — Inicio y Catálogo

Fecha: 14/10/2026. Revisión automatizada por Codex; aceptación humana pendiente.

**Resultado: la web actual no es igual a los mockups.** Se verificaron las referencias de Inicio y Catálogo y se identificaron diferencias de composición, navegación y tarjetas. Esta nota documenta la comparación; no implementa la adaptación visual ni cierra H3.

## Referencias verificadas

Fuente facilitada por Giuliano: [Mockups — Inicio, catálogo y producto](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-3). Se consultaron metadatos, contexto y capturas mediante la conexión Figma, con acceso de lectura a Escuela. No se modificó el archivo de diseño.

| Vista | Sección | Frames principales inspeccionados visualmente |
|---|---|---|
| V-005 Inicio | [V-005](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=265-8) | [Desktop público](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-111), [Mobile público](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-293) |
| V-006 Catálogo y resultados | [V-006](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=339-870) | [Desktop catálogo](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=339-881), [Mobile catálogo](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=339-1026), [Mobile resultados](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=360-1734) |

Los metadatos identifican 14 frames de V-005 y 20 de V-006. Sus enlaces individuales están registrados en [V-005](../../SPECS/ui/vistas/V-005-inicio.md) y [V-006](../../SPECS/ui/vistas/V-006-catalogo-resultados.md). Verificar que existen los 34 nodos no equivale a revisar visualmente todos sus estados. Los frames adicionales son referencias existentes, sin ampliar el alcance de implementación hasta semana 8.

## Implementación contrastada

Frontend: rama `feat/s1-f006-f007-catalogo`, commit `241401c`; el incremento de componentes compartidos está en `119b117`. Se inspeccionaron la cabecera, el pie, las vistas de inicio y catálogo y sus estilos.

Se reutilizaron estas capturas locales de la verificación H3, bajo `G1-Marketplace-Frontend/test-results/`:

- `inicio-desktop.png`: inicio a 1280 px de ancho; modificación local 14/10/2026, 23:08:35.
- `catalogo-mobile.png`: resultados para `q=running` a 390 px de ancho; modificación local 14/10/2026, 23:08:40.

Son artefactos ignorados por Git de una ejecución anterior. No se ejecutó una nueva sesión de navegador para esta revisión documental. La comparación directa corresponde a inicio desktop y resultados mobile; los otros tres frames se inspeccionaron como referencia. La evaluación es cualitativa: no se realizó superposición de píxeles y el inicio desktop no usa el mismo ancho que el frame de Figma.

## Diferencias observadas

| Elemento | Mockup | Web H3 actual | Tratamiento pendiente |
|---|---|---|---|
| Hero de inicio | Un bloque oscuro con texto y fotografía de calzado integrados. | Texto sobre fondo claro y un panel gráfico abstracto separado. | Alinear composición, dimensiones, tipografía y recursos visuales de H3. |
| Categorías | Cuatro tarjetas ilustradas con ejemplos de categorías. | Tres tarjetas de texto con datos mock. | Alinear el componente visual; nombres, cantidad y contenido deben proceder de la fuente autorizada. |
| Cabecera y pie | Cabecera con dos filas, navegación e iconos; pie con enlaces de ayuda y políticas. | Cabecera, navegación y pie simplificados. | Alinear la estructura compartida y coordinar destinos y controles con sus responsables. |
| Grilla móvil | Una tarjeta por fila en los frames de 390 px. | Dos tarjetas por fila a 390 px. | Corregir la distribución responsive dentro de H3. |
| Tarjetas de producto | Fotografía, marca, precio, disponibilidad y favorito. | SVG de demostración, nombre, texto neutro y enlace al producto. | Alinear la anatomía visual y obtener los datos y capacidades autorizados para cada campo. |
| Destacados | Sección poblada con productos. | Sección omitida cuando el proveedor devuelve una lista vacía. | Resolver G-FEATURED y la fuente de datos; conservar la regla de omisión mientras corresponda. |
| Filtros, orden y controles de cuenta | El diseño presenta filtros, chips, orden, favoritos, cuenta y carrito. | El corte implementa inicio y búsqueda con sus fundamentos H3. | Respetar responsables, contratos y alcance temporal; su presencia en Figma no autoriza implementarlos en este corte. |

Además de la estructura, quedan por ajustar tamaños, espaciados y presentación de los componentes. No se atribuye conformidad visual por compartir colores o fuentes con DS-001.

El orden «Novedades» mostrado en el mockup necesita reconciliarse con el contrato vigente antes de habilitarlo. Tampoco se deben inventar precios, stock, marcas, categorías o resultados destacados para reproducir una captura. La ficha de producto sigue siendo responsabilidad de su bloque; esta comparación no añade esa implementación.

## Documentación actualizada y siguiente trabajo

Se registraron enlaces de sección, página y frame en V-005/V-006 y en el paquete visual existente. [DS-001](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md) distingue ahora la carpeta organizativa del archivo Mockups; DS-OPEN-07 sigue pendiente para las demás vistas, prototipo y aprobación humana. F-006/F-007 enlazan sus frames principales y corrigen su referencia de iteración a S1/H3, semanas 7–8.

Para la adaptación visual de H3 quedan la cabecera y pie aplicables, el hero, las categorías, la grilla responsive y los estados de componentes. Deben verificarse después con capturas nuevas en los tamaños de los frames. La integración real de Productos, los acuerdos de datos y la aceptación humana siguen pendientes según la [evidencia H3](H3-GIULIANO-CATALOGO-2026-10-14.md).

Esta actualización es documental: no cambia código ni tokens y no vuelve a ejecutar las pruebas de aplicación. La validación comprobó 81 enlaces locales y 72 referencias a nodos Figma, incluyendo los 34 identificadores de frames y sus nombres, sin errores. `git diff --check` pasó. No representa aprobación de los mockups ni revisión humana del código.
