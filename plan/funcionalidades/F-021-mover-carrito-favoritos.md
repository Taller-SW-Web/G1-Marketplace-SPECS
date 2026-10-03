# Plan de implementación — F-021 Mover un ítem del carrito a favoritos

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-021 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 3, semanas 10–11 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-021-mover-carrito-favoritos.md), [UI](../../SPECS/ui/F-021-mover-carrito-favoritos.md), [API](../../SPECS/contrato-api/F-021-mover-carrito-favoritos.md), [React](../../SPECS/componentes-react/F-021-mover-carrito-favoritos.md) |
| Ejecución y revisores | [Tareas de F-021](../seguimiento/F-021-mover-carrito-favoritos.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar mover un ítem del carrito a favoritos conforme comportamiento/UI/API/React, no una pantalla aislada.
Sin sesión conserva línea e inicia auth con retorno; intención puede volver a ofrecerse después de login, no ejecutar silenciosamente una mutación tras login.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `MoveCartToWishlistAction`; hook `useMoveCartToWishlist`; arquitectura transversal React. |
| Backend / adaptador | Upsert WishlistItem a nivel productId + quitar línea/versionar en única transacción, con titular del JWT. |
| Persistencia | CartItem/WishlistItem. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | Invalidar cart/wishlist y quote sólo tras éxito; no intentar encadenar POST wishlist + DELETE desde navegador. |
| Seguridad específica | Movimiento sólo titular y transacción sin borrado parcial ni favorito ajeno. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-019](F-019-visualizar-carrito.md), [F-036](F-036-agregar-favorito.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; transacción local CartItem/WishlistItem.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-021-mover-carrito-favoritos.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin sesión no POST.
- fallo conserva línea.
- ya favorito quita sólo al confirmar.
- ambas cachés se actualizan.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Movimiento sólo titular y transacción sin borrado parcial ni favorito ajeno.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

READY → AUTH_REQUIRED | MOVING → MOVED | ALREADY_FAVORITE | ERROR; error conserva línea.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

