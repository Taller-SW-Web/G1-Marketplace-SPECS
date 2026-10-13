# Decisiones y bloqueos de implementación

Versión 0.3.0 · En revisión · Reparto propuesto 2026-10-13; revisión intermodular previa 2026-10-10. Se contrastaron las ramas remotas de Productos y Ventas con el reporte de consistencia del 05/10; esto no equivale a aprobación ni a prueba de integración.

## Integraciones externas: evidencia pendiente, no solicitudes nuevas

Fuente: [brechas BD/integración](../Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/03-Decisiones-y-brechas-de-integracion.md) y contratos F individuales. Se respeta el acuerdo de verificación de Seguridad registrado en F-001; los estados siguientes no significan que nadie haya respondido, sino que **falta registrar contrato/configuración/prueba suficiente en repo para activar integración**.

| Gate | Funcionalidades | Evidencia que libera | Límite para el plan |
|---|---|---|---|
| I-01 / H-01 | Catálogo F-006–017,019–021,023–026,031,036–037,039 | OpenAPI de Productos por versión, rutas/auth/error y prueba de mapeo. Ordenamiento vigente sólo por nombre; validación de N unidades y semántica de destacados siguen como brechas, no se deducen del estado comercial. | **Semana 7**: mínimo F-006/F-007 para H3; resto antes de F-016 en S2. Fixture local no libera. |
| I-02 / H-02 | F-025–027,034 | Contrato homologado con Ventas: `POST /pedidos` idempotente devuelve `201/CREADO` con reserva, cupón y total; Ventas inicia el simulador y G1 consulta `GET /pedidos/{pedidoId}` hasta `PAGADO` o `ANULADO`. Falta implementar/probar el flujo y precisar `pago.metodoPago` para G1; Marketplace no invoca el webhook de pasarela. | Pruebas y mapeo hasta **semana 11**; integración S3. |
| I-03 / H-03 | F-028–032,040 | Ventas publicó `/pedidos/me` con identidad JWT y detalle propio con `403` para ajenos. Probar autorización, paginación 1→0 y proyección mínima; el filtro de fechas de F-029 aún no existe en `/me`. | F-032 antes de **semana 14**; resto antes de S5. |
| I-04 / H-04 | F-040 | Ventas publicó CSAT 5/3/1, comentario de motivos, titularidad y errores `422 ORDER_NOT_DELIVERED`/`409 CSAT_ALREADY_SUBMITTED`. Probar integración y ciclo local del prompt. | Antes de **semana 15**. |
| I-05 / H-05 | F-035 y origen externo de notificaciones si aplica | Ventas publicó webhook `pedidos.envio.estado_actualizado` v1.0.0 con `orderId` textual. Faltan mecanismo de entrega, autenticación, reintentos, responsable y prueba de deduplicación. | Acordar hasta **semana 11**, preparar S3 y demostrar H5 en **semana 14**. |
| I-06 / H-06 | F-023,025,032 | Cliente técnico por ambiente y scopes cotizaciones:calcular/seguimientos:leer probados; acuerdo Seguridad no basta sin Despacho | Contrato/configuración hasta **semana 11**; pruebas S3–S4. |

Cuando se libere un gate: enlazar evidencia/versiones, fecha, aprobador y prueba; revisar tareas dependientes manualmente. No marcar todos los INT como terminados por recibir una respuesta de chat.

## Brechas técnicas locales detectadas y tratamiento

| Gate | Evidencia / problema | Tratamiento para código (sin endpoint inventado) | Límite para el plan |
|---|---|---|---|
| G-STACK | **Framework frontend resuelto por el PO (2026-10-10): React + TypeScript + Next.js App Router.** El frontend aún requiere inicialización; DS-001 propone Mantine/Tabler, mientras fuentes históricas citan Tailwind/shadcn | Pendiente: aprobar un único UI kit, versiones compatibles y lockfile; no interpretar la decisión de Next.js como aprobación de Mantine ni como aplicación ya desplegada | Semana 7 |
| G-SHELL | Header/footer final aún no aprobado en UI; checkout sólo logo+4 etapas fue preferencia del PO | Diseñar wrappers desacoplados. Validar logo/no salida accidental/progreso y footer antes pixel final; sin rutas legales/ayuda supuestas | Antes del primer layout en S1 |
| G-AUTH | F-002 abrevia token/desafío, no MFA/refresh/transporte completo; políticas y URLs base pendientes | Tipos de desafío, endpoint MFA, transporte seguro/CORS/CSRF, expiración y PASSWORD_CADUCADA según Seguridad. Registro usa canal fijo y regreso /login sin token | Semana 9, antes de auth real |
| G-SKU | F-011 no devuelve SKU; ejemplo variantes sólo hasVariants=true | Extender/documentar proyección autorizada de SKU simple de F-013; frontend nunca usa productId como SKU | Antes de F-016, semana 10 |
| G-ADD | F-016 409 stock retorna ajustado vs CA dice ninguna mutación en fallo | Aclarar estados que confirman ajuste frente rechazo sin mutación; UI sólo acepta snapshot confirmado, nunca incremento supuesto | Antes de F-016, semana 10 |
| G-UNDO | UI exige Deshacer y O-006 reconoce contrato de restauración no aprobado | Carrito: definir operación/restauración concurrencia/stock; F-016 suma y no garantiza restaurar cantidad original. Favoritos: reutilizar F-036 tras DELETE, producto puede no estar activo. Sin resolver no prometer restauración ni marcar F-018/038 completas | Antes de cerrar F-038 en S2 y F-018 en S3 |
| G-ADDRESS | label/phone/mapa maestros no completamente definidos | Usar campos contractuales, token titular y memoria; acordar límites y fuente geo. No añadir mapas/SUNAT/RENIEC por mockup | Antes de F-022, semana 12 |
| G-BENEFIT | Quitar cupón y degradación error no endpoints/política completos | Recotizar F-023 sin cupón; confirmar combinabilidad/formato y validez quote base. Sin monto autoritativo no continuar | Antes de F-024, semana 12 |
| G-COUPON-RELEASE | Ventas confirma el cupón al crear, pero reconoce que liberar el beneficio al anular por pago rechazado carece de contrato con Productos | Ventas y Productos deben publicar responsable, operación idempotente y tratamiento de timeout; G1 no libera el cupón por su cuenta. | Antes de probar rechazo con cupón en S3 |
| G-MONEY | Snapshot final y procedencia de descuentos/cupón/envío sin contrato único | Productos/Ventas/Despacho definen precio/versiones, `evaluation_id` o equivalente, beneficios aplicados, quote de envío, vigencias y owner de congelación. Marketplace transporta y muestra, no recalcula. | Hasta semana 11, antes de S3 |
| G-QUANTITY | Estado comercial por SKU no valida la cantidad solicitada | No inferir N unidades ni máximo disponible desde `DISPONIBLE`/`STOCK_BAJO`; pedir operación comercial `sku` + `quantity` sin saldos internos y mantener reserva final en Ventas. | Hasta semana 11, antes de S3 |
| G-SORT | F-009 pedía precio/relevancia/novedad sin contrato del provider | Habilitar sólo `NAME_ASC/DESC` mapeados a `NOMBRE_ASC/DESC`; el resto necesita regla/product-level y nueva homologación antes de exponerse. | Antes de F-009, semana 9 |
| G-FEATURED | `featuredProducts[]` no tiene owner de selección | Propuesta de curaduría editorial G1 por IDs con datos/elegibilidad de Productos; acordar owner y persistencia o dejar sección vacía. | Semana 7; omitir destacados si sigue abierto |
| G-CHECKOUT | POST preparación/orden usan distinto payload y misma tabla key/fingerprint; reload/TTL no definido | Definir ámbito/fingerprint por fase y clave estable de operación. GEToperation necesita operación conocida. Recuperación segura y mapeo orderId↔operationId; no inventar lookup ni reenvío nuevo en SUBMITTED | Hasta semana 11, antes de S3 |
| G-CONFIRM | V-014 pública por orderId, API GET por operationId; resumen artículos/email faltan | Durante flujo conservar asociación opaca; deep link/reload requiere contrato acordado, detalle F-030 sólo confirma pedido autorizado, no sustituye resultado operación. No cart reconstruido | Antes de F-027, semana 13 |
| G-PAID | G1-P0-01: F-025 `PREPARED` y F-026 `CREADO` se presentaban como pago/compra final | Ventas cerró el protocolo documental: `PREPARED` sólo registra consentimiento; `201/CREADO` acredita reserva/cupón, Ventas activa el simulador y G1 espera `PAGADO` verificado para F-027/V-014. `ANULADO` por `PAGO_NO_COMPLETADO` es fallo. Faltan pruebas y ajuste de frames de error. | Pruebas hasta semana 11, antes de S3 |
| G-REORDER | POST reorder sin clave; unicidad SKU no impide doble aumento | Homologar garantía de dedupe/idempotencia con backend. Timeout relee carrito y nunca retry automático de POST; cerrar V-016-OPEN-03 | Antes de F-031, semana 15 |
| G-PROMPT | CSAT POST existe, leer/elegible/SHOWN/DISMISSED no endpoints en contrato | Diseñar ciclo prompt y políticas ahora no/Escape/superficies V-016/017; ampliar contrato antes persistir transiciones reales. No deducir durable status desde localStorage | Antes de F-040, semana 15 |
| G-MAIL | Proveedor/motor/retención/retry y fuente de payload no cerrados | Email server-only, outbox y cifrado/reconciliación provider timeout, URLs seguras. React renderer opcional, no librería instalada por suposición | Antes de F-034, semana 13 |
| G-DB | El backend remoto ya publica Prisma, migración inicial y `render.yaml`, pero su consistencia con el modelo lógico y ejecución real no se verificó | Auditar esquema/constraints/migración y entorno de prueba; no afirmar que un blueprint o health aislado prueban toda la BD ni borrar datos | S1, semana 7 |
| G-CLOUD-H3 | Frontend remoto sólo README y ninguna URL pública verificada; H3 exige demo en nube | Inicializar FE/BFF, desplegar ambos, configurar secretos/CORS, verificar URL externa y flujo con Productos; conservar evidencia de deploy | H3, semana 8 |
| G-API-MGMT | H5 pide API Management aplicado, no sólo OpenAPI o proxy local | Elegir gateway/producto autorizado; documentar rutas, auth, rate limiting y logs; probar tráfico y política efectiva | Diseño hasta semana 11; evidencia H5 semana 14 |
| G-ASYNC-H5 | No hay evento intermodular F-035 acordado ni broker/consumer probado | Acordar proveedor/esquema/transporte, implementar productor/consumidor, retry/dedupe y traza; no contar outbox interno como intercambio entre microservicios | Contrato semana 11; evidencia H5 semana 14 |
| G-OBS-H6 | No hay telemetría/alertas de release verificadas | Logs/métricas/trazas con correlación, umbral y alerta disparada/revisada, sin PII | H6, semana 16 |
| G-CAPACITY | S2 contiene 15 funciones, S3 doce y S5 nueve más regresión; capacidad humana aún sin estimar | [Matriz propuesta](../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md): cada owner estima horas FE/BE/INT/QA y revisión, confirma disponibilidad; Diego/Jim redistribuyen apoyo o resecuencian por decisión, sin marcar trabajo como ejecutado | Antes de aceptar cada iteración |
| G-OWNERSHIP | Ocho bloques del sílabo y siete integrantes; falta confirmar interpretación del profesor y aceptación/capacidad individual | Jim valida si Fernando puede llevar seguimiento y notificaciones relacionados y si seis cortes H3 MOCK parciales cuentan como evidencia individual sin cerrar hito; registrar respuesta, estimaciones, revisores y cambio de matriz/paquetes si procede | Antes de aprobar el reparto/H3 |

La autoría de diseño visual permanece separada. La [matriz de implementación](../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) propone responsables/revisores para F-001–F-040; cada uno debe aceptar capacidad y alcance antes de iniciar. G-OWNERSHIP registra la validación académica pendiente.

## Registro de cierre (a completar con evidencia real)

| Gate | Decisión/evidencia versionada | Prueba | Fecha/semana | Validado por | Estado |
|---|---|---|---|---|---|
| Ninguno liberado por esta entrega | Elaborar documentación no cierra contratos | — | — | — | Pendiente |

Registrar cada cierre en una fila; no borrar la explicación original del riesgo. Pruebas con fixtures = prueba local, no aceptación del proveedor.
