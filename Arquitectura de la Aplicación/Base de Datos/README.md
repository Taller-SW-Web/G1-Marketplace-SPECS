# Base de Datos e Integraciones del Marketplace

Esta carpeta contiene la base arquitectónica de la Fase 2.6 del proceso SDD. No reemplaza las specs por funcionalidad ni el esquema Prisma preliminar: define qué datos pertenecen a Marketplace, qué datos son externos y qué debe validarse antes de traducir el modelo al esquema físico.

## Documentos

| Documento | Propósito |
| --- | --- |
| [01-Modelo-logico-inicial.md](01-Modelo-logico-inicial.md) | Modelo lógico inicial de los datos propios del canal Marketplace. |
| [02-Matriz-de-integracion-y-contratos.md](02-Matriz-de-integracion-y-contratos.md) | Matriz de ownership, identificadores y contratos entre Marketplace y otros módulos. |
| [03-Decisiones-y-brechas-de-integracion.md](03-Decisiones-y-brechas-de-integracion.md) | Decisiones que refinan el modelo y acuerdos que aún requieren homologación externa. |

## Alcance y estado

- **Base lógica:** aprobada para guiar las specs de Fase 3.
- **Modelo físico:** pendiente por funcionalidad; se implementará en PostgreSQL 16 con Prisma sólo después de aprobar la spec funcional, UI y contrato API correspondientes.
- **Regla de aislamiento:** Marketplace no realiza consultas SQL ni establece claves foráneas hacia bases de datos de Seguridad, Productos y Ofertas, Ventas y Postventa o Despacho.
- **Fecha de consolidación:** 27 de septiembre de 2026.

Los documentos se basan en la revisión de los repositorios de Seguridad, Productos y Ofertas, Ventas y Postventa, y Despacho. Toda ruta señalada como `TBD`, provisional o pendiente debe confirmarse con su módulo dueño antes de usarse en una spec de contrato API.
