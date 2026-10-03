# Plan de preparación y reparto de vistas para mockups

> Este plan termina cuando los cinco integrantes del equipo UI reciben un paquete de vistas completamente especificado y listo para empezar a diseñar en Figma. No incluye base de datos, implementación frontend ni preparación de la exposición del hito.

## 1. Metadatos

| Campo | Valor |
|---|---|
| Versión | `0.2.0` |
| Estado | Preparado para validación y aceptación del equipo |
| Fecha | 2026-09-28 |
| Última actualización | 2026-10-02 |
| Equipo | Diego Espinoza, Fernando José Saire Tello, Giuliano Macchiavello, Sebastián Malca y Jim Segovia |
| Punto de inicio | `DS-001` v0.2.0 consolidado de forma preliminar, tres logos incorporados, enlaces de Figma registrados, 40 specs UI por funcionalidad y documentación histórica de 15 pantallas |
| Estado alcanzado | Inventario de 29 piezas validado documentalmente y cinco paquetes equilibrados preparados; faltan aceptación, decisiones abiertas, enlaces de frames y revisión humana |
| Punto de cierre | Cinco paquetes de diseño aceptados, revisados y con Definition of Ready completada |

## 2. Objetivo

Preparar una fuente de verdad visual suficientemente clara para repartir el diseño sin que cada integrante tenga que interpretar por su cuenta requisitos, estados, componentes o navegación.

Al cerrar este plan, cada integrante debe conocer:

- qué vistas le corresponden;
- qué funcionalidades `F-###` implementa cada vista;
- qué versiones desktop y mobile debe producir;
- qué estados, overlays y comunicaciones debe diseñar;
- qué componentes del sistema de diseño debe usar;
- qué decisiones continúan abiertas;
- quién revisará su trabajo.

## 3. Estado de las condiciones para repartir

| Condición | Situación actual | Siguiente acción |
|---|---|---|
| Sistema de diseño parcialmente consolidado | `DS-001` v0.2.0 integra la guía preliminar, tres logos y los enlaces de Figma. Siguen pendientes SVG, versión inversa, licencias, responsable de biblioteca y stack UI. | Resolver o asignar `DS-OPEN-01` a `DS-OPEN-08`. |
| Catálogo visual | **Resuelto documentalmente:** 17 vistas, 10 overlays y 2 comunicaciones vigentes. | Aprobación humana del catálogo. |
| Specs por pieza | **Resuelto documentalmente:** las 29 piezas declaran composición, estados, responsive, accesibilidad, navegación y frames. | Revisión cruzada y resolución de decisiones abiertas. |
| Rutas, overlays y comunicaciones | **Resuelto:** identificadores `V`, `O` y `C` separados y navegación actualizada. | Mantener trazabilidad al diseñar. |
| Estimación visual | **Resuelto:** 226 puntos visuales + 4 de gobernanza, con factores auditables. | Ajustar sólo si el equipo modifica el alcance. |
| Paquetes individuales | **Preparados:** cinco documentos ejecutables, entre 42 y 49 puntos. | Cada integrante debe aceptar su paquete y completar su Definition of Ready. |
| Figma de mockups | [Carpeta de vistas](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394) registrada, distinta del archivo de la biblioteca `DS-001`. El enlace recibido lleva a una carpeta, no al archivo de pantallas. | Registrar URL directa del archivo, páginas y frames cuando estén disponibles. |

## 4. Principios para organizar la documentación

1. Las specs `SPECS/ui/F-###` siguen describiendo el comportamiento visual de cada funcionalidad.
2. Las nuevas specs `V-###` describen la composición completa de una ruta o pantalla.
3. Las nuevas specs `O-###` describen overlays reutilizables o interacciones superpuestas relevantes.
4. Las nuevas specs `C-###` describen comunicaciones visuales, como correos.
5. Una vista puede reunir varias funcionalidades; no se crea un frame independiente por cada `F-###`.
6. Las specs históricas sirven como fuente, pero no pueden contradecir a las specs vigentes.
7. Figma representa las specs aprobadas; no introduce comportamiento nuevo sin documentarlo primero.

## 5. Fase 1 — Reunir y consolidar el sistema de diseño

**Estado al 2026-09-28:** en progreso. La guía preliminar fue revisada, `DS-001` se actualizó a `0.2.0`, los enlaces de Figma quedaron registrados, los logos Ink, Volt y Signal se incorporaron al repositorio y se confirmó que los cinco integrantes tienen acceso al archivo de Figma. Esta fase aún no está cerrada porque quedan recursos y decisiones de gobernanza/implementación pendientes.

### 5.1 Crear el paquete de fuentes

Crear esta estructura:

```text
SPECS/ui/sistema-diseno/
├── README.md
├── marca-y-logotipo.md
├── recursos-y-licencias.md
├── figma-y-versionado.md
└── assets/
    ├── logos/
    ├── iconos/
    └── referencias/
```

### 5.2 Inventariar la información disponible

- [x] Recibir los logos Ink, Volt y Signal disponibles en PNG.
- [ ] Recibir las variantes restantes: SVG maestro, versión inversa, favicon e isotipo reducido.
- [x] Recibir y revisar el documento preliminar de diseño de 43 páginas.
- [x] Registrar en `DS-001` el enlace oficial de Figma y el nodo de logos.
- [x] Confirmar que los cinco integrantes del equipo tienen acceso al archivo de Figma.
- [x] Identificar y documentar paleta, tipografías, iconografía, superficies, motivo gráfico y tono verbal.
- [ ] Completar reglas y fuentes de fotografía e ilustración.
- [ ] Registrar origen y licencia de cada recurso.
- [x] Separar decisiones vigentes, contenido preliminar y pendientes mediante el estado y la sección `DS-OPEN`.
- [x] Detectar y documentar la contradicción entre Mantine/Tabler y el stack histórico Tailwind/shadcn/Lucide.

### 5.3 Actualizar `DS-001`

El documento debe dejar cerrados o explícitamente pendientes:

- identidad, versiones del logo y usos incorrectos;
- colores semánticos y combinaciones de contraste;
- tipografías, pesos, escala y fallbacks;
- espaciado, grilla, breakpoints, radios, bordes y elevaciones;
- iconografía e imágenes;
- patrones de cabecera, navegación, catálogo, ficha, carrito, checkout y pedidos;
- componentes y todas sus variantes visuales;
- reglas responsive y accesibilidad;
- estructura, URL y versionado de Figma;
- convención de nombres para páginas, componentes y frames.

### 5.4 Criterio de cierre

La fase se cierra cuando:

- [x] `DS-001` alcanza la versión `0.2.0`.
- [ ] `DS-OPEN-01` a `DS-OPEN-04` están resueltos o tienen responsable y fecha.
- [ ] Existe una única fuente aprobada para cada logo, token y componente; por ahora los PNG son evidencia recibida y Figma debe aportar los maestros.
- [ ] Los cinco integrantes entienden cómo construir una vista sin inventar estilos.

## 6. Fase 2 — Corregir la arquitectura documental de UI

**Estado al 2026-09-28:** completada. La nomenclatura, los índices y las plantillas ya existen. El documento de 15 pantallas quedó identificado como antecedente con correspondencia al catálogo vigente, y el diagrama de navegación fue sustituido por el flujo actual de 17 vistas, overlays y comunicaciones.

### 6.1 Actualizar nomenclatura

Agregar a `SPECS/NOMENCLATURA-SDD.md`:

| Prefijo | Significado | Ejemplo |
|---|---|---|
| `V-###` | Vista o ruta principal | `V-007-ficha-producto.md` |
| `O-###` | Overlay o feedback superpuesto | `O-002-visor-galeria.md` |
| `C-###` | Comunicación visual externa | `C-001-correo-confirmacion.md` |

### 6.2 Crear estructura e índices

```text
SPECS/ui/
├── vistas/
│   ├── README.md
│   ├── PLANTILLA.md
│   └── V-001 ... V-017
├── overlays/
│   ├── README.md
│   ├── PLANTILLA.md
│   └── O-001 ... O-010
└── comunicaciones/
    ├── README.md
    ├── PLANTILLA.md
    ├── C-001-correo-confirmacion-pedido.md
    └── C-002-correo-actualizacion-despacho.md
```

### 6.3 Tratar los documentos históricos

- [x] Añadir una advertencia de antecedente al documento de 15 pantallas.
- [x] Conservarlo para trazabilidad; no eliminarlo.
- [x] Sustituir su inventario vigente por enlaces a los catálogos nuevos y conservar la correspondencia histórica.
- [x] Actualizar el diagrama de navegación con las rutas vigentes.
- [x] Eliminar del flujo actual el formulario de tarjeta antiguo: F-025 define pago simulado sin tarjeta ni CVV.
- [x] Resolver “modal o vista” en acceso: las rutas vigentes son pantallas; el overlay sólo redirige y conserva retorno.

### 6.4 Criterio de cierre

- [x] La nomenclatura está documentada.
- [x] Existen índices y plantillas para vista, overlay y comunicación.
- [x] El documento histórico ya no puede confundirse con la fuente vigente.
- [x] El diagrama de navegación refleja el catálogo actual.

## 7. Fase 3 — Especificar el catálogo visual vigente

**Estado al 2026-09-28:** catálogo visual completamente especificado y estimado en borrador: 17 vistas, 10 overlays y 2 comunicaciones están en revisión. El reparto ya fue preparado; faltan resolver o clasificar decisiones abiertas, incorporar enlaces finales de Figma y obtener la aprobación humana.

### 7.1 Vistas principales

| ID | Vista | Ruta | Funcionalidades |
|---|---|---|---|
| `V-001` | Login | `/login` | F-002, F-020 |
| `V-002` | Registro | `/registro` | F-001 |
| `V-003` | Recuperación de contraseña | `/recuperar-contrasena` | F-004 |
| `V-004` | Restablecimiento de contraseña | `/restablecer-contrasena` | F-005 |
| `V-005` | Inicio | `/` | F-006, F-036 |
| `V-006` | Catálogo y resultados | `/catalogo` | F-007–F-010, F-036 |
| `V-007` | Ficha del producto | `/productos/{slug}` | F-011–F-016, F-036 |
| `V-008` | Carrito | `/carrito` | F-017–F-021 |
| `V-009` | Favoritos | `/favoritos` | F-037–F-039 |
| `V-010` | Dirección de envío | `/checkout/direccion` | F-022 |
| `V-011` | Resumen, envío y beneficio | `/checkout/resumen` | F-023, F-024 |
| `V-012` | Pago simulado | `/checkout/pago` | F-025 |
| `V-013` | Creación de la orden | `/checkout/confirmacion` | F-026 |
| `V-014` | Pedido confirmado | `/checkout/confirmado/{orderId}` | F-027, F-034 |
| `V-015` | Historial de pedidos | `/mis-pedidos` | F-028, F-029 |
| `V-016` | Detalle y reordenado | `/mis-pedidos/{orderId}` | F-030, F-031 |
| `V-017` | Seguimiento | `/mis-pedidos/{orderId}/seguimiento` | F-032 |

### 7.2 Overlays y comunicaciones

| ID | Elemento | Funcionalidades relacionadas |
|---|---|---|
| `O-001` | Filtros mobile | F-008, F-029 |
| `O-002` | Visor de galería | F-011 |
| `O-003` | Autenticación requerida con retorno | F-002, F-021, F-036 |
| `O-004` | Confirmación de cierre durante checkout | F-003 |
| `O-005` | Producto agregado al carrito | F-016 |
| `O-006` | Deshacer eliminación | F-018, F-038 |
| `O-007` | Resultado de fusión de carrito | F-020 |
| `O-008` | Resultado de reordenado | F-031 |
| `O-009` | Evaluación postentrega | F-040 |
| `O-010` | Alertas y feedback global | Transversal |
| `C-001` | Correo de confirmación de pedido | F-033, F-034 |
| `C-002` | Correo de actualización de despacho | F-033, F-035 |

### 7.3 Contenido obligatorio de cada spec por vista

- [x] Metadatos, responsable, versión y estado.
- [x] Ruta, actor, permisos y condiciones de entrada.
- [x] Lista de funcionalidades relacionadas.
- [x] Jerarquía visual de regiones y componentes.
- [x] Textos y acciones principales.
- [x] Estado principal desktop y mobile.
- [x] Estados aplicables: carga, vacío, error, validación, no disponible, conflicto y éxito.
- [x] Overlays, feedback y comunicaciones asociados.
- [x] Entradas y salidas de navegación.
- [x] Conservación de filtros, carrito, sesión o retorno cuando aplique.
- [x] Reglas responsive y accesibilidad.
- [x] Lista exacta de frames requeridos.
- [x] Criterios de aceptación visuales.
- [ ] Enlace de Figma, inicialmente pendiente y luego obligatorio.

## 8. Fase 4 — Estimar antes de repartir

**Estado al 2026-09-28:** completada. Los 29 entregables fueron puntuados en [`SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md`](../SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md). La carga visual suma 226 puntos y se añadieron 4 puntos de gobernanza de `DS-001`, para un total de 230.

No se debe repartir por número de pantallas. Se usará una puntuación simple:

| Factor | 0 puntos | 1 punto | 2 puntos |
|---|---|---|---|
| Complejidad de layout | Simple | Media | Alta |
| Formularios | Ninguno | Corto | Largo/múltiple |
| Estados visuales | 1–2 | 3–4 | 5 o más |
| Responsive | Cambio menor | Reorganización | Patrón distinto |
| Overlays/interacciones | Ninguno | Uno | Varios |
| Dependencias funcionales | 1 F | 2–3 F | 4 o más F |

Cada vista tendrá una estimación de 0 a 12. Después se sumarán también overlays y correos. El reparto se considera equilibrado cuando las cargas totales son cercanas, aunque la cantidad de vistas sea distinta.

## 9. Reparto equilibrado entre los cinco integrantes

Este reparto se ajustó después de estimar las 29 piezas. Mantiene flujos coherentes y distribuye componentes transversales para que la diferencia entre la carga más alta y la más baja sea menor al 20 %. Falta la aceptación humana del equipo.

| Integrante | Paquete | Vistas y elementos | Puntos |
|---|---|---|---:|
| Giuliano Macchiavello | Sistema de diseño, acceso y confirmación | Custodia de `DS-001`; `V-001`–`V-004`; `O-003`, `O-004`; `C-001` | **49** |
| Fernando José Saire Tello | Descubrimiento, producto y feedback global | `V-005`–`V-007`; `O-002`, `O-010` | **49** |
| Sebastián Malca | Carrito, favoritos y filtros mobile | `V-008`, `V-009`; `O-001`, `O-005`–`O-007` | **43** |
| Jim Segovia | Checkout | `V-010`–`V-014` | **42** |
| Diego Espinoza | Pedidos, postentrega y despacho | `V-015`–`V-017`; `O-008`, `O-009`; `C-002` | **47** |

### Revisores cruzados

| Autor | Revisor principal | Aspecto |
|---|---|---|
| Giuliano | Jim | Claridad de flujos de acceso y producto |
| Fernando | Giuliano | Consistencia visual y componentes |
| Sebastián | Diego | Estados, accesibilidad y trazabilidad |
| Jim | Fernando | Coherencia visual y continuidad del flujo de checkout |
| Diego | Sebastián | Responsive, contenido y continuidad de pedidos |

Resultado: mínimo 42, máximo 49 y diferencia conservadora de `16.7 %` respecto al paquete menor. El reparto cumple el límite del 20 %. Los cálculos y factores están en el inventario enlazado.

## 10. Definition of Ready para entregar un paquete a un diseñador

Ninguna vista se asigna formalmente hasta cumplir lo siguiente:

- [x] Tiene ID `V-###`, nombre y ruta definidos.
- [x] Tiene responsable y revisor.
- [x] Enlaza todas sus specs `F-###` vigentes.
- [x] Declara los frames desktop y mobile requeridos.
- [x] Declara estados críticos y overlays.
- [x] Fue contrastada documentalmente con contratos API y reglas funcionales disponibles.
- [x] Usa componentes y tokens de `DS-001` o registra la necesidad de coordinación.
- [x] Tiene microcopy principal y mensajes de error relevantes.
- [x] Declara navegación de entrada, salida y retorno.
- [x] Incluye criterios de accesibilidad.
- [x] Tiene estimación de complejidad.
- [x] No conserva decisiones obsoletas del documento de 15 pantallas.
- [ ] Fue revisada por otra persona.

Los requisitos documentales ya están cubiertos. El último punto permanece abierto porque exige una acción humana posterior al reparto.

## 11. Paquete de entrega para cada integrante

Los paquetes ya están materializados en [`SPECS/ui/reparto/`](../SPECS/ui/reparto/README.md). Cada uno contiene su tabla de entregables, frames exactos, dependencias, decisiones abiertas, secuencia recomendada y checklist de aceptación/revisión.

Cada persona debe recibir una fila o tablero con:

| Campo | Contenido |
|---|---|
| Responsable | Nombre del diseñador |
| Vista | ID, nombre y ruta |
| Spec | Enlace al archivo `V-###` |
| Funcionalidades | Lista `F-###` |
| Sistema de diseño | Versión de `DS-001` |
| Frames | Lista exacta desktop/mobile/estado |
| Overlays | IDs `O-###` relacionados |
| Componentes | Instancias requeridas de la biblioteca |
| Complejidad | Puntuación y observaciones |
| Pendientes | Decisiones que no bloquean o que deben resolverse |
| Revisor | Nombre y fecha de revisión |

## 12. Secuencia de ejecución recomendada

| Paso | Actividad | Resultado |
|---:|---|---|
| 1 | Reunir logos, documento y Figma | Paquete de fuentes completo |
| 2 | Consolidar y aprobar `DS-001` | Reglas visuales compartidas |
| 3 | Actualizar nomenclatura y carpetas | Arquitectura documental lista |
| 4 | Confirmar catálogo `V/O/C` | Inventario visual cerrado |
| 5 | Redactar specs por vista | Frames y estados definidos |
| 6 | Actualizar navegación y trazabilidad | Flujos coherentes |
| 7 | Estimar cada vista | Carga comparable |
| 8 | Ajustar y preparar reparto | Cinco paquetes equilibrados y documentados |
| 9 | Aceptar y revisar paquetes con Definition of Ready | Inicio seguro del trabajo en Figma |

## 13. Criterio de finalización de este plan

Este plan termina —y recién entonces comienza el diseño distribuido— cuando:

- [ ] El sistema de diseño está consolidado y versionado.
- [ ] El catálogo de vistas, overlays y comunicaciones está aprobado.
- [ ] Todas las vistas tienen una spec de composición revisada.
- [x] El diagrama de navegación coincide con las vistas vigentes.
- [x] Cada vista tiene lista de frames y estimación.
- [x] La diferencia de carga entre integrantes fue calculada y documentada.
- [ ] Cada uno de los cinco recibió su paquete con Definition of Ready.
- [ ] El equipo confirmó el reparto antes de crear mockups finales.

### Avance verificable previo a la aceptación

- [x] Existen cinco paquetes individuales enlazados desde un índice común.
- [x] Cada paquete identifica responsable, revisor, carga y dependencias.
- [x] Los 29 entregables aparecen exactamente una vez en el reparto.
- [x] Los nombres de frames de los paquetes coinciden con sus specs.
