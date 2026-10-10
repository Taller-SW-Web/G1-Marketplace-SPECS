# Spec funcional — F-006 Visualizar inicio, categorías y destacados

| ID | Estado |
|---|---|
| `F-006` | Aprobada; Catálogo/Taxonomía condicionados por `I-01`. |

Presenta inicio público con categorías activas y productos destacados comercialmente elegibles; enlaza a catálogo/ficha y excluye personalización/administración.

La elección de destacados se propone como curaduría editorial de Marketplace por identificadores de producto; Productos mantiene la autoridad sobre nombre, imagen, slug, precio y elegibilidad comercial. Esta frontera es una **propuesta pendiente de acuerdo F-P1-04**, no una capacidad ya publicada por Productos. Hasta homologarla, la sección puede omitirse y el inicio conserva categorías y navegación.

- Sólo categorías/productos activos y con tarjeta completa se muestran.
- Destacado sin imagen/slug válido se omite.

- [ ] **CA-F006-01:** Inicio vacío no bloquea navegación.
- [ ] **CA-F006-02:** Ningún destacado muestra datos locales que contradigan la proyección comercial vigente de Productos.
