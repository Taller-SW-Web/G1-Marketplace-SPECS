# S2 — Segundo demo, APIs y autenticación (semanas 9–11)

Versión 0.4.0 · Replanificación para Hito 4. Carga alta: usar estimación base y avance observado antes de prometer cierre completo.

## Objetivo y alcance

Cerrar F-001–003 (registro, login, logout), F-008–014 (filtro, orden, paginación, ficha, precio/oferta, variantes y stock), F-016 (agregar al carrito), F-019 (ver carrito) y F-036–038 (favoritos). F-004/005 de recuperación se programan en S5; no simular que son parte del login implementado. F-015 relacionados queda en S5. Contratos externos vigentes y propiedad de datos prevalecen sobre mockups.

## Secuencia por semana

- **Semana 9:** publicar/validar diseño OpenAPI del BFF y mapa de adaptadores; acordar G-AUTH con Seguridad (token, MFA, retorno, expiración, CORS/cookies). Activar CI con build, typecheck, tests y secretos; preparar despliegue automático por entorno. Completar filtro/orden/página y ficha con datos comerciales autorizados.
- **Semana 10:** integrar registro/login/logout con Seguridad en pantallas **y** APIs protegidas; probar usuario ajeno, token vencido y MFA. Entregar variantes/SKU/precio/stock sin inferir cantidades desde estado comercial. Agregar/ver carrito con persistencia propia y errores controlados; favoritos básicos si la capacidad lo permite.
- **Semana 11:** ejecutar pipeline build→test→deploy, revisión de seguridad, prueba de contrato/e2e y segundo demo en nube. Evidenciar funciones nuevas, autenticación, diseño de APIs y CI/CD. Cerrar I-02/I-06 y escoger contrato/evento real para H5; no postergar esa coordinación a semana 14.

## Gates y evidencia H4

- OpenAPI versionado, ejemplos de request/response/error y prueba de contrato; no basta un diagrama de endpoints.
- CI/CD con ejecución y despliegue observables, configuración sin secretos en Git, rollback definido y al menos un cambio que recorra el pipeline.
- Login real en UI y autorización real en BFF; API pública separada de protegida. Si Seguridad no publica contrato/entorno, reportar bloqueo, no declarar autenticación terminada.
- Segundo demo que amplíe H3 y no dependa exclusivamente de fixtures. Evidencias sanitizadas de Git, pipeline, despliegue y casos negativos.

Consultar [gates](../DECISIONES-Y-BLOQUEOS.md), [plan general](../PLAN-IMPLEMENTACION.md) y [tablero](../seguimiento/README.md). La asignación y estimación base decididas por el PO están en la matriz; la capacidad real se vigila durante la ejecución.

## Responsables propuestos y carga

Según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), Jim lleva F-001–003 (cuenta), Giuliano F-008–010 (catálogo), Sebastian F-011–014 (detalle), Andres F-016/F-019 (carrito) y Diego F-036–038 (favoritos). Cada uno conserva FE+BE Marketplace, pruebas y documentación; Fernando y Leonidas revisan según especialidad sin sustituir ownership. Los 15 cierres de S2 requieren comparar la base de esfuerzo con el avance y tiempo disponible antes de prometer H4. Auth real depende de Seguridad y producto comercial de Productos; `MOCK` permite avance pero no cierra INT.
