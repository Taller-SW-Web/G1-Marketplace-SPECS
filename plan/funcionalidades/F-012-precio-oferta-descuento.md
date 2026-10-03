# Plan de implementación — F-012 Visualizar precio, oferta y descuento vigente

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-012 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 2, semanas 8–9 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-012-precio-oferta-descuento.md), [UI](../../SPECS/ui/F-012-precio-oferta-descuento.md), [API](../../SPECS/contrato-api/F-012-precio-oferta-descuento.md), [React](../../SPECS/componentes-react/F-012-precio-oferta-descuento.md) |
| Ejecución y revisores | [Tareas de F-012](../seguimiento/F-012-precio-oferta-descuento.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar precio, oferta y descuento vigente conforme comportamiento/UI/API/React, no una pantalla aislada.
F-013 resuelve SKU; respuesta vieja no pisa selección nueva. Expiración invalida región y refresca según vigencia, no promete precio final.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ProductPriceRegion`, `PriceDisplay`; hook `useProductPrice`; arquitectura transversal React. |
| Backend / adaptador | Adaptar Pricing por SKU/canal/momento, validar vigencia y precio, limitar caché y derivar descuento de importes autoritativos. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','price',slug,sku]; deshabilitar query hasta SKU aplicable; freshness no supera validUntil. |
| Seguridad específica | SKU de otro producto, versión/vigencia inválida y caché sin costos internos. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-011](F-011-detalle-producto.md), [F-013](F-013-seleccion-atributos-variante.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01/Pricing; cache comercial no autoritativa.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-012-precio-oferta-descuento.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- sin SKU no precio ajeno.
- sin oferta no 0%.
- caducidad retira badge y referencia juntos.
- error no oculta descripción.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: SKU de otro producto, versión/vigencia inválida y caché sin costos internos.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

WAITING_FOR_VARIANT → LOADING → REGULAR | SALE | UNAVAILABLE; al cambiar SKU retirar importe previo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

