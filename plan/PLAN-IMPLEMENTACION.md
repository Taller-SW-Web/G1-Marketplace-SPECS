# Plan de implementación

Versión 0.1.0 · En revisión · 2026-10-02 · PO: Jim Bryan Segovia Valencia · Coordinación: Diego Steven Martin Espinoza Picon.

## 1. Resultado y alcance

Construir iterativamente las 40 funcionalidades especificadas, con frontend, BFF, persistencia propia, integración, QA, documentación y DevSecOps. El plan llega a **semana 15**, no17. Son diez semanas académicas y cinco sprints de dos semanas; sin fechas de calendario supuestas ni equivalencias con hitos del profesor no confirmadas.

El alcance es F-001–F-040 y sus 17 vistas / 10 overlays / 2 correos, no las ocho specs depreciadas ni los puntos históricos 91/230 como estimación de código. Las 40 specs React se mantienen [aquí](../SPECS/componentes-react/README.md). Backend/frontend locales contienen sólo README; no existe una aplicación ejecutable verificada, por lo que la base técnica está incluida en S1.

## 2. Secuencia y entregas

| Sprint | Semanas | Funcionalidades objetivo | Incremento demostrable |
|---|---|---|---|
| [S1](iteraciones/S01-semanas-06-07.md) | 6–7 | F-001–005 + base técnica | Acceso/registro/recuperación, política de sesión y MFA homologada; repos de código inicializados, CI con pruebas/escaneos y BD/migraciones auditadas. |
| [S2](iteraciones/S02-semanas-08-09.md) | 8–9 | F-006–016 | Inicio → catálogo/búsqueda/filtro/orden/página → ficha/variantes/precio/stock → agregar SKU. |
| [S3](iteraciones/S03-semanas-10-11.md) | 10–11 | F-017–021 y F-036–039 | Carrito/fusión/continuar sin combinar, favoritos y movimientos seguros. |
| [S4](iteraciones/S04-semanas-12-13.md) | 12–13 | F-022–027 | Checkout titular: dirección → quote/beneficio → simulación → creación única → confirmación cierta/pendiente. |
| [S5](iteraciones/S05-semanas-14-15.md) | 14–15 | F-028–035 y F-040 + estabilización | Historial/detalle/recompra/tracking, correos worker y encuesta entregada; regresión integral, mobile, seguridad y entrega técnica. |

La secuencia de elaboración React comenzó por acceso/carrito/favoritos conforme lista; **la secuencia de código prioriza catálogo/SKU antes de activar carrito real**, porque esas mutaciones revalidan productos/precios/stock. No es un cambio funcional.

No esperar a S5 para todo lo transversal: contratos, fixtures, diseño de worker/outbox y casos QA se preparan antes; la ejecución final de esas funcionalidades está en S5. Un sprint no espera a otro para investigar su gate, pero no implementa integración no autorizada.

## 3. Bloques de trabajo por incremento

En cada funcionalidad: componentes/estados → BFF/validación → persistencia cuando corresponde → adaptadores y pruebas de contrato → E2E y seguridad → evidencias. Se puede paralelizar FE con fixtures y BE/DB bajo contrato acordado; integración real sólo cuando haya contrato/configuración/prueba externa.

- **FE:** rutas, compuestos, formularios, estado/caché, recuperación, desktop primero y responsive posteriormente. Mobile se acepta antes de cerrar cada función salvo pendiente de diseño explícitamente registrado; no denominar Terminado un desktop-only cuando spec exige ambos.
- **BE:** autenticación/ownership y reglas de orquestación, DTO/Problem Details, versiones/idempotencia y adapter boundary.
- **DB:** Leonidas y Andres, conforme decisión del PO; seis entidades propias, migraciones y verificación constraints/triggers. Sin réplica de usuarios/direcciones/catálogo/pedidos/CSAT.
- **INT:** fixtures del contrato BFF y de proveedores, homologación documentada y pruebas positivas/negativas autorizadas.
- **QA/DevSecOps:** pruebas unitarias/componentes/API/DB/E2E/seguridad y controles automatizados en cada sprint, no al final.
- **DOC/OPS:** actualizar trazabilidad y operación, pipeline/entornos, logs sin PII y evidencias de despliegue.

## 4. Responsabilidad sin confundir diseño con código

Los nombres cortos de tareas tienen esta equivalencia:

| Nombre | Nombre completo | Referencia de rol actual |
|---|---|---|
| Giuliano | Giuliano Macchiavello Perez | UX/UI y frontend |
| Sebastian | Sebastian Matias Malca Agüero | Documentación y frontend |
| Leonidas | Leonidas Garcia Lescano | Arquitectura/backend; BD junto Andres |
| Andres | Andres Fernando Morales Usca | DevOps/seguridad; BD junto Leonidas |
| Fernando | Fernando Jose Saire Tello | QA |
| Diego | Diego Steven Martin Espinoza Picon | JP/coordinación |
| Jim | Jim Bryan Segovia Valencia | PO/validación alcance |

Las tareas incluyen **referente responsable y revisor propuestos según esos roles**, no asignación humana confirmada ni modificación de paquetes UI. Confirmar carga antes de pasar tarea a En progreso. No convertir el paquete de Figma en obligación de código ni mezclar a Fernando en BD: Leonidas+Andres son BD; Fernando mantiene QA en este plan.

BE tiene un referente principal, y FE dos: es un riesgo de cuello de botella, no una disponibilidad asumida. Revisor distinto de autor, y QA final independiente.

## 5. Preparación, priorización y capacidad

P0 = flujo esencial/dependencia crítica, P1 = capacidad principal complementaria, P2 = mejora no crítica al flujo de compra. La prioridad no elimina P2 del alcance final; todas las 40 permanecen objetivo.

Semana 6: Diego recoge horas/persona por semana y ausencias; equipo estima tareas en horas tras revisar contratos, con capacidad restante real. No inventar fechas ni estimaciones numéricas sin disponibilidad. Reservar **20% de capacidad propuesta** para correcciones/seguridad/contratos; revisar valor con equipo. Límite de trabajo: una tarea de implementación activa por persona más revisiones pequeñas; preferir terminar un corte vertical a comenzar diez pantallas.

Por función medir capacidad: FE+BE+QA+INT+DOC y DB si aplica; por sprint sumarlas y comparar con horas disponibles. Si excede capacidad, registrar desvío y secuencia con PO/JP, sin declarar cobertura completa ni esconder funciones. S5 concentra 9 funciones más estabilización y tiene riesgo alto: preparar fixtures/worker desde S3 y cerrar gates a más tardar S4. Si sigue sobrecargado, reasignación/replanificación debe acordarse, no inventarse.

## 6. Puertas de entrada y bloqueos

[DECISIONES-Y-BLOQUEOS](DECISIONES-Y-BLOQUEOS.md) es registro único. I-01/H-01 catálogo, I-02/H-02 creación idempotente, I-03/H-03 historial autorizado, I-04/H-04 CSAT, I-05/H-05 eventos, I-06/H-06 cliente técnico.

Seguridad tiene acuerdo de verificación confirmado; no se vuelve a negociar ni se diseña nueva pantalla. H-06 fue aceptado verbalmente por Seguridad según contexto, pero la documentación local aún pide configuración/scopes y prueba Despacho: registrar evidencia, no tratar todo I-06 como cerrado.

Una integración está lista sólo con contrato versionado, configuración ambiental y prueba de contrato aprobada. Envío de solicitudes ≠ aceptación. Estado inicial de tareas INT externas = Bloqueado; FE/BE con mocks y QA local pueden avanzar sin afirmar que servicio real funciona.

En autenticación, método MFA/transporte y política requieren G-AUTH; checkout requiere mapping/recuperación G-CHECKOUT; no fabricar endpoints para esquivar pendientes. Cambiar una spec de origen necesita cambio explícito y versionado previo a código.

## 7. Definition of Ready y Definition of Done

**Ready:** cuatro specs leídas, DTO/endpoint/gates entendidos; responsable/revisor aceptaron tarea; fixtures y casos negativos; estimación/capacidad; mockups del estado a construir o excepción documentada. INT real adicionalmente exige homologación y entorno autorizado.

**Done:** implementación completa de alcance, tipos/lint/build, unitarias/componentes/API/DB relevantes, E2E positivo y error, pruebas de seguridad, responsive/a11y, contrato real cuando corresponda y evidencias. Sin secretos/PII, sin vulnerabilidad crítica/alta explotable abierta, docs/fuentes actualizadas y revisión independiente. Si hay dependencia externa sin cerrar, tarea real sigue Bloqueado aunque mocks pasen.

## 8. Seguimiento y cadencia

[Seguimiento](seguimiento/README.md) mantiene estado por tarea; no marcar todo sprint terminado al cerrar documentos.

Propuesta: revisión breve de10–15 min dos veces por semana (Diego coordina), planificación inicio sprint, demo/QA/revisión seguridad al final, retrospectiva y ajuste del siguiente. No es automatización ni reunión creada.

Informe corto: terminado con evidencia, en progreso, bloqueos con dueño/fecha académica, capacidad/desvíos y riesgo para semana 15. Si bloqueo dura dos revisiones, PO/JP escalando al módulo dueño; trabajo local continúa en partes no bloqueadas.

## 9. Operación, rollback y entrega

Backend y PostgreSQL 16 en Render; Prisma con migraciones versionadas; frontend según arquitectura Vercel, revisar decisión al preparar entorno. No crear cuentas/desplegar ahora. Entornos y credenciales fuera repo, mocks explícitos sólo dev/test.

Ensayar restauración de backup en BD de prueba, migración forward/compatibilidad y rollback de versión app; no ejecutar SQL inicial repetidamente sobre producción ni borrar BD. Semana15: build/artefacto versionado, config sin secretos, evidencias regresión/seguridad, contratos cerrados, manual operativo y registro de pendientes reales. La entrega de estas specs/planes no equivale a entrega del software.

