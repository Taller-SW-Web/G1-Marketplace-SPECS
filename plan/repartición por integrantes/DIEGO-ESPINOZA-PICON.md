# Diego Steven Martin Espinoza Picon — Jefe de Proyecto / QA — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **5. Favoritos; F-040 adicional**; IDs: **F-036–F-040 (F-040 fuera de los ocho bloques literales)**. Revisor principal: **Fernando Saire**. Hitos: S2: F-036–038; S5: F-039/040. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Fuentes y alcance

- Specs funcionales de entrada: [F-036](../../SPECS/funcional/F-036-agregar-favorito.md), [F-037](../../SPECS/funcional/F-037-visualizar-favoritos.md), [F-038](../../SPECS/funcional/F-038-quitar-favorito.md), [F-039](../../SPECS/funcional/F-039-mover-favorito-carrito.md), [F-040](../../SPECS/funcional/F-040-evaluacion-postentrega.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-009, O-003/O-006/O-009; controles de V-005–V-007. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: G-AUTH, I-01, I-04 (F-040), G-UNDO, G-PROMPT y contrato de Postventa; F-039 depende del carrito de Andres.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-036](../seguimiento/F-036-agregar-favorito.md), [F-038](../seguimiento/F-038-quitar-favorito.md). El corte de H3 se vincula con `TASK-F036-FE-001`, `TASK-F036-BE-001` y `TASK-F036-QA-001`, `TASK-F038-FE-001`, `TASK-F038-BE-001` y `TASK-F038-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Como JP, medir capacidad, coordinar PR/revisión y ejecutar QA cruzada de H3–H6. No autoaprobar sus tareas. Revisa checkout de Leonidas.

## Incremento vertical individual de H3 / semana 8

F-036/F-038: control de favorito y BFF/persistencia WishlistItem de Marketplace en sandbox; caso agregar/quitar y rechazo sin sesión. MOCK hasta auth/elegibilidad real.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Fernando Saire, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar V-009 y controles de favoritos de V-005/V-006/V-007; F-039 entrega al carrito de Andres. En S5 implementar O-009 evaluación postentrega, sólo tras elegibilidad autorizada.
- **Backend Marketplace:** Implementar rutas y ownership por cliente de favoritos, deduplicación y persistencia Marketplace; F-040 usa adaptador a Postventa/CSAT aprobado y no deduce estado durable de localStorage.
- **Pruebas:** Alta repetida, quitar, otra sesión, producto inactivo, transferencia al carrito, evaluación elegible/no elegible y retry; pruebas de UI/BE y evidencia separada MOCK/REAL.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Andres recibe contrato de transferencia; Fernando recibe enlace a evaluación desde detalle/seguimiento.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos o desvíos de capacidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si la carga o el gate impiden el objetivo del hito, proponer resecuenciación documentada antes del corte.
