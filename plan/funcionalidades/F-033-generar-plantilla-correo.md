# Plan de implementación — F-033 Generar plantilla de correo

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-033 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 5, semanas 14–15 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-033-generar-plantilla-correo.md), [UI](../../SPECS/ui/F-033-generar-plantilla-correo.md), [API](../../SPECS/contrato-api/F-033-generar-plantilla-correo.md), [React](../../SPECS/componentes-react/F-033-generar-plantilla-correo.md) |
| Ejecución y revisores | [Tareas de F-033](../seguimiento/F-033-generar-plantilla-correo.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar generar plantilla de correo conforme comportamiento/UI/API/React, no una pantalla aislada.
F-034/F-035 worker invoca renderer interno. React Email u otra librería no elegida: estos componentes expresan anatomía, no obligación de instalar librería ni endpoint público.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `TransactionalEmailTemplate`, `EmailOrderSummary`; hook `No hook cliente; renderEmail(payload) sólo servidor`; arquitectura transversal React. |
| Backend / adaptador | Render interno versionado HTML/texto seguro desde snapshot autorizado, recomendaciones opcionales y URLs configuradas. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | No query desde browser; entrada interna versionada y snapshot autorizado. |
| Seguridad específica | Inyección HTML/asunto / URL y secretos/PII ausentes, /internal inaccesible navegador. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: base técnica y contratos aplicables; no otra funcionalidad obligatoria.
- Gates: G-MAIL; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: C-001/C-002, proveedor y motor render por confirmar.
- Responsable/revisor confirman disponibilidad, estimación y criterio; contrato/fixtures definidos; estados de UI leídos. Mockups no asignan automáticamente código.
- Si gate afecta operación real, limitar trabajo a componentes puros, fixtures y tests locales. Nunca interpretar eso como integración terminada.

## 5. Fases, entregables y validación

| Fase | Entregable | Depende de | Verificación |
|---|---|---|---|
| 1 | Contratos tipados, fixtures y casos negativos | Ready y specs | Shape de API, estados y seguridad trazables |
| 2 | Componentes/contendedor o render server-only + BFF | Base, API/React; DB si aplica | Build/lint/typecheck y pruebas de contrato local |
| 3 | Persistencia/adaptador real o integración local | Gates aplicables y transacciones | Pruebas API/DB y sandbox autorizado |
| 4 | E2E/responsive/accesibilidad y seguridad | Partes conectadas | Casos de React y QA-002, scans y DAST aplicable |
| 5 | Revisión/evidencias/entrega | Pruebas y contratos aprobados | DoD, documentación y resultado demostrable |

Puede trabajarse FE/BE con mocks en paralelo, pero las condiciones bloquean activación real hasta cierre.
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-033-generar-plantilla-correo.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin imágenes texto/CTA útil.
- HTML escapa contenido malicioso.
- misma versión render semántico igual.
- sin recomendaciones correo válido.
- no JS ni secretos.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Inyección HTML/asunto / URL y secretos/PII ausentes, /internal inaccesible navegador.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

VALID_INPUT → RENDERED | RENDER_FAILED; recomendaciones vacías/fallidas omiten sección sin impedir correo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

