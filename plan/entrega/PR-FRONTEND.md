# Título propuesto

test(h3): verificar la web con NestJS y automatizar los controles de catálogo

Base manual: **main**. Rama: `feat/s1-f006-f007-catalogo`.

## Descripción para copiar

Las pruebas de navegador del catálogo ahora compilan e inician Backend NestJS con MOCK explícito y configuración sintética. CI usa Chromium en Linux; la ejecución local conserva Edge. El workflow obtiene Backend público por SHA fijo, instala lockfiles y ejecuta lint, componentes, build, E2E, tipado y análisis de seguridad sin secretos de Productos ni despliegue.

El diseño Figma y la implementación H3 ya forman parte del baseline main; este PR debe revisarse por su diff actual de pruebas/automatización y documentación. No incluye el `next-env.d.ts` local generado por desarrollo. Guía de controles en `docs/CI-H3.md`.

Validación, hallazgos y límites: [evidencia H3 publicada](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/docs/giuliano-elementos-compartidos/plan/evidencias/H3-AUTONOMIA-2026-10-16.md). El recorrido web→Next→BFF se verifica con fixtures; no acredita integración REAL ni aceptación visual humana. Permanecen pendientes Productos, despliegue y revisión independiente.
