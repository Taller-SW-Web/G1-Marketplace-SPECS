# S4 — Evidencia de integración, rendimiento y asincronía (semana 14)

Versión 0.3.0 · Corte del Hito 5. Semana de cierre/medición, no de diseño inicial.

## Objetivo y alcance

Cerrar F-032 (seguimiento) y F-035 (actualización de despacho) si I-05/I-06 publicaron contrato de evento y consulta. Ejecutar y conservar evidencia de CI/CD con revisión de seguridad, pruebas de integración y performance, API Management y mecanismo asíncrono **entre dos módulos reales**.

## Evidencia mínima H5

| Requisito | Prueba exigida |
|---|---|
| CI/CD + revisión de seguridad | Run identificable de build/test/deploy, SAST/SCA/secret scan o controles acordados, hallazgos/correcciones/retest y decisión de release. |
| Integración | E2E o contrato consumidor-productor en entorno autorizado; caso exitoso, error/timeout y versión de ambas APIs. |
| Performance | Carga reproducible, versión/herramienta, concurrencia/dataset/entorno, latencia p50/p95, tasa de errores, umbral acordado y conclusión/corrección. No saturar servicios ajenos sin permiso. |
| API Management | Ruta externa publicada/configurada, autenticación/limitación/traza y prueba de tráfico por gateway; no confundir un proxy local con una política aplicada. |
| Asincronía | Evento/mensaje versionado, productor y consumidor de **módulos distintos**, correlación en logs, reintento/dedupe y prueba de fallo/recuperación. Una llamada REST o correo síncrono no bastan. |

Si Despacho/Ventas no ofrece evento apto para F-035, acordar otro intercambio intermodular real **antes** de esta semana, actualizar specs/contratos y registrar cuál funcionalidad queda bloqueada. No inventar un mensaje ni marcar H5 cumplido con un mock. La asignación humana propuesta requiere aceptación y estimación; [plan general](../PLAN-IMPLEMENTACION.md) gobierna capacidad y escalamiento.

## Responsable de F-032/F-035

Fernando es dueño de FE+BE Marketplace de seguimiento y notificación; Jim revisa aceptación y Leonidas el contrato/evento. Andres apoya gateway y despliegue; Diego lidera verificación cruzada. Mantener F-032/F-035 `Bloqueado` donde falten I-05/I-06 o prueba de dos módulos reales. La [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) no cambia el gate H5 ni la necesidad de medición, API Management y asincronía efectiva.
