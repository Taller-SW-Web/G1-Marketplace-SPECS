# Diego Steven Martin Espinoza Picon — jefe de proyecto y QA — H3

**Repos de trabajo:** FE y BE para pruebas/CI; SPECS para registro de gate. **Rama sugerida:** `test/s1-catalogo-e2e` desde `develop` en el repo pertinente. **Revisor:** Jim; Leonidas revisa pruebas de backend. **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Liderar `TASK-F006-QA-001/002`, `TASK-F007-QA-001/002` y `TASK-TRANS-S01-QA-001`: crear suite automatizada con fixtures para FE→BFF y BE→Productos, después ejecutar casos equivalentes contra entorno real autorizado. Cubrir home, búsqueda válida/inválida, vacío, error, timeout, respuesta tardía, producto no elegible, XSS/longitud, foco y viewport responsive.
- Configurar runners de tests mínimos en CI con Andres; fallos reales deben bloquear merge, no saltarse. La prueba de contrato consumidor de Jim entra al mismo pipeline. Distinguir en nombres/reporte tests MOCK de tests REAL.
- Como JP, confirmar capacidad/estimaciones y revisar que PR tengan autor distinto del aprobador, ID de tarea, evidencia IA, specs/mockups citados y prueba reproducible. Coordinar secuencia de PR a `develop` y release PR `develop`→`main` sin force-push.
- Preparar gate H3 con Jim: código/commits, URL pública FE/BE, respuesta real intermodular, seguridad básica, diagramas as-built y lista honesta de brechas. Si G6 no entrega API/grant, registrar bloqueo y avisar al profesor; no declarar integrado por pasar tests con mock.

**Entradas:** [S1](../iteraciones/S01-semanas-07-08.md), [seguimiento F-006](../seguimiento/F-006-inicio-categorias-destacados.md), [seguimiento F-007](../seguimiento/F-007-buscar-productos-texto.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [V-005](../../SPECS/ui/vistas/V-005-inicio.md), [V-006](../../SPECS/ui/vistas/V-006-catalogo-resultados.md).

**Entregar a equipo:** tablero de PR/revisiones, reporte automático de pruebas y checklist de gate. **Evidencia IA:** nota propia según [guía](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante).
