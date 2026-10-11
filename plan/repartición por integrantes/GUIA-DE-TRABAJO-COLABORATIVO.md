# Guía de trabajo colaborativo — semana 8

Aplica a los repos de [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend), [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend) y [SPECS](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS). No crear una base de código dentro de SPECS. Esta política es **propuesta S1**: Diego/PO confirman protección y permisos reales en GitHub antes de usarla. No se han creado ramas ni PR por este documento.

## Ramas, PR y propiedad de archivos

1. `main` queda como rama estable. Diego crea/protege `develop` desde `main` en cada repo de código si aún no existe, sin reescribir historial; `develop` será la base de integración S1. Si la protección exige otra política, acordarla antes del primer PR y actualizar aquí.
2. Cada persona crea desde `develop` una rama corta `feat/s1-<id>-<tema>`, `fix/s1-<id>-<tema>`, `test/s1-<id>-<tema>`, `docs/s1-<id>-<tema>` o `chore/s1-<id>-<tema>`. Ejemplos: `feat/s1-f007-resultados`, `feat/s1-f007-bff`, `test/s1-f006-f007-e2e`. Una rama por repo y unidad revisable, no una rama eterna por persona.
3. Antes de codificar, abrir issue/tarea con ID de `plan/seguimiento`, alcance, archivos previstos, dependencia y criterio de prueba. Giuliano es dueño de shell/buscador compartido; Fernando de Home; Sebastian de resultados/cliente; Leonidas de rutas/adaptador; Andres de configuración/deploy; Diego de suite E2E; Jim de test consumidor. Avisar en issue antes de tocar archivos de otro dueño.
4. Integrar en este orden cuando aplique: base/contratos de FE/BE → componentes y adaptador en paralelo → pruebas → deploy. Abrir PR **hacia `develop`** en cuanto exista un corte revisable, incluso si está en borrador. Actualizarlo frecuentemente desde `develop` sin sobrescribir cambios ajenos. PR pequeño, con tests y captura cuando afecte UI.
5. Revisor distinto del autor según [matriz](README.md). Cambios de contrato o seguridad requieren también a Leonidas/Andres; UX a Giuliano/Fernando; aceptación funcional a Jim; gate de pruebas a Diego. Aprobar antes de fusionar; el autor no se autoaprueba. Preferir squash merge sólo si la política del equipo lo acepta y conserva autoría/evidencia.
6. Hacia el corte H3, Diego abre PR `develop` → `main` con release verificable. No fusionarlo ni afirmar entrega hasta que pasen pruebas, deploy y validación de Jim. Si la integración externa está pendiente, se registra explícitamente y no se etiqueta como completa.

## Conventional Commits en español

Formato `tipo(alcance): descripción en español`, verbo en infinitivo y sin punto final. Tipos: `feat`, `fix`, `docs`, `test`, `refactor`, `chore`, `ci`, `build`. Ejemplos: `feat(catalogo): implementar búsqueda por texto`, `test(integracion): cubrir respuesta vacía de Productos`, `ci(despliegue): validar build del frontend`. No subir `.env`, claves, tokens, datos personales, capturas con secretos ni logs crudos. Un commit no sustituye el PR ni la evidencia de ejecución.

## Definition of Ready, Done y bloqueo

- **Ready:** leer specs funcional/UI/API/React y mockup correspondiente; fijar versión/SHA del contrato externo; confirmar archivos compartidos, estimación, responsable y revisor. Dependencias I-01/G-STACK/G-SHELL visibles.
- **Done local:** build/typecheck/lint/test pertinentes, estados positivos/negativos, accesibilidad y responsive del alcance, revisión independiente, evidencia de comando y resultado. Fixture = `MOCK`, no integración real.
- **Done H3:** lo anterior **más** URL pública FE y BE, llamada web→BFF→Productos con datos remotos, logs/capturas saneados, diagrama conforme a lo desplegado y aprobación de PO/JP. Si falta URL/grant/datos de Productos, dejar INT bloqueada y avisar de inmediato; no desactivar una prueba para pasar el gate.
- No leer BD de Productos ni almacenar su catálogo en BD Marketplace. El token técnico y secretos quedan sólo en backend. CORS no debe quedar en `*` para el entorno final. Registrar errores/timeout sin exponer detalles internos.

## Seguimiento, evidencia y uso de IA — obligatorio para **cada** integrante

Cada autor actualiza la tarea correspondiente en `plan/seguimiento`, enlaza su issue/PR/commit y guarda en el PR o en `docs/evidencias/h3/` del repo de código una nota Markdown propia. Un formato breve suficiente:

```md
# Evidencia H3 — nombre — TASK-ID
Fecha / entorno / repositorio / rama / commit:
Specs leídas (IDs y versión), vista y frame Figma usados:
Trabajo manual y decisiones tomadas:
IA utilizada (herramienta/modelo si se conoce, propósito y resumen del prompt; sin secretos):
Código o pruebas generados por IA (archivos/funciones/commit) y qué revisé/corregí:
Pruebas ejecutadas (comando, casos y resultado; MOCK o REAL):
URL, petición/respuesta sanitizada, captura/log y limitaciones:
Revisor y enlace de PR:
```

No pegar prompts con credenciales ni atribuir a la IA una prueba no ejecutada. Si no se usó IA, escribir «No se usó IA». El código generado requiere lectura, adaptación a specs/mockups, pruebas y responsabilidad del autor. El PR debe explicar cualquier desviación de la spec y enlazar la decisión aprobada; no cambiar comportamiento sólo porque lo produjo la herramienta.

Hacer un check-in breve diario en el issue: hecho, siguiente, bloqueo y enlace a evidencia. Diego coordina dependencias y revisión; Jim decide alcance funcional y comunica bloqueo intermodular. Ninguno reemplaza el trabajo ni las pruebas del autor.
