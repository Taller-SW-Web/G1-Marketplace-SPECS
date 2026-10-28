# Jim Bryan Segovia Valencia — Product Owner — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **1. Cuenta y acceso**; IDs: **F-001–F-005**. Revisor principal: **Andres Morales**. Hitos: S02/H4 F-001–F-005. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Trabajo asignado para S02 y Hito 4

El PO confirma **disponibilidad sin restricción horaria**. Todas las funciones del paquete reciben implementación/pruebas G1 H4 donde las reglas/contratos estén definidos; los cierres completos conservan gates externos. [S02](../iteraciones/S02-semanas-09-11.md) y [alcance](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).

- **F-001:** Implementar registro MARKETPLACE, validación/errores neutros, verificación de correo y retorno al login conforme G7; probar enlace válido/vencido/usado. Registro no inicia sesión por inferencia. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-002:** Implementar login y desafío OTP según política efectiva G7, sesión/refresh, transporte seguro y retorno seguro; probar credenciales inválidas, expiración y separación usuario/servicio. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-003:** Implementar logout G7 y limpieza de sesión/caché de usuario; probar UI y API después de salir, expiración y repetición idempotente. Cierre objetivo: S02/H4, semanas 9–11; cierre sólo con gates y prueba en despliegue.
- **F-004:** Por [decisión PO 26/10](../coordinacion/G7-F004-F005-ALCANCE-2026-10-27.md), implementar entrada G1 a recuperación en SPA G7; conservar BFF y probar API/entrega del correo, 202 uniforme, límite y antienumeración. Cierre objetivo: S02/H4, semanas 9–11; sólo con gates y prueba en despliegue.
- **F-005:** G7 opera formulario y política de reset en su SPA. G1 conserva BFF e integración, prueba enlace/token válido, vencido y usado y retorno G7 → login G1 sin sesión implícita. Cierre objetivo: S02/H4, semanas 9–11; sólo con gates y prueba en despliegue.

**Transversal:** AUTH-001: las cinco F de cuenta con G7, revisadas por Andres. Corregir los tres estados visuales Checkout con revisión Fernando; no omitir recuperación por tiempo. IDs TASK-TRANS-S02- en [TRANSVERSALES](../seguimiento/TRANSVERSALES.md).

**Evidencia:** diseño/contrato/frame revisado; commit FE+BE/fixture y pruebas positivo-negativo; integración REAL con proveedor/auth/traza; despliegue con URLs/SHAs/run. Registrar cada nivel sin inferencias. Ante frontera sin acuerdo, implementar la parte propia definida, registrar owner/bloqueo y continuar otras operaciones. No cerrar INT por doble, contrato escrito o tiempo disponible.

## Fuentes y alcance

- Specs funcionales de entrada: [F-001](../../SPECS/funcional/F-001-registrar-cliente.md), [F-002](../../SPECS/funcional/F-002-iniciar-sesion.md), [F-003](../../SPECS/funcional/F-003-cerrar-sesion.md), [F-004](../../SPECS/funcional/F-004-solicitar-recuperacion-password.md), [F-005](../../SPECS/funcional/F-005-restablecer-password.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-001–V-004, O-003. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: G-AUTH, Seguridad y G-STACK; F-020 de Andres; la política de MFA/transporte y URL deben aprobarse antes de integración REAL.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-002](../seguimiento/F-002-iniciar-sesion.md). El corte de H3 se vincula con `TASK-F002-FE-001`, `TASK-F002-BE-001` y `TASK-F002-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Como PO, obtener decisiones externas y aceptar alcance; eso no sustituye su código FE+BE ni la revisión independiente. Revisa correos y seguimiento de Fernando.

## Incremento vertical individual de H3 / semana 8

F-002: formulario V-001 que muestre validación y error neutro, conectado a una ruta BFF/adaptador de sesión con fixture de Seguridad. Caso positivo y credenciales inválidas sin exponer información de cuenta. Etiquetar MOCK; no crear sesión real.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Andres Morales, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar estados de V-001/V-002; para F-004/F-005, reemplazar la entrada/formularios G1 preparados por la navegación acordada con SPA G7 y probar retorno. V-003/V-004 G1 son referencias históricas, no la UI final. Integrar F-020 sólo mediante contrato con Andres. Respetar foco, errores neutros y responsive.
- **Backend Marketplace:** Implementar adaptador BFF de identidad y validación de respuesta sin guardar contraseñas ni emitir tokens propios. Seguir contrato publicado por Seguridad para registro, sesión, salida y recuperación; tokens/cookies/MFA requieren G-AUTH.
- **Pruebas:** Válido/inválido, antienumeración, expiración y usuario ajeno; prueba de contrato local, después entorno real autorizado. Evidenciar UI y API protegida en H4.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Andres recibe el estado/identificador de sesión pactado; Diego recibe casos de aceptación.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos contractuales/técnicos o hallazgos de calidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si un gate externo impide integrar, registrar por operación owner, prueba faltante y continuidad del trabajo propio; no reducir el alcance por disponibilidad horaria.
