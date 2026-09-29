# Overlay — O-004 Confirmación de cierre durante checkout

> Diálogo que evita abandonar inadvertidamente una sesión mientras existe un checkout en curso.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-004` |
| Nombre | Confirmación de cierre durante checkout |
| Tipo | Modal de confirmación |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** confirmar el cierre de sesión cuando puede interrumpir o volver inaccesible el contexto de checkout.
- **Funcionalidad:** `F-003` Cerrar sesión.
- **Vistas que lo invocan:** [`V-010`](../vistas/V-010-direccion-envio.md), [`V-011`](../vistas/V-011-resumen-envio-beneficio.md), [`V-012`](../vistas/V-012-pago-simulado.md) y [`V-013`](../vistas/V-013-creacion-orden.md).
- **Spec UI de origen:** [`UI F-003`](../F-003-cerrar-sesion.md).

Cerrar sesión no equivale a cancelar una orden enviada ni revierte operaciones externas.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir | Seleccionar “Cerrar sesión” con checkout en curso | Bloquea fondo y explica consecuencia según etapa. |
| Continuar checkout | Acción recomendada | Cierra modal, conserva contexto y devuelve foco a Cerrar sesión. |
| Cerrar sesión | Confirmación explícita | Invalida sesión, descarta contexto local permitido y navega a `V-005`. |
| Escape/cerrar | Cualquier etapa cancelable | Igual a continuar checkout; no cierra sesión. |
| Envío en curso | `V-013 SUBMITTED`/verificación | No se afirma que el pedido se cancelará; aplica política segura de consulta. |

## 4. Estructura, contenido y acciones

```text
O-004 Confirmación de cierre
├── Título “¿Cerrar sesión?”
├── Consecuencia contextual
├── Acción recomendada “Continuar checkout”
└── Acción destructiva “Cerrar sesión”
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Encabezado | Pregunta clara | Orientar | Primaria |
| Consecuencia | Progreso local puede descartarse; carrito permanece según reglas | Informar | Primaria |
| Continuar | “Continuar checkout” | Cancelar logout | Primaria/recomendada |
| Cerrar | “Cerrar sesión” | Confirmar logout | Destructiva/secundaria visual |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Dirección/resumen | `V-010` o `V-011` | Explica que la selección/cotización puede perder vigencia | Sí |
| Pago preparado | `V-012 PREPARED` | Explica que la preparación no es pedido y puede requerir reinicio | Sí |
| Orden no enviada | `V-013` antes de POST | Explica que todavía no existe pedido | Anotado |
| Orden enviada/verificando | `SUBMITTED` | Explica que cerrar no cancela; resultado debe consultarse después | Sí |
| Cerrando sesión | Usuario confirmó | Acciones bloqueadas y progreso breve | Sí, anotado |
| Error al cerrar | Logout falla | Sesión/estado según Seguridad, mensaje y reintento | Sí |

## 6. Responsive y accesibilidad

- Modal compacto en desktop y diálogo/bottom sheet en mobile con ambas acciones siempre visibles.
- Foco inicial en “Continuar checkout”, no en la acción destructiva.
- Trampa de foco; Escape equivale a cancelar y devuelve foco al invocador.
- Acción destructiva usa texto explícito, no sólo color rojo o icono.
- Durante logout, se evita doble activación y se anuncia progreso.
- Al completar, foco llega al título de `V-005` y se anuncia “Sesión cerrada”.
- En estado `SUBMITTED`, el texto sobre pedido pendiente es accesible antes de las acciones.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-004 / Desktop / Checkout en edición` | Desktop | Dirección/resumen |
| `O-004 / Mobile / Pago preparado` | Mobile | Preparación |
| `O-004 / Desktop / Orden verificándose` | Desktop | Resultado incierto |
| `O-004 / Mobile / Error al cerrar` | Mobile | Recuperable |

## 8. Criterios de aceptación visual

- [ ] `UI-O004-001`: Sólo aparece durante checkout; fuera de él F-003 cierra sesión sin confirmación innecesaria.
- [ ] `UI-O004-002`: “Continuar checkout” es la acción recomendada y recibe foco inicial.
- [ ] `UI-O004-003`: El texto no afirma que cerrar sesión cancele una orden enviada.
- [ ] `UI-O004-004`: Confirmar invalida la sesión y navega a inicio sin exponer tokens ni causas técnicas.
- [ ] `UI-O004-005`: Escape/cerrar conserva el checkout y devuelve foco.
- [ ] El overlay cumple `DS-001` y diferencia acción destructiva sin depender sólo del color.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-004-OPEN-01` | Definir política exacta de logout mientras F-026 está `SUBMITTED` o verificándose. | Seguridad + Backend + Producto | Abierta |
| `O-004-OPEN-02` | Confirmar qué contexto de checkout se descarta y qué puede recuperarse tras volver a iniciar sesión. | Arquitectura + Producto | Abierta |
