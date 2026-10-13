# SPECS vigentes — Marketplace

Las **40 funcionalidades F-001–F-040** constituyen el catálogo de implementación. Cada ID tiene cuatro fuentes complementarias: [funcional](funcional/), [UI](ui/), [contrato API](contrato-api/) y [componentes React](componentes-react/). La [nomenclatura](NOMENCLATURA-SDD.md) define los identificadores; el [inventario de fuentes](INVENTARIO-FUENTES.md) documenta su origen. La [matriz de ocho bloques y siete responsables](RESPONSABILIDADES-PUNTA-A-PUNTA.md) fija ownership punta a punta, revisores y estimación base para S1–S5 por decisión del PO. La consulta académica al profesor sigue abierta.

## Orden de lectura por funcionalidad

1. Buscar el ID F-### en la [matriz](RESPONSABILIDADES-PUNTA-A-PUNTA.md) para identificar bloque, owner, revisor, hito y gates.
2. Leer el mismo archivo F-### en [funcional/](funcional/), [ui/](ui/), [contrato-api/](contrato-api/) y [componentes-react/](componentes-react/). Una decisión de reparto **no cambia** comportamiento, API, diseño ni su versión.
3. Revisar entregables visuales en [vistas V-###](ui/vistas/README.md), [overlays O-###](ui/overlays/README.md), [correos C-###](ui/comunicaciones/README.md) y [DS-001](ui/DS-001-sistema-diseno-marketplace.md). El [reparto de mockups](ui/INVENTARIO-VISUAL-Y-ESTIMACION.md) identifica autores de diseño, no dueños del código.
4. Consultar [plan por funcionalidad](../plan/README.md), [tareas/estados](../plan/seguimiento/README.md), [paquete individual](../plan/repartición%20por%20integrantes/README.md) y [decisiones/gates](../plan/DECISIONES-Y-BLOQUEOS.md). Una tarea bloqueada sigue bloqueada hasta prueba y revisión del proveedor; fixture `MOCK` no equivale a integración `REAL`.

## Límites vigentes

- Frontend decidido por el PO: **React + TypeScript + Next.js App Router**. UI kit/versiones/lockfile siguen pendientes; no deducir una aplicación funcional de estas specs.
- Marketplace implementa su propio BFF/adaptadores y persistencia definida por el [modelo lógico](../Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/01-Modelo-logico-inicial.md). Seguridad, Productos, Ventas y Despacho conservan datos y reglas de sus dominios. Contratos y entornos se comprueban antes de codificar rutas ajenas.
- [`specs-depreciadas/`](specs-depreciadas/) contiene los antiguos SPEC-01–SPEC-08, épicas e historias como **antecedente histórico**. Sus nombres, puntos y responsables no gobiernan F-001–F-040, el reparto actual ni la fecha de integración. F-040, evaluación postentrega, es adicional a los ocho bloques literales del sílabo.
- Plan, código, pruebas y despliegues tienen fuentes de verdad distintas. Una spec aprobada o un mockup no acredita software ejecutado; el cierre se prueba en el seguimiento con PR, commit, pruebas y evidencia `REAL` cuando corresponda.
