# Plan de implementación — F-022 Capturar o seleccionar dirección de envío

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-022 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 4, semanas 12–13 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-022-seleccionar-direccion-envio.md), [UI](../../SPECS/ui/F-022-seleccionar-direccion-envio.md), [API](../../SPECS/contrato-api/F-022-seleccionar-direccion-envio.md), [React](../../SPECS/componentes-react/F-022-seleccionar-direccion-envio.md) |
| Ejecución y revisores | [Tareas de F-022](../seguimiento/F-022-seleccionar-direccion-envio.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar capturar o seleccionar dirección de envío conforme comportamiento/UI/API/React, no una pantalla aislada.
BFF GET/POST consulta y registra con token titular, nunca técnico. 201 seleccionar addressId confirmado; cambiar selección invalida quote y PREPARED; revalidar carrito antes de continuar.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `DeliveryAddressPicker`, `NewDeliveryAddressForm`, `AddressStepContainer`; hook `useDeliveryAddresses`; arquitectura transversal React. |
| Backend / adaptador | Adaptar GET/POST direcciones Seguridad con token del titular, sin userId manipulable ni persistencia local. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['checkout','addresses',sessionScope] con caché efímera; sólo addressId seleccionado en contexto de flujo. |
| Seguridad específica | Token titular no técnico, dirección ajena rechazada y cuerpos excluidos storage/logs. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-002](F-002-iniciar-sesion.md), [F-019](F-019-visualizar-carrito.md).
- Gates: G-ADDRESS; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: Contrato Seguridad confirmado; límites/maestros aún abiertos V-010-OPEN-01/02.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-022-seleccionar-direccion-envio.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- vacío formulario abierto.
- 400 conserva campos válidos.
- 401 retira direcciones.
- request no incluye identidad editable.
- dirección cambio invalida quote.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Token titular no técnico, dirección ajena rechazada y cuerpos excluidos storage/logs.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → LIST | NEW_ADDRESS | ERROR; SAVE → CREATED_SELECTED | FIELD_ERROR | ERROR; EMPTY abre formulario;401 limpia datos.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

