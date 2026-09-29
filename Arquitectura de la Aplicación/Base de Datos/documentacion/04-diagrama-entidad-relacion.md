# Diagrama entidad-relación

Esta vista representa conceptos del dominio y sus cardinalidades. Incluye entidades externas para explicar de dónde provienen los identificadores, pero no describe claves foráneas físicas.

```mermaid
erDiagram
    CLIENTE_EXTERNO o|--o{ CARRITO : "identifica"
    SESION_ANONIMA o|--o{ CARRITO : "identifica"
    CARRITO ||--o{ LINEA_CARRITO : "contiene"
    CARRITO ||--o{ OPERACION_CHECKOUT : "origina"
    CARRITO o|--o{ CARRITO : "recibe fusiones"

    CLIENTE_EXTERNO ||--o{ FAVORITO : "guarda"
    PRODUCTO_EXTERNO ||--o{ FAVORITO : "es guardado"

    SKU_EXTERNO ||--o{ LINEA_CARRITO : "identifica compra"
    PRODUCTO_EXTERNO o|--o{ LINEA_CARRITO : "apoya navegacion"
    VARIANTE_EXTERNA o|--o{ LINEA_CARRITO : "apoya presentacion"

    CLIENTE_EXTERNO ||--o{ OPERACION_CHECKOUT : "confirma"
    PEDIDO_EXTERNO o|--o{ OPERACION_CHECKOUT : "resulta de"

    CLIENTE_EXTERNO ||--o{ INVITACION_POSTENTREGA : "recibe"
    PEDIDO_EXTERNO ||--o{ INVITACION_POSTENTREGA : "habilita"

    CLIENTE_EXTERNO ||--o{ ENTREGA_NOTIFICACION : "es destinatario"
    PEDIDO_EXTERNO ||--o{ ENTREGA_NOTIFICACION : "genera"

    CLIENTE_EXTERNO {
        uuid customerId
    }
    SESION_ANONIMA {
        string secretHash
    }
    PRODUCTO_EXTERNO {
        string productId
    }
    VARIANTE_EXTERNA {
        string variantId
    }
    SKU_EXTERNO {
        string sku
    }
    PEDIDO_EXTERNO {
        string pedidoId
    }
    CARRITO {
        uuid id
        string owner
        string state
        int version
    }
    LINEA_CARRITO {
        uuid id
        string sku
        int quantity
        decimal priceSnapshot
    }
    FAVORITO {
        uuid id
        uuid customerId
        string productId
    }
    OPERACION_CHECKOUT {
        uuid id
        string idempotencyKey
        string state
        string externalOrderId
    }
    INVITACION_POSTENTREGA {
        uuid id
        string externalOrderId
        string state
    }
    ENTREGA_NOTIFICACION {
        uuid id
        string eventKey
        string type
        string state
    }
```

## Cómo leerlo

- `CLIENTE_EXTERNO`, `SESION_ANONIMA`, `PRODUCTO_EXTERNO`, `VARIANTE_EXTERNA`, `SKU_EXTERNO` y `PEDIDO_EXTERNO` no son tablas del Marketplace.
- Un carrito tiene exactamente un tipo de propietario: cliente o sesión anónima. El XOR se expresa como regla porque Mermaid no tiene una notación directa para esta exclusión.
- Las asociaciones con entidades externas representan identificadores intercambiados por API.
- La única relación recursiva es la trazabilidad de un carrito anónimo fusionado hacia su carrito autenticado receptor.
- La vista física contiene sólo las FK realmente creadas en PostgreSQL.
