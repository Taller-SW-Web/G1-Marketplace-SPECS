# Comunicación — C-### [Nombre]

> Especificación visual y de contenido de una comunicación externa al producto navegable.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `C-###` |
| Nombre | [Nombre] |
| Canal | [Correo electrónico] |
| Versión | `0.1.0` |
| Estado | Borrador |
| Responsable | Por asignar |
| Revisor | Por asignar |
| Enlace de Figma | Pendiente |

## 2. Propósito y trazabilidad

- **Evento de envío:** [Evento funcional].
- **Destinatario:** [Actor].
- **Funcionalidades:** [F-###].
- **Spec UI/funcional de origen:** [Enlaces].

## 3. Jerarquía del contenido

| Orden | Bloque | Contenido | Datos dinámicos | Obligatorio |
|---:|---|---|---|---:|
| 1 | Preheader | [Texto] | [Variable] | Sí/No |
| 2 | Encabezado | [Logo/título] | [Variable] | Sí/No |
| 3 | Cuerpo | [Mensaje] | [Variable] | Sí/No |
| 4 | Acción | [CTA] | [URL] | Sí/No |
| 5 | Pie | [Ayuda/legal] | [Variable] | Sí/No |

## 4. Copy y variables

| Elemento | Texto base | Variable | Fallback o restricción |
|---|---|---|---|
| Asunto | [Texto] | `{{variable}}` | [Regla] |

## 5. Estados y variantes

| Variante | Condición | Diferencia visible | Frame requerido |
|---|---|---|---|
| Principal | [Condición] | [Contenido] | Sí |
| Incidencia | [Condición] | [Mensaje/acción] | Sí/No |

## 6. Responsive, compatibilidad y accesibilidad

- Ancho y estructura desktop.
- Reflujo en mobile sin desplazamiento horizontal.
- Texto alternativo para imágenes informativas.
- Jerarquía semántica y orden de lectura.
- CTA comprensible sin depender del color.
- Información esencial disponible aunque las imágenes no carguen.
- Versión en texto plano o contenido equivalente.

## 7. Frames requeridos

| Frame | Plataforma | Estado |
|---|---|---|
| `C-### / Desktop / Principal` | Desktop | Principal |
| `C-### / Mobile / Principal` | Mobile | Principal |

## 8. Criterios de aceptación visual

- [ ] `UI-C###-001`: [Condición verificable].
- [ ] Todos los datos dinámicos y sus restricciones están identificados.
- [ ] La comunicación es legible en desktop y mobile.
- [ ] El contenido esencial funciona sin imágenes.
- [ ] La pieza aplica `DS-001` sin usar patrones exclusivos de la interfaz web.

## 9. Decisiones pendientes

| ID | Pregunta o decisión | Responsable | Estado |
|---|---|---|---|
| `C-###-OPEN-01` | [Pendiente] | Por asignar | Abierta |
