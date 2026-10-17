# Marketplace — Grupo 1

Repositorio de **especificaciones, arquitectura, diseño visual y planificación** del canal Marketplace de Inka Athletics. El código se desarrolla en repositorios separados: [frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend). Marketplace presenta la experiencia de compra y coordina servicios propietarios de Productos y Ofertas, Seguridad y Gestión de Usuarios, Ventas y Postventa y Despacho; no lee directamente las bases de datos de otros módulos.

> **Estado documental al 13 de octubre de 2026:** los mockups están elaborados y aprobados según el PO, pero eso no equivale a software implementado. El plan de desarrollo de semanas 8–16 tiene responsables y estimación base decididos por el PO; cada tarea se cierra únicamente con código, pruebas y evidencia. La integración real con Productos para la semana 8 depende de que ese módulo publique entorno, datos y autorización utilizables.

## Por dónde empezar

1. [Plan de implementación](plan/PLAN-IMPLEMENTACION.md): hitos de semanas 8, 11, 14 y 16, alcance y criterios de evidencia.
2. [Matriz de bloques y responsables punta a punta](SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) y [paquetes individuales](plan/repartición%20por%20integrantes/README.md) para H3–H6. Leer también la [guía de colaboración](plan/repartición%20por%20integrantes/GUIA-DE-TRABAJO-COLABORATIVO.md) antes de abrir ramas o PR.
3. [Decisiones y bloqueos](plan/DECISIONES-Y-BLOQUEOS.md): dependencias intermodulares y técnicas pendientes; no asumir que una API o un despliegue está listo porque exista un documento.
4. [Nomenclatura SDD](SPECS/NOMENCLATURA-SDD.md) y [fuentes](SPECS/INVENTARIO-FUENTES.md): cómo identificar specs y rastrear su origen.
5. Para una funcionalidad, leer en orden su spec [funcional](SPECS/funcional/), [UI](SPECS/ui/), [contrato API](SPECS/contrato-api/) y [componentes React](SPECS/componentes-react/); después su archivo en [plan/funcionalidades](plan/funcionalidades/) y sus tareas en [plan/seguimiento](plan/seguimiento/).

La documentación en [specs históricas](SPECS/specs-depreciadas/) y las épicas/historias originales es **antecedente**, no sustituto de las specs vigentes F-001–F-040. Ante una contradicción, registrar la decisión y actualizar la fuente vigente antes de implementar.

## Equipo

Los roles generales se conservan. La [matriz de implementación](SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) fija un responsable y revisor por F-001–F-040 a lo largo de S1–S5; cada integrante debe tocar interfaz y backend propio en un corte vertical. Jim, como PO, decidió la asignación y la estimación base sin exigir aceptación individual previa. La interpretación académica de ocho bloques para siete personas se consultará al profesor sin detener el trabajo. El [reparto de diseño visual](SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md) sigue siendo distinto del ownership del código.

| Integrante | Rol general |
|---|---|
| Diego Steven Martin Espinoza Picon | Jefe de Proyecto / QA |
| Leonidas Garcia Lescano | Arquitecto de Software / Backend |
| Giuliano Macchiavello Perez | UX/UI / Frontend |
| Sebastian Matias Malca Agüero | Documentación / Frontend |
| Andres Fernando Morales Usca | DevOps / Seguridad |
| Fernando Jose Saire Tello | QA / Cloud |
| Jim Bryan Segovia Valencia | Product Owner |

## Organización vigente

```text
SPECS/
├── funcional/             comportamiento, reglas y estados por F-###
├── ui/                    sistema de diseño, vistas V-###, overlays O-### y correos C-###
├── contrato-api/          datos y operaciones del BFF e integraciones
├── componentes-react/     composición y estados para implementación React
├── specs-depreciadas/     ocho SPEC históricos; sólo antecedente
├── NOMENCLATURA-SDD.md
└── INVENTARIO-FUENTES.md
plan/
├── PLAN-IMPLEMENTACION.md
├── iteraciones/           S1–S5, alineadas a hitos
├── funcionalidades/       planes F-001–F-040
├── seguimiento/           tareas, estados y evidencias
└── repartición por integrantes/   paquetes y reglas de H3
Arquitectura de la Aplicación/      diagramas y modelo lógico de base de datos
Diagrama de Procesos/              procesos de negocio
Especificación de Requisitos/       fuentes históricas y trazabilidad
Wireframes y Prototipo/             antecedentes visuales
```

El [modelo lógico vigente](Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/01-Modelo-logico-inicial.md) guía la persistencia propia. La arquitectura o el esquema históricos de dos tablas no reemplazan ese modelo. **Plan y tareas no son specs**: por eso viven fuera de `SPECS/`.

## Primer corte funcional: H3, semana 8

La [iteración S1](plan/iteraciones/S01-semanas-07-08.md) y los [siete paquetes individuales](plan/repartición%20por%20integrantes/README.md) priorizan **F-006** (inicio/categorías) y **F-007** (búsqueda por texto), con un flujo visible `navegador → frontend Marketplace → BFF Marketplace → API real de Productos`. Las pantallas previstas son [V-005 Inicio](SPECS/ui/vistas/V-005-inicio.md) y el alcance de búsqueda de [V-006 Catálogo y resultados](SPECS/ui/vistas/V-006-catalogo-resultados.md), incluidos carga, resultados, vacío y error. Desktop y responsive se validan según sus specs; las funciones de filtros, ordenamiento y paginación completos pertenecen a iteraciones posteriores.

La API de Productos **alimenta** estas vistas: conectarse con otro módulo no crea por sí mismo una pantalla nueva. El frontend no debe llamar a Productos con secretos ni copiar su catálogo a la base Marketplace. Un fixture local puede ayudar al desarrollo, pero **no acredita** la integración ni el despliegue requeridos por H3.

## Diseño, arquitectura y tecnología

- [Modelo C4](Arquitectura%20de%20la%20Aplicación/Modelo%20C4.md): diagramas de contexto, contenedores y componentes de frontend/backend. [Arquitectura de la Aplicación](Arquitectura%20de%20la%20Aplicación/Arquitectura.md): vista por capas, stack, despliegue, persistencia, CI y responsabilidades; ambos documentos actualizados al corte H3 de `develop`.
- [Sistema de diseño DS-001](SPECS/ui/DS-001-sistema-diseno-marketplace.md) y [catálogo visual](SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md): fuente de composición, identidad y estados. Los [mockups de Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) están separados de la biblioteca de sistema de diseño.
- [Arquitectura React](SPECS/componentes-react/ARQUITECTURA-REACT.md): diseño técnico de frontend, no prueba de que el código ya exista.
- [Arquitectura y base de datos](Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/): PostgreSQL/Prisma y el despliegue previsto se contrastan con el backend real antes de migrar o publicar.
- **Corte de código del 17/10/2026:** el frontend `develop` usa Next.js 16, React 19 y TypeScript; el backend `develop` usa NestJS 11 y Prisma. Consultar la [arquitectura actualizada](Arquitectura%20de%20la%20Aplicación/Arquitectura.md) para rutas, persistencia, estado del despliegue y límites de las integraciones. Las propuestas de bibliotecas contenidas en documentos históricos no acreditan su uso en el código.

## Cómo contribuir

Trabajamos con especificaciones antes de código, contratos versionados y pruebas proporcionales al cambio. Para el código de H3 en frontend/backend, las ramas personales salen de `develop` **cuando el equipo la cree**, los PR se abren hacia `develop` y el corte verificado pasa a `main`. En este repositorio SPECS, la documentación revisada se publica con commit/push directo a `main`, según indicación del PO del 13/10/2026. La [guía colaborativa](plan/repartición%20por%20integrantes/GUIA-DE-TRABAJO-COLABORATIVO.md) define revisores, criterios de cierre y Conventional Commits con descripción en español. Cada autor documenta qué specs/mockups usó, qué código generó o modificó con IA, qué revisó personalmente y qué pruebas ejecutó. No subir secretos, datos personales ni afirmar «integrado» por pruebas con mocks.
