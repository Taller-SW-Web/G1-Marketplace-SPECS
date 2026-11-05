# F008 — cierre por tarea al 05/11/2026

Responsable: Giuliano. Revisor principal asignado: Sebastián. Esta actualización documenta trabajo entregado y requisitos de cierre; no cambia el DoD, los responsables ni las dependencias. Son seis tareas trabajadas, no seis implementaciones ausentes.

## Ya realizado y qué permanece

**Entregado:** Filtros únicos por categoría/marca, maestros, combinación/rango, limpieza y reset de página; validación de IDs y parámetros administrativos.

**Evidencia REAL disponible:** Sondeo del 05/11: categorías 200; marcas 503 y precioMin=0 503 SERVICIO_NO_DISPONIBLE. El filtro global ya existe en el código G6 revisado; falta operación/datos y retest.

**Retirado de pendientes actuales:** La ruta de filtros ya existe: no conservar 404 como diagnóstico vigente. El sondeo web actual devuelve CATALOG_TIMEOUT. No pedir reimplementar marcas o precio desde cero por sus 503.

**Frontera restante de la función:** G6 debe resolver/probar marcas y el camino ordinario de precio con Catalog/Pricing. Giuliano retesta maestros, combinaciones, límites/vacío/errores, limpieza y reset en UI publicada; corrige mapping si aparece una discrepancia propia.

## Matriz individual de las seis issues

| Tarea / issue | Commit individual original | Incorporado a develop | Qué falta para cerrar esta tarea |
| --- | --- | --- | --- |
| [TASK-F008-FE-001](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/31) | [1d63997165](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/1d63997165728b9487dc14d5f2b9a0b6d68aa06a) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Registrar la aceptación de los criterios FE de esta tarea con Sebastián (estados, props/eventos, desktop/mobile y navegación/URL aplicables) y de su dependencia OPS. El merge revisado por Jim ya está acreditado. Los pendientes de integración de la función no se convierten en falta de implementación del componente. |
| [TASK-F008-BE-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/52) | [1a936193b3](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/1a936193b3e4eaa808200c0941d960efe23d82ef) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Registrar la aceptación del DoD Backend y dependencia OPS con el revisor asignado: DTO, validación, errores y proyección/ownership probados. Jim ya aprobó el merge; Leónidas revisó el alcance MOCK. Los casos REAL pendientes pertenecen al cierre de INT; no exigir reescribir el adaptador ya entregado. |
| [TASK-F008-INT-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53) | [ab7e86b501](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/ab7e86b5019adee2dc6c060ceec16c53d45f766f) | Entrega incorporada por squash de PR; SHA individual conservado en rama | G6 debe resolver/probar marcas y el camino ordinario de precio con Catalog/Pricing. Giuliano retesta maestros, combinaciones, límites/vacío/errores, limpieza y reset en UI publicada; corrige mapping si aparece una discrepancia propia. Confirmar configuración/acceso del entorno: public-read-only explícito tras integrar #273, o JWT con grant/emisión verificados. JWT no es un prerrequisito técnico del modo público acordado. Conservar las dependencias formales originales de esta INT. |
| [TASK-F008-QA-001](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/32) | [27542836e7](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/27542836e7b45f4932a33cadeeda570453cbea1e) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Completar y revisar la matriz por criterio de esta QA con Sebastián/QA, incluyendo el recorrido REAL y los casos pendientes de la función en el entorno acordado. G6 debe resolver/probar marcas y el camino ordinario de precio con Catalog/Pricing. Giuliano retesta maestros, combinaciones, límites/vacío/errores, limpieza y reset en UI publicada; corrige mapping si aparece una discrepancia propia. Las pruebas locales/fixtures ya ejecutadas permanecen como evidencia y no se repiten por rutina. |
| [TASK-F008-QA-002](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/54) | [c2c1baabb6](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/c2c1baabb6a0820bf81e4f7631815206f42a6467) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Adjuntar/revisar negativos del corte y SAST/SCA/secret scan ya existentes; completar DAST aplicable y revisión de riesgos con Andrés/seguridad en entorno propio/autorizado, corregir/reprobar hallazgos y acreditar la dependencia OPS de la tarea. No confundir controles locales/CI con aceptación de staging. |
| [TASK-F008-DOC-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/55) | [fe53b3792d](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/commit/fe53b3792d439932bbd288f3f20dc9ac54029586) | No; documento entregado en SPECS #16 | Revisión independiente y merge de esta actualización en SPECS #16; coherencia de fuentes/specs/evidencias y dependencias INT/QA funcional/QA seguridad originales satisfechas. El texto y el commit documental ya están entregados; no falta redactar la tarea desde cero. |

Se verificaron los 30 commits individuales en sus ramas de entrega. Los 25 aportes FE/BE/INT/QA se incorporaron mediante los squash de FE #124 y BE #265; esos SHA individuales no son ancestros literales de develop. Los cinco DOC permanecen en SPECS #16. Incorporar el artefacto de INT/QA no acredita que sus pruebas externas o aceptación estén completas.

No se exige que las 30 issues cierren juntas. FE/BE se evalúan con su DoD y dependencias; INT exige evidencia REAL y despliegue; ambas QA conservan su alcance; DOC conserva sus dependencias INT/QA. La revisión de merge de Jim se registra y no se borra, pero no se atribuye una aceptación de todos los criterios a Sebastián sin su registro.

## Entregas y revisiones comprobadas al 05/11

- [Frontend #124](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/124) y [Backend #265](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/265) aprobados por Jim y fusionados. HEAD de código revisado: FE dcd949374ee173a70be621bac3c61401637313df; BE 9a1909522aa80b2abdc117b9a7c0c9e729b5dc28. La aprobación se refiere al alcance MOCK revisado, no a una aceptación REAL por función.
- [Backend #273](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/273) prepara public-read-only, tiene aprobación técnica de Leónidas y tres CI correctas; sigue abierto a develop. Mantiene service-token por defecto y demo-no-auth prohibido en producción.
- [Backend #275](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/275) ya implementa F011 REAL por slug sobre #273; tres CI correctas, pendiente de revisión de Sebastián, cambio de base tras el merge del padre e integración. Es apoyo al bloque de detalle, no otra tarea nueva F006–F010.
- [Frontend #132](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/132) ya publica runner/guía REAL reproducibles y pins; cinco ejecuciones correctas. [Prueba desde otra red](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/42077019424): TLS verificado e instalación/build nuevos con Next→BFF→G6 REAL. Falta revisión/merge; al integrar el nuevo Backend, actualizar pins para el conjunto.
- [Leónidas #274](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/274) ya prepara client_credentials/caché/renovación, con CI correcta; falta grant/emisión real. Una simulación de merge reproduce conflicto en provider.ts entre los modos público y client-credentials. Si se integran ambos, reconciliar y retestar; el cliente F011 de #275 necesita integración explícita para usar client-credentials.

No se han solicitado nuevas revisiones formales ni modificado asignaciones con esta reconciliación. Mantener un revisor independiente del artefacto.

## Corte público y límites de la evidencia

Sondeo del 05/11/2026, inicio 13:45:09 Lima; GET acotados sin credenciales y con TLS, máximo tres lectores. G1 web Home/búsqueda/filtros: 503 CATALOG_TIMEOUT (aprox. 9,5 s); BFF directo: sin respuesta dentro de 20 s. No se identifica la causa, SHA o configuración activa sin evidencia OPS. G6: categorías 200 (ocho), listado 200 (cuatro; 12,2 s), marcas 503, precioMin=0 503 SERVICIO_NO_DISPONIBLE. Son observaciones puntuales, no un SLA. No conservar filtros 404 ni UNCONFIGURED del sondeo anterior como diagnóstico actual.

Andrés/Fernando verifican runtime/readiness/logs, SHA FE/BFF, destino Next y configuración efectiva de auth, contrato, medios y presupuestos; Giuliano prueba el recorrido publicado. El host slzglmtiyrzygpkiuthf.supabase.co continúa autorizado sólo para ensayo local hasta confirmación/aprobación remotas. El objetivo G6 de cinco segundos sigue pendiente de acreditación.

## Reproducir y completar la aceptación

1. Reutilizar scripts y comandos de [la evidencia del 03/11](H4-GIULIANO-F008-2026-11-03.md), con el SHA/modo realmente ensayados. No ejecutar contra BD/secretos productivos.
2. Registrar por caso: criterio, SHA FE/BFF/contrato/proveedor, URL/entorno, configuración sanitizada, entrada lógica, esperado, observado, estado PASS/FAIL/BLOCKED/INCONCLUSIVE, correlación y revisor. No publicar tokens/cookies/PII.
3. Separar fixture, doble HTTP, G6 REAL local, otro origen de red y G1 publicado. Los CI de #273/#275 incluyen pruebas sintéticas; #132 aporta una prueba viva local/CI. Ninguno declara por sí solo producción aceptada.
4. Giuliano: consumidor/QA; Vicuz/Taxonomy: marcas; Gabriel/Catalog y Leonardo/Pricing: precio/datos; Marco: Gateway; Andrés/Fernando: publicación; Sebastián: revisión.
5. Atender observaciones y cerrar cada issue que cumpla su DoD; registrar explícitamente el pendiente de las demás.

## Procedencia

Reconciliación documental y lectura de API GitHub/código/CI existentes; no se ejecutaron suites de aplicación nuevas para esta edición de Markdown. Sondeo de sólo lectura descrito arriba. IA: Codex para contrastar fuentes y preparar documentación; aceptación humana independiente pendiente. Los informes privados de la raíz y .local-private no forman parte de esta entrega.
