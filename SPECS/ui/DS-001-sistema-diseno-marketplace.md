# DS-001 — Sistema de diseño de Inka Athletics

> Especificación UI transversal para los mockups de Figma y la futura interfaz web del Canal Marketplace. Consolida la guía UX/UI preliminar, los recursos de marca recibidos y las reglas vigentes de las specs `F-001` a `F-040`.

## 1. Metadatos y estado

| Campo | Valor |
|---|---|
| ID | `DS-001` |
| Nombre | Sistema de diseño de Inka Athletics |
| Versión | `0.3.0` |
| Estado | Dirección visual H5 aprobada por el revisor principal el 24/11/2026; implementación de shell y vistas comerciales habilitada. Biblioteca y aceptación final de componentes pendientes |
| Custodio | Giuliano Macchiavello |
| Revisor principal | Jim Segovia |
| Aprobación de la dirección visual | [Jim Segovia en #141, 24/11/2026](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/141#issuecomment-7121747860) |
| Benchmark H5 | [Benchmark](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-565) |
| Mockups H5 aprobados | [Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-560) — shell, inicio, catálogo, ficha, carrito y checkout |
| Marca | Inka Athletics |
| Herramienta oficial | Figma |
| Biblioteca del sistema de diseño en Figma | [Sistema de Diseño](https://www.figma.com/design/rKPdRQHLLUkYk5VdiEErqZ/Sistema-De-Dise%C3%B1o?node-id=57-15&t=eO6m1Plz1xQ5sFgn-1) |
| Sección de logos en Figma | [Logos de Inka Athletics](https://www.figma.com/design/rKPdRQHLLUkYk5VdiEErqZ/Sistema-De-Dise%C3%B1o?node-id=56-7&t=0TSK36SaklUJeiyS-4) |
| Carpeta de mockups de vistas en Figma | [Marketplace — vistas](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394) (carpeta organizativa) |
| Archivo de mockups de vistas | [Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) |
| Página de inicio, catálogo y producto | [Inicio, catálogo y producto](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-3) — enlaces de V-005/V-006 verificados el 14/10/2026 |
| Mockups de vistas en Figma | [Carpeta Marketplace](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394) y [página Checkout](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5) del archivo Mockups; faltan enlaces finales de otras vistas/estados |
| Framework frontend decidido (PO, 2026-10-10) | React + TypeScript + Next.js App Router; FE `main@ec1acfb` instala Next.js `16.4.1`, React `19.3.1` y TypeScript `5.9.3` con lockfile |
| UI kit descrito por la guía preliminar | Mantine `9.6.2` + Tabler Icons; propuesta, no aprobación. Checkout F-022–F-027 usa la base kit-neutral existente; `DS-OPEN-03` permanece abierto para las demás familias. |
| Última revisión documental | 2026-11-24; dirección visual H5 aprobada. Guía visual original 2026-10-01 |
| Alcance | Canal Marketplace web responsive y componentes compartidos |
| Issues que habilita | [#143](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/143), [#144](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/144), [#145](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/145), [#153](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/153) y [#154](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/154) |

### 1.1 Vigencia y decisión técnica preliminar

Este documento es la fuente visual vigente para los mockups. La versión `0.2.0` incorporó la identidad Inka Athletics y reemplazó los tokens provisionales de `DS-001` v0.1.0.

La versión `0.3.0` registra la **dirección visual H5 aprobada en la revisión de Jim Segovia el 24/11/2026** en [#141](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/141#issuecomment-7121747860): shell global, inicio, catálogo, ficha, carrito y checkout. Los frames aprobados están en la sección [Mockups H5](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-560), con el [benchmark](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-565) como antecedente de análisis.

Esta versión **no introduce tokens nuevos ni cambia los contratos de componentes**: la dirección aprobada reutiliza Foundations 5.1–5.7 y concreta composición, patrones y estados. Los cambios de token, tipografía, radios o color requieren una propuesta propia con impacto y revisión. La aprobación visual habilita la implementación; no cierra por sí sola la aceptación de una vista ni publica la biblioteca Figma.

La dirección ya se aplicó en V-001 a V-004 ([#150](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/150)) y V-010 ([#148](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/148)). Las implementaciones deben adjuntar capturas desktop/móvil del mismo SHA y conservar los estados descritos en la sección 8.8.

El PO decidió React + TypeScript + Next.js App Router para la implementación frontend el 2026-10-10. FE `main@ec1acfb`, revisado el 18/10, usa Next.js `16.4.1`, React `19.3.1`, CSS, tokens y componentes propios; no tiene Mantine ni Tabler en sus dependencias. La guía recibida propone Mantine `9.6.2` y Tabler Icons; otros documentos históricos mencionan Tailwind CSS, shadcn/ui, Radix UI y Lucide React. Esta propuesta no equivale a una decisión global aprobada. Checkout F-022–F-027 se mantiene neutral respecto del kit y usa los tokens del diseño. Para no mezclar dos sistemas:

- los mockups y la biblioteca de Figma seguirán los tokens y propiedades documentados aquí;
- Checkout conserva la implementación kit-neutral existente (`Button`, `TextField`, tokens DS-001 y estilos base), ajustándola a los frames aprobados;
- Mantine + Tabler siguen siendo una propuesta para decisión global, no dependencia de Checkout;
- antes de instalar otro UI kit en las demás familias, el equipo debe aprobarlo y actualizar los documentos que aún indiquen el kit anterior;
- mientras esa decisión no se cierre, las reglas de comportamiento, accesibilidad, tokens y composición de este documento sí son obligatorias.

## 2. Propósito y principios

El sistema centraliza decisiones visuales, de interacción y contenido. Complementa las specs funcionales; no las reemplaza.

1. **Producto antes que decoración.** Imagen, nombre, información comercial y acción principal reciben la mayor jerarquía.
2. **Claridad para decidir.** Precio, disponibilidad, envío, estados y errores se explican sin ambigüedad.
3. **Una acción principal por momento.** Las acciones secundarias no compiten con la decisión principal.
4. **Energía sin agresividad.** La experiencia transmite movimiento sin gritar, presionar o culpabilizar.
5. **Móvil como experiencia completa.** Mobile no es una versión recortada de desktop.
6. **Accesibilidad por defecto.** Contraste, foco, teclado, etiquetas y objetivos táctiles se diseñan desde el inicio.
7. **Componentes antes que copias.** Se usan instancias publicadas; no se redibujan componentes localmente.
8. **Trazabilidad.** Cada pantalla referencia su spec `V-###`, sus funcionalidades `F-###` y esta versión de `DS-001`.

### 2.1 Inspiración deportiva

Nike y Adidas se conservan como referencias de experiencia para estudiar jerarquía de producto, fotografía protagonista, navegación clara, composición amplia y CTA directos. No se reutilizan logos, símbolos, campañas, tipografías propietarias, fotografías, textos ni paletas distintivas.

Inka Athletics debe ser reconocible por decisiones propias: naranja de acción, acentos Volt y Signal, superficies Ink/Cloud, Oswald + Inter, líneas de velocidad y logotipo propio.

## 3. Identidad de marca

### 3.1 Nombre, propósito y personalidad

**Inka Athletics** combina una identidad peruana contemporánea con deporte, movimiento, rendimiento y progreso. La referencia peruana debe comunicarse con autenticidad, sin clichés ni recursos folclóricos superficiales.

> Impulsar a más personas a vivir el deporte con confianza, encontrando equipamiento, ropa y accesorios adecuados para cada meta.

La personalidad es determinada, cercana, contemporánea, confiable, activa y orgullosamente peruana. La marca transmite energía, pero también acompañamiento; no es distante ni excesivamente agresiva.

## 4. Logotipo

### 4.1 Variantes recibidas

| Variante | Uso recomendado | Token | Recurso local |
|---|---|---|---|
| Ink | Fondos claros y aplicaciones generales | `color/surface/ink` | [inka-athletics-logo-ink.png](sistema-diseno/assets/logos/inka-athletics-logo-ink.png) |
| Volt | Promociones, campañas y alto impacto | `color/accent/volt` | [inka-athletics-logo-volt.png](sistema-diseno/assets/logos/inka-athletics-logo-volt.png) |
| Signal | Aplicaciones digitales y destacados | `color/accent/signal` | [inka-athletics-logo-signal.png](sistema-diseno/assets/logos/inka-athletics-logo-signal.png) |

Los archivos recibidos son PNG de `1448 × 1086 px`, RGB y fondo opaco claro. Para implementación y exportaciones finales se debe obtener de Figma el SVG maestro y las versiones optimizadas con transparencia.

### 4.2 Reglas de uso

No se permite:

- estirar, comprimir, deformar o rotar;
- cambiar colores fuera de las variantes aprobadas;
- añadir sombras, contornos o efectos no documentados;
- usar fondos con contraste insuficiente;
- recortar símbolo o logotipo;
- modificar la relación entre símbolo y nombre;
- sustituir un icono funcional por el logo.

La versión blanca/inversa debe incorporarse antes de usar el logo sobre `color/surface/ink`.

### 4.3 Accesibilidad y pendientes

- Si identifica la marca o navega al inicio, el nombre accesible es “Inka Athletics”.
- Si es decorativo y el nombre ya está visible, se oculta para tecnologías de asistencia.
- Pendientes: SVG maestro, versión inversa, favicon, isotipo reducido, área de seguridad, tamaño mínimo y confirmación de autoría/licencia.

## 5. Foundations

### 5.1 Color

La paleta separa acciones, acentos, superficies, texto y estados semánticos. Los nombres deben coincidir entre variables de Figma y el tema de implementación.

| Token | HEX | Función |
|---|---:|---|
| `color/action/primary` | `#F76707` | CTA, botones principales y enlaces activos |
| `color/action/primary-hover` | `#C2410C` | Hover principal y acciones secundarias |
| `color/action/primary-soft` | `#FCE3D0` | Fondo suave relacionado con la acción |
| `color/accent/volt` | `#C3E504` | Promoción, disponibilidad y celebración visual |
| `color/accent/volt-soft` | `#EEF7B0` | Fondo suave Volt |
| `color/accent/signal` | `#4361EE` | Foco global, confirmación/pago y contenido nuevo |
| `color/accent/signal-soft` | `#E1E6FB` | Fondo suave Signal |
| `color/surface/ink` | `#1B1812` | Fondo oscuro de alto contraste |
| `color/surface/ink-soft` | `#26221A` | Superficie elevada sobre Ink |
| `color/surface/cloud` | `#F7F5F0` | Fondo claro principal |
| `color/surface/cloud-subtle` | `#EDEAE2` | Fondo secundario sobre Cloud |
| `color/text/primary` | `#1B1812` | Texto principal sobre claro |
| `color/text/inverse` | `#F7F5F0` | Texto principal sobre oscuro |
| `color/text/secondary` | `#495057` | Información secundaria |
| `color/text/disabled` | `#868E96` | Texto deshabilitado |
| `color/border/default` | `#DEE2E6` | Bordes sobre claro |
| `color/border/inverse` | `#3A362C` | Bordes sobre oscuro |
| `color/success/default` | `#2F9E44` | Confirmación positiva |
| `color/success/background` | `#EBFBEE` | Fondo de éxito |
| `color/warning/default` | `#F08C00` | Advertencia |
| `color/warning/background` | `#FFF9DB` | Fondo de advertencia |
| `color/error/default` | `#E03131` | Error y acción destructiva |
| `color/error/background` | `#FFF5F5` | Fondo de error |
| `color/info/default` | `#1971C2` | Información contextual |
| `color/info/background` | `#E7F5FF` | Fondo informativo |

#### Reglas de color

- `action/primary` se usa para la acción principal, no para decorar.
- Volt no sustituye la acción principal ni un estado semántico.
- Signal es acento de marca y foco; no sustituye `info/default`.
- Pantallas transaccionales usan Cloud por defecto.
- Heroes, campañas y footer pueden usar Ink con texto inverso.
- No se mezclan Ink y Cloud dentro del mismo componente o tarjeta.
- Éxito, advertencia, error e información combinan color con texto y, cuando corresponda, icono.

| Fondo | Texto | Contraste aprox. | Uso |
|---|---|---:|---|
| `#F76707` | `#1B1812` | 5.82:1 | Botón principal |
| `#C2410C` | `#F7F5F0` | 4.75:1 | Hover principal |
| `#1B1812` | `#F7F5F0` | 16.25:1 | Texto sobre Ink |
| `#F7F5F0` | `#1B1812` | 16.25:1 | Texto sobre Cloud |
| `#EDEAE2` | `#1B1812` | 14.73:1 | Superficie secundaria |
| `#C3E504` | `#1B1812` | 12.25:1 | Promoción y disponibilidad |
| `#4361EE` | `#FFFFFF` | 5.02:1 | Confirmación, pago y nuevo |

No se usa texto blanco sobre el naranja principal ni sobre Volt. El objetivo mínimo es WCAG 2.2 AA.

### 5.2 Tipografía

| Rol | Familia | Regla |
|---|---|---|
| H1-H3 | Oswald | Peso 700, mayúsculas, uso breve y de alto impacto |
| H4, subtítulos, cuerpo, formularios y UI | Inter | No sustituir por Oswald |
| Respaldo | `system-ui`, `-apple-system`, `BlinkMacSystemFont`, `Segoe UI`, `sans-serif` | Si la fuente web no carga |

Fuentes aprobadas: Inter `400/500/600/700` y Oswald `500/700`.

| Estilo | Tamaño | Peso | Línea | Uso |
|---|---:|---:|---:|---|
| `Typography/Heading/H1` | 32 px | 700 | 40 px | Título principal |
| `Typography/Heading/H2` | 28 px | 700 | 36 px | Sección principal |
| `Typography/Heading/H3` | 24 px | 700 | 32 px | Subsección |
| `Typography/Heading/H4` | 20 px | 700 | 28 px | Tarjeta, modal o bloque |
| `Typography/Subtitle` | 18 px | 600 | 26 px | Encabezado secundario |
| `Typography/Body` | 16 px | 400 | 24 px | Texto principal |
| `Typography/Body/Small` | 14 px | 400 | 20 px | Información secundaria |
| `Typography/Label` | 14 px | 600 | 20 px | Etiqueta y control |
| `Typography/Auxiliary` | 12 px | 400 | 16 px | Ayuda y metadatos |

### 5.3 Espaciado

| Token | Valor | Uso |
|---|---:|---|
| `spacing/xs` | 4 px | Separación mínima |
| `spacing/sm` | 8 px | Icono-texto y controles relacionados |
| `spacing/md` | 16 px | Padding y separación estándar |
| `spacing/lg` | 24 px | Grupos y bloques |
| `spacing/xl` | 32 px | Secciones |

No se introducen valores arbitrarios; una necesidad nueva se propone como token.

### 5.4 Grilla y breakpoints

La grilla usa 12 columnas en todos los tamaños.

| Breakpoint | Referencia | Margen | Gutter | Máximo |
|---|---:|---:|---:|---:|
| Base | `<576 px` | 16 px | 16 px | Fluido |
| `xs` | `≥576 px` | 20 px | 16 px | 540 px |
| `sm` | `≥768 px` | 24 px | 20 px | 720 px |
| `md` | `≥992 px` | 32 px | 24 px | 960 px |
| `lg` | `≥1200 px` | 32 px | 24 px | 1140 px |
| `xl` | `≥1408 px` | 40 px | 24 px | 1320 px |

Una tarjeta ocupa como referencia 12 columnas en móvil, 6 en tablet y 3 en desktop. Los mockups incluyen mobile y desktop cuando el patrón cambie de manera relevante.

### 5.5 Radios, bordes y foco

| Token | Valor | Uso |
|---|---:|---|
| `radius/xs` | 4 px | Control compacto |
| `radius/sm` | 8 px | Botón, input y dropdown |
| `radius/md` | 12 px | Tarjeta y contenedor |
| `radius/lg` | 16 px | Modal y superficie destacada |
| `radius/full` | 999 px | Badge, tag y pill |

- Radio predeterminado: 8 px.
- Borde predeterminado: 1 px `color/border/default`.
- Foco global: `color/accent/signal`, contraste mínimo 3:1.
- Objetivo táctil recomendado: 44 × 44 px.

### 5.6 Iconografía

El set oficial es **Tabler Icons**, con equivalencia preliminar en `@tabler/icons-react`.

- Lienzo: 24 × 24 px; trazo: 2 px.
- Tamaños aprobados: 16, 20 y 24 px.
- Tamaño estándar en botones e inputs: 20 px.
- Separación icono-texto: 8 px.
- Color: `currentColor` salvo semántica definida.
- Un icono que actúa solo debe estar dentro de un control accesible con nombre.

### 5.7 Superficies y motivo gráfico

Las líneas de velocidad son diagonales delgadas de aproximadamente 110°-120°, en naranja, Volt o Signal. Sólo son decoración de heroes o divisores; no comunican estado ni información. Falta enlazar su componente oficial de Figma.

## 6. Brand y UX Writing

Inka Athletics comunica de forma directa, motivadora, humana y segura. Habla con energía sin exagerar.

- Comenzar acciones con verbos: Comprar, Guardar, Aplicar, Continuar o Volver.
- Mantener el mismo término para una acción en todas las vistas.
- Explicar primero qué ocurrió y después qué puede hacer el usuario.
- Evitar códigos internos, culpas, tecnicismos y exclamaciones innecesarias.
- Usar mayúscula inicial; no escribir botones completos en mayúsculas.
- Evitar inglés innecesario, agresividad, informalidad forzada, clichés y promesas absolutas.

| Situación | Recomendado | Evitar |
|---|---|---|
| Compra | “Comprar ahora” | “Haz clic aquí” |
| Filtros | “Aplicar filtros” | “Aceptar” |
| Pago | “Continuar al pago” | “Siguiente” |
| Guardado | “Guardar cambios” | “Enviar” |
| Stock agotado | “Este producto está agotado. Prueba otra talla o revisa productos similares.” | “Error de stock” |
| Campo requerido | “Ingresa tu correo electrónico.” | “Campo inválido” |
| Conexión | “No pudimos cargar la información. Inténtalo nuevamente.” | “Error 500” |

La referencia del documento preliminar a “tarjeta rechazada” no aplica al alcance vigente: `F-025` define pago simulado sin tarjeta ni CVV.

## 7. UI Kit

### 7.1 Base preliminar

La guía propone Mantine `9.6.2` sobre React y TypeScript. Figma debe usar propiedades equivalentes cuando sea posible: `variant`, `size`, `color`, `radius`, `disabled`, `loading`, `error`, `checked`, `searchable` y `clearable`.

Reglas comunes:

- usar componentes existentes antes de crear uno personalizado;
- utilizar sólo tokens de Foundations;
- representar los estados que realmente apliquen;
- impedir acciones repetidas durante `loading` cuando sea necesario;
- mantener foco visible y nombres accesibles;
- documentar responsive y probar cada componente en una vista real.

### 7.2 Botones

| Uso | Variante | Color | Texto |
|---|---|---|---|
| Principal | `filled` | `action/primary` | `text/primary` |
| Secundaria | `outline` | `action/primary-hover` | `action/primary-hover` |
| Terciaria | `subtle` | `action/primary-hover` | `action/primary-hover` |
| Confirmación/pago general | `filled` | `accent/signal` | Blanco |
| CTA principal de Checkout F-022–F-027 | `filled` | `action/primary` (naranja) | Texto de alto contraste según token |
| Destructiva | `filled` | `error/default` | Blanco |

- Tamaños: `sm`, `md`, `lg`; predeterminado `md`.
- Icono: `none`, `left`, `right`.
- Estados: `default`, `hover`, `focus`, `disabled`, `loading`.
- En móvil, acciones principales de formularios y checkout pueden ocupar todo el ancho.
- Volt no se usa como botón principal.

### 7.3 Campos y búsqueda

- Base preliminar: `TextInput`, `PasswordInput`, `NumberInput`, `Textarea` y búsqueda con `IconSearch`.
- Label visible; placeholder no sustituye al label.
- Error concreto y accionable.
- Estados: `default`, `hover`, `focus`, `filled`, `disabled`, `loading`, `error`.
- Búsqueda puede ofrecer limpiar y loader; “Sin resultados” no es error técnico.

### 7.4 Checkbox

- Para opciones independientes o múltiples; para exclusión mutua usar Radio.
- Estados: `unchecked`, `checked`, `indeterminate` combinados con `default`, `hover`, `focus`, `disabled`, `error`.
- Toda la etiqueta activa el control.
- El error explica la acción requerida.

### 7.5 Dropdowns

| Necesidad | Componente preliminar |
|---|---|
| Selección única | `Select` |
| Selección múltiple | `MultiSelect` |
| Sugerencias | `Autocomplete` |
| Avanzado | `Combobox` |

Estados: `default`, `hover`, `focus`, `open`, `selected`, `disabled`, `loading`, `error`. En móvil ocupan el ancho disponible y mantienen la lista dentro del viewport.

### 7.6 Badges, chips y pills

| Elemento | Propósito |
|---|---|
| Badge | Estado, categoría o característica; no interactivo |
| Chip | Opción seleccionable |
| Pill | Valor removible |

Badge admite `neutral`, `info`, `success`, `warning`, `error`, `promotion`, `availability`, `new`; tamaños `sm` y `md`. Chip usa `default`, `hover`, `focus`, `selected`, `disabled`. El botón de eliminación de Pill requiere nombre accesible.

### 7.7 Componentes de aplicación requeridos

- **Shell:** `PromoBar`, `Header`, `CategoryMenu`, `SearchBox` con sugerencias, `Footer`.
- **Comercio:** `ProductCard` con agregado rápido restringido, `ProductGallery`, `CartLine`, `QuantityStepper`, `OrderSummary`.
- **Estado y feedback:** `Skeleton`, `EmptyState`, `StatePanel` para “por confirmar”, `Alert`, `Toast`, `Modal` y panel mobile.
- **Navegación:** `Breadcrumb`, paginación, carrusel manual y línea de tiempo de pedido/despacho.

La dirección visual H5 aprueba la composición de estos patrones, no la publicación de una biblioteca de componentes. Cada componente compuesto se completa desde las specs por vista, conserva su contrato y requiere revisión de implementación y accesibilidad antes de declararse aceptado.

## 8. Patrones comunes

> La dirección visual H5 (`0.3.0`) concreta estos patrones en los frames aprobados. Las reglas de esta sección son obligatorias; la composición exacta sigue el frame y cualquier diferencia se anota en la spec de la vista y se revisa con el custodio.

### 8.1 Shell global

El shell agrupa barra de promociones, cabecera, navegación de categorías, contenido y pie. Se comparte entre `V-005`, `V-006`, `V-007`, `V-008` y `V-009`; checkout conserva su cabecera reducida.

| Región | Contenido | Regla |
|---|---|---|
| Barra de promociones | Mensaje editorial aprobado y cierre | Opcional. Sólo con contenido aprobado; no comunica errores, estados ni información transaccional. Ocupa su altura sin saltos de layout y se oculta completa si no hay contenido. |
| Cabecera | Logo, categorías, búsqueda, cuenta, favoritos y carrito | Mantiene las acciones esenciales visibles. Puede compactarse o fijarse al desplazar sólo si no tapa el salto al contenido, el foco ni mensajes. |
| Categorías | Acceso al menú de categorías activas | Desktop: divulgación o mega menú. Mobile: drawer con foco atrapado. Sólo categorías activas de F-006; no se inventan destinos. |
| Búsqueda | Campo con etiqueta “Buscar productos” | Conserva mínimo/máximo de F-007. Sugerencias opcionales, nunca requisito para buscar. |
| Cuenta, favoritos y carrito | Acceso y contador cuando exista | El contador acompaña a una etiqueta accesible; no sustituye el nombre del control. Sin sesión, favoritos y áreas privadas activan `O-003`. |
| Pie | Ayuda, políticas y navegación secundaria | Ver 8.9. No compite con la acción principal de la vista. |

Reglas del menú de categorías:

- Abre con Enter/Espacio o clic; en desktop admite flechas para recorrer opciones.
- Escape cierra y devuelve el foco al disparador; seleccionar una categoría navega a `V-006` filtrada.
- En mobile usa drawer: foco atrapado, fondo inerte, cierre explícito y restauración de foco.
- El estado abierto no depende de hover y no deja controles inalcanzables por teclado.
- Si las categorías no cargan, el resto de la cabecera sigue operativo y el error se limita a esa región.

Reglas de búsqueda con sugerencias:

- Se alimentan de la misma consulta F-007; no se introduce un endpoint ni un contrato nuevos.
- Se activan desde 2 caracteres, con retardo breve, cancelación de la consulta anterior y un máximo de seis resultados.
- Teclado: flechas recorren, Enter abre la sugerencia activa, Escape cierra sin borrar el texto.
- “Sin sugerencias” es un estado neutral, no un error; si el servicio falla, el envío de la búsqueda sigue disponible.
- No muestran datos privados, precios no confirmados ni términos inventados.

### 8.2 Inicio

Orden aprobado: barra de promociones, cabecera, hero, categorías con imagen, carruseles de productos y pie. Las secciones sin datos se omiten por completo, incluido su título y espacio reservado.

- **Hero:** un único CTA inequívoco y contenido editorial aprobado. Si hay texto sobre imagen, se usa una capa de contraste; la legibilidad no depende del color de la fotografía. Sin autoplay.
- **Categorías:** tarjeta con imagen y nombre, sólo categorías activas. La grilla es fluida y mantiene el ancho mínimo del frame; en mobile no obliga a desplazamiento horizontal para completar una categoría.
- **Carruseles:** manuales, sin autoplay. Controles visibles de al menos 44 px, desplazamiento por teclado, `scroll-snap` y una tarjeta parcial como pista de continuidad. No se usan puntos como único control.
- **Carga y error:** skeleton y error por sección; un fallo de destacados no reemplaza el hero ni las categorías válidas.
- **ProductCard:** aplica 8.3, incluido el agregado rápido restringido.

### 8.3 Tarjeta de producto

La tarjeta muestra, en este orden: medio con espacio reservado, descuento o promoción vigente, favorito, marca, nombre, precio, disponibilidad y acción. La relación de imagen y el número de líneas del nombre se fijan en el frame aprobado y se mantienen iguales entre tarjetas de la misma grilla.

| Elemento | Regla |
|---|---|
| Imagen | Con `alt` útil cuando existe; si falta, placeholder local “Sin imagen”. No se inventa una imagen ni se rompe la alineación. |
| Descuento | Sólo si F-012 confirma una oferta vigente. Se muestra el porcentaje con texto y el precio actual antes del anterior; nunca depende sólo de color o tachado. |
| Favorito | Acción separada del enlace principal, objetivo de 44 px y nombre “Guardar/Quitar de favoritos”. Requiere sesión y conserva el retorno mediante `O-003`. |
| Nombre y marca | El nombre enlaza a `V-007`; la marca no sustituye al nombre ni se usa como texto decorativo. |
| Precio y disponibilidad | Reflejan la respuesta vigente. Ante fallo se usa “Precio por confirmar” o “Disponibilidad por confirmar”, nunca `S/ 0` ni “Agotado”. |
| Acción | “Agregar” sólo con un SKU vendible resuelto; en producto variable o sin SKU se muestra “Ver opciones” y navega a `V-007`. |

Agregado rápido:

- Sólo aplica cuando el producto expone un único SKU comprable y la disponibilidad permite la acción; no se infiere talla, color ni SKU.
- No se anida dentro del enlace de la tarjeta; es un control independiente con foco visible.
- Durante el envío queda ocupado y no acepta doble pulsación; el éxito usa `O-005` y el error se explica junto a la tarjeta con reintento.
- Con precio o stock “por confirmar” el agregado rápido no se habilita.

Estados mínimos: default, hover, foco visible, favorito guardando/guardado, sin imagen, precio por confirmar, agotado, producto no disponible y skeleton de carga.

### 8.4 Catálogo y filtros

- Encabezado con título o consulta, cantidad de resultados, acceso a filtros y orden; chips de criterios aplicados.
- Desktop: panel lateral de filtros. Mobile: `O-001`. El panel no comprime la grilla por debajo del ancho mínimo de tarjeta del frame.
- Opciones vigentes: categoría, marca y rango de precio. No se agregan facetas sin contrato.
- Aplicar o limpiar actualiza la URL y reinicia la página; cancelar en mobile conserva los criterios aplicados.
- Vacío, error y “por confirmar” son estados distintos (8.8). Un fallo de precio/stock no convierte la grilla en vacía.
- Al paginar o aplicar criterios, el foco llega al encabezado de resultados y la cantidad se anuncia sin mover el foco.

### 8.5 Carrito y resumen

- Lista semántica de líneas y resumen; en mobile el resumen aparece después de las líneas y no se fija un CTA que oculte controles o avisos.
- El resumen desktop puede permanecer visible dentro de su columna sólo si no tapa pie, avisos ni acciones.
- Subtotal informativo, sin envío, descuentos ni total final. Una línea en atención se explica antes del CTA y lo bloquea hasta corregirse.
- Cantidad, quitar y mover a favoritos conservan foco y estados locales; los cambios confirmados no se anuncian como totales de checkout.

### 8.6 Overlays

Se reservan para tareas que requieren atención o feedback superpuesto. Aplican a `O-001` a `O-010`.

- Scrim Ink semitransparente que separa el contenido sin sustituir el contraste del texto.
- Modal con `radius/lg`; drawer mobile a pantalla parcial o completa con áreas seguras. No se mezclan dos overlays de la misma tarea.
- Encabezado con título y cierre de 44 px; `aria-modal`, nombre accesible y foco inicial en el título o primer control.
- Foco atrapado, Escape cuando sea seguro y restauración al disparador. El fondo queda inerte y sin desplazamiento.
- Acciones destructivas se confirman explícitamente y nunca son la acción predeterminada.
- Toasts y banners siguen `O-010`: deduplicados, sin mover foco, con acción concreta. Sólo éxito o información sin acción pueden cerrarse solos, después de tiempo suficiente y pausando el cierre con hover o foco.
- Los overlays usan los tokens vigentes; no introducen una paleta propia.

### 8.7 Carga y skeletons

El skeleton aproxima la estructura final y reserva su espacio para evitar saltos. Se usa por región (tarjeta, listado, ficha, carrito, resumen y pedido); no reemplaza toda la página cuando ya existe contenido útil. Un grupo de skeletons tiene un único anuncio accesible y respeta `prefers-reduced-motion`. El spinner se limita a acciones o regiones pequeñas.

### 8.8 Estados consistentes

Todas las vistas definen en su sección de estados los casos aplicables: **cargando, vacío, error y por confirmar**. “Por confirmar” no es un error, un vacío ni un agotado.

| Estado | Cuándo | Tratamiento visual y de contenido | Acción | Nunca |
|---|---|---|---|---|
| Cargando | Lectura inicial o actualización de una región | Skeleton con la forma final; cabecera y contenido válido permanecen operativos | Esperar o navegar | Mostrar datos ficticios, precios en cero o un vacío prematuro |
| Vacío | Respuesta válida sin elementos | Superficie neutra, explicación breve y salida útil | Explorar, limpiar o corregir | Estilo de error, culpar al usuario o dejar la vista en blanco |
| Error | Fallo de red, proveedor o validación no recuperable en el sitio | Superficie de error, qué ocurrió y qué puede hacer; conserva criterios y contexto | Reintentar o volver | Presentarlo como vacío, “agotado” o pérdida de datos |
| Por confirmar | Precio, stock u otro proveedor no respondió pero la vista sigue siendo útil | Superficie de advertencia con texto “Por confirmar”; el dato no se afirma y la compra se bloquea con explicación | Reintentar el dato | `S/ 0`, “Agotado”, éxito simulado o error técnico crudo |
| No disponible | Recurso inexistente, inactivo o `404` | Estado neutral, sin contenido parcial | Volver al catálogo o actualizar | Reutilizar el estilo de error técnico o mostrar una ficha incompleta |

Reglas transversales:

- Un fallo regional no reemplaza una página con contenido válido; el error se limita a la región afectada.
- Cargando y resultados usan `role="status"`/`aria-live="polite"`; los errores que bloquean usan `alert` sin mover el foco de forma inesperada.
- Ningún estado depende sólo de color: siempre hay texto y, cuando aporte, icono.
- El copy explica primero qué ocurrió y después la recuperación. No se muestran códigos HTTP, IDs de traza ni nombres de proveedores.
- La evidencia de implementación incluye una captura por estado aplicable, en desktop y mobile, del mismo SHA. Una vista no se acepta si puede quedar en blanco ante un proveedor que no responde.

### 8.9 Pie global

- Agrupa marca, ayuda, políticas y navegación secundaria; no repite la acción principal de la vista.
- Sólo publica enlaces con destino aprobado. Si un destino no existe, se omite o se muestra como texto no interactivo; no se crean enlaces ficticios.
- Desktop en columnas legibles; mobile puede usar acordeones accesibles. Mantiene contraste, foco visible y orden de lectura.
- El copyright y los enlaces legales no se anuncian como navegación principal.

## 9. Accesibilidad

- WCAG 2.2 AA como mínimo.
- Orden de foco equivalente al orden lógico y visual.
- Un `h1` por pantalla y encabezados jerárquicos.
- Formularios con label, ayuda y error asociados.
- Estados anunciados mediante `status` o `alert` según severidad.
- Imágenes de producto con texto alternativo; decoración oculta.
- Controles táctiles principales de al menos 44 × 44 px.
- Sin carruseles automáticos; animaciones respetan `prefers-reduced-motion`.
- Ninguna información depende sólo de color, posición, hover o gesto.

## 10. Organización y versionado de Figma

El archivo **Sistema de Diseño** enlazado arriba es la biblioteca de Foundations, marca, componentes y patrones. La [carpeta de mockups de vistas](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394) es un espacio distinto para las pantallas del Marketplace. El archivo de pantallas identificado es [Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups); la página [Inicio, catálogo y producto](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-3) contiene las secciones de Inicio, Catálogo y Ficha. Las specs [V-005](vistas/V-005-inicio.md) y [V-006](vistas/V-006-catalogo-resultados.md) ya enlazan sus respectivas secciones y sus 34 frames desktop/mobile localizados. El [archivo Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) contiene la [página Checkout](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=1-5), verificada el 18/10; los enlaces representativos de V-010–V-014 figuran en cada spec. La existencia del frame no equivale a aprobación de contenido.

La sección [Mockups H5](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-560) es la referencia aprobada el 24/11/2026 para shell, inicio, catálogo, ficha, carrito y checkout. El [benchmark](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=537-565) documenta el análisis previo y no sustituye los frames de entrega. Los enlaces por frame de V-007 y V-008 y de los estados restantes se completan en el seguimiento de [#142](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/142); mientras falten, la vista se considera aprobada en dirección visual pero no en trazabilidad frame a frame.

Páginas mínimas sugeridas para la biblioteca del sistema de diseño:

1. `00 — Readme y changelog`
2. `01 — Foundations`
3. `02 — Brand`
4. `03 — Components`
5. `04 — Patterns`
6. `05 — Playground y QA`

Frames de pantalla:

```text
V-### / Desktop|Mobile / Estado
```

Componentes:

```text
Categoría / Componente / Variante
```

Cada frame indica `DS-001 v0.3.0` y enlaza su spec.

El orden desktop→mobile de checkout (`V-010` a `V-014`) fue una intención de producción ya superada: se hallaron variantes en ambas plataformas. El [índice de vistas](vistas/README.md) registra conteos y discrepancias. Conservar ambos formatos, completar estados faltantes y conciliar el contenido de V-014 con el contrato antes de pasar a `Aprobada`.

## 11. Gobernanza

- La biblioteca central contiene Foundations, marca, componentes y patrones compartidos.
- Los módulos consumen instancias y mantienen sus pantallas en archivos de trabajo.
- Un componente específico permanece local hasta demostrar reutilización.
- No se editan ni separan componentes maestros dentro del archivo de pantallas.

Para proponer un cambio:

1. Confirmar que la necesidad no esté cubierta.
2. Documentar problema y vistas afectadas.
3. Proponer la solución en el archivo del módulo.
4. Incluir variantes, estados, responsive, contenido y accesibilidad.
5. Revisar con el responsable de biblioteca.
6. Tras aprobación, incorporar, documentar, versionar y publicar.

Versionado:

- `0.2.x`: consolidación preliminar antes del hito.
- `0.3.0`: dirección visual H5 aprobada; patrones de shell, tarjeta, carrito, overlays y estados consistentes documentados.
- `0.3.x`: ajustes de patrón o enlaces de frames sin cambio de tokens ni de contratos.
- `1.0.0`: identidad, stack UI, tokens, componentes y gobernanza aprobados.

## 12. Uso desde las specs UI

Cada spec `F-###` o `V-###` indica:

- versión de `DS-001`;
- componentes y patrones usados;
- estados necesarios;
- excepciones o componentes nuevos;
- frame desktop, mobile y prototipo;
- criterios de accesibilidad particulares.

Una spec de vista no vuelve a declarar tokens base salvo que proponga un cambio a este sistema.

## 13. Decisiones abiertas

| ID | Decisión pendiente | Impacto |
|---|---|---|
| `DS-OPEN-01` | Autoría/licencia, SVG, versión inversa, favicon, área de seguridad y tamaño mínimo del logo. | Identidad final |
| `DS-OPEN-02` | Responsable único de biblioteca y canal de propuestas. | Gobernanza |
| `DS-OPEN-03` | Definir UI kit global para familias distintas del slice Checkout. Para Checkout F-022–F-027 se decidió usar los componentes propios/tokens existentes, sin Mantine. | Implementación transversal |
| `DS-OPEN-04` | Completar diez tonalidades de Volt, Signal, Ink y Cloud. | Tema Mantine |
| `DS-OPEN-05` | Verificar la correspondencia entre tokens de Figma/DS-001 y `src/theme/tokens.css` del frontend; no presuponer un `theme.ts` ni una biblioteca aún no instalada. | Código-diseño |
| `DS-OPEN-06` | **Resuelta para H5:** patrones de shell, ProductCard, filtros, carrito, overlays y estados documentados en la sección 8. La publicación de la biblioteca de componentes sigue pendiente de implementación y revisión. | Mockups |
| `DS-OPEN-07` | **Parcial:** dirección visual H5 aprobada y enlazada; V-005/V-006 conservan frames H3 y la sección H5. Faltan enlaces por frame de V-007/V-008, estados y prototipo, y la conciliación de frames heredados de checkout. | Trazabilidad Figma |
| `DS-OPEN-08` | **Resuelta:** changelog incorporado en la sección 15; la publicación de la biblioteca mantiene el proceso de la sección 11. | Mantenimiento |
| `DS-OPEN-09` | Completar los enlaces individuales de frames H5 de V-007, V-008 y de cada estado/overlay aprobado; no cambiar el diseño durante ese registro. | Trazabilidad Figma |
| `DS-OPEN-10` | Confirmar en implementación la correspondencia de los patrones 8.1–8.9 con los frames aprobados y registrar diferencias antes de la aceptación visual. | Código-diseño |

## 14. Fuentes

- **Guía UX UI del Marketplace Multicanal — Inka Athletics**, documento preliminar de 43 páginas recibido el 28 de septiembre de 2026.
- Archivo central de Figma y nodo de logos enlazados en metadatos.
- Logos Ink, Volt y Signal recibidos en PNG e incorporados a `SPECS/ui/sistema-diseno/assets/logos/`.
- Specs funcionales, UI y contratos `F-001` a `F-040`.
- Wireframes históricos como referencia, no como fuente vigente.
- Nike y Adidas únicamente como inspiración de experiencia, sin reutilización de identidad ni activos.

## 15. Changelog

| Versión | Fecha | Cambio | Compatibilidad |
|---|---|---|---|
| `0.3.0` | 2026-11-24 | Dirección visual H5 aprobada en #141 por el revisor principal. Se documentan shell global, inicio, ProductCard con agregado rápido restringido, catálogo, carrito, overlays, skeletons y estados consistentes (cargando, vacío, error, por confirmar, no disponible). V-005 a V-008 quedan habilitadas para implementar. | Sin cambios de tokens, props ni contratos. Los frames aprobados reutilizan Foundations 5.1–5.7. La aceptación de cada vista y de la biblioteca sigue siendo independiente. |
| `0.2.0` | 2026-10-18 | Identidad Inka Athletics, tokens, tipografía, UI kit preliminar, accesibilidad y gobernanza. | Reemplaza los tokens provisionales de `0.1.0`. |
