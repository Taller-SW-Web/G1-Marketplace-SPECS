# Sebastian Matias Malca Agüero — Documentación / Frontend — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **3. Detalle de producto**; IDs: **F-011–F-015**. Revisor principal: **Giuliano Macchiavello**. Hitos: S02/H4 F-011–F-015. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Trabajo asignado para S02 y Hito 4

El PO confirma **disponibilidad sin restricción horaria**. Todas las funciones del paquete reciben implementación/pruebas G1 H4 donde las reglas/contratos estén definidos; los cierres completos conservan gates externos. [S02](../iteraciones/S02-semanas-09-11.md) y [alcance](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

- **F-011:** Integrar detalle por slug, galería/marca/atributos, simple y variantes; probar producto ausente/no elegible, errores y navegación tarjeta→ficha sin completar DTO con datos inventados. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-012:** Integrar precio/oferta por SKU/canal con importe, moneda, vigencia y errores autoritativos G6; no calcular descuentos ni presentar oferta no publicada. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-013:** Integrar SKU simple sku_base y variantes elegibles variant_id/sku; validar selección inválida y handoff F-016, sin convertir productId en SKU. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-014:** Resolver G-G6-COMPAT y luego integrar/probar disponibilidad comercial G6: estados acordados incluido INDETERMINADO, fuente realizable y errores; no sumar ubicaciones ni inferir N unidades. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-015:** Implementar e integrar recomendaciones G6, enriquecimiento, máximo 8 tarjetas, dedupe/sin origen y degradación; cerrar sólo con request, grant y runtime autorizados y probados. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.

**Transversal:** API-002 ejemplos/schema/consumer tests revisados por Leonidas y DOC-001 por Jim; resolver G-G6-COMPAT con las fuentes G1/G6 antes de activar F-014. IDs TASK-TRANS-S02- en [TRANSVERSALES](../seguimiento/TRANSVERSALES.md).

**Evidencia:** diseño/contrato/frame revisado; commit FE+BE/fixture y pruebas positivo-negativo; integración REAL con proveedor/auth/traza; despliegue con URLs/SHAs/run. Registrar cada nivel sin inferencias. Ante frontera sin acuerdo, implementar la parte propia definida, registrar owner/bloqueo y continuar otras operaciones. No cerrar INT por doble, contrato escrito o tiempo disponible.

## Fuentes y alcance

- Specs funcionales de entrada: [F-011](../../SPECS/funcional/F-011-detalle-producto.md), [F-012](../../SPECS/funcional/F-012-precio-oferta-descuento.md), [F-013](../../SPECS/funcional/F-013-seleccion-atributos-variante.md), [F-014](../../SPECS/funcional/F-014-consultar-disponibilidad-stock.md), [F-015](../../SPECS/funcional/F-015-productos-relacionados.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-007, O-002, DS-001. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: I-01 Productos, G-SKU, G-QUANTITY; F-006/007 para entrada navegable; revisión de contrato por Leonidas.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-011](../seguimiento/F-011-detalle-producto.md). El corte de H3 se vincula con `TASK-F011-FE-001`, `TASK-F011-BE-001` y `TASK-F011-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Conservar trazabilidad documental specs→código→pruebas de su bloque y ayudar a recopilar enlaces de otros sin atribuirse su evidencia individual. Revisa PR de catálogo de Giuliano.

## Incremento vertical individual de H3 / semana 8

F-011: abrir V-007 desde una tarjeta de V-006; mostrar nombre/imagen/descripción o estado ausente/error mediante proyección BFF propia sobre fixture. Prueba de producto válido y no encontrado; MOCK salvo proveedor probado.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Giuliano Macchiavello, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar V-007 y O-002 con estados de ficha, precio/variante/stock sólo cuando el contrato los entregue; integrar botones de carrito/favoritos a través de APIs de Andres/Diego, sin adquirir ownership de esas mutaciones.
- **Backend Marketplace:** Implementar BFF de detalle/proyección y validar identificadores/respuestas comerciales de Productos; no usar productId como SKU ni inferir cantidad desde DISPONIBLE. Related F-015 sólo con fuente aprobada.
- **Pruebas:** Detalle válido/404/error/timeout, variante sin SKU aprobado y producto no elegible; pruebas responsive/a11y y contrato local/REAL diferenciados.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Andres recibe SKU/identificador autorizado para carrito; Diego recibe elegibilidad de favorito.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos contractuales/técnicos o hallazgos de calidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si un gate externo impide integrar, registrar por operación owner, prueba faltante y continuidad del trabajo propio; no reducir el alcance por disponibilidad horaria.
