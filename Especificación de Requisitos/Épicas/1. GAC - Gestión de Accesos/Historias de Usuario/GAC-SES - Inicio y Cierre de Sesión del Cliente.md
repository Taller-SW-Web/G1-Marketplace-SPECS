- **Épica Relacionada:** `EP-GAC` - Gestión de Accesos del Cliente
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 3 pts
- **Responsable / Rol:** Integrante 1 - Andrés (Gestión de Accesos / DevOps)
- **Precondiciones:**
    1. El usuario posee una cuenta de cliente previamente registrada.
    2. El usuario se encuentra en la vista de inicio de sesión o cuenta con una sesión activa en el Marketplace.

- **Descripción Ágil:** **Como** cliente registrado del Marketplace, **quiero** iniciar y cerrar sesión con mis credenciales de acceso, **para** acceder a mi espacio personal de forma segura y proteger mi cuenta cuando termine de usar la plataforma.

- **Reglas de Negocio:**
    1. El inicio de sesión correcto habilita las funciones personalizadas del cliente (favoritos, historial de compras, checkout).
    2. El cierre de sesión invalida e inhabilita inmediatamente la sesión activa en el navegador.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Inicio de sesión exitoso**

```
Dado que un cliente registrado está en el formulario de inicio de sesión,
Y proporciona un correo/usuario y contraseña válidos,
Cuando solicita iniciar sesión,
Entonces el sistema valida las credenciales exitosamente,
Y le concede acceso a su cuenta habilitando las funciones autenticadas.
```

- **Escenario 2: Ingreso de credenciales incorrectas**

```
Dado que un cliente está en el formulario de inicio de sesión,
Y proporciona un usuario o contraseña inválidos,
Cuando intenta iniciar sesión,
Entonces el sistema deniega el acceso,
Y despliega una alerta de error genérica sin revelar el campo fallido.
```

- **Escenario 3: Cierre de sesión voluntario**

```
Dado que un cliente se encuentra autenticado con una sesión activa,
Cuando selecciona la opción "Cerrar Sesión",
Entonces el sistema invalida la sesión activa,
Y lo redirige a la vista pública del Marketplace.
```