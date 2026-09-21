### **Canal Marketplace — Capa de Adaptadores (`axios-mock-adapter` / `@nestjs/axios`)**

---

## **1. Introducción y Matriz de Cobertura Integral**
Este documento consolida la especificación **100% completa y exhaustiva** de contratos simulados (*Mocks*) que consumirá la **Capa de Adaptadores (Capa D)** en NestJS mediante `@nestjs/axios` y `axios-mock-adapter` durante los Hitos 1 a 3 (Semanas 4 a 8).

Garantiza la cobertura absoluta de los escenarios **BDD (Gherkin)**, **Reglas de Negocio (RN-GEN)** y **Requisitos No Funcionales (RNF)** para las **22 Historias de Usuario (83 PH)** distribuidas en las **7 Épicas** del módulo.

---

## **2. Módulo de Seguridad y Usuarios (`EP-GAC`)**
* **Owner de Entidad:** Módulo de Seguridad y Usuarios
* **Rol del Marketplace:** Delegación total de autenticación vía JWT (sin almacenamiento local de contraseñas).

### **2.1. Registro de Cliente (`HU-GAC-REG`)**
* **Endpoint:** `POST /api/v1/auth/register`
* **Headers:** `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "firstName": "Juan",
    "lastName": "Pérez",
    "email": "juan.perez@deportes.com",
    "password": "SecretPassword123",
    "phone": "987654321"
  }
  ```
* **Response `201 Created` (Escenario 1 - Registro exitoso):**
  ```json
  {
    "statusCode": 201,
    "message": "Usuario registrado exitosamente",
    "customerId": "CUST-8842"
  }
  ```
* **Response `409 Conflict` (Escenario 2 - Correo ya existente):**
  ```json
  {
    "statusCode": 409,
    "error": "Conflict",
    "message": "El correo electrónico ya se encuentra registrado en la plataforma"
  }
  ```

### **2.2. Inicio de Sesión (`HU-GAC-SES`)**
* **Endpoint:** `POST /api/v1/auth/login`
* **Headers:** `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "email": "juan.perez@deportes.com",
    "password": "SecretPassword123"
  }
  ```
* **Response `200 OK` (Escenario 1 - Credenciales válidas):**
  ```json
  {
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiJDVVNULTg4NDIiLCJuYW1lIjoiSnVhbiBQw6lyZXoiLCJlbWFpbCI6Imp1YW4ucGVyZXpAZGVwb3J0ZXMuY29tIiwiaWF0IjoxNzI2MTEzNjAwLCJleHAiOjE3MjYxOTcwMDB9.signature",
    "customer": {
      "id": "CUST-8842",
      "name": "Juan Pérez",
      "email": "juan.perez@deportes.com"
    }
  }
  ```
* **Response `401 Unauthorized` (Escenario 2 - Credenciales incorrectas):**
  ```json
  {
    "statusCode": 401,
    "error": "Unauthorized",
    "message": "Credenciales de acceso incorrectas"
  }
  ```

### **2.3. Solicitud de Recuperación de Contraseña (`HU-GAC-REC`)**
* **Endpoint:** `POST /api/v1/auth/recover-password`
* **Headers:** `Content-Type: application/json`
* **Request Body:** `{ "email": "juan.perez@deportes.com" }`
* **Response `200 OK` (Escenario 1 y 2 - Respuesta neutra por RN-GEN-03.2 / RNF-SEC):**
  ```json
  {
    "statusCode": 200,
    "message": "Si el correo se encuentra registrado, se han enviado las instrucciones de restablecimiento."
  }
  ```

### **2.4. Restablecimiento de Contraseña mediante Enlace (`HU-GAC-REC`)**
* **Endpoint:** `POST /api/v1/auth/reset-password`
* **Headers:** `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "token": "recovery-token-uuid-v4",
    "newPassword": "NewSecretPassword123"
  }
  ```
* **Response `200 OK` (Escenario 3 - Cambio exitoso):**
  ```json
  {
    "statusCode": 200,
    "message": "Contraseña actualizada exitosamente."
  }
  ```
* **Response `400 Bad Request` (Escenario 4 - Token expirado o alterado):**
  ```json
  {
    "statusCode": 400,
    "error": "Bad Request",
    "message": "El enlace de recuperación ha expirado o es inválido. Por favor solicite uno nuevo."
  }
  ```

---

## **3. Módulo de Productos y Ofertas (`EP-VEC` / `EP-DDP` / `EP-SNT`)**
* **Owner de Entidad:** Módulo de Productos y Ofertas
* **Rol del Marketplace:** Consulta del catálogo, filtros dinámicos, ficha técnica, cupones y revalidación de stock.

### **3.1. Listado de Categorías del Catálogo (`HU-VEC-HOM`)**
* **Endpoint:** `GET /api/v1/categories`
* **Response `200 OK`:**
  ```json
  [
    { "id": "CAT-1", "nombre": "Calzado deportivo", "slug": "calzado", "icon": "shoe" },
    { "id": "CAT-2", "nombre": "Ropa y Equipación", "slug": "ropa", "icon": "shirt" },
    { "id": "CAT-3", "nombre": "Accesorios y Equipos", "slug": "accesorios", "icon": "dumbbell" }
  ]
  ```

### **3.2. Listado de Marcas Activas (`HU-VEC-FIL`)**
* **Endpoint:** `GET /api/v1/brands`
* **Response `200 OK`:**
  ```json
  [
    { "id": "BRD-1", "nombre": "Nike", "slug": "nike" },
    { "id": "BRD-2", "nombre": "Adidas", "slug": "adidas" },
    { "id": "BRD-3", "nombre": "Puma", "slug": "puma" },
    { "id": "BRD-4", "nombre": "Under Armour", "slug": "under-armour" }
  ]
  ```

### **3.3. Productos Destacados para Home y Correo (`HU-VEC-HOM`, `HU-SNT-TMP`)**
* **Endpoint:** `GET /api/v1/products/featured`
* **Response `200 OK`:**
  ```json
  [
    {
      "codProducto": "PROD-100",
      "nombre": "Zapatillas Running Pro 5",
      "marca": "Nike",
      "precioRegular": 349.90,
      "precioOferta": 299.90,
      "descuentoPorcentaje": 14,
      "imagenUrl": "https://cdn.marketplace.com/prod-100.jpg"
    }
  ]
  ```

### **3.4. Búsqueda y Catálogo Filtrado (`HU-VEC-BUS`, `HU-VEC-FIL`, `HU-VEC-ORD`)**
* **Endpoint:** `GET /api/v1/products`
* **Query Parameters:** `search=zapatillas&category=running&brand=nike&sort=price_asc&page=1&limit=12`
* **Response `200 OK` (Escenario 1 - Coincidencias encontradas):**
  ```json
  {
    "total": 1,
    "page": 1,
    "limit": 12,
    "items": [
      {
        "codProducto": "PROD-100",
        "nombre": "Zapatillas Running Pro 5",
        "marca": "Nike",
        "categoria": "Calzado deportivo",
        "precioRegular": 349.90,
        "precioOferta": 299.90,
        "descuentoPorcentaje": 14,
        "stockTotal": 12,
        "imagenUrl": "https://cdn.marketplace.com/prod-100.jpg"
      }
    ]
  }
  ```
* **Response `200 OK` (Escenario 2 - Sin resultados coincidentes):**
  ```json
  {
    "total": 0,
    "page": 1,
    "limit": 12,
    "items": []
  }
  ```

### **3.5. Detalle y Ficha Técnica (`HU-DDP-FIC`, `HU-DDP-ATR`)**
* **Endpoint:** `GET /api/v1/products/:id`
* **Response `200 OK` (Escenario 1 y 2 - Ficha y ofertas):**
  ```json
  {
    "codProducto": "PROD-100",
    "nombre": "Zapatillas Running Pro 5",
    "descripcion": "Calzado de alto rendimiento para maratones y entrenamiento diario.",
    "marca": "Nike",
    "precioRegular": 349.90,
    "precioOferta": 299.90,
    "descuentoPorcentaje": 14,
    "imagenes": [
      "https://cdn.marketplace.com/prod-100-front.jpg",
      "https://cdn.marketplace.com/prod-100-side.jpg"
    ],
    "atributos": [
      { "nombre": "Talla", "opciones": ["39", "40", "41", "42"] },
      { "nombre": "Color", "opciones": ["Negro/Azul", "Blanco/Rojo"] }
    ]
  }
  ```
* **Response `404 Not Found` (Escenario 3 - Producto no disponible o inexistente):**
  ```json
  {
    "statusCode": 404,
    "error": "Not Found",
    "message": "El producto solicitado no existe o se encuentra descontinuado"
  }
  ```

### **3.6. Revalidación de Stock Positivo y Pre-Pago (`HU-DDP-STK`, `HU-TRX-PAG`, `RN-GEN-02.2`)**
* **Endpoint:** `GET /api/v1/products/:id/stock`
* **Response `200 OK` (Stock Disponible):**
  ```json
  {
    "codProducto": "PROD-100",
    "availableStock": 12,
    "isAvailable": true
  }
  ```
* **Response `200 OK` (Agotado - Stock = 0):**
  ```json
  {
    "codProducto": "PROD-100",
    "availableStock": 0,
    "isAvailable": false
  }
  ```

### **3.7. Validación de Cupones y Promociones en Tiempo Real (`RN-GEN-02.4`)**
* **Endpoint:** `POST /api/v1/coupons/validate`
* **Headers:** `Content-Type: application/json`
* **Request Body:** `{ "couponCode": "VERANO2026", "cartTotal": 299.90 }`
* **Response `200 OK` (Cupón Válido):**
  ```json
  {
    "isValid": true,
    "couponCode": "VERANO2026",
    "discountType": "PERCENTAGE",
    "discountValue": 10.0,
    "discountAmount": 29.99,
    "message": "Cupón aplicado exitosamente (10% de descuento)."
  }
  ```
* **Response `400 Bad Request` (Cupón Expirado o Inválido):**
  ```json
  {
    "statusCode": 400,
    "error": "Bad Request",
    "message": "El cupón ingresado es inválido o se encuentra vencido."
  }
  ```

### **3.8. Disparo de Consumo de Inventario (`RN-GEN-02.5`)**
* **Endpoint:** `POST /api/v1/products/discount-stock`
* **Headers:** `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "orderId": "ORD-2026-9941",
    "items": [
      { "productId": "PROD-100", "quantity": 1 }
    ]
  }
  ```
* **Response `200 OK`:**
  ```json
  {
    "statusCode": 200,
    "message": "Inventario actualizado satisfactoriamente."
  }
  ```

### **3.9. Productos Relacionados y Sugeridos (`HU-DDP-REL`)**
* **Endpoint:** `GET /api/v1/products/:id/related`
* **Response `200 OK`:** Devuelve lista de productos complementarios de la misma categoría/marca.

---

## **4. Módulo de Ventas y Postventa (`EP-TRX` / `EP-SHP`)**
* **Owner de Entidad:** Módulo de Ventas y Postventa
* **Rol del Marketplace:** Empaquetado y transmisión del pedido tras el pago; visor de historial "Mis Pedidos".

### **4.1. Generación y Registro de Pedido (`HU-TRX-ORD`)**
* **Endpoint:** `POST /api/v1/orders`
* **Headers:** `Authorization: Bearer <JWT_TOKEN>`, `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "customerId": "CUST-8842",
    "items": [
      { "productId": "PROD-100", "quantity": 1, "unitPrice": 299.90 }
    ],
    "shippingAddress": {
      "street": "Av. Principal 123, Dpto 402",
      "city": "Lima",
      "district": "Miraflores",
      "phone": "987654321"
    },
    "paymentSummary": {
      "subtotal": 299.90,
      "shippingCost": 15.00,
      "discount": 29.99,
      "totalPaid": 284.91,
      "paymentMethod": "CARD_SIMULATION"
    }
  }
  ```
* **Response `201 Created` (Escenario 1 - Registro exitoso):**
  ```json
  {
    "orderId": "ORD-2026-9941",
    "status": "REGISTERED",
    "createdAt": "2026-09-11T22:00:00Z",
    "message": "Pedido registrado exitosamente en el Módulo de Ventas"
  }
  ```
* **Response `503 Service Unavailable` (Escenario 2 - Interrupción en API de Ventas):**
  ```json
  {
    "statusCode": 503,
    "error": "Service Unavailable",
    "message": "Servicio de Ventas temporalmente no disponible. La orden se encuentra en proceso de verificación."
  }
  ```

### **4.2. Historial de Pedidos (`HU-SHP-HIS`)**
* **Endpoint:** `GET /api/v1/orders/customer/:customerId`
* **Query Parameters:** `status=IN_PROCESS` (Opcional)
* **Response `200 OK` (Escenario 1 y 2 - Con compras y filtrado):**
  ```json
  [
    {
      "orderId": "ORD-2026-9941",
      "date": "2026-09-11T22:00:00Z",
      "totalItems": 1,
      "totalAmount": 284.91,
      "status": "IN_PROCESS"
    }
  ]
  ```
* **Response `200 OK` (Escenario 3 - Sin compras registradas):**
  ```json
  []
  ```

### **4.3. Detalle de Pedido Específico y Reorder (`HU-SHP-DET`)**
* **Endpoint:** `GET /api/v1/orders/:orderId`
* **Response `200 OK`:** Desglose completo de productos, imágenes, precios, dirección de entrega y resumen de costos.

---

## **5. Módulo de Despacho y Entrega a Domicilio (`EP-SHP`)**
* **Owner de Entidad:** Módulo de Despacho y Entrega
* **Rol del Marketplace:** Consulta del estado de envío para la barra de seguimiento en ruta.

### **5.1. Seguimiento del Paquete en Ruta (`HU-SHP-TRK`)**
* **Endpoint:** `GET /api/v1/dispatch/order/:orderId`
* **Response `200 OK` (Escenario 1 - Flujo normal en ruta):**
  ```json
  {
    "orderId": "ORD-2026-9941",
    "trackingStep": "IN_TRANSIT",
    "allowedSteps": ["REGISTERED", "PREPARING", "IN_TRANSIT", "DELIVERED"],
    "estimatedDelivery": "2026-09-14T18:00:00Z",
    "carrier": "Courier Deportivo Express",
    "incident": null
  }
  ```
* **Response `200 OK` (Escenario 2 - Incidencia o reprogramación de entrega):**
  ```json
  {
    "orderId": "ORD-2026-9941",
    "trackingStep": "IN_TRANSIT",
    "allowedSteps": ["REGISTERED", "PREPARING", "IN_TRANSIT", "DELIVERED"],
    "estimatedDelivery": "2026-09-15T18:00:00Z",
    "carrier": "Courier Deportivo Express",
    "incident": {
      "type": "RESCHEDULED",
      "message": "Entrega reprogramada por dirección con acceso restringido. Nuevo intento coordinado.",
      "updatedAt": "2026-09-12T10:30:00Z"
    }
  }
  ```

---

## **6. Servicio Externo de Correo SaaS (`EP-SNT` / Resend API)**
* **Proveedor SaaS:** Resend (`https://api.resend.com`)
* **Rol del Marketplace:** Disparo asíncrono en segundo plano tras evento `order.created` o cambio de estado en despacho (`HU-SNT-EML`, `HU-SNT-DES`).

### **6.1. Despacho de Correo Transaccional (`HU-SNT-EML`, `HU-SNT-DES`)**
* **Endpoint:** `POST https://api.resend.com/emails`
* **Headers:** `Authorization: Bearer re_123456789`, `Content-Type: application/json`
* **Request Body:**
  ```json
  {
    "from": "Canal Marketplace <pedidos@deportes.com>",
    "to": ["juan.perez@deportes.com"],
    "subject": "Confirmación de Pedido #ORD-2026-9941",
    "html": "<html>...Plantilla HTML compilada desde React Email...</html>"
  }
  ```
* **Response `200 OK`:**
  ```json
  {
    "id": "email_9981a7b2-3c41-4122-b2d9-129482910281"
  }
  ```
