# Plan de implementación — F-037 Visualizar favoritos

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-037 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 3, semanas 10–11 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-037-visualizar-favoritos.md), [UI](../../SPECS/ui/F-037-visualizar-favoritos.md), [API](../../SPECS/contrato-api/F-037-visualizar-favoritos.md), [React](../../SPECS/componentes-react/F-037-visualizar-favoritos.md) |
| Ejecución y revisores | [Tareas de F-037](../seguimiento/F-037-visualizar-favoritos.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar favoritos conforme comportamiento/UI/API/React, no una pantalla aislada.
GET propia lista; F-038/039 mutaciones actualizan colección. Sin sesión redirección segura, caché privada limpia.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `WishlistPageContainer`, `WishlistProductCard`; hook `useWishlist`; arquitectura transversal React. |
| Backend / adaptador | Leer propios favoritos por createdAt DESC, enriquecer y definir producto retirado sin borrar intención. |
| Persistencia | WishlistItem (sólo lectura). Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['wishlist',sessionScope]; lista privada enriquecida, nunca persistir favorita de otro titular. |
| Seguridad específica | Caché/fuga entre cuentas, no dato sensible en fav. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-036](F-036-agregar-favorito.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; política mostrar/omitir producto retirado abierta V-009.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-037-visualizar-favoritos.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- lista vacía con CTA.
- producto retirado sin compra.
- 503 no borra intención.
- 401 no conserva datos previos.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Caché/fuga entre cuentas, no dato sensible en fav.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → READY | EMPTY | ERROR; item UNAVAILABLE distingue producto retirado de fallo global de catálogo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

