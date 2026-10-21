# Tareas y seguimiento — F-002 Iniciar sesión

Versión 0.2.0 · Avance local H4 · integración REAL y revisión humana pendientes.

## Fuente y control

- [Plan F-002](../funcionalidades/F-002-iniciar-sesion.md); [iteración S02/H4](../iteraciones/S02-semanas-09-11.md).
- [Funcional](../../SPECS/funcional/F-002-iniciar-sesion.md), [UI](../../SPECS/ui/F-002-iniciar-sesion.md), [API](../../SPECS/contrato-api/F-002-iniciar-sesion.md), [React](../../SPECS/componentes-react/F-002-iniciar-sesion.md).
- [Reglas del seguimiento](README.md), [pruebas/DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [gates](../DECISIONES-Y-BLOQUEOS.md).
- Responsable asignado por el PO: **Jim Segovia**; revisor principal: **Andres Morales** según la [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base fijada en la matriz; ejecución y evidencia pendientes. La semana objetivo es académica, no fecha de calendario.
- Mock y real se reportan por separado. Existe evidencia local enlazada abajo; QA REAL, despliegue y aprobación siguen pendientes.

## Corte planificado de H4

**Objetivo de cierre H4.** Implementar login y desafío OTP según política efectiva G7, sesión/refresh, transporte seguro y retorno seguro; probar credenciales inválidas, expiración y separación usuario/servicio.

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. Disponibilidad sin restricción horaria por decisión del PO. Las entregas «local» o «con dobles» son etapas del mismo TASK, no cierres de INT. DOC prepara desde specs y QA ejecuta casos propios antes de INT; el cierre completo conserva dependencias/DoD. [Alcance H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md). Los estados no cambian al replanificar.

| Nivel de evidencia | Registro del corte de esta F |
|---|---|
| Diseñado | Specs enlazadas arriba; añadir revisión del flujo/contrato/frame concreto de H4. Su existencia no acredita aprobación de todas las discrepancias |
| Implementado con datos de prueba | FE [PR #105](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/105), BE [PR #229](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/229). G7 simulado, PostgreSQL real local; 15 pruebas auth dirigidas y 2 recorridos web. Evidencias y límites en las PR; no acredita cierre integral |
| Integrado con otro módulo | Pendiente de evidencia por operación: proveedor/versión, entorno, auth, request/response REAL, negativos y traza; respetar gates de esta F |
| Probado en el despliegue | Pendiente: URLs/SHAs/run CI-CD y caso desde web/API desplegada con revisión independiente. No inferir de prueba local ni de provider directo |

La actualización del 19/10/2026 cambia planificación, no estados de ejecución ni aprobación de gates. Registrar aquí evidencia concreta a medida que exista, sin calificar todo el bloque por una sola prueba.

## Tablero

| ID | Área | Responsable | Revisor | Prioridad | Depende de | Semana objetivo | Estado |
|---|---|---|---|---|---|---|---|
| TASK-F002-FE-001 | Frontend | Jim Segovia | Andres Morales | P0 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | Pendiente |
| TASK-F002-BE-001 | Backend | Jim Segovia | Andres Morales | P0 | TASK-TRANS-S01-OPS-001 | 9–10/H4 | Pendiente |
| TASK-F002-INT-001 | Integración | Jim Segovia | Andres Morales | P0 | TASK-F002-BE-001 + G-AUTH + TASK-F001-INT-001 | 11/H4 | Bloqueado |
| TASK-F002-QA-001 | QA funcional | Jim Segovia | Andres Morales | P0 | TASK-F002-FE-001 + TASK-F002-BE-001 | 11/H4 | Pendiente |
| TASK-F002-QA-002 | QA seguridad / DevSecOps | Jim Segovia | Andres Morales | P0 | TASK-F002-FE-001 + TASK-F002-BE-001 + TASK-TRANS-S02-OPS-002 | 11/H4 | Pendiente |
| TASK-F002-DOC-001 | Documentación | Jim Segovia | Andres Morales | P0 | H4 diseño/implementación: specs y pruebas locales; cierre completo: TASK-F002-INT-001 + TASK-F002-QA-001 + TASK-F002-QA-002 | 11/H4 | Pendiente |

Referente de BD: Jim Segovia para este bloque, con revisión de Andres Morales; Andres mantiene soporte transversal de migraciones. Ver [matriz](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md).

## Trabajo, Definition of Done y evidencia

### TASK-F002-FE-001

- **Trabajo:** Implementar LoginForm, MfaChallengeForm, LoginFlowContainer y todos los estados de React/UI.
- **Terminado cuando:** Props/eventos tipados, estado específico, sin requests internos navegador; desktop/mobile aplicables y casos de spec React cubiertos.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F002-BE-001

- **Trabajo:** Validar respuesta de login/desafío, completar MFA homologado y establecer sesión sólo al autenticarse; no fabricar sesión local.
- **Terminado cuando:** DTO, validación, errores y ownership probados con fixtures; transacciones/versiones donde aplica. Adaptador real no activado si gate externo sigue abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F002-INT-001

- **Trabajo:** Homologar y probar integración real y condiciones: G-AUTH; no sólo fixture.
- **Terminado cuando:** Contrato/configuración y gates enlazados, pruebas positivas/negativas y timeout autorizadas pasan; evidencia distingue sandbox de mock.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Falta cierre documentado de G-AUTH. Contrato/configuración y prueba enlazados antes de cambiar a En progreso.

### TASK-F002-QA-001

- **Trabajo:** Probar 401 es genérico; desafío no habilita rutas privadas; retorno externo rechazado; falla merge permite continuar sin sumar invitado; incluir cada estado visual y transición documentada.
- **Terminado cuando:** Casos unitarios/componentes/API y E2E aplicables pasan con evidencias; pruebas mock y reales etiquetadas. Hallazgos corregidos/reprobados.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F002-QA-002

- **Trabajo:** MFA no bypass, JWT inválido/expirado, open redirects, rate limit y no tokens en almacenamiento web.
- **Terminado cuando:** Negativos de seguridad pasan en entorno propio/autorizado, scans SAST/SCA/secrets y DAST aplicable adjuntos sin secretos. Sin hallazgo crítico/alto explotable abierto.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.

### TASK-F002-DOC-001

- **Trabajo:** Actualizar trazabilidad specs↔implementación↔pruebas, enlaces Figma y decisiones resueltas; documentar operación/errores relevantes.
- **Terminado cuando:** Fuentes vigentes coherentes, evidencias reales y revisión independiente; no marcar funcionalidad terminada con integración pendiente.
- **Evidencia:** Pendiente. Añadir revisión de código, comando/entorno/casos/resultados, hallazgos/retest y aprobación; sin secretos/PII.
- **Bloqueo / liberación:** Respetar dependencias del tablero y Ready; no existe evidencia de ejecución todavía.


## Registro de revisión

| Fecha/semana | Cambios de estado | Evidencia / bloqueo / decisión | Revisó |
|---|---|---|---|
| Semana 6, preparación | Creación de tareas; sin ejecución | Specs y plan elaborados; integración pendiente donde se indica | Revisión humana pendiente |

Actualizar filas existentes; no crear un segundo conjunto de tareas por variante desktop/mobile ni por cada estado visual. Si hace falta dividir una tarea, conservar ID padre y crear sufijo incremental con alcance/existencia verificable.

## Avance local — 21/10/2026

Jim inició FE/BE/QA local/DOC. Fuentes G7: docs 1b034d2, backend develop 4bd7b61. Implementación FE 0dc5d6e + CI 59de6cc, BE 068fbf9. [Frontend #105](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/105), [Backend #229](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/229), [contrato propuesto #9](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/9). Revisor solicitado: Andrés; aprobación pendiente.

[Casos FE y capturas](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/s2-f002-f003-g7/docs/evidencias/H4/jim-segovia/F002-F003.md), [casos BE](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s2-f002-f003-g7/docs/evidencias/H4/jim-segovia/F002-F003.md) y [preparación G7](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s2-f002-f003-g7/docs/INTEGRACION-G7-H4.md). Backend CI: auth-session y matriz Node 22/24 PASS. No hay cuentas A/B G7 ni URL/revisión BFF desplegada confirmadas (Jim indicó pendientes). G-DB heredado también continúa abierto.

QA local prueba MFA, credenciales neutras, cookie HttpOnly, refresh concurrente/timeout/reinicio, A/B, expiración, logout y otra pestaña. No acredita SAST/SCA/DAST completos, homologación, validación visual independiente ni despliegue. F-002 conserva la dependencia de fusión F-020; F-003 requiere completar validación de O-004 y su política durante envío. Las tareas permanecen En progreso y las INT Bloqueado.

Los textos iniciales de evidencia Pendiente de cada DoD se completan mediante este registro; no se marca Terminado por pruebas con dobles. Codex generó y probó los cambios; revisión humana de Jim/Andrés pendiente.
