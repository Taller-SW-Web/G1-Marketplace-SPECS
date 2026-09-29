# Diagrama de navegación vigente del Marketplace

Este documento representa la navegación entre las 17 vistas vigentes y sus relaciones principales con overlays y comunicaciones. Los IDs y rutas proceden del [`catálogo de vistas`](../SPECS/ui/vistas/README.md); el comportamiento detallado continúa definido por las specs `F-001` a `F-040`.

## Convenciones

- Flecha continua: navegación entre rutas.
- Flecha punteada: apertura de overlay, retorno condicionado o comunicación externa.
- Los overlays no son rutas ni sustituyen a las vistas.
- La navegación posterior al login regresa al origen protegido o a la acción que solicitó autenticación.

## Navegación principal

```mermaid
flowchart TD
    subgraph ACCESO["Cuenta y acceso"]
        V001["V-001 · Login<br/>/login"]
        V002["V-002 · Registro<br/>/registro"]
        V003["V-003 · Recuperación<br/>/recuperar-contrasena"]
        V004["V-004 · Restablecimiento<br/>/restablecer-contrasena"]
    end

    subgraph DESCUBRIMIENTO["Descubrimiento y producto"]
        V005["V-005 · Inicio<br/>/"]
        V006["V-006 · Catálogo y resultados<br/>/catalogo"]
        V007["V-007 · Ficha del producto<br/>/productos/{slug}"]
    end

    subgraph INTENCION["Carrito y favoritos"]
        V008["V-008 · Carrito<br/>/carrito"]
        V009["V-009 · Favoritos<br/>/favoritos"]
    end

    subgraph CHECKOUT["Checkout y orden"]
        V010["V-010 · Dirección de envío<br/>/checkout/direccion"]
        V011["V-011 · Resumen, envío y beneficio<br/>/checkout/resumen"]
        V012["V-012 · Pago simulado<br/>/checkout/pago"]
        V013["V-013 · Creación de la orden<br/>/checkout/confirmacion"]
        V014["V-014 · Pedido confirmado<br/>/checkout/confirmado/{orderId}"]
    end

    subgraph POSTVENTA["Pedidos y entrega"]
        V015["V-015 · Historial de pedidos<br/>/mis-pedidos"]
        V016["V-016 · Detalle y reordenado<br/>/mis-pedidos/{orderId}"]
        V017["V-017 · Seguimiento<br/>/mis-pedidos/{orderId}/seguimiento"]
    end

    V005 -->|"Buscar o elegir categoría"| V006
    V005 -->|"Abrir producto destacado"| V007
    V006 -->|"Abrir producto"| V007
    V007 -->|"Abrir producto relacionado"| V007

    V001 <-->|"Crear cuenta / Iniciar sesión"| V002
    V001 -->|"Olvidé mi contraseña"| V003
    V003 -.->|"Enlace recibido por correo"| V004
    V003 -->|"Volver"| V001
    V004 -->|"Contraseña actualizada"| V001
    V001 -.->|"Éxito: volver al origen"| V005

    V005 -->|"Abrir carrito"| V008
    V006 -->|"Abrir carrito"| V008
    V007 -->|"Abrir carrito"| V008
    V005 -->|"Abrir favoritos"| V009
    V006 -->|"Abrir favoritos"| V009
    V007 -->|"Abrir favoritos"| V009
    V008 -->|"Explorar tienda"| V005
    V008 -->|"Mover a favoritos"| V009
    V009 -->|"Producto con variantes"| V007
    V009 -->|"Producto simple disponible"| V008

    V008 -->|"Checkout autenticado"| V010
    V008 -.->|"Checkout sin sesión: login con retorno"| V001
    V010 -->|"Dirección válida"| V011
    V011 -->|"Resumen aceptado"| V012
    V012 -->|"Pago simulado preparado"| V013
    V013 -->|"Orden creada"| V014
    V014 -->|"Seguir comprando"| V005
    V014 -->|"Ver mi pedido"| V016

    V005 -->|"Mis pedidos"| V015
    V015 -->|"Abrir pedido"| V016
    V015 -->|"Ver seguimiento"| V017
    V016 -->|"Rastrear envío"| V017
    V016 -->|"Ver carrito tras reordenar"| V008
    V017 -->|"Volver al pedido"| V016
```

## Overlays dentro del flujo

```mermaid
flowchart LR
    V006["V-006 Catálogo"] -.-> O001["O-001 Filtros mobile"]
    V015["V-015 Historial"] -.-> O001
    V007["V-007 Producto"] -.-> O002["O-002 Visor de galería"]

    PROTEGIDA["Acción protegida en V-005 a V-009"] -.-> O003["O-003 Autenticación requerida"]
    O003 --> V001["V-001 Login"]
    V001 -.-> ORIGEN["Retorno a vista y acción de origen"]

    CHECKOUT["V-010 a V-013"] -.-> O004["O-004 Confirmar cierre de sesión"]
    V007 -.-> O005["O-005 Producto agregado"]
    O005 --> V008["V-008 Carrito"]
    V008 -.-> O006["O-006 Deshacer eliminación"]
    V009 -.-> O006
    V001 -.-> O007["O-007 Resultado de fusión"]
    V016["V-016 Detalle"] -.-> O008["O-008 Resultado de reordenado"]
    ENTREGADO["Pedido entregado"] -.-> O009["O-009 Evaluación postentrega"]
    GLOBAL["Cualquier vista"] -.-> O010["O-010 Alertas y feedback global"]
```

## Comunicaciones externas

```mermaid
flowchart LR
    V014["V-014 Pedido confirmado"] -.-> C001["C-001 Correo de confirmación"]
    EVENTO["Cambio de estado de despacho"] -.-> C002["C-002 Correo de actualización"]
    C001 -.-> V016["V-016 Detalle del pedido"]
    C002 -.-> V017["V-017 Seguimiento"]
```

## Reglas resueltas

1. Login, registro, recuperación y restablecimiento son vistas con ruta propia (`V-001` a `V-004`). `O-003` sólo explica la autenticación requerida y conserva el retorno.
2. El carrito es una vista completa (`V-008`), no un drawer.
3. El pago de `V-012` es una simulación explícita sin tarjeta, CVV ni iconografía de cobro real.
4. La preparación del pago (`V-012`), la creación de la orden (`V-013`) y la confirmación (`V-014`) son resultados distintos.
5. Reordenar agrega artículos disponibles al carrito mediante `O-008`; no confirma una compra.
6. Los correos se documentan como comunicaciones `C-###` y no como pantallas navegables.

## Pendientes que no cambian la arquitectura

- Confirmar el patrón visual final de la navegación global en desktop y mobile.
- Confirmar desde qué superficies exactas se ofrece la evaluación postentrega `O-009`.
- Completar en cada spec la conservación de filtros, scroll, carrito y ruta de retorno.
