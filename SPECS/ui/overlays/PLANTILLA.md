# Overlay — O-### [Nombre]

> Especificación de un modal, drawer, toast, visor o elemento de feedback superpuesto.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-###` |
| Nombre | [Nombre] |
| Tipo | [Modal/drawer/toast/banner/visor] |
| Versión | `0.1.0` |
| Estado | Borrador |
| Responsable | Por asignar |
| Revisor | Por asignar |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** [Qué comunica o permite resolver].
- **Funcionalidades:** [F-###].
- **Vistas que lo invocan:** [V-###].
- **Spec UI de origen:** [Enlaces].

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Apertura | [Disparador] | [Estado inicial] |
| Acción principal | [Condición] | [Resultado/destino] |
| Acción secundaria | [Condición] | [Resultado] |
| Cierre | Escape, botón, fondo o tiempo | [Qué opciones aplican] |

## 4. Estructura, contenido y acciones

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| [Región] | [Texto/dato] | [Acción] | Primaria/Secundaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Principal | [Condición] | [Contenido] | Sí |
| Cargando | [Condición] | [Progreso] | Sí/No |
| Error | [Condición] | [Mensaje/recuperación] | Sí/No |
| Éxito | [Condición] | [Confirmación] | Sí/No |

## 6. Responsive y accesibilidad

- Desktop: [Tamaño, posición y bloqueo del fondo].
- Mobile: [Adaptación a hoja inferior, pantalla completa u otra variante].
- Foco inicial y retorno del foco al elemento invocador.
- Trampa de foco sólo para overlays modales.
- Cierre por teclado cuando corresponda.
- Anuncio accesible de mensajes dinámicos.
- No depender sólo del color.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-### / Desktop / Principal` | Desktop | Principal |
| `O-### / Mobile / Principal` | Mobile | Principal |

## 8. Criterios de aceptación visual

- [ ] `UI-O###-001`: [Condición verificable].
- [ ] La activación, el cierre y el retorno de foco están definidos.
- [ ] Las variantes desktop y mobile están especificadas.
- [ ] El componente cumple `DS-001` y no modifica comportamiento funcional.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-###-OPEN-01` | [Pendiente] | Por asignar | Abierta |
