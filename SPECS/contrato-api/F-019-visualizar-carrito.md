# Spec de contrato API — F-019 Visualizar el carrito

`GET /api/v1/carts/current`

```json
{"data":{"cartId":"CART-1","version":5,"items":[{"sku":"AERO-42-BLK","product":{"slug":"aero-x","name":"Aero X","imageUrl":"https://cdn.example.com/a.webp"},"quantity":2,"unitPrice":{"amount":170,"currency":"PEN","version":8},"availability":"AVAILABLE","attention":null}],"subtotal":{"amount":340,"currency":"PEN"}}}
```

`items` puede ser vacío. `subtotal` es `null` si una línea no posee precio vigente. Errores: `503 CART_ENRICHMENT_UNAVAILABLE` sólo cuando no se puede devolver ni representación local coherente; de otro modo devuelve `200` con `attention` por línea. Autenticación/cookie como F-016. No se devuelven dirección, cupón, envío ni impuesto.

- [ ] **API-CA-F019-01:** Un carrito vacío devuelve arreglo vacío y versión.
- [ ] **API-CA-F019-02:** Precio/stock externo no cambia cantidad local en una lectura.
