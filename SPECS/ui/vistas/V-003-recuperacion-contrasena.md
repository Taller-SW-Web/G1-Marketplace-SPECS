# Vista — V-003 Recuperación de contraseña

> Pantalla pública para solicitar instrucciones de recuperación sin revelar si el correo pertenece a una cuenta.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-003` |
| Nombre | Recuperación de contraseña |
| Ruta | `/recuperar-contrasena` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** solicitar instrucciones para recuperar el acceso a su cuenta.
- **Actor principal:** visitante que no puede iniciar sesión.
- **Permiso:** público.
- **Condición de entrada:** acceso desde `V-001` o URL directa.
- **Resultado esperado:** confirmación pública uniforme; la existencia de la cuenta nunca se confirma.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-004` | [`F-004 Solicitar recuperación`](../../funcional/F-004-solicitar-recuperacion-password.md) | [`UI F-004`](../F-004-solicitar-recuperacion-password.md) | Captura de correo, respuesta uniforme y límite de solicitudes. |

Contrato consultado: [`API F-004`](../../contrato-api/F-004-solicitar-recuperacion-password.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto conservado |
|---|---|---|---|
| `V-001` → “¿Olvidaste tu contraseña?” | `V-003` | Recuperación solicitada | Correo sólo si la política aprobada permite precarga. |
| “Volver a iniciar sesión” | `V-001` | Antes o después de solicitar | Retorno interno seguro, si existía. |
| Enlace recibido por correo | `V-004` | Token válido administrado por Seguridad | Sólo parámetros opacos requeridos; nunca se presentan completos. |
| “Intentar nuevamente” | `V-003` | Usuario decide enviar otra solicitud permitida | Correo conservado, contraseña inexistente. |

## 5. Jerarquía y composición visual

```text
V-003 Recuperación de contraseña
├── Marca o cabecera pública mínima
├── Tarjeta de recuperación
│   ├── Título
│   ├── Explicación de respuesta neutral
│   ├── Campo correo electrónico
│   ├── Acción “Enviar instrucciones”
│   └── Enlace “Volver a iniciar sesión”
└── Región de ayuda
```

Después de una respuesta `202`, la tarjeta cambia a confirmación neutral. No muestra ilustraciones, etiquetas ni acciones que permitan deducir si se envió realmente un correo.

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Visibilidad |
|---|---|---|---|
| Título | “Recupera tu contraseña” | — | Formulario. |
| Explicación | “Ingresa tu correo y te indicaremos los siguientes pasos.” | — | Formulario. |
| Campo | “Correo electrónico” | Capturar correo | Formulario. |
| CTA | “Enviar instrucciones” | Solicitar recuperación una vez | Formulario válido y no ocupado. |
| Confirmación | “Si el correo es válido, recibirás instrucciones para continuar.” | Informar resultado uniforme | Respuesta `202`. |
| Ayuda | “Revisa también la carpeta de correo no deseado.” | Orientar sin confirmar envío | Confirmación. |
| Retorno | “Volver a iniciar sesión” | Abrir `V-001` | Siempre. |

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Principal | Entrada | Formulario de correo | Completar | Sí |
| Validación local | Vacío o formato inválido | Error asociado al campo | Corregir | Sí |
| Enviando | Solicitud válida | CTA bloqueado y progreso | Esperar | Sí |
| Confirmación uniforme | Respuesta `202`, exista o no la cuenta | Mensaje neutral y retorno a login | Revisar correo o volver | Sí |
| Límite temporal | Respuesta `429` | Espera neutral; correo permanece | Esperar/reintentar | Sí |
| Error recuperable | Fallo distinto a límite | Mensaje general | Reintentar | Sí |

La duración visual y el contenido del resultado no deben variar según la existencia de la cuenta.

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Continuación |
|---|---|---|---|
| `O-010` | Alertas y feedback global | Error temporal no asociado al campo | Reintentar o cerrar. |

El correo de recuperación pertenece al módulo de Seguridad y no corresponde a las comunicaciones comerciales `C-001` o `C-002`.

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla | Mensaje | Estado visual |
|---|---|---:|---|---|---|
| Correo electrónico | Email | Sí | Formato válido | “Ingresa un correo electrónico válido” | Default/foco/error |

El botón puede habilitarse cuando el formato local es válido. La validación local no implica que el correo esté registrado.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Tarjeta centrada de una columna y ancho legible.
- La confirmación mantiene dimensiones semejantes al formulario para evitar saltos innecesarios.

### Mobile

- **Referencia:** 390 px.
- Contenido apilado con CTA a ancho disponible.
- El teclado no oculta el error ni la acción.
- La explicación y confirmación evitan líneas excesivamente largas.

### Anchuras intermedias

- Mantener ancho máximo del formulario y variar el espacio exterior, sin crear columnas.

## 11. Accesibilidad

- Título enfocable como destino de navegación y etiqueta persistente para el correo.
- El error se asocia al campo y el resumen de confirmación recibe foco tras la respuesta.
- El progreso impide reenvíos repetidos sin borrar el valor.
- El límite temporal se comunica con texto; no depender de un contador animado.
- La confirmación `202` usa el mismo anuncio exista o no la cuenta.
- Contraste, foco visible y tamaño táctil siguen `DS-001`.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-003 / Desktop / Principal` | Desktop | Principal | Formulario y retorno. |
| `V-003 / Mobile / Principal` | Mobile | Principal | Composición apilada. |
| `V-003 / Desktop / Validación` | Desktop | Error local | Campo inválido. |
| `V-003 / Mobile / Enviando` | Mobile | Progreso | CTA bloqueado. |
| `V-003 / Desktop / Confirmación uniforme` | Desktop | Éxito público | Mensaje neutral. |
| `V-003 / Mobile / Límite temporal` | Mobile | `429` | Correo conservado y espera. |

El error recuperable puede anotarse como variante del frame de límite cuando no altera la estructura, manteniendo copy y acción diferentes.

## 13. Criterios de aceptación visual

- [ ] `UI-V003-001`: La confirmación es idéntica para correos existentes y no existentes.
- [ ] `UI-V003-002`: La vista conserva el correo ante límite temporal y no expone información de cuenta.
- [ ] `UI-V003-003`: El CTA no puede repetirse durante el envío.
- [ ] `UI-V003-004`: Desktop y mobile permiten volver a `V-001` en todos los estados.
- [ ] `UI-V003-005`: Foco, errores y anuncios dinámicos están definidos.
- [ ] La vista aplica `DS-001`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-003-OPEN-01` | Confirmar si el correo puede precargarse desde `V-001` sin afectar la política de privacidad. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-003-OPEN-02` | Definir el tiempo o copy permitido para el límite `429`. | Andrés / Seguridad + UX | Antes del diseño final | Abierta |
