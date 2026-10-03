# Plan de implementación — F-006 Visualizar inicio, categorías y destacados

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-006 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 2, semanas 8–9 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [UI](../../SPECS/ui/F-006-inicio-categorias-destacados.md), [API](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [React](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md) |
| Ejecución y revisores | [Tareas de F-006](../seguimiento/F-006-inicio-categorias-destacados.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar inicio, categorías y destacados conforme comportamiento/UI/API/React, no una pantalla aislada.
BFF entrega categories y featuredProducts. Favoritos autenticados se resuelven aparte por F-036/037 y no se incrustan en caché pública.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `HomePageContainer`, `CategoryGrid`, `FeaturedProducts`; hook `useHome`; arquitectura transversal React. |
| Backend / adaptador | Adaptar home Catálogo, filtrar tarjetas/categorías activas completas y permitir listas vacías. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','home']; sólo caché pública, sin almacenar datos personalizados aquí. |
| Seguridad específica | Producto inactivo no publicable, enlaces hero seguros y medios allowlist. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: base técnica y contratos aplicables; no otra funcionalidad obligatoria.
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; contenido hero, reglas editoriales y navegación pendientes de V-005.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-006-inicio-categorias-destacados.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- ambos arreglos vacíos ofrecen catálogo.
- error no rompe cabecera.
- categoría genera URL válida.
- favorito sin sesión abre O-003.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: Producto inactivo no publicable, enlaces hero seguros y medios allowlist.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → READY | EMPTY | ERROR; categories vacías omiten categoría; destacados vacíos omiten sección; ambos vacíos mantienen acceso a catálogo.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

