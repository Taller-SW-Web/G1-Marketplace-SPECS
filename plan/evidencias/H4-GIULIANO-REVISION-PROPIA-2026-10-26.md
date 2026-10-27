# H4 — revisión propia de catálogo e inicio

Giuliano, 26/10/2026, rama `feat/giuliano-hito4`. Continuación de la [evidencia del bloque F-006–F-010](H4-GIULIANO-2026-10-26.md). Este corte contiene correcciones propias y preparación de demo; no revisa ni aprueba código de otros integrantes.

## Cambios verificables

| Commit Frontend | Resultado |
|---|---|
| `fd0b499` | Panel y barra de resultados desktop, filtros/orden de ancho completo mobile, iconos Figma, contador accesible de criterios aplicados, correcciones de foco y cuatro pruebas adicionales |
| `ea31091` | Comando de demo sintética aislada, ampliación de regresiones/capturas en CI y documentación |

La revisión consultó contexto y screenshots de los nodos inicio [274:111](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p?node-id=274-111), [274:293](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p?node-id=274-293), catálogo [339:881](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p?node-id=339-881) y [339:1026](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p?node-id=339-1026). No se localizó un frame llamado O-001 en las páginas de catálogo/overlays consultadas; el comportamiento del modal se verificó contra su spec y conserva revisión humana pendiente.

Se corrigieron dos defectos de foco: quitar el chip de búsqueda y aplicar filtros móviles sin cambios. La regresión de quitar búsqueda falló antes de la corrección y pasó después. También se corrigió la visibilidad del disparador móvil en desktop, detectada al inspeccionar las capturas, y se añadió su comprobación.

## Verificación de este corte

| Comprobación | Resultado |
|---|---|
| Tipos Frontend | PASS |
| Componentes/DTO/estado | 225 PASS en 28 archivos |
| Lint | Sin errores; un warning previo en `OrdersHistory.tsx` |
| Build Next de producción | PASS, repetido tras la última corrección CSS |
| Playwright H3 + H4 + revisión propia | 21 PASS, Next → BFF MOCK |
| Demo `npm run demo:catalogo:h4 -- --check` y variante `--skip-build` | Ambas PASS: compilación de ambos repos en el comando completo, home/filtros/búsqueda por Next → BFF y procesos propios cerrados |
| YAML CI | Parseado; limitado a la rama propia y con la suite visual incluida |
| Seguridad final, fuente/historial de los dos commits/artefacto `.next/static` | PASS: secretos, cuatro reglas SAST, controles positivos y SCA runtime/dev con cero vulnerabilidades; [metadatos saneados](H4-GIULIANO-REVISION-PROPIA-2026-10-26/frontend-security.json) |
| CI remoto del HEAD `ea31091` | [Run #40436511585](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/actions/runs/40436511585) SUCCESS: lint, componentes, servidor, build/tipos, Chromium, 21 recorridos y seguridad; [metadatos](H4-GIULIANO-REVISION-PROPIA-2026-10-26/frontend-ci.json) |

No hubo cambios de Backend ni de lógica del proxy servidor; sus pruebas del corte previo mantienen el alcance registrado en la evidencia anterior. Los 21 recorridos incluyen cuatro nuevos; no sumar ambas corridas como casos distintos.

Capturas de inicio/catálogo a 1440/390 px, error/vacío y rango inválido en `test-results/h4-visual-*.png`, ignoradas por Git y configuradas como artefacto de CI. Se comprobó ausencia de desbordamiento horizontal a 320 px. Las capturas no equivalen a una comparación pixel a pixel ni a una auditoría completa de accesibilidad.

## Alcance y pendientes

La demo se ejecuta desde Frontend mediante `npm run demo:catalogo:h4`: compila ambos repos, usa Next 3500/BFF 10500 y datos MOCK explícitos. No cambia `.env`, no usa credenciales reales y no escribe en BD. `/live` no acredita readiness de PostgreSQL.

No se habilitaron precio/disponibilidad en tarjetas, órdenes ni multiselección sin soporte contractual. Curaduría de destacados, identidad técnica G1–G6/G7, marcas/filtros/orden/páginas estables en G6, aprobación visual independiente, despliegue/CD y DAST conservan sus gates. No se repitió integración REAL en este corte ni se cerraron issues.

Los dos commits de Frontend se publicaron en `origin/feat/giuliano-hito4`, sin PR. El CI de esta rama no ejecuta despliegue. Los planes e informes personales permanecen locales, ignorados y sin seguimiento por Git.
