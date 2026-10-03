# Sprint 1 — Base técnica y cuenta

Versión 0.1.0 · En revisión · Semanas 6–7, sin fechas calendario. Coordinación Diego; priorización Jim. No ejecutado por esta documentación.

## Objetivo e incremento

Preparar repos de código, sesión protegida y API de acceso; registrar/recuperar/reset/login/MFA/logout sin crear usuarios/tokens locales.

**Demo al cierre:** Registro pendiente de verificación en Seguridad, regreso /login sin token; login normal/MFA, recuperación y logout. Mocks etiquetados si transporte aún pendiente.

## Alcance trazable

| ID | Plan | Tareas |
|---|---|---|
| F-001 · Registrar cliente | [Plan](../funcionalidades/F-001-registrar-cliente.md) | [Seguimiento](../seguimiento/F-001-registrar-cliente.md) |
| F-002 · Iniciar sesión | [Plan](../funcionalidades/F-002-iniciar-sesion.md) | [Seguimiento](../seguimiento/F-002-iniciar-sesion.md) |
| F-003 · Cerrar sesión | [Plan](../funcionalidades/F-003-cerrar-sesion.md) | [Seguimiento](../seguimiento/F-003-cerrar-sesion.md) |
| F-004 · Solicitar recuperación de contraseña | [Plan](../funcionalidades/F-004-solicitar-recuperacion-password.md) | [Seguimiento](../seguimiento/F-004-solicitar-recuperacion-password.md) |
| F-005 · Restablecer contraseña | [Plan](../funcionalidades/F-005-restablecer-password.md) | [Seguimiento](../seguimiento/F-005-restablecer-password.md) |

Son 5 funcionalidades y 30 tareas por área; además tareas comunes. Cada plan enlaza cuatro specs. No nuevas épicas ni historias de usuario.

## Entrada y bloqueos

G-STACK, G-AUTH, G-DB, G-SHELL; contrato/versiones/lockfile y capacidad de equipo.

Leer [decisiones](../DECISIONES-Y-BLOQUEOS.md) y confirmar Ready/capacidad. Gates externos abiertos bloquean integración real, no componentes puros o preparación de fixtures. Fuente local vigente, no APIs asumidas por mensajes no registrados.

## Trabajo por semana

- **Semana 6:** cerrar preparación/decisiones y priorizar corte vertical; FE estados con fixtures, BE DTO/adaptador y DB según ownership; escribir tests funcionales/seguridad antes o junto al código.
- **Semana7:** conectar partes y contrato real sólo aprobado; E2E/negativos/correcciones, responsive/a11y, escaneos y revisión independiente. No dejar toda seguridad para release.
- Inicializar FE/BE, tipado y cliente API, pipeline unit/component/API; auditar baseline de seis entidades, Render/PostgreSQL 16/Prisma sin desplegar con secretos en repo.

Frontend: Giuliano referentes propuestos; backend Leonidas; DB Leonidas+Andres; QA Fernando; DevSecOps Andres; documentación Sebastian; coordinación Diego; alcance/riesgo Jim. Propuesta por rol, no altera responsables de mockups.

## Pruebas y DevSecOps obligatorios

Antienumeración, rate limit, JWT expirado, MFA bypass, retorno interno seguro y tokens fuera de storage/logs. Scans iniciales SAST/SCA/secrets, pruebas CORS/CSRF/cookies según transporte.

Además pruebas por tarea QA-001 y QA-002 de cada funcionalidad, y regresión acumulativa. Tool/version/entorno y resultados en evidencia. No scans de terceros sin autorización.

## Tareas comunes del sprint

- [TASK-TRANS-S01-OPS-001](../seguimiento/TRANSVERSALES.md#task-trans-s01-ops-001) — Andres; revisor Leonidas; semana 6.
- [TASK-TRANS-S01-OPS-002](../seguimiento/TRANSVERSALES.md#task-trans-s01-ops-002) — Andres; revisor Fernando; semana7.
- [TASK-TRANS-S01-QA-001](../seguimiento/TRANSVERSALES.md#task-trans-s01-qa-001) — Fernando; revisor Diego; semana7.
- [TASK-TRANS-S01-DOC-001](../seguimiento/TRANSVERSALES.md#task-trans-s01-doc-001) — Sebastian; revisor Jim; semana7.
- [TASK-TRANS-S01-DOC-002](../seguimiento/TRANSVERSALES.md#task-trans-s01-doc-002) — Diego; revisor Jim; semana 6.
- [TASK-TRANS-S01-DB-001](../seguimiento/TRANSVERSALES.md#task-trans-s01-db-001) — Leonidas; revisor Andres; semana 6.

## Cierre y Definition of Done

Cuenta y base técnica demostrables, pruebas positivas/negativas; política de sesión y BD baseline trazable o bloqueo explícito. No aprobar MFA inventado.

- Cumplir [DoD global](../PLAN-IMPLEMENTACION.md#7-definition-of-ready-y-definition-of-done).
- Demo y evidencia real, no sólo mockups; distinguir contract fixture/sandbox/real.
- Tablero mantiene tareas no acabadas con motivo/gate/objetivo; no declarar sprint completo por un camino feliz.
- Revisar capacidad del siguiente corte y riesgo de semana 15, sin perder funcionalidades del alcance.

