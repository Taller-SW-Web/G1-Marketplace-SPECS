# Trabajo independiente de Giuliano — H3, 16/10/2026

Alcance limitado a semanas 7–8, F-006/F-007 y su verificación/documentación. Autoría asistida por Codex. No se ha solicitado revisión a terceros ni abierto PR, desplegado servicios o modificado main/develop. Los recorridos funcionales son **MOCK**; la PostgreSQL temporal de CI prueba el baseline propio, no Productos REAL.

## Cambios publicados

| Repositorio | Rama y revisión | Cambio de este corte |
|---|---|---|
| Backend | `feat/s1-f006-f007-catalogo`, [63071c8](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/63071c833b7bd72f2ffbfca2f47d0695c9d9992b) | CI, controles de seguridad/inventario y smoke del ejecutable compilado; conserva baseline develop ed9582e |
| Frontend | `feat/s1-f006-f007-catalogo`, [ad7206c](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/ad7206c0c83f5845a1564f7eb03bcf727674ff5f) | CI sobre Backend público fijado a 63071c8, Chromium en CI/Edge local, controles y claridad del ID Figma; conserva baseline main 0f47537 |
| SPECS | `docs/giuliano-elementos-compartidos` | Seguimiento, evidencia, [entrega/demo/trazabilidad](../../entrega/H3-GIULIANO.md), tres borradores manuales de PR y workflow de enlaces; conserva main a8c3a7e |

Las guías operativas están en [Backend/docs/CI-H3.md](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/63071c833b7bd72f2ffbfca2f47d0695c9d9992b/docs/CI-H3.md) y [Frontend/docs/CI-H3.md](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/ad7206c0c83f5845a1564f7eb03bcf727674ff5f/docs/CI-H3.md). Los scripts/reglas comunes son iguales en ambos repositorios; no se añaden dependencias a la aplicación.

## Ejecución local observada

Entorno: Windows, Node **22.18.0**, npm **11.13.0**, Python nativo **3.13.3**, Semgrep CE **1.181.0**, Gitleaks **8.30.1**. Datos sintéticos; sin conexión ni escaneo de terceros. Las ejecuciones ocurrieron durante la preparación de los commits anteriores; el campo head de los reportes locales corresponde al commit previo y no certifica un árbol Git limpio. CI identifica el commit publicado exacto.

| Comando / comprobación | Resultado |
|---|---|
| BE npm run build / lint / prisma:validate | Pasaron; Prisma Client generado, TypeScript y esquema válidos |
| BE npm test | **34** pruebas aprobadas: 32 catálogo/proveedor + 2 health del baseline |
| BE npm run test:e2e | **19** aprobadas: 13 catálogo/AppModule + 6 health del baseline |
| BE node scripts/smoke-h3.mjs | **6** comprobaciones aprobadas contra `dist/main.js`: liveness, readiness 503 sin BD, catálogo/cabeceras/CORS, origen sin concesión, queries inválidas y q ausente de logs |
| FE npm run lint / build / typecheck | Pasaron con tipos de build generados |
| FE npm run test:components | **10** aprobadas |
| FE npx playwright test, después del build | **16** aprobadas en Edge contra Next y Nest compilados, incluyendo responsive 1440/390/320, errores, URL, carrera de respuestas y XSS como texto |
| Scripts security-check.py en BE y FE | Controles positivos de Semgrep/Gitleaks, secretos de snapshot/historial/artefacto, SAST, SCA e inventario finalizaron correctamente tras las correcciones descritas abajo |
| YAML | Tres workflows analizados con ruamel.yaml; acciones fijadas a SHA y permisos contents:read |
| Git | Diff sin errores de whitespace; next-env.d.ts de FE conservado byte a byte y excluido del commit; archivos centrales del baseline BE sin cambios |

La prueba de humo usa loopback 10101 y detiene su proceso. Las pruebas de navegador usan 3100/10100 y detienen sus servidores. Ninguna prueba aplica migraciones a una BD del equipo. No se cambiaron bootstrap, módulos health/Prisma, esquema, migraciones, SQL, package.json/lock ni Render del baseline Backend.

## Seguridad y hallazgos

| Control | Backend local | Frontend local | Límite |
|---|---|---|---|
| SAST Semgrep, cuatro reglas locales | 21 archivos TS/JS, 0 coincidencias y 0 errores | 23 archivos TS/JS, 0 coincidencias y 0 errores | `src` + `scripts`; ejecución dinámica, HTML, TLS, shell; no auditoría exhaustiva ni análisis interarchivo |
| Gitleaks snapshot Git | 0 hallazgos finales | 0 hallazgos finales | Archivos versionados y nuevos no ignorados; no .env privado/node_modules |
| Gitleaks historial | 0 hallazgos en develop ed9582e..HEAD preparado | 0 hallazgos en main 0f47537..HEAD preparado | CI repite contra el HEAD publicado, sin omitir comentarios de exclusión |
| Gitleaks artefactos | `dist`: 0 | `.next/static`: 0 | No equivale a escanear todos los secretos de la infraestructura |
| npm audit completo | **19 moderadas dev**, 0 altas/críticas | 0 vulnerabilidades | Gate high/critical aprobado; moderadas sin aceptación humana todavía |
| npm audit --omit=dev | 0 vulnerabilidades | 0 vulnerabilidades | Estado de la base de advisories al ejecutar; no garantía permanente |
| Inventario licencias | 639 entradas, 0 UNKNOWN | 267 entradas, 0 UNKNOWN | Inventario Windows; CI puede incluir otras opcionales. No aprobación legal |

Se conservan reportes locales sanitizados y copias de los reportes finales de CI en [H3-AUTONOMIA-2026-10-16](H3-AUTONOMIA-2026-10-16/README.md). Los scripts capturan JSON/stdout crudos en temporal y exportan sólo metadatos permitidos; nunca Match/Secret/snippets/email. Los artefactos remotos tienen retención **7 días**; los resúmenes versionados mantienen la evidencia básica después de expirar. Los ZIP descargados de CI se verificaron contra el digest SHA-256 de GitHub antes de copiar únicamente summary/licenses/smoke; no se versionan ZIP ni enlaces temporales de descarga.

Incidencias de la preparación y retest:

- Semgrep no pudo acceder inicialmente al almacén de certificados dentro del sandbox de Windows. Se ejecutó con los permisos del entorno aprobados, sin desactivar TLS. Su control positivo y el análisis final pasaron.
- El primer control sintético de Gitleaks era una cadena repetida que no activaba el detector; esa ejecución se marcó fallida. Se sustituyó por un valor aleatorio temporal sin cuenta ni servicio y se verificó la detección antes de aceptar los scans.
- Gitleaks señaló `generic-api-key` en `public/figma/manifest.json:2`: era el ID de archivo presente en el enlace Figma suministrado por Giuliano, campo `fileKey`, no una credencial. Se renombró el metadato a **figmaFileId**, sin cambiar su valor, assets ni hashes; ningún consumidor de aplicación usa ese campo. Se repitió el scan completo: cero hallazgos, sin allowlist ni exclusión de regla. La interpretación se deja disponible para revisión humana.
- El inventario inicial no reconocía las declaraciones legacy `licenses` de busboy/streamsearch. Se añadió lectura de ese formato; los manifests y LICENSE instalados declaran MIT. El retest eliminó los dos UNKNOWN sin modificar paquetes.

Las **19 moderadas heredadas** están en el árbol de Jest (incluye js-yaml, argparse y sprintf-js). Se propone responsable de evaluación Leonidas/seguridad y revisión **antes de aceptar el PR Backend**; asignación y riesgo aún no aceptados por humanos. No se ejecutó audit fix/force. La coincidencia con el baseline se respalda en la igualdad de package.json/lock y en la [auditoría anterior](H3-ADAPTACION-BASELINE-NESTJS-2026-10-15.md). El inventario FE incluye expresiones LGPL/MPL y fuentes OFL; requiere revisión del uso/distribución según licencia, sin inferir incompatibilidad ni aceptación automática.

Los negativos unitarios/HTTP/navegador prueban límites, DTO público, medios permitidos, redirect/timeout, errores sin detalles internos, logs sin q y render de XSS como texto. El smoke es **validación dinámica dirigida local**, no DAST baseline de staging. DAST staging sigue pendiente de un destino propio y coordinación operativa. No se han escaneado G6, Figma, GitHub ni entornos de otros grupos.

## CI remoto y trazabilidad de ejecución

La primera ejecución de Backend sobre [f9349c3](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/38854461076) **terminó con éxito**: instalación, build/tipado, 34+19 pruebas, Prisma validate, migración inicial en PostgreSQL 16 temporal, smoke con readiness UP, herramientas/controles y artefacto sanitizado. El ajuste posterior de licencias no altera aplicación, schema ni dependencias; tiene nueva ejecución sobre 63071c8.

Las dos revisiones finales de código **terminaron con éxito en GitHub Actions**. Se comprobaron sus conclusiones, commits y reportes descargados. Las copias `*-ci-summary.json` incluyen passed=true y el SHA correspondiente; `backend-ci-smoke.json` confirma readiness con BD temporal. Los inventarios Linux tienen también 639 entradas BE y 267 FE, sin UNKNOWN.

| Repositorio | Revisión | Ejecución final |
|---|---|---|
| Backend | 63071c8 | [Run 38854701659 — success](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/38854701659), incluido PostgreSQL/migración/readiness y controles |
| Frontend | ad7206c | [Run 38854728651 — success](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/38854728651), incluidos Chromium, 16 E2E y controles |
| SPECS | e6cb4e9, publicación inicial de esta evidencia | [Run 38855080128 — success](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/actions/runs/38855080128), 26 Markdown / 189 destinos / 0 ausentes en Ubuntu |

El validador de SPECS comprobó localmente **26 Markdown modificados, 189 destinos relativos y 0 ausentes** al preparar el paquete. Sólo analiza enlaces inline locales fuera de bloques de código en documentos cambiados desde main a8c3a7e: no verifica disponibilidad de URLs externas, anclas ni toda la documentación del equipo.

La comprobación final confirmó ramas propias sincronizadas (0 commits por subir/bajar), Backend y SPECS limpios y Frontend únicamente con el next-env.d.ts preexistente, conservado byte a byte. Los refs remotos compartidos siguen en BE main d98b01c/develop ed9582e, FE main 0f47537 y SPECS main a8c3a7e. No se abrió PR. Esta anotación documental vuelve a pasar el mismo workflow al publicarse; el enlace anterior identifica la ejecución observada del paquete inicial.

## Estado y pendientes

TASK-F006/F007-QA-002 y DOC-001 pasan a **En progreso** porque ya existen controles/documentación ejecutables y evidencia. FE/BE/QA-001 mantienen En progreso hasta revisión. INT sigue **Bloqueado** por I-01. No se cambia ningún ID, se completa una revisión en nombre de otro integrante ni se declara Terminado.

Quedan coordinación/configuración y prueba **REAL** de Productos, G-FEATURED/campos comerciales según contrato, URLs de despliegue propias, DAST staging, revisión independiente, aceptación de riesgo/licencias y aceptación H3. La [guía de entrega](../../entrega/H3-GIULIANO.md) especifica responsables propuestos y evidencia de salida. No se desarrollan funciones posteriores a semana 8.
