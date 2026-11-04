# Spec de componentes React — F-005 Restablecer contraseña

> **Alcance actualizado por el PO el 26/10/2026:** el formulario de restablecimiento, sus estados y el token del correo pertenecen a la SPA G7. Las secciones de `ResetPasswordForm`, `ResetLinkOutcome` y sus casos de componente describen la implementación G1 anterior; ya no son la composición web objetivo. G1 prueba el regreso al login Marketplace sin sesión implícita. Véase [decisión y gates](../../plan/coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md). Esta spec no certifica código ni integración.

## 1. Metadatos y trazabilidad

| Campo | Valor |
|---|---|
| ID funcional | `F-005` |
| Versión / estado | `0.1.0` / En revisión |
| Fecha | 2026-10-02 |
| Funcional | [F-005](../funcional/F-005-restablecer-password.md) |
| UI funcional | [F-005](../ui/F-005-restablecer-password.md) |
| Contrato API | [F-005](../contrato-api/F-005-restablecer-password.md) |
| Entregables visuales | [V-004](../ui/vistas/V-004-restablecimiento-contrasena.md) |
| Base transversal | [Arquitectura React](ARQUITECTURA-REACT.md), [DS-001 v0.2.0](../ui/DS-001-sistema-diseno-marketplace.md) |
| Stack | React + TypeScript + Next.js App Router (PO, 2026-10-10); FE main@ec1acfb observado el 18/10: Next.js 16.4.1, React 19.3.1 y TypeScript 5.9.3 con lockfile; kit global pendiente de DS-OPEN-03. Es corte de código, no aprobación de esta spec |
| Responsables de implementación | Asignación del PO en [plan F-005](../../plan/funcionalidades/F-005-restablecer-password.md); no reemplaza el reparto de mockups |
| Iteración objetivo | S02/H4, semanas 9–11; integración sujeta a gates y evidencia, sin restricción horaria por decisión del PO |

## 2. Rutas y pantallas

| Ruta / superficie | Acceso | Composición |
|---|---|---|
| `/restablecer-contrasena?token=...` en la SPA G7 | Pública con enlace de recuperación (no verificación de correo) | Formulario y estados G7; retorno a login G1 mediante destino fijo permitido. |

G1 no recibe el token en su ruta homónima en el recorrido acordado. El árbol y contratos de `ResetPasswordForm` siguientes quedan como referencia histórica del código ya preparado, sujetos a reemplazo en G1 FE; no son nuevos entregables de cierre.

Los enlaces de vistas/overlays definen todos los frames y variantes; no crear un nuevo ID V para un estado de la misma pantalla. Desktop y mobile siguen dentro del alcance; consultar frames y estados vigentes en las specs UI enlazadas. Mobile no se simula reduciendo el desktop.

## 3. Árbol de componentes

```text
Layout de ruta → límite público/privado correspondiente
├── ResetPasswordForm
└── ResetLinkOutcome
    └── Feedback accesible compartido según estado
```

El contenedor coordina transporte/estado; los componentes presentacionales no llaman servicios externos ni contienen reglas de descuento, stock o autorización.

## 4. Contratos de componentes

| ID / componente | Responsabilidad | Props tipadas (propuesta) | Eventos |
|---|---|---|---|
| `CMP-F005-001` · `ResetPasswordForm` | Muestra política vigente y coincidencia. | `policy: PasswordPolicy; busy: boolean; errors: FieldErrors` | onSubmit({nuevaContrasena,confirmacion}) |
| `CMP-F005-002` · `ResetLinkOutcome` | Separa enlace inválido/vencido de éxito sin iniciar sesión. | `kind: 'INVALID' \| 'EXPIRED' \| 'SUCCESS' \| 'ERROR'` | onRecover(); onLogin(); onRetry() |

Los nombres de DTO y drafts son contratos TypeScript de implementación, no nuevos campos de la API. Su estructura se deriva exclusivamente del contrato enlazado; aplicar las convenciones de tipos de [ARQUITECTURA-REACT](ARQUITECTURA-REACT.md#3-tipos-y-contratos). Props con `busy` no habilitan dobles mutaciones. Eventos se invocan una vez y devuelven control al contenedor.

## 5. Estado y flujo de datos

- **Local:** Token de recuperación y contraseñas en memoria; ocultar token en URL visible con reemplazo tras capturarlo, no en history state; no analytics del enlace original.
- **Compartido:** sólo sesión no sensible, identidad del contexto y contexto transitorio del flujo; no duplicar datos remotos en stores independientes.
- **Remoto / caché:** Sin query inventada de validación de token. Sólo POST definido; estado inicial comprueba presencia/forma local.
- **Flujo específico vigente:** El enlace abre G7 y el token permanece allí; no se confunde con verificación F-001. G7 procesa el `204`, borra secretos y ofrece el login G1 permitido, sin sesión automática. El retorno aún necesita implementación y prueba.
- Cancelar o ignorar respuestas de identidad/selección anterior. No guardar cuerpos sensibles en devtools, logs o analítica. Los cachés privados se eliminan al cerrar o cambiar de sesión.

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente |
|---|---|---|
| `usePasswordReset` | Orquestar el flujo descrito; presentación consume estado discriminado y callbacks | Funcional F-005, UI F-005, API F-005 |
| Adaptador tipado | Validar DTO y mapear error público; sin aceptar shape externo no homologado | Contrato API enlazado |
| Validación local | Ayuda inmediata, nunca reemplaza validación ni autorización del servidor | Reglas siguientes |

Confirmación coincide; política publicada. 401/410 eliminan formulario y ofrecen recuperación; 422 permite corregir según respuesta.

### Operaciones documentadas

- `POST /api/v1/password/restablecer` permanece como adaptador BFF y caso API G1, no como operación obligatoria de la UI G1 en el recorrido acordado.

Auth y rutas `/password` se traducen mediante el límite de integración aprobado; no se presupone que ya exista proxy BFF ni CORS habilitado. Rutas `/internal` jamás se consumen desde el navegador. Header, request y response exactos pertenecen al contrato API, no a las props.

## 7. Estados, errores y recuperación

CHECKING_INPUT → EDITING → SAVING → SUCCESS | INVALID | EXPIRED | POLICY_ERROR | ERROR; comprobación inicial no certifica vigencia externa.

- **Carga:** skeleton de la región que consulta, o progreso local de mutación; nunca datos o importes de ejemplo.
- **Vacío / no aplicable:** sólo ante respuesta válida o condición explícita; errores nunca se convierten en colección vacía, precio cero o stock agotado.
- **Error:** mensaje público y recuperación específica del flujo; errores de campo se asocian a su control. Conservar valores no sensibles cuando sea seguro.
- **Éxito:** se deriva de la respuesta confirmada y actualiza sólo los recursos indicados; no usar navegación, color o cierre del modal como prueba de persistencia.
- **Reintentos:** lecturas acotadas/manuales; mutaciones no se repiten automáticamente si el contrato no garantiza idempotencia. `401` limpia datos privados y ofrece retorno interno seguro.

## 8. Accesibilidad, responsive y pruebas previstas

- Aplicar DS-001: etiquetas visibles, orden semántico, foco visible, controles de 44 px, contraste AA y movimiento reducido. No anidar botones de favoritos dentro de enlaces de tarjeta.
- Anunciar progreso/resultado sin duplicar anuncios; error de campo con `aria-describedby`, feedback con `status`/`alert` según severidad.
- Modal/drawer: nombre accesible, foco atrapado cuando modal, cierre permitido según spec y retorno a un elemento existente. Tras eliminar, foco a siguiente elemento/título.
- Probar desktop y, cuando estén listos los frames, mobile con teclado, zoom/reflow y sin depender de hover. Si es correo: HTML/texto legible sin imágenes/scripts, no aplicar roles de app interactiva.

| Caso técnico | Verificación mínima |
|---|---|
| `RC-F-005-01` | sin token no llama API. |
| `RC-F-005-02` | 401 y 410 ofrecen nuevo enlace. |
| `RC-F-005-03` | 422 no muestra token. |
| `RC-F-005-04` | 204 no crea sesión. |
| Estados UI | Render y transición de cada estado de la sección 7 y de la spec visual relacionada. |
| Transporte | Fixture de éxito, vacío/no aplicable, validación, autorización, conflicto, timeout y fallo externo que realmente correspondan al contrato. |
| Accesibilidad | Teclado/foco, nombre de controles, anuncios y contraste; pruebas automáticas más revisión manual. |

Los casos `RC-F-005-*` de formulario G1 son regresión de la implementación anterior, no sustituyen las pruebas en la SPA G7. Probar enlace del correo hacia G7, token válido/vencido/usado, política, ausencia de sesión implícita y retorno G7 → login G1 en navegador; probar el adaptador BFF por API de forma separada. Una demo con mocks no acredita integración real.

## 9. Criterios de aceptación técnica

- [ ] `RC-F-005-CONTRATO`: props, callbacks, DTO y operaciones respetan las specs enlazadas sin campos/endpoints inventados.
- [ ] `RC-F-005-ESTADOS`: todos los estados aplicables tienen render, transición, foco y prueba, incluidos vacíos y errores.
- [ ] `RC-F-005-DATOS`: autorización en servidor, caché aislada por sesión y ninguna persistencia de datos externos o secretos prohibidos.
- [ ] `RC-F-005-PRUEBAS`: casos de la sección 8 pasan y quedan evidencias vinculadas a las tareas.
- [ ] `RC-F-005-INTEGRACION`: condiciones de entrada resueltas y prueba de contrato externa aprobada antes de habilitar el flujo real.

## 10. Condiciones pendientes y límites de implementación

V-004-OPEN-02: validación previa no tiene endpoint; usar validación al enviar hasta homologarlo.

Estos pendientes no se resuelven inventando rutas ni comportamiento. El [registro de decisiones](../../plan/DECISIONES-Y-BLOQUEOS.md) separa las soluciones locales propuestas de las confirmaciones externas. Se puede diseñar, construir componentes puros y probar mocks sin activar una integración bloqueada.

