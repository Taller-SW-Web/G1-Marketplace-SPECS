# Plan de trabajo — Giuliano — H3, semanas 7–8

Alcance indicado por Giuliano: únicamente hasta la semana 8. Este plan cubre F-006/F-007 y la base compartida necesaria para su entrega. El estado de ejecución se consulta en los archivos de seguimiento y en la [evidencia H3](../evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md).

Trabajar en ramas independientes por repositorio, crear commits y subir únicamente esas ramas. No modificar main ni abrir PR; Giuliano preparará los PR manualmente.

## 1. Entrega y responsabilidades

| Funcionalidad | Resultado esperado | Responsable / revisor |
|---|---|---|
| F-006 | Inicio público, categorías activas y destacados vacíos sin selección homologada | Giuliano / Sebastian |
| F-007 | Búsqueda pública por texto, resultados mínimos y recuperación de errores | Giuliano / Sebastian |

Giuliano desarrolla Frontend y BFF propio de Marketplace. Leonidas revisa contrato/adaptador; Andres coordina entorno, seguridad y despliegue; Fernando revisa composición visual; Diego verifica evidencias y Jim acepta el resultado. Cada integrante conserva la implementación de su propio bloque.

La ruta que debe acreditar H3 es **usuario → frontend desplegado → BFF desplegado → API real de Productos**. Login, carrito y ficha no son requisitos previos para consultar el catálogo público.

## 2. Secuencia hasta la semana 8

| Semana | Trabajo | Evidencia necesaria |
|---|---|---|
| 7 | Revisar contratos, preparar ramas, base React/Next/TypeScript, componentes compartidos y lecturas BFF | Código ejecutable, configuración documentada y pruebas locales |
| 7 | Implementar inicio y búsqueda con carga, vacío y error | Recorrido web→Next→BFF probado con fixtures explícitos |
| 8 | Homologar y probar Productos real; configurar FE/BFF y CORS en el ambiente aprobado | Versión/SHA, endpoint, respuesta sanitizada y prueba real |
| 8 | Desplegar, revisar, corregir y preparar demo | URLs públicas, pipeline mínimo, arquitectura, pruebas y aceptación |

Las semanas son académicas; este documento no fija fechas de calendario ni aprueba una estimación nueva. Registrar disponibilidad y horas reales con Diego.

## 3. Fuentes y condiciones de entrada

- [Matriz de responsabilidades](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), [iteración S1](../iteraciones/S01-semanas-07-08.md), [decisiones y bloqueos](../DECISIONES-Y-BLOQUEOS.md).
- Specs funcional/UI/API/React de F-006 y F-007, V-005/V-006, [DS-001](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md) y [arquitectura React](../../SPECS/componentes-react/ARQUITECTURA-REACT.md).
- [Componentes compartidos](../../SPECS/ui/sistema-diseno/ELEMENTOS-COMPARTIDOS.md) y guías de consumo en los repositorios de código.
- I-01: contrato y revisión acordados, origen por ambiente, cliente técnico, grants, medios permitidos y datos de prueba autorizados. Secretos exclusivamente en el entorno del BFF.
- G-STACK/G-SHELL: React + TypeScript + Next App Router decidido; biblioteca UI y aceptación visual pendientes según las decisiones registradas. No presentar la propuesta local como Figma aprobado.

## 4. Inicio — F-006

- [ ] Implementar `/` con cabecera/buscador, categorías y regiones de contenido.
- [ ] Mostrar únicamente categorías activas; destacados vacíos u omitidos mientras no exista selección homologada.
- [ ] Cubrir carga por región, contenido, arreglos vacíos y error recuperable; conservar navegación y buscador operativos.
- [ ] Implementar `GET /api/v1/catalog/home`, proyectando sólo información pública y sin copiar catálogo a BD propia.
- [ ] Validar medios/datos, timeout y errores seguros; error externo no se convierte en vacío válido.
- [ ] Probar escritorio, móvil, teclado y estados; registrar evidencia MOCK y REAL por separado.

## 5. Búsqueda — F-007

- [ ] Implementar `/catalogo`, texto en edición separado de q aplicada y criterios en URL.
- [ ] Normalizar espacios y validar 2–120 caracteres; vacío elimina q. Enter envía una sola vez.
- [ ] Repetir validación en BFF antes de consultar al proveedor; responder 400 INVALID_SEARCH_QUERY si corresponde.
- [ ] Consumir `GET /api/v1/catalog/products` con página cero basada y tamaño inicial 24, máximo 48, para la lectura mínima de resultados.
- [ ] Proyectar DTO público, cancelar/ignorar respuestas anteriores y ofrecer reintento ante error.
- [ ] Registrar hash de búsqueda y diagnóstico sanitizado, sin token, consulta cruda ni payload privado.
- [ ] Entregar a Sebastian ProductCard/DTO y el contrato de enlace previsto; no implementar su ficha.

## 6. Base compartida del corte

- [ ] Mantener Button, TextField, EmptyState y Skeleton/LoadingState con contratos tipados y estados accesibles.
- [ ] Mantener tokens DS-001, tipografías locales y shell de inicio/búsqueda; actualizar guía e inventario al cambiar un componente.
- [ ] Revisar labels, foco visible, mensajes, contraste, zoom, teclado y responsive con los responsables.
- [ ] No simular precio, stock, favoritos, sesión ni carrito que no estén integrados.

## 7. Pruebas y evidencia

- Inicio: categorías activas, destacados omitidos, vacío/error sin romper cabecera.
- Búsqueda: límites 1/2/120/121, espacios normalizados, q vacía, cero resultados, criterios conservados y respuesta anterior ignorada.
- BFF: parámetros inválidos antes del proveedor, proyección pública, CORS, 401/403/429/5xx y timeout traducidos a error seguro.
- Ejecución: instalación reproducible, TypeScript, lint, build y pruebas de Frontend/Backend; registrar comandos y resultados reales.
- Operación: web publicada consulta BFF publicado y llega a Productos real; incluir URLs, versión/SHA, capturas/logs sanitizados y diagrama correspondiente al despliegue.

Conservar las seis tareas existentes por F-006 y F-007: FE, BE, INT, QA funcional, QA seguridad y DOC. No duplicarlas por plataforma ni marcar integración terminada por un fixture.

## 8. Cierre de H3

- [ ] Frontend y BFF desplegados con configuración/CORS aprobados y pipeline mínimo observable.
- [ ] Búsqueda intermodular real de Productos probada desde la URL pública.
- [ ] Casos positivos, negativos, vacío/error/timeout, responsive y seguridad aplicable verificados.
- [ ] Contrato, commits, arquitectura, URLs y evidencias coherentes con lo ejecutado.
- [ ] Revisión de Sebastian/Leonidas y responsables transversales; observaciones corregidas y aceptación de Jim.
- [ ] Giuliano puede explicar personalmente UI, BFF, adaptador, pruebas y dependencias pendientes.

Si I-01 o el ambiente siguen pendientes, informar el bloqueo con evidencia y continuar sólo preparación local dentro de H3. Un catálogo MOCK o un health aislado no cierran el hito.
