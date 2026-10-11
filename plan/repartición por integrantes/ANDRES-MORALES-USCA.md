# Andres Fernando Morales Usca — DevOps, seguridad y backend — H3

**Repos de trabajo:** G1-Marketplace-Backend y G1-Marketplace-Frontend sólo en configuración/deploy. **Ramas sugeridas:** `chore/s1-base-despliegue` y `ci/s1-build-test-deploy`, separadas por repo desde `develop`. **Revisor:** Leonidas; Diego verifica pipeline. **Estado inicial:** pendiente; estimación por confirmar. Leer [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md).

## Entrega de software

- Liderar `TASK-TRANS-S01-OPS-001` y `TASK-TRANS-S01-OPS-002`: auditar Prisma/migración y `render.yaml` existente sin destruir datos; preparar runtime reproducible, variables de entorno, health seguro y CI mínimo de build/test. Coordinar interfaz de arranque con Leonidas antes de editar su servidor.
- Configurar despliegue de frontend y BFF, URL pública, origen CORS concreto y secretos fuera de Git. Retirar `Access-Control-Allow-Origin: *` del entorno final; `/health` debe acreditar servicio/DB sin exponer conteos o mensajes internos. Verificar un redeploy desde commit conocido y registrar rollback posible.
- Preparar `PRODUCTOS_BASE_URL`, credenciales de servicio y obtención/caché segura del JWT **sólo en backend**, conforme al contrato acordado con Seguridad. No inventar secretos, grants o endpoints; si faltan, dejar plantilla `.env.example` sin valores reales y registrar el bloqueo I-01. Asistir a Leonidas con respuesta 401/403/429 y redacción de logs.
- `TASK-TRANS-S01-DB-001`: revisar que el esquema actual corresponda al modelo lógico; para H3 no crear tablas de productos ni usar BD de G6. Reportar divergencias de Prisma como hallazgo, sin migración destructiva en producción.

**Entradas:** [S1](../iteraciones/S01-semanas-07-08.md), [DevSecOps](../DEVSECOPS-Y-PRUEBAS.md), [decisiones G-DB/G-CLOUD-H3/I-01](../DECISIONES-Y-BLOQUEOS.md), [backend actual](https://github.com/Taller-SW-Web/G1-Marketplace-Backend), [DS-001/G-STACK](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md).

**Entregar a todos:** URLs de entorno, comandos de build/test/deploy, variables requeridas sin secretos y procedimiento de recuperación. **PR:** al `develop` de cada repo afectado, nunca cambios de infraestructura mezclados sin coordinación con el BFF. **Evidencia IA:** nota propia según [guía](GUIA-DE-TRABAJO-COLABORATIVO.md#seguimiento-evidencia-y-uso-de-ia--obligatorio-para-cada-integrante).
