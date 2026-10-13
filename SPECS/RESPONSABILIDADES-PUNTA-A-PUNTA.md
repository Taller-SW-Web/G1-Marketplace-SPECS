# Matriz de responsabilidad punta a punta — Marketplace

Versión 0.1.0 · Propuesta de implementación del 13/10/2026. **Pendiente de estimación, aceptación individual y validación del PO/profesor.** Esta matriz asigna trabajo futuro; no acredita código, integración ni aprobación de un hito. Las specs funcionales, UI, API y React conservan sus reglas; el responsable de implementación no sustituye al responsable del **diseño de una vista** que aparezca en V/O/C o en el inventario visual.

## Criterio de reparto

El sílabo tiene ocho bloques y el equipo siete integrantes. Proponemos agrupar **consulta/seguimiento de pedidos** y **notificaciones del pedido** bajo Fernando: comparten el estado del pedido y la señal de Despacho, y se desarrollan en S3–S4. No se presume que el profesor exija exactamente un bloque por persona; Jim debe validar esta interpretación. Fernando recibe colaboración de Jim para aceptación de contenido de correos y de Leonidas para el contrato/evento; conserva un único ownership técnico de ambos bloques. Su carga se revisa antes de S3; si no cabe, se resecuencia o se solicita una decisión explícita, sin presentar funciones bloqueadas como cerradas.

Cada responsable implementa al menos un corte de **interfaz y backend propio de Marketplace**. Para Seguridad, Productos, Ventas y Despacho, backend propio significa ruta BFF, adaptador, orquestación o persistencia **de Marketplace** según la spec. El módulo proveedor conserva sus reglas y datos. El revisor principal es distinto del autor; Leonidas revisa además cambios de contrato/backend y Andres revisa seguridad cuando apliquen. Los roles generales del [equipo](../README.md#equipo) continúan.

| Bloque del sílabo | F-### bajo un único responsable | Vistas, overlays y correos relacionados | Responsable / revisor principal | Gate externo principal | Cierre objetivo |
|---|---|---|---|---|---|
| 1. Registro e inicio de sesión | F-001–F-005 | V-001–V-004; O-003; V-001 también recibe F-020 de carrito | Jim Segovia / Andres Morales | Seguridad: G-AUTH, contrato y entorno | H4/S2 F-001–003; H6/S5 F-004–005 |
| 2. Búsqueda y navegación del catálogo | F-006–F-010 | V-005–V-006; O-001; O-010 compartido | Giuliano Macchiavello / Sebastian Malca | Productos I-01, G-FEATURED, G-SORT | H3/S1 F-006–007; H4/S2 F-008–010 |
| 3. Detalle del producto | F-011–F-015 | V-007; O-002; acciones de carrito/favorito pertenecen a otros bloques | Sebastian Malca / Giuliano Macchiavello | Productos I-01, G-SKU, G-QUANTITY | H4/S2 F-011–014; H6/S5 F-015 |
| 4. Carrito de compras | F-016–F-021 | V-008; O-005–O-007; alta desde V-007 y fusión en V-001 | Andres Morales / Leonidas Garcia | Productos I-01, Seguridad G-AUTH, G-ADD, G-UNDO, G-DB | H4/S2 F-016/019; S3 F-017/018; H6/S5 F-020/021 |
| 5. Favoritos / lista de deseos | F-036–F-039 | V-009; controles en V-005–V-007; O-003/O-006 compartidos | Diego Espinoza / Fernando Saire | Seguridad G-AUTH, Productos I-01; carrito para F-039 | H4/S2 F-036–038; H6/S5 F-039 |
| 6. Checkout y generación del pedido | F-022–F-027 | V-010–V-014; O-004; O-010 compartido | Leonidas Garcia / Diego Espinoza | Ventas I-02, Despacho I-06, Productos I-01, G-MONEY/G-CHECKOUT/G-PAID | S3 antes de H5; cierre sólo con PAGADO confirmado |
| 7. Notificaciones por correo | F-033–F-035 | C-001–C-002; confirmación visible en V-014 | Fernando Saire / Jim Segovia | Ventas I-02 (confirmación), I-05 (despacho), G-MAIL, G-ASYNC-H5 | S3 F-033/034; H5/S4 F-035 |
| 8. Consulta y seguimiento de pedidos | F-028–F-032 | V-015–V-017; O-008; F-040 se abre tras entrega | Fernando Saire / Jim Segovia | Ventas I-03, Despacho I-06, G-REORDER | S3 F-028/030; H5/S4 F-032; H6/S5 F-029/031 |

**Adicional fuera de los ocho bloques literales:** F-040, evaluación postentrega, pertenece al canal Marketplace pero no es un noveno bloque del sílabo citado. Responsable **Diego**, revisor **Fernando**; O-009, con acceso desde V-016/V-017; objetivo H6/S5 y gates I-04/G-PROMPT con Ventas. Así quedan F-001–F-040 asignadas exactamente una vez.

## Cruces e integración

- **F-020** tiene owner Andres (carrito); Jim provee el estado de login y revisa el handoff de identidad. **F-021** queda con Andres y **F-039** con Diego; usan contratos compartidos de carrito/favoritos con pruebas de duplicado/timeout.
- **F-016** se invoca desde V-007, pero Andres conserva la mutación del carrito; Sebastian integra el control en la ficha. **F-036** aparece en V-005/V-006/V-007; Diego conserva el BFF/persistencia de favorito y los dueños de las vistas integran el control. Diseñador visual y dueño de implementación son campos distintos.
- **F-025–F-027** dependen de Ventas y de los importes/stock autorizados por Productos/Despacho. Leonidas integra el checkout; Fernando consume el pedido autorizado para F-028–F-035. No se replica la BD de otros módulos.
- **F-032 y F-035** comparten señal de Despacho, con Fernando como responsable de integración y Leonidas como revisor técnico del contrato/evento. La decisión sobre proveedor, ruta, esquema y token queda abierta hasta publicación y prueba. No se fija aquí un endpoint nuevo.
- **O-010 y DS-001** son componentes de diseño transversales, no funcionalidades asignadas. Giuliano custodia el sistema visual; cada dueño aplica sus estados. La propiedad histórica de los 29 mockups permanece en el [inventario visual](ui/INVENTARIO-VISUAL-Y-ESTIMACION.md) y no concede ownership del código.
- Los 40 IDs permanecen estables. La cobertura de cada tarea y su estado se controla en [seguimiento](../plan/seguimiento/README.md); un corte `MOCK` local no libera una tarea `INT` bloqueada.

El [archivo de mockups en Figma](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible mediante la conexión del equipo el 13/10/2026. Sólo se confirmó el archivo y su página de nivel superior «Acceso y cuenta»; los enlaces a frames individuales aún deben verificarse antes de usarlos como evidencia de una vista.

## H3: siete incrementos individuales, un solo gate común

La ruta crítica común sigue siendo **F-006/F-007 → V-005 y búsqueda de V-006 → frontend desplegado → BFF Marketplace → API real de Productos**. Giuliano es dueño del bloque; Sebastian colabora en V-006, Leonidas revisa adaptador y contrato, Andres prepara nube, Fernando hace smoke, Diego verifica y Jim acepta. Las aportaciones de apoyo no sustituyen el incremento propio de cada persona. Los seis cortes secundarios son **avances parciales** que pueden trabajarse con fixture local rotulado `MOCK`; no se suman a la aceptación de H3 ni se prometen como flujos integrados. [Paquetes individuales](../plan/repartición%20por%20integrantes/README.md) detallan UI, BE, pruebas y evidencia.

| Persona | Corte vertical demostrable en semana 8 | Límite de la evidencia |
|---|---|---|
| Giuliano | Búsqueda F-007 en V-005/V-006 con ruta BFF propia, estados y pruebas; integrar Productos real si I-01 se libera | Es el gate H3 sólo con web y backend desplegados y respuesta real |
| Jim | Estado de formulario F-002 y adaptador BFF de sesión contra fixture de Seguridad; válido/inválido | `MOCK`; no autentica usuario real ni cierra G-AUTH |
| Sebastian | Ficha F-011 desde una tarjeta V-006 a V-007, con proyección BFF y estados de producto presente/ausente | `MOCK` salvo prueba con API autorizada; no promete SKU/stock real |
| Andres | Agregar/ver un ítem F-016/F-019 en V-008 mediante endpoint y persistencia local aislada de Marketplace | `MOCK`; sin reserva ni inventario confirmado |
| Diego | Agregar y quitar favorito F-036/F-038 con control UI y BFF/persistencia propia en sandbox | `MOCK`; auth y elegibilidad real pendientes |
| Leonidas | Resumen previo F-023 en V-011 con validación BFF de un snapshot de prueba, sin acción de pago | `MOCK`; no cotización, orden ni pago real |
| Fernando | Historial F-028 en V-015 con consulta BFF sobre fixture autorizado sin datos personales reales | `MOCK`; Ventas y control de titular pendientes |

Para cada corte: caso positivo y negativo automatizable, componente/estado UI, ruta/adaptador o persistencia propia de Marketplace, PR/commit revisado por otra persona, explicación individual y evidencia con fuente, comando/resultado y etiqueta `MOCK`/`REAL`. Ninguna tarea externa pasa de `Bloqueado` a `Terminado` sin contrato, entorno y prueba reales.

## Capacidad y decisiones por validar

Estimación inicial para discutir capacidad, en **días persona de 8 h de trabajo activo** (FE+BE+INT+QA/documentación del bloque; excluye esperas de proveedores y correcciones de revisión). Es un rango de planificación, no una fecha comprometida ni una estimación aceptada por cada integrante:

| Dueño | Bloque(s) | Rango preliminar | Pico previsto |
|---|---|---:|---|
| Jim | Cuenta/acceso, 5 F | 8–14 días | S2 y recuperación S5 |
| Giuliano | Catálogo/búsqueda, 5 F | 10–16 días | H3/S1 y S2 |
| Sebastian | Detalle, 5 F | 8–13 días | S2 |
| Andres | Carrito, 6 F | 11–18 días | S2/S3; más CI/deploy transversal |
| Leonidas | Checkout, 6 F | 15–25 días | S3; más arquitectura transversal |
| Fernando | Seguimiento + correo, 8 F | 17–28 días | S3/S4; más QA/cloud transversal |
| Diego | Favoritos + F-040, 5 F | 9–15 días | S2/S5; más JP/QA transversal |

Fernando y Leonidas concentran los mayores riesgos de capacidad; la preparación de contratos de Ventas/Despacho/correo debe empezar antes de S3 y tener colaboradores/revisión acordados. Si la disponibilidad semanal no cubre el rango, Jim/Diego registran una resecuenciación de objetivos y la consultan antes de prometer el hito. La ruta H3 de catálogo absorbe la prioridad de S1; los seis cortes individuales secundarios se dimensionan como prototipos verticales parciales, no como implementaciones completas.

El número de IDs no mide horas: checkout, auth, pedido/evento y correo tienen gates costosos. Antes de aceptar S2/S3, cada responsable estima FE, BE, INT, QA y OPS, incluyendo revisión cruzada y reserva de correcciones. Diego y Jim comparan horas disponibles por semana y resecuencian sólo mediante decisión documentada. **No se promete el cierre de ocho flujos en H3.**

Jim debe confirmar con el profesor: (1) si un responsable puede asumir los bloques 7 y 8 relacionados; (2) si el incremento vertical individual de semana 8 puede ser parcial y `MOCK` fuera de la demo común; (3) qué evidencia individual espera en H3; (4) si un gate proveedor bloqueado permite presentar avance parcial sin calificarlo como terminado. La respuesta se registra en [decisiones](../plan/DECISIONES-Y-BLOQUEOS.md) y se ajusta esta matriz; no se anticipa aprobación.
