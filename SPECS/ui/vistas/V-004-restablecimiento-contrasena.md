# Vista — V-004 Restablecimiento de contraseña

> Pantalla pública abierta desde un enlace de recuperación para definir una contraseña nueva con un token de un solo uso.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-004` |
| Nombre | Restablecimiento de contraseña |
| Ruta | `/restablecer-contrasena` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

El token puede llegar como parámetro opaco requerido por Seguridad, pero no forma parte del nombre visible de la vista, no se muestra y no se persiste en almacenamiento del Marketplace.

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** reemplazar su contraseña mediante un enlace válido de recuperación.
- **Actor principal:** persona que recibió el enlace administrado por Seguridad.
- **Permiso:** público condicionado a token válido, vigente y no utilizado.
- **Condición de entrada:** enlace recibido tras `V-003`.
- **Resultado esperado:** contraseña actualizada, sesiones anteriores revocadas según Seguridad e invitación a iniciar sesión; no se crea una sesión automática.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-005` | [`F-005 Restablecer contraseña`](../../funcional/F-005-restablecer-password.md) | [`UI F-005`](../F-005-restablecer-password.md) | Token de un solo uso, contraseña nueva, política, errores y salida. |

Contrato consultado: [`API F-005`](../../contrato-api/F-005-restablecer-password.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto conservado |
|---|---|---|---|
| Enlace de recuperación | `V-004` | Token presente | Token sólo en memoria el tiempo mínimo necesario. |
| “Solicitar otro enlace” | `V-003` | Token ausente, inválido, vencido o utilizado | Ningún token; correo sólo si la política lo permite. |
| “Iniciar sesión” | `V-001` | Contraseña actualizada | Retorno seguro; nunca contraseña ni token. |
| “Volver al inicio” | `V-005` | Usuario abandona el flujo | Ningún dato secreto. |

Recargar o volver atrás no debe reutilizar un token ya consumido ni reponer los campos de contraseña.

## 5. Jerarquía y composición visual

```text
V-004 Restablecimiento de contraseña
├── Marca o cabecera pública mínima
├── Estado del enlace
│   ├── Validando
│   └── Inválido/vencido, cuando corresponda
├── Tarjeta de nueva contraseña
│   ├── Título e instrucción
│   ├── Nueva contraseña + mostrar/ocultar
│   ├── Confirmación + mostrar/ocultar
│   ├── Política vigente
│   └── Acción “Guardar nueva contraseña”
└── Resultado
    ├── Contraseña actualizada
    └── Acción “Iniciar sesión”
```

El formulario sólo se muestra cuando el flujo puede procesar el token. Un enlace inválido o vencido presenta una salida clara hacia `V-003`, no campos deshabilitados que sugieran que aún puede funcionar.

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Visibilidad |
|---|---|---|---|
| Título | “Crea una nueva contraseña” | — | Token procesable. |
| Contraseña | “Nueva contraseña” | Capturar secreto | Formulario. |
| Confirmación | “Confirma tu contraseña” | Confirmar coincidencia | Formulario. |
| Política | Requisitos vigentes | Informar cumplimiento | Formulario. |
| CTA | “Guardar nueva contraseña” | Enviar una vez | Formulario válido y no ocupado. |
| Enlace inválido | “Este enlace no es válido o ya fue utilizado” | Informar sin revelar cuenta | Respuesta `401`. |
| Enlace vencido | “Este enlace venció” | Informar caducidad | Respuesta `410`. |
| Nueva solicitud | “Solicitar otro enlace” | Abrir `V-003` | Enlace no utilizable. |
| Confirmación | “Tu contraseña fue actualizada” | Informar éxito | Respuesta `204`. |
| Acceso | “Iniciar sesión” | Abrir `V-001` | Éxito. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Validando enlace | Entrada con token | Progreso neutral; no se muestran campos todavía | Esperar | Sí |
| Formulario principal | Token procesable | Dos campos y política | Completar | Sí |
| Validación local | Vacíos, no coincidencia o reglas visibles incumplidas | Errores asociados y requisitos | Corregir | Sí |
| Guardando | Envío válido | CTA bloqueado; campos no repetibles | Esperar | Sí |
| Política rechazada | Respuesta `422` | Requisitos externos incumplidos; token sigue sujeto a validez | Corregir y reenviar | Sí |
| Token inválido o usado | Respuesta `401` o ausencia inválida | No se muestra formulario; explicación neutral | Solicitar otro enlace | Sí |
| Token vencido | Respuesta `410` | No se muestra formulario; caducidad y salida | Solicitar otro enlace | Sí |
| Error recuperable | Fallo temporal sin consumir token confirmado | Mensaje general | Reintentar de forma segura | Sí |
| Contraseña actualizada | Respuesta `204` | Confirmación y acción a login | Iniciar sesión | Sí |

Éxito, token inválido y token vencido son estados finales visualmente distintos. El éxito no entrega ni promete una sesión activa.

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Continuación |
|---|---|---|---|
| `O-010` | Alertas y feedback global | Fallo temporal fuera de los campos | Reintentar o salir. |

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje | Estado visual |
|---|---|---:|---|---|---|
| Nueva contraseña | Password | Sí | Política vigente de Seguridad | Lista de requisitos accesible | Default/foco/error/éxito parcial |
| Confirmación | Password | Sí | Coincidir con la nueva contraseña | “Las contraseñas deben coincidir” | Default/foco/error |

El token no es un campo visible ni editable. Mostrar/ocultar funciona por campo, conserva el valor y anuncia su estado.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Tarjeta de una columna con ancho legible; política próxima a la nueva contraseña.
- Estados finales usan la misma región central para mantener continuidad.

### Mobile

- **Referencia:** 390 px.
- Campos, política y CTA apilados.
- El teclado no oculta errores, requisitos ni acción.
- Los estados de enlace inválido/vencido ofrecen una acción primaria visible sin desplazamiento excesivo.

### Anchuras intermedias

- Mantener el formulario en una sola columna y variar sólo su ancho máximo y espacio exterior.

## 11. Accesibilidad

- El estado de validación del enlace se anuncia sin repetir mensajes continuamente.
- Al mostrarse el formulario, el foco llega al título; al fallar, al error final o primer campo inválido.
- Requisitos de contraseña expresados con texto e iconos, no sólo color.
- Los controles de visibilidad tienen nombre y estado accesibles.
- Al actualizarse la contraseña, el foco llega al título de confirmación.
- El historial del navegador no debe exponer el token en títulos, analítica o mensajes visibles.
- Contraste, foco y tamaños táctiles siguen `DS-001`.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-004 / Desktop / Validando enlace` | Desktop | Progreso | Estado previo al formulario. |
| `V-004 / Mobile / Principal` | Mobile | Formulario | Campos apilados y política. |
| `V-004 / Desktop / Principal` | Desktop | Formulario | Composición central. |
| `V-004 / Mobile / Validación` | Mobile | Error local | Coincidencia y requisitos. |
| `V-004 / Desktop / Política rechazada` | Desktop | Error `422` | Reglas externas. |
| `V-004 / Mobile / Enlace inválido` | Mobile | Error final | Nueva solicitud. |
| `V-004 / Desktop / Enlace vencido` | Desktop | Error final | Caducidad diferenciada. |
| `V-004 / Mobile / Actualizada` | Mobile | Éxito | Login como siguiente acción. |

El error recuperable puede documentarse como variante anotada de “Política rechazada” sólo si conserva el layout y diferencia claramente su acción.

## 13. Criterios de aceptación visual

- [ ] `UI-V004-001`: El token nunca aparece como contenido, campo, mensaje o dato copiable.
- [ ] `UI-V004-002`: La vista distingue política incumplida, enlace inválido y enlace vencido sin revelar información de cuenta.
- [ ] `UI-V004-003`: Un token no utilizable no muestra el formulario de contraseña.
- [ ] `UI-V004-004`: El envío es único mientras está en progreso y el éxito no inicia sesión automáticamente.
- [ ] `UI-V004-005`: Todos los estados finales ofrecen una salida segura hacia recuperación, login o inicio.
- [ ] `UI-V004-006`: Desktop y mobile mantienen requisitos, errores y foco accesibles.
- [ ] La vista aplica `DS-001`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-004-OPEN-01` | Incorporar la política exacta y vigente de contraseña publicada por Seguridad. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-004-OPEN-02` | Confirmar si Seguridad permite validar el token antes del envío o sólo al intentar restablecer. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-004-OPEN-03` | Definir el texto aprobado sobre revocación de sesiones anteriores. | Andrés / Seguridad + UX | Antes del diseño final | Abierta |
