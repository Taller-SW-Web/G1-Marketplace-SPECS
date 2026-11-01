# S5 — Cobertura final y release (semanas 15–16)

Versión 0.7.0 · Revisión 19/10/2026 sin restricción horaria; cierre integral H6 condicionado por contratos y evidencia.

## Objetivo y alcance

Cerrar F-029/F-031 (filtro del historial y recompra) y F-040 (evaluación postentrega): tres cierres nuevos. F-004/F-005/F-015/F-020/F-021/F-039 se adelantan al objetivo H4 y mantienen regresión H6. F-028/F-030 debieron cerrarse en S3 para habilitar F-032 en H5. Mantener F-001–040 integradas; ninguna funcionalidad previa se considera cerrada si su gate real sigue abierto. Completar mobile/responsive, accesibilidad y consistencia visual según specs.

## Secuencia por semana

- **Semana 15:** cerrar funciones residuales y contratos de postventa y CSAT/ownership; repetir pruebas de recuperación integrada desde H4. Ensayar E2E compra→pedido→seguimiento→evaluación con datos autorizados. Actualizar arquitectura **as built** y ejecutar dos controles/pruebas de seguridad OWASP distintos, documentando hallazgo o resultado y retest cuando haya corrección. Montar telemetría y alertas con umbrales/owner.
- **Semana 16:** regresión final multi-módulo y smoke sobre release desplegado; disparar/probar al menos una alerta, revisar logs/métricas/trazas sin PII, accesibilidad/responsive, rollback y backup/migraciones. Congelar versión demostrable; enlazar commits, revisiones y contribuciones verificables de integrantes, diagramas finales, pruebas y URL. No incluir evidencia fabricada ni credenciales.

## Gate H6

Aplicación y funcionalidades realmente operativas con módulos dueños, arquitectura final consistente con el despliegue, al menos dos evidencias de desarrollo seguro/OWASP, UI/UX comprobable, observabilidad y alerta ensayada, repositorios actualizados y demo final reproducible. Los bloqueos se comunican; no se cierran por omisión. [Plan general](../PLAN-IMPLEMENTACION.md), [gates](../DECISIONES-Y-BLOQUEOS.md) y [seguimiento](../seguimiento/README.md) son fuentes de control.

## Responsables asignados y cierre individual

Fernando conserva F-029/F-031 y Diego F-040, con implementación/pruebas propias H4 y cierre integral S05 según contrato G5/G6/G-REORDER/G-PROMPT. Jim prueba la regresión de cuenta/recuperación F-001–F-005; Sebastian ficha/relacionados F-011–F-015; Andres carrito/fusión/movimiento F-016–F-021; Diego favoritos/movimiento F-036–F-039. Giuliano/Leonidas y todos los demás aportan regresión, arquitectura, seguridad y correcciones de sus bloques.

## Avance recibido de H4

Los 40 IDs reciben implementación/pruebas propias H4 donde sus reglas y contratos están definidos. S05 completa filtros/recompra/CSAT con fuentes autoritativas, prueba la regresión de todo lo anterior y conserva OWASP, alertas/observabilidad, accesibilidad y release H6. Una parte bloqueada externamente sigue visible por ID, sin declarar cierre a partir de diseño/fixture ni retirar requisitos de H6. El PO no limita dedicación; contratos/entornos/autorización/pruebas siguen siendo condiciones de aceptación.

La evidencia conserva diseñado, implementado con datos de prueba, integrado con otro módulo y probado en despliegue. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

Extensión H4 por contratos: F-031 puede aceptarse anticipadamente sólo con pedido autorizado, revalidación G6, dedupe y prueba desplegada. En ese caso S05 conserva dos cierres nuevos F-029/F-040 y regresión de recompra; hasta aceptación mantiene los tres objetivos base.
