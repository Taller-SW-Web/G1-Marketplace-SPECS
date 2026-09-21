**Sí, es necesario actualizar el diagrama de navegación del canal** [128–130].

Al redefinir la **Pantalla 8 (P8: Carrito de Compras)** para que sea una **vista de página completa independiente (`/carrito`)** en lugar de un panel lateral emergente (_drawer_), la arquitectura de navegación cambia en los siguientes puntos clave:

1. **Ruta Dedicada del Carrito (`/carrito`)**: La navegación desde el botón "Bolsa" de la cabecera (P5, P6), el botón "Agregar al Carrito" de la ficha técnica (P7) o la acción "Mover a la Bolsa" de Favoritos (P9) pasa a ser una transición de página completa hacia **P8** [129, 186–188].
2. **Estado Vacío y Retorno al Catálogo**: La **P8** incorpora un flujo directo de retorno mediante el botón **"Explorar Tienda"** hacia la vitrina (**P5/P6**).
3. **Flujo de Autenticación Interceptado**: Si el usuario no tiene sesión iniciada al hacer clic en **"Iniciar Checkout"** dentro de **P8**, la aplicación lo redirige a la pantalla completa de **Inicio de Sesión (P1)**, unificando la bolsa anónima previa y permitiendo el paso posterior al **Checkout Paso 1 (P10)**.

---

### **Diagrama de Navegación Actualizado del Canal (15 Pantallas Web)**

```mermaid.js
flowchart TD
    %% SUBGRAPH: VITRINA Y EXPLORACIÓN
    subgraph VEC["Vitrina y Exploración del Catálogo (EP-VEC)"]
        P5["P5: Página Principal / Home"]
        P6["P6: Catálogo, Búsqueda y Filtros"]
    end

    %% SUBGRAPH: GESTIÓN DE ACCESOS
    subgraph GAC["Gestión de Accesos del Cliente (EP-GAC)"]
        P1["P1: Vista de Inicio de Sesión (Login)"]
        P2["P2: Vista de Registro de Cliente"]
        P3["P3: Vista de Recuperación de Clave"]
        P4["P4: Vista de Restablecimiento / Reset"]
    end

    %% SUBGRAPH: DETALLE DE PRODUCTO
    subgraph DDP["Detalle y Disponibilidad (EP-DDP)"]
        P7["P7: Ficha Técnica y Variantes"]
    end

    %% SUBGRAPH: CARRITO Y FAVORITOS
    subgraph ITC["Intención de Transacción y Carrito (EP-ITC)"]
        P8["P8: Vista Principal del Carrito (/carrito)"]
        P9["P9: Vista 'Mis Favoritos' (/favoritos)"]
    end

    %% SUBGRAPH: CHECKOUT MULTIPASO
    subgraph TRX["Transacción y Checkout (EP-TRX)"]
        P10["P10: Checkout Paso 1 (Dirección)"]
        P11["P11: Checkout Paso 2 (Pago & Cupones)"]
        P12["P12: Checkout Paso 3 (Confirmación)"]
    end

    %% SUBGRAPH: HISTORIAL Y TRACKING
    subgraph SHP["Historial y Seguimiento (EP-SHP)"]
        P13["P13: Panel 'Mis Pedidos'"]
        P14["P14: Detalle de Pedido + Reorder"]
        P15["P15: Vista Tracking de Envío"]
    end

    %% ==========================================
    %% FLUJOS Y TRANSICIONES DE NAVEGACIÓN
    %% ==========================================

    %% Rutas de Exploración
    P5 -->|"Buscador / Categorías"| P6
    P5 -->|"Clic Producto Destacado"| P7
    P6 -->|"Clic en Grilla"| P7
    P7 -->|"Navegar Recomendados"| P7

    %% Rutas de Acceso al Carrito y Favoritos
    P5 -.->|"Header: Bolsa"| P8
    P6 -.->|"Header: Bolsa"| P8
    P7 -->|"Agregar al Carrito"| P8
    P5 -.->|"Header: Mis Favoritos"| P9
    P6 -.->|"Header: Mis Favoritos"| P9

    %% Transferencia entre Carrito y Favoritos
    P8 <-->|"Mover a Favoritos / Mover a la Bolsa"| P9
    P8 -.->|"Carrito Vacío: 'Explorar Tienda'"| P5

    %% Rutas de Autenticación (Pantallas Dedicadas)
    P5 -.->|"Header: 'Mi Cuenta'"| P1
    P6 -.->|"Header: 'Mi Cuenta'"| P1
    P7 -.->|"Guardar Favorito (Sin Sesión)"| P1
    P8 -.->|"Iniciar Checkout (Sin Sesión)"| P1
    P9 -.->|"Acceso (Sin Sesión)"| P1

    P1 <-->|"Enlace 'Crear cuenta' / 'Inicia sesión'"| P2
    P1 -->|"Enlace '¿Olvidaste tu contraseña?'"| P3
    P3 -->|"Enlace 'Volver al Login'"| P1
    P3 -.->|"Enlace enviado por Email"| P4
    P4 -->|"Clave Actualizada"| P1

    P1 -.->|"Login Exitoso (Redirección al Origen)"| P5
    P1 -.->|"Login Exitoso + Unificación Carrito"| P8
    P1 -.->|"Login Exitoso"| P10
    P1 -.->|"Login Exitoso"| P9

    %% Flujo de Checkout
    P8 -->|"Iniciar Checkout (Autenticado)"| P10
    P10 -->|"Dirección Validada"| P11
    P11 -->|"Pago & Stock Aprobados"| P12

    %% Transiciones desde Confirmación
    P12 -->|"Boton 'Seguir Comprando'"| P5
    P12 -->|"Boton 'Ver Mi Pedido'"| P14

    %% Postventa y Seguimiento
    P5 -.->|"Header: Mis Pedidos"| P13
    P13 -->|"Seleccionar Orden"| P14
    P13 -->|"Ver Tracking"| P15
    P14 -->|"Rastrear Envío"| P15
    P14 -->|"Volver a Comprar (Reorder)"| P8
```

---

🛒 Con esta actualización, tanto la especificación formal del prototipo (**`especificacion-pantallas-prototipo-v5.md`**) como el **Diagrama de Navegación** reflejan la misma estructura para la generación en **Stitch AI**.