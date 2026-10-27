# Leonidas Garcia Lescano — Arquitecto de Software / Backend — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **6. Checkout y generación del pedido**; IDs: **F-022–F-027**. Revisor principal: **Diego Espinoza**. Hitos: Implementación propia H4 de F-022–F-027; cierre integral S03. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Trabajo asignado para S02 y Hito 4

El PO confirma **disponibilidad sin restricción horaria**. Todas las funciones del paquete reciben implementación/pruebas G1 H4 donde las reglas/contratos estén definidos; los cierres completos conservan gates externos. [S02](../iteraciones/S02-semanas-09-11.md) y [alcance](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

- **F-022:** Implementar UI+BFF/adaptador de dirección del titular, estados y pruebas con contrato/fixture explícito; integrar G7/G2 donde exista entorno. Cierre completo S03 con logística y titularidad probadas. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-023:** Implementar resumen FE+BE, adaptadores/precio/beneficios G6 y pruebas positivas/negativas; usar envío/total de prueba si G2/G5 siguen bloqueados. Cierre integral S03 exige snapshot autoritativo conjunto. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-024:** Implementar cupón/promoción FE+BE, evaluación/validación G6 y errores/timeout; consumo/restauración sólo por G5/G6 y contrato G-BENEFIT/G-MONEY/G-COUPON-RELEASE. Cierre completo S03. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-025:** Implementar preparación/consentimiento UI+BFF y adaptadores/casos de cantidad/fulfillment/vigencias conforme contrato; fixtures rotulados donde falte proveedor. PREPARED no es pedido ni pago; cierre S03. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-026:** Implementar orquestación G1, payload/clave/fingerprint, persistencia permitida y recuperación idempotente; probar con dobles y con G5 al habilitarse. G5 crea/reserva/inicia simulador; cierre S03. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.
- **F-027:** Implementar estados UI+BFF incierto/CREADO/PAGADO/ANULADO y recuperación conforme contrato; integrar los frames corregidos por Jim/revisados por Fernando. Cierre S03 exige PAGADO verificado G5. Cierre objetivo: S03, semanas 12–13; implementación y pruebas propias comienzan en H4.

**Transversal:** API-001 diseño OpenAPI e INT-001 identidad técnica G6 revisados por Jim; revisión DB/pipeline/guard. Implementar todas las partes G1 definidas y conectar tramos G6 disponibles, aislando la frontera G5/G2 pendiente. IDs TASK-TRANS-S02- en [TRANSVERSALES](../seguimiento/TRANSVERSALES.md).

**Evidencia:** diseño/contrato/frame revisado; commit FE+BE/fixture y pruebas positivo-negativo; integración REAL con proveedor/auth/traza; despliegue con URLs/SHAs/run. Registrar cada nivel sin inferencias. Ante frontera sin acuerdo, implementar la parte propia definida, registrar owner/bloqueo y continuar otras operaciones. No cerrar INT por doble, contrato escrito o tiempo disponible.

## Fuentes y alcance

- Specs funcionales de entrada: [F-022](../../SPECS/funcional/F-022-seleccionar-direccion-envio.md), [F-023](../../SPECS/funcional/F-023-calcular-resumen-envio.md), [F-024](../../SPECS/funcional/F-024-validar-aplicar-cupon-promocion.md), [F-025](../../SPECS/funcional/F-025-simular-pago-revalidar-stock.md), [F-026](../../SPECS/funcional/F-026-crear-orden-ventas.md), [F-027](../../SPECS/funcional/F-027-confirmacion-orden.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-010–V-014, O-004/O-010. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: I-01/I-02/I-06, G-ADDRESS, G-BENEFIT, G-MONEY, G-QUANTITY, G-CHECKOUT, G-PAID, G-CONFIRM y G-COUPON-RELEASE.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-023](../seguimiento/F-023-calcular-resumen-envio.md). El corte de H3 se vincula con `TASK-F023-FE-001`, `TASK-F023-BE-001` y `TASK-F023-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Como arquitecto revisa adaptadores de otros bloques y el contrato de evento de Fernando; no absorbe la implementación FE+BE de ellos. Revisa carrito de Andres y BE de catálogo/detalle.

## Incremento vertical individual de H3 / semana 8

F-023: resumen V-011 con snapshot de prueba y ruta BFF que valida entradas e informa monto recibido; positivo y monto/cotización inválidos. MOCK, sin simular pago ni crear pedido.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Diego Espinoza, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar V-010–V-014 y O-004 con estados de dirección, resumen, simulación, resultado incierto y confirmación sólo tras PAGADO verificado; UI protegida y responsive.
- **Backend Marketplace:** Implementar orquestación BFF de quote, beneficio, preparación, orden idempotente y consulta de estado; Marketplace sólo guarda CheckoutOperation/datos propios permitidos. No emitir pago/orden por una lectura de fixture.
- **Pruebas:** Dirección inválida, cupón rechazado, stock cambiante, doble clic, timeout, expiración, PREPARED/CREADO no pagado, PAGADO/ANULADO y recuperación; contrato real con Ventas/Productos/Despacho.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Fernando recibe orderId/estado autorizado, sin exponer CheckoutOperation como pedido final.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos contractuales/técnicos o hallazgos de calidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si un gate externo impide integrar, registrar por operación owner, prueba faltante y continuidad del trabajo propio; no reducir el alcance por disponibilidad horaria.
