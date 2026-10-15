# Catálogo de elementos compartidos — Marketplace

Versión documental **0.2.0**, 14/10/2026, **en revisión**. Custodio: Giuliano Macchiavello. Describe la base local del corte F-006/F-007 y sus componentes reutilizables; la biblioteca completa y su aceptación siguen pendientes. No cambia la versión ni las reglas de DS-001.

## 1. Fuentes y ubicación

- [DS-001 v0.2.0](../DS-001-sistema-diseno-marketplace.md): autoridad de marca, tokens, accesibilidad y gobernanza.
- [Arquitectura React](../../componentes-react/ARQUITECTURA-REACT.md): composición, separación de datos y contratos compartidos.
- [Matriz de responsabilidades](../../RESPONSABILIDADES-PUNTA-A-PUNTA.md): responsables de implementación y revisión.
- [O-010](../overlays/O-010-alertas-feedback-global.md): feedback transversal completo; no se considera implementado por tener una alerta de catálogo.
- [Evidencia local](../../../plan/evidencias/H3-GIULIANO-CATALOGO-2026-10-14.md): comprobaciones ejecutadas y límites.
- [Changelog de esta documentación](CHANGELOG-COMPARTIDOS.md).

| Repositorio | Documento o carpeta | Propósito |
|---|---|---|
| SPECS | Este archivo | Inventario, responsabilidades, decisiones y brechas |
| Frontend | [docs/ELEMENTOS-COMPARTIDOS.md](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/feat/s1-f006-f007-catalogo/docs/ELEMENTOS-COMPARTIDOS.md) | Imports, props reales, ejemplos y restricciones de uso |
| Frontend | `src/shared/ui/` | Shell y feedback reutilizado por el corte actual |
| Frontend | `src/features/catalog/` | Tarjeta, buscador, tipos y lógica compartidos dentro de catálogo |
| Frontend | `src/theme/tokens.css`, `src/app/globals.css` | Tokens implementados y estilos locales |
| Backend | [docs/ELEMENTOS-COMPARTIDOS.md](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/feat/s1-f006-f007-catalogo/docs/ELEMENTOS-COMPARTIDOS.md) | Contratos y utilidades comunes del BFF de catálogo |

Los documentos de código permanecen en sus repositorios. Se indican rutas relativas y de checkout para facilitar el consumo; las ramas de trabajo se publican por instrucción de Giuliano y sus enlaces se registran en la evidencia. El hecho de que un archivo se encuentre en `features/catalog` no autoriza duplicarlo dentro de otro módulo.

## 2. Foundations implementadas y pendientes

La implementación actual traduce un **subconjunto de 24 variables CSS**, no el sistema completo:

| Grupo | Variables CSS implementadas | Referencia DS-001 |
|---|---|---|
| Acción | `--action-primary`, `--action-hover`, `--action-soft` | `color/action/primary`, `primary-hover`, `primary-soft` |
| Acentos | `--accent-volt`, `--accent-signal` | `color/accent/volt`, `signal` |
| Superficies | `--surface-ink`, `--surface-cloud`, `--surface-subtle` | `color/surface/ink`, `cloud`, `cloud-subtle` |
| Texto | `--text-primary`, `--text-inverse`, `--text-secondary` | Roles equivalentes de texto |
| Bordes | `--border`, `--border-inverse` | Bordes default/inverse |
| Error | `--error`, `--error-background` | Error default/background |
| Radios | `--radius-sm`, `--radius-md`, `--radius-lg`, `--radius-full` | 8 px, 12 px, 16 px, 999 px |
| Espaciado | `--spacing-xs`, `--spacing-sm`, `--spacing-md`, `--spacing-lg`, `--spacing-xl` | 4 px, 8 px, 16 px, 24 px, 32 px |

Inter 400/500/600/700 y Oswald 700 se sirven desde dependencias locales. Oswald 500, el resto de colores semánticos, escala tipográfica y otros tokens DS aún no están expuestos como una API completa de tema. El CSS conserva medidas locales que deben revisarse y normalizarse antes de aprobar la biblioteca.

Reglas de consumo:

- Usar tokens existentes para colores/estados; proponer extensiones con vistas afectadas antes de introducir nuevos roles.
- Botón principal: naranja y texto oscuro; hover naranja oscuro y texto inverso. No usar blanco sobre el naranja principal ni sobre Volt.
- Foco Signal visible, texto/ícono además del color, controles táctiles de referencia de 44 px y movimiento reducido.
- Logo Ink recibido, conservado sin modificar. SVG maestro, inverso, favicon, licencia y dimensiones de uso definitivas siguen pendientes de DS-OPEN-01.

La grilla local usa 4 columnas desde 992 px, 3 entre 768–991, 2 entre 360–767 y 1 por debajo de 360. **Es propuesta del corte**, no aprobación del ancho mínimo de tarjeta ni sustitución de los seis breakpoints de DS-001. V-006-OPEN-04 y la revisión responsive deben cerrar esa diferencia.

## 3. Inventario real del frontend

Todos los elementos siguientes existen en el checkout local. Su estado es implementación parcial con pruebas del corte, **pendiente de revisión independiente**.

| Elemento / archivo | Contrato actual | Consumo y límite |
|---|---|---|
| `Button`, `src/shared/ui/Button.tsx` | Props nativas/ref; variantes primary/secondary/tertiary, tamaños sm/md/lg, loading, iconos y fullWidth; type=button por defecto | SearchBox, reintento y limpieza de búsqueda. Loading bloquea eventos y mantiene nombre accesible; no ejecuta reglas de negocio |
| `TextField`, `src/shared/ui/TextField.tsx` | Input/ref, label, hint/error, adornos, clases de composición e IDs generados | Buscador global; label visible por defecto. Label/error/ayuda asociados y soporte de varias instancias sin IDs fijos |
| `EmptyState`, `src/shared/ui/EmptyState.tsx` | title, description, actions, icon, headingLevel 2/3 y className | Vacíos de home/listado. La condición de vacío y la recuperación permanecen en el contenedor |
| `Skeleton` / `LoadingState`, `src/shared/ui/Skeleton.tsx` | Forma block/line/circle y grupo con label, children decorativos y clase de layout | Carga de categorías y productos. Un anuncio por grupo y respeto de movimiento reducido |
| `Header`, `src/shared/ui/Header.tsx` | Sin props; logo, acceso a catálogo, salto al contenido y SearchBox bajo Suspense | Layout raíz de home/catálogo. No es todavía AppShell configurable ni header de checkout |
| `Footer`, `src/shared/ui/Footer.tsx` | Sin props; marca y enlaces Inicio/Catálogo | Layout raíz. No incluye enlaces legales/ayuda no aprobados ni variante checkout |
| `SearchBox`, `src/features/catalog/SearchBox.tsx` | Sin props; usa router/URL, TextField y Button; texto/error local y transición | Normaliza 2–120 caracteres, Enter, limpieza y reinicio de página; evita repetir navegación pendiente. No es input genérico |
| `ProductCard`, `src/features/catalog/ProductCard.tsx` | `product: ProductCardDTO`, `returnPath: string` | Home/listado; navegación por slug. Sin precio, stock ni favorito; destino de ficha pendiente de Sebastian |
| `ErrorState`, `src/shared/ui/Feedback.tsx` | `message: string`, `onRetry: () => void` | Error persistente de catálogo con anuncio y recuperación. Título/enlace están fijados a catálogo; no es O-010 genérico |
| `MockNotice`, mismo archivo | Sin props | Aviso de datos sintéticos, sólo cuando `source === 'MOCK'` |
| `ProductSkeletons`, mismo archivo | Sin props; ocho tarjetas decorativas y un estado accesible | Carga de listado. No ofrece todavía variantes para ficha, carrito o checkout |
| `CategoryChip`, `src/features/catalog/CategoryChip.tsx` | `categoryId: string`, `onRemove: () => void` | Criterio de categoría en catálogo; obtiene nombre desde home; no expone el ID opaco como etiqueta |
| `useCatalog`, `src/features/catalog/useCatalog.ts` | `path`, validador runtime; devuelve `state`, `retry` | Transporte sólo de catálogo con cancelación/errores. No es cliente de auth, checkout ni caché global |
| `isHome`, `isCatalogPage`, `readCatalog` | Validación de `unknown`, AbortSignal y proyección tipada | Límite HTTP del catálogo; no sustituye autorización del backend |

`Home`, `Catalog` y `CatalogResults` son contenedores de página. No se presentan como componentes de biblioteca.

### Relación entre estilos y componentes

| Estilo | Uso actual | Trabajo pendiente para biblioteca |
|---|---|---|
| `.button`, `.button--*` | Button tipado y CTA Link | Mantener semánticas separadas: un Link no admite disabled nativo |
| `.text-link` | Enlace secundario | Definir API de enlace y estados sin sustituir semántica nativa |
| `.field-*`, `.search-control` | TextField, adornos y composición de búsqueda | Campos/selecciones especializados aún pendientes; el contenedor controla reglas y acciones |
| `.product-grid`, `.category-grid`, `.container` | Layout del catálogo | Normalizar tokens y ancho mínimo/columnas con el diseño aprobado |
| `.empty-state`, `.skeleton` | EmptyState, Skeleton y LoadingState | Completar composiciones específicas de otras vistas con sus responsables |
| `.feedback` | ErrorState local de catálogo | Falta feedback transversal O-010 completo |

Button, TextField, EmptyState y Skeleton/LoadingState tienen APIs React implementadas y pruebas. No se declara una biblioteca completa: campos especializados, Modal y Toast/O-010 siguen pendientes. Los contratos y ejemplos exactos están en la guía de consumo del frontend.

## 4. DTO, estado y límites de datos

| Tipo implementado | Campos / significado |
|---|---|
| `Category` | `categoryId`, `name` |
| `ProductCardDTO` | `productId`, `slug`, `name`, `categoryId`, `brandId`, `image: {url, alt}` |
| `HomeDTO` | `categories[]`, `featuredProducts[]` |
| `PageMeta` | `number`, `size`, `totalElements`, `totalPages`; página API desde cero |
| `CatalogPageDTO` | `data[]`, `page` |
| `CatalogSource` | `MOCK`, `REAL`, `UNCONFIGURED`; clasifica evidencia, no elegibilidad comercial |
| `QueryState<T>` | `loading`, `ready(data,source)`, `error(message,code)` |

En el código actual el vacío es `ready` con un arreglo vacío válido; no existe una rama `empty` independiente. Un error nunca se transforma en vacío. La propuesta más general de arquitectura no implica que todos sus tipos estén implementados.

- Producto, variante y SKU son identidades distintas; la tarjeta no autoriza compra ni construye SKU.
- El contrato candidato G6 del primer corte no incluye precio/stock/nombre de marca. La tarjeta completa requiere acuerdo y enriquecimiento autorizado; no se rellenan valores ficticios.
- Los criterios aplicados viven en URL; borradores en estado local; el servidor conserva la autoridad.
- `returnPath` lo genera hoy el contenedor con una ruta relativa de catálogo. **El receptor no debe confiar en `returnTo` de una URL pública:** el validador común InternalPath todavía está pendiente y debe preceder cualquier redirección.
- No incluir token técnico, contraseñas o datos privados en props, variables públicas, logs ni cachés de catálogo.

## 5. Elementos comunes del backend

Las utilidades actuales tienen **alcance de catálogo**, no de todo Marketplace:

- `CatalogError` y `problem`: errores públicos uniformes; diagnóstico interno separado.
- `parseQuery`: normalización, límites, parámetros permitidos y rechazo antes del proveedor.
- `createProvider`: selección explícita de mock/real/no configurado; ningún fallback silencioso.
- `createRealProvider` y `projectProduct`: HTTP técnico, timeout, revisión contractual fijada, proyección pública y allowlist de medios.
- `createApp`: enrutamiento, CORS, UUID, log seguro y health inyectable; `server.js` es el punto de arranque, no una utilidad para importar desde tests o frontend.

Ninguna utilidad da acceso directo a BD de Productos, reemplaza autorización de otros módulos o implementa reglas de precio/pedido. Configuración y ejemplos están en `G1-Marketplace-Backend/docs/ELEMENTOS-COMPARTIDOS.md`.

## 6. Handoff y responsabilidad

| Persona | Coordinación concreta |
|---|---|
| Giuliano | Custodia DS-001, tokens, catálogo de elementos y coherencia del frontend; autor del corte F-006/F-007 hasta semana 8 |
| Sebastian | Revisor principal de ese bloque; recibe ProductCard/DTO/ruta de ficha y retorno; Giuliano revisa su UI de detalle |
| Fernando | Diseño de V-005/V-006 y O-010 según inventario; revisión de coherencia con el código |
| Leonidas | Revisión de contratos, DTO, adaptador y cambios de backend |
| Andres | Revisión de seguridad y coordinación de CORS/entorno/despliegue |
| Diego | Verificación, coordinación de archivos/dependencias y capacidad |
| Jim | Aceptación funcional y decisiones de shell/UI kit; revisión del paquete visual propio de Giuliano |

Revisar ownership antes de tocar archivos compartidos. En esta sesión la coordinación y revisión se dejan preparadas localmente; no se envían mensajes a terceros.

## 7. Gobernanza, versionado y revisión

1. Identificar la necesidad y las vistas consumidoras; revisar DS-001 y el inventario antes de duplicar.
2. Acordar el archivo y contrato con el responsable; distinguir diseño visual de implementación.
3. Implementar el cambio en la rama de trabajo, con props/eventos, estados y accesibilidad definidos.
4. Probar el comportamiento afectado y revisar los consumidores reales; incluir contrato público y casos negativos cuando aplique.
5. Actualizar este inventario, la guía de uso del repo y el changelog con compatibilidad, migración y evidencia.
6. Obtener revisión de las personas correspondientes antes de declarar aceptación. Tener un documento no publica ni aprueba una biblioteca.

Versiones documentales: `0.1.x` registra el inventario inicial; `0.2.0` añade APIs reutilizables e integración sin retirar exports previos. Un cambio incompatible debe explicitar migración y nueva versión de implementación. La versión de DS-001 y la versión de este documento son independientes. La biblioteca aún no se distribuye como paquete npm ni se declara DS-001 0.3.0/1.0.0.

**Política actualizada de esta sesión, por instrucción de Giuliano:** crear commits y subir las ramas de trabajo de cada repositorio; no subir a main ni abrir PR. Giuliano preparará los PR manualmente al terminar. La revisión se realiza sobre las ramas y sus diffs; las instrucciones históricas de commit directo a main no aplican a esta entrega.

## 8. Pendientes para completar la biblioteca

- [ ] Resolver G-STACK/DS-OPEN-03 y G-SHELL antes de aprobar el sistema visual implementado.
- [ ] Completar tokens y normalizar medidas locales; verificar contraste, foco, teclado, zoom y responsive de cada componente.
- [x] Implementar Button, TextField, EmptyState y Skeleton/LoadingState tipados e integrarlos en las vistas del corte; revisión humana pendiente.
- [ ] Completar campos/selecciones especializados, variantes de carga por vista y aceptación visual/accesible de la base.
- [ ] Extender ProductCard con datos comerciales autorizados y el control de favorito del bloque de Diego.
- [ ] Acordar variantes comerciales/checkout de shell con sus responsables.
- [ ] Implementar O-010 completo: severidades, cola, deduplicación, acciones, persistencia y reglas de temporización; ErrorState por sí solo no lo cubre.
- [ ] Incorporar los patrones requeridos por otros bloques cuando sus responsables los integren: galería, carrito, resumen y timelines; no atribuir todo su backend a Giuliano.
- [ ] Resolver InternalPath y la conservación segura de retorno con los flujos que lo consumen.
- [ ] Verificar frames Figma y enlazar cada variante con su spec/código/evidencia.
- [ ] Registrar revisión humana y el proceso/canal de publicación antes de considerar cerrada la gobernanza.

Verificaciones ejecutadas: 10 pruebas de componentes y 13 de navegador del frontend, más lint/TypeScript/build. Las 34 pruebas previas de backend siguen documentadas en la evidencia y ese código no cambia en este incremento. No es certificación completa de accesibilidad ni aceptación de todas las variantes de una biblioteca.
