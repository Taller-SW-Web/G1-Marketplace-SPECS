# Inventario de fuentes para la migración SDD

Este inventario identifica la documentación existente que se utilizará como fuente para redactar las nuevas especificaciones del módulo Marketplace.

## Regla de uso

- Toda la documentación existente del repositorio se considera una fuente de consulta.
- Los documentos actuales no se moverán ni eliminarán durante la primera etapa.
- La información será consolidada progresivamente en las carpetas `SPECS/funcional`, `SPECS/ui`, `SPECS/contrato-api` y `SPECS/componentes-react`.
- Cuando existan contradicciones, la nueva spec no debe asumir una respuesta: debe registrar el punto como decisión pendiente.
- Las nuevas specs serán la fuente de verdad una vez aprobadas; los documentos anteriores quedarán como antecedente y referencia de migración.

## 1. Contexto y visión general

| Fuente | Aporte principal |
|---|---|
| `README.md` | Visión del Canal Marketplace, integrantes, alcance, catálogo de documentos y tecnologías previstas. |
| `SPECS/README.md` | Catálogo de documentación técnica existente, relaciones entre funcionalidades y lineamientos SDD previos. |
| `NOMENCLATURA-SDD.md` | Convenciones oficiales para las nuevas specs, planes y tareas. |

## 2. Fuentes funcionales

| Ubicación | Aporte principal |
|---|---|
| `Especificación de Requisitos/Reglas de Negocio/` | Reglas generales y reglas aplicables a cada funcionalidad. |
| `Especificación de Requisitos/Requisitos No Funcionales.md` | Seguridad, rendimiento, accesibilidad y otras restricciones de calidad. |
| `Especificación de Requisitos/Matriz de Integración y Límites de Dominio.md` | Límites de responsabilidad del Marketplace e integraciones requeridas. |
| `Especificación de Requisitos/Trazabilidad Completa de Especificación de Requisitos.md` | Relación entre capacidades, validaciones, dependencias y responsables históricos. |
| `Especificación de Requisitos/Épicas/` | Descripciones y comportamiento detallado existente de acceso, catálogo, detalle de producto, carrito, checkout, seguimiento, notificaciones y favoritos. |
| `SPECS/specs-depreciadas/SPEC-01-EP-GAC-Gestion-de-Accesos.md` a `SPECS/specs-depreciadas/SPEC-08-EP-FAV-Gestion-de-Favoritos.md` | Especificaciones técnicas históricas; sirven como fuente de comportamiento, reglas, casos y criterios, pero no son la fuente de verdad vigente. |

## 3. Fuentes de interfaz y experiencia de usuario

| Ubicación | Aporte principal |
|---|---|
| `Wireframes y Prototipo/Especificación de pantallas del canal.md` | Pantallas, navegación, contenidos y comportamiento de interfaz. |
| `Wireframes y Prototipo/Diagrama de Navegación.md` | Rutas, relaciones entre pantallas y recorridos de usuario. |
| `Especificación de Requisitos/Épicas/` | Detalles de interacción, mensajes y validaciones incluidos en documentos existentes. |
| `SPECS/specs-depreciadas/SPEC-01-EP-GAC-Gestion-de-Accesos.md` a `SPECS/specs-depreciadas/SPEC-08-EP-FAV-Gestion-de-Favoritos.md` | Diseño técnico de frontend existente, componentes y estados de interfaz de referencia histórica. |

## 4. Fuentes para contratos API e integraciones

| Ubicación | Aporte principal |
|---|---|
| `Arquitectura de la Aplicación/Contratos de Mocks API.md` | Endpoints, payloads, mocks y acuerdos de integración existentes. |
| `Especificación de Requisitos/Matriz de Integración y Límites de Dominio.md` | Servicios externos que debe consumir el Marketplace y límites entre módulos. |
| `SPECS/specs-depreciadas/SPEC-01-EP-GAC-Gestion-de-Accesos.md` a `SPECS/specs-depreciadas/SPEC-08-EP-FAV-Gestion-de-Favoritos.md` | Contratos, DTOs, validaciones y flujos de integración previamente descritos. |
| `Arquitectura de la Aplicación/Plan de Acción para la Transición de Mocks a APIs Reales.md` | Estrategia para sustituir mocks por servicios integrados. |

## 5. Fuentes de arquitectura y componentes React

| Ubicación | Aporte principal |
|---|---|
| `Arquitectura de la Aplicación/Arquitectura.md` | Capas, servicios, decisiones técnicas e integración general. |
| `Arquitectura de la Aplicación/Modelo C4.md` | Contexto, contenedores y componentes de la solución. |
| `Arquitectura de la Aplicación/Esquema de Prisma (Preliminar).md` | Persistencia local y modelos de datos previstos. |
| `SPECS/specs-depreciadas/SPEC-01-EP-GAC-Gestion-de-Accesos.md` a `SPECS/specs-depreciadas/SPEC-08-EP-FAV-Gestion-de-Favoritos.md` | Componentes React, hooks, estado, endpoints y persistencia descritos de forma preliminar. |

## 6. Fuentes de procesos y calidad

| Ubicación | Aporte principal |
|---|---|
| `Diagrama de Procesos/Diagramas de Procesos Preliminares.md` | Flujos de negocio y procesos transversales. |
| `Especificación de Requisitos/Épicas/Definition of Done.md` | Criterios de calidad y verificación existentes. |
| `Arquitectura de la Aplicación/Plan de Acción para la Transición de Mocks a APIs Reales.md` | Criterios de transición, integración y validación. |

## 7. Estado de migración

| Área destino | Estado | Fuente principal |
|---|---|---|
| `SPECS/funcional/` | Pendiente de migración | Requisitos, reglas, documentos funcionales y SPECS existentes |
| `SPECS/ui/` | Pendiente de migración | Wireframes, navegación y diseño frontend existente |
| `SPECS/contrato-api/` | Pendiente de migración | Contratos de mocks, integración y SPECS existentes |
| `SPECS/componentes-react/` | Pendiente de migración | Diseño frontend y arquitectura existente |

## 8. Siguiente paso

Revisar y clasificar el contenido de estas fuentes para detectar información repetida, contradicciones, vacíos y documentos desactualizados antes de redactar las nuevas specs.
