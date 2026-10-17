# Reportes sanitizados H3 — 16/10/2026

Contexto y resultados: [evidencia principal](../H3-AUTONOMIA-2026-10-16.md).

| Archivos | Procedencia y alcance |
|---|---|
| [backend-summary.json](backend-summary.json), [frontend-summary.json](frontend-summary.json) | Ejecuciones locales Windows sobre el árbol preparado antes de commit; head refleja el commit anterior, no un árbol limpio |
| [backend-licenses.json](backend-licenses.json), [frontend-licenses.json](frontend-licenses.json) | Inventario local del lockfile y manifests instalados, incluyendo declaraciones legacy; no aprobación legal |
| [backend-smoke-local.json](backend-smoke-local.json) | Proceso compilado local con BD ausente y readiness DOWN esperado |
| [backend-ci-summary.json](backend-ci-summary.json), [backend-ci-licenses.json](backend-ci-licenses.json), [backend-ci-smoke.json](backend-ci-smoke.json) | CI Ubuntu, commit 63071c8; el smoke comprueba readiness UP con PostgreSQL 16 temporal |
| [frontend-ci-summary.json](frontend-ci-summary.json), [frontend-ci-licenses.json](frontend-ci-licenses.json) | CI Ubuntu, commit ad7206c; Frontend prueba Backend 63071c8 y conserva fuentes/versiones fijadas |

Artefactos originales, descargados y verificados antes de extraer estos JSON:

| Repo / artefacto | Run | SHA-256 ZIP |
|---|---|---|
| Backend, 12027105707 | [38854701659](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/38854701659) | `cc8efa11623e6ab112a3733bf54c2ffa25b31fafa9d080dcc6392428d8ce4312` |
| Frontend, 12026747277 | [38854728651](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/38854728651) | `4c4977c688095d9730ac8a80a1dde09ada42bac85e136887e1893b7a3ba45078` |

Los ZIP de GitHub caducan a los 7 días. Este directorio sólo conserva metadatos permitidos: no contiene coincidencias de secretos, código fuente del escáner, emails, tokens, URLs de descarga firmadas ni logs crudos. El reporte de navegador completo con fixtures sintéticos permanece en el artefacto FE durante su retención.

Un gate aprobado no implica aceptación humana de las 19 vulnerabilidades moderadas de desarrollo del baseline BE, aprobación legal del inventario, revisión visual, integración REAL ni cierre H3.
