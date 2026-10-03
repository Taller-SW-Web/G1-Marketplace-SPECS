# Tareas transversales — Base, BD, DevSecOps, QA y coordinación

Fuente: [plan general](../PLAN-IMPLEMENTACION.md) y [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md). Referentes/revisores propuestos, no aceptación humana. Evidencia inicial pendiente.

## Tablero único

| ID | Responsable | Revisor | Prioridad | Depende de | Semana | Estado |
|---|---|---|---|---|---|---|
| TASK-TRANS-S01-OPS-001 | Andres | Leonidas | P0 | G-STACK/G-AUTH: cerrar decisiones antes activar | 6 | Pendiente |
| TASK-TRANS-S01-OPS-002 | Andres | Fernando | P0 | TASK-TRANS-S01-OPS-001 + código/entorno propio o autorizado | 7 | Pendiente |
| TASK-TRANS-S01-QA-001 | Fernando | Diego | P0 | QA-001/QA-002 funcionales del sprint + OPS-002 + INT reales para prueba externa | 7 | Pendiente |
| TASK-TRANS-S01-DOC-001 | Sebastian | Jim | P1 | Resultados QA/INT/OPS del sprint; no esperar para registrar bloqueos | 7 | Pendiente |
| TASK-TRANS-S01-DOC-002 | Diego | Jim | P0 | Plan + capacidad confirmada por cada referente | 6 | Pendiente |
| TASK-TRANS-S02-OPS-001 | Andres | Leonidas | P0 | TASK-TRANS-S01-OPS-001; base y gates del sprint | 8 | Pendiente |
| TASK-TRANS-S02-OPS-002 | Andres | Fernando | P0 | TASK-TRANS-S02-OPS-001 + código/entorno propio o autorizado | 9 | Pendiente |
| TASK-TRANS-S02-QA-001 | Fernando | Diego | P0 | QA-001/QA-002 funcionales del sprint + OPS-002 + INT reales para prueba externa | 9 | Pendiente |
| TASK-TRANS-S02-DOC-001 | Sebastian | Jim | P1 | Resultados QA/INT/OPS del sprint; no esperar para registrar bloqueos | 9 | Pendiente |
| TASK-TRANS-S02-DOC-002 | Diego | Jim | P0 | Plan + capacidad confirmada por cada referente | 8 | Pendiente |
| TASK-TRANS-S03-OPS-001 | Andres | Leonidas | P0 | TASK-TRANS-S01-OPS-001; base y gates del sprint | 10 | Pendiente |
| TASK-TRANS-S03-OPS-002 | Andres | Fernando | P0 | TASK-TRANS-S03-OPS-001 + código/entorno propio o autorizado | 11 | Pendiente |
| TASK-TRANS-S03-QA-001 | Fernando | Diego | P0 | QA-001/QA-002 funcionales del sprint + OPS-002 + INT reales para prueba externa | 11 | Pendiente |
| TASK-TRANS-S03-DOC-001 | Sebastian | Jim | P1 | Resultados QA/INT/OPS del sprint; no esperar para registrar bloqueos | 11 | Pendiente |
| TASK-TRANS-S03-DOC-002 | Diego | Jim | P0 | Plan + capacidad confirmada por cada referente | 10 | Pendiente |
| TASK-TRANS-S04-OPS-001 | Andres | Leonidas | P0 | TASK-TRANS-S01-OPS-001; base y gates del sprint | 12 | Pendiente |
| TASK-TRANS-S04-OPS-002 | Andres | Fernando | P0 | TASK-TRANS-S04-OPS-001 + código/entorno propio o autorizado | 13 | Pendiente |
| TASK-TRANS-S04-QA-001 | Fernando | Diego | P0 | QA-001/QA-002 funcionales del sprint + OPS-002 + INT reales para prueba externa | 13 | Pendiente |
| TASK-TRANS-S04-DOC-001 | Sebastian | Jim | P1 | Resultados QA/INT/OPS del sprint; no esperar para registrar bloqueos | 13 | Pendiente |
| TASK-TRANS-S04-DOC-002 | Diego | Jim | P0 | Plan + capacidad confirmada por cada referente | 12 | Pendiente |
| TASK-TRANS-S05-OPS-001 | Andres | Leonidas | P0 | TASK-TRANS-S01-OPS-001; base y gates del sprint | 14 | Pendiente |
| TASK-TRANS-S05-OPS-002 | Andres | Fernando | P0 | TASK-TRANS-S05-OPS-001 + código/entorno propio o autorizado | 15 | Pendiente |
| TASK-TRANS-S05-QA-001 | Fernando | Diego | P0 | QA-001/QA-002 funcionales del sprint + OPS-002 + INT reales para prueba externa | 15 | Pendiente |
| TASK-TRANS-S05-DOC-001 | Sebastian | Jim | P1 | Resultados QA/INT/OPS del sprint; no esperar para registrar bloqueos | 15 | Pendiente |
| TASK-TRANS-S05-DOC-002 | Diego | Jim | P0 | Plan + capacidad confirmada por cada referente | 14 | Pendiente |
| TASK-TRANS-S01-DB-001 | Leonidas | Andres | P0 | G-DB: artefacto físico no presente; resolver baseline con equipo | 6 | Bloqueado |
| TASK-TRANS-S05-OPS-003 | Andres | Leonidas | P0 | Regresión S5 + gates reales cerrados + entorno propio autorizado | 15 | Pendiente |

## Trabajo y criterios de terminado

### TASK-TRANS-S01-OPS-001

- **Trabajo:** Inicializar FE/BE, tipado y cliente API, pipeline unit/component/API; auditar baseline de seis entidades, Render/PostgreSQL 16/Prisma sin desplegar con secretos en repo.
- **DoD:** Pipeline/entorno reproducible, contratos y decisiones enlazados; evidencia sin credenciales ni cambios sobre infraestructura ajena.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S01-OPS-002

- **Trabajo:** Ejecutar typecheck/lint/build, SAST, SCA/licencias, secret scanning y DAST aplicable; clasificar/corregir/retest hallazgos del incremento. Antienumeración, rate limit, JWT expirado, MFA bypass, retorno interno seguro y tokens fuera de storage/logs. Scans iniciales SAST/SCA/secrets, pruebas CORS/CSRF/cookies según transporte.
- **DoD:** Reportes sanitizados versionados, reglas/versión/entorno documentados y sin riesgo crítico/alto explotable abierto; controles no ejecutados no aparecen aprobados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S01-QA-001

- **Trabajo:** Regresión acumulativa de incrementos previos y nuevo corte vertical; probar navegación/estados/error/timeout, teclado/mobile según specs y pruebas de seguridad. Registro pendiente de verificación en Seguridad, regreso /login sin token; login normal/MFA, recuperación y logout. Mocks etiquetados si transporte aún pendiente.
- **DoD:** Cuenta y base técnica demostrables, pruebas positivas/negativas; política de sesión y BD baseline trazable o bloqueo explícito. No aprobar MFA inventado. Evidencias incluidas y todos hallazgos con dueño; no usar demo aislada como cobertura completa.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S01-DOC-001

- **Trabajo:** Consolidar specs↔tareas↔código↔pruebas, links Figma y gates, documentación operativa; revisar coherencia con modelo lógico y API vigente.
- **DoD:** Cada salida tiene evidencia; docs no prometen trabajo no realizado, quedan pendientes/entorno mock/reales identificados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S01-DOC-002

- **Trabajo:** Revisar horas/carga, estimar y confirmar responsables de ejecución sin cambiar paquetes UI; revisar tablero dos veces/semana, escalar gates y medir riesgo para semana 15.
- **DoD:** Registro de planificación/revisiones con cambios de estado/evidencia, desvíos y decisiones del PO; no agenda ficticia ni aprobación supuesta.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S02-OPS-001

- **Trabajo:** Contrato local con fixture autorizado por cada región; cache policy/ETag/timeouts y observabilidad, preparar recursos DB del carrito sin reserva inventada.
- **DoD:** Pipeline/entorno reproducible, contratos y decisiones enlazados; evidencia sin credenciales ni cambios sobre infraestructura ajena.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S02-OPS-002

- **Trabajo:** Ejecutar typecheck/lint/build, SAST, SCA/licencias, secret scanning y DAST aplicable; clasificar/corregir/retest hallazgos del incremento. XSS/traversal, medios/URL/SSRF, enums/rangos/pageSize abusivos, producto privado y cantidades/precios no autoritativos. Scans y DAST sobre entorno propio.
- **DoD:** Reportes sanitizados versionados, reglas/versión/entorno documentados y sin riesgo crítico/alto explotable abierto; controles no ejecutados no aparecen aprobados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S02-QA-001

- **Trabajo:** Regresión acumulativa de incrementos previos y nuevo corte vertical; probar navegación/estados/error/timeout, teclado/mobile según specs y pruebas de seguridad. Buscar, filtrar, ordenar, paginar, abrir galería/variante, precio/oferta y disponibilidad, agregar una unidad con resultado ajustado/error.
- **DoD:** Catálogo y ficha completa con todos los estados relevantes; ningún error se convierte en agotado/gratis; una pulsación de adición no duplica solicitud. Evidencias incluidas y todos hallazgos con dueño; no usar demo aislada como cobertura completa.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S02-DOC-001

- **Trabajo:** Consolidar specs↔tareas↔código↔pruebas, links Figma y gates, documentación operativa; revisar coherencia con modelo lógico y API vigente.
- **DoD:** Cada salida tiene evidencia; docs no prometen trabajo no realizado, quedan pendientes/entorno mock/reales identificados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S02-DOC-002

- **Trabajo:** Revisar horas/carga, estimar y confirmar responsables de ejecución sin cambiar paquetes UI; revisar tablero dos veces/semana, escalar gates y medir riesgo para semana 15.
- **DoD:** Registro de planificación/revisiones con cambios de estado/evidencia, desvíos y decisiones del PO; no agenda ficticia ni aprobación supuesta.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S03-OPS-001

- **Trabajo:** Validar transacciones/constraints Prisma/DB; preparar fixtures del worker/eventos/CSAT y casos negativos para no concentrar preparación en S5.
- **DoD:** Pipeline/entorno reproducible, contratos y decisiones enlazados; evidencia sin credenciales ni cambios sobre infraestructura ajena.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S03-OPS-002

- **Trabajo:** Ejecutar typecheck/lint/build, SAST, SCA/licencias, secret scanning y DAST aplicable; clasificar/corregir/retest hallazgos del incremento. IDOR carrito/favoritos y cookie ajena, CSRF según transporte, carrera If-Match/merge, rollback y limpieza de caché entre dos cuentas. Scans y DAST autenticado sólo autorizado.
- **DoD:** Reportes sanitizados versionados, reglas/versión/entorno documentados y sin riesgo crítico/alto explotable abierto; controles no ejecutados no aparecen aprobados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S03-QA-001

- **Trabajo:** Regresión acumulativa de incrementos previos y nuevo corte vertical; probar navegación/estados/error/timeout, teclado/mobile según specs y pruebas de seguridad. Invitado agrega, inicia sesión, merge completo/parcial/error; continuar sólo muestra cuenta, retry seguro; mover entre listas, producto retirado, variante requerida y vacío.
- **DoD:** Carrito/favoritos y ambas salidas de merge probadas; Deshacer sólo completo si restauración segura contratada. No duplicar carrito ni guardar favoritado por SKU. Evidencias incluidas y todos hallazgos con dueño; no usar demo aislada como cobertura completa.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S03-DOC-001

- **Trabajo:** Consolidar specs↔tareas↔código↔pruebas, links Figma y gates, documentación operativa; revisar coherencia con modelo lógico y API vigente.
- **DoD:** Cada salida tiene evidencia; docs no prometen trabajo no realizado, quedan pendientes/entorno mock/reales identificados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S03-DOC-002

- **Trabajo:** Revisar horas/carga, estimar y confirmar responsables de ejecución sin cambiar paquetes UI; revisar tablero dos veces/semana, escalar gates y medir riesgo para semana 15.
- **DoD:** Registro de planificación/revisiones con cambios de estado/evidencia, desvíos y decisiones del PO; no agenda ficticia ni aprobación supuesta.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S04-OPS-001

- **Trabajo:** CheckoutOperation y recuperación, probar timeout con respuesta tardía; preparar NotificationDelivery/outbox con contrato aunque correo final se completa S5.
- **DoD:** Pipeline/entorno reproducible, contratos y decisiones enlazados; evidencia sin credenciales ni cambios sobre infraestructura ajena.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S04-OPS-002

- **Trabajo:** Ejecutar typecheck/lint/build, SAST, SCA/licencias, secret scanning y DAST aplicable; clasificar/corregir/retest hallazgos del incremento. Token titular vs técnico, IDOR de dirección/quote/operación, alteración montos, cupón sin consumo, fingerprints/idempotencia/replay y no PII/tarjetas. Scans/DAST autorizado y concurrencia controlada.
- **DoD:** Reportes sanitizados versionados, reglas/versión/entorno documentados y sin riesgo crítico/alto explotable abierto; controles no ejecutados no aparecen aprobados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S04-QA-001

- **Trabajo:** Regresión acumulativa de incrementos previos y nuevo corte vertical; probar navegación/estados/error/timeout, teclado/mobile según specs y pruebas de seguridad. Seleccionar/crear dirección V-010; cotizar/cupón/no cobertura/expiración; preparar; crear pedido o mostrar SUBMITTED y consultar operación original.
- **DoD:** Un pedido bajo doble click/retry y estado incierto recuperable; deep link/mapping definidos, ningún PREPARED se presenta como pedido. Email envío todavía asíncrono, no afirmación SENT. Evidencias incluidas y todos hallazgos con dueño; no usar demo aislada como cobertura completa.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S04-DOC-001

- **Trabajo:** Consolidar specs↔tareas↔código↔pruebas, links Figma y gates, documentación operativa; revisar coherencia con modelo lógico y API vigente.
- **DoD:** Cada salida tiene evidencia; docs no prometen trabajo no realizado, quedan pendientes/entorno mock/reales identificados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S04-DOC-002

- **Trabajo:** Revisar horas/carga, estimar y confirmar responsables de ejecución sin cambiar paquetes UI; revisar tablero dos veces/semana, escalar gates y medir riesgo para semana 15.
- **DoD:** Registro de planificación/revisiones con cambios de estado/evidencia, desvíos y decisiones del PO; no agenda ficticia ni aprobación supuesta.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S05-OPS-001

- **Trabajo:** Semana14 completar/enganchar funciones sobre fixtures preparados; semana 15 cerrar regresión, responsive/a11y, contrato real, reproducibilidad/migraciones/backup/runbook y evidencias.
- **DoD:** Pipeline/entorno reproducible, contratos y decisiones enlazados; evidencia sin credenciales ni cambios sobre infraestructura ajena.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S05-OPS-002

- **Trabajo:** Ejecutar typecheck/lint/build, SAST, SCA/licencias, secret scanning y DAST aplicable; clasificar/corregir/retest hallazgos del incremento. IDOR pedidos/tracking/CSAT, replay webhook, remitente autenticado, plantilla XSS/header injection/URLs, email cifrado, no secretos/PII. Scans y DAST finales, regresión MFA/checkout y restauración backup propia.
- **DoD:** Reportes sanitizados versionados, reglas/versión/entorno documentados y sin riesgo crítico/alto explotable abierto; controles no ejecutados no aparecen aprobados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S05-QA-001

- **Trabajo:** Regresión acumulativa de incrementos previos y nuevo corte vertical; probar navegación/estados/error/timeout, teclado/mobile según specs y pruebas de seguridad. Pedido propio/histórico → tracking/202; recomprar sin precio histórico; confirmación email y evento homologado sin duplicados; GOOD/REGULAR/BAD en ENTREGADO, duplicado controlado.
- **DoD:** Cobertura F-001–F-040 demostrada con evidencia, no hallazgos críticos/altos explotables abiertos; lista honesta de bloqueos/desvíos si algo no cabe. Mock no se reporta como integración real. Evidencias incluidas y todos hallazgos con dueño; no usar demo aislada como cobertura completa.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S05-DOC-001

- **Trabajo:** Consolidar specs↔tareas↔código↔pruebas, links Figma y gates, documentación operativa; revisar coherencia con modelo lógico y API vigente.
- **DoD:** Cada salida tiene evidencia; docs no prometen trabajo no realizado, quedan pendientes/entorno mock/reales identificados.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S05-DOC-002

- **Trabajo:** Revisar horas/carga, estimar y confirmar responsables de ejecución sin cambiar paquetes UI; revisar tablero dos veces/semana, escalar gates y medir riesgo para semana 15.
- **DoD:** Registro de planificación/revisiones con cambios de estado/evidencia, desvíos y decisiones del PO; no agenda ficticia ni aprobación supuesta.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.

### TASK-TRANS-S01-DB-001

- **Trabajo:** Localizar baseline físico del equipo o formalizar migración inicial en backend; verificar Cart,CartItem,WishlistItem,CheckoutOperation,PostDeliveryPrompt,NotificationDelivery y constraints/triggers frente modelo/diccionario. No reconstruir ni sobrescribir trabajo del equipo sin comparar.
- **DoD:** Artefacto ejecutable localizado/versionado, esquema Prisma y migraciones probados en PostgreSQL 16 de prueba; cero réplica externa, redacción de logs y revisión por ambos responsables BD.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** G-DB: documentación refiere SQL04 ausente; requiere artefacto/migración verificable antes de aplicar baseline.

### TASK-TRANS-S05-OPS-003

- **Trabajo:** Ensayar entrega/rollback app, migraciones forward compatibles y restore de backup en BD de prueba; Render backend/PostgreSQL y Prisma según arquitectura, frontend Vercel según decisión confirmada. Revisar TLS/secrets/least privilege, logs/alertas y configuración mocks deshabilitada en entorno real.
- **DoD:** Runbook y restore reproducibles, evidencia release y riesgos, sin secretos en bundle/config/versionado, ni migración destructiva en BD real; aprobación independiente.
- **Evidencia:** Pendiente; registrar comando/entorno/casos/resultados/revisión reales, sin secretos ni PII.
- **Bloqueo actual:** Ready y dependencias del tablero; ninguna ejecución constatada.


## Revisión

| Semana | Decisión/cambio de estado | Evidencia | Revisó |
|---|---|---|---|
| 6, preparación | Creación, sin ejecución | Planes y tareas; baseline física pendiente | Validación humana pendiente |

