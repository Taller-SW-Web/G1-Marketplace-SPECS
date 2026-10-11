# Leonidas Garcia Lescano — arquitectura y backend — H3

**Repos de trabajo:** G1-Marketplace-Backend; SPECS sólo para decisiones contractuales aprobadas. **Rama sugerida:** `feat/s1-f007-bff-catalogo` desde `develop`. **Revisor:** Diego (Andres revisa configuración de seguridad). **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Liderar `TASK-F006-BE-001` y `TASK-F007-BE-001`: rutas BFF de home/catálogo y búsqueda pública; validar `q` (vacía o 2–120 según spec), página, errores y DTOs; probar con fixtures antes del proveedor.
- Liderar `TASK-F006-INT-001` y `TASK-F007-INT-001` junto a Jim: adaptador server-only para `GET /api/v1/productos?q=...&canal=MARKETPLACE`, bearer de servicio `catalogo:leer` cuando Seguridad otorgue grant; correlación, timeout, 401/403/429/5xx y mapeo de respuesta comercial. Separar claramente cliente externo del contrato público `/api/v1/catalog/products` del BFF. No inventar endpoint de home ni persistir catálogo ajeno.
- Revisar el backend actual (`src/server.js`, Prisma, `render.yaml`) con Andres. Reutilizar lo seguro y documentar brechas: hoy `/health` no es un BFF de catálogo y devuelve detalles internos de error; reemplazar esa exposición antes de publicar. Acordar si continuar la base JS o migrar a la arquitectura especificada; no mezclar stacks sin decisión G-STACK.
- Entregar tests de transformación, validación, vacío/error/timeout con fixtures; después repetir contra la API real y registrar SHA del contrato G6. Si no hay URL/token/datos, dejar INT bloqueadas, no maquillar con fixture.

**Entradas:** [plan S1](../iteraciones/S01-semanas-07-08.md), [F-006 API](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [F-007 API](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [modelo arquitectónico](../../SPECS/componentes-react/ARQUITECTURA-REACT.md), [OpenAPI de Productos](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/contratos/http/openapi.yaml) y [alineación intermodular](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/integraciones/ALINEACION_MARKETPLACE.md).

**Entregar a Sebastian/Fernando:** DTO de frontend y ejemplos sanitizados de éxito, vacío y error; ruta/base configurables, nunca URL de Productos ni secreto en navegador. **PR:** al `develop` del backend con pruebas y referencia a I-01. **Evidencia IA:** nota propia siguiendo la [plantilla](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante), incluso si no usa IA.
