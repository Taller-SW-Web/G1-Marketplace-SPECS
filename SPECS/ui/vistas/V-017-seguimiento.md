# Vista — V-017 Seguimiento

> Pantalla privada para consultar el estado, los hitos y la fecha estimada de un despacho propio. No muestra ubicación en tiempo real, mapa, repartidor ni coordenadas.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-017` |
| Nombre | Seguimiento de despacho |
| Ruta | `/mis-pedidos/{orderId}/seguimiento` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Diego Espinoza |
| Revisor | Sebastián Malca |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** saber en qué estado se encuentra la entrega, qué hitos ocurrieron y cuál es la fecha estimada vigente.
- **Actor principal:** cliente autenticado propietario del pedido.
- **Permiso:** privado; Marketplace verifica propiedad con Ventas antes de consultar Despacho.
- **Condición de entrada:** pedido propio con o sin tracking todavía disponible.
- **Resultado esperado:** estado público de Despacho comprensible o explicación informativa si aún no existe seguimiento.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-032` | [`Consultar seguimiento`](../../funcional/F-032-seguimiento-despacho.md) | [`UI F-032`](../F-032-seguimiento-despacho.md) | Estado, hitos, fecha estimada, incidencia y seguridad. |

Contrato consultado: [`API F-032`](../../contrato-api/F-032-seguimiento-despacho.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| `V-015` → seguimiento | `V-017` | Pedido elegible | Filtros/página de historial. |
| `V-016` → “Seguir envío” | `V-017` | Tracking consultable | Pedido seleccionado. |
| Enlace de `C-002` | `V-017` | Autenticación y propiedad | `orderId`; sin PII en URL. |
| “Volver al pedido” | `V-016` | Acción explícita | Pedido y origen. |
| “Mis pedidos” | `V-015` | Acción explícita | Filtros previos cuando existan. |
| Sesión vencida | `O-003` → `V-001` | `401` | Retorno autorizado a esta ruta. |

## 5. Jerarquía y composición visual

```text
V-017 Seguimiento
├── Cabecera global autenticada
├── Migas / volver al pedido
├── Encabezado
│   ├── “Seguimiento del pedido {orderId}”
│   ├── Estado actual
│   └── Última actualización, si está disponible
├── Fecha estimada o reprogramada
├── Incidencia publicable, condicional
├── Línea de tiempo de hitos
│   └── Estado + fecha/hora × N
├── Nota sobre alcance del seguimiento
└── Acciones volver / actualizar
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Estado actual | Etiqueta pública de Despacho | Primaria | Texto, icono y color; no inferido por Marketplace. |
| Fecha estimada | Día/ventana vigente | Primaria | Se identifica como estimada y cambia si Despacho reprograma. |
| Incidencia | Mensaje genérico publicable | Primaria | No incluye datos operativos, repartidor ni coordenadas. |
| Timeline | Hitos fechados | Primaria | Lista textual accesible; orden cronológico definido por contrato. |
| Actualizar | Reconsultar | Secundaria | Evita solicitudes repetidas y no promete “tiempo real”. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Seguimiento del pedido {código}” | Copiar/volver | Pedido autorizado. |
| Estado | Etiqueta publicada por Despacho | — | Tracking disponible. |
| Fecha | “Entrega estimada: {fecha}” | — | Valor disponible. |
| Incidencia | Mensaje/reprogramación publicable | — | Despacho la devuelve. |
| Hito | Estado y fecha/hora | — | Cada milestone. |
| Actualizar | “Actualizar seguimiento” | Reconsultar | Tracking listo o error recuperable. |
| Sin tracking | “Aún estamos preparando tu pedido” | Volver al detalle/actualizar después | Respuesta `202`. |
| Nota | “El seguimiento muestra estados de entrega; no ubicación en vivo.” | — | Cuando ayude a ajustar expectativas. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Consulta inicial | Skeleton de estado/timeline; sin hitos ficticios | Esperar | Sí |
| Seguimiento disponible | `200` con hitos | Estado, fecha y timeline | Actualizar/volver | Sí |
| Incidencia o reprogramación | Datos publicables | Alerta contextual y fecha actualizada | Revisar/actualizar | Sí |
| Entregado | Estado final publicado | Timeline completo; puede habilitar elegibilidad de `O-009` | Volver/evaluar si aplica | Sí |
| Aún sin despacho | `202 TRACKING_NOT_READY` | Mensaje informativo, no alerta técnica | Volver/actualizar después | Sí |
| Pedido no disponible | Ajeno/inexistente | Estado neutral sin filtrar existencia | Volver a `V-015` | Sí |
| Seguimiento no disponible | `503` | Error recuperable; no transforma estado en “sin despacho” | Reintentar/volver | Sí |
| Sesión vencida | `401` | Datos retirados y acceso requerido | Login | Se diseña en `O-003` |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida | Sesión ausente/vencida | Login y retorno tras autorizar propiedad. |
| `O-009` | Evaluación postentrega | Pedido entregado y elegible según política | Enviar, “Ahora no” o cerrar. |
| `O-010` | Alertas y feedback global | Error de actualización o acción secundaria | Reintentar/cerrar. |
| `C-002` | Correo de actualización de despacho | Evento publicable de Despacho | Enlaza a esta vista tras autenticación. |

## 9. Formularios y validación visual

No existen formularios ni controles de modificación. El usuario sólo puede consultar, actualizar y navegar; Marketplace no permite editar hitos, fecha o despacho.

| Control | Regla | Feedback |
|---|---|---|
| Actualizar seguimiento | Una solicitud activa; respeta intervalo aprobado | Progreso discreto y nueva marca temporal si existe. |

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Encabezado y fecha estimada forman un resumen claro; timeline puede ser horizontal sólo si cada hito/fecha conserva espacio.
- Incidencias aparecen antes del timeline y no se reducen a tooltip.

### Mobile

- **Referencia:** 390 px.
- Timeline vertical con estado y fecha junto a cada hito.
- Estado/fecha/incidencia aparecen antes del historial.
- No existe mapa ni contenedor vacío reservado para geolocalización.
- Acciones apiladas con objetivos táctiles suficientes.

### Anchuras intermedias

- Timeline cambia a vertical antes de truncar etiquetas o fechas.

## 11. Accesibilidad

- Timeline es una lista ordenada; líneas y conectores son decorativos.
- Cada hito incluye texto y fecha; actual/completado no se comunica sólo por color.
- Incidencia usa un encabezado y mensaje comprensible, sin depender de icono.
- “Aún estamos preparando tu pedido” se anuncia como estado informativo, no error.
- Actualizar conserva el foco y anuncia el resultado sin recargar toda la página de forma desorientadora.
- Fechas se leen en zona local y los cambios/reprogramaciones se distinguen del valor anterior cuando sea necesario.
- No se exponen coordenadas, teléfono o nombre del repartidor al árbol accesible ni visualmente.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-017 / Desktop / Disponible` | Desktop | Principal | Resumen y timeline. |
| `V-017 / Mobile / Disponible` | Mobile | Timeline vertical | Orden apilado. |
| `V-017 / Desktop / Incidencia` | Desktop | Atención | Reprogramación publicable. |
| `V-017 / Mobile / Entregado` | Mobile | Estado final | Elegibilidad de evaluación anotada. |
| `V-017 / Desktop / Aún sin despacho` | Desktop | Informativo | `202`, sin error. |
| `V-017 / Mobile / Pedido no disponible` | Mobile | No disponible | Estado neutral. |
| `V-017 / Desktop / Error recuperable` | Desktop | `503` | Reintento. |
| `V-017 / Mobile / Cargando` | Mobile | Skeleton | Sin hitos ficticios. |

## 13. Criterios de aceptación visual

- [ ] `UI-V017-001`: La vista verifica propiedad antes de presentar seguimiento y usa un estado neutral para pedido ajeno/inexistente.
- [ ] `UI-V017-002`: “Aún estamos preparando tu pedido” se distingue de un error técnico.
- [ ] `UI-V017-003`: Cada hito comunica estado y fecha en texto; la línea gráfica es complementaria.
- [ ] `UI-V017-004`: Incidencia/reprogramación muestra información publicable y la fecha estimada vigente.
- [ ] `UI-V017-005`: La vista no contiene mapa, ubicación en vivo, coordenadas, datos del repartidor ni acciones de modificación.
- [ ] `UI-V017-006`: Error `503` permite reintentar y no se traduce en “sin despacho”.
- [ ] `UI-V017-007`: Desktop y mobile conservan los mismos estados y datos esenciales.
- [ ] La vista aplica `DS-001`, foco, contraste y reducción de movimiento.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-017-OPEN-01` | Resolver `I-06`: scope técnico `seguimientos:leer` y contrato autorizado con Despacho. | Despacho + Arquitectura | Antes de implementación; informar diseño | Abierta |
| `V-017-OPEN-02` | Publicar estados/hitos de Despacho y su mapeo a etiquetas/iconos de UI; no asumir sólo las cuatro etapas históricas. | Despacho + UX | Antes del diseño final | Abierta |
| `V-017-OPEN-03` | Definir si existe actualización manual, polling y el intervalo permitido; evitar prometer tiempo real. | Backend + Producto | Antes del diseño final | Abierta |
| `V-017-OPEN-04` | Confirmar política que habilita `O-009` al llegar a Entregado. | Producto + UX | Antes del diseño final | Abierta |
