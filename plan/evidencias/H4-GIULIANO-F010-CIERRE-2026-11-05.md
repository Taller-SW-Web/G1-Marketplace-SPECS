# F010 — cierre por tarea al 05/11/2026

Responsable: Giuliano. Revisor principal asignado: Sebastián. Esta actualización documenta trabajo entregado y requisitos de cierre; no cambia el DoD, los responsables ni las dependencias. Son seis tareas trabajadas, no seis implementaciones ausentes.

## Ya realizado y qué permanece

**Entregado:** Paginación G1 cero basada → G6 uno basada, límites/tamaño, totales, recuperación fuera de rango y conservación/reset de criterios.

**Evidencia REAL disponible:** Reensayo local del 04/11: siete casos PASS de paginación, incluidas primera/siguiente/última/fuera de rango y límites inválidos. No acredita el G1 publicado.

**Retirado de pendientes actuales:** No falta escribir de nuevo la paginación ni conseguir una primera prueba REAL local: ya existe. Falta acreditar el corte publicado y su aceptación.

**Frontera restante de la función:** Repetir con universo G6 conocido: total, páginas/extremos y ausencia de duplicados observados; verificar desde UI publicada reset y criterios de URL, OPEN-03 y revisión. No presumir snapshot global entre solicitudes.

## Matriz individual de las seis issues

| Tarea / issue | Commit individual original | Incorporado a develop | Qué falta para cerrar esta tarea |
| --- | --- | --- | --- |
| [TASK-F010-FE-001](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/35) | [bf810b7e29](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/bf810b7e299c0ff595143cb252d271e9c9d1f1e8) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Registrar la aceptación de los criterios FE de esta tarea con Sebastián (estados, props/eventos, desktop/mobile y navegación/URL aplicables) y de su dependencia OPS. El merge revisado por Jim ya está acreditado. Los pendientes de integración de la función no se convierten en falta de implementación del componente. |
| [TASK-F010-BE-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/60) | [33caa34a33](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/33caa34a33d3b09270a0f78ef87e37fb52f53e9f) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Registrar la aceptación del DoD Backend y dependencia OPS con el revisor asignado: DTO, validación, errores y proyección/ownership probados. Jim ya aprobó el merge; Leónidas revisó el alcance MOCK. Los casos REAL pendientes pertenecen al cierre de INT; no exigir reescribir el adaptador ya entregado. |
| [TASK-F010-INT-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/61) | [a51edffe9f](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/a51edffe9fb881de5e1db7e5f14807d1f772f785) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Repetir con universo G6 conocido: total, páginas/extremos y ausencia de duplicados observados; verificar desde UI publicada reset y criterios de URL, OPEN-03 y revisión. No presumir snapshot global entre solicitudes. Confirmar configuración/acceso del entorno: public-read-only explícito tras integrar #273, o JWT con grant/emisión verificados. JWT no es un prerrequisito técnico del modo público acordado. Conservar las dependencias formales originales de esta INT. |
| [TASK-F010-QA-001](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/36) | [237cc57aa6](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/237cc57aa679523dd52e2b85df19b88e5b56a6ce) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Completar y revisar la matriz por criterio de esta QA con Sebastián/QA, incluyendo el recorrido REAL y los casos pendientes de la función en el entorno acordado. Repetir con universo G6 conocido: total, páginas/extremos y ausencia de duplicados observados; verificar desde UI publicada reset y criterios de URL, OPEN-03 y revisión. No presumir snapshot global entre solicitudes. Las pruebas locales/fixtures ya ejecutadas permanecen como evidencia y no se repiten por rutina. |
| [TASK-F010-QA-002](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/62) | [693e9ad0b1](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/693e9ad0b15b0666fd18b205c04f6a41f7f83365) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Adjuntar/revisar negativos del corte y SAST/SCA/secret scan ya existentes; completar DAST aplicable y revisión de riesgos con Andrés/seguridad en entorno propio/autorizado, corregir/reprobar hallazgos y acreditar la dependencia OPS de la tarea. No confundir controles locales/CI con aceptación de staging. |
| [TASK-F010-DOC-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/63) | [87f7d4fd57](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/commit/87f7d4fd57f39178c91375f7d6e334ab3f62d9ee) | No; documento entregado en SPECS #16 | Revisión independiente y merge de esta actualización en SPECS #16; coherencia de fuentes/specs/evidencias y dependencias INT/QA funcional/QA seguridad originales satisfechas. El texto y el commit documental ya están entregados; no falta redactar la tarea desde cero. |

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

1. Reutilizar scripts y comandos de [la evidencia del 03/11](H4-GIULIANO-F010-2026-11-03.md), con el SHA/modo realmente ensayados. No ejecutar contra BD/secretos productivos.
2. Registrar por caso: criterio, SHA FE/BFF/contrato/proveedor, URL/entorno, configuración sanitizada, entrada lógica, esperado, observado, estado PASS/FAIL/BLOCKED/INCONCLUSIVE, correlación y revisor. No publicar tokens/cookies/PII.
3. Separar fixture, doble HTTP, G6 REAL local, otro origen de red y G1 publicado. Los CI de #273/#275 incluyen pruebas sintéticas; #132 aporta una prueba viva local/CI. Ninguno declara por sí solo producción aceptada.
4. Giuliano: casos/UI/evidencia; G6: dataset/versión/universo; Andrés/Fernando: publicación; Sebastián/Leónidas: revisión aplicable.
5. Atender observaciones y cerrar cada issue que cumpla su DoD; registrar explícitamente el pendiente de las demás.

## Procedencia

Reconciliación documental y lectura de API GitHub/código/CI existentes; no se ejecutaron suites de aplicación nuevas para esta edición de Markdown. Sondeo de sólo lectura descrito arriba. IA: Codex para contrastar fuentes y preparar documentación; aceptación humana independiente pendiente. Los informes privados de la raíz y .local-private no forman parte de esta entrega.
