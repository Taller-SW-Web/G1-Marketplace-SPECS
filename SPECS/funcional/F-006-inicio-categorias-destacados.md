# Spec funcional — F-006 Visualizar inicio, categorías y destacados

| ID | Estado |
|---|---|
| `F-006` | Aprobada; Catálogo/Taxonomía condicionados por `I-01`. |

Presenta inicio público con categorías activas y productos destacados comercialmente elegibles; enlaza a catálogo/ficha y excluye personalización/administración.

La elección de destacados se propone como curaduría editorial de Marketplace por identificadores de producto; Productos mantiene la autoridad sobre nombre, imagen, slug, precio y elegibilidad comercial. Esta frontera es una **propuesta pendiente de acuerdo F-P1-04**, no una capacidad ya publicada por Productos. Hasta homologarla, la sección puede omitirse y el inicio conserva categorías y navegación.

Ajuste solicitado por Giuliano el 16/10/2026, pendiente de revisión: la imagen de producto es opcional y su ausencia se representa con un placeholder local de Marketplace, sin atribuirlo a G6 ni alterar elegibilidad o selección de destacados.

- Sólo categorías/productos activos y con los datos públicos requeridos se muestran; la imagen puede estar ausente.
- Destacado sin slug válido se omite. Si sólo falta la imagen, la tarjeta conserva el producto y muestra «Sin imagen».

- [ ] **CA-F006-01:** Inicio vacío no bloquea navegación.
- [ ] **CA-F006-02:** Ningún destacado muestra datos locales que contradigan la proyección comercial vigente de Productos.
