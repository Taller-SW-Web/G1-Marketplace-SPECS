# Vista — V-001 Inicio de sesión

> Pantalla pública para autenticar a un cliente, resolver un desafío MFA cuando corresponda y regresar de forma segura a la acción que originó el acceso.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-001` |
| Nombre | Inicio de sesión |
| Ruta | `/login` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** acceder a su cuenta con correo y contraseña para continuar navegando o retomar una acción protegida.
- **Actor principal:** cliente registrado sin sesión activa.
- **Permiso:** público; si ya existe una sesión válida, la ruta no debe volver a solicitar credenciales y redirige al destino seguro disponible.
- **Condiciones de entrada:** acceso directo, enlace “Iniciar sesión”, redirección desde una acción que requiere autenticación o regreso desde la pantalla de Seguridad tras verificar el correo.
- **Resultado esperado:** sesión iniciada, carrito anónimo fusionado cuando exista y retorno a la ruta o acción de origen; si no existe origen, navegación a `V-005`.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-002` | [`F-002 Iniciar sesión`](../../funcional/F-002-iniciar-sesion.md) | [`UI F-002`](../F-002-iniciar-sesion.md) | Credenciales, MFA condicional, sesión y retorno. |
| `F-020` | [`F-020 Fusionar carrito`](../../funcional/F-020-fusionar-carrito-anonimo.md) | [`UI F-020`](../F-020-fusionar-carrito-anonimo.md) | Fusión automática y comunicación de ajustes. |

Contratos consultados: [`API F-002`](../../contrato-api/F-002-iniciar-sesion.md) y [`API F-020`](../../contrato-api/F-020-fusionar-carrito-anonimo.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| Cabecera pública | `V-001` | Selección de “Iniciar sesión” | Ruta anterior segura. |
| `O-003` Autenticación requerida | `V-001` | Acción protegida sin sesión | Ruta de origen, intención pendiente y parámetros no sensibles. |
| `V-001` → “Crear cuenta” | `V-002` | Usuario sin cuenta | Retorno seguro, si existe. Nunca contraseña ni errores. |
| `V-001` → “Olvidé mi contraseña” | `V-003` | Recuperación solicitada | Correo sólo si la política de privacidad y seguridad lo permite. |
| Seguridad → `V-001` | Correo verificado correctamente tras un registro con `canalOrigen=MARKETPLACE` | Destino `/login` configurado por Seguridad | Formulario de inicio de sesión; no llega el token de verificación ni una sesión iniciada. |
| Seguridad → `V-001` | Enlace de verificación ya usado; usuario pulsa “Iniciar sesión” en Seguridad | Destino `/login` configurado por Seguridad | El mismo formulario principal, sin token ni sesión transferida; no se afirma un nuevo éxito. |
| Inicio exitoso | Ruta de origen | Existe retorno interno válido | Intención pendiente, filtros y scroll cuando puedan restaurarse. |
| Inicio exitoso | `V-005` | No existe retorno válido | Sesión y carrito autenticado. |

El retorno después de iniciar sesión sólo admite rutas internas permitidas. Nunca se muestra ni se navega a una URL externa recibida como parámetro. El regreso desde Seguridad utiliza el formulario principal y requiere autenticación normal; no se interpreta un parámetro de URL como prueba de cuenta verificada.

## 5. Jerarquía y composición visual

```text
V-001 Inicio de sesión
├── Enlace de retorno o cabecera pública mínima
├── Región de marca
│   └── Logo oficial de Inka Athletics
├── Tarjeta de acceso
│   ├── Título y texto de contexto
│   ├── Alerta global accesible
│   ├── Formulario de credenciales
│   │   ├── Correo electrónico
│   │   ├── Contraseña + mostrar/ocultar
│   │   └── Recuperar contraseña
│   ├── Acción primaria “Iniciar sesión”
│   └── Enlace “Crear cuenta”
└── Región de ayuda y términos aplicables
```

Cuando Seguridad devuelve un desafío MFA, la tarjeta conserva el contexto de acceso y sustituye el formulario de credenciales por el bloque de verificación. MFA nunca se muestra de forma preventiva.

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Marca | Logo principal | Secundaria | No compite con el título ni actúa como única forma de volver. |
| Contexto | Título “Inicia sesión” y explicación breve | Primaria | Si existe retorno, puede explicar de forma genérica que se continuará con la acción solicitada. |
| Formulario | Correo y contraseña | Primaria | Una columna, etiquetas persistentes y errores junto al campo. |
| Ayuda | Recuperación de contraseña | Secundaria | Navega a `V-003`. |
| CTA | “Iniciar sesión” | Primaria | Una sola acción por envío; muestra progreso y queda bloqueada durante la solicitud. |
| Alternativa | “Crear cuenta” | Secundaria | Navega a `V-002` conservando retorno seguro. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Inicia sesión” | — | Siempre. |
| Campo correo | Etiqueta “Correo electrónico” | Capturar identidad | Estado de credenciales. |
| Campo contraseña | Etiqueta “Contraseña” | Capturar secreto | Estado de credenciales. |
| Visibilidad | “Mostrar contraseña” / “Ocultar contraseña” | Alternar presentación sin alterar el valor | Campo contraseña presente. |
| Recuperación | “¿Olvidaste tu contraseña?” | Abrir `V-003` | Estado de credenciales. |
| Acción primaria | “Iniciar sesión” | Enviar una vez | Formulario válido y no ocupado. |
| Registro | “¿Aún no tienes cuenta? Crear cuenta” | Abrir `V-002` | Estado de credenciales. |
| Desafío MFA | Instrucción neutral y campo de código | Verificar segundo factor | Sólo tras desafío válido. |
| Reenvío MFA | Texto con espera y acción “Reenviar código” | Solicitar nuevo código | Sólo si el método permite reenvío. |

Los mensajes no deben revelar si el correo existe, qué credencial falló, tokens, IDs de solicitud ni causas internas.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Principal | Entrada sin desafío | Formulario de correo y contraseña | Completar e iniciar sesión | Sí |
| Validación local | Campo vacío o correo con formato inválido | Mensaje junto al campo y resumen accesible si hay varios errores | Corregir | Sí |
| Autenticando | Envío válido | CTA bloqueado, indicador de progreso y campos no repetibles | Esperar | Sí |
| Credenciales inválidas | Respuesta `401` | Alerta genérica “No pudimos iniciar sesión con esos datos” | Revisar o recuperar contraseña | Sí |
| MFA requerido | Seguridad devuelve desafío | Instrucción, campo de código y acción de verificación | Verificar/reintentar | Sí |
| MFA verificando o inválido | Envío de código o rechazo | Progreso o error neutral junto al código | Corregir/reintentar | Sí |
| Límite temporal | Respuesta `429` | Mensaje de espera sin detalle técnico | Esperar y volver a intentar | Sí |
| Contraseña caducada | Respuesta `403 PASSWORD_CADUCADA` | Explicación y acción definida por Seguridad | Continuar con recuperación/actualización aprobada | Sí |
| Sesión iniciada, sin fusión | Autenticación exitosa y `merged:false` | Confirmación breve accesible | Retornar al origen o inicio | No; documentar como transición |
| Fusionando carrito | Existe carrito anónimo | Mensaje “Actualizando tu carrito” sin bloquear innecesariamente toda la vista | Esperar | Sí |
| Fusión con ajustes | Cantidades o SKU fueron ajustados | `O-007` resume producto y cantidad, sin datos internos | Ver carrito o cerrar | Se diseña en `O-007` |
| Fusión fallida | Fallo antes del commit | Sesión permanece iniciada; mensaje “No pudimos actualizar tu carrito” | Reintentar | Sí |

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-003` | Autenticación requerida con retorno | Antes de llegar a esta vista desde una acción protegida | Continuar a `V-001` o cancelar y permanecer en origen. |
| `O-007` | Resultado de fusión del carrito | Inicio exitoso con ajustes de SKU o cantidades | “Ver carrito” abre `V-008`; “Cerrar” retorna al origen. |
| `O-010` | Alertas y feedback global | Mensajes no asociados a un campo o recuperación temporal | Acción contextual o cierre accesible. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Correo electrónico | Email | Sí | Formato de correo; normalización técnica sin cambiar lo escrito de forma sorpresiva | “Ingresa un correo electrónico válido” | Default/foco/error |
| Contraseña | Password | Sí | No validar localmente reglas de creación ni revelar requisitos de la cuenta | “Ingresa tu contraseña” | Default/foco/error |
| Código MFA | Texto de un solo uso | Condicional | Formato y longitud definidos por Seguridad | Mensaje neutral ante código inválido o vencido | Default/foco/error |

La tecla Enter envía el paso activo cuando es válido. El error de autenticación se asocia al formulario completo y no marca sólo correo o contraseña.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Tarjeta centrada con ancho legible y una sola columna de formulario.
- La marca puede compartir una composición amplia, pero el formulario mantiene prioridad y no depende de una imagen decorativa.
- Los enlaces secundarios permanecen próximos a la acción relacionada.

### Mobile

- **Referencia:** 390 px.
- Contenido en una columna con márgenes del sistema de diseño; sin tarjeta flotante si reduce innecesariamente el espacio.
- CTA a ancho disponible y controles táctiles de al menos el tamaño definido en `DS-001`.
- El teclado no debe ocultar el campo activo, los errores ni el CTA.

### Anchuras intermedias

- Mantener un ancho máximo de formulario y aumentar únicamente el espacio exterior; no convertir el formulario en dos columnas.

## 11. Accesibilidad

- El foco inicial llega al título o al correo según el tipo de navegación, sin saltarse el contexto.
- Las etiquetas permanecen visibles; el placeholder no reemplaza la etiqueta.
- Mostrar/ocultar contraseña anuncia su estado y conserva el foco.
- Los errores de campos usan descripción asociada; la alerta global utiliza `role="alert"` o `aria-live` apropiado.
- Al pasar a MFA, el foco se mueve al título del nuevo paso y se anuncia el cambio.
- Durante el envío se impide la repetición sin retirar inesperadamente el foco.
- Tras el éxito, la navegación anuncia el título del destino; si falla la fusión, la sesión ya iniciada no se presenta como fallida.
- Contraste, foco visible, tamaño táctil y reducción de movimiento siguen `DS-001`.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-001 / Desktop / Principal` | Desktop | Principal | Formulario de credenciales. |
| `V-001 / Mobile / Principal` | Mobile | Principal | Composición móvil y teclado considerado. |
| `V-001 / Desktop / Validación` | Desktop | Validación | Errores locales y foco. |
| `V-001 / Mobile / Credenciales inválidas` | Mobile | Error de autenticación | Alerta genérica y recuperación. |
| `V-001 / Desktop / MFA` | Desktop | MFA requerido | Segundo factor sin formulario de contraseña. |
| `V-001 / Mobile / MFA error` | Mobile | MFA inválido | Mensaje, reintento y reenvío si aplica. |
| `V-001 / Desktop / Fusionando carrito` | Desktop | Progreso posterior al login | Confirmación de sesión y fusión en curso. |
| `V-001 / Mobile / Fusión fallida` | Mobile | Error recuperable | Sesión activa y acción de reintento. |

Los estados de límite temporal y contraseña caducada pueden documentarse como variantes anotadas del frame de error si el layout no cambia; el copy debe quedar visible en la spec o en Figma.

## 13. Criterios de aceptación visual

- [ ] `UI-V001-001`: La vista diferencia claramente credenciales, MFA y fusión del carrito sin presentar los tres pasos al mismo tiempo.
- [ ] `UI-V001-002`: El error de credenciales es genérico y no identifica si falló el correo o la contraseña.
- [ ] `UI-V001-003`: El CTA no puede ejecutarse dos veces mientras la solicitud está en curso.
- [ ] `UI-V001-004`: Un acceso originado por una acción protegida conserva un retorno interno seguro y comprensible.
- [ ] `UI-V001-005`: La falla de fusión no invalida visualmente la sesión ya iniciada y ofrece reintento.
- [ ] `UI-V001-006`: Desktop y mobile incluyen estados de validación, error y MFA con foco y anuncios definidos.
- [ ] `UI-V001-007`: No se muestran tokens, causas técnicas ni datos sensibles en alertas o URLs visibles.
- [ ] `UI-V001-008`: El regreso desde Seguridad, tras verificar o desde un enlace ya usado, muestra el login normal; no crea sesión automáticamente ni recibe el token del correo.
- [ ] La vista utiliza componentes y estilos de `DS-001`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-001-OPEN-01` | Confirmar método, longitud, expiración y reglas de reenvío del MFA con Seguridad. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-001-OPEN-02` | Confirmar el destino aprobado para `PASSWORD_CADUCADA`. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-001-OPEN-03` | Definir el copy exacto y el tiempo comunicado para el estado `429`. | Andrés / Seguridad + UX | Antes del diseño final | Abierta |
