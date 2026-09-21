- **Épica Relacionada:** `EP-TRX` - Transacción y Realización de Checkout
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 5 - Giuliano (UX/UI / Transacción y Checkout)
- **Precondiciones:**
    1. El cliente cuenta con al menos un producto en su carrito de compras.
    2. El cliente ha iniciado sesión con su cuenta registrada en la plataforma.

- **Descripción Ágil:** **Como** cliente del Marketplace, **quiero** ingresar y confirmar mi dirección y datos de contacto para la entrega, **para** especificar el destino donde deseo recibir mis productos deportivos.

- **Reglas de Negocio:**
    1. Todos los campos de dirección (calle/avenida, departamento, provincia, distrito y teléfono de contacto) son obligatorios.
    2. La interfaz permite seleccionar direcciones previamente guardadas o ingresar una nueva dirección de envío.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Captura exitosa de la dirección de envío**

```
Dado que un cliente autenticado se encuentra en el primer paso del checkout,
Y completa todos los campos obligatorios de dirección de entrega con datos válidos,
Cuando presiona el botón "Continuar al Pago",
Entonces el sistema valida la información de envío,
Y habilita el siguiente paso del formulario correspondiente a la revisión y pago.
```

- **Escenario 2: Intento de avanzar con datos de envío incompletos**

```
Dado que un cliente se encuentra en la etapa de dirección de envío,
Y omite completar uno o más campos obligatorios,
Cuando intenta presionar "Continuar al Pago",
Entonces el sistema bloquea el avance,
Y resalta visualmente los campos faltantes requiriendo su atención.
```