# Overlay — O-002 Visor de galería

> Diálogo modal para observar una imagen de producto ampliada y navegar por los medios válidos sin abandonar la ficha.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-002` |
| Nombre | Visor de galería |
| Tipo | Visor modal; pantalla completa en mobile |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Leonidas Garcia |
| Revisor | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** ampliar el medio seleccionado y permitir recorrer la galería ordenada del producto.
- **Funcionalidad:** `F-011` Visualizar ficha y galería.
- **Vista que lo invoca:** [`V-007`](../vistas/V-007-ficha-producto.md).
- **Spec UI de origen:** [`UI F-011`](../F-011-detalle-producto.md).

No añade imágenes, precios o información de variante. La galería visible es la misma lista válida y ordenada de la ficha.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir | Activar imagen principal o “Ampliar imagen” | Muestra el medio actualmente seleccionado y enfoca el título/cierre. |
| Anterior/siguiente | Existen varios medios | Cambia selección dentro de límites y anuncia posición. |
| Miniatura | Variante de diseño aprobada | Selecciona medio sin cerrar. |
| Cerrar | Botón Cerrar o Escape | Cierra y devuelve foco al control/imagen que lo abrió. |
| Fondo | Clic fuera | Sólo cierra si el patrón DS-001 lo permite de forma consistente; nunca única salida. |
| Navegación de ruta | Usuario abandona la ficha | Cierra y permite la navegación solicitada. |

## 4. Estructura, contenido y acciones

```text
O-002 Visor de galería
├── Encabezado
│   ├── nombre accesible del producto
│   ├── “Imagen X de Y”
│   └── Cerrar
├── Área de imagen ampliada / respaldo
├── Anterior y Siguiente, si aplica
└── Miniaturas opcionales
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Encabezado | Nombre y posición | Orientar/cerrar | Primaria |
| Imagen | Medio y texto alternativo | Observar; zoom adicional sólo si se aprueba | Primaria |
| Navegación | Anterior/siguiente | Cambiar medio | Primaria |
| Miniaturas | Medios ordenados | Seleccionar | Secundaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Una imagen | Galería de un medio | Sin anterior/siguiente ni miniaturas redundantes | Sí |
| Varias imágenes | Dos o más medios | Posición y controles disponibles | Sí |
| Cargando medio | Cambio de imagen | Área conserva dimensiones y muestra progreso no distractor | Sí, anotado |
| Imagen no descargable | Fallo del navegador | Respaldo “Imagen no disponible”; navegación restante funciona | Sí |
| Todas fallan | Ningún medio descarga | Respaldo estable y cierre; ficha textual permanece al volver | Sí, variante |

La navegación no debe circular infinitamente salvo decisión explícita; en los extremos, el control correspondiente queda deshabilitado o se aplica el patrón aprobado y documentado.

## 6. Responsive y accesibilidad

- Desktop usa diálogo amplio dentro del viewport, con imagen contenida sin recorte informativo.
- Mobile usa pantalla completa o casi completa, respeta áreas seguras y mantiene Cerrar siempre alcanzable.
- Gestos táctiles pueden complementar, nunca sustituir, botones anterior/siguiente.
- Existe trampa de foco; Escape cierra y el fondo queda no interactivo.
- Flechas izquierda/derecha pueden navegar si no interfieren con otros controles; se documentan mediante ayuda accesible cuando corresponda.
- El cambio anuncia “Imagen X de Y” y texto alternativo sin repetir información innecesaria.
- Controles tienen nombre accesible con producto/posición cuando ayude.
- Movimiento/transiciones respetan reducción de movimiento.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-002 / Desktop / Varias imágenes` | Desktop | Principal |
| `O-002 / Mobile / Varias imágenes` | Mobile | Pantalla completa |
| `O-002 / Desktop / Una imagen` | Desktop | Sin navegación |
| `O-002 / Mobile / Imagen no disponible` | Mobile | Respaldo |

## 8. Criterios de aceptación visual

- [ ] `UI-O002-001`: El visor abre en la imagen seleccionada y conserva el orden de la ficha.
- [ ] `UI-O002-002`: Anterior/siguiente sólo son operables cuando existe un destino válido.
- [ ] `UI-O002-003`: Cerrar devuelve el foco al elemento invocador y Escape funciona.
- [ ] `UI-O002-004`: Cada medio tiene texto alternativo útil o respaldo generado por F-011.
- [ ] `UI-O002-005`: El fallo de una imagen no cierra el visor ni impide navegar por las demás.
- [ ] `UI-O002-006`: Mobile mantiene controles explícitos aunque admita gestos.
- [ ] El overlay cumple `DS-001` y no introduce contenido comercial nuevo.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-002-OPEN-01` | Definir navegación en extremos: controles deshabilitados o recorrido circular. | UX/UI | Abierta |
| `O-002-OPEN-02` | Confirmar si se admite zoom/pan adicional y sus controles accesibles. | UX/UI | Abierta |
| `O-002-OPEN-03` | Confirmar si las miniaturas permanecen visibles en mobile o sólo posición + controles. | UX/UI | Abierta |
