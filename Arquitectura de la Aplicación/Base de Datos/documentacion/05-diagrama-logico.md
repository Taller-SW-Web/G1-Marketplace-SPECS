# Diagrama lógico

Esta vista muestra qué información conserva Marketplace y qué información consulta o referencia en módulos dueños.

```mermaid
flowchart LR
    subgraph MKT["Marketplace - persistencia local"]
        C["Cart<br/>propietario, estado, version"]
        CI["CartItem<br/>sku, cantidad, snapshot"]
        W["WishlistItem<br/>producto guardado"]
        CO["CheckoutOperation<br/>idempotencia y resultado"]
        PP["PostDeliveryPrompt<br/>estado UX"]
        ND["NotificationDelivery<br/>salida de correo"]

        C -->|"1:N local"| CI
        C -->|"1:N local"| CO
        C -->|"fusion local"| C
    end

    subgraph SEC["Seguridad y Usuarios"]
        CUSTOMER["Cliente<br/>customerId"]
        SESSION["Sesion anonima<br/>secreto de cookie"]
    end

    subgraph PROD["Productos y Ofertas"]
        PRODUCT["Producto<br/>productId"]
        VARIANT["Variante<br/>variantId"]
        SKU["Unidad comprable<br/>sku"]
        PRICE["Precio y disponibilidad<br/>autoritativos"]
    end

    subgraph SALES["Ventas y Postventa"]
        ORDER["Pedido<br/>pedidoId"]
        CSAT["Calificacion CSAT"]
    end

    subgraph DISPATCH["Despacho y Entrega"]
        TRACKING["Tracking y entrega"]
    end

    CUSTOMER -. "customerId" .-> C
    CUSTOMER -. "customerId" .-> W
    CUSTOMER -. "customerId" .-> CO
    CUSTOMER -. "customerId" .-> PP
    CUSTOMER -. "customerId" .-> ND
    SESSION -. "hash, no secreto" .-> C

    SKU -. "sku" .-> CI
    PRODUCT -. "productId" .-> CI
    VARIANT -. "variantId" .-> CI
    PRODUCT -. "productId" .-> W
    PRICE -. "revalidacion" .-> CI

    CO -. "crea y referencia" .-> ORDER
    ORDER -. "pedidoId" .-> PP
    ORDER -. "pedidoId" .-> ND
    PP -. "registra respuesta" .-> CSAT
    TRACKING -. "confirma entrega" .-> PP
    TRACKING -. "evento homologado pendiente" .-> ND
```

## Leyenda

- Flecha continua: relación local implementada mediante FK o autorreferencia.
- Flecha discontinua: integración o referencia externa sin FK.
- Los snapshots de precio son informativos; la fuente autoritativa permanece en Productos y Ofertas.
- `PostDeliveryPrompt` no contiene la respuesta CSAT.
- `NotificationDelivery` no contiene el pedido ni el historial de despacho.
- La entrada de actualizaciones de despacho permanece condicionada por `I-05`.
