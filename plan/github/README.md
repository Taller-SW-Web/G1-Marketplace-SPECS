# Projects de Marketplace y trazabilidad de tareas

Corte inicial 19/10/2026 · Plan 0.7.0. Se publica una issue por TASK sin duplicar entre repositorios. Las 293 tareas conservan responsables, revisores, estados de origen y criterios de cierre del plan.

## Tableros

| Repositorio | Project | Inventario |
|---|---|---|
| Frontend | [Marketplace Frontend S02 H4](https://github.com/orgs/Taller-SW-Web/projects/3) | [88 tareas](lista-frontend.md) |
| Backend | [Marketplace Backend S02 H4](https://github.com/orgs/Taller-SW-Web/projects/4) | [205 tareas](lista-backend.md) |

Frontend contiene FE, QA funcional/E2E y correcciones visuales. Backend contiene BE, BD, integración, QA de seguridad, documentación y coordinación transversal. Cada responsable conserva la entrega FE+BE de su bloque; el reparto por repositorio organiza artefactos y no cambia ownership. Las dependencias enlazan issues de ambos repositorios.

## Alcance y evidencia

| Clasificación | Tareas | Sentido |
|---|---:|---|
| H4 cierre objetivo | 160 | Trabajo de las 25 F principales: F-001–F-021 y F-036–F-039 |
| H4 avance y cierre posterior | 96 | Trabajo G1 de las otras 15 F; cierre integral según contratos y plan |
| H4 transversal | 21 | 15 tareas S02 y 6 arrastres o tareas S01 por revisar |
| Posterior a H4 | 16 | Continuidad transversal S03–S05 |

Total: 256 tareas funcionales y 37 transversales. No son 293 funcionalidades. La disponibilidad no limita el alcance. Las ampliaciones F-023–F-026 y F-031 sólo se anticipan con contratos y pruebas; mantienen su clasificación de origen hasta aceptación registrada.

Las vistas de ejecución separan Pendiente, En progreso, En revisión, Bloqueado y Terminado. Estado, Alcance y Revisor se cargan por tarea; responsable, prioridad y clasificación se heredan de la issue. Semana, función y cierre base están en el cuerpo de cada issue. Los cuatro campos Diseño, Datos de prueba, Integración y Despliegue se actualizan al aportar evidencia: vacío equivale a Por verificar, y no niega diseño o código existentes. Algunas filas tienen Por verificar explícito por la carga inicial; ambos registros tienen el mismo sentido. Cada issue conserva además las cuatro casillas de evidencia separadas. No se cierran gates al publicar.

Cada issue incluye trabajo, DoD, responsable, revisor, prioridad, semana, dependencias, nivel de evidencia y fuente. Para cambiar un estado: registrar commit/entorno/caso/resultado y revisión independiente, actualizar la issue y reconciliar la fila del seguimiento. El inventario enlazado conserva el estado de origen y no es un segundo tablero vivo.

## Asignaciones técnicas H4

| Entrega | Responsable | Colaboración o revisión |
|---|---|---|
| CI/CD OPS-001/002 | Andres | Fernando build/deploy/runtime; Leonidas revisa |
| Cloud y CD OPS-003 | Fernando | Andres revisa |
| OpenAPI API-001 | Leonidas | Jim revisa |
| Ejemplos y consumer tests API-002 | Sebastian | Leonidas revisa; cada owner aporta casos |
| Cuenta UI+BFF AUTH-001 | Jim | Andres revisa |
| Guard y autorización SEC-001 | Andres | Leonidas revisa; cada owner aplica titularidad |
| Token G1→G6 INT-001 | Leonidas | Jim revisa; grants G6/G7 pendientes |
| QA por F QA-002 | Diego | Fernando revisa |
| Demo E2E QA-001 | Fernando | Jim revisa |

## Cuentas y distribución

| Responsable | Cuenta | Frontend | Backend | Total |
|---|---|---:|---:|---:|
| Jim Segovia | @JimSegovia | 13 | 25 | 38 |
| Giuliano Macchiavello | @GiulianoMaPe | 10 | 20 | 30 |
| Sebastian Malca | @SebastianMalca | 10 | 25 | 35 |
| Andres Morales | @andreus710 | 12 | 43 | 55 |
| Diego Espinoza | @DiesmEsp | 13 | 28 | 41 |
| Leonidas Garcia | @LeonidasGarcia | 12 | 29 | 41 |
| Fernando Saire | @saire22 | 18 | 35 | 53 |

Los conteos incluyen toda la continuidad S01–S05 y tareas de complejidad distinta; no son una estimación de esfuerzo. La administración de colaboradores de los Projects fue rechazada por permisos de la cuenta durante la creación. Las asignaciones de issues sí se realizaron; un administrador debe confirmar acceso de lectura/edición del equipo a los Projects privados. No se atribuye un permiso no comprobado.

[Seguimiento](../seguimiento/README.md) · [S02](../iteraciones/S02-semanas-09-11.md) · [Plan maestro](../PLAN-IMPLEMENTACION.md).
