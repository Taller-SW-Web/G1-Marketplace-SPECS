# Plan de implementación — F-005 Restablecer contraseña

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-005 / 0.1.0 / En revisión |
| Objetivo académico | S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-005-restablecer-password.md), [UI](../../SPECS/ui/F-005-restablecer-password.md), [API](../../SPECS/contrato-api/F-005-restablecer-password.md), [React](../../SPECS/componentes-react/F-005-restablecer-password.md) |
| Ejecución y revisores | [Tareas de F-005](../seguimiento/F-005-restablecer-password.md); responsable asignado por el PO: **Jim Segovia**; revisor principal: **Andres Morales**. [Matriz de bloques](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md). Estimación base en la matriz; ejecución y evidencia pendientes. |
| Plan general / seguridad | [Semanas 7–16](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## Entrega de H4 y cierre objetivo

**Objetivo de cierre H4, actualizado por decisión PO 26/10/2026.** G7 implementa el formulario y la política de restablecimiento en su SPA; G1 mantiene el adaptador BFF y prueba la integración API, la entrada desde Marketplace y el retorno permitido al login G1. Probar enlace/token válido, vencido y usado, errores neutros y ausencia de sesión implícita. [Alcance y pendientes](../coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md).

**Cierre base:** S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue. El PO establece disponibilidad sin restricción horaria; todo el trabajo propio definido se implementa y prueba en H4. Los límites son contrato, entorno, datos, autorizaciones y calidad. [Inventario H4](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [S02](../iteraciones/S02-semanas-09-11.md). Registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en el despliegue por separado; no inventar contrato ni liberar gates por planificar.

## 2. Objetivo y límites

Entregar el recorrido Marketplace → G7 → login Marketplace. El correo abre la SPA G7 y el token permanece allí; el formulario G1 preparado antes de la decisión no es el recorrido objetivo. No confundir el token con verificación F-001. El 204 borra secretos y ofrece login G1, sin sesión automática.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | Formulario y estados en G7; G1 trata su ruta anterior sin recibir tokens del enlace. Retorno G7 → login G1 con destino fijo permitido. |
| Backend / adaptador | Delegar reset con token efímero, política y errores401/410/422; no sesión automática. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Sin query inventada de validación de token. El adaptador BFF conserva el POST para pruebas API; el navegador G1 no recibe el token del correo. |
| Seguridad específica | Token reset usado/vencido, contraseña no filtrada, referrer/analítica y no sesión automática. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-004](F-004-solicitar-recuperacion-password.md).
- Gates: G-AUTH; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: G7 debe permitir el retorno fijo a login G1 y probarlo; V-004-OPEN-02 sobre validación previa pertenece a la SPA G7 y no habilita un endpoint G1 inventado.
- Responsable/revisor confirman alcance, contrato y criterios de prueba; contrato/fixtures definidos; estados de UI leídos. Mockups no asignan automáticamente código.
- Si gate afecta operación real, limitar trabajo a componentes puros, fixtures y tests locales. Nunca interpretar eso como integración terminada.

## 5. Fases, entregables y validación

| Fase | Entregable | Depende de | Verificación |
|---|---|---|---|
| 1 | Contratos tipados, fixtures y casos negativos | Ready y specs | Shape de API, estados y seguridad trazables |
| 2 | Tratamiento de ruta G1 anterior, retorno G7 y BFF existente | Base, API/React; DB si aplica | Build/lint/typecheck y pruebas de navegación/contrato local |
| 3 | Persistencia/adaptador real o integración local | Gates aplicables y transacciones | Pruebas API/DB y sandbox autorizado |
| 4 | E2E/responsive/accesibilidad y seguridad | Partes conectadas | Casos de React y QA-002, scans y DAST aplicable |
| 5 | Revisión/evidencias/entrega | Pruebas y contratos aprobados | DoD, documentación y resultado demostrable |

Puede trabajarse FE/BE con mocks en paralelo, pero las condiciones bloquean activación real hasta cierre.
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-005-restablecer-password.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin token no llama API.
- 401 y 410 ofrecen nuevo enlace.
- 422 no muestra token.
- 204 no crea sesión.
- El enlace del correo abre G7, nunca un formulario G1 con token.
- El éxito de G7 vuelve al login G1 mediante destino fijo permitido, sin sesión ni token en la URL de retorno.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Token reset usado/vencido, contraseña no filtrada, referrer/analítica y no sesión automática.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-done-y-evidencia).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

CHECKING_INPUT → EDITING → SAVING → SUCCESS | INVALID | EXPIRED | POLICY_ERROR | ERROR; comprobación inicial no certifica vigencia externa.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Los riesgos de contrato, entorno y calidad se revisan por operación, sin retirar esta funcionalidad por disponibilidad horaria.
