# Vista — V-### [Nombre]

> Especificación del entregable visual para una pantalla completa en desktop y mobile.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-###` |
| Nombre | [Nombre de la vista] |
| Ruta | `/ruta` |
| Versión | `0.1.0` |
| Estado | Borrador |
| Responsable | Por asignar |
| Revisor | Por asignar |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** [Resultado que busca conseguir].
- **Actor principal:** [Visitante/cliente autenticado].
- **Permiso:** [Público/autenticado/condicional].
- **Condiciones de entrada:** [Datos, sesión o contexto necesario].
- **Resultado esperado:** [Estado o destino tras completar la tarea].

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-###` | [Enlace] | [Enlace] | [Comportamiento o contenido] |

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| [Origen] | [Destino] | [Condición] | [Filtros, retorno, carrito, sesión, etc.] |

## 5. Jerarquía y composición visual

```text
V-### [Nombre]
├── Navegación global [si aplica]
├── Región principal
│   ├── [Bloque]
│   └── [Bloque]
└── Pie o navegación secundaria [si aplica]
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| [Región] | [Elemento] | Primaria/Secundaria | [Regla] |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| [Elemento] | [Copy o dato] | [Acción] | [Condición] |

## 7. Estados de la vista

Documentar únicamente los estados aplicables; si uno no aplica, justificarlo.

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Principal | Entrada válida | [Contenido] | [Acción] | Sí |
| Cargando | Espera de datos | [Skeleton/progreso] | Esperar/cancelar | Sí/No |
| Vacío | Sin resultados o elementos | [Mensaje y ayuda] | [CTA] | Sí/No |
| Error recuperable | Fallo temporal | [Mensaje] | Reintentar | Sí/No |
| No disponible | Recurso inexistente o sin stock | [Mensaje] | [Alternativa] | Sí/No |
| Validación | Datos inválidos | [Errores junto al campo] | Corregir | Sí/No |
| Conflicto | Datos cambiaron durante el flujo | [Explicación] | Revisar/volver | Sí/No |
| Éxito | Tarea completada | [Confirmación] | Continuar | Sí/No |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-###` / `C-###` | [Nombre] | [Condición] | [Acción] |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| [Campo] | [Tipo] | Sí/No | [Regla] | [Copy] | Default/error/éxito |

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- **Composición:** [Columnas, anchos máximos y jerarquía].
- **Cambios relevantes:** [Reglas].

### Mobile

- **Referencia:** 390 px.
- **Composición:** [Orden, apilamiento y controles].
- **Cambios relevantes:** [Navegación, overlays o acciones persistentes].

### Anchuras intermedias

- [Regla de adaptación; evitar depender de un único punto de quiebre].

## 11. Accesibilidad

- Orden de foco y navegación por teclado.
- Nombre accesible de iconos y controles.
- Asociación entre etiquetas, ayuda y errores.
- Gestión del foco al navegar o abrir overlays.
- No depender sólo del color para comunicar estado.
- Objetivos táctiles, contraste y reducción de movimiento según `DS-001`.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-### / Desktop / Principal` | Desktop | Principal | [Contenido] |
| `V-### / Mobile / Principal` | Mobile | Principal | [Contenido] |

## 13. Criterios de aceptación visual

- [ ] `UI-V###-001`: [Condición verificable].
- [ ] `UI-V###-002`: [Condición verificable].
- [ ] Existen variantes desktop y mobile de todos los estados obligatorios.
- [ ] La navegación y los overlays coinciden con las specs enlazadas.
- [ ] No se introducen componentes o estilos fuera de `DS-001` sin registrar la decisión.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-###-OPEN-01` | [Pendiente] | Por asignar | Por definir | Abierta |
