- **Épica Relacionada:** `EP-GAC` - Gestión de Accesos del Cliente
- **Prioridad:** Alta
- **Puntos de Historia (Estimación):** 5 pts
- **Responsable / Rol:** Integrante 1 - Andrés (Gestión de Accesos / DevOps)
- **Precondiciones:**
    1. El usuario se encuentra en el formulario público de registro del Marketplace.
    2. El servicio de la API del Módulo de Seguridad y Autenticación de Usuarios se encuentra disponible o simulado (_mock_).

- **Descripción Ágil:** **Como** visitante del Marketplace, **quiero** registrarme creando una cuenta con mis datos personales, **para** formar parte de la plataforma y realizar compras en el futuro.

- **Reglas de Negocio:**
    1. El correo electrónico proporcionado debe ser único dentro de la plataforma.
    2. Todos los campos obligatorios del formulario deben completarse adecuadamente.

- **Criterios de Aceptación (Sintaxis Gherkin):**

- **Escenario 1: Registro exitoso de un nuevo cliente**

```
Dado que un visitante no registrado está en el formulario de registro,
Y completa todos los campos obligatorios con datos válidos,
Cuando presiona el botón de confirmación de registro,
Entonces el sistema crea la cuenta exitosamente,
Y muestra un mensaje de confirmación invitando a iniciar sesión.
```

- **Escenario 2: Intento de registro con correo ya existente**

```
Dado que un usuario está en el formulario de registro,
Y utiliza un correo electrónico que ya pertenece a una cuenta registrada,
Cuando solicita la creación de la cuenta,
Entonces el sistema deniega el registro,
Y despliega una alerta indicando que el correo ya se encuentra en uso.
```

- **Escenario 3: Campos obligatorios incompletos**

```
Dado que un usuario está en el formulario de registro,
Y omite rellenar uno o más campos obligatorios,
Cuando intenta enviar el formulario,
Entonces el sistema resalta los campos faltantes con un mensaje de error visual,
Y no procesa la solicitud de registro.
```