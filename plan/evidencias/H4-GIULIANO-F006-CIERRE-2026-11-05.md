# F006 — cierre por tarea al 05/11/2026

Responsable: Giuliano. Revisor principal asignado: Sebastián. Esta actualización documenta trabajo entregado y requisitos de cierre; no cambia el DoD, los responsables ni las dependencias. Son seis tareas trabajadas, no seis implementaciones ausentes.

## Ya realizado y qué permanece

**Entregado:** Home/categorías/tarjetas y estados; prioridad definidos → históricos → aleatorios ante ausencia de historial comprobada; puerto de ranking, revalidación G6 y tres caminos probados con datos sintéticos.

**Evidencia REAL disponible:** Categorías G6 públicas 200 (ocho). El ensayo REAL de categorías/listado no acredita ranking real ni destacados omitidos.

**Retirado de pendientes actuales:** La prioridad y la métrica ya están decididas. No volver a pedir una definición inicial de destacados; queda su fuente real y aceptación operativa.

**Frontera restante de la función:** Conectar el adaptador real de ranking: G5 confirma fuente/contrato, pagos/devoluciones, mapping SKU→producto y acceso; Giuliano implementa y prueba. Validar selección/operación con Jim/PO y el recorrido REAL de Home, incluido favorito/autenticación aplicable.

## Matriz individual de las seis issues

| Tarea / issue | Commit individual original | Incorporado a develop | Qué falta para cerrar esta tarea |
| --- | --- | --- | --- |
| [TASK-F006-FE-001](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/27) | [aee8dcd296](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/aee8dcd296ea15be4773ee6922fb54d0e6e6ec01) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Registrar la aceptación de los criterios FE de esta tarea con Sebastián (estados, props/eventos, desktop/mobile y navegación/URL aplicables) y de su dependencia OPS. El merge revisado por Jim ya está acreditado. Los pendientes de integración de la función no se convierten en falta de implementación del componente. |
| [TASK-F006-BE-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/44) | [01c0882fc3](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/01c0882fc3bb295437cfe98cb2c4c4ee5345e5c6) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Registrar la aceptación del DoD Backend y dependencia OPS con el revisor asignado: DTO, validación, errores y proyección/ownership probados. Jim ya aprobó el merge; Leónidas revisó el alcance MOCK. Para completar la nueva política REAL de Home sigue faltando el adaptador de ranking; el puerto y las pruebas sintéticas ya existen. |
| [TASK-F006-INT-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/45) | [c3271c8146](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/c3271c8146f90ac35f5a2b64311fa449c2986a83) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Conectar el adaptador real de ranking: G5 confirma fuente/contrato, pagos/devoluciones, mapping SKU→producto y acceso; Giuliano implementa y prueba. Validar selección/operación con Jim/PO y el recorrido REAL de Home, incluido favorito/autenticación aplicable. Confirmar configuración/acceso del entorno: public-read-only explícito tras integrar #273, o JWT con grant/emisión verificados. JWT no es un prerrequisito técnico del modo público acordado. Conservar las dependencias formales originales de esta INT. |
| [TASK-F006-QA-001](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/28) | [0897f9c08d](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/0897f9c08d4f3638453b14a7d9c00f927506a415) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Completar y revisar la matriz por criterio de esta QA con Sebastián/QA, incluyendo el recorrido REAL y los casos pendientes de la función en el entorno acordado. Conectar el adaptador real de ranking: G5 confirma fuente/contrato, pagos/devoluciones, mapping SKU→producto y acceso; Giuliano implementa y prueba. Validar selección/operación con Jim/PO y el recorrido REAL de Home, incluido favorito/autenticación aplicable. Las pruebas locales/fixtures ya ejecutadas permanecen como evidencia y no se repiten por rutina. |
| [TASK-F006-QA-002](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/46) | [fa1ed63dd7](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/fa1ed63dd7c7421b56f92e6d61a21581eb8d52c2) | Entrega incorporada por squash de PR; SHA individual conservado en rama | Adjuntar/revisar negativos del corte y SAST/SCA/secret scan ya existentes; completar DAST aplicable y revisión de riesgos con Andrés/seguridad en entorno propio/autorizado, corregir/reprobar hallazgos y acreditar la dependencia OPS de la tarea. No confundir controles locales/CI con aceptación de staging. |
| [TASK-F006-DOC-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/47) | [54b3a9af31](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/commit/54b3a9af31771b508f19a5ac034ca3f53697bc48) | No; documento entregado en SPECS #16 | Revisión independiente y merge de esta actualización en SPECS #16; coherencia de fuentes/specs/evidencias y dependencias INT/QA funcional/QA seguridad originales satisfechas. El texto y el commit documental ya están entregados; no falta redactar la tarea desde cero. |

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

1. Reutilizar scripts y comandos de [la evidencia del 03/11](H4-GIULIANO-F006-2026-11-03.md), con el SHA/modo realmente ensayados. No ejecutar contra BD/secretos productivos.
2. Registrar por caso: criterio, SHA FE/BFF/contrato/proveedor, URL/entorno, configuración sanitizada, entrada lógica, esperado, observado, estado PASS/FAIL/BLOCKED/INCONCLUSIVE, correlación y revisor. No publicar tokens/cookies/PII.
3. Separar fixture, doble HTTP, G6 REAL local, otro origen de red y G1 publicado. Los CI de #273/#275 incluyen pruebas sintéticas; #132 aporta una prueba viva local/CI. Ninguno declara por sí solo producción aceptada.
4. Giuliano: consumidor/pruebas; Michael, Joseph y Luis Alejandro (G5): agregado y semántica; Jim/PO: selección/aceptación; Leónidas: revisión técnica; OPS: publicación.
5. Atender observaciones y cerrar cada issue que cumpla su DoD; registrar explícitamente el pendiente de las demás.

## Procedencia

Reconciliación documental y lectura de API GitHub/código/CI existentes; no se ejecutaron suites de aplicación nuevas para esta edición de Markdown. Sondeo de sólo lectura descrito arriba. IA: Codex para contrastar fuentes y preparar documentación; aceptación humana independiente pendiente. Los informes privados de la raíz y .local-private no forman parte de esta entrega.
