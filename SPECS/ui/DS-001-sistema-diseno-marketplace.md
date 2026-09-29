# DS-001 — Sistema de diseño de Inka Athletics

> Especificación UI transversal para los mockups de Figma y la futura interfaz web del Canal Marketplace. Consolida la guía UX/UI preliminar, los recursos de marca recibidos y las reglas vigentes de las specs `F-001` a `F-040`.

## 1. Metadatos y estado

| Campo | Valor |
|---|---|
| ID | `DS-001` |
| Nombre | Sistema de diseño de Inka Athletics |
| Versión | `0.2.0` |
| Estado | Borrador avanzado para el hito de mockups; pendiente de aprobación final |
| Custodio | Giuliano Macchiavello |
| Revisor principal | Jim Segovia |
| Marca | Inka Athletics |
| Herramienta oficial | Figma |
| Archivo central de Figma | [Sistema de Diseño](https://www.figma.com/design/rKPdRQHLLUkYk5VdiEErqZ/Sistema-De-Dise%C3%B1o?node-id=57-15&t=eO6m1Plz1xQ5sFgn-1) |
| Sección de logos en Figma | [Logos de Inka Athletics](https://www.figma.com/design/rKPdRQHLLUkYk5VdiEErqZ/Sistema-De-Dise%C3%B1o?node-id=56-7&t=0TSK36SaklUJeiyS-4) |
| Implementación descrita por la guía preliminar | React + TypeScript + Mantine `9.6.2` + Tabler Icons |
| Última actualización | 2026-09-28 |
| Alcance | Canal Marketplace web responsive y componentes compartidos |

### 1.1 Vigencia y decisión técnica preliminar

Este documento es la fuente visual vigente para los mockups. La versión `0.2.0` incorpora la identidad Inka Athletics y reemplaza los tokens provisionales de `DS-001` v0.1.0.

La guía recibida define Mantine `9.6.2` y Tabler Icons como base de implementación. Otros documentos todavía mencionan Tailwind CSS, shadcn/ui, Radix UI y Lucide React. Para no mezclar dos sistemas:

- los mockups y la biblioteca de Figma seguirán los tokens y propiedades documentados aquí;
- Mantine + Tabler se consideran la dirección técnica preliminar más reciente del UI Kit;
- antes de implementar frontend, el equipo debe aprobar esa migración y actualizar los documentos que aún indiquen el stack anterior;
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
| Confirmación/pago | `filled` | `accent/signal` | Blanco |
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

- `ActionIcon`, `ProductCard`, `ProductGallery`, `CartLine`, `OrderSummary`.
- `Breadcrumb`, `Alert`, `Skeleton`, `Modal`, panel mobile, `EmptyState`, `Toast`.
- Navegación global/mobile y línea de tiempo de pedido/despacho.

Los componentes compuestos se completarán desde las specs por vista; no se aprueban sólo por aparecer en esta lista.

## 8. Patrones comunes

### 8.1 Tarjeta de producto

Debe mostrar imagen con espacio reservado, marca/nombre, precio/promoción cuando aplique, disponibilidad, favorito y navegación a ficha. Pendiente: proporción definitiva, máximo de líneas, truncamiento, acción por contexto, responsive y estados.

### 8.2 Navegación

Identifica marca y mantiene acceso a búsqueda, catálogo, cuenta, favoritos y carrito. En móvil ninguna acción esencial depende de hover. Pendiente: orden definitivo, sticky, breakpoint, menú mobile y estados.

### 8.3 Filtros

Panel lateral en desktop y panel accesible en móvil. Muestra filtros activos, cantidad cuando exista, Aplicar, Limpiar y retiro individual sin perder contexto. Opciones vigentes: categoría, marca y rango de precio.

### 8.4 Modales y overlays

Se reservan para tareas que requieren atención. Tienen nombre accesible, foco atrapado, Escape cuando sea seguro y restauración de foco. En móvil pueden convertirse en panel de pantalla completa.

### 8.5 Carga y skeletons

El skeleton aproxima la estructura final. Se requieren patrones para tarjeta, listado, ficha, carrito, resumen y pedido. Spinner se limita a acciones o regiones pequeñas.

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

El archivo central enlazado contiene Foundations, marca, componentes y patrones. Las pantallas del Marketplace pueden vivir en un archivo de módulo que consuma esa biblioteca.

Páginas mínimas sugeridas:

1. `00 — Readme y changelog`
2. `01 — Foundations`
3. `02 — Brand`
4. `03 — Components`
5. `04 — Patterns`
6. `05 — Playground y QA`

Frames de pantalla:

```text
V-### / Estado / Desktop|Mobile
```

Componentes:

```text
Categoría / Componente / Variante
```

Cada frame indica `DS-001 v0.2.0` y enlaza su spec.

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
- `0.3.0`: biblioteca inicial y patrones usados por primeras vistas.
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
| `DS-OPEN-03` | Aprobar Mantine + Tabler o definir equivalencia definitiva con el stack histórico. | Implementación |
| `DS-OPEN-04` | Completar diez tonalidades de Volt, Signal, Ink y Cloud. | Tema Mantine |
| `DS-OPEN-05` | Enlazar `src/theme/theme.ts` en el frontend. | Código-diseño |
| `DS-OPEN-06` | Completar ProductCard, navegación, modales, filtros y skeletons desde specs por vista. | Mockups |
| `DS-OPEN-07` | Registrar archivo de pantallas/prototipo del Marketplace. | Trazabilidad Figma |
| `DS-OPEN-08` | Definir changelog y proceso de publicación. | Mantenimiento |

## 14. Fuentes

- **Guía UX UI del Marketplace Multicanal — Inka Athletics**, documento preliminar de 43 páginas recibido el 28 de septiembre de 2026.
- Archivo central de Figma y nodo de logos enlazados en metadatos.
- Logos Ink, Volt y Signal recibidos en PNG e incorporados a `SPECS/ui/sistema-diseno/assets/logos/`.
- Specs funcionales, UI y contratos `F-001` a `F-040`.
- Wireframes históricos como referencia, no como fuente vigente.
- Nike y Adidas únicamente como inspiración de experiencia, sin reutilización de identidad ni activos.
