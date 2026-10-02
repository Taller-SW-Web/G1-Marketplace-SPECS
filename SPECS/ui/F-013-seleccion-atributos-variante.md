# Spec UI — F-013 Seleccionar atributos y variante del producto

| Campo | Valor |
|---|---|
| ID | `F-013` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |
| Sistema de diseño | `DS-001` v`0.1.0` |
| Ruta | `/productos/{slug}` |

```text
Región de compra de la ficha
├── Grupo “Color” → botones de opción
├── Grupo “Talla” → botones de opción
├── Mensaje de combinación no disponible (si aplica)
└── Resumen de selección accesible
```

| Estado | Interfaz |
|---|---|
| Cargando | Skeleton de controles, sin valores ficticios. |
| Sin variantes | No se renderiza la región; aplica SKU simple. |
| Selección incompleta | Grupos activos y texto “Selecciona tus opciones”. |
| Selección válida | Valores elegidos y actualización de imagen/precio/stock independientes. |
| Combinación inválida | Valor deshabilitado con explicación; no conserva un SKU previo. |
| Error | Mensaje y Reintentar sólo variantes. |

- Los valores son `button` agrupados con `fieldset`/`legend`, no sólo círculos de color; color incorpora etiqueta textual.
- La selección se distingue con borde, icono y `aria-pressed`, no sólo color. Objetivos táctiles de 44 px y foco visible según DS-001.
- En móvil los grupos se apilan; en desktop permanecen en el resumen comercial. Cambios se anuncian con `aria-live="polite"` sin mover foco.

- [ ] **UI-F013-01:** Teclado y lector de pantalla permiten identificar atributo, valor, seleccionado y no disponible.
- [ ] **UI-F013-02:** Elegir un valor incompatible elimina la selección inválida y comunica el resultado.
- [ ] **UI-F013-03:** El estado agotado futuro de F-014 no se representa como una variante inexistente.

Pendiente: prototipo Figma y homologación `I-01`.
