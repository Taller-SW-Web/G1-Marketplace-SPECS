# Plan de implementación — F-004 Solicitar recuperación de contraseña

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-004 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-004-solicitar-recuperacion-password.md), [UI](../../SPECS/ui/F-004-solicitar-recuperacion-password.md), [API](../../SPECS/contrato-api/F-004-solicitar-recuperacion-password.md), [React](../../SPECS/componentes-react/F-004-solicitar-recuperacion-password.md) |
| Ejecución y revisores | [Tareas de F-004](../seguimiento/F-004-solicitar-recuperacion-password.md); responsable asignado por el PO: **Jim Segovia**; revisor principal: **Andres Morales**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4, actualizado por decisión PO 26/10/2026.** Implementar la entrada G1 a la recuperación en la SPA G7; mantener y probar el adaptador BFF G1 como integración API separada. G7 presenta el formulario, 202 uniforme, rate limit, correo y enlace. Probar el entorno, la entrega del enlace y el regreso a Marketplace sin emitir identidad propia. [Alcance y pendientes](../coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar la entrada desde Marketplace a G7 y la integración comprobable. La UI final de correo y confirmación reside en G7; el formulario G1 preparado antes de la decisión no es el recorrido objetivo. El 202 muestra el mismo copy exista o no cuenta. G1 no invoca email/provider ni crea token desde frontend.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | Entrada de login hacia SPA G7 mediante origen configurado; retirar o redirigir la ruta/formulario G1 anterior sin aceptar destino arbitrario. |
| Backend / adaptador | Delegar recuperación con202 uniforme y rate limiting publicado, sin existencia de cuenta ni tokens locales. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | El navegador G1 no envía correo en el recorrido elegido; el adaptador BFF conserva sus pruebas API sin cachear correo ni resultado por usuario. |
| Seguridad específica | Respuesta/latencia antienumeración y rate limit; no email/token en logs. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: base técnica y contratos aplicables; no otra funcionalidad obligatoria.
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: destino G7 configurado, condición de disponibilidad y retorno permitido a login G1; tiempo/copy de límite en la SPA G7 con Seguridad.
- Responsable/revisor confirman alcance, contrato y criterios de prueba; contrato/fixtures definidos; estados de UI leídos. Mockups no asignan automáticamente código.
- Si gate afecta operación real, limitar trabajo a componentes puros, fixtures y tests locales. Nunca interpretar eso como integración terminada.

## 5. Fases, entregables y validación

| Fase | Entregable | Depende de | Verificación |
|---|---|---|---|
| 1 | Contratos tipados, fixtures y casos negativos | Ready y specs | Shape de API, estados y seguridad trazables |
| 2 | Entrada G1 a G7, tratamiento de ruta G1 anterior y BFF existente | Base, API/React; DB si aplica | Build/lint/typecheck y pruebas de navegación/contrato local |
| 3 | Persistencia/adaptador real o integración local | Gates aplicables y transacciones | Pruebas API/DB y sandbox autorizado |
| 4 | E2E/responsive/accesibilidad y seguridad | Partes conectadas | Casos de React y QA-002, scans y DAST aplicable |
| 5 | Revisión/evidencias/entrega | Pruebas y contratos aprobados | DoD, documentación y resultado demostrable |

Puede trabajarse FE/BE con mocks en paralelo, pero las condiciones bloquean activación real hasta cierre.
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-004-solicitar-recuperacion-password.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- 202 idéntico con ambos fixtures de existencia.
- La entrada de login G1 abre la SPA G7 desde configuración confiable; no conserva formulario competidor.
- El correo G7 lleva a restablecimiento G7; retorno a login G1 probado en navegador y sin sesión implícita.
- formato inválido no llama API.
- 429 no enumera.
- Enter no duplica envío.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Respuesta/latencia antienumeración y rate limit; no email/token en logs.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

EDITING → REQUESTING → ACCEPTED | RATE_LIMITED | ERROR; 429 conserva correo y permite reintento después de espera aprobada.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
