# Overlay — O-003 Autenticación requerida con retorno

> Diálogo de decisión que explica por qué una acción requiere sesión y conduce al login conservando un retorno interno seguro.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-003` |
| Nombre | Autenticación requerida con retorno |
| Tipo | Modal de decisión |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** interceptar una acción protegida antes de navegar a [`V-001`](../vistas/V-001-inicio-sesion.md), explicar el motivo y permitir cancelar sin perder el contexto visual.
- **Funcionalidades:** `F-002`, `F-021` y `F-036`; también patrón transversal para rutas privadas.
- **Vistas que lo invocan:** `V-005` a `V-017` cuando una acción/ruta requiere sesión.
- **Specs UI de origen:** [`UI F-002`](../F-002-iniciar-sesion.md), [`UI F-021`](../F-021-mover-carrito-favoritos.md) y [`UI F-036`](../F-036-agregar-favorito.md).

Este overlay no contiene campos de credenciales. Login, registro y recuperación son rutas completas `V-001` a `V-004`.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Abrir por acción | Favorito, mover, checkout o área privada sin sesión | Explica la acción concreta y conserva intención permitida. |
| Abrir por expiración | Sesión vence en ruta privada | Retira/oculta datos privados y explica que debe volver a ingresar. |
| Iniciar sesión | CTA principal | Navega a `V-001` con retorno interno seguro. |
| Crear cuenta | Enlace secundario si aplica | Navega a `V-002` conservando retorno; luego requiere login. |
| Cancelar/cerrar | Botón, Escape o fondo según patrón | Vuelve foco al invocador y no ejecuta la acción. |

La intención se guarda sólo con identificadores/contexto mínimos permitidos. Nunca incluye contraseña, token, URL externa, datos privados visibles o payload completo.

## 4. Estructura, contenido y acciones

```text
O-003 Autenticación requerida
├── Icono contextual no exclusivo
├── Título
├── Explicación breve de la acción
├── Acción “Iniciar sesión”
├── Acción secundaria “Crear cuenta”, cuando aplique
└── “Ahora no” / Cerrar
```

| Región | Contenido | Acción | Prioridad |
|---|---|---|---|
| Encabezado | “Inicia sesión para continuar” o “Tu sesión terminó” | Orientar | Primaria |
| Contexto | Guardar favorito, mover, checkout, pedidos, etc. | Explicar retorno | Primaria |
| CTA | “Iniciar sesión” | Abrir `V-001` | Primaria |
| Registro | “Crear cuenta” | Abrir `V-002` | Secundaria; no en expiración si confunde |
| Cancelar | “Ahora no” / “Volver” | Cerrar sin cambios | Secundaria |

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Favorito | Guardar/quitar protegido sin sesión | “Inicia sesión para guardar este producto” | Sí |
| Mover a favoritos | Acción F-021 desde carrito anónimo | Explica que la línea no cambiará hasta autenticar | Sí, anotado |
| Checkout | Iniciar checkout sin sesión | Explica que el carrito se conservará/fusionará según F-020 | Sí |
| Área privada | Abrir favoritos o pedidos | Explica acceso a información propia | Sí |
| Sesión vencida | `401` durante ruta privada | “Tu sesión terminó”; datos privados dejan de mostrarse | Sí |
| Intención ya no válida | Tras login cambió producto/carrito | No ejecuta silenciosamente; muestra recuperación en vista destino | Se diseña en vista/O-010 |

## 6. Responsive y accesibilidad

- Desktop usa modal compacto; mobile usa diálogo centrado o bottom sheet aprobado con título visible.
- Foco inicial en título o CTA principal según patrón; trampa de foco y fondo no interactivo.
- Escape/cerrar devuelve foco al control invocador si sigue existiendo.
- Título y explicación nombran la acción; no dependen sólo de icono.
- Acciones tienen jerarquía inequívoca y objetivos táctiles adecuados.
- La navegación a login mueve foco al título de `V-001`.
- Si la sesión venció, contenido privado subyacente se oculta o deja de ser accesible antes de mostrar el overlay.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-003 / Desktop / Favorito` | Desktop | Acción protegida |
| `O-003 / Mobile / Checkout` | Mobile | Acción protegida |
| `O-003 / Desktop / Área privada` | Desktop | Navegación protegida |
| `O-003 / Mobile / Sesión vencida` | Mobile | Reautenticación |

## 8. Criterios de aceptación visual

- [ ] `UI-O003-001`: El overlay no incluye correo, contraseña ni formulario de login.
- [ ] `UI-O003-002`: Explica qué acción requiere sesión y qué ocurrirá al volver.
- [ ] `UI-O003-003`: Cancelar no muta favorito, carrito ni ruta protegida y devuelve foco.
- [ ] `UI-O003-004`: El retorno sólo acepta rutas internas permitidas y contexto mínimo.
- [ ] `UI-O003-005`: Sesión vencida no deja datos privados visibles detrás del modal.
- [ ] `UI-O003-006`: Tras login, la intención se revalida antes de completarse; no se ejecuta si dejó de ser válida.
- [ ] El overlay cumple `DS-001` y separa claramente acceso de registro.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-003-OPEN-01` | Definir lista permitida y representación técnica de intenciones pendientes. | Seguridad + Frontend | Abierta |
| `O-003-OPEN-02` | Confirmar en qué variantes se ofrece “Crear cuenta” además de login. | Producto + UX | Abierta |
| `O-003-OPEN-03` | Aprobar tratamiento del fondo cuando la sesión vence y contiene datos privados. | Seguridad + UX | Abierta |
