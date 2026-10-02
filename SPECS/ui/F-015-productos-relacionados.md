# Spec UI — F-015 Visualizar productos relacionados

| Campo | Valor |
|---|---|
| ID | `F-015` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |
| Sistema de diseño | `DS-001` v`0.1.0` |

```text
Productos relacionados
├── Título de sección
└── Lista horizontal o cuadrícula de ProductCard
    ├── Imagen, marca y nombre
    ├── Precio informativo
    └── Etiqueta Cross-sell/Upsell si es comprensible para UX
```

| Estado | Interfaz |
|---|---|
| Cargando | Skeletons de tarjetas. |
| Con resultados | Entre 1 y 8 tarjetas, en orden recibido. |
| Vacío/error | Sección omitida; no hay bloque vacío ni alerta invasiva. |

La tarjeta completa es enlace a `/productos/{slug}`; no usa botón de carrito. En móvil hay desplazamiento horizontal con controles de teclado alternativos; en desktop cuadrícula o carrusel sólo si conserva navegación por teclado. Imagen y nombre accesibles; no se usa autoplay.

- [ ] **UI-F015-01:** Una tarjeta es operable por teclado y anuncia nombre/precio antes de tipo comercial.
- [ ] **UI-F015-02:** Sin resultados válidos no queda título ni contenedor vacío.
