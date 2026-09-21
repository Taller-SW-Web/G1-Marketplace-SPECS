- **Épica Relacionada:** `EP-GAC` - Gestión de Accesos del Cliente
- **Prioridad:** Media
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 1 - Andrés (Gestión de Accesos / DevOps)
- **Precondiciones:**
    1. El usuario se encuentra en la vista o modal de recuperación de contraseña del Marketplace.
    2. La API del Módulo de Seguridad y Autenticación de Usuarios está disponible para el procesamiento de tokens de recuperación.

- **Descripción Ágil:** **Como** cliente registrado que ha olvidado su contraseña, **quiero** solicitar el restablecimiento y actualizar mi clave mediante un enlace de recuperación, **para** recuperar el acceso a mi cuenta de manera segura.

- **Reglas de Negocio:**
    1. Por motivos de seguridad, la respuesta de la interfaz ante solicitudes de recuperación no revelará explícitamente si un correo existe o no en el sistema.
    2. El enlace o token de recuperación debe contar con un tiempo de caducidad definido antes de ser utilizado.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Solicitud de recuperación con correo registrado**

```
Dado que un usuario está en la vista de recuperación de contraseña,
Y proporciona un correo electrónico registrado en el sistema,
Cuando presiona el botón de restablecer contraseña,
Entonces el sistema procesa el envío de las instrucciones al correo,
Y muestra un mensaje de confirmación neutro.
```

- **Escenario 2: Solicitud con correo no registrado**

```
Dado que un usuario está en la vista de recuperación de contraseña,
Y proporciona un correo electrónico que no existe en el sistema,
Cuando presiona el botón de restablecer contraseña,
Entonces el sistema muestra el mismo mensaje de confirmación neutro,
Y no realiza el envío de instrucciones.
```

- **Escenario 3: Cambio exitoso de contraseña mediante enlace de recuperación**

```
Dado que un usuario ingresa al formulario de restablecimiento mediante un enlace de recuperación válido,
Y proporciona una nueva contraseña que cumple con las políticas de seguridad,
Cuando confirma la actualización de su clave,
Entonces el sistema valida la solicitud y confirma el cambio de contraseña exitosamente,
Y permite al usuario iniciar sesión utilizando su nueva credencial.
```

- **Escenario 4: Intento de cambio con token vencido o inválido**

```
Dado que un usuario intenta acceder al formulario de restablecimiento con un enlace expirado o alterado,
Cuando el sistema procesa la validación del enlace,
Entonces el sistema deniega el acceso al formulario de cambio,
Y muestra una alerta indicando que el enlace ha expirado solicitando generar un nuevo pedido.
```