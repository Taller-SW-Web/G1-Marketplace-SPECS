# DS-001 — Sistema de diseño Marketplace

> Especificación UI transversal para los mockups de Figma y la futura interfaz web. Define fundamentos, tokens, componentes y patrones comunes; las specs UI por funcionalidad referencian este documento y sólo describen sus excepciones o necesidades particulares.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `DS-001` |
| Nombre | Sistema de diseño Marketplace |
| Versión | `0.1.0` |
| Estado | Borrador base para Hito 2 |
| Herramienta oficial | Figma |
| Implementación objetivo | Tailwind CSS 4 + shadcn/ui (Radix UI) + Lucide React |
| Última actualización | `2026-09-27` |
| Alcance | Todo el canal Marketplace web responsivo |

## 2. Propósito y principios

El sistema busca una experiencia de comercio deportivo en la que el producto sea protagonista, las decisiones de compra sean claras y la interfaz responda con energía sin convertirse en una copia de otra marca.

La referencia de Nike y Adidas se limita a principios observables de e-commerce deportivo: imágenes de producto protagonistas, composición amplia, llamadas a la acción directas, categorías ligadas a deportes, tarjetas visuales y navegación clara. No se reutilizan logos, nombres, campañas, tipografías propietarias, fotografías, textos, paletas distintivas ni otros activos de esas marcas. Las páginas oficiales de [Nike](https://about.nike.com/) y [Adidas](https://www.adidas.com/us) se usan sólo como inspiración de experiencia, no como fuente de recursos visuales.

### Principios de diseño

1. **Producto antes que decoración.** Las imágenes, nombre, información relevante y acción principal reciben la mayor jerarquía.
2. **Rendimiento legible.** La estética es deportiva y contundente, pero todos los datos de compra deben ser comprensibles y accesibles.
3. **Una acción principal por momento.** Cada pantalla prioriza una decisión; las acciones secundarias no compiten visualmente.
4. **Confianza durante la compra.** Precio, disponibilidad, costos, estados de pedido y errores deben explicarse sin ambigüedad cuando sus funcionalidades los definan.
5. **Movimiento con propósito.** Animaciones cortas orientan cambios de estado; nunca bloquean navegación ni ignoran preferencias de movimiento reducido.
6. **Móvil como escenario completo.** La experiencia móvil no es una reducción decorativa de escritorio: mantiene navegación, información y acciones esenciales.
7. **Accesible por defecto.** Contraste, foco, teclado, etiquetas y mensajes no son mejoras posteriores.

## 3. Identidad de marca provisional

La marca visual definitiva, nombre comercial y logotipo aún no han sido proporcionados. Hasta definirlos, los mockups usarán la etiqueta textual **Marketplace** y un bloque de logotipo provisional; no se dibujará ni se imitará el swoosh de Nike, las tres franjas de Adidas ni símbolos similares.

| Recurso | Regla provisional | Pendiente |
|---|---|---|
| Logotipo | Wordmark textual `Marketplace` en tipografía de interfaz; sin isotipo derivado de terceros. | `DS-OPEN-01`: proveer nombre y logo oficial. |
| Favicon | Monograma temporal `M` geométrico, original y sin semejanza intencional con marcas deportivas existentes. | Reemplazar al aprobar logo. |
| Fotografía | Fotos propias, licenciadas o de bancos autorizados. Deben mostrar el producto de forma clara. | Definir repositorio y licencia de activos. |
| Tono verbal | Directo, activo y cercano: “Explora”, “Elige”, “Entrena”, “Tu pedido está en ruta”. | Validar mensajes finales por UX/UI y PO. |

## 4. Fundamentos visuales

### 4.1 Color

La paleta usa un azul deportivo propio como color de acción y un acento verde-lima sólo para énfasis visual controlado. El negro y blanco construyen alto contraste y permiten que las fotos de producto destaquen.

| Token | Valor | Uso permitido |
|---|---|---|
| `color.brand.primary` | `#1D4ED8` | Botón principal, enlaces destacados, foco, acciones seleccionadas. |
| `color.brand.primary-hover` | `#1E40AF` | Hover/pressed de acción primaria. |
| `color.brand.accent` | `#B7F500` | Acento sobre fondo oscuro, etiquetas editoriales y destacados no críticos. Nunca como único indicador de estado. |
| `color.neutral.950` | `#111827` | Texto principal, fondo oscuro, navegación destacada. |
| `color.neutral.700` | `#374151` | Texto secundario fuerte. |
| `color.neutral.500` | `#6B7280` | Texto auxiliar e iconos secundarios. |
| `color.neutral.200` | `#E5E7EB` | Bordes y divisores. |
| `color.neutral.100` | `#F3F4F6` | Superficies secundarias y skeleton. |
| `color.neutral.0` | `#FFFFFF` | Fondo principal y texto sobre fondos oscuros. |
| `color.feedback.success` | `#15803D` | Confirmación positiva con texto o icono complementario. |
| `color.feedback.warning` | `#B45309` | Advertencias no bloqueantes. |
| `color.feedback.error` | `#B42318` | Error, acción destructiva o validación bloqueante. |
| `color.feedback.info` | `#075985` | Información contextual. |

Reglas:

- Todo par texto/fondo debe cumplir al menos WCAG 2.2 AA: 4.5:1 para texto normal y 3:1 para texto grande o controles gráficos.
- `color.brand.accent` se usa con `color.neutral.950` como fondo/texto contrastante; no se usa para texto pequeño sobre blanco.
- Éxito, advertencia y error combinan color, icono y mensaje; nunca se distinguen sólo por color.

### 4.2 Tipografía

| Token | Familia | Uso |
|---|---|---|
| `font.display` | `Barlow Condensed`, sans-serif | Titulares editoriales, banners y campañas; uso breve y en mayúsculas sólo si sigue siendo legible. |
| `font.body` | `Inter`, system-ui, sans-serif | Navegación, formularios, producto, precios, mensajes y contenido funcional. |
| `font.mono` | `ui-monospace`, monospace | Códigos técnicos visibles sólo cuando una funcionalidad lo requiera. |

Escala mínima:

| Token | Tamaño / línea | Uso |
|---|---|---|
| `display-xl` | 48 / 52 px desktop; 36 / 40 px móvil | Hero o campaña. |
| `heading-1` | 32 / 38 px desktop; 28 / 34 px móvil | Título principal de pantalla. |
| `heading-2` | 24 / 30 px | Sección relevante. |
| `heading-3` | 20 / 26 px | Subsección o tarjeta. |
| `body-md` | 16 / 24 px | Texto base. |
| `body-sm` | 14 / 20 px | Metadatos y contenido secundario. |
| `label-sm` | 12 / 16 px | Etiquetas; nunca para información crítica sin alternativa. |

### 4.3 Espaciado, tamaño y superficie

| Fundación | Regla |
|---|---|
| Escala de espacio | Múltiplos de 4 px: `4, 8, 12, 16, 24, 32, 40, 48, 64, 80`. |
| Área táctil | Mínimo 44 × 44 px para controles interactivos principales. |
| Radio | `8 px` controles, `12 px` tarjetas, `16 px` modales/zonas de contenido; no mezclar radios arbitrarios. |
| Borde | 1 px `color.neutral.200`; foco visible de 2 px `color.brand.primary` con separación de 2 px. |
| Sombra | `surface-1` sutil para tarjetas; `surface-2` para menú/modal. Las sombras no comunican estado crítico. |
| Imagen | Fondo neutro, proporción consistente por contexto y espacio reservado para evitar saltos al cargar. |

### 4.4 Grilla y breakpoints

| Contexto | Ancho | Regla de composición |
|---|---:|---|
| Móvil | 320–767 px | 4 columnas, margen 16 px, separación 16 px. |
| Tablet | 768–1023 px | 8 columnas, margen 24 px, separación 24 px. |
| Desktop | 1024–1439 px | 12 columnas, margen 32 px, separación 24 px. |
| Wide | ≥ 1440 px | Contenedor máximo de 1440 px, margen automático y 48 px interiores. |

## 5. Biblioteca de componentes

### 5.1 Implementación y equivalencias

| Necesidad visual | Base técnica declarada | Regla |
|---|---|---|
| Botón, input, select, checkbox, tabs, accordion y skeleton | shadcn/ui + Radix UI | Se personalizan mediante tokens; no se modifica su semántica accesible. |
| Modal, sheet, popover y tooltip | Radix UI vía shadcn/ui | Deben gestionar foco, Escape y etiquetas accesibles. |
| Iconos | Lucide React | Tamaño consistente de 20 o 24 px; icono sin texto sólo cuando tiene nombre accesible. |
| Estilos responsivos | Tailwind CSS 4 | Los tokens de este documento se traducen a variables y utilidades; no se usan valores arbitrarios sin justificarlos. |
| Formularios | React Hook Form + Zod | La validación visual refleja el contrato funcional y de API, no reglas inventadas en UI. |
| Toasts | Sonner | Sólo confirma acciones breves; errores bloqueantes o recuperables deben ser visibles en contexto. |

### 5.2 Componentes mínimos para Hito 2

| Componente | Variantes o estados mínimos | Uso |
|---|---|---|
| `Button` | primaria, secundaria, terciaria/enlace, destructiva; normal, hover, focus, disabled, loading. | Acciones de formularios, compra y navegación. |
| `IconButton` | neutra, primaria, destructiva; con tooltip/etiqueta accesible. | Buscar, cerrar, favorito, galería. |
| `TextField` | vacío, focus, filled, validado, error, disabled. | Login, registro, dirección, cupón y pago simulado. |
| `Select` / `Checkbox` / `Radio` | normal, focus, seleccionado, error, disabled. | Filtros y formularios. |
| `ProductCard` | imagen, marca, nombre, zona de precio, etiqueta y acción secundaria. | Home, catálogo y recomendaciones. |
| `ProductGallery` | loading, imagen principal, miniaturas, respaldo de imagen, visor ampliado. | Ficha `F-011`. |
| `Badge` | neutro, éxito, advertencia, error, promoción. | Estado de pedido, stock, descuentos y novedades. |
| `Alert` | información, éxito, advertencia, error; con acción opcional. | Estados de integración y formularios. |
| `Skeleton` | tarjeta, galería, texto, resumen de pedido. | Carga sin desplazamiento visual. |
| `Modal` / `Sheet` | foco atrapado, cierre explícito y con Escape. | Acceso, filtros móviles, confirmaciones. |
| `EmptyState` | título, explicación, ilustración original y CTA. | Carrito, favoritos, historial, búsqueda. |
| `Toast` | éxito e información breve. | Confirmaciones no críticas. |

Un componente se considera listo en Figma sólo si posee sus variantes, estados, comportamiento responsive y anotaciones de accesibilidad; no basta una única captura visual.

## 6. Patrones de experiencia

| Patrón | Regla de uso |
|---|---|
| Cabecera | Logo textual, buscador, categorías y accesos a cuenta, favoritos y carrito. En móvil, los accesos críticos siguen disponibles sin depender de hover. |
| Producto protagonista | Imagen grande sobre fondo neutro, título claro y una sola acción primaria cuando su funcionalidad esté definida. |
| Filtros | Panel lateral en desktop; sheet/modal en móvil. Debe indicar filtros activos, permitir limpiar y mantener la consulta accesible. |
| Ficha de producto | Galería y contenido descriptivo primero; información de compra se integra en regiones definidas por `F-012` a `F-016`. |
| Checkout | Pasos visibles, resumen persistente cuando el espacio lo permita, validación cerca del campo y una acción principal por paso. |
| Estados vacíos | Explican qué sucede, no culpan al usuario y ofrecen un siguiente paso real. |
| Errores | Mensaje en lenguaje claro, causa sólo cuando ayuda a recuperarse y acción explícita: corregir, reintentar o volver. |
| Feedback postentrega | No interrumpe justo después de pagar; se activa tras entrega confirmada según `F-040`. |

## 7. Accesibilidad y contenido

- Objetivo mínimo: WCAG 2.2 nivel AA.
- Orden de foco igual al orden visual y lógico; foco visible en todos los controles.
- Un único `h1` por pantalla; encabezados jerárquicos sin saltos arbitrarios.
- Cada formulario expone etiqueta visible, ayuda cuando aplique y error vinculado al campo.
- Los diálogos bloquean interacción de fondo, atrapan el foco y restauran el foco de origen al cerrar.
- Imágenes de producto requieren texto alternativo descriptivo; imágenes decorativas usan alternativa vacía.
- No usar carruseles con reproducción automática. Si una animación existe, debe poder pausarse o respetar `prefers-reduced-motion`.
- Todo texto visible se redacta en español claro y consistente; evitar mensajes técnicos como “Error 500” como explicación principal al cliente.

## 8. Biblioteca en Figma y entregables del Hito 2

La biblioteca de Figma tendrá estas páginas, en este orden:

1. `00-Cover y guía`: propósito, versión, enlaces y responsables.
2. `01-Foundations`: colores, tipografías, espaciado, grilla, iconos y elevación.
3. `02-Components`: componentes, variantes, estados, anatomía y notas de accesibilidad.
4. `03-Patterns`: cabecera, producto, filtros, ficha, checkout, estados vacíos y errores.
5. `04-Screens`: mockups de las pantallas del módulo con vínculo a su ID funcional.
6. `05-Prototypes`: flujos navegables y escenarios de prueba.

Checklist mínimo de Hito 2:

- [ ] Variables de color, texto, espaciado y radio creadas en Figma.
- [ ] Tipos de texto y estilos de efecto configurados.
- [ ] Componentes mínimos con variantes y estados documentados.
- [ ] Logo o wordmark provisional identificado y pendiente de reemplazo visible.
- [ ] Mockups de las pantallas del módulo construidos con instancias de la biblioteca, no elementos duplicados manualmente.
- [ ] Prototipo de al menos los flujos prioritarios y estados de error/carga relevantes.
- [ ] Revisión de contraste, foco y navegación móvil.

## 9. Uso en specs UI individuales

Cada spec UI debe incluir una referencia a `DS-001` e indicar solamente:

- componentes de la biblioteca que utiliza;
- patrones aplicados;
- tokens relevantes cuando una decisión es significativa para la funcionalidad;
- excepciones o componentes nuevos que deban incorporarse al sistema;
- enlace a la pantalla/prototipo de Figma cuando exista.

Ejemplo:

```text
Sistema de diseño: DS-001 v0.1.0.
Componentes: ProductGallery, Breadcrumb, Button, Alert y Skeleton.
Patrón: ficha de producto.
Excepción: ninguna.
Figma: pendiente de enlace a P7.
```

Una spec individual no vuelve a declarar hexadecimales, márgenes o anatomía base de componentes salvo que proponga un cambio a `DS-001`.

## 10. Decisiones abiertas y versionado

| ID | Decisión pendiente | Impacto |
|---|---|---|
| `DS-OPEN-01` | Nombre comercial, logo, favicon y manual de uso de marca. | Reemplaza el wordmark provisional sin alterar tokens funcionales. |
| `DS-OPEN-02` | Enlace oficial a la biblioteca y prototipo Figma. | Necesario para aprobar specs UI del Hito 2. |
| `DS-OPEN-03` | Validar disponibilidad/licencia de las fuentes `Inter` y `Barlow Condensed` en el entorno de frontend. | Define carga de fuentes y fallback final. |
| `DS-OPEN-04` | Aprobar valores de contraste con la paleta final al incorporar logo. | Revisión de accesibilidad antes de `1.0.0`. |

- `0.1.x`: ajustes de tokens, componentes o documentación sin romper mockups existentes.
- `0.2.0`: incorpora biblioteca inicial de Figma y patrones del Hito 2.
- `1.0.0`: identidad de marca, tokens y componentes base aprobados por PO y UX/UI.
- Un cambio que modifique el uso de un componente o elimine un token exige documentar migración en las specs afectadas.

## 11. Fuentes

- Arquitectura de Marketplace: Figma, Tailwind CSS 4, shadcn/ui, Radix UI, Lucide React, React Hook Form, Zod y Sonner.
- `Wireframes y Prototipo/Especificación de pantallas del canal.md`.
- Inspiración de experiencia — no de identidad: [Nike](https://about.nike.com/) y [Adidas](https://www.adidas.com/us). Las páginas oficiales muestran una experiencia centrada en campañas, categorías deportivas y navegación de productos; las decisiones de este documento son una interpretación propia para Marketplace.
