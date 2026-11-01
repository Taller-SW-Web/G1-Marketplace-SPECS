# Fernando Jose Saire Tello — QA / Cloud — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **7. Notificaciones y 8. Consulta/seguimiento de pedidos**; IDs: **F-028–F-035**. Revisor principal: **Jim Segovia**. Hitos: Implementación propia H4 de F-028–F-035; cierres S03/S04/S05. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Trabajo asignado para S02 y Hito 4

El PO confirma **disponibilidad sin restricción horaria**. Todas las funciones del paquete reciben implementación/pruebas G1 H4 donde las reglas/contratos estén definidos; los cierres completos conservan gates externos. [S02](../iteraciones/S02-semanas-09-11.md) y [alcance](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

- **F-028:** Implementar historial FE+BFF con fixture o Ventas autorizado, paginación/vacío/error y usuarios A/B; integrar G5 donde esté habilitado. Cierre integral S03 con titularidad y despliegue. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-029:** Implementar filtros/estado UI y lógica G1 con dobles; aislar el adaptador de la brecha de fechas de /me G5. No inventar endpoint ni declarar filtro REAL sin contrato; cierre S05. Cierre objetivo: S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4.
- **F-030:** Implementar detalle FE+BFF de pedido propio y estados/errores, con pruebas de ajeno y acceso neutral; usar snapshot G5, sin refrescar importes históricos con G6. Cierre S03. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-031:** Implementar recompra G1, dedupe/ajustes/transacción carrito, autorización del pedido y revalidación SKU/precio/cantidad G6; fixtures donde falte G5. Resolver I-03/G-REORDER antes del cierre S05. Cierre objetivo: S05/H6, semanas 15–16; implementación propia y pruebas con dobles en H4.
- **F-032:** Implementar vista/BFF/adaptador de seguimiento conforme G2/G5, estados/errores y pruebas con dobles/entorno autorizado. Consulta titular y trazas reales cierran S04/H5. Cierre objetivo: S04/H5, semana 14; implementación y preparación de integración en H4.
- **F-033:** Implementar plantillas accesibles server-only C-001/C-002 y render/pruebas con snapshot autorizado o fixture; no usar precios actuales G6 ni enviar correo fingido. Fuente/payload/motor G-MAIL condicionan cierre S03. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-034:** Implementar orquestación/outbox/worker G1 donde el contrato esté definido, cifrado/dedupe/retry/timeout y pruebas en sandbox propio. Disparo sólo PAGADO verificado; proveedor/entrega real condicionan cierre S03. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-035:** Implementar consumidor/lógica/plantilla de actualización donde exista contrato de evento G5/G2; probar auth/dedupe/retry con fixtures explícitos. No inventar emisor/transporte/esquema; intercambio real cierra S04/H5. Cierre objetivo: S04/H5, semana 14; implementación y preparación de integración en H4.

**Transversal:** OPS-003 cloud/rollback revisado por Andres y QA-001 E2E revisado por Jim; colaborar build/deploy pipeline. Implementar historial/detalle/filtros/recompra y plantillas/worker/consumidor en la frontera definida por los contratos. IDs TASK-TRANS-S02- en [TRANSVERSALES](../seguimiento/TRANSVERSALES.md).

**Evidencia:** diseño/contrato/frame revisado; commit FE+BE/fixture y pruebas positivo-negativo; integración REAL con proveedor/auth/traza; despliegue con URLs/SHAs/run. Registrar cada nivel sin inferencias. Ante frontera sin acuerdo, implementar la parte propia definida, registrar owner/bloqueo y continuar otras operaciones. No cerrar INT por doble, contrato escrito o tiempo disponible.

## Fuentes y alcance

- Specs funcionales de entrada: [F-028](../../SPECS/funcional/F-028-historial-pedidos.md), [F-029](../../SPECS/funcional/F-029-filtrar-historial-pedidos.md), [F-030](../../SPECS/funcional/F-030-detalle-pedido.md), [F-031](../../SPECS/funcional/F-031-reordenar-compra.md), [F-032](../../SPECS/funcional/F-032-seguimiento-despacho.md), [F-033](../../SPECS/funcional/F-033-generar-plantilla-correo.md), [F-034](../../SPECS/funcional/F-034-enviar-confirmacion-asincrona.md), [F-035](../../SPECS/funcional/F-035-enviar-actualizacion-despacho.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-015–V-017, O-008, C-001/C-002; V-014 recibe confirmación. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: I-02/I-03/I-05/I-06, G-ASYNC-H5, G-MAIL, G-REORDER y proveedor de correo/evento publicados; F-040 de Diego consume elegibilidad postentrega.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-028](../seguimiento/F-028-historial-pedidos.md). El corte de H3 se vincula con `TASK-F028-FE-001`, `TASK-F028-BE-001` y `TASK-F028-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Como QA/cloud ejecuta smoke de H3 y revisa favoritos de Diego; Jim valida contenido del correo, Leonidas revisa contrato/evento. Ambos bloques se implementan/prueban en su alcance G1 durante H4 y cierran integración S03–S04 según contrato; mantener apoyo y revisión independiente.

## Incremento vertical individual de H3 / semana 8

F-028: V-015 con lista vacía/con pedidos desde BFF propio sobre fixture sin PII; prueba de titular correcto y acceso ajeno. MOCK hasta Ventas/autorización reales. Notificación se prepara después; no prometer envío en H3.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Jim Segovia, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar V-015–V-017 y O-008; diseñar/renderizar C-001/C-002 en servidor y mostrar estados de confirmación/seguimiento autorizados. F-029/F-031 se cierran en S5.
- **Backend Marketplace:** Implementar adaptadores BFF a Ventas/Despacho para historial, detalle y tracking; enviar correos server-only según proveedor aprobado y outbox/evento intermodular real para F-034/035. No leer BD ajena ni mandar correo desde navegador.
- **Pruebas:** Titular/ajeno, vacío, filtros/reorder duplicado, estado despacho tardío, entrega duplicada de evento, reintento y plantilla sin PII; MOCK y REAL diferenciados, traza de dos módulos para H5.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Diego recibe elegibilidad de F-040; Jim valida contenido y criterio de aceptación de correo.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos contractuales/técnicos o hallazgos de calidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si un gate externo impide integrar, registrar por operación owner, prueba faltante y continuidad del trabajo propio; no reducir el alcance por disponibilidad horaria.
