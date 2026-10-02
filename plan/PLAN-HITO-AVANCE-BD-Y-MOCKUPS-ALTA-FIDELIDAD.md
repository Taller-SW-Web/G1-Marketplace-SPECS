# Plan de trabajo del hito — Base de datos y mockups de alta fidelidad

> Plan de coordinación para producir evidencia verificable del avance del Canal Marketplace: modelo físico inicial de base de datos y mockups web/mobile de alta fidelidad derivados de especificaciones aprobadas.

## 1. Metadatos

| Campo | Valor |
|---|---|
| Versión | `0.1.0` |
| Estado | Borrador para revisión del equipo |
| Fecha de elaboración | 2026-09-28 |
| Fecha de presentación | Próxima semana; fecha exacta por confirmar |
| Alcance | Base de datos, sistema de diseño, especificaciones por vista y mockups de alta fidelidad |
| Equipo de base de datos | Andrés Fernando Morales Usca y Fernando José Saire Tello |
| Equipo de UI/Figma | Diego Espinoza, Leonidas Garcia, Giuliano Macchiavello, Sebastián Malca y Jim Segovia |

## 2. Resultado esperado del hito

Al momento de la presentación, el equipo debe poder demostrar que los avances no fueron diseñados o modelados empíricamente. Cada artefacto debe tener una fuente, un responsable, una versión y una relación trazable con las funcionalidades `F-001` a `F-040`.

Los entregables mínimos son:

1. Sistema de diseño consolidado, con recursos visuales inventariados y `DS-001` actualizado.
2. Catálogo vigente de vistas, overlays, mensajes y correos que deben diseñarse.
3. Especificaciones por vista que compongan las specs UI por funcionalidad existentes.
4. Mockups de alta fidelidad web y mobile construidos con la biblioteca de Figma.
5. Prototipo navegable de los flujos prioritarios y sus estados críticos.
6. Modelo físico inicial de PostgreSQL/Prisma, diagrama ER, migración, datos de prueba y evidencia de validación.
7. Matriz final de trazabilidad entre funcionalidad, vista, frame de Figma, componente y entidad de datos cuando corresponda.

## 3. Resultado de la auditoría documental

### 3.1 Lo que ya existe y se puede reutilizar

- Hay 40 specs UI, una por cada funcionalidad `F-001` a `F-040`.
- `F-011` y `F-012` tienen una estructura UI completa y pueden utilizarse como referencia de profundidad.
- `F-013` y `F-015` tienen desarrollo parcial.
- Las otras 36 specs UI son resúmenes válidos como punto de partida, pero no bastan por sí solas para justificar mockups de alta fidelidad.
- Existe `DS-001` versión `0.1.0`, con principios, tokens, breakpoints, accesibilidad, componentes mínimos y organización propuesta para Figma.
- Existe una especificación histórica de 15 pantallas y un diagrama histórico de navegación.
- La base de datos cuenta con un modelo lógico inicial que define `Cart`, `CartItem`, `WishlistItem`, `CheckoutOperation`, `PostDeliveryPrompt` y `NotificationDelivery`.
- Ya están documentados los límites de propiedad frente a Seguridad, Productos y Ofertas, Ventas y Despacho.

### 3.2 Brechas detectadas

| Brecha | Consecuencia | Acción requerida |
|---|---|---|
| Las specs UI están organizadas por funcionalidad y no por pantalla. | Una misma vista, como ficha de producto o checkout, queda fragmentada entre varios archivos. | Crear una capa de specs por vista que componga las `F-###` sin reemplazarlas. |
| Sólo 2 de 40 specs UI tienen profundidad completa. | Faltan estados, layout, responsive, navegación y criterios visuales verificables en la mayoría de funcionalidades. | Completar primero las specs por vista y ampliar una spec funcional sólo cuando exista una regla visual propia que no pueda quedar en la vista. |
| El catálogo histórico de 15 pantallas quedó desactualizado. | No refleja todas las rutas actuales, el flujo de pago simulado, los correos ni la evaluación postentrega. | Crear un catálogo visual vigente y marcar el documento de 15 pantallas como antecedente. |
| El documento histórico propone formulario de tarjeta. | Contradice `F-025`, que prohíbe solicitar o almacenar tarjeta/CVV y usa confirmación de pago simulado. | La versión vigente debe usar checkbox/confirmación explícita de simulación, sin campos de tarjeta. |
| Login y recuperación aparecen como “modal/vista”. | Deja ambiguo el frame y la navegación. | Adoptar las rutas vigentes `/login`, `/registro`, `/recuperar-contrasena` y `/restablecer-contrasena`; usar overlay sólo para avisar y redirigir con retorno. |
| `DS-001` todavía usa marca provisional. | Los mockups podrían usar logo, colores o tipografías no documentados. | Reunir logos, manual, paleta, tipografías, licencias y enlace de Figma; actualizar `DS-001` antes de repartir vistas. |
| No hay enlace oficial al archivo/biblioteca de Figma. | No se puede verificar versión ni correspondencia entre spec y frame. | Cerrar `DS-OPEN-02` y registrar URL, páginas, responsables y convención de nombres. |
| `SPECS/componentes-react/` sólo contiene una plantilla. | No hay especificaciones implementables de componentes compuestos. | Para este hito, documentar en `DS-001` la biblioteca visual; después crear specs React para los componentes que pasen a implementación. |
| El modelo de base de datos todavía es lógico. | No hay evidencia de PostgreSQL, restricciones, migraciones o datos de prueba. | Derivar un primer esquema físico verificable y documentar las decisiones pendientes. |

### 3.3 Regla de prioridad documental

Cuando exista contradicción, se aplica este orden:

1. Specs vigentes `SPECS/funcional/F-###`.
2. Specs vigentes `SPECS/ui/F-###` y `SPECS/contrato-api/F-###`.
3. `DS-001` y las nuevas specs por vista aprobadas.
4. Modelo lógico y decisiones de arquitectura vigentes.
5. Documentos históricos de épicas, pantallas y specs depreciadas, únicamente como referencia.

## 4. Arquitectura documental propuesta para UI

Las specs por funcionalidad no se deben eliminar. Se añadirá una capa de composición visual, porque una pantalla puede implementar varias funcionalidades y una funcionalidad puede aparecer en varias pantallas.

```text
SPECS/ui/
├── DS-001-sistema-diseno-marketplace.md
├── sistema-diseno/
│   ├── README.md
│   ├── marca-y-logotipo.md
│   ├── recursos-y-licencias.md
│   ├── figma-y-versionado.md
│   └── assets/
│       ├── logos/
│       ├── iconos/
│       └── referencias/
├── vistas/
│   ├── README.md
│   ├── V-001-login.md
│   ├── V-002-registro.md
│   └── ...
├── overlays/
│   ├── README.md
│   ├── O-001-filtros-mobile.md
│   └── ...
└── comunicaciones/
    ├── C-001-correo-confirmacion-pedido.md
    └── C-002-correo-actualizacion-despacho.md
```

Antes de crear estas carpetas se debe actualizar `NOMENCLATURA-SDD.md` para reconocer:

- `V-###`: vista o ruta componible en un frame principal.
- `O-###`: overlay, diálogo, sheet, banner o interacción superpuesta con comportamiento propio.
- `C-###`: comunicación visual fuera de la aplicación, como correos transaccionales.

Cada spec por vista debe incluir:

- ID, nombre, versión, responsable y estado.
- Ruta o condición de aparición.
- Funcionalidades `F-###` que compone.
- Actores y permisos.
- Jerarquía de regiones y componentes.
- Contenido visible y microcopy esencial.
- Estados: carga, vacío, éxito, validación, error, no disponible y conflicto, según aplique.
- Interacciones, entradas, salidas y conservación de contexto.
- Comportamiento desktop, tablet y mobile.
- Accesibilidad: foco, teclado, lectores de pantalla, contraste y objetivos táctiles.
- Overlays/notificaciones usados.
- Enlace exacto al frame desktop, frame mobile y prototipo de Figma.
- Criterios de aceptación visuales y fuentes.

## 5. Catálogo visual que se debe especificar antes de diseñar

### 5.1 Vistas principales

| ID propuesto | Vista/ruta | Funcionalidades principales | Mockups mínimos |
|---|---|---|---|
| `V-001` | Login `/login` | F-002, F-020 | Desktop, mobile, error, MFA y retorno |
| `V-002` | Registro `/registro` | F-001 | Desktop, mobile, validación y confirmación |
| `V-003` | Recuperación `/recuperar-contrasena` | F-004 | Desktop, mobile, éxito neutro y límite |
| `V-004` | Restablecimiento `/restablecer-contrasena` | F-005 | Desktop, mobile, token válido/vencido y éxito |
| `V-005` | Inicio `/` | F-006, F-036 | Desktop, mobile, carga y contenido vacío parcial |
| `V-006` | Catálogo `/catalogo` | F-007–F-010, F-036 | Desktop, mobile, filtros, sin resultados y error |
| `V-007` | Ficha `/productos/{slug}` | F-011–F-016, F-036 | Desktop, mobile, variante, oferta, agotado, error y galería |
| `V-008` | Carrito `/carrito` | F-017–F-021 | Desktop, mobile, vacío, ajustes y conflicto |
| `V-009` | Favoritos `/favoritos` | F-037–F-039 | Desktop, mobile, vacío, retirado y variante requerida |
| `V-010` | Dirección `/checkout/direccion` | F-022 | Desktop, mobile, selección, formulario y error |
| `V-011` | Resumen `/checkout/resumen` | F-023, F-024 | Desktop, mobile, cotización, cupón y sin cobertura |
| `V-012` | Pago simulado `/checkout/pago` | F-025 | Desktop, mobile, revalidación, cambio y error; sin tarjeta/CVV |
| `V-013` | Crear orden `/checkout/confirmacion` | F-026 | Desktop, mobile, contacto faltante, envío y verificación pendiente |
| `V-014` | Pedido confirmado `/checkout/confirmado/{orderId}` | F-027, F-034 | Desktop, mobile, éxito y verificación pendiente |
| `V-015` | Mis pedidos `/mis-pedidos` | F-028, F-029 | Desktop, mobile, vacío, filtros, cero resultados y error |
| `V-016` | Detalle de pedido `/mis-pedidos/{orderId}` | F-030, F-031 | Desktop, mobile, recompra total/parcial y pedido no disponible |
| `V-017` | Seguimiento `/mis-pedidos/{orderId}/seguimiento` | F-032 | Desktop, mobile, sin despacho, hitos e incidencia |

### 5.2 Overlays, feedback y estados transversales

| ID propuesto | Elemento | Fuente |
|---|---|---|
| `O-001` | Sheet de filtros en móvil | F-008, F-029 |
| `O-002` | Visor ampliado de galería | F-011 |
| `O-003` | Intercepción de autenticación con retorno | F-002, F-021, F-036 |
| `O-004` | Confirmación de cierre durante checkout | F-003 |
| `O-005` | Toast de ítem agregado al carrito | F-016 |
| `O-006` | Toast con Deshacer al quitar carrito/favorito | F-018, F-038 |
| `O-007` | Resultado de fusión de carrito | F-020 |
| `O-008` | Resultado de reordenado total/parcial | F-031 |
| `O-009` | Encuesta postentrega | F-040 |
| `O-010` | Sistema de alertas: éxito, información, advertencia y error | DS-001 y todas las vistas |

No todo toast necesita una nueva funcionalidad. Se especifica como parte de la vista o como overlay reutilizable cuando tiene estados, foco, duración o consecuencias propias.

### 5.3 Comunicaciones visuales

| ID propuesto | Pieza | Funcionalidades |
|---|---|---|
| `C-001` | Correo de confirmación de pedido | F-033, F-034 |
| `C-002` | Correo de actualización de despacho | F-033, F-035 |

Ambos requieren versión desktop y mobile/responsive, funcionamiento sin imágenes, CTA accesible y ausencia de información sensible.

## 6. Fases de trabajo y puertas de control

### Fase 0 — Congelar alcance y fuentes

- [ ] Confirmar fecha y formato de presentación del hito.
- [ ] Registrar la URL oficial de Figma y permisos de edición.
- [ ] Confirmar que `main` contiene la última documentación antes de repartir trabajo.
- [ ] Acordar que los documentos históricos son referencia y las specs `F-###` son fuente vigente.

**Puerta de salida:** equipo usa una sola versión del repositorio y un solo archivo de Figma.

### Fase 1 — Consolidar el sistema de diseño

- [ ] Crear `SPECS/ui/sistema-diseno/` y su índice.
- [ ] Reunir logos en formatos editables y de exportación (`SVG`, `PNG`), variantes, zonas de seguridad y tamaños mínimos.
- [ ] Registrar nombre de marca, tono, paleta, tipografías, iconografía, fotografía, licencias y fuentes de los recursos.
- [ ] Registrar URL, páginas y convención de nombres del archivo Figma.
- [ ] Comparar el documento/guía existente y Figma contra `DS-001`.
- [ ] Resolver `DS-OPEN-01` a `DS-OPEN-04` o marcar responsable y fecha.
- [ ] Actualizar `DS-001` a `0.2.0` cuando la biblioteca inicial y los recursos estén consolidados.
- [ ] Construir en Figma Foundations y componentes con variantes: default, hover, focus, pressed, disabled, loading, error y success cuando aplique.
- [ ] Validar contraste WCAG 2.2 AA, área táctil mínima de 44×44 px y responsive.

**Puerta de salida:** no se reparte ninguna vista hasta que tokens, componentes base y nomenclatura de frames estén disponibles.

### Fase 2 — Especificar el inventario visual

- [ ] Actualizar `NOMENCLATURA-SDD.md` con `V-###`, `O-###` y `C-###`.
- [ ] Crear los índices de vistas, overlays y comunicaciones.
- [ ] Crear una plantilla de spec por vista basada en `SPECS/ui/PLANTILLA.md`.
- [ ] Redactar y revisar `V-001` a `V-017`.
- [ ] Redactar `O-001` a `O-010` y `C-001` a `C-002`.
- [ ] Actualizar el diagrama de navegación para las 17 vistas vigentes.
- [ ] Crear la matriz `F-### ↔ V/O/C ↔ frame Figma`.
- [ ] Eliminar ambigüedades de rutas, estados y mensajes antes de dibujar.

**Puerta de salida:** cada frame requerido tiene una spec aprobada o, como mínimo, en revisión con decisiones abiertas explícitas.

### Fase 3 — Producir mockups de alta fidelidad

- [ ] Crear un frame desktop y un frame mobile para la vista principal de cada `V-###`.
- [ ] Diseñar estados críticos sólo cuando sean visualmente distintos: carga, vacío, error, validación, no disponible, conflicto o éxito.
- [ ] Usar instancias de la biblioteca y no recrear componentes localmente.
- [ ] Nombrar frames con el formato `V-### / Estado / Desktop|Mobile`.
- [ ] Anotar el frame con versión de `DS-001`, funcionalidades cubiertas y enlace a la spec.
- [ ] Crear prototipos navegables para exploración/compra y pedidos/postentrega.
- [ ] Revisar consistencia visual, contenido, foco y comportamiento responsive.

**Puerta de salida:** ningún frame se declara terminado sin enlaces de trazabilidad y checklist visual.

### Fase 4 — Llevar el modelo lógico a un avance físico verificable

- [ ] Revisar el esquema Prisma preliminar contra el modelo lógico vigente.
- [ ] Definir tablas, enums, tipos, nulabilidad, relaciones locales, restricciones e índices.
- [ ] Implementar primero `Cart`, `CartItem` y `WishlistItem`.
- [ ] Incluir `CheckoutOperation`, `NotificationDelivery` y `PostDeliveryPrompt` si sus dependencias del hito están aceptadas; de lo contrario, documentar su diseño físico pendiente.
- [ ] Generar diagrama ER actualizado.
- [ ] Crear y ejecutar la primera migración reproducible.
- [ ] Preparar datos seed representativos: carrito anónimo, carrito autenticado, fusión, favoritos y estados de checkout permitidos.
- [ ] Verificar unicidades, checks, concurrencia/versionado e idempotencia.
- [ ] Documentar instalación local, variables de entorno, migración, seed y consulta de evidencia.
- [ ] Adjuntar evidencia de ejecución sin exponer secretos ni datos personales reales.

**Puerta de salida:** otra persona puede levantar la base desde cero y reproducir las tablas y datos de prueba siguiendo el README.

### Fase 5 — Auditoría y preparación de la presentación

- [ ] Revisión cruzada: diseñador distinto al autor verifica cada bloque.
- [ ] Validar que no existan campos de tarjeta/CVV en el pago simulado.
- [ ] Validar que ninguna vista muestre cantidades internas de stock ni datos de otros módulos.
- [ ] Verificar todos los enlaces entre Markdown y Figma.
- [ ] Ejecutar checklist de accesibilidad en frames prioritarios.
- [ ] Preparar una narrativa corta: problema, especificación, diseño, modelo de datos y evidencia.
- [ ] Definir quién presenta sistema de diseño, mockups, navegación y base de datos.

## 7. Reparto propuesto

El reparto se organiza por vistas completas, no por componentes aislados. Cada responsable entrega desktop, mobile, estados asignados, enlace de Figma y actualización de su spec por vista.

### 7.1 Equipo UI/Figma

| Responsable | Bloque principal | Artefactos |
|---|---|---|
| Giuliano Macchiavello | Sistema de diseño y acceso | Coordinación de `DS-001`, biblioteca Figma, `V-001`–`V-004`, `O-003`, `O-004` |
| Leonidas Garcia | Descubrimiento y producto | `V-005`–`V-007`, `O-001`, `O-002`, revisión de coherencia técnica con F-006–F-016 |
| Sebastián Malca | Carrito y favoritos | `V-008`, `V-009`, `O-005`–`O-007`, estados vacío/conflicto/deshacer |
| Jim Segovia | Checkout | `V-010`–`V-014`, cotización, cupón, pago simulado y confirmación |
| Diego Espinoza | Pedidos, comunicaciones y QA | `V-015`–`V-017`, `O-008`–`O-010`, `C-001`, `C-002`, navegación y trazabilidad final |

Revisión cruzada propuesta:

- Giuliano revisa consistencia visual y uso de componentes.
- Jim revisa claridad de producto, contenido y alcance.
- Diego revisa criterios de aceptación, estados y trazabilidad.
- Leonidas revisa consistencia con contratos y límites de dominio.
- Sebastián revisa documentación, responsive y continuidad de flujos.

### 7.2 Equipo de base de datos

| Responsable | Bloque principal | Evidencia esperada |
|---|---|---|
| Andrés Morales | Esquema físico, seguridad e integridad | `schema.prisma`, migración, restricciones, índices y decisiones de privacidad |
| Fernando Saire | ERD, datos de prueba y validación | Diagrama ER, seed, pruebas de restricciones, guía de ejecución y evidencia |

Ambos deben revisar juntos los límites de ownership: no crear tablas locales para usuario, dirección, producto, precio, inventario, pedido, despacho ni CSAT.

## 8. Cronograma sugerido para una semana

| Día | UI/Figma | Base de datos | Resultado común |
|---|---|---|---|
| 1 | Reunir recursos, auditar Figma y cerrar inventario de vistas | Revisar modelo lógico y Prisma preliminar | Alcance congelado y responsables confirmados |
| 2 | Consolidar `DS-001`, Foundations y biblioteca base | Diseñar esquema físico e índices | Revisión conjunta de decisiones |
| 3 | Redactar/aprobar specs `V/O/C` y navegación | Implementar migración inicial | Specs suficientes para diseñar |
| 4 | Diseñar primera mitad de vistas desktop/mobile | Crear seed y pruebas de restricciones | Demostración interna parcial |
| 5 | Diseñar segunda mitad, overlays y correos | Ajustar ERD, migración y documentación | Todos los entregables en revisión |
| 6 | Prototipo, responsive, accesibilidad y revisión cruzada | Prueba de instalación desde cero | Correcciones finales |
| 7 | Congelar versión, exportar evidencia y ensayar | Congelar versión y capturas | Paquete de presentación listo |

## 9. Definition of Done del hito

### 9.1 Mockup o vista terminada

- [ ] Tiene spec por vista y funcionalidades enlazadas.
- [ ] Usa la versión vigente de `DS-001`.
- [ ] Tiene frame principal desktop y mobile.
- [ ] Incluye estados críticos aplicables sin inventar reglas.
- [ ] Usa componentes de la biblioteca Figma.
- [ ] Tiene textos, validaciones y acciones consistentes con las specs.
- [ ] Cumple contraste, foco, teclado previsto y área táctil.
- [ ] Tiene nombre normalizado y enlace desde Markdown.
- [ ] Fue revisada por una persona distinta al autor.

### 9.2 Avance de base de datos terminado

- [ ] El esquema representa sólo datos propios de Marketplace.
- [ ] El ERD coincide con Prisma y la migración.
- [ ] Claves, restricciones, índices y enums están documentados.
- [ ] La migración funciona sobre una base limpia.
- [ ] El seed produce escenarios demostrables sin datos reales.
- [ ] Se probaron unicidad de carrito/favoritos e idempotencia aplicable.
- [ ] El README permite reproducir el entorno.
- [ ] Las decisiones no cerradas aparecen como pendientes y no como supuestos implementados.

## 10. Matriz de control semanal

| Artefacto | Responsable | Estado | Enlace/evidencia | Revisor |
|---|---|---|---|---|
| Recursos y marca inventariados | Giuliano | Pendiente | — | Jim |
| `DS-001` v0.2.0 | Giuliano | Pendiente | — | Equipo UI |
| Catálogo `V/O/C` | Diego + Leonidas | Pendiente | — | Jim |
| Specs por vista | Equipo UI | Pendiente | — | Revisión cruzada |
| Biblioteca Figma | Giuliano | Pendiente | — | Sebastián |
| Mockups desktop/mobile | Equipo UI | Pendiente | — | Revisión cruzada |
| Prototipo navegable | Diego + Jim | Pendiente | — | Equipo UI |
| Esquema Prisma | Andrés | Pendiente | — | Fernando |
| ERD y seed | Fernando | Pendiente | — | Andrés |
| Migración reproducible | Andrés + Fernando | Pendiente | — | Leonidas |
| Presentación y trazabilidad | Diego + Jim | Pendiente | — | Todo el equipo |

## 11. Riesgos y decisiones que deben cerrarse pronto

| Riesgo o pendiente | Impacto | Decisión/mitigación |
|---|---|---|
| No contar con todos los logos, fuentes o permisos de uso | Alto | Inventariar y validar licencias el Día 1; usar provisional sólo si está claramente marcado. |
| Empezar mockups antes de cerrar `DS-001` | Alto | Aplicar la puerta de salida de Fase 1. |
| Intentar crear un frame independiente por cada `F-###` | Alto | Diseñar por vistas compuestas `V-###`; conservar las `F-###` para trazabilidad. |
| Repetir componentes distintos entre cinco diseñadores | Alto | Instancias desde una sola biblioteca y revisión de Giuliano. |
| Diseñar sólo el estado exitoso | Alto | La spec por vista debe declarar estados críticos antes de Figma. |
| Mantener el pago con campos de tarjeta del wireframe histórico | Alto | Seguir F-025: pago simulado sin tarjeta ni CVV. |
| Crear tablas de datos externos | Alto | Revisar ownership antes de aprobar Prisma. |
| Incluir todas las combinaciones desktop/mobile/estado como frames completos | Medio | Crear frames completos para principales y críticos; resolver estados repetidos como variantes de componentes. |
| Fecha exacta o rúbrica del profesor no confirmada | Medio | Confirmarla en Fase 0 y ajustar alcance sin perder trazabilidad. |

## 12. Orden inmediato de ejecución

1. El equipo entrega logos, documento de diseño y enlace de Figma en una única carpeta inventariada.
2. Se consolida esa información en `DS-001` y la biblioteca Figma.
3. Se aprueba el catálogo `V-001` a `V-017`, overlays y correos.
4. Se redactan las specs por vista y se actualiza navegación.
5. Sólo entonces se asignan y producen los frames web/mobile.
6. En paralelo, Andrés y Fernando derivan y prueban el modelo físico.
7. El último día se congela versión, se completa la trazabilidad y se prepara la demostración.
