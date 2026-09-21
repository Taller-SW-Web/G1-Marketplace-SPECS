- **Épica Relacionada:** `EP-TRX` - Transacción y Realización de Checkout
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 5 - Giuliano (UX/UI / Transacción y Checkout)
- **Precondiciones:**
    1. El cliente ha completado la confirmación de la dirección de envío.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** revisar el desglose total e ingresar los datos de mi tarjeta de crédito o débito, **para** simular el pago de mi compra y autorizar la transacción de manera segura.

- **Reglas de Negocio:**
    1. La interfaz exhibirá el desglose transparente del monto final (Subtotal + Costo de envío = Total a pagar).
    2. Antes de procesar el pago, el backend verificará asíncronamente con el Módulo de Productos y Ofertas que el stock siga disponible.
    3. No se almacenarán datos sensibles de tarjetas de crédito en bases de datos locales por motivos de seguridad.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Simulación de pago aprobada exitosamente**

```
Dado que un cliente se encuentra en la etapa de pago con stock confirmado,
Y proporciona datos válidos de una tarjeta de crédito o débito,
Cuando confirma la acción de pago,
Entonces el sistema procesa la simulación exitosamente,
Y procede a la etapa de generación y empaquetado del pedido.
```

- **Escenario 2: Rechazo por alteración de stock de último minuto**

```
Dado que un cliente intenta procesar el pago de su orden,
Pero el stock de uno de sus productos se agotó en el Módulo de Productos mientras completaba sus datos,
Cuando el sistema revalida el inventario previo al cobro,
Entonces detiene la transacción sin realizar cobro alguno,
Y notifica al usuario qué producto ya no cuenta con stock disponible.
```

- **Escenario 3: Rechazo de transacción por datos de tarjeta inválidos**

```
Dado que un cliente ingresa un número de tarjeta, fecha de vencimiento o CVV con formato erróneo,
Cuando intenta procesar la simulación de pago,
Entonces el sistema deniega la transacción,
Y despliega un mensaje indicando que los datos de la tarjeta son incorrectos.
```