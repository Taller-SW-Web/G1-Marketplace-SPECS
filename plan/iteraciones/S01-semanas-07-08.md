# S1 — Primer flujo funcional en nube (semanas 7–8)

Versión 0.2.0 · Replanificación para Hito 3. No se infiere ejecución de este plan.

## Objetivo y alcance

Cerrar **F-006 inicio/categorías** y **F-007 búsqueda** como corte público mínimo: usuario → frontend → BFF de Marketplace → API real de Productos. El resultado debe verse en una URL desplegada, con vacío/error recuperables. Destacados no se inventan: sección vacía u omitida mientras G-FEATURED siga abierta. No se anteponen F-001–005 al flujo público.

La base remota de backend/Prisma y Render se **audita y aprovecha** si corresponde; `/health` no es integración con otro módulo. Inicializar frontend y BFF según specs, sin presentar README/Figma como aplicación.

## Secuencia por semana

- **Semana 7:** cerrar mínimo I-01 para lectura pública de Productos (versión/ruta/auth/datos/prueba), UI kit/versiones/lockfile pendientes de G-STACK, arquitectura de despliegue y dueños de entorno. Inicializar el frontend con React + TypeScript + Next.js App Router decidido por el PO. Auditar migración/DB existente. Crear frontend/BFF ejecutables, contrato tipado y adaptador, estados básicos; pipeline build/test mínimo.
- **Semana 8, antes de presentación:** conectar datos reales de Productos, probar vacío/error/timeout, desplegar FE y BE en nube y verificar la URL desde fuera del equipo. Registrar commit, endpoint, petición/respuesta sanitizada, logs y capturas; diagrama de contexto y arquitectura deben corresponder al despliegue. Ensayar demo/rollback. Si I-01 no se libera, escalar inmediatamente: un fixture no cumple el requisito de integración.

## Tareas técnicas y evidencia

| Bloque | Cierre verificable |
|---|---|
| FE | Home/búsqueda públicas utilizables en desktop y responsive exigido, estados de carga/vacío/error; acción real en URL pública. |
| BE/INT | BFF valida consulta, usa endpoint aprobado de Productos, traduce datos/errores, timeout y log sin PII; prueba de contrato positiva/negativa. |
| DB/OPS | Base Prisma auditada; configuración y secretos por entorno; FE/BE desplegados, health, CORS y build reproducible. No copiar catálogo a BD local. |
| QA/DOC | Prueba web→BFF→Productos en nube, regresión mínima, diagramas y evidencias con commit/versiones/URL. |

**Gate H3:** demo funcional, llamada intermodular real, despliegue accesible y evidencias de arquitectura/código. No marcar F-006/F-007 `Terminado` si sólo funciona un mock. Usar [decisiones](../DECISIONES-Y-BLOQUEOS.md), [seguimiento](../seguimiento/README.md) y [paquetes personales S1](../repartición%20por%20integrantes/README.md). La asignación es propuesta pendiente de estimación/aceptación por cada integrante.
