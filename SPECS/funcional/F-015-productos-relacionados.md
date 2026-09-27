# Spec funcional — F-015 Visualizar productos relacionados

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `F-015` |
| Versión | `0.1.0` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |

## 2. Objetivo y alcance

Presenta candidatos Cross-sell y Upsell relevantes debajo de la ficha para facilitar exploración. Incluye orden, deduplicación, tarjetas y enlace; excluye personalización por IA, añadir automáticamente al carrito y garantía de precio/stock final.

## 3. Reglas y comportamiento

- **RN-F015-01:** Promociones es dueño de reglas y candidatos; sólo participan reglas activas, vigentes y productos activos con disponibilidad.
- **RN-F015-02:** El orden es prioridad de regla ascendente y orden de presentación ascendente; duplicados conservan la primera aparición.
- **RN-F015-03:** Marketplace enriquece cada `productId` candidato con catálogo para obtener slug, nombre e imagen. Si no logra una tarjeta comercial completa, omite sólo ese candidato.
- **RN-F015-04:** El precio y disponibilidad son informativos; abrir la ficha aplica F-011 a F-014 y no conserva promesas anteriores.
- **RN-F015-05:** Lista vacía es resultado válido y se oculta la sección, sin error.

Flujo: al cargar la ficha, BFF consulta candidatos por producto/categoría, filtra/enriquece y muestra hasta 8 tarjetas en orden. Fallo recuperable: se oculta la región y registra incidente; no bloquea la ficha.

- [ ] **CA-F015-01:** Un producto repetido por dos reglas se visualiza una vez en posición de mayor prioridad.
- [ ] **CA-F015-02:** Una tarjeta lleva a su slug propio y no añade ni reemplaza el producto actual.
- [ ] **CA-F015-03:** La ausencia de resultados no muestra carrusel vacío.

## 4. Dependencias

Fuente: `SPEC-007`, `EXT-OUT-REC-01` y Catálogo. El enriquecimiento de tarjeta resuelve que la respuesta externa mínima no contiene nombre/slug/imagen; la estrategia batch y OpenAPI quedan por homologar en `I-01`.
