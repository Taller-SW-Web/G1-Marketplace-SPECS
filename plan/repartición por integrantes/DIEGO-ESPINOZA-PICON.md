# Diego Steven Martin Espinoza Picon — Jefe de Proyecto / QA — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **5. Favoritos; F-040 adicional**; IDs: **F-036–F-040 (F-040 fuera de los ocho bloques literales)**. Revisor principal: **Fernando Saire**. Hitos: S02/H4 F-036–F-039; implementación propia H4 y cierre S05 F-040. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Trabajo asignado para S02 y Hito 4

El PO confirma **disponibilidad sin restricción horaria**. Todas las funciones del paquete reciben implementación/pruebas G1 H4 donde las reglas/contratos estén definidos; los cierres completos conservan gates externos. [S02](../iteraciones/S02-semanas-09-11.md) y [alcance](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

- **F-036:** Implementar alta favorita idempotente por usuario G7, elegibilidad G6, BD propia y negativos de titular; token técnico nunca identifica al comprador. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-037:** Implementar lista por titular con enriquecimiento G6, precio/elegibilidad/vacío/error y aislamiento A/B; no copiar catálogo ajeno a BD G1. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-038:** Implementar DELETE del titular y Deshacer mediante F-036 con elegibilidad actual G6, producto inactivo y fallo de restauración explícitos; resolver G-UNDO antes del cierre. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-039:** Implementar favorito→carrito con selección SKU, precio/cantidad G6, identidad G7 y handoff con Andres; destino confirmado antes de quitar origen y pruebas de replay/fallo sin pérdida. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-040:** Implementar prompt/formulario CSAT y adaptador conforme G5, reglas/payload/casos con fixture de pedido entregado; aislar transiciones durables aún sin contrato SHOWN/DISMISSED. Cierre S05 exige I-04/G-PROMPT resueltos. Cierre objetivo: S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4.

**Transversal:** QA-002 integración por F revisada por Fernando y DOC-002 seguimiento de gates por Jim. Coordinar desbloqueos/evidencia sin reducir funciones por disponibilidad horaria. IDs TASK-TRANS-S02- en [TRANSVERSALES](../seguimiento/TRANSVERSALES.md).

**Evidencia:** diseño/contrato/frame revisado; commit FE+BE/fixture y pruebas positivo-negativo; integración REAL con proveedor/auth/traza; despliegue con URLs/SHAs/run. Registrar cada nivel sin inferencias. Ante frontera sin acuerdo, implementar la parte propia definida, registrar owner/bloqueo y continuar otras operaciones. No cerrar INT por doble, contrato escrito o tiempo disponible.

## Fuentes y alcance

- Specs funcionales de entrada: [F-036](../../SPECS/funcional/F-036-agregar-favorito.md), [F-037](../../SPECS/funcional/F-037-visualizar-favoritos.md), [F-038](../../SPECS/funcional/F-038-quitar-favorito.md), [F-039](../../SPECS/funcional/F-039-mover-favorito-carrito.md), [F-040](../../SPECS/funcional/F-040-evaluacion-postentrega.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-009, O-003/O-006/O-009; controles de V-005–V-007. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: G-AUTH, I-01, I-04 (F-040), G-UNDO, G-PROMPT y contrato de Postventa; F-039 depende del carrito de Andres.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-036](../seguimiento/F-036-agregar-favorito.md), [F-038](../seguimiento/F-038-quitar-favorito.md). El corte de H3 se vincula con `TASK-F036-FE-001`, `TASK-F036-BE-001` y `TASK-F036-QA-001`, `TASK-F038-FE-001`, `TASK-F038-BE-001` y `TASK-F038-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Como JP, seguir contratos/entornos/evidencia, coordinar PR/revisión y ejecutar QA cruzada de H3–H6. No autoaprobar sus tareas. Revisa checkout de Leonidas.

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

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos contractuales/técnicos o hallazgos de calidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si un gate externo impide integrar, registrar por operación owner, prueba faltante y continuidad del trabajo propio; no reducir el alcance por disponibilidad horaria.
