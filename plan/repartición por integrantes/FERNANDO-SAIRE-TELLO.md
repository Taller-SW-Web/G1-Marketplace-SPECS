# Fernando Jose Saire Tello — QA/cloud y frontend — H3

**Repo de trabajo:** G1-Marketplace-Frontend. **Rama sugerida:** `feat/s1-f006-inicio` desde `develop`. **Revisor:** Sebastian (Giuliano revisa coherencia visual). **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Liderar `TASK-F006-FE-001`: implementar `V-005` Inicio con `HomePageContainer`, categorías reales que enlacen a `/catalogo`, sección de destacados **sólo si hay fuente/curaduría aprobada** y estados independientes de carga/vacío/error. Hero sólo con contenido y destino aprobados. Navegación y buscador común de Giuliano; tarjeta compartida con Sebastian.
- Asegurar composición desktop y responsive descrita por spec, navegación por teclado y texto alternativo; no dejar controles de favoritos/cuenta/carrito como acciones ficticias de H3. Probar que categorías vacías o fallidas no rompen el buscador ni el acceso a catálogo.
- Apoyar `TASK-TRANS-S01-QA-001` y cloud: ejecutar smoke en URL pública después del deploy de Andres desde red/navegador externo al entorno local; capturar estado home, búsqueda real, vacío y error de forma sanitizada. Las capturas de Figma no sustituyen la web desplegada.
- Revisar la implementación del shell/buscador de Giuliano y reportar diferencias entre mock aprobado y spec en issue; no alterar silenciosamente el sistema de diseño.

**Entradas:** [funcional F-006](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [UI F-006](../../SPECS/ui/F-006-inicio-categorias-destacados.md), [API F-006](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [React F-006](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md), [V-005](../../SPECS/ui/vistas/V-005-inicio.md), [Figma Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups).

**Entregar a Diego/Jim:** URL y capturas de smoke con hora/commit, diferenciando MOCK/REAL. **PR:** al `develop` de frontend. **Evidencia IA:** nota propia según [guía](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante).
