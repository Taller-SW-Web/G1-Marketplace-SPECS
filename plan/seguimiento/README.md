# Seguimiento de tareas — Marketplace

Corte inicial 2026-10-02 · Semanas 6–15 · Ninguna implementación ejecutada en esta entrega.

## 1. Inventario y responsables

256 tareas funcionales en40 archivos + 27 tareas transversales = **283 tareas**. Son unidades de trabajo por área, no283 funcionalidades ni nuevas pantallas. La división permite FE/BE/DB/INT/QA/DOC/OPS trazables, estimar y revisar sin pedir un prompt por funcionalidad.

Responsables y revisores de cada tabla son propuesta por rol actual; confirmar capacidad antes de iniciar. Nombres completos en [plan general](../PLAN-IMPLEMENTACION.md#4-responsabilidad-sin-confundir-diseño-con-código). BD = Leonidas+Andres; Fernando = QA. No se modifican paquetes UI ni se reparte nuevamente el diseño.

## 2. Uso del tablero

Editar estado/semana en la tabla de cada archivo y añadir evidencia en la sección de tarea. No mantener una copia de estados por sprint: esos archivos sólo indexan planes.

Estados permitidos:

- **Pendiente:** no iniciada; referente/revisor propuestos y Ready por revisar.
- **En progreso:** responsable confirmó y está implementando, con alcance claro.
- **En revisión:** evidencia disponible, revisor independiente asignado.
- **Bloqueado:** condición concreta impide esa tarea, con gate/evidencia requerida y dueño.
- **Terminado:** DoD cumplido y aprobado, no sólo código escrito o mock listo.

Al bloquear: escribir motivo, gate/tarea, dueño externo/interno, semana objetivo y próximo paso. Al liberar: enlazar decisión/contrato/configuración/prueba y revisar dependencias. Cierre QA local no termina INT real.

Campos obligatorios: ID estable, área, trabajo, prioridad, dependencia, responsable, revisor, semana objetivo, estado, DoD y evidencia. No aceptación/resultado falso.

## 3. Convenciones y prioridad

IDs base [nomenclatura](../../SPECS/NOMENCLATURA-SDD.md): TASK-F###-FE/BE/DB/INT/QA-###. Este plan añade **DOC** y **OPS** para documentación/DevOps y **TASK-TRANS-S##-ÁREA-###** para trabajo transversal del sprint; no son IDs de specs. QA-002 = seguridad específica por funcionalidad. No confundir seguridad sólo con pipeline: autor corrige, QA verifica y release revisa.

P0 bloqueo/esencial; P1 capacidad principal; P2 mejora dentro del alcance. INT externo inicia Bloqueado si falta evidencia; otros componentes/tests pueden avanzar con fixtures y quedan rotulados mock. Contenedor correo server-only no se entrega como SPA.

## 4. Catálogo del seguimiento

| ID | Tareas | Sprint | Enlaces |
|---|---|---|---|
| F-001 | 6 | S1 | [Tablero](F-001-registrar-cliente.md) · [Plan](../funcionalidades/F-001-registrar-cliente.md) |
| F-002 | 6 | S1 | [Tablero](F-002-iniciar-sesion.md) · [Plan](../funcionalidades/F-002-iniciar-sesion.md) |
| F-003 | 6 | S1 | [Tablero](F-003-cerrar-sesion.md) · [Plan](../funcionalidades/F-003-cerrar-sesion.md) |
| F-004 | 6 | S1 | [Tablero](F-004-solicitar-recuperacion-password.md) · [Plan](../funcionalidades/F-004-solicitar-recuperacion-password.md) |
| F-005 | 6 | S1 | [Tablero](F-005-restablecer-password.md) · [Plan](../funcionalidades/F-005-restablecer-password.md) |
| F-006 | 6 | S2 | [Tablero](F-006-inicio-categorias-destacados.md) · [Plan](../funcionalidades/F-006-inicio-categorias-destacados.md) |
| F-007 | 6 | S2 | [Tablero](F-007-buscar-productos-texto.md) · [Plan](../funcionalidades/F-007-buscar-productos-texto.md) |
| F-008 | 6 | S2 | [Tablero](F-008-filtrar-catalogo.md) · [Plan](../funcionalidades/F-008-filtrar-catalogo.md) |
| F-009 | 6 | S2 | [Tablero](F-009-ordenar-catalogo.md) · [Plan](../funcionalidades/F-009-ordenar-catalogo.md) |
| F-010 | 6 | S2 | [Tablero](F-010-paginar-catalogo.md) · [Plan](../funcionalidades/F-010-paginar-catalogo.md) |
| F-011 | 6 | S2 | [Tablero](F-011-detalle-producto.md) · [Plan](../funcionalidades/F-011-detalle-producto.md) |
| F-012 | 6 | S2 | [Tablero](F-012-precio-oferta-descuento.md) · [Plan](../funcionalidades/F-012-precio-oferta-descuento.md) |
| F-013 | 6 | S2 | [Tablero](F-013-seleccion-atributos-variante.md) · [Plan](../funcionalidades/F-013-seleccion-atributos-variante.md) |
| F-014 | 6 | S2 | [Tablero](F-014-consultar-disponibilidad-stock.md) · [Plan](../funcionalidades/F-014-consultar-disponibilidad-stock.md) |
| F-015 | 6 | S2 | [Tablero](F-015-productos-relacionados.md) · [Plan](../funcionalidades/F-015-productos-relacionados.md) |
| F-016 | 7 | S2 | [Tablero](F-016-agregar-item-carrito.md) · [Plan](../funcionalidades/F-016-agregar-item-carrito.md) |
| F-017 | 7 | S3 | [Tablero](F-017-cambiar-cantidad-item-carrito.md) · [Plan](../funcionalidades/F-017-cambiar-cantidad-item-carrito.md) |
| F-018 | 7 | S3 | [Tablero](F-018-quitar-item-carrito.md) · [Plan](../funcionalidades/F-018-quitar-item-carrito.md) |
| F-019 | 7 | S3 | [Tablero](F-019-visualizar-carrito.md) · [Plan](../funcionalidades/F-019-visualizar-carrito.md) |
| F-020 | 7 | S3 | [Tablero](F-020-fusionar-carrito-anonimo.md) · [Plan](../funcionalidades/F-020-fusionar-carrito-anonimo.md) |
| F-021 | 7 | S3 | [Tablero](F-021-mover-carrito-favoritos.md) · [Plan](../funcionalidades/F-021-mover-carrito-favoritos.md) |
| F-022 | 6 | S4 | [Tablero](F-022-seleccionar-direccion-envio.md) · [Plan](../funcionalidades/F-022-seleccionar-direccion-envio.md) |
| F-023 | 6 | S4 | [Tablero](F-023-calcular-resumen-envio.md) · [Plan](../funcionalidades/F-023-calcular-resumen-envio.md) |
| F-024 | 6 | S4 | [Tablero](F-024-validar-aplicar-cupon-promocion.md) · [Plan](../funcionalidades/F-024-validar-aplicar-cupon-promocion.md) |
| F-025 | 7 | S4 | [Tablero](F-025-simular-pago-revalidar-stock.md) · [Plan](../funcionalidades/F-025-simular-pago-revalidar-stock.md) |
| F-026 | 7 | S4 | [Tablero](F-026-crear-orden-ventas.md) · [Plan](../funcionalidades/F-026-crear-orden-ventas.md) |
| F-027 | 7 | S4 | [Tablero](F-027-confirmacion-orden.md) · [Plan](../funcionalidades/F-027-confirmacion-orden.md) |
| F-028 | 6 | S5 | [Tablero](F-028-historial-pedidos.md) · [Plan](../funcionalidades/F-028-historial-pedidos.md) |
| F-029 | 6 | S5 | [Tablero](F-029-filtrar-historial-pedidos.md) · [Plan](../funcionalidades/F-029-filtrar-historial-pedidos.md) |
| F-030 | 6 | S5 | [Tablero](F-030-detalle-pedido.md) · [Plan](../funcionalidades/F-030-detalle-pedido.md) |
| F-031 | 6 | S5 | [Tablero](F-031-reordenar-compra.md) · [Plan](../funcionalidades/F-031-reordenar-compra.md) |
| F-032 | 6 | S5 | [Tablero](F-032-seguimiento-despacho.md) · [Plan](../funcionalidades/F-032-seguimiento-despacho.md) |
| F-033 | 6 | S5 | [Tablero](F-033-generar-plantilla-correo.md) · [Plan](../funcionalidades/F-033-generar-plantilla-correo.md) |
| F-034 | 7 | S5 | [Tablero](F-034-enviar-confirmacion-asincrona.md) · [Plan](../funcionalidades/F-034-enviar-confirmacion-asincrona.md) |
| F-035 | 7 | S5 | [Tablero](F-035-enviar-actualizacion-despacho.md) · [Plan](../funcionalidades/F-035-enviar-actualizacion-despacho.md) |
| F-036 | 7 | S3 | [Tablero](F-036-agregar-favorito.md) · [Plan](../funcionalidades/F-036-agregar-favorito.md) |
| F-037 | 7 | S3 | [Tablero](F-037-visualizar-favoritos.md) · [Plan](../funcionalidades/F-037-visualizar-favoritos.md) |
| F-038 | 7 | S3 | [Tablero](F-038-quitar-favorito.md) · [Plan](../funcionalidades/F-038-quitar-favorito.md) |
| F-039 | 7 | S3 | [Tablero](F-039-mover-favorito-carrito.md) · [Plan](../funcionalidades/F-039-mover-favorito-carrito.md) |
| F-040 | 7 | S5 | [Tablero](F-040-evaluacion-postentrega.md) · [Plan](../funcionalidades/F-040-evaluacion-postentrega.md) |

Trabajo común: [TRANSVERSALES](TRANSVERSALES.md). QA/DevSecOps: [estrategia de pruebas](../DEVSECOPS-Y-PRUEBAS.md). Gates: [decisiones/bloqueos](../DECISIONES-Y-BLOQUEOS.md).

## 5. Revisión y evidencia

Diego coordina propuesta de dos revisiones breves por semana, planificación/demo/retro de sprint. No se crea ninguna automatización ni evento de calendario. Reportar sólo avance con evidencia, bloqueos y riesgo de capacidad.

Evidencia: revisión/artefacto futuro, herramienta/comando/entorno, casos resultado, fecha, hallazgos/corrección/retest y revisor. Sanitizar PII/secrets y respetar autorización de entornos. Un link a Figma acredita diseño, no prueba de API.

## 6. Checklist de preparación documental

- [x] Specs React F-001–F-040 elaboradas.
- [x] Plan por funcionalidad y cinco iteraciones hasta semana 15.
- [x] Tareas FE/BE/DB/INT/QA funcional/QA seguridad/DOC/OPS.
- [x] Prioridad, dependencias, referentes/revisores propuestos, semana, estados, DoD y evidencia requerida.
- [x] Integraciones sin evidencia marcadas Bloqueado.
- [ ] Aceptación de responsables y estimación de horas/capacidad reales.
- [ ] Contratos/configuración/pruebas externos y gates locales cerrados.
- [ ] Código, pruebas/escaneos y despliegues realizados.
- [ ] Revisión periódica de tablero practicada y avances aprobados.

La lista externa original se deja intacta: sus puntos1,4,5 no forman parte de este encargo.

