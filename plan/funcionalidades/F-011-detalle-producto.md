# Plan de implementación — F-011 Visualizar ficha y galería del producto

## 1. Metadatos y entradas

| Campo | Valor |
|---|---|
| ID / versión / estado | F-011 / 0.1.0 / En revisión |
| Objetivo académico | Sprint 2, semanas 8–9 |
| Entrada SDD | [Funcional](../../SPECS/funcional/F-011-detalle-producto.md), [UI](../../SPECS/ui/F-011-detalle-producto.md), [API](../../SPECS/contrato-api/F-011-detalle-producto.md), [React](../../SPECS/componentes-react/F-011-detalle-producto.md) |
| Ejecución y revisores | [Tareas de F-011](../seguimiento/F-011-detalle-producto.md), propuesta según roles actuales |
| Plan general / seguridad | [Semanas 6–15](../PLAN-IMPLEMENTACION.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md) |

## 2. Objetivo y límites

Entregar visualizar ficha y galería del producto conforme comportamiento/UI/API/React, no una pantalla aislada.
Reintentar sólo detalle. Imagen principal fallida usa respaldo y no borra texto; secundaria fallida conserva principal anterior. F-013 puede proveer imagen de variante sin mutar DTO.

## 3. Decisiones técnicas

| Área | Trabajo / decisión |
|---|---|
| Frontend / render | `ProductDetailContainer`, `ProductGallery`, `GalleryViewer`, `TechnicalSpecifications`; hook `useProductDetail`; arquitectura transversal React. |
| Backend / adaptador | Adaptar detalle público/slug, marca/medios/especificaciones, ETag y exclusión de regiones comerciales. |
| Persistencia | Sin persistencia de dominio local. Siempre modelo lógico vigente, nunca el esquema histórico de dos tablas. |
| Remoto / caché | ['catalog','detail',slug]; respetar ETag/cache del BFF; query independiente de precio/variantes/stock. |
| Seguridad específica | XSS en descripción/especificaciones, slug traversal y SSRF/medios fuera allowlist. |
| UI Kit | DS-001 v0.2.0; G-STACK pendiente, no fijar versiones no verificadas. |

## 4. Dependencias y Definition of Ready

- Dependencias de comportamiento/flujo: [F-006](F-006-inicio-categorias-destacados.md).
- Gates: I-01; consultar [registro](../DECISIONES-Y-BLOQUEOS.md). G-STACK/G-SHELL para interfaz compartida aplicable.
- Pendientes específicos: I-01; detalle no entrega SKU simple: resolver en contrato variantes F-013, cerrar shape hasVariants=false.
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
Las tareas y el estado real viven únicamente en [seguimiento](../seguimiento/F-011-detalle-producto.md); aquí no se duplica un tablero.

## 6. Criterios de terminado y pruebas

- controles deshabilitados en extremos.
- imagen fallida conserva texto.
- 404 neutral.
- visor Escape restaura foco.
- descripción maliciosa no ejecuta script.
- Cada estado documentado tiene caso verificable y foco/recuperación correctos.
- Seguridad: XSS en descripción/especificaciones, slug traversal y SSRF/medios fuera allowlist.
- DB si aplica: identidad/constraints/versiones/transacción y rollback probados sin persistencia prohibida.
- Evidencias sanitizadas y revisión por persona distinta, según [DoD general](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Cuando se exige homologación, prueba real aprobada además de fixture. Si bloqueada, funcionalidad no se declara completa.

## 7. Riesgos y recuperación

LOADING → READY | NOT_AVAILABLE | ERROR; MEDIA_FALLBACK es estado de render de una imagen válida, no respuesta sin medios.

No reintentos ilimitados ni datos locales como fuente externa de verdad. Campos, endpoints y política que sigan abiertos permanecen explícitos; resolver/actualizar spec de origen antes de modificar código. Riesgo de capacidad/fecha se revisa cada sprint sin retirar esta funcionalidad ocultamente.

