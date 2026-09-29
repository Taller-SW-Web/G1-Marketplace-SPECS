# Vista — V-015 Historial de pedidos

> Pantalla privada para consultar y filtrar la lista paginada de pedidos propios, usando Ventas como fuente de verdad.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-015` |
| Nombre | Historial de pedidos |
| Ruta | `/mis-pedidos` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Diego Espinoza |
| Revisor | Sebastián Malca |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** localizar pedidos propios por estado o fecha y abrir su detalle o seguimiento.
- **Actor principal:** cliente autenticado.
- **Permiso:** privado; la identidad deriva exclusivamente del JWT.
- **Condición de entrada:** sesión activa desde cabecera, confirmación o enlace autorizado.
- **Resultado esperado:** lista paginada mínima y acceso al pedido elegido; Marketplace no replica el historial.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-028` | [`Consultar historial`](../../funcional/F-028-historial-pedidos.md) | [`UI F-028`](../F-028-historial-pedidos.md) | Pedidos propios, resumen, paginación, vacío y error. |
| `F-029` | [`Filtrar historial`](../../funcional/F-029-filtrar-historial-pedidos.md) | [`UI F-029`](../F-029-filtrar-historial-pedidos.md) | Estado, rango de fechas, validación y limpieza. |

Contratos consultados: [`API F-028`](../../contrato-api/F-028-historial-pedidos.md) y [`API F-029`](../../contrato-api/F-029-filtrar-historial-pedidos.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| Cabecera autenticada | `V-015` | Sesión válida | Sesión. |
| `V-014` / otras áreas | `V-015` | Acción “Mis pedidos” | Sesión. |
| Seleccionar pedido | `V-016` | Pedido propio | Filtros, página y posición para volver. |
| “Ver seguimiento” | `V-017` | Pedido con despacho consultable | Filtros/página de origen. |
| Estado vacío | `V-006` | Sin pedidos | Sesión. |
| Sesión vencida | `O-003` → `V-001` | `401` | Retorno a `V-015` sin conservar datos ajenos. |

Filtros y página deben representarse en URL cuando sean válidos para que el retorno y la recarga sean reproducibles; nunca se admite `clienteId`.

## 5. Jerarquía y composición visual

```text
V-015 Historial de pedidos
├── Cabecera global autenticada
├── Encabezado “Mis pedidos”
├── Filtros
│   ├── Estado
│   ├── Fecha desde/hasta
│   ├── Aplicar
│   └── Limpiar
├── Chips/resumen de filtros activos
├── Lista o tabla responsive de pedidos
│   └── Código, fecha, total, estado y acciones
├── Paginación
└── Estado vacío/error
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Filtros desktop | Estado y rango | Primaria | En línea o panel superior; aplicar explícito. |
| Filtros mobile | Botón/resumen | Primaria | Abre variante de `O-001`; cancelar no cambia resultados. |
| Lista | Resumen mínimo de pedido | Primaria | Desktop puede usar tabla; mobile siempre tarjetas legibles. |
| Estado | Badge con texto, icono y color | Primaria | Valores publicados por Ventas, no inventados localmente. |
| Paginación | 10 por página inicial | Primaria | Conserva filtros; páginas inexistentes no operables. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Mis pedidos” | — | Siempre. |
| Estado | Lista publicada por Ventas | Filtrar | Filtros. |
| Desde/hasta | Fechas locales | Definir intervalo | Filtros. |
| Aplicar | “Aplicar filtros” | Consultar y volver a página cero | Filtros válidos. |
| Limpiar | “Limpiar filtros” | Quitar criterios y recuperar historial | Existe criterio/borrador. |
| Pedido | Código, fecha, total y estado | Abrir `V-016` | Resultado. |
| Seguimiento | “Ver seguimiento” | Abrir `V-017` | Estado/pedido elegible. |
| Vacío general | “Aún no has realizado pedidos” | Explorar catálogo | Historial realmente vacío. |
| Vacío filtrado | “No encontramos pedidos con estos filtros” | Limpiar criterios | Cero coincidencias con filtros. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Cargando | Consulta inicial | Skeleton de filas/tarjetas y paginación; sin pedidos ficticios | Esperar | Sí |
| Con pedidos | Página válida | Lista, estados y acciones | Abrir/paginar | Sí |
| Con filtros | Criterios aplicados | Chips/resumen y lista filtrada | Quitar/limpiar | Sí |
| Historial vacío | Total cero sin filtros | Mensaje y CTA a catálogo | Explorar | Sí |
| Sin coincidencias | Total cero con filtros | Criterios visibles y limpiar | Limpiar/editar | Sí |
| Rango inválido | Desde posterior a hasta o intervalo > un año | Errores asociados; no consulta Ventas | Corregir | Sí |
| Actualizando | Aplicar/limpiar/paginar | Resultados ocupados sin mezclar página vieja como nueva | Esperar | Sí |
| Página fuera de rango | URL o historial cambió | Estado controlado y retorno a página válida | Ir a primera/última definida | Sí |
| Error recuperable | Ventas/BFF no disponible | No se presenta falso vacío; filtros permanecen | Reintentar | Sí |
| Sesión vencida | `401` | Datos retirados de pantalla y autenticación requerida | Login | Se diseña en `O-003` |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-001` | Filtros mobile — variante pedidos | Activar filtros en pantalla estrecha | Aplicar actualiza URL; cancelar conserva criterios aplicados. |
| `O-003` | Autenticación requerida | Acceso sin sesión o sesión vencida | Login y retorno autorizado. |
| `O-010` | Alertas y feedback global | Error temporal/página corregida | Reintentar/cerrar. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Estado | Select | No | Sólo estados publicados por Ventas | “Todos los estados” como ausencia de filtro | Default/foco |
| Desde | Fecha | No | ISO al enviar; no posterior a Hasta | Mensaje vinculado a ambos campos | Default/foco/error |
| Hasta | Fecha | No | Intervalo máximo de un año y no anterior a Desde | Mensaje vinculado a ambos campos | Default/foco/error |

Las fechas se muestran en zona local y se convierten al formato del contrato sin cambiar silenciosamente el día elegido.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Tabla o lista alineada con columnas código, fecha, total, estado y acciones.
- Encabezados permanecen asociados; no usar tabla si fuerza desplazamiento horizontal innecesario.
- Filtros visibles sobre resultados y paginación al final.

### Mobile

- **Referencia:** 390 px.
- Cada pedido es tarjeta con código como encabezado, seguida de fecha, total, estado y acciones.
- Filtros usan `O-001`; el resumen activo permanece visible en la página.
- No ocultar total o estado para conservar una tabla compacta.

### Anchuras intermedias

- Cambiar de tabla a tarjetas cuando los datos o acciones dejen de ser legibles, no sólo por un breakpoint nominal.

## 11. Accesibilidad

- Tabla desktop usa encabezados correctos; tarjetas mobile conservan el mismo orden semántico.
- Cada pedido tiene un enlace accesible que incluye su código.
- Badges usan texto/icono/color y no dependen de abreviaturas sin explicación.
- Filtros activos pueden retirarse con teclado y se anuncian al aplicarse.
- Resultado/cantidad se anuncia sin mover el foco; tras paginar, foco al encabezado de resultados.
- Errores de rango se asocian a Desde y Hasta; no se realiza solicitud inválida.
- Controles de paginación deshabilitados no son enlaces operables.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-015 / Desktop / Con pedidos` | Desktop | Principal | Tabla/lista y filtros. |
| `V-015 / Mobile / Con pedidos` | Mobile | Tarjetas | Resumen de filtros. |
| `V-015 / Desktop / Con filtros` | Desktop | Filtrado | Chips y paginación. |
| `V-015 / Mobile / Historial vacío` | Mobile | Vacío general | CTA catálogo. |
| `V-015 / Desktop / Sin coincidencias` | Desktop | Vacío filtrado | Limpiar criterios. |
| `V-015 / Mobile / Rango inválido` | Mobile | Validación | Errores relacionados. |
| `V-015 / Desktop / Cargando` | Desktop | Skeleton | Filas y paginación. |
| `V-015 / Mobile / Error recuperable` | Mobile | Error | Filtros preservados. |

## 13. Criterios de aceptación visual

- [ ] `UI-V015-001`: La vista no acepta ni muestra un control `clienteId`; sólo presenta pedidos del JWT.
- [ ] `UI-V015-002`: Historial vacío y cero resultados filtrados son estados diferentes y ofrecen acciones adecuadas.
- [ ] `UI-V015-003`: Aplicar filtros reinicia la página y conserva el ámbito del cliente.
- [ ] `UI-V015-004`: Rango invertido o mayor a un año no realiza solicitud.
- [ ] `UI-V015-005`: Cada pedido muestra código, fecha, total, estado y enlace accesible al detalle.
- [ ] `UI-V015-006`: Desktop y mobile conservan los mismos datos esenciales; los estados no dependen sólo del color.
- [ ] `UI-V015-007`: El error de Ventas no se representa como lista vacía.
- [ ] La vista aplica `DS-001` y la variante mobile de `O-001`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-015-OPEN-01` | Resolver `I-03`: endpoint `/me` o validación estricta del cliente contra JWT en Ventas. | Ventas + Arquitectura | Antes de implementación; informar diseño | Abierta |
| `V-015-OPEN-02` | Publicar estados, etiquetas y orden de presentación permitidos por Ventas. | Ventas + Producto | Antes del diseño final | Abierta |
| `V-015-OPEN-03` | Definir política para página fuera de rango y orden predeterminado. | Backend + Ventas | Antes del diseño final | Abierta |
| `V-015-OPEN-04` | Confirmar en qué estados se ofrece acceso directo a seguimiento. | Despacho + Producto | Antes del diseño final | Abierta |
