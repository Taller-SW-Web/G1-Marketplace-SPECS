# Jim Bryan Segovia Valencia — Product Owner — responsabilidad punta a punta

**Propuesta 13/10/2026; pendiente de aceptación y estimación personal.** Bloque: **1. Cuenta y acceso**; IDs: **F-001–F-005**. Revisor principal: **Andres Morales**. Hitos: S2: F-001–003; S5: F-004–005. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

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

- **Frontend:** Implementar estados de V-001/V-002 y después V-003/V-004 según specs; integrar el resultado de F-020 sólo mediante contrato con Andres. Respetar foco, errores neutros y responsive.
- **Backend Marketplace:** Implementar adaptador BFF de identidad y validación de respuesta sin guardar contraseñas ni emitir tokens propios. Seguir contrato publicado por Seguridad para registro, sesión, salida y recuperación; tokens/cookies/MFA requieren G-AUTH.
- **Pruebas:** Válido/inválido, antienumeración, expiración y usuario ajeno; prueba de contrato local, después entorno real autorizado. Evidenciar UI y API protegida en H4.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Andres recibe el estado/identificador de sesión pactado; Diego recibe casos de aceptación.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Antes de iniciar:** estimar FE/BE/INT/QA/revisión por semana; acordar archivos compartidos y capacidad con Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si la carga o el gate impiden el objetivo del hito, proponer resecuenciación documentada antes del corte.
