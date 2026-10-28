# Spec funcional — F-039 Agregar al carrito conservando favorito

Decisión del responsable solicitante, 28/10/2026: conservar el favorito en éxito y fallo. Sustituye la semántica previa de mover/eliminar. Revisión independiente de Fernando Saire pendiente; no acredita cierre de las issues #190–#194.

| ID | Estado |
|---|---|
| `F-039` | Cambio conservar favorito en revisión; Catálogo/stock condicionados por `I-01`. |

Agrega una unidad al carrito y conserva el favorito y su fecha original. Producto simple usa SKU vendible; producto con variantes redirige a ficha para F-013. Cada solicitud explícita agrega una unidad; no se anuncia idempotencia ni se repiten mutaciones automáticamente.

- [ ] **CA-F039-01:** Fallo de carrito no elimina favorito.
- [ ] **CA-F039-02:** Variante requerida abre ficha, no elige SKU arbitrario.
- [ ] **CA-F039-03:** Éxito actualiza el carrito sin eliminar ni cambiar la fecha del favorito.
