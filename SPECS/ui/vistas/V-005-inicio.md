# Vista — V-005 Inicio

> Página pública de entrada al Marketplace para descubrir categorías y productos destacados, buscar productos y acceder a las áreas globales del canal.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-005` |
| Nombre | Inicio |
| Ruta | `/` |
| Versión | `0.2.0` |
| Estado | Aprobada para implementar (dirección visual H5; trazabilidad por frame en curso) |
| Responsable | Fernando José Saire Tello |
| Revisor | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) v`0.3.0` |
| Aprobación visual | [Jim Segovia, 24/11/2026](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/141#issuecomment-7121747860) |
| Enlace de Figma H5 | [Mockups H5 — inicio](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-560) |
| Enlace de Figma heredado | [Sección V-005](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=265-8) (frames H3, referencia) |
| Página de Figma | [Inicio, catálogo y producto](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-3) |
| Enlaces verificados | 2026-10-14 para frames H3; 2026-11-24 para la sección H5 aprobada. Enlaces por frame H5 pendientes |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** orientarse, descubrir categorías o productos destacados y comenzar una búsqueda o compra.
- **Actor principal:** visitante o cliente autenticado.
- **Permiso:** público.
- **Condiciones de entrada:** URL principal, logo de la cabecera, retorno desde un flujo o CTA “Seguir comprando”.
- **Resultado esperado:** navegación hacia `V-006` o `V-007`, o acceso a carrito, favoritos, pedidos y cuenta según el estado de sesión.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-006` | [`F-006 Inicio, categorías y destacados`](../../funcional/F-006-inicio-categorias-destacados.md) | [`UI F-006`](../F-006-inicio-categorias-destacados.md) | Hero, categorías activas, productos destacados y degradación por sección. |
| `F-036` | [`F-036 Agregar favorito`](../../funcional/F-036-agregar-favorito.md) | [`UI F-036`](../F-036-agregar-favorito.md) | Control de favorito en `ProductCard`, autenticación y feedback. |

Contratos consultados: [`API F-006`](../../contrato-api/F-006-inicio-categorias-destacados.md) y [`API F-036`](../../contrato-api/F-036-agregar-favorito.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| Logo o URL principal | `V-005` | Cualquier usuario | Sesión y carrito. |
| Búsqueda enviada | `V-006` | Término válido según F-007 | Consulta ingresada. |
| Categoría seleccionada | `V-006` | Categoría activa | Filtro de categoría y origen. |
| Producto destacado | `V-007` | Producto activo con slug válido | Origen para volver y posición cuando sea viable. |
| Carrito en cabecera | `V-008` | Cualquier usuario | Carrito y sesión. |
| Favoritos en cabecera | `V-009` | Cliente autenticado | Sesión. Sin sesión se activa `O-003`. |
| Mis pedidos | `V-015` | Cliente autenticado | Sesión. Sin sesión se activa `O-003`. |
| Iniciar sesión / cuenta | `V-001` o menú de cuenta | Según sesión | Ruta de retorno interna. |

## 5. Jerarquía y composición visual

```text
V-005 Inicio
├── Barra de promociones (opcional, contenido aprobado)
├── Cabecera global
│   ├── Logo
│   ├── Menú de categorías
│   ├── Buscador con sugerencias
│   ├── Cuenta, favoritos y carrito con contadores
│   └── Menú móvil
├── Contenido principal
│   ├── Hero editorial/comercial
│   ├── Categorías activas con imagen
│   └── Carruseles de productos
│       ├── Destacados
│       └── ProductCard × N
└── Pie global
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Barra de promociones | Mensaje editorial aprobado y cierre | Secundaria | Opcional; se oculta completa sin contenido. No comunica errores ni estados. |
| Cabecera | Logo, categorías, búsqueda y accesos globales | Primaria | Shell de `DS-001` §8.1, coherente con `V-006` y `V-007`; puede compactarse al desplazarse sin ocultar acciones esenciales ni foco. |
| Menú de categorías | Categorías activas | Primaria | Desktop con divulgación; mobile en drawer accesible. Sólo categorías activas de F-006. |
| Búsqueda | Campo y sugerencias de F-007 | Primaria | Sugerencias opcionales desde la misma consulta; si fallan, la búsqueda sigue disponible. |
| Hero | Mensaje, imagen y CTA editorial | Primaria | Un CTA inequívoco; contenido aprobado; sin autoplay ni promociones inventadas. |
| Categorías | Imagen y nombre | Primaria | Sólo categorías activas; la grilla mantiene el ancho mínimo del frame y no exige desplazamiento horizontal para completar una tarjeta. |
| Destacados | Carrusel manual de `ProductCard` | Primaria | Sólo productos activos con slug; la tarjeta aplica `DS-001` §8.3. Ausencia de imagen muestra placeholder local «Sin imagen». |
| Pie | Ayuda, políticas y navegación secundaria | Secundaria | Enlaces sólo con destino aprobado; no duplica la acción primaria del hero. |

Los carruseles son manuales: controles visibles de 44 px, teclado, `scroll-snap` y tarjeta parcial como pista. No hay autoplay. Una sección sin datos se omite completamente, incluyendo su título y espacio reservado. La ausencia de categorías o destacados no bloquea la cabecera, búsqueda ni navegación restante; un error de una sección no invalida las demás.

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Barra de promociones | Mensaje editorial aprobado | Cerrar | Sólo con contenido aprobado. |
| Logo | Variante oficial aprobada | Volver a `V-005` | Siempre. |
| Buscador | Etiqueta accesible “Buscar productos” | Abrir resultados en `V-006` | Siempre. |
| Sugerencias | Hasta seis coincidencias de F-007 | Abrir `V-006` o `V-007` según el resultado | Cuando el servicio responde y la consulta tiene al menos 2 caracteres. |
| Menú de categorías | Categorías activas | Abrir `V-006` filtrada o drawer mobile | Siempre; opciones según catálogo. |
| Acceso de cuenta | “Iniciar sesión” o menú del cliente | Abrir acceso/cuenta | Según sesión. |
| Favoritos | Icono + etiqueta + contador cuando exista | Abrir `V-009` o `O-003` | Siempre; estado según sesión. |
| Carrito | Icono + etiqueta + cantidad | Abrir `V-008` | Siempre. |
| Hero | Título, apoyo, recurso visual y CTA | Abrir destino editorial permitido | Cuando exista contenido aprobado; no inventar promoción. |
| Categoría | Nombre e imagen/icono | Abrir `V-006` filtrada | Categoría activa. |
| Producto | Imagen, marca, nombre, precio y oferta si aplica | Abrir `V-007` | Tarjeta comercial completa. |
| Acción rápida | “Agregar” o “Ver opciones” | Ejecutar F-016 o abrir `V-007` | “Agregar” sólo con un SKU vendible resuelto; en producto variable se usa “Ver opciones”. |
| Favorito de producto | “Guardar en favoritos” / “Quitar de favoritos” | Ejecutar F-036 o activar `O-003` | En cada tarjeta válida. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Principal público | Datos disponibles sin sesión | Inicio completo y acciones públicas | Explorar/iniciar sesión | Sí |
| Principal autenticado | Datos disponibles con sesión | Cuenta, favoritos y contadores personalizados | Explorar áreas privadas | Sí |
| Cargando | Solicitud inicial | Skeleton independiente para categorías y productos; cabecera operativa | Esperar/navegar | Sí |
| Categorías vacías | `categories: []` | Sección omitida; destacados permanecen | Explorar destacados/buscar | No; anotar en frame principal |
| Destacados vacíos | `featuredProducts: []` | Sección omitida; categorías permanecen | Explorar categorías/buscar | No; anotar en frame principal |
| Inicio sin contenido | Ambos arreglos vacíos | Orientación breve y CTA a `V-006`; navegación global operativa | Explorar catálogo | Sí |
| Catálogo no disponible | Respuesta `503` | Mensaje por región o estado general sin romper cabecera | Reintentar/usar navegación disponible | Sí |
| Precio o stock por confirmar | F-012/F-014 no responden para una tarjeta | La tarjeta conserva imagen y nombre; precio/stock indican “Por confirmar” y el agregado rápido no se habilita | Reintentar el dato o abrir ficha | Sí, variante de tarjeta |
| Sugerencias no disponibles | F-007 falla al sugerir | No se muestra lista; el envío de búsqueda sigue operativo | Buscar normalmente | No; anotar en frame principal |
| Menú móvil abierto | Pulsar categorías en mobile | Drawer con foco atrapado y fondo inerte | Navegar o cerrar | Sí |
| Favorito guardando | Cliente pulsa corazón | Control ocupado sin duplicar solicitud | Esperar | Sí, como variante de tarjeta |
| Favorito guardado | `201/200` | Estado activo con texto/icono y anuncio accesible | Continuar | Sí, como variante de tarjeta |
| Favorito sin sesión | Visitante pulsa corazón | Se activa `O-003`; no se crea favorito anónimo | Iniciar sesión o cancelar | Se diseña en `O-003` |
| Producto no disponible | F-036 devuelve `404` | Tarjeta se marca no disponible o se retira tras informar | Actualizar/explorar | Sí, como variante de tarjeta |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida con retorno | Favorito, pedidos u otra acción protegida sin sesión | Login conserva `V-005` y la intención; cancelar mantiene posición. |
| `O-010` | Alertas y feedback global | Error de favoritos o indisponibilidad recuperable | Cerrar o reintentar sin perder contexto. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Buscar productos | Search | No | Aplicar mínimo y normalización definidos por F-007 | Ayuda breve; no lanzar consulta inválida | Default/foco/error |

El hero no contiene formularios en el alcance actual. Sus CTA sólo apuntan a rutas internas aprobadas.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Barra de promociones opcional sobre la cabecera; si existe, no genera salto de layout al cargar.
- Cabecera con logo, menú de categorías, buscador visible y acciones globales; las categorías conservan alternativa accesible por teclado.
- Hero amplio con texto e imagen equilibrados según `DS-001`; el CTA principal no compite con enlaces secundarios.
- Categorías con imagen y productos usan grillas responsivas; las tarjetas mantienen relación de imagen y alineación de precios/acciones.
- No iniciar carruseles automáticamente; los carriles ofrecen controles visibles, teclado, `scroll-snap` y una tarjeta parcial como pista.

### Mobile

- **Referencia:** 390 px.
- Cabecera compacta con acceso claro a búsqueda, cuenta, favoritos y carrito; el menú de categorías se abre en drawer accesible y los contadores no reemplazan sus etiquetas.
- Hero prioriza título, CTA e imagen sin forzar texto sobre zonas ilegibles.
- Categorías mantienen una grilla legible; destacados usan carril manual y no dependen de autoplay.
- Las tarjetas conservan nombre, precio, favorito y acción rápida sin objetivos táctiles superpuestos ni anidados.

### Anchuras intermedias

- Ajustar columnas por ancho mínimo de tarjeta y contenido, no por cantidad fija.
- El buscador puede cambiar de fila antes de comprimirse por debajo de su ancho usable.

## 11. Accesibilidad

- Existe un único encabezado principal y regiones con nombres comprensibles.
- Se ofrece salto al contenido principal.
- Todas las tarjetas tienen un enlace accesible; el control de favorito es una acción separada y no anida botones dentro del enlace.
- Imágenes comerciales tienen texto alternativo útil; decoración usa alternativa vacía.
- Precio anterior, actual y descuento se leen en orden comprensible sin depender del tachado o color.
- Controles de carril, si existen, funcionan con teclado y no mueven contenido automáticamente.
- El cambio de favorito se anuncia y mantiene el foco; doble pulsación no duplica el cambio.
- Skeletons no se anuncian como contenido repetitivo y respetan reducción de movimiento.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| [`V-005 / Desktop / Público`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-111) | Desktop | Principal | Hero, categorías, destacados y cabecera pública. |
| [`V-005 / Mobile / Público`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-293) | Mobile | Principal | Cabecera compacta y secciones apiladas. |
| [`V-005 / Desktop / Autenticado`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-477) | Desktop | Principal con sesión | Cuenta y estados de favorito. |
| [`V-005 / Mobile / Cargando`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-659) | Mobile | Skeleton por sección | Cabecera operativa. |
| [`V-005 / Desktop / Sin contenido`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-717) | Desktop | Vacío total | Orientación a catálogo. |
| [`V-005 / Mobile / Catálogo no disponible`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-762) | Mobile | Error `503` | Reintento sin bloquear navegación. |
| [`V-005 / Desktop / ProductCard favorita`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-811) | Desktop | Variante de componente | Estado guardando y guardado anotados. |
| [`V-005 / Mobile / Producto no disponible`](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=274-866) | Mobile | Variante de tarjeta | Feedback y retirada/actualización. |

Los estados de una sola sección vacía se documentan como anotaciones del frame principal, porque la sección se omite y no crea un layout nuevo.

La dirección visual H5 aprobada el 24/11/2026 se encuentra en la sección [Mockups H5](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-560). Los frames de la tabla anterior son del corte H3 y se conservan como referencia; no acreditan por sí solos la composición H5. Los enlaces por frame H5 de esta vista se completan en el seguimiento de [#142](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/142) sin alterar el diseño aprobado.

### Referencias adicionales localizadas

Estos frames existen en el archivo consultado; se registran como referencias visuales, sin ampliar por ello los requisitos de implementación de H3 ni aprobar su diseño.

| Frame existente | Enlace directo |
|---|---|
| `V-005 / Mobile / Autenticado` | [Abrir frame](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=294-566) |
| `V-005 / Desktop / Cargando` | [Abrir frame](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=294-720) |
| `V-005 / Mobile / Sin contenido` | [Abrir frame](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=294-827) |
| `V-005 / Desktop / Catálogo no disponible` | [Abrir frame](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=294-911) |
| `V-005 / Mobile / ProductCard favorita` | [Abrir frame](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=294-998) |
| `V-005 / Desktop / Producto no disponible` | [Abrir frame](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=294-1037) |

Enlaces verificados el 14/10/2026 mediante metadatos de Figma. La existencia de un frame no acredita aprobación, integración de datos ni fidelidad de la web. La [comparación del corte H3](../../../plan/evidencias/H3-GIULIANO/H3-COMPARACION-FIGMA-2026-10-14.md) registra las diferencias encontradas. Las capacidades mostradas en el mockup se habilitan sólo cuando lo permitan el alcance y los contratos vigentes.

## 13. Criterios de aceptación visual

- [ ] `UI-V005-001`: Sólo se muestran categorías y productos activos con los datos mínimos completos.
- [ ] `UI-V005-002`: Una sección vacía se omite sin bloquear búsqueda, cabecera ni otras secciones.
- [ ] `UI-V005-003`: Mobile no depende de carrusel automático para acceder al contenido.
- [ ] `UI-V005-004`: Cada `ProductCard` separa navegación y favorito con nombres y focos accesibles.
- [ ] `UI-V005-005`: Guardar favorito sin sesión activa `O-003`, no crea estado anónimo y conserva el retorno.
- [ ] `UI-V005-006`: Precios y ofertas mantienen jerarquía semántica y no dependen sólo de color o tachado.
- [ ] `UI-V005-007`: Los estados de carga/error se resuelven por sección cuando todavía existe contenido útil.
- [ ] `UI-V005-008`: El menú de categorías y el drawer móvil son operables por teclado, restauran el foco y no dependen de hover.
- [ ] `UI-V005-009`: Los carruseles son manuales, tienen controles visibles y no mueven contenido automáticamente.
- [ ] `UI-V005-010`: El agregado rápido sólo aparece con un SKU vendible resuelto; en producto variable o con precio/stock “por confirmar” se muestra “Ver opciones” o se deshabilita con explicación.
- [ ] `UI-V005-011`: Cargando, vacío, error y “por confirmar” son distinguibles, accesibles y no dejan la vista en blanco.
- [ ] La vista aplica `DS-001` v`0.3.0` y reutiliza los mismos patrones globales de `V-006` y `V-007`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-005-OPEN-01` | Definir contenido, CTA, fuente y caducidad del hero; no inventar promociones en Figma. | Producto + UX | Antes del diseño final | Abierta |
| `V-005-OPEN-02` | Confirmar orden, cantidad máxima e imagen/icono de categorías. | Catálogo + Producto | Antes del diseño final | Abierta |
| `V-005-OPEN-03` | Confirmar cantidad y regla editorial de productos destacados. | Catálogo + Producto | Antes del diseño final | Abierta |
| `V-005-OPEN-04` | Aprobar patrón de cabecera y navegación mobile compartido por las vistas comerciales. | UX/UI | Antes del diseño final | **Resuelta** por la dirección visual H5 aprobada el 24/11/2026 |
| `V-005-OPEN-05` | Registrar los enlaces directos por frame H5 de inicio y de cada estado; la sección aprobada ya es la referencia. | UX/UI | Antes de la aceptación visual | Abierta |
