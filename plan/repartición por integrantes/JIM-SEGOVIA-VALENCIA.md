# Jim Bryan Segovia Valencia — product owner — H3

**Repos de trabajo:** G1-Marketplace-Backend para test consumidor/fixtures; SPECS para decisión de I-01 y evidencia. **Rama sugerida:** `test/s1-contrato-productos` desde `develop`; docs en PR aparte. **Revisor:** Leonidas; Diego revisa aceptación. **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Coordinar con Gabriel/G6 la URL de desarrollo, SHA OpenAPI, respuesta ejemplo, `q`, canal MARKETPLACE, datos de prueba visibles y autorización `catalogo:leer` con Seguridad. Publicar lo confirmado en I-01 sin credenciales. Si todavía lo desarrollan esta semana, acordar fecha de disponibilidad y escalar riesgo antes del corte.
- Aportar **código verificable**, no sólo coordinación: test de contrato consumidor/fixtures versionados del adaptador de Productos con Leonidas, que compruebe campos usados por F-006/F-007, listas vacías, error público y diferencia `product_id`/SKU. No modificar los archivos del adaptador de Leonidas ni asumir respuesta que OpenAPI no define; el test sigue MOCK hasta correr contra API real.
- Cerrar decisión de alcance editorial para Home: hero/destacados aprobados o sección omitida sin promociones falsas; validar que `V-006` de H3 sólo presenta acciones implementadas. Registrar diferencias mock/spec como decisión, no corregirlas a escondidas.
- Liderar `TASK-TRANS-S01-DOC-001/002` con Sebastian/Diego: diagrama de contexto/arquitectura as-built, enlace a código/commit/URL, evidencia de llamada intermodular real y resumen honesto de uso de IA del equipo. Preparar aceptación del demo H3 con Diego.

**Entradas:** [plan H3](../PLAN-IMPLEMENTACION.md), [I-01 y bloqueos](../DECISIONES-Y-BLOQUEOS.md), [API F-006](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [API F-007](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [OpenAPI G6](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/contratos/http/openapi.yaml), [Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups).

**Entregar a Leo/Andres:** datos/URL/grant confirmados o bloqueo explícito; a Diego, criterios de aceptación. **PR:** test al `develop` de backend; documentación en PR propio. **Evidencia IA:** nota propia según [guía](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante).
