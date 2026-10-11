# Sebastian Matias Malca Agüero — frontend y documentación — H3

**Repo de trabajo:** G1-Marketplace-Frontend; documentación S1 en SPECS mediante PR aparte si hay decisiones aprobadas. **Rama sugerida:** `feat/s1-f007-resultados` desde `develop`. **Revisor:** Giuliano (Diego revisa tests). **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Liderar `TASK-F007-FE-001`: implementar el corte H3 de `V-006` con heading de resultados, grilla de tarjetas comerciales, estados carga/vacío/error/timeout y recuperación. Leer `q` de URL y evitar que respuesta antigua reemplace consulta nueva. Responsive y foco conforme a UI; no implementar filtros, orden ni paginación completos de S2 como si fueran requisito H3.
- Crear cliente tipado del **BFF Marketplace**, nunca invocar G6 desde el navegador. Pactar DTO con Leonidas; dejar adaptador de fixture sólo para desarrollo/test y configurar cambio a entorno real sin bifurcar la UI. No crear precios, stock ni promociones falsos en pantalla publicada.
- Compartir componente de tarjeta con Fernando sin hacer que dependa de login/favoritos/carrito de S2; controles aún no operativos no deben parecer funcionales. Añadir pruebas de query 1/121 caracteres, vacío, error, request anterior y navegación desde Home.
- Como documentador, coordinar `TASK-F006-DOC-001`, `TASK-F007-DOC-001`: actualizar trazabilidad specs→código→tests, decisiones de desviación aprobadas y enlaces a PR/URL/capturas. No marcar integración terminada hasta evidencia real revisada por Jim/Diego.

**Entradas:** [funcional F-007](../../SPECS/funcional/F-007-buscar-productos-texto.md), [UI F-007](../../SPECS/ui/F-007-buscar-productos-texto.md), [API F-007](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [React F-007](../../SPECS/componentes-react/F-007-buscar-productos-texto.md), [V-006](../../SPECS/ui/vistas/V-006-catalogo-resultados.md), [Figma Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups).

**Entregar a Diego/Jim:** pruebas y tabla de trazabilidad por estado. **PR:** al `develop` de frontend; docs en PR separado a la rama acordada de SPECS. **Evidencia IA:** nota propia según [guía](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante), además de recopilar los enlaces de los demás, sin escribir sus declaraciones por ellos.
