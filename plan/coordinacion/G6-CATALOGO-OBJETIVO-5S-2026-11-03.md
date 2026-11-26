# Catálogo G1/G6: objetivo de cinco segundos y perfil temporal

Propuesta técnica de G1 para revisión, 03/11/2026. No es aceptación bilateral de rendimiento ni evidencia de grant/despliegue.

Giuliano indicó preparar ahora el perfil de integración **15 s hacia G6 / 18 s en Next**, con documentación para que G6 responda dentro de **5 s**. El presupuesto ampliado facilita las pruebas; el objetivo de cinco segundos se mantiene y los defaults de producción no se modifican.

## Evidencia

GET públicos sin JWT, una muestra por operación, 03/11/2026 16:41 Lima:

| Operación | HTTP | Respuesta completa | Objetivo 5 s |
| --- | --- | --- | --- |
| Búsqueda | 200 | 5743 ms | No cumplido en esta muestra |
| Orden por nombre | 200 | 10824 ms | No cumplido en esta muestra |
| Segunda página | 200 | 10840 ms | No cumplido en esta muestra |

Las tres completaron dentro de 15 s. No se deduce un p95, capacidad bajo carga o causa exacta con tres lecturas. Un error rápido no satisface el objetivo. El reporte no retiene payload ni texto de búsqueda.

## Trabajo a coordinar con G6

Confirmar SHA y modo desplegados, dataset y operación; correlacionar SQL, taxonomía, identidad y enriquecimiento de precios. El preview revisado en código enriquece candidatos antes de paginar: investigar si explica los tiempos, sin atribuirlo al despliegue sin trazas. Optimizar/acotar consultas internas para entregar respuestas comerciales correctas y completas al cliente G1 en un máximo propuesto de 5000 ms.

El objetivo debe acordarse con G6 en el entorno correspondiente. La solución no será filtrar una página incompleta, ocultar fallos con vacío o considerar 15 s el nuevo compromiso definitivo.

## Preparación G1

Se prepararon perfiles 5/8 s y 15/18 s, comprobador externo con margen 11/21 s, medición GET acotada y comprobación offline de configuración que no imprime secretos. El pin rc1 se mantiene para el subconjunto consumido; se verificó la operación por ID en su blob. La compatibilidad/configuración efectiva y la aceptación final de los contratos conservan su revisión.

Referencias de implementación: [tiempos](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/giuliano-h4-issues-20261103/docs/CATALOGO-H4-TIEMPOS.md), [verificación/configuración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/giuliano-h4-issues-20261103/docs/CATALOGO-H4-VERIFICACION.md). La web pública de G1 sigue con lecturas 503/filtros 404 en el corte; no se afirma cierre de I-01.
