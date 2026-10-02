# Especificaciones UI del Marketplace

Este directorio separa las reglas visuales transversales, el comportamiento UI por funcionalidad y los entregables concretos que se diseñarán en Figma.

## Capas documentales

| Capa | Identificador | Propósito | Ubicación |
|---|---|---|---|
| Sistema de diseño | `DS-###` | Define identidad, tokens, componentes, accesibilidad y reglas compartidas | [`DS-001`](./DS-001-sistema-diseno-marketplace.md) |
| Comportamiento UI funcional | `F-###` | Describe la experiencia y estados asociados a una capacidad atómica | Archivos `F-001` a `F-040` de este directorio |
| Vistas | `V-###` | Integra una o más funcionalidades en una pantalla completa desktop/mobile | [`vistas/`](./vistas/README.md) |
| Overlays | `O-###` | Especifica modales, drawers, visores, toasts y feedback superpuesto | [`overlays/`](./overlays/README.md) |
| Comunicaciones | `C-###` | Especifica piezas visuales externas, como correos transaccionales | [`comunicaciones/`](./comunicaciones/README.md) |

## Planificación y reparto

| Documento | Uso |
|---|---|
| [`Inventario visual y estimación`](./INVENTARIO-VISUAL-Y-ESTIMACION.md) | Consolida las 29 piezas, su puntuación y el equilibrio de carga. |
| [`Paquetes individuales`](./reparto/README.md) | Entrega a cada integrante sus specs, frames, dependencias, pendientes, orden y checklist. |

## Cómo leer la documentación

1. Consultar `DS-001` para conocer las reglas visuales comunes.
2. Abrir el documento `V-###`, `O-###` o `C-###` del entregable que se diseñará.
3. Seguir sus enlaces hacia las specs `F-###` para validar reglas, acciones y estados.
4. Diseñar todos los frames requeridos y conservar los identificadores en Figma.
5. Registrar en la spec cualquier decisión nueva antes de incorporarla como comportamiento definitivo.

## Fuente vigente y antecedentes

- Los catálogos `V`, `O` y `C` son el inventario vigente para planificar y repartir el diseño.
- Las specs `F-###` continúan siendo la fuente del comportamiento UI de cada funcionalidad.
- Los documentos de `Wireframes y Prototipo/` son antecedentes y no deben prevalecer cuando contradicen las specs vigentes.
- La nomenclatura completa se encuentra en [`SPECS/NOMENCLATURA-SDD.md`](../NOMENCLATURA-SDD.md).

## Criterio para comenzar un mockup

Un entregable puede asignarse cuando su spec:

- identifica todas las funcionalidades relacionadas;
- define composición, contenido, acciones y navegación;
- cubre sus estados aplicables;
- especifica desktop, mobile y accesibilidad;
- enumera los frames requeridos;
- no mantiene decisiones abiertas que cambien sustancialmente el layout.
