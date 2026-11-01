# Tareas y seguimiento — F-025 Simular pago y revalidar stock

Versión 0.1.0 · Planificación inicial · F-025 no está implementada por estos documentos.

## Fuente y control

- [Plan F-025](../funcionalidades/F-025-simular-pago-revalidar-stock.md); [iteración S3](../iteraciones/S03-semanas-12-13.md).
- [Funcional](../../SPECS/funcional/F-025-simular-pago-revalidar-stock.md), [UI](../../SPECS/ui/F-025-simular-pago-revalidar-stock.md), [API](../../SPECS/contrato-api/F-025-simular-pago-revalidar-stock.md), [React](../../SPECS/componentes-react/F-025-simular-pago-revalidar-stock.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Leonidas Garcia**; revisor principal: **Diego Espinoza** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. QA local puede avanzar con fixtures; QA real requiere INT. Evidencia inicial pendiente, no pruebas ejecutadas.

## Corte planificado de H4

**Implementación y pruebas G1 en H4; cierre intermodular posterior.** Implementar preparación/consentimiento UI+BFF y adaptadores/casos de cantidad/fulfillment/vigencias conforme contrato; fixtures rotulados donde falte proveedor. PREPARED no es pedido ni pago; cierre S03.

**Cierre base:** S03, semanas 12–13; implementación y pruebas propias comienzan en H4. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

Extensión por contratos: puede cerrar H4 si todas sus dependencias y pruebas reales pasan; mantener cierre base posterior hasta esa aceptación, sin duplicar conteo.

| Nivel de evidencia | Registro del corte de esta F |
|---|---|
| Diseñado | Specs enlazadas arriba; añadir revisión del flujo/contrato/frame concreto de H4. Su existencia no acredita aprobación de todas las discrepancias |
| Implementado con datos de prueba | Enlazar commit FE/BE, fixture explícito, comando y resultado positivo/negativo. Recuperar evidencia del código existente antes de certificar cobertura completa |
| Integrado con otro módulo | Pendiente de evidencia por operación: proveedor/versión, entorno, auth, request/response REAL, negativos y traza; respetar gates de esta F |
| Probado en el despliegue | Pendiente: URLs/SHAs/run CI-CD y caso desde web/API desplegada con revisión independiente. No inferir de prueba local ni de provider directo |

La actualización del 19/10/2026 cambia planificación, no estados de ejecución ni aprobación de gates. Registrar aquí evidencia concreta a medida que exista, sin calificar todo el bloque por una sola prueba.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F025-FE-001 | Frontend | Leonidas Garcia | Diego Espinoza | P0 | TASK-TRANS-S01-OPS-001 | 9–11 implementación H4 | Pendiente |
| TASK-F025-BE-001 | Backend | Leonidas Garcia | Diego Espinoza | P0 | TASK-TRANS-S01-OPS-001 + TASK-TRANS-S01-DB-001 | 9–11 implementación H4 | Pendiente |
| TASK-F025-DB-001 | BD / Prisma | Leonidas Garcia | Diego Espinoza | P0 | TASK-TRANS-S01-DB-001 | 9–11 implementación H4 | Pendiente |
| TASK-F025-INT-001 | Integración | Leonidas Garcia | Diego Espinoza | P0 | TASK-F025-BE-001 + TASK-F025-DB-001 + I-01 + I-02 + I-06 + G-CHECKOUT + TASK-F023-INT-001 + TASK-F024-INT-001 | 11 H4 REAL si gates; 13/S03 REAL | Bloqueado |
| TASK-F025-QA-001 | QA funcional | Leonidas Garcia | Diego Espinoza | P0 | TASK-F025-FE-001 + TASK-F025-BE-001 + TASK-F025-DB-001 | 11 H4 REAL si gates; 13/S03 REAL | Pendiente |
| TASK-F025-QA-002 | QA seguridad / DevSecOps | Leonidas Garcia | Diego Espinoza | P0 | TASK-F025-FE-001 + TASK-F025-BE-001 + TASK-TRANS-S02-OPS-002 (local H4); TASK-TRANS-S03-OPS-002 (cierre posterior) | 11 H4 REAL si gates; 13/S03 REAL | Pendiente |
| TASK-F025-DOC-001 | Documentación | Leonidas Garcia | Diego Espinoza | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F025-INT-001 + TASK-F025-QA-001 + TASK-F025-QA-002 | 11 H4 REAL si gates; 13/S03 REAL | Pendiente |

Referente de BD: Leonidas Garcia para este bloque, con revisión de Diego Espinoza; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F025-FE-001

- **Trabajo:** Implementar PaymentSimulationForm, PreparationOutcome y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico y sin requests internos navegador; usar los frames V-012 del [canvas Checkout en Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5&p=f&t=PXeKrikbDjSdUQ5l-0) como referencia visual. Cubrir estados desktop/mobile y casos de spec React.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F025-BE-001

- **Trabajo:** Preparar CheckoutOperation con clave/fingerprint, revalidar todo, PREPARED sin pedido/cobro/reserva.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F025-DB-001

- **Trabajo:** Integrar/verificar persistencia CheckoutOperation; sin crear entidades externas. Reutilizar migración común, no recrear tablas por funcionalidad.
- **Terminado cuando:** Modelo Prisma/migraciones y documentación concuerdan con baseline; prueba constraints/ownership/concurrencia/rollback pertinente pasa en PostgreSQL 16 temporal.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F025-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: I-01, I-02, I-06, G-CHECKOUT; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de I-01, I-02, I-06, G-CHECKOUT. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F025-QA-001

- **Trabajo:** Probar sin checkbox no preparación; doble click único intento; reintento misma clave; PREPARED no pantalla pedido exitoso; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F025-QA-002

- **Trabajo:** Fingerprint/clave reutilizada, replay de POST y concurrencia; no tarjeta/CVV ni reserva.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F025-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.
