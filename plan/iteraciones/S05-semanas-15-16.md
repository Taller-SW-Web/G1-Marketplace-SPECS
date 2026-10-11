# S5 — Cobertura final y release (semanas 15–16)

Versión 0.2.0 · Replanificación para Hito 6. Carga alta; sin capacidad estimada no se garantiza cierre de nueve funciones más regresión.

## Objetivo y alcance

Cerrar F-004–005 (recuperación), F-015 (relacionados), F-020–021 (fusión/movimiento desde carrito), F-029/F-031 (filtro del historial y recompra), F-039 (favorito→carrito) y F-040 (evaluación postentrega). F-028/F-030 debieron cerrarse en S3 para habilitar F-032 en H5. Mantener F-001–040 integradas; ninguna funcionalidad previa se considera cerrada si su gate real sigue abierto. Completar mobile/responsive, accesibilidad y consistencia visual según specs.

## Secuencia por semana

- **Semana 15:** cerrar funciones residuales y contratos de postventa, CSAT/ownership y recuperación. Ensayar E2E compra→pedido→seguimiento→evaluación con datos autorizados. Actualizar arquitectura **as built** y ejecutar dos controles/pruebas de seguridad OWASP distintos, documentando hallazgo o resultado y retest cuando haya corrección. Montar telemetría y alertas con umbrales/owner.
- **Semana 16:** regresión final multi-módulo y smoke sobre release desplegado; disparar/probar al menos una alerta, revisar logs/métricas/trazas sin PII, accesibilidad/responsive, rollback y backup/migraciones. Congelar versión demostrable; enlazar commits, revisiones y contribuciones verificables de integrantes, diagramas finales, pruebas y URL. No incluir evidencia fabricada ni credenciales.

## Gate H6

Aplicación y funcionalidades realmente operativas con módulos dueños, arquitectura final consistente con el despliegue, al menos dos evidencias de desarrollo seguro/OWASP, UI/UX comprobable, observabilidad y alerta ensayada, repositorios actualizados y demo final reproducible. Los bloqueos se comunican; no se cierran por omisión. [Plan general](../PLAN-IMPLEMENTACION.md), [gates](../DECISIONES-Y-BLOQUEOS.md) y [seguimiento](../seguimiento/README.md) son fuentes de control.
