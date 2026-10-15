# Changelog — documentación de elementos compartidos

Este registro describe documentación y contratos de consumo. No acredita publicación de una biblioteca, revisión humana ni una nueva versión de DS-001.

## 0.2.1 — 15/10/2026 — En revisión

- Inicio y Catálogo adoptan la composición de sus frames Figma dentro de H3: shell, hero, categorías, tarjetas, estados y grilla de una columna en móvil.
- Se añaden CategoryNavigation y CategoryArtwork dentro de catálogo; ErrorState incorpora `home?: boolean` sin romper consumidores existentes.
- ProductSkeletons compone seis tarjetas; SearchBox conserva etiqueta visible y botón accesible con icono.
- Se registran recursos exactos de Figma en Frontend con nodos de origen, dimensiones y SHA-256. Productos y categorías siguen sujetos al BFF; no se inventan precio/stock/destacados ni se añade funcionalidad H4.
- Se actualizan guías de consumo y la [evidencia de adaptación](../../../plan/evidencias/H3-ADAPTACION-FIGMA-2026-10-15.md). Revisión humana y gates externos pendientes.

Compatibilidad: Button, TextField, EmptyState, Skeleton, DTO y rutas HTTP mantienen sus contratos. La nueva prop de ErrorState es opcional. DS-001 conserva su versión 0.2.0.

## 0.2.0 — 14/10/2026 — En revisión

- Se implementan Button (variantes, tamaños, loading/disabled e iconos), TextField (IDs únicos y label/hint/error asociados), EmptyState y Skeleton/LoadingState.
- Se integran en SearchBox, reintento, vacíos y carga de categorías/productos, conservando los exports de feedback existentes.
- El buscador deja de utilizar IDs fijos y bloquea envíos mientras la navegación está pendiente.
- Se añaden action-soft y cinco tokens de espaciado de DS-001: la traducción local pasa de 18 a 24 variables CSS.
- Se añaden 10 pruebas de componentes con Vitest/Happy DOM; pasan las 13 pruebas de navegador existentes, lint, TypeScript y build. Dependencias de prueba compatibles con Node 22.18; auditoría de instalación sin vulnerabilidades reportadas.
- Se actualizan contratos, ejemplos y pendientes de la guía del frontend y este inventario. Modal, campos especializados y feedback O-010 completo permanecen pendientes.

Compatibilidad: los componentes anteriores mantienen sus contratos. Los IDs del campo son un detalle interno generado; los consumidores y pruebas deben usar label/rol en lugar de depender de buscar-productos/search-error. DS-001 conserva su versión 0.2.0 y revisión pendiente.

## 0.1.0 — 14/10/2026 — En revisión

- Se crea [el catálogo de elementos compartidos](ELEMENTOS-COMPARTIDOS.md) con ubicación, responsabilidades, foundations, DTO y límites de uso.
- Se registran los elementos presentes en el corte local: Header/Footer, SearchBox, ProductCard, feedback de catálogo, skeletons, CategoryChip y hook/validadores.
- Se distinguen los estilos CSS de los componentes React todavía pendientes; ErrorState no se declara O-010 completo.
- Se documenta el subconjunto de 18 variables CSS, tipografías instaladas y diferencias responsive pendientes de aceptación.
- Se añaden guías de consumo en los repositorios Frontend y Backend, con ejemplos y handoff.
- Se registra la política actualizada de la sesión: commits y publicación de las ramas de trabajo por repositorio, sin cambios publicados a main ni apertura automática de PR; Giuliano los preparará manualmente al terminar.
- Se enlazan las guías compartidas desde las ramas de código y se registran los commits publicados de Frontend/Backend en la evidencia del corte.

Compatibilidad: este cambio es documental; no modifica exports, props, comportamiento ni contratos HTTP. Conserva como pendientes las revisiones y los gates externos.
