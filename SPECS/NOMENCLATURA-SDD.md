# Nomenclatura e identificadores SDD

Este documento define los nombres e identificadores oficiales para las especificaciones, planes, tareas y componentes del módulo Marketplace.

## 1. Principios

- Los identificadores representan funcionalidades, no personas.
- Los identificadores son estables: no cambian cuando cambia el responsable.
- Los nombres deben ser breves, descriptivos y consistentes.
- Se usará español para los nombres funcionales y nombres técnicos estándar cuando corresponda.
- No se usarán códigos de épicas o historias como estructura principal de las nuevas specs.
- Los códigos antiguos se conservarán sólo como referencias de migración cuando sea necesario.

## 2. Identificadores funcionales

Cada funcionalidad atómica usa el formato `F-###`, con numeración consecutiva de tres dígitos. Ejemplo: `F-011` para visualizar ficha y galería del producto.

El catálogo oficial, sus nombres cortos y sus fuentes están en [`03-Catalogo-de-funcionalidades-Marketplace.md`](../../../Almacen%20de%20Contexto/03-Catalogo-de-funcionalidades-Marketplace.md). El análisis que sustenta el catálogo está en [`ANALISIS-FASE-2.md`](../../../Almacen%20de%20Contexto/ANALISIS-FASE-2.md). El ID `F-###` conecta todos los documentos de una misma funcionalidad.

Las ocho agrupaciones anteriores se conservan únicamente como **áreas de organización**; no son IDs de specs ni unidades de implementación.

| Área | Cobertura funcional |
|---|---|
| Cuenta y acceso | `F-001` a `F-005` |
| Descubrimiento del catálogo | `F-006` a `F-010` |
| Evaluación del producto | `F-011` a `F-015` |
| Carrito de compra | `F-016` a `F-021` |
| Checkout y orden | `F-022` a `F-027` |
| Pedidos y entrega | `F-028` a `F-032` |
| Notificaciones por correo | `F-033` a `F-035` |
| Favoritos | `F-036` a `F-039` |
| Evaluación postentrega | `F-040` |

### Identificadores transversales de diseño

Los documentos que definen reglas visuales aplicables a más de una funcionalidad usan el formato `DS-###`. No son funcionalidades ni tareas; se referencian desde las specs UI individuales.

| ID | Uso |
|---|---|
| `DS-001` | Sistema de diseño transversal del Marketplace. |

### Identificadores de entregables visuales

Las funcionalidades `F-###` describen capacidades del sistema, pero no equivalen necesariamente a una pantalla de Figma. Para especificar los entregables visuales se usan los siguientes identificadores:

| Prefijo | Significado | Cuándo se usa | Ejemplo |
|---|---|---|---|
| `V-###` | Vista o ruta principal | Pantalla completa con ruta propia o estado principal claramente navegable | `V-007-ficha-producto.md` |
| `O-###` | Overlay o feedback superpuesto | Modal, drawer, toast, visor, confirmación o interacción que aparece sobre una vista | `O-002-visor-galeria.md` |
| `C-###` | Comunicación visual externa | Pieza que se diseña fuera de la interfaz navegable, como un correo transaccional | `C-001-correo-confirmacion-pedido.md` |

Reglas de uso:

- Una vista puede agrupar varias funcionalidades `F-###`.
- Una funcionalidad puede afectar más de una vista, overlay o comunicación.
- No se crea una vista independiente cuando el comportamiento corresponde a un estado, una variante responsive o un overlay.
- Cada documento `V-###`, `O-###` o `C-###` debe declarar las funcionalidades relacionadas y enlazar sus specs UI de origen.
- Los frames de Figma deben conservar el identificador del documento correspondiente para mantener la trazabilidad.

## 3. Nombres de archivos

Cada tipo de documento usa el mismo ID y nombre corto:

```text
SPECS/funcional/F-011-detalle-producto.md
SPECS/ui/F-011-detalle-producto.md
SPECS/contrato-api/F-011-detalle-producto.md
SPECS/componentes-react/F-011-detalle-producto.md
SPECS/ui/DS-001-sistema-diseno-marketplace.md
SPECS/ui/vistas/V-007-ficha-producto.md
SPECS/ui/overlays/O-002-visor-galeria.md
SPECS/ui/comunicaciones/C-001-correo-confirmacion-pedido.md

plan/F-011-detalle-producto.md
tareas/F-011-detalle-producto.md
```

No se deben agregar nombres de integrantes, fechas o tecnologías al nombre del archivo. Esa información pertenece a los metadatos del documento.

## 4. Identificadores internos

| Prefijo | Uso | Ejemplo |
|---|---|---|
| `FR-F###-###` | Regla o requisito funcional | `FR-F011-001` |
| `UI-F###-###` | Requisito o comportamiento de interfaz | `UI-F011-001` |
| `API-F###-###` | Endpoint o elemento del contrato API | `API-F011-001` |
| `CMP-F###-###` | Componente React | `CMP-F011-001` |
| `DS-###` | Documento transversal de sistema de diseño | `DS-001` |
| `V-###` | Vista o ruta principal | `V-007` |
| `O-###` | Overlay o feedback superpuesto | `O-002` |
| `C-###` | Comunicación visual externa | `C-001` |
| `TASK-F###-FE-###` | Tarea de frontend | `TASK-F011-FE-001` |
| `TASK-F###-BE-###` | Tarea de backend | `TASK-F011-BE-001` |
| `TASK-F###-DB-###` | Tarea de persistencia | `TASK-F011-DB-001` |
| `TASK-F###-INT-###` | Tarea de integración | `TASK-F011-INT-001` |
| `TASK-F###-QA-###` | Tarea de pruebas y validación | `TASK-F011-QA-001` |

Los números se asignan de forma incremental dentro de cada funcionalidad y tipo.

## 5. Versionado

Cada documento debe indicar una versión con formato `MAJOR.MINOR.PATCH`:

| Versión | Uso |
|---|---|
| `0.1.0` | Primer borrador |
| `0.2.0` | Borrador ampliado o en revisión |
| `1.0.0` | Documento aprobado |
| `1.1.0` | Cambio compatible que agrega o aclara información |
| `2.0.0` | Cambio que modifica el comportamiento o contrato aprobado |
| `1.0.1` | Corrección editorial o aclaración menor |

## 6. Estados de los documentos

- `Borrador`: contenido inicial en elaboración.
- `En revisión`: pendiente de validación del responsable y revisor.
- `Aprobada`: validada por el equipo y lista para derivar el siguiente artefacto.
- `En cambio`: se está modificando por una decisión nueva.
- `Obsoleta`: reemplazada por una versión posterior.

## 7. Reglas de trazabilidad

- Toda spec debe indicar su `F-###` y sus documentos relacionados.
- Todo plan debe enlazar a las cuatro specs de entrada.
- Toda tarea debe enlazar al plan y a las specs que le dieron origen.
- Todo cambio de comportamiento debe actualizar la spec funcional.
- Todo cambio visual debe actualizar la spec UI.
- Todo cambio de integración debe actualizar la spec de contrato API.
- Todo cambio de estructura React debe actualizar la spec de componentes React.

## 8. Referencias de migración

Los códigos anteriores pueden aparecer en documentos heredados. Durante la migración se podrán anotar como referencia, pero los documentos nuevos deben usar los IDs `F-001` a `F-040` definidos en el catálogo oficial.

| Referencia anterior | ID nuevo |
|---|---|
| Acceso | `F-001` a `F-005` |
| Catálogo | `F-006` a `F-010` |
| Detalle de producto | `F-011` a `F-015` |
| Carrito | `F-016` a `F-021` |
| Checkout y pago | `F-022` a `F-027` |
| Seguimiento y pedidos | `F-028` a `F-032` |
| Notificaciones | `F-033` a `F-035` |
| Favoritos | `F-036` a `F-039` |
| Evaluación postentrega | `F-040` |
