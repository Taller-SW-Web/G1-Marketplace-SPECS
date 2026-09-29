# Vista — V-002 Registro

> Pantalla pública para solicitar la creación de una cuenta de cliente y explicar el paso de verificación por correo antes de iniciar sesión.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID | `V-002` |
| Nombre | Registro de cliente |
| Ruta | `/registro` |
| Versión | `0.1.0` |
| Estado | En revisión |
| Responsable | Giuliano Macchiavello |
| Revisor | Jim Segovia |
| Sistema de diseño | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) |
| Enlace de Figma | Pendiente |

## 2. Propósito, actor y acceso

- **Objetivo del usuario:** solicitar una cuenta con sus datos básicos para posteriormente verificar su correo e iniciar sesión.
- **Actor principal:** visitante sin sesión.
- **Permiso:** público; una sesión activa redirige a un destino seguro y evita registrar otra cuenta por error.
- **Condiciones de entrada:** acceso directo o enlace “Crear cuenta” desde `V-001`.
- **Resultado esperado:** solicitud enviada una sola vez, explicación de verificación por correo y acceso a `V-001`; el registro no inicia sesión automáticamente.

## 3. Trazabilidad

| Funcionalidad | Spec funcional | Spec UI de origen | Aporte a esta vista |
|---|---|---|---|
| `F-001` | [`F-001 Registrar cliente`](../../funcional/F-001-registrar-cliente.md) | [`UI F-001`](../F-001-registrar-cliente.md) | Formulario, términos, política de contraseña y resultado del registro. |

Contrato consultado: [`API F-001`](../../contrato-api/F-001-registrar-cliente.md).

## 4. Entradas, salidas y conservación de contexto

| Origen o acción | Destino | Condición | Contexto que se conserva |
|---|---|---|---|
| Acceso directo | `V-002` | Visitante sin sesión | Ninguno. |
| `V-001` → “Crear cuenta” | `V-002` | Visitante decide registrarse | Retorno interno seguro, si existía. |
| “Ya tengo una cuenta” | `V-001` | Usuario decide iniciar sesión | Retorno interno seguro; nunca la contraseña. |
| Registro aceptado → “Ir a iniciar sesión” | `V-001` | Usuario comprende que debe verificar su correo | Correo sólo si Seguridad permite precargarlo; retorno seguro. |

La vista no debe conservar la contraseña al navegar, recargar o volver desde otra ruta.

## 5. Jerarquía y composición visual

```text
V-002 Registro
├── Cabecera pública mínima o retorno a login
├── Región de marca
├── Encabezado
│   ├── Título “Crea tu cuenta”
│   └── Explicación breve
├── Formulario
│   ├── Nombres
│   ├── Apellidos
│   ├── Correo electrónico
│   ├── Celular
│   ├── Contraseña + mostrar/ocultar
│   ├── Confirmación de contraseña + mostrar/ocultar
│   ├── Política/medidor de contraseña
│   └── Aceptación de términos
├── Acción “Crear cuenta”
└── Enlace “Ya tengo una cuenta”
```

| Región | Componente o contenido | Prioridad | Comportamiento |
|---|---|---|---|
| Introducción | Título y propósito | Primaria | Aclara que habrá verificación por correo. |
| Identidad | Nombres y apellidos | Primaria | Campos separados y de ancho suficiente. |
| Contacto | Correo y celular | Primaria | Ayuda de formato sin anticipar si ya existe cuenta. |
| Seguridad | Contraseña, confirmación y política | Primaria | Reglas visibles antes del envío; validación final pertenece a Seguridad. |
| Consentimiento | Casilla y enlaces de términos/privacidad | Primaria | No viene seleccionada y debe poder operarse por teclado. |
| Acciones | Crear cuenta / iniciar sesión | Primaria/Secundaria | CTA único durante el envío. |

## 6. Contenido y acciones

| Elemento | Texto o dato | Acción | Condición de visibilidad |
|---|---|---|---|
| Título | “Crea tu cuenta” | — | Estado de formulario. |
| Introducción | “Compra, guarda favoritos y consulta tus pedidos.” | — | Estado de formulario. |
| Campos | Nombres, apellidos, correo, celular, contraseña y confirmación | Capturar datos | Estado de formulario. |
| Política | Requisitos vigentes de contraseña | Informar cumplimiento | Al enfocar o editar contraseña; puede permanecer visible. |
| Términos | “Acepto los términos y la política de privacidad” | Marcar consentimiento y abrir documentos | Estado de formulario. |
| CTA | “Crear cuenta” | Enviar solicitud | Formulario válido y no ocupado. |
| Alternativa | “Ya tengo una cuenta. Iniciar sesión” | Abrir `V-001` | Estado de formulario. |
| Confirmación | “Revisa tu correo para verificar tu cuenta” | Informar siguiente paso | Solicitud aceptada. |

`canalOrigen=MARKETPLACE` es un dato técnico fijo: no se presenta ni se permite editar.

## 7. Estados de la vista

| Estado | Disparador | Cambios visibles | Acción o recuperación | Frame requerido |
|---|---|---|---|---|
| Principal | Entrada pública | Formulario vacío y política disponible | Completar | Sí |
| En progreso | Usuario completó parte del formulario | Valores y validaciones no intrusivas | Continuar | No; documentar en principal |
| Validación local | Campos obligatorios, formatos, coincidencia o términos inválidos | Errores junto a campos y resumen si hay varios | Corregir | Sí |
| Política visible | Contraseña en edición | Lista de requisitos con estado textual e iconográfico | Cumplir requisitos | Sí |
| Enviando | Formulario válido enviado | CTA bloqueado y progreso | Esperar | Sí |
| Correo no disponible | Respuesta `409` | Mensaje neutral que no confirma una cuenta existente | Usar otro correo, iniciar sesión o recuperar acceso | Sí |
| Política rechazada | Respuesta `422` | Reglas incumplidas marcadas sin borrar los demás campos | Corregir contraseña | Sí |
| Error recuperable | Servicio temporalmente no disponible | Mensaje general; datos no sensibles permanecen | Reintentar | Sí |
| Solicitud aceptada | Respuesta `201/202` | Confirmación, correo parcialmente oculto si se muestra y siguiente paso | Abrir correo o ir a login | Sí |

El estado de éxito no afirma que la cuenta esté activa ni que la sesión haya comenzado.

## 8. Overlays y comunicaciones asociadas

| ID | Elemento | Cuándo aparece | Cómo se cierra o continúa |
|---|---|---|---|
| `O-010` | Alertas y feedback global | Error del servicio o aviso que no pertenece a un campo | Reintentar o cerrar con foco controlado. |

La verificación de cuenta enviada por Seguridad no forma parte de `C-001` o `C-002`; esos IDs están reservados para pedidos y despacho.

## 9. Formularios y validación visual

| Campo | Tipo | Obligatorio | Regla visual | Mensaje o ayuda | Estado visual |
|---|---|---:|---|---|---|
| Nombres | Texto | Sí | No aceptar sólo espacios; longitud final según Seguridad | “Ingresa tus nombres” | Default/foco/error |
| Apellidos | Texto | Sí | No aceptar sólo espacios; longitud final según Seguridad | “Ingresa tus apellidos” | Default/foco/error |
| Correo electrónico | Email | Sí | Formato válido | “Ingresa un correo electrónico válido” | Default/foco/error |
| Celular | Teléfono | Sí | Formato y longitud aprobados para el mercado objetivo | Ayuda con ejemplo no personalizado | Default/foco/error |
| Contraseña | Password | Sí | Política publicada por Seguridad | Lista de requisitos, nunca valor visible por defecto | Default/foco/error/éxito parcial |
| Confirmación | Password | Sí | Coincidir con contraseña | “Las contraseñas deben coincidir” | Default/foco/error |
| Términos | Checkbox | Sí | Debe marcarse deliberadamente | “Debes aceptar los términos para continuar” | Default/foco/error |

Los errores del servicio se mapean al campo sólo cuando la respuesta permite hacerlo sin revelar información sensible. La contraseña nunca aparece en logs, alertas, URLs ni analítica visual.

## 10. Responsive

### Desktop

- **Referencia:** 1440 px.
- Formulario en tarjeta o contenedor de ancho legible.
- Nombres/apellidos y contraseña/confirmación pueden usar dos columnas únicamente si las etiquetas, ayudas y errores mantienen suficiente espacio.
- Correo, celular, política y términos ocupan el ancho completo del formulario.

### Mobile

- **Referencia:** 390 px.
- Todos los campos se apilan en una sola columna.
- La política de contraseña se mantiene próxima al campo sin empujar fuera de contexto el CTA.
- El teclado no oculta el campo activo ni el primer error.
- Términos y enlaces tienen áreas táctiles separadas para marcar y abrir documentos sin acciones accidentales.

### Anchuras intermedias

- Pasar a una columna cuando dos campos con ayuda o error ya no conservan un ancho legible; no depender sólo de un breakpoint fijo.

## 11. Accesibilidad

- Orden de foco igual al orden visual y semántico.
- Etiquetas persistentes, agrupación clara y autocompletado adecuado para datos personales.
- Mostrar/ocultar contraseña tiene nombre y estado accesibles independientes para ambos campos.
- La lista de requisitos comunica cumplimiento con texto e icono, no sólo con color.
- El checkbox incluye etiqueta completa; los enlaces dentro del texto no impiden activarlo con teclado.
- Al fallar el envío, el foco llega al resumen o al primer campo inválido; al aceptarse, llega al título de confirmación.
- Los mensajes dinámicos usan anuncios que no interrumpen cada pulsación.
- Contraste, foco, tamaños táctiles y movimiento siguen `DS-001`.

## 12. Frames requeridos en Figma

| Frame | Plataforma | Estado | Contenido diferencial |
|---|---|---|---|
| `V-002 / Desktop / Principal` | Desktop | Principal | Composición completa y posibles pares de campos. |
| `V-002 / Mobile / Principal` | Mobile | Principal | Formulario apilado. |
| `V-002 / Desktop / Validación` | Desktop | Error local | Varios campos, términos y resumen de errores. |
| `V-002 / Mobile / Política contraseña` | Mobile | Ayuda activa | Requisitos visibles durante edición. |
| `V-002 / Desktop / Enviando` | Desktop | Progreso | CTA no repetible. |
| `V-002 / Mobile / Correo no disponible` | Mobile | Error neutral | Mensaje y alternativas. |
| `V-002 / Desktop / Política rechazada` | Desktop | Error `422` | Reglas externas incumplidas. |
| `V-002 / Mobile / Solicitud aceptada` | Mobile | Éxito | Verificación por correo y login. |

El error temporal puede anotarse como variante del frame “Correo no disponible” si conserva el layout, pero debe usar copy y acciones diferentes.

## 13. Criterios de aceptación visual

- [ ] `UI-V002-001`: La vista deja claro antes y después del envío que la cuenta requiere verificación por correo.
- [ ] `UI-V002-002`: El estado `409` no confirma que el correo pertenezca a una cuenta existente.
- [ ] `UI-V002-003`: La política de contraseña es legible, accesible y distingue requisitos cumplidos sin depender del color.
- [ ] `UI-V002-004`: El envío no puede repetirse mientras está en curso y no inicia sesión automáticamente.
- [ ] `UI-V002-005`: Las variantes desktop y mobile preservan etiquetas, ayudas, errores y términos sin ocultarlos.
- [ ] `UI-V002-006`: La contraseña se descarta al abandonar la vista y nunca se expone en mensajes o URLs.
- [ ] `UI-V002-007`: `canalOrigen` no aparece como campo editable.
- [ ] La vista utiliza componentes y estilos de `DS-001`.

## 14. Decisiones y pendientes

| ID | Pregunta o decisión | Responsable | Fecha límite | Estado |
|---|---|---|---|---|
| `V-002-OPEN-01` | Incorporar la política exacta y vigente de contraseña publicada por Seguridad. | Andrés / Seguridad | Antes del diseño final | Abierta |
| `V-002-OPEN-02` | Confirmar formato, país por defecto y restricciones del celular. | Producto + Seguridad | Antes del diseño final | Abierta |
| `V-002-OPEN-03` | Registrar URLs y versión aprobada de términos y política de privacidad. | Producto | Antes del diseño final | Abierta |
| `V-002-OPEN-04` | Confirmar si el correo puede precargarse en `V-001` tras el registro aceptado. | Andrés / Seguridad | Antes del diseño final | Abierta |
