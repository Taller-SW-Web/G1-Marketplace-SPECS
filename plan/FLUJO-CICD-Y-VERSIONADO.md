# Flujo de trabajo, CI/CD y versionado (H4)

Versión 1.0.0 · 04/11/2026 · Aplica a los repos de código: [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend). Complementa la [guía de trabajo colaborativo](repartición%20por%20integrantes/GUIA-DE-TRABAJO-COLABORATIVO.md); ante contradicción sobre ramas o despliegue, rige este documento.

## Resumen en una línea

**Issue → rama desde `develop` → PR hacia `develop` → merge → el pipeline compila, prueba, versiona y despliega solo.** Nadie despliega ni edita versiones a mano.

## 1. De la issue al despliegue

```text
Issue (TASK-Fxxx-...)
   │  crear rama desde develop:  feat/f0xx-tema · fix/f0xx-tema · test/... · docs/... · ci/...
   ▼
Commits convencionales en español   (ver §2)
   ▼
Pull Request  ───►  base: develop        (NUNCA hacia main)
   │  corre: Build → Compile → Test      (debe quedar en verde)
   │  revisión del revisor asignado en la issue
   ▼
Merge a develop
   │  corre el pipeline completo (cicd.yml):
   │  Build → Compile → Test → Versionado → Deploy → Smoke test
   ▼
Producción de la demo: Render (BE) y Vercel (FE) despliegan DESDE develop
```

Puntos clave:

- **`develop` es la rama de integración y de despliegue.** Render (backend) y Vercel (frontend) despliegan desde `develop`. `main` no es la fuente del despliegue mientras no se acuerde otra cosa.
- **Toda PR va hacia `develop`.** Ramas cortas (una por tarea), creadas desde `develop` actualizado. No hacer push directo a `develop`.
- **Una PR roja no se fusiona.** Si Build, Compile o Test fallan, se corrige en la misma rama.
- Enlazar la issue en la PR (`closes #N`) y registrar la evidencia en la issue, como pide la guía colaborativa.
- Los PR de SPECS siguen la excepción vigente: documentación revisada con commit directo a `main`.

## 2. Commits convencionales: ahora determinan la versión

El formato es `tipo(alcance): descripción en español` (verbo en infinitivo, sin punto final). **El tipo decide el número de versión**, así que hay que usarlo bien:

| Commit | Efecto en la versión (SemVer) | Ejemplo |
|---|---|---|
| `fix:` | PATCH (1.0.0 → 1.0.1) | `fix(carrito): corregir cantidad al fusionar carritos` |
| `feat:` | MINOR (1.0.1 → 1.1.0) | `feat(favoritos): agregar mover al carrito` |
| `feat!:` o pie `BREAKING CHANGE:` | MAJOR (1.1.0 → 2.0.0) | `feat!(api): cambiar contrato de /carts/current` |
| `docs`, `test`, `ci`, `chore`, `refactor`, `build` | Sin versión nueva | `test(auth): cubrir sesión vencida` |

Reglas:

- **No editar `version` en `package.json` ni `CHANGELOG.md` a mano.** El pipeline los actualiza.
- Un `feat!` (cambio incompatible) debe avisarse en la issue y al revisor antes de fusionar.
- Si una PR se fusiona con *squash*, **el título de la PR es el commit** que se analiza: debe seguir el formato convencional.

## 3. Qué hace el pipeline (`.github/workflows/cicd.yml`)

| Etapa | Cuándo corre | Qué hace |
|---|---|---|
| Build | PR y push a `develop` | BE: `prisma generate` + `tsc`. FE: `next build`. |
| Compile | PR y push a `develop` | Verificación de tipos (`tsc --noEmit`); en FE también `eslint`. |
| Test | PR y push a `develop` | BE: unitarias, e2e, mock-auth y sonda G6. FE: pruebas de componentes y de servidor. |
| Versionado | Solo push a `develop` | `semantic-release`: calcula la versión, actualiza `package.json` y `CHANGELOG.md`, crea el tag `vX.Y.Z` y el release en GitHub. |
| Imagen Docker | Solo si hubo versión nueva | Construye el `Dockerfile` y publica `ghcr.io/taller-sw-web/<repo>:X.Y.Z` y `latest`, con la **misma versión** del tag. |
| Deploy | Solo push a `develop`, tras Test | Dispara el deploy hook de Render (BE) o Vercel (FE). |
| Smoke test | Después del deploy | `curl` con reintentos a `/health` (BE) o al sitio (FE); falla si no responde 200. |

Notas:

- El release crea un commit `chore(release): X.Y.Z [skip ci]` en `develop`. **Hacer `git pull` antes de continuar** para no divergir.
- El backend en Render (plan gratuito) puede tardar ~30 s en despertar; el smoke test reintenta.
- Las pruebas E2E con Playwright siguen en sus workflows propios (`e2e.yml`, `auth-h4.yml`, etc.) y no sustituyen a este pipeline.

## 4. Corregir un error en producción (hotfix)

1. Rama `fix/<tema>` desde `develop` con una **prueba que reproduce el error** y la corrección mínima.
2. PR hacia `develop` con pipeline en verde y revisión.
3. Al fusionar, el commit `fix:` genera una versión PATCH y se despliega.
4. **Rollback** (volver a la versión anterior) si el fallo no depende de datos: redeploy del release anterior en Render/Vercel, y registrar en la issue la causa y el tag al que se volvió.

## 5. Estado de la configuración (al 04/11/2026)

| Elemento | Estado |
|---|---|
| Workflows `cicd.yml`, `.releaserc.json` y `docs/CICD-H4.md` en FE y BE | Fusionados a `develop` (ver PR de cada repo) |
| Build, Compile y Test en GitHub Actions | Verificado en las PR |
| Versionado, imagen Docker, Deploy y Smoke test | Se ejecutan por primera vez al fusionar; confirmar el resultado en la pestaña *Actions* |
| Secretos `RENDER_DEPLOY_HOOK_URL` y `VERCEL_DEPLOY_HOOK_URL` | **Pendiente**: sin ellos el job Deploy falla a propósito |
| Desactivar auto-deploy de Render y Vercel | **Pendiente**: hasta entonces el proveedor también despliega por su cuenta al hacer push |
| Versión base | Primera versión automática: **1.0.0** |

Actualizar esta tabla cuando se cierren los pendientes.
