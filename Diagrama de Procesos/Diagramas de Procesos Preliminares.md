### **1. Proceso de Selección, Carrito y Compra de Productos (EP-ITC, EP-TRX, EP-SNT)**

Describe el recorrido funcional completo del cliente desde la selección de artículos en la vitrina hasta la confirmación de la compra y la emisión de recomendaciones. Incorpora la gestión del carrito como proceso cíclico, un nuevo rombo de decisión ante productos agotados y la integración del **Subproceso de Confirmación y Recomendaciones de Catálogo**.

```mermaid
flowchart TD
    Inicio([Inicio: Cliente en la Tienda]) --> SeleccionarProducto[Explorar y seleccionar producto con variante de talla y color]
    SeleccionarProducto --> VerificarStock{¿Hay inventario disponible?}

    %% Flujo Sin Stock (Nuevo Rombo de Decisión)
    VerificarStock -- No --> MostrarAgotado[Mostrar mensaje de producto agotado]
    MostrarAgotado --> DecisionAgotado{¿Qué desea hacer?}
    DecisionAgotado -- Regresar a Exploración --> SeleccionarProducto
    DecisionAgotado -- Finalizar Navegación --> FinAgotado([Fin: Producto Agotado])

    %% Flujo Con Stock y Carrito Cíclico
    VerificarStock -- Sí --> AgregarBolsa[Agregar producto a la bolsa / carrito de compras]
    AgregarBolsa --> GestionarCarrito[Gestionar Carrito: Modificar cantidades / Aplicar cupón]
    GestionarCarrito --> DecisionCarrito{¿Desea seguir comprando o ir al Checkout?}
    
    DecisionCarrito -- Seguir Comprando --> SeleccionarProducto
    DecisionCarrito -- Iniciar Checkout --> ValidarSesion{¿Tiene la sesión iniciada?}

    %% Autenticación
    ValidarSesion -- No --> SubprocesoAcceso[[Subproceso: Registro y Acceso a la Cuenta - Diagrama 2]]
    SubprocesoAcceso --> PasoDireccion
    ValidarSesion -- Sí --> PasoDireccion[Ingresar o seleccionar dirección de entrega]

    %% Revalidación y Pago
    PasoDireccion --> RevalidarInventario{¿El inventario sigue disponible?}
    RevalidarInventario -- No --> AlertaSinStock[Notificar cambio de disponibilidad de producto] --> DecisionAgotado

    RevalidarInventario -- Sí --> IngresarPago[Ingresar datos de pago y confirmar]
    IngresarPago --> ValidarPago{¿Pago autorizado?}

    ValidarPago -- No --> ErrorPago[Mostrar mensaje de error en el pago] --> IngresarPago

    ValidarPago -- Sí --> VaciarBolsa[Vaciar la bolsa de compras del cliente]
    VaciarBolsa --> SubprocesoConfirmacion[[Subproceso: Confirmación y Recomendaciones de Catálogo]]
    SubprocesoConfirmacion --> FinCompra([Fin del Proceso de Compra])
```

---

### **2. Proceso de Registro y Acceso a la Cuenta (EP-GAC, EP-ITC)**

Muestra los caminos de decisión para el registro de nuevos usuarios, el inicio de sesión y la delegación del flujo "Olvidó su clave" como un **subproceso reutilizable** que retorna al inicio de sesión tras actualizar las credenciales.

```mermaid
flowchart TD
    InicioAcceso([Inicio: Cliente requiere acceder a su cuenta]) --> ElegirOpcion{¿Qué acción desea realizar?}

    %% Registro de Cuenta
    ElegirOpcion -- Crear Cuenta --> FormRegistro[Completar datos personales en formulario]
    FormRegistro --> ValidarCorreo{¿El correo ya está registrado?}
    ValidarCorreo -- Sí --> AlertaCorreoExiste[Mostrar alerta de correo en uso] --> FormRegistro
    ValidarCorreo -- No --> CrearCuenta[Crear cuenta de usuario]
    CrearCuenta --> ConfirmacionRegistro[Mostrar confirmación e invitar a iniciar sesión] --> FormLogin

    %% Iniciar Sesión y Enlace a Subproceso de Recuperación
    ElegirOpcion -- Iniciar Sesión --> FormLogin[Ingresar correo y contraseña]
    FormLogin --> DecisionLogin{¿Credenciales válidas o olvidó clave?}
    
    DecisionLogin -- Credenciales Correctas --> AbrirPerfil[Conceder acceso a la cuenta]
    AbrirPerfil --> UnificarBolsa[Consolidar productos guardados anónimamente] --> FinLogin([Fin: Sesión Iniciada])
    
    DecisionLogin -- Credenciales Incorrectas --> ErrorLogin[Mostrar mensaje de error genérico] --> FormLogin
    DecisionLogin -- Olvidó su Clave --> SubprocesoRecuperar[[Subproceso: Recuperación y Restablecimiento de Clave]]

    %% Acceso Directo a Olvidó Clave
    ElegirOpcion -- Olvidó su Clave --> SubprocesoRecuperar
    SubprocesoRecuperar --> FormLogin
```

#### **Subproceso: Recuperación y Restablecimiento de Clave (Reutilizable)**
```mermaid
flowchart TD
    InicioRecuperar([Inicio: Solicitud de Recuperación]) --> FormRecuperar[Ingresar correo electrónico registrado]
    FormRecuperar --> MensajeNeutro[Mostrar mensaje neutro de instrucciones enviadas por seguridad]
    MensajeNeutro --> AbrirEnlace[Cliente abre enlace recibido en su buzón de correo]
    AbrirEnlace --> ValidarEnlace{¿El enlace o token es válido?}
    
    ValidarEnlace -- No --> AlertaEnlaceVencido[Mostrar alerta de enlace expirado o inválido] --> FinEnlaceExpirado([Fin: Solicitar Nuevo Enlace])
    ValidarEnlace -- Sí --> NuevaClave[Ingresar nueva contraseña y confirmación]
    NuevaClave --> ConfirmarCambio[Confirmar actualización exitosa de clave] --> FinSubproceso([Retornar a Inicio de Sesión])
```

---

### **3. Procesos de Búsqueda y Filtrado en el Catálogo (EP-VEC, EP-DDP)**

Se ha dividido la exploración en dos diagramas independientes y cíclicos para permitir búsquedas continuas y ajustes dinámicos de catálogo sin perder el flujo de navegación.

#### **Diagrama 3A: Proceso de Búsqueda de Productos por Palabra Clave**
```mermaid
flowchart TD
    InicioBusqueda([Inicio: Cliente en la Barra de Búsqueda]) --> EscribirTexto[Escribir palabra clave o término de búsqueda]
    EscribirTexto --> ValidarLongitud{¿Tiene al menos 2 caracteres?}

    ValidarLongitud -- No --> IndicarMinimo[Mostrar indicación visual: Requiere mínimo 2 caracteres] --> EscribirTexto

    ValidarLongitud -- Sí --> BuscarProductos[Consultar catálogo por palabras clave]
    BuscarProductos --> HayResultados{¿Se encontraron coincidencias?}

    HayResultados -- No --> MostrarVacio[Mostrar mensaje 'No se encontraron productos' y sugerencias]
    MostrarVacio --> DecisionNuevaBusqueda{¿Desea intentar otra búsqueda?}
    DecisionNuevaBusqueda -- Sí --> EscribirTexto
    DecisionNuevaBusqueda -- No --> FinBusquedaVacia([Fin de Búsqueda / Volver a Portada])

    HayResultados -- Sí --> MostrarListado[Desplegar grilla de productos encontrados y total de resultados]
    MostrarListado --> DecisionAccionBusqueda{¿Qué desea hacer?}
    DecisionAccionBusqueda -- Refinar Búsqueda --> EscribirTexto
    DecisionAccionBusqueda -- Seleccionar Producto --> AbrirFicha[Abrir Ficha Técnica del Producto] --> FinBusquedaExitosa([Ir a Ficha de Producto])
```

#### **Diagrama 3B: Proceso de Navegación y Filtrado Dinámico por Categorías y Marcas**
```mermaid
flowchart TD
    InicioFiltros([Inicio: Cliente en el Catálogo de Productos]) --> ElegirFiltros[Seleccionar opciones en panel lateral: Categoría, Marca, Rango de Precios]
    ElegirFiltros --> CoincidenFiltros{¿Existen productos con esos criterios?}

    CoincidenFiltros -- No --> MostrarMensajeFiltro[Mostrar aviso sin coincidencias y opción 'Limpiar Filtros']
    MostrarMensajeFiltro --> DecisionFiltrosVacio{¿Qué desea hacer?}
    DecisionFiltrosVacio -- Limpiar Filtros --> LimpiarFiltros[Restablecer catálogo al estado inicial] --> ElegirFiltros
    DecisionFiltrosVacio -- Finalizar --> FinFiltrosVacio([Fin de Filtrado])

    CoincidenFiltros -- Sí --> MostrarListadoFiltrado[Actualizar grilla dinámicamente con productos coincidentes]
    MostrarListadoFiltrado --> DecisionAccionFiltros{¿Qué desea hacer?}
    DecisionAccionFiltros -- Ajustar / Combinar Filtros --> ElegirFiltros
    DecisionAccionFiltros -- Limpiar Filtros --> LimpiarFiltros
    DecisionAccionFiltros -- Seleccionar Producto --> AbrirFichaFiltrada[Abrir Ficha Técnica del Producto] --> FinFiltrosExitosa([Ir a Ficha de Producto])
```

---

### **4. Proceso de Historial de Compras y Seguimiento de Envío (EP-SHP)**

Contempla la lectura de pedidos pasados, el seguimiento del paquete con notas de entrega (*tocar timbre, tocar puerta, etc.*) y la reutilización explícita del **Proceso de Selección, Carrito y Compra (Diagrama 1)** para la opción de volver a comprar (*reorder*).

```mermaid
flowchart TD
    InicioHistorial([Inicio: Cliente ingresa a 'Mis Pedidos']) --> ConsultarCompras[Cargar historial de compras del cliente]
    ConsultarCompras --> TieneCompras{¿Tiene compras anteriores?}

    TieneCompras -- No --> MensajeSinCompras[Mostrar 'Aún no has realizado compras' y botón a la tienda] --> FinSinCompras([Fin])

    TieneCompras -- Sí --> DesplegarPedidos[Mostrar lista de pedidos ordenados por fecha]
    DesplegarPedidos --> ElegirAccion{¿Qué desea hacer?}

    %% Ver Tracking de Envío con Notas de Entrega
    ElegirAccion -- Ver Seguimiento del Envío --> ConsultarDespacho[Cargar información del transporte y ruta]
    ConsultarDespacho --> HayIncidencia{¿Hay alguna reprogramación o alerta?}
    
    HayIncidencia -- Sí --> MostrarAlertaEnvio[Mostrar aviso explicativo de incidencia] --> MostrarLineaTiempo
    HayIncidencia -- No --> MostrarLineaTiempo
    
    MostrarLineaTiempo[Desplegar barra de progreso: Registrado ➔ En preparación ➔ En ruta ➔ Entregado]
    MostrarLineaTiempo --> MostrarNotasEnvio[Visualizar notas de entrega e instrucciones de repartidor: Tocar timbre, tocar puerta, observaciones]
    MostrarNotasEnvio --> FinTracking([Fin de Consulta de Tracking])

    %% Volver a Comprar (Reutilizando Diagrama 1)
    ElegirAccion -- Volver a Comprar --> Reordenar[Seleccionar 'Volver a Comprar' en pedido anterior]
    Reordenar --> ValidarStockReorden{¿Hay inventario disponible?}
    
    ValidarStockReorden -- Sí --> SubprocesoCompra[[Reutilizar Proceso de Selección, Carrito y Compra de Productos - Diagrama 1]]
    SubprocesoCompra --> IrAProcesoCompra([Ir al Diagrama 1: Proceso de Compra])
    
    ValidarStockReorden -- No --> AvisarSinStock[Notificar qué productos no tienen stock disponible actualmente] --> FinReorden([Fin de Reordenado])
```

---

### **5. Proceso de Gestión de Lista de Deseos / Favoritos (EP-ITC)**

Detalla cómo el cliente registrado guarda artículos de interés en su espacio personal y los traslada a la bolsa de compras tras validar su disponibilidad.

```mermaid
flowchart TD
    InicioFav([Inicio: Cliente explorando productos]) --> MarcarFavorito[Hacer clic en 'Guardar en Favoritos']
    MarcarFavorito --> ValidarAcceso{¿Tiene sesión iniciada?}

    ValidarAcceso -- No --> SolicitarLogin[Pedir iniciar sesión para guardar en favoritos] --> SubprocesoAccesoFav[[Subproceso: Registro y Acceso a la Cuenta - Diagrama 2]]

    ValidarAcceso -- Sí --> GuardarLista[Guardar producto en la lista personal de favoritos]
    GuardarLista --> VerLista[Cliente ingresa a la sección 'Mis Favoritos']
    VerLista --> ElegirAccionFav{¿Qué desea hacer con el producto?}

    ElegirAccionFav -- Quitar de Favoritos --> EliminarFav[Remover artículo de la lista] --> ListaActualizada([Lista Actualizada])

    ElegirAccionFav -- Mover a la Bolsa de Compras --> MoverABolsa[Presionar 'Mover a la Bolsa']
    MoverABolsa --> ConsultarInventario{¿Hay inventario disponible?}
    ConsultarInventario -- Sí --> TransferirBolsa[Añadir producto a la bolsa de compras] --> IrABolsa([Ir a la Bolsa de Compras - Diagrama 1])
    ConsultarInventario -- No --> NotificarAgotado[Avisar que el producto está agotado actualmente] --> VerLista
```

---

### **6. Proceso de Notificaciones y Comunicaciones de Despacho (EP-SNT)**

Centrado en las notificaciones automáticas en segundo plano enviadas al cliente durante el ciclo de vida del despacho (*En Ruta / Entregado*). El subproceso de confirmación de compra y recomendaciones de catálogo se ha desacoplado para ser ejecutado directamente en el **Diagrama 1**.

```mermaid
flowchart TD
    InicioNotif([Inicio: Ocurre actualización en el Módulo de Despacho]) --> EvaluarEvento{¿Qué tipo de evento ocurrió?}

    %% Actualización de Estado de Envío
    EvaluarEvento -- Paquete en Ruta --> PrepararCorreoRuta[Generar aviso de despacho: 'Tu pedido está en camino']
    PrepararCorreoRuta --> DespacharCorreoRuta[Enviar correo automático con número de seguimiento] --> FinNotif1([Notificación Enviada])

    EvaluarEvento -- Paquete Entregado --> PrepararCorreoEntrega[Generar confirmación de entrega y solicitud de valoración]
    PrepararCorreoEntrega --> DespacharCorreoEntrega[Enviar correo automático de confirmación de recepción] --> FinNotif2([Notificación Enviada])
```

#### **Subproceso: Confirmación y Recomendaciones de Catálogo (Invocado desde Diagrama 1)**
```mermaid
flowchart TD
    InicioConfirmacion([Inicio: Orden Aprobada en Diagrama 1]) --> PrepararCorreoCompra[Generar comprobante digital con número de orden ORD-2026-XXXX]
    PrepararCorreoCompra --> IncluirRecomendados[Agregar bloque con productos recomendados del catálogo]
    IncluirRecomendados --> DespacharCorreoCompra[Enviar correo de confirmación al buzón del cliente] --> FinSubprocesoNotif([Fin del Subproceso])
```

---

### **Resumen de Cobertura y Cambios Estructurales**

| N° Diagrama | Nombre del Proceso | Novedades e Integración |
| :---: | :--- | :--- |
| **1** | Selección, Carrito y Compra | Carrito de compras cíclico, rombo de decisión si no hay stock (regresar a exploración o terminar) y llamada al subproceso de confirmación/recomendaciones. |
| **2** | Registro y Acceso a la Cuenta | Subproceso reutilizable de "Olvidó su clave" enlazado con el formulario de Inicio de Sesión. |
| **3A** | Búsqueda por Palabra Clave | Proceso independiente con validación de longitud (mínimo 2 letras) y bucles para intentar nuevas búsquedas. |
| **3B** | Filtrado Dinámico de Catálogo | Proceso independiente con combinación de filtros laterales, limpieza en un clic y bucles de ajuste. |
| **4** | Historial y Tracking de Envío | Reutilización directa del **Diagrama 1** para la opción *Volver a Comprar* e inclusión de **notas para seguimiento de envío** (tocar puerta, tocar timbre, etc.). |
| **5** | Lista de Deseos / Favoritos | Transferencia de favoritos hacia el carrito de compras previa validación de inventario. |
| **6** | Notificaciones de Despacho | Centrado en notificaciones de envío (*En Ruta / Entregado*). La confirmación de pedido y recomendaciones pasó al Diagrama 1. |
