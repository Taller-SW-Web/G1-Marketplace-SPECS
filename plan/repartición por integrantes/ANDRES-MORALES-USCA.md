# Andres Fernando Morales Usca — DevOps / Seguridad — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **4. Carrito de compras**; IDs: **F-016–F-021**. Revisor principal: **Leonidas Garcia**. Hitos: S02/H4 F-016–F-021. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Trabajo asignado para S02 y Hito 4

El PO confirma **disponibilidad sin restricción horaria**. Todas las funciones del paquete reciben implementación/pruebas G1 H4 donde las reglas/contratos estén definidos; los cierres completos conservan gates externos. [S02](../iteraciones/S02-semanas-09-11.md) y [alcance](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

- **F-016:** Implementar alta FE+BE por SKU elegible con precio/cantidad G6, BD propia, cookie invitado o titular G7; probar duplicado/rechazo/carrera y resolver G-ADD/G-DB/G-QUANTITY. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-017:** Implementar cambio de cantidad absoluta, versión/concurrencia, insuficiencia y reconciliación; verificar N con G6, sin deducirlo del estado comercial. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-018:** Implementar DELETE idempotente y Deshacer acordado con versión/concurrencia/revalidación; DELETE aislado no libera G-UNDO ni cierra toda la función. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-019:** Implementar carrito vacío/con líneas, snapshot, precio/elegibilidad G6, totales autorizados y errores/titularidad. Total de carrito no es total final de pedido. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-020:** Implementar fusión invitado→login con G7 y revalidación G6, transacción/dedupe/replay/carreras y fallo sin pérdida. Login no acredita por sí solo fusión. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-021:** Implementar carrito→favoritos con G7/G6 y contrato Andres–Diego: confirmar destino antes de quitar origen, dedupe/compensación y prueba de fallos. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.

**Transversal:** G-DB, OPS-001/002 CI-CD y SEC-001 guard, revisados por Leonidas. Fernando colabora implementando build/deploy/runtime; Jim sesión y Leonidas contratos. Cada F de carrito incluye sus pruebas y evidencia propias. IDs TASK-TRANS-S02- en [TRANSVERSALES](../seguimiento/TRANSVERSALES.md).

**Evidencia:** diseño/contrato/frame revisado; commit FE+BE/fixture y pruebas positivo-negativo; integración REAL con proveedor/auth/traza; despliegue con URLs/SHAs/run. Registrar cada nivel sin inferencias. Ante frontera sin acuerdo, implementar la parte propia definida, registrar owner/bloqueo y continuar otras operaciones. No cerrar INT por doble, contrato escrito o tiempo disponible.

## Fuentes y alcance

- Specs funcionales de entrada: [F-016](../../SPECS/funcional/F-016-agregar-item-carrito.md), [F-017](../../SPECS/funcional/F-017-cambiar-cantidad-item-carrito.md), [F-018](../../SPECS/funcional/F-018-quitar-item-carrito.md), [F-019](../../SPECS/funcional/F-019-visualizar-carrito.md), [F-020](../../SPECS/funcional/F-020-fusionar-carrito-anonimo.md), [F-021](../../SPECS/funcional/F-021-mover-carrito-favoritos.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-008, O-005–O-007; V-007/V-001 como puntos de entrada. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: I-01 Productos, G-AUTH, G-SKU, G-ADD, G-UNDO, G-DB; interfaz F-039 con Diego. No forzar migración destructiva.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-016](../seguimiento/F-016-agregar-item-carrito.md), [F-019](../seguimiento/F-019-visualizar-carrito.md). El corte de H3 se vincula con `TASK-F016-FE-001`, `TASK-F016-BE-001` y `TASK-F016-QA-001`, `TASK-F019-FE-001`, `TASK-F019-BE-001` y `TASK-F019-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Mantener además base FE/BE, CI/deploy, secretos, CORS y health seguro de H3; estos son roles transversales, no sustituyen su corte carrito. Revisar seguridad de cuenta de Jim.

## Incremento vertical individual de H3 / semana 8

F-016/F-019: control de agregar un ítem y V-008 con endpoint BFF y persistencia propia en sandbox aislado; caso agregado y rechazo por producto no elegible. MOCK hasta validar stock/identidad reales.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Leonidas Garcia, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar estado del carrito V-008 y O-005–O-007 según specs; mostrar totales sólo desde snapshot autorizado, sin incremento supuesto. F-020 usa identidad de Jim y F-021 coordina con Diego.
- **Backend Marketplace:** Implementar rutas, ownership de carrito y persistencia Marketplace conforme al modelo lógico; transacciones/idempotencia según contrato, sin almacenar catálogo o stock ajeno. G-UNDO requiere acuerdo antes de prometer restauración.
- **Pruebas:** Alta/duplicado, cambio/quitar, carrera, sesión ajena, stock insuficiente, timeout y rollback; DB en entorno temporal y negativos de seguridad; MOCK/REAL diferenciados.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Giuliano usa el DTO público; Diego recibe contrato de mover favorito al carrito; Leonidas recibe snapshot de checkout.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos contractuales/técnicos o hallazgos de calidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si un gate externo impide integrar, registrar por operación owner, prueba faltante y continuidad del trabajo propio; no reducir el alcance por disponibilidad horaria.
