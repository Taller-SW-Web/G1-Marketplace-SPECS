# Plan de implementación — hitos de semanas 8 a 16

Versión 0.5.0 · Revisión del corte: 2026-10-18. Reparto y estimación base decididos por el PO el 2026-10-13; validación académica pendiente. Este documento planifica **software y evidencia técnica**, no la PPT ni el guion de exposición.

## 1. Punto de partida y regla de verdad

Los mockups están elaborados y aprobados según el PO, pero eso no acredita código funcional. Al [corte del 18/10](CORTE-H3-Y-TRASPASO-H4.md), FE `main@ec1acfb` y BE `main@c7e8e8e` contienen código y pruebas parciales de catálogo, ficha, carrito, favoritos y checkout MOCK. La web pública permite catálogo, búsqueda, ficha y carrito de demostración; sus rutas de catálogo respondieron 200 con `X-Catalog-Source: MOCK` al repetir la consulta. Hay una prueba local documentada de categorías G6 REAL, pero no una búsqueda positiva ni la ruta completa desplegada en modo REAL. Las tareas de H3 que carecen de esa evidencia pasan explícitamente a S2/H4; no se consideran ejecutadas por figurar en el plan.

Meta: llegar a semana 16 con F-001–F-040 implementadas, integradas y probadas donde corresponda. Las 17 vistas, 10 overlays y 2 correos siguen sujetos a sus specs; no se reduce el alcance silenciosamente. La viabilidad depende de capacidad real, contratos ajenos y disponibilidad de entornos. La estimación base ya está fijada; si la capacidad observada no alcanza, Jim/Diego documentan la resecuenciación y consultan al profesor cuando afecte la entrega; este calendario no es una garantía ficticia.

## 2. Hitos obligatorios y evidencia de software

| Hito | Semana | Salida que debe poder comprobarse |
|---|---:|---|
| H3, primer avance | **8** | Primer flujo funcional de Marketplace en la nube: página pública de catálogo/búsqueda, BFF y **una llamada real** a la API de Productos (F-006/F-007). Mostrar URL de frontend, petición/respuesta entre módulos, logs sanitizados y URL de salud del backend. Figma o fixture aislado no sustituyen esta prueba. Adjuntar diagramas de contexto/arquitectura vigentes y enlaces al código. |
| H4, segundo demo | **11** | Nuevas funciones operativas (ficha/SKU y carrito/favoritos básicos); CI/CD que ejecuta build, test y deploy; diseño de APIs versionado y verificable; autenticación en pantallas y APIs con Seguridad. Evidencia del segundo flujo y de autorización/errores, no sólo botón de login. |
| H5, ingeniería e integración | **14** | Pipeline con revisión de seguridad; pruebas de integración y performance con resultados; API Management configurado para al menos el flujo intermodular demostrado; **mecanismo asíncrono real entre microservicios** con contrato, productor/consumidor, reintento/deduplicación y traza. F-032/F-035 son el objetivo si Despacho/Ventas publican evento; alternativa requiere nuevo acuerdo/versionado, no inventar proveedor. |
| H6, final | **16** | Aplicación completa y operativa con otros módulos, arquitectura final actualizada, demo extremo a extremo, al menos dos evidencias distintas de seguridad/OWASP y desarrollo seguro, observabilidad/alertas probadas, UI/UX mejorada, repositorios actualizados con contribuciones verificables. |

**Tensión documental:** la ficha específica de H3 exige integración vía API ya en semana 8, mientras el cronograma general destaca integración en H4. Se planifica cumplir el requisito **más temprano**. Si el profesor aclara otra interpretación, registrar la decisión sin retirar la integración del plan por defecto.

## 3. Iteraciones orientadas a hitos

| Iteración                              | Semanas   | Funcionalidades de cierre                            | Trabajo transversal y corte demostrable                                                                                                                                                                                                                              |
| -------------------------------------- | --------- | ---------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| [S1](iteraciones/S01-semanas-07-08.md) | **7–8**   | F-006, F-007 **sin cierre integral en H3**             | Hay código y conexión local parcial a G6; falta acreditar búsqueda y ruta completa en nube. Ver [corte y traspaso](CORTE-H3-Y-TRASPASO-H4.md). |
| [S2](iteraciones/S02-semanas-09-11.md) | **9–11**  | F-006/F-007 pendientes + F-001–003, F-008–014, F-016, F-019, F-036–038 | H4 recibe el gate de H3 y mantiene auth, catálogo detallado, carrito/favoritos, CI/CD y OpenAPI. La carga supera el objetivo original de 15 funciones: **revisar capacidad y resecuenciar antes de comprometer cierre**. |
| [S3](iteraciones/S03-semanas-12-13.md) | **12–13** | F-017–018, F-022–028, F-030, F-033–034               | Checkout y confirmación honesta, primer historial/detalle para habilitar seguimiento, y notificación asíncrona. Preparar proveedor/evento de F-032/F-035 y ensayos de performance antes de H5. 12 funciones, integración de Ventas/Despacho sujeta a gates.          |
| [S4](iteraciones/S04-semana-14.md)     | **14**    | F-032, F-035                                         | Corte H5: seguimiento y evento/notificación de despacho, API Management, pruebas de integración/performance y revisión de seguridad CI/CD. No es una semana libre para empezar infraestructura desde cero.                                                           |
| [S5](iteraciones/S05-semanas-15-16.md) | **15–16** | F-004–005, F-015, F-020–021, F-029, F-031, F-039–040 | Completar recuperación, relacionados, fusión/movimientos, filtros/recompra y evaluación; regresión E2E, accesibilidad, OWASP, observabilidad, alertas, arquitectura y release final. 9 funciones más estabilización: **carga alta** y margen de corrección reducido. |

Los números de funciones son **objetivos de cierre**, no permiso para investigar sus contratos sólo en ese sprint. Contratos de Productos para S1, Seguridad para S2, Ventas/Despacho para S3–S4 y evento asíncrono de H5 se gestionan desde la primera semana. La UI puede avanzar con fixtures, pero ninguna integración se marca terminada sin prueba intermodular autorizada. Ninguna función se da por terminada sólo por tener mockup desktop; responsive, estados y a11y siguen su spec.

## 4. Ruta crítica planificada para semanas 7–8

Los pasos siguientes conservan el objetivo original. El código FE/BE se creó después, pero el [corte H3](CORTE-H3-Y-TRASPASO-H4.md) muestra que la ruta pública completa y su evidencia siguen pendientes para H4.

1. **Entrada inmediata de S2/H4:** confirmar URL/base, versión, ruta pública, payload y datos de prueba de Productos; cerrar el mínimo de I-01 para F-007. Frontend decidido e integrado: React + TypeScript + Next.js App Router con lockfile observado en FE `main@ec1acfb`; cerrar la decisión global de UI kit (`DS-OPEN-03`), verificar esas versiones en el pipeline desplegado y actualizar el diagrama/deploy objetivo. Si el proveedor no tiene entorno alcanzable, escalar el gate: un mock no acredita integración REAL.
2. **Base ejecutable:** inicializar frontend; usar el backend/Prisma remoto como antecedente auditado, sin suponer que `/health` representa el BFF especificado. Configurar BFF público de catálogo con timeout, validación, error y secreto de entorno; CI mínimo build/test. No almacenar catálogo ajeno.
3. **Corte vertical:** F-006 puede mostrar categorías/enlace de búsqueda sin prometer destacados sin curaduría; F-007 ejecuta búsqueda real desde la web → BFF → Productos, con vacío/error. Probar solicitud real y ruta visible. Si el contrato no permite búsqueda, acordar **antes de implementar** otra lectura pública de Productos y actualizar F-006/F-007/specs/plan.
4. **Nube y evidencia:** desplegar frontend y backend en entornos propios, configurar CORS/orígenes, URL y secretos, revisar logs sin PII, capturar build, test, deploy y una respuesta intermodular. Diagramas/versiones/enlaces deben corresponder al sistema efectivamente desplegado. Ensayar recuperación si uno de los servicios falla.
5. **Gate H3:** URL pública operativa, acción del usuario con dato remoto observable, backend saludable, evidencia de petición/respuesta, diagramas y commits. Sin alguno de esos elementos, informar la brecha; no sustituirla por Figma ni declarar hito completo.

## 5. Preparación temprana de H4–H6

- **Hasta semana 9:** definir política real de login/MFA con Seguridad (G-AUTH), ownership de APIs y endpoints; entregar OpenAPI del BFF y pruebas de contrato. Definir `build → test → deploy` por entorno, secretos fuera de Git, rollback y reglas de rama. H4 exige autenticación de pantallas **y** APIs.
- **Hasta semana 11:** cerrar I-02 (orden idempotente, aptitud para pagar y confirmación simulada) e I-06 (Despacho), más el evento I-05 para H5. Acordar API Management (producto, rutas, auth, rate limit, logs) y mecanismo asíncrono concreto (broker/cola/evento, esquema, owner, consumidor, retry, DLQ o política equivalente). Un outbox interno sin intercambio entre módulos **no** satisface H5.
- **Semanas 12–13:** implementar flujo de checkout sin presentar `PREPARED`/`CREADO` como pagado; F-027 requiere `PAGADO` confirmado por Ventas. Preparar tráfico/fixtures/umbrales de performance, prueba de integración y revisión de seguridad; no esperar a semana 14 para empezar.
- **Semana 14:** ejecutar prueba de integración positiva/negativa, prueba de carga en entorno autorizado con métricas y umbral, evidencia del gateway y mensaje asíncrono real con traza/deduplicación/reintento, y revisión CI/CD de seguridad. Registrar limitaciones y correcciones.
- **Semanas 15–16:** cerrar F-001–040, E2E y regresión con servicios reales; documentar arquitectura **as built**, al menos dos prácticas/pruebas OWASP distintas con corrección/retest, telemetría y una alerta disparada/verificada. UI/UX final y contribuciones Git verificables. Congelar cambios de alto riesgo antes de demo final salvo correcciones necesarias.

## 6. Bloqueos, decisiones y gestión de capacidad

[DECISIONES-Y-BLOQUEOS](DECISIONES-Y-BLOQUEOS.md) conserva los gates I-01–I-06 y G-*. Agregar allí evidencia de cierre antes de usar un contrato real. El checkout simulado no puede inventar webhook/pago. Datos personales, direcciones y pedidos siguen en los servicios dueños; Marketplace sólo conserva lo definido en su modelo lógico. No mezclar bases de datos de otros módulos.

La [matriz punta a punta](../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) y los [paquetes personales](repartición%20por%20integrantes/README.md) fijan responsables/revisores de F-001–F-040 y una estimación base de 104 días persona más 20 % de reserva, por decisión del PO. No se exige aceptación ni estimación individual para iniciar; pasar una tarea a En progreso requiere que el responsable efectivamente la inicie y registre avance. Los nombres en tableros son **asignaciones, no ejecución**. El owner del bloque implementa UI y backend propio; colaboradores transversales apoyan sin duplicar ownership. Si S2/S5 o los gates no caben, PO/JP registran desvío y acuerdan resecuenciación explícita; no declarar cumplido lo que sólo funciona con mock. Mantener pequeño margen de correcciones, especialmente antes de H3 y H6.

## 7. Definition of Ready, Done y evidencia

**Ready:** specs vigentes, contrato/versiones y entorno disponibles o fixture rotulado, dependencias/gates conocidos, casos positivos y negativos, estimación base y responsable/revisor asignados por el PO. En integración real, una homologación verbal o TXT no sustituye contrato publicado y prueba.

**Done:** FE/BE con tipos/build y pruebas pertinentes, seguridad y accesibilidad/responsive según spec, API real y autorización cuando aplique, negativos/timeout, observabilidad sin PII, evidencia de deploy/integración, revisión independiente y trazabilidad specs↔código↔tests. Una tarea bloqueada externamente no pasa a Terminado por pruebas con mock.

La evidencia técnica mínima por hito se registra con URL, commit, contrato/versiones, entorno, fecha, comando/caso/resultado y captura o log saneado. Las diapositivas y el relato del uso de IA se preparan para la exposición fuera de este cronograma de desarrollo.
