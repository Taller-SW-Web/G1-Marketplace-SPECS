# Giuliano Macchiavello Perez — UX/UI / Frontend — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **2. Búsqueda y navegación**; IDs: **F-006–F-010**. Revisor principal: **Sebastian Malca**. Hitos: S1: F-006/007; S2: F-008–010. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Fuentes y alcance

- Documentación transversal del corte: [catálogo de elementos compartidos](../../SPECS/ui/sistema-diseno/ELEMENTOS-COMPARTIDOS.md) y [changelog](../../SPECS/ui/sistema-diseno/CHANGELOG-COMPARTIDOS.md). Guías de imports/props y utilidades en `docs/ELEMENTOS-COMPARTIDOS.md` de Frontend y Backend. Estado en revisión; no sustituye DS-001 ni acredita biblioteca completa.

- Specs funcionales de entrada: [F-006](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [F-007](../../SPECS/funcional/F-007-buscar-productos-texto.md), [F-008](../../SPECS/funcional/F-008-filtrar-catalogo.md), [F-009](../../SPECS/funcional/F-009-ordenar-catalogo.md), [F-010](../../SPECS/funcional/F-010-paginar-catalogo.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-005/V-006, O-001, DS-001. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: I-01 Productos, G-FEATURED, G-SORT, G-STACK, G-SHELL y G-CLOUD-H3. Si faltan URL/token/datos, integración H3 bloqueada aunque la UI con fixture pase.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-006](../seguimiento/F-006-inicio-categorias-destacados.md), [F-007](../seguimiento/F-007-buscar-productos-texto.md). El corte de H3 se vincula con `TASK-F006-FE-001`, `TASK-F006-BE-001` y `TASK-F006-QA-001`, `TASK-F007-FE-001`, `TASK-F007-BE-001` y `TASK-F007-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Custodia DS-001/shell y revisa UI de Sebastian. Andres opera despliegue; Diego prueba gate; Jim acepta. Leonidas revisa BE/contrato.

## Incremento vertical individual de H3 / semana 8

F-006/F-007: buscador de V-005 y resultados mínimos V-006 conectados a ruta BFF Marketplace propia. Carga, resultados, vacío y error; query válida/inválida; prueba con fixture MOCK y luego Productos REAL autorizado.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Sebastian Malca, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar V-005, el corte de búsqueda de V-006, control tipado y estados responsive/accesibles. Filtros, orden y paginación completos se completan en S2. Mantener DS-001 y coordinación con diseñador de vistas, sin confundir diseño con implementación.
- **Backend Marketplace:** Implementar o coimplementar como autor responsable rutas BFF de categorías/búsqueda, validación y proyección comercial, con timeout y error seguro; Leonidas hace revisión técnica del adaptador. Secretos y JWT técnico sólo en servidor; no copiar catálogo a BD.
- **Pruebas:** Búsqueda válida/inválida, vacío, 401/403/429/5xx y timeout; caso con datos de Productos en nube para H3. Registrar SHA del contrato, URLs y respuesta sanitizada.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Sebastian recibe DTO y tarjeta compartida; Andres recibe configuración sin secretos y prueba de health.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos o desvíos de capacidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si la carga o el gate impiden el objetivo del hito, proponer resecuenciación documentada antes del corte.
