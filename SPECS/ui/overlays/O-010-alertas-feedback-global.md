# Overlay — O-010 Alertas y feedback global

> Patrón transversal para comunicar resultados, información, advertencias y errores que no pertenecen exclusivamente a un campo o componente local.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `O-010` |
| Nombre | Alertas y feedback global |
| Tipo | Toast, banner o alerta contextual según persistencia y alcance |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Leonidas Garcia |
| Revisor | Giuliano Macchiavello |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Propósito:** ofrecer una gramática visual y accesible consistente para feedback transversal.
- **Funcionalidades:** transversal a `F-001`–`F-040`; cada spec determina el mensaje y la recuperación.
- **Vistas que lo invocan:** `V-001`–`V-017` y overlays cuando el resultado no cabe en una región local.
- **Fuente UI:** [`DS-001`](../DS-001-sistema-diseno-marketplace.md), secciones de color semántico, UX writing, componentes y accesibilidad.

O-010 no reemplaza errores asociados a campos, estados vacíos, páginas completas de error ni overlays especializados `O-003`–`O-009`.

## 3. Activación y cierre

| Evento | Condición | Resultado |
|---|---|---|
| Mostrar toast | Resultado breve y no bloqueante | Aparece en región global sin mover foco. |
| Mostrar banner | Situación persistente que afecta una página/sección | Se integra cerca del encabezado o región afectada. |
| Mostrar alerta contextual | Problema recuperable ligado a una acción/región | Permanece junto al contexto y ofrece acción. |
| Acción | Reintentar, revisar, deshacer o navegar | Ejecuta una acción concreta una vez. |
| Cerrar | Mensaje descartable | Retira sólo la presentación; no deshace el resultado. |
| Repetición | Mismo evento/mensaje | Deduplica o actualiza el existente; no apila duplicados. |

## 4. Estructura, contenido y acciones

```text
Feedback
├── Icono semántico complementario
├── Título breve, cuando se necesita
├── Mensaje concreto y accionable
├── Acción primaria contextual, opcional
├── Acción secundaria, excepcional
└── Cerrar, si es descartable
```

| Variante | Uso | Persistencia | Ejemplo de acción |
|---|---|---|---|
| `success` | Resultado confirmado | Puede cerrar automáticamente si no requiere lectura/acción | Ver carrito |
| `info` | Contexto o transición | Temporal o persistente según relevancia | Ver detalles |
| `warning` | Atención sin fallo definitivo | Persistente hasta comprender/corregir | Revisar |
| `error` | Acción fallida o servicio no disponible | Persistente si requiere recuperación | Reintentar |

Reglas de contenido:

- Explicar qué ocurrió y qué puede hacer el usuario.
- Usar lenguaje del dominio, no códigos HTTP, nombres de excepciones, request IDs o infraestructura.
- No culpar al usuario ni prometer un resultado no confirmado.
- No incluir contraseñas, tokens, correo/dirección completos, documento, tarjeta u otros datos sensibles.
- Una acción principal por mensaje; una segunda sólo si resuelve una necesidad distinta.

## 5. Estados y variantes

| Estado o variante | Cuándo aparece | Cambio visual | Frame requerido |
|---|---|---|---|
| Toast éxito | Confirmación breve sin bloqueo | Fondo/icono/texto success | Sí |
| Toast informativo | Actualización neutral | Estilo info | Sí |
| Banner advertencia | Cotización, carrito o sesión requieren atención | Persistente y asociado al contexto | Sí |
| Alerta error recuperable | Solicitud falló | Mensaje + Reintentar | Sí |
| Error no recuperable localmente | Requiere navegar/soporte | Acción segura, sin reintento infinito | Sí, anotado |
| Acción en curso | Reintento activado | Acción ocupada, no repetible | Sí, anotado |
| Cola/deduplicación | Varios eventos | Máximo visible y prioridad definidos; duplicados agrupados | Sí |
| Offline/conectividad | Estado transversal confirmado | Banner persistente; no inventa resultados | Sí |

Prioridad sugerida: error bloqueante > warning accionable > success/info. Un mensaje nuevo no debe retirar otro crítico antes de que pueda comprenderse.

## 6. Responsive y accesibilidad

- Desktop: toasts en una región global consistente; banners dentro del ancho del contenido.
- Mobile: feedback respeta áreas seguras, navegación inferior, teclado y CTA persistentes; puede ocupar ancho disponible.
- `role="status"`/`aria-live="polite"` para success/info; `role="alert"` sólo para errores que requieren anuncio inmediato.
- No mover foco al toast. Banners/alertas de flujo pueden recibir foco programático cuando bloquean continuidad.
- Temporizadores se pausan con foco/hover y no se usan para mensajes críticos o con acciones esenciales.
- Color siempre se combina con icono y texto; contraste según WCAG 2.2 AA.
- Cerrar tiene nombre accesible; al desaparecer un toast no se pierde el foco.
- Reducir movimiento desactiva entradas/salidas animadas no esenciales.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `O-010 / Desktop / Toast success` | Desktop | Confirmación |
| `O-010 / Mobile / Toast info` | Mobile | Información |
| `O-010 / Desktop / Banner warning` | Desktop | Atención persistente |
| `O-010 / Mobile / Error con reintento` | Mobile | Recuperable |
| `O-010 / Desktop / Cola priorizada` | Desktop | Varios mensajes |
| `O-010 / Mobile / Sin conexión` | Mobile | Banner transversal |

Las instancias especializadas `O-005`–`O-009` usan este lenguaje visual, pero conservan sus propias specs y frames.

## 8. Criterios de aceptación visual

- [ ] `UI-O010-001`: Cada mensaje usa severidad coherente y combina texto, icono y color.
- [ ] `UI-O010-002`: Errores incluyen recuperación cuando existe y nunca exponen detalles técnicos.
- [ ] `UI-O010-003`: Feedback breve no roba foco; mensajes bloqueantes lo gestionan de forma explícita.
- [ ] `UI-O010-004`: Mensajes críticos o con acciones no desaparecen automáticamente antes de poder usarse.
- [ ] `UI-O010-005`: Eventos duplicados se deduplican y la cola conserva prioridad comprensible.
- [ ] `UI-O010-006`: Mobile no oculta navegación, teclado, áreas seguras o CTA esenciales.
- [ ] `UI-O010-007`: Cerrar la presentación no deshace una operación ya confirmada.
- [ ] El patrón cumple `DS-001`, WCAG 2.2 AA y reducción de movimiento.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `O-010-OPEN-01` | Aprobar posición global de toasts en desktop/mobile y convivencia con navegación/CTA. | UX/UI | Abierta |
| `O-010-OPEN-02` | Definir duraciones por severidad y reglas de pausa/tiempo extendido. | UX/UI + QA | Abierta |
| `O-010-OPEN-03` | Definir máximo visible, prioridad y deduplicación de la cola. | Frontend + UX | Abierta |
| `O-010-OPEN-04` | Aprobar catálogo de mensajes recurrentes y responsables de su copy. | Producto + UX | Abierta |
