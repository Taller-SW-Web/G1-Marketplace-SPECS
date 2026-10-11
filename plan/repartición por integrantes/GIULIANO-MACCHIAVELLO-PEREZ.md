# Giuliano Macchiavello Perez — UX/UI y frontend — H3

**Repo de trabajo:** G1-Marketplace-Frontend. **Rama sugerida:** `feat/s1-shell-buscador` desde `develop`. **Revisor:** Fernando; Jim acepta composición funcional. **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Acordar con Andres el stack frontend ejecutable y lockfile (G-STACK). Implementar base visual compartida de `V-005/V-006`: tema DS-001, logo aprobado, cabecera comercial, buscador accesible, layout/footer **sólo con enlaces existentes**, regiones de carga/error y responsive. No introducir dos UI kits.
- Implementar `SearchBox` tipado de F-007: entrada, validación de 2–120, envío por Enter/botón, manejo de vacío y navegación interna a `/catalogo?q=...`; mostrar query aplicada desde URL sin almacenar tokens. Compartir props/eventos con Sebastian y Fernando antes de fusionar.
- Traducir mockups aprobados al código respetando jerarquía y estados de [V-005](../../SPECS/ui/vistas/V-005-inicio.md), [V-006](../../SPECS/ui/vistas/V-006-catalogo-resultados.md) y [DS-001](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md). Si el mockup exhibe acciones de S2 aún no implementadas, no crear interacciones ficticias: anotar desviación para Jim.
- Añadir prueba de componente de validación/foco/navegación del buscador y revisar accesibilidad de las dos vistas. No asumir que diseñar el mockup equivale a implementar toda la vista.

**Tareas relacionadas:** porción compartida de `TASK-F006-FE-001`, `TASK-F007-FE-001` y base FE de `TASK-TRANS-S01-OPS-001`; Fernando/Sebastian conservan titularidad de las pantallas. **Entradas:** [React F-006](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md), [React F-007](../../SPECS/componentes-react/F-007-buscar-productos-texto.md), [arquitectura React](../../SPECS/componentes-react/ARQUITECTURA-REACT.md), [Figma Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups).

**Entregar a Fernando/Sebastian:** API de componentes compartidos y capturas desktop/mobile. **PR:** al `develop` de frontend. **Evidencia IA:** nota propia según [guía](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante).
