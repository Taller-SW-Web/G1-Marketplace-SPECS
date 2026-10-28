# Alcance de Productos y Seguridad para H4

Versión 0.7.0 · 19/10/2026, Lima. [S02](iteraciones/S02-semanas-09-11.md) organiza la ejecución; este inventario clasifica las 40 F y conserva sus dueños. Las cifras son objetivos de cierre condicionados a contrato, entorno, autorización y prueba, no integraciones ya logradas.

## 1. Cobertura y escenarios

**23 F necesitan datos comerciales actuales de G6:** F-006–F-017, F-019–F-021, F-023–F-026, F-031, F-036–F-037 y F-039. Se añaden **F-018/F-038 como dependencias indirectas o condicionales**: su DELETE es local, pero Deshacer vuelve a usar altas y elegibilidad. El universo dependiente de Productos es de **25 F**, sin atribuir 25 llamadas externas.

De ellas, **20** forman el circuito catálogo/ficha/carrito/favoritos (F-006–F-021 y F-036–F-039). Las otras **5** son checkout F-023–F-026 y recompra F-031, con dependencias adicionales. §3 clasifica las otras 15 F.

| Alcance H4 | Productos del circuito | Del universo de 25 dependientes de G6 | Cuenta/Seguridad | F distintas con objetivo de cierre |
|---|---:|---:|---:|---:|
| Principal: F-001–F-021 y F-036–F-039 | 20/20 | 20/25 | 5/5 | 25 |
| Tramo comercial adicional F-023–F-026 y F-031 | 0 adicionales al circuito | 5/25 adicionales con implementación/pruebas G1 y G6 donde el provider esté disponible | — | Hasta 5 adicionales, 30 F total; S03/S05 base hasta aceptación |

**Decisión vigente del PO, 19/10/2026:** todos tienen disponibilidad sin restricción horaria para esta planificación. Se retiran cupos de horas, techos por dedicación, ampliaciones por tiempo y recortes por dedicación. Las **25 F principales** son objetivo de H4; las demás 15 también reciben implementación/pruebas de su parte propia G1 y adaptadores conforme contratos definidos. No se inventan endpoints/campos/reglas para completar código cuando la frontera sigue sin acuerdo.

Se adelantan al cierre H4 **F-017/F-018** desde S03 y **F-004/F-005/F-015/F-020/F-021/F-039** desde S05. Las anteriores ampliaciones de registro, precio/SKU/stock, carrito y favoritos pasan al principal. Esta decisión retira la limitación interna de tiempo; no acredita disponibilidad de otros grupos, integración ni despliegue.

El principal integra las 20 F del circuito comercial con G6 y las 5 de cuenta con G7. Si una operación no tiene contrato/configuración/runtime/prueba, su código G1 avanza con doble rotulado y su INT continúa bloqueada; al corte se informa por F nivel real y pendiente externo. No se considera cumplido el número 25 por contar pantallas o mocks.

**Extensión por contratos, sin condición de tiempo:** F-023/F-024/F-025/F-026 y F-031 pueden cerrar anticipadamente en H4 si también se liberan y prueban todas sus dependencias de Ventas/Despacho/Seguridad, además de G6. Son **5 F adicionales**, hasta **25/25 dependientes de Productos + 5 cuenta = 30 F distintas**. Su cierre base sigue S03 (cuatro) o S05 (recompra) hasta aceptación; después se descuenta de esa iteración y mantiene regresión. No se bloquea un cierre probado sólo para reservarlo a otro hito; H5/H6 conservan sus requisitos de ingeniería/calidad.

## 2. Todas las funciones dependientes de Productos

Las 20 F del circuito son principales H4; F-023–F-026/F-031 reciben implementación/pruebas propias H4 y conservan cierre integral base posterior; pueden anticiparlo sólo al probar las dependencias adicionales. Cada ID exige aceptación individual y evidencia desplegada para declararse completo.

| F y dueño | Necesidad de G6 | Entrega verificable H4 | Gate o dependencia adicional | Cierre base |
|---|---|---|---|---|
| F-006 · Giuliano | Categorías y productos elegibles, destacados | Integrar inicio/categorías/productos elegibles con G6 REAL y traza web→BFF→G6. Resolver campos de tarjetas y curaduría; destacados omitidos no acreditan su criterio de cierre. | I-01/G-FEATURED; acordar slug/imagen de categoría y curaduría. Omitir destacados no cierra esa parte | H4; condicionado a gates/prueba REAL |
| F-007 · Giuliano | Búsqueda comercial por texto/canal | Integrar búsqueda REAL por texto/canal con producto vendible, vacío/error/timeout, parámetros y evidencia desde la web desplegada. | Dataset vendible y grant técnico G7 | H4; condicionado a gates/prueba REAL |
| F-008 · Giuliano | Filtros soportados por catálogo | Integrar filtros soportados y homologados con G6; probar combinación/reset de página/vacío/error. No activar filtros sin semántica contractual. | Homologar parámetros; controles no soportados no se activan | H4; condicionado a gates/prueba REAL |
| F-009 · Giuliano | Orden publicado | Integrar orden NAME_ASC/DESC→NOMBRE_ASC/DESC y estabilidad entre páginas; otros criterios permanecen en G-SORT hasta homologación. | G-SORT; precio/relevancia/novedad requieren otro acuerdo | H4; condicionado a gates/prueba REAL |
| F-010 · Giuliano | Página/tamaño/total | Integrar paginación page 0→pagina 1, tamaño/total/límites/última página y cambios de consulta con G6. | No mezclar páginas de consultas | H4; condicionado a gates/prueba REAL |
| F-011 · Sebastian | Detalle por slug, galería, marca/atributos | Integrar detalle por slug, galería/marca/atributos, simple y variantes; probar producto ausente/no elegible, errores y navegación tarjeta→ficha sin completar DTO con datos inventados. | DTO BFF mapeado sin campos inventados | H4; condicionado a gates/prueba REAL |
| F-012 · Sebastian | Precio por SKU/canal, oferta publicada | Integrar precio/oferta por SKU/canal con importe, moneda, vigencia y errores autoritativos G6; no calcular descuentos ni presentar oferta no publicada. | Pricing real; G-MONEY cuando afecte ficha. No recomputar descuentos ni dar oferta por cerrada sin semántica | H4; condicionado a gates/prueba REAL |
| F-013 · Sebastian | sku_base o variant_id/sku elegible | Integrar SKU simple sku_base y variantes elegibles variant_id/sku; validar selección inválida y handoff F-016, sin convertir productId en SKU. | G-SKU; productId ≠ variantId ≠ SKU; mapear status del BFF | H4; condicionado a gates/prueba REAL |
| F-014 · Sebastian | Disponibilidad comercial | Resolver G-G6-COMPAT y luego integrar/probar disponibilidad comercial G6: estados acordados incluido INDETERMINADO, fuente realizable y errores; no sumar ubicaciones ni inferir N unidades. | G-G6-COMPAT/G-QUANTITY: cuatro estados y fuente realizable; no sumar ubicaciones | H4; condicionado a gates/prueba REAL |
| F-015 · Sebastian | Candidatos y enriquecimiento comercial | Implementar e integrar recomendaciones G6, enriquecimiento, máximo 8 tarjetas, dedupe/sin origen y degradación; cerrar sólo con request, grant y runtime autorizados y probados. | Ruta/request, enriquecimiento, recomendaciones:leer y runtime para G1 por comprobar | H4; condicionado a gates/prueba REAL |
| F-016 · Andres | SKU elegible, precio, cantidad N | Implementar alta FE+BE por SKU elegible con precio/cantidad G6, BD propia, cookie invitado o titular G7; probar duplicado/rechazo/carrera y resolver G-ADD/G-DB/G-QUANTITY. | I-01/G-SKU/G-ADD/G-QUANTITY/G-DB; G7 para autenticado, cookie propia para invitado | H4; condicionado a gates/prueba REAL |
| F-017 · Andres | Revalidar N al cambiar cantidad | Implementar cambio de cantidad absoluta, versión/concurrencia, insuficiencia y reconciliación; verificar N con G6, sin deducirlo del estado comercial. | G-QUANTITY y BD limpia; DISPONIBLE no garantiza N | H4; condicionado a gates/prueba REAL |
| F-018 · Andres | DELETE local; Deshacer reutiliza alta | Implementar DELETE idempotente y Deshacer acordado con versión/concurrencia/revalidación; DELETE aislado no libera G-UNDO ni cierra toda la función. | G-UNDO; DELETE aislado no cierra toda la F si falta Deshacer | H4; condicionado a gates/prueba REAL |
| F-019 · Andres | Precio/elegibilidad actual y snapshot | Implementar carrito vacío/con líneas, snapshot, precio/elegibilidad G6, totales autorizados y errores/titularidad. Total de carrito no es total final de pedido. | I-01/G-MONEY/G-DB; total carrito no es total final pedido | H4; condicionado a gates/prueba REAL |
| F-020 · Andres | Revalidar líneas en fusión | Implementar fusión invitado→login con G7 y revalidación G6, transacción/dedupe/replay/carreras y fallo sin pérdida. Login no acredita por sí solo fusión. | G7/F-002, transacción/dedupe G1, G-QUANTITY | H4; condicionado a gates/prueba REAL |
| F-021 · Andres | Elegibilidad carrito→favoritos | Implementar carrito→favoritos con G7/G6 y contrato Andres–Diego: confirmar destino antes de quitar origen, dedupe/compensación y prueba de fallos. | G7/F-036, handoff con Diego, atomicidad/compensación propia | H4; condicionado a gates/prueba REAL |
| F-023 · Leonidas | Precio/beneficios y perfil de líneas | Implementar resumen FE+BE, adaptadores/precio/beneficios G6 y pruebas positivas/negativas; usar envío/total de prueba si G2/G5 siguen bloqueados. Cierre integral S03 exige snapshot autoritativo conjunto. | También Despacho I-06 y total final Ventas G-MONEY | S03 integral; implementación H4 |
| F-024 · Leonidas | Evaluar promoción/validar cupón | Implementar cupón/promoción FE+BE, evaluación/validación G6 y errores/timeout; consumo/restauración sólo por G5/G6 y contrato G-BENEFIT/G-MONEY/G-COUPON-RELEASE. Cierre completo S03. | G-BENEFIT/G-MONEY, grants G7, consumo/restauración G5/G6 y G-COUPON-RELEASE | S03 integral; implementación H4 |
| F-025 · Leonidas | SKU/cantidad/vigencias al preparar | Implementar preparación/consentimiento UI+BFF y adaptadores/casos de cantidad/fulfillment/vigencias conforme contrato; fixtures rotulados donde falte proveedor. PREPARED no es pedido ni pago; cierre S03. | Ventas/Despacho, fulfillment, G-CHECKOUT/G-PAID/G-QUANTITY | S03 integral; implementación H4 |
| F-026 · Leonidas | Transportar snapshot comercial | Implementar orquestación G1, payload/clave/fingerprint, persistencia permitida y recuperación idempotente; probar con dobles y con G5 al habilitarse. G5 crea/reserva/inicia simulador; cierre S03. | I-02/G-MONEY/G-CHECKOUT; G5 crea/reserva e inicia simulador | S03 integral; implementación H4 |
| F-031 · Fernando | SKU/precio/stock actuales desde compra anterior | Implementar recompra G1, dedupe/ajustes/transacción carrito, autorización del pedido y revalidación SKU/precio/cantidad G6; fixtures donde falte G5. Resolver I-03/G-REORDER antes del cierre S05. | Ventas I-03, titularidad, carrito G1 y G-REORDER | S05 integral; implementación H4 |
| F-036 · Diego | Elegibilidad para guardar | Implementar alta favorita idempotente por usuario G7, elegibilidad G6, BD propia y negativos de titular; token técnico nunca identifica al comprador. | G7/I-01/BD propia; token técnico no identifica persona | H4; condicionado a gates/prueba REAL |
| F-037 · Diego | Enriquecimiento actual de favoritos | Implementar lista por titular con enriquecimiento G6, precio/elegibilidad/vacío/error y aislamiento A/B; no copiar catálogo ajeno a BD G1. | G7/I-01; no copiar catálogo ajeno | H4; condicionado a gates/prueba REAL |
| F-038 · Diego | DELETE local; Deshacer reutiliza F-036 | Implementar DELETE del titular y Deshacer mediante F-036 con elegibilidad actual G6, producto inactivo y fallo de restauración explícitos; resolver G-UNDO antes del cierre. | G-UNDO/G-AUTH; producto inactivo no se restaura como disponible | H4; condicionado a gates/prueba REAL |
| F-039 · Diego | SKU/precio/cantidad favorito→carrito | Implementar favorito→carrito con selección SKU, precio/cantidad G6, identidad G7 y handoff con Andres; destino confirmado antes de quitar origen y pruebas de replay/fallo sin pérdida. | F-016/F-013, handoff con Andres, G7/G-QUANTITY | H4; condicionado a gates/prueba REAL |

## 3. Las otras 15 funciones

| F y dueño | Relación con Productos y avance H4 | Cierre base |
|---|---|---|
| F-001–F-003 · Jim | Sin G6; implementar/integrar registro, verificación/retorno, login/MFA efectivo, refresh/logout y protección UI/API G7 | H4 |
| F-004/F-005 · Jim | Sin G6; implementar UI/BFF y recuperación/restablecimiento G7, enlace/correo/expiración/usado y antienumeración. Si falta provider, conservar INT bloqueada | H4, adelantadas desde S05 |
| F-022 · Leonidas | Dirección del titular G7 y cotización G2; sin llamada G6 propia. Implementación UI/BFF/adaptador y pruebas locales; integración real donde exista entorno | S03 |
| F-027 · Leonidas | Snapshot G5; implementar estados incierto/CREADO/PAGADO y recuperación con contrato/dobles. No refrescar compra con precios actuales | S03 |
| F-028–F-030 · Fernando | Histórico G5; implementar F-028/F-030 FE+BFF y F-029 UI/lógica G1 con dobles o G5 autorizado. Aislar brecha del filtro fecha en /me sin inventar interfaz | S03 F-028/F-030; S05 F-029 |
| F-032 · Fernando | Pedido autorizado G5 y seguimiento G2; implementar vista/BFF/adaptador con contrato/dobles, preparar y probar I-06 | S04 |
| F-033/F-034 · Fernando | Snapshot G5; implementar plantillas server-only, payload/outbox/retry/dedupe G1 conforme contrato. Disparo sólo PAGADO; dobles explícitos no prueban entrega real | S03 |
| F-035 · Fernando | Evento G5/G2 y snapshot; implementar lógica/consumidor/C-002 donde haya contrato; probar auth/retry/dedupe con dobles y acordar frontera del emisor | S04 |
| F-040 · Diego | CSAT/pedido entregado G5; implementar prompt/formulario/adaptador y pruebas conforme G5; aislar persistencia SHOWN/DISMISSED no publicada | S05 |

Son 6 F sin dependencia comercial G6 (cuenta y dirección) y 9 con datos derivados de pedido/entrega. Un snapshot histórico en correo o seguimiento no crea una nueva integración de precios actuales con G6 ni autoriza modificar importes de la compra.

## 4. Evidencia de partida y factibilidad

Revisión de archivos locales y metadata de PR el 19/10. SHAs identifican fuentes, no despliegues. Esta planificación no ejecutó suites de aplicaciones ni probó servicios ajenos.

| Fuente | Hallazgo y consecuencia |
|---|---|
| G1 SPECS main 4e703ac; FE ec1acfb; BE c7e8e8e | El [corte H3](CORTE-H3-Y-TRASPASO-H4.md) es antecedente. ProductDetailService retorna fixtures; AuthService.login devuelve MOCK/authenticated=false. Hay AuthGuard RS256/JWKS y código carrito/favoritos; reutilizarlo y verificar cobertura por F, sin certificar auth o nube |
| [OpenAPI G6 0.6.0-rc.1](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/contratos/http/openapi.yaml), [respuesta G1](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/c36bd9a18f4fdb188df0d7e5158a431cf4b4ea7b/integraciones/ACUERDOS_G1_MARKETPLACE_2026-10-13.md) | Candidato, no homologación bilateral/runtime. Cantidad/snapshot/grants condicionados. F-014 G1 admite tres estados y agregación; G6 exige INDETERMINADO y fuente realizable: resolver G-G6-COMPAT |
| [G6 backend master 9205eb4](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-backend/tree/9205eb4) | Hay controladores comerciales de catálogo y lecturas de Pricing. InventorySvcController y PromotionsSvcController examinados sólo exponen health; no se acredita su operación comercial. Pedir revisión/entorno implementado antes de declararla REAL |
| [G7 contrato v1.1.0 y v2 parcial](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/tree/bf97a2b/specs/contrato-api), [kit](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/blob/bf97a2b/specs/kit-integracion.md) | Login/JWKS/registro/refresh/logout/recuperación documentados. Confirmar MFA efectivo, entorno y grants propios G1; los de Chatbot no se heredan |
| [G7 backend main d51ac2e](https://github.com/Taller-SW-Web/Modulo-de-Seguridad-Backend/tree/d51ac2e) | Se observaron controladores login, refresh, logout, OTP y descubrimiento. No se encontró controlador HTTP registro/recuperación en el inventario revisado: F-001/F-004/F-005 necesitan confirmar implementación y entorno con G7 |
| FE [#16](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/16)/[#9](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/9), BE [#23](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/23)/[#17](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/17) | Las cuatro siguen abiertas/sin fusionar al consultar metadata. No se suman a main. Sus resultados declarados no se reejecutaron; comprobar checks, G-DB y continuidad cookie/SKU antes del demo |
| Workflows FE/BE de esos SHAs | Existen build/tests y CI H3. Algunos FE sólo disparan en ramas personales; backend-ci no provee PostgreSQL real. Conectar validación de PR/develop/main, BD desechable y deploy del corte aprobado; YAML no demuestra ejecución/CD |

G6 frontend master dd1e11c y G7 frontend main a7e9947 son referencias auxiliares de interfaz, no prueba de API/adaptador G1 ni despliegue. No se libera ningún gate por esta actualización.

## 5. Disponibilidad y secuencia por dependencias

El PO dispone planificación **sin restricción horaria**. La estimación histórica de esfuerzo puede describir complejidad; no se usa como cupo ni motivo para posponer una función. Las pruebas, revisión y correcciones son trabajo obligatorio. Se conserva la secuencia por dependencia, aunque todos pueden desarrollar en paralelo sus partes independientes.

| Integrante | Objetivo principal de cierre H4 | Trabajo adicional H4 y coordinación |
|---|---|---|
| Jim | F-001–F-005: 5 | Registro/verificación, login/MFA/refresh/logout y recuperación; integración G7 y tres correcciones visuales Checkout |
| Giuliano | F-006–F-010: 5 | Catálogo REAL y mapeos/query/filtros/orden/página; apoyo a tarjetas relacionadas |
| Sebastian | F-011–F-015: 5 | Detalle/SKU/precio/disponibilidad/recomendaciones G6; ejemplos/schema/consumer tests API-002 |
| Andres | F-016–F-021: 6 | Carrito completo, fusión y movimiento; G-DB/guard/CI-CD con colaboración Fernando/Leonidas/Jim |
| Diego | F-036–F-039: 4 | Favoritos completos/movimiento; implementar parte propia de F-040, QA y seguimiento de gates |
| Leonidas | 0 cierres integrales por defecto; 6 F propias implementadas/probadas en su parte G1 | F-022–F-027, adaptadores G6/G5/G2, contratos/casos bloqueados aislados; API-001 e identidad técnica INT-001 |
| Fernando | 0 cierres integrales por defecto; 8 F propias implementadas/probadas en su parte G1 | F-028–F-035, historial/detalle/filtros/recompra/seguimiento/plantillas/worker donde el contrato lo permita; cloud/CI-deploy/E2E |

Semana 9: cerrar contratos/semántica/configuración y datos, reparar instalación limpia y tener CI/API/guard base. Semana 10: integrar todos los tramos G6/G7 disponibles y desarrollar/probar las partes independientes de las 40 F. Semana 11: corregir/retestar, ejecutar build/compile/test/deploy, demo REAL y evidencia individual. Una ruta bloqueada no detiene otras operaciones.

Andres conserva responsabilidad de pipeline/guard; Fernando colabora implementando pasos build/deploy/runtime, Leonidas valida contratos/API y Jim implementa sesión/consumo del guard. Los owners no cambian. Si un revisor aportó al artefacto, Diego designa segunda revisión independiente.

Por cada bloqueo, registrar owner externo, operación, contrato o configuración faltante y prueba que lo libera. G6/G7 deben confirmar su propia capacidad publicada; la disponibilidad de G1 no la sustituye. Sólo un bloqueo técnico/contractual/calidad justifica mantener una F principal parcial; no una cuota de horas. H5/H6 conservan ingeniería, integración/performance/evento, seguridad, regresión y observabilidad.

## 6. Cuatro niveles de avance y aceptación

| Nivel | Evidencia mínima | Afirmación permitida |
|---|---|---|
| Diseñado | Spec/contrato/flujo o frame versionado, estados/revisión y discrepancias | Diseño revisado del alcance |
| Implementado con datos de prueba | Commit FE/BE, fixture declarado, positivo/negativo, comando/resultado | Código probado con dobles |
| Integrado con otro módulo | Versiones G1/provider, entorno autorizado, request/response REAL, auth/error y traza | Operación intermodular probada en ese entorno |
| Probado en el despliegue | URLs/SHAs FE/BE/provider, run build/test/deploy, caso desde web y negativos, revisión | Alcance demostrado en nube |

Estos niveles no reemplazan estados del tablero ni se infieren entre sí. Cada TASK conserva su estado hasta su DoD. F completa exige todos sus criterios: si falta Deshacer/filtro/oferta/estado obligatorio, registrar Parcial aunque funcione el DELETE o la vista básica. Los tableros F registran evidencia por nivel; no se marca Terminado al planificar.

## 7. Dependencias y decisiones abiertas

| Owner de respuesta; coordinación G1 | Frontera y objetivo | Evidencia de desbloqueo |
|---|---|---|
| G6/G7; Leonidas/Jim | URL/versiones, modulo-marketplace, aud api-productos y grants; semana 9 | Token real por entorno y 200/401/403 por ruta. Catálogo/precio/inventario primero; otros scopes sólo al consumirlos |
| G6; Giuliano/Sebastian | Tarjetas/filtros/orden/slug/SKU/precio; semana 9 | Mapeo y dataset simple/variantes, positivo/vacío, contrato consumidor-provider |
| G6/G2/G5; Sebastian/Andres/Leonidas | F-014, cantidad, fulfillment y snapshot; decisión semana 9/prueba antes de semana 11 | G-G6-COMPAT resuelto, endpoint N ejecutable binding=false, fuente realizable; sin saldos ni fulfillment_ref inventado |
| G7; Jim/Andres | Registro/login/MFA/issuer/JWKS/transporte/refresh/logout; semanas 9–10 | Entorno y usuarios A/B; UI+API con expiración/logout/401/403; antienumeración y sin tokens propios |
| G1; Andres/Leonidas | G-DB/G-ADD/G-UNDO y cookie/SKU; semanas 9–10 | BD desechable desde cero, carreras/restauración aprobadas. Auditar historial/esquema Render por separado |
| G5/G2/G6; Leonidas y Fernando | I-02/I-03/I-05/I-06, G-MONEY/G-COUPON-RELEASE; hasta semana 11 | Snapshot/estados/idempotencia/titular/envío/evento/auth/retry/dedupe publicados y prueba acotada, preparando S03/H5 |
| G1/G7; Jim/Diego | Seguimiento de contratos/entornos/datos/gates; semanal | Owner de bloqueo, decisión técnica/contractual y prueba por F; cierre sólo tras DoD |

Registrar liberaciones en [decisiones](DECISIONES-Y-BLOQUEOS.md) y resultados en [seguimiento](seguimiento/README.md). Este reparto asigna trabajo G1; no atribuye aceptación ni impone entregas a otros equipos.
