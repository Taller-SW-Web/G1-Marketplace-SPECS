# Seguimiento de tareas — Marketplace

Corte planificado 2026-10-10 · H3 2026-10-18 · Replanificación H4 2026-10-19. El tablero no prueba ejecución de software. F-006/F-007 y gates de nube pasan como arrastre prioritario a S2/H4 según el [corte verificable](../CORTE-H3-Y-TRASPASO-H4.md); los IDs y semanas originales se registran junto a la nueva semana objetivo para trazabilidad.

## 1. Inventario y responsables

256 tareas funcionales en 40 archivos + 37 tareas transversales = **293 tareas**. Son unidades de trabajo por área, no 293 funcionalidades ni nuevas pantallas. La división permite FE/BE/DB/INT/QA/DOC/OPS y diseño visual trazables.

La [matriz punta a punta](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) fija un owner y revisor distintos por F-001–F-040 por decisión del PO. Las 256 filas funcionales conservan IDs/estados; la estimación base está en la matriz. Pasar a En progreso requiere inicio efectivo y registro de avance, no aceptación formal previa. La responsabilidad de diseño visual permanece separada.

## Seguimiento de las entregas H4

[S02](../iteraciones/S02-semanas-09-11.md) fija 25 cierres principales condicionados a contratos/entornos/pruebas (20 circuito Productos + 5 cuenta), sin restricción horaria. [Inventario](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) clasifica 25 dependientes G6 y las otras 15. Se conservan los 256 IDs/estados funcionales, con nuevas semanas y evidencia por etapa; no se duplica trabajo.

Por F registrar diseñado, implementado con datos de prueba, integrado con otro módulo y probado en despliegue. Las 25 principales tienen objetivo H4; las otras 15 implementación/pruebas propias H4 y cierre integral posterior. DOC y QA local avanzan sin INT, pero su DoD completo conserva dependencias. Gates abiertos conservan F parcial, sin descontar ni duplicar cierres y sin cambiar estados por planificar.

## 2. Uso del tablero

Editar estado/semana en la tabla de cada archivo y añadir evidencia en la sección de tarea. No mantener una copia de estados por sprint: esos archivos sólo indexan planes.

Estados permitidos:

- **Pendiente:** no iniciada; asignación y Ready por revisar.
- **En progreso:** responsable asignado está implementando, con alcance claro y evidencia de inicio.
- **En revisión:** evidencia disponible, revisor independiente asignado.
- **Bloqueado:** condición concreta impide esa tarea, con gate/evidencia requerida y dueño.
- **Terminado:** DoD cumplido y aprobado, no sólo código escrito o mock listo.

Al bloquear: escribir motivo, gate/tarea, dueño externo/interno, semana objetivo y próximo paso. Al liberar: enlazar decisión/contrato/configuración/prueba y revisar dependencias. Cierre QA local no termina INT real.

Campos obligatorios: ID estable, área, trabajo, prioridad, dependencia, responsable, revisor, semana objetivo, estado, DoD y evidencia. No aceptación/resultado falso.

## 3. Convenciones y prioridad

IDs base [nomenclatura](../../SPECS/NOMENCLATURA-SDD.md): TASK-F###-FE/BE/DB/INT/QA-###. Este plan añade **DOC** y **OPS** para documentación/DevOps y **TASK-TRANS-S##-ÁREA-###** para trabajo transversal del sprint; no son IDs de specs. QA-002 = seguridad específica por funcionalidad. No confundir seguridad sólo con pipeline: autor corrige, QA verifica y release revisa.

P0 bloqueo/esencial; P1 alcance principal; P2 mejora dentro del alcance. INT externo inicia Bloqueado si falta evidencia; otros componentes/tests pueden avanzar con fixtures y quedan rotulados mock. Contenedor correo server-only no se entrega como SPA.

## 4. Catálogo del seguimiento

| ID | Tareas | Sprint | Enlaces |
|---|---|---|---|
| F-001 | 6 | S02/H4 | [Tablero](F-001-registrar-cliente.md) · [Plan](../funcionalidades/F-001-registrar-cliente.md) |
| F-002 | 6 | S02/H4 | [Tablero](F-002-iniciar-sesion.md) · [Plan](../funcionalidades/F-002-iniciar-sesion.md) |
| F-003 | 6 | S02/H4 | [Tablero](F-003-cerrar-sesion.md) · [Plan](../funcionalidades/F-003-cerrar-sesion.md) |
| F-004 | 6 | S02/H4 | [Tablero](F-004-solicitar-recuperacion-password.md) · [Plan](../funcionalidades/F-004-solicitar-recuperacion-password.md) |
| F-005 | 6 | S02/H4 | [Tablero](F-005-restablecer-password.md) · [Plan](../funcionalidades/F-005-restablecer-password.md) |
| F-006 | 6 | S02/H4 (arrastre H3) | [Tablero](F-006-inicio-categorias-destacados.md) · [Plan](../funcionalidades/F-006-inicio-categorias-destacados.md) |
| F-007 | 6 | S02/H4 (arrastre H3) | [Tablero](F-007-buscar-productos-texto.md) · [Plan](../funcionalidades/F-007-buscar-productos-texto.md) |
| F-008 | 6 | S02/H4 | [Tablero](F-008-filtrar-catalogo.md) · [Plan](../funcionalidades/F-008-filtrar-catalogo.md) |
| F-009 | 6 | S02/H4 | [Tablero](F-009-ordenar-catalogo.md) · [Plan](../funcionalidades/F-009-ordenar-catalogo.md) |
| F-010 | 6 | S02/H4 | [Tablero](F-010-paginar-catalogo.md) · [Plan](../funcionalidades/F-010-paginar-catalogo.md) |
| F-011 | 6 | S02/H4 | [Tablero](F-011-detalle-producto.md) · [Plan](../funcionalidades/F-011-detalle-producto.md) |
| F-012 | 6 | S02/H4 | [Tablero](F-012-precio-oferta-descuento.md) · [Plan](../funcionalidades/F-012-precio-oferta-descuento.md) |
| F-013 | 6 | S02/H4 | [Tablero](F-013-seleccion-atributos-variante.md) · [Plan](../funcionalidades/F-013-seleccion-atributos-variante.md) |
| F-014 | 6 | S02/H4 | [Tablero](F-014-consultar-disponibilidad-stock.md) · [Plan](../funcionalidades/F-014-consultar-disponibilidad-stock.md) |
| F-015 | 6 | S02/H4 | [Tablero](F-015-productos-relacionados.md) · [Plan](../funcionalidades/F-015-productos-relacionados.md) |
| F-016 | 7 | S02/H4 | [Tablero](F-016-agregar-item-carrito.md) · [Plan](../funcionalidades/F-016-agregar-item-carrito.md) |
| F-017 | 7 | S02/H4 | [Tablero](F-017-cambiar-cantidad-item-carrito.md) · [Plan](../funcionalidades/F-017-cambiar-cantidad-item-carrito.md) |
| F-018 | 7 | S02/H4 | [Tablero](F-018-quitar-item-carrito.md) · [Plan](../funcionalidades/F-018-quitar-item-carrito.md) |
| F-019 | 7 | S02/H4 | [Tablero](F-019-visualizar-carrito.md) · [Plan](../funcionalidades/F-019-visualizar-carrito.md) |
| F-020 | 7 | S02/H4 | [Tablero](F-020-fusionar-carrito-anonimo.md) · [Plan](../funcionalidades/F-020-fusionar-carrito-anonimo.md) |
| F-021 | 7 | S02/H4 | [Tablero](F-021-mover-carrito-favoritos.md) · [Plan](../funcionalidades/F-021-mover-carrito-favoritos.md) |
| F-022 | 6 | S03 integral; implementación H4 | [Tablero](F-022-seleccionar-direccion-envio.md) · [Plan](../funcionalidades/F-022-seleccionar-direccion-envio.md) |
| F-023 | 6 | S03 integral; implementación H4 | [Tablero](F-023-calcular-resumen-envio.md) · [Plan](../funcionalidades/F-023-calcular-resumen-envio.md) |
| F-024 | 6 | S03 integral; implementación H4 | [Tablero](F-024-validar-aplicar-cupon-promocion.md) · [Plan](../funcionalidades/F-024-validar-aplicar-cupon-promocion.md) |
| F-025 | 7 | S03 integral; implementación H4 | [Tablero](F-025-simular-pago-revalidar-stock.md) · [Plan](../funcionalidades/F-025-simular-pago-revalidar-stock.md) |
| F-026 | 7 | S03 integral; implementación H4 | [Tablero](F-026-crear-orden-ventas.md) · [Plan](../funcionalidades/F-026-crear-orden-ventas.md) |
| F-027 | 7 | S03 integral; implementación H4 | [Tablero](F-027-confirmacion-orden.md) · [Plan](../funcionalidades/F-027-confirmacion-orden.md) |
| F-028 | 6 | S03 integral; implementación H4 | [Tablero](F-028-historial-pedidos.md) · [Plan](../funcionalidades/F-028-historial-pedidos.md) |
| F-029 | 6 | S05 integral; implementación H4 | [Tablero](F-029-filtrar-historial-pedidos.md) · [Plan](../funcionalidades/F-029-filtrar-historial-pedidos.md) |
| F-030 | 6 | S03 integral; implementación H4 | [Tablero](F-030-detalle-pedido.md) · [Plan](../funcionalidades/F-030-detalle-pedido.md) |
| F-031 | 6 | S05 integral; implementación H4 | [Tablero](F-031-reordenar-compra.md) · [Plan](../funcionalidades/F-031-reordenar-compra.md) |
| F-032 | 6 | S04 integral; implementación H4 | [Tablero](F-032-seguimiento-despacho.md) · [Plan](../funcionalidades/F-032-seguimiento-despacho.md) |
| F-033 | 6 | S03 integral; implementación H4 | [Tablero](F-033-generar-plantilla-correo.md) · [Plan](../funcionalidades/F-033-generar-plantilla-correo.md) |
| F-034 | 7 | S03 integral; implementación H4 | [Tablero](F-034-enviar-confirmacion-asincrona.md) · [Plan](../funcionalidades/F-034-enviar-confirmacion-asincrona.md) |
| F-035 | 7 | S04 integral; implementación H4 | [Tablero](F-035-enviar-actualizacion-despacho.md) · [Plan](../funcionalidades/F-035-enviar-actualizacion-despacho.md) |
| F-036 | 7 | S02/H4 | [Tablero](F-036-agregar-favorito.md) · [Plan](../funcionalidades/F-036-agregar-favorito.md) |
| F-037 | 7 | S02/H4 | [Tablero](F-037-visualizar-favoritos.md) · [Plan](../funcionalidades/F-037-visualizar-favoritos.md) |
| F-038 | 7 | S02/H4 | [Tablero](F-038-quitar-favorito.md) · [Plan](../funcionalidades/F-038-quitar-favorito.md) |
| F-039 | 7 | S02/H4 | [Tablero](F-039-mover-favorito-carrito.md) · [Plan](../funcionalidades/F-039-mover-favorito-carrito.md) |
| F-040 | 7 | S05 integral; implementación H4 | [Tablero](F-040-evaluacion-postentrega.md) · [Plan](../funcionalidades/F-040-evaluacion-postentrega.md) |

Trabajo común: [TRANSVERSALES](TRANSVERSALES.md). QA/DevSecOps: [estrategia de pruebas](../DEVSECOPS-Y-PRUEBAS.md). Gates: [decisiones/bloqueos](../DECISIONES-Y-BLOQUEOS.md).

## 5. Revisión y evidencia

Dos revisiones breves por semana, planificación/demo/retro de iteración; Diego coordina el tablero con Jim y sigue avance, calidad y desbloqueos. No se crea ninguna automatización ni evento de calendario. Reportar sólo avance con evidencia, bloqueos y riesgo de contrato, entorno o calidad.

Evidencia: revisión/artefacto futuro, herramienta/comando/entorno, casos resultado, fecha, hallazgos/corrección/retest y revisor. Sanitizar PII/secrets y respetar autorización de entornos. Un link a Figma acredita diseño, no prueba de API.

## 6. Checklist de preparación documental

- [x] Specs React F-001–F-040 elaboradas.
- [x] Plan por funcionalidad y cinco iteraciones hasta semana 16, alineadas a H3–H6.
- [x] Tareas FE/BE/DB/INT/QA funcional/QA seguridad/DOC/OPS.
- [x] Prioridad, dependencias, semana, estados, DoD y evidencia requerida; responsables/revisores asignados por el PO en la matriz.
- [x] Integraciones sin evidencia marcadas Bloqueado.
- [x] Responsables/revisores y estimación base fijados por el PO; no se exige aceptación individual.
- [ ] Contratos/entornos y bloqueos por operación contrastados con evidencia durante cada iteración.
- [ ] Contratos/configuración/pruebas externos y gates locales cerrados.
- [ ] Código, pruebas/escaneos y despliegues realizados.
- [ ] Revisión periódica de tablero practicada y avances aprobados.

Este seguimiento cubre requisitos técnicos de los hitos, no la preparación de PPT ni el relato de uso de IA.

## Projects y asignaciones en GitHub

[Índice de los dos Projects y las 293 issues](../github/README.md): 88 frontend y 205 backend. Una issue por TASK, mismos responsables/revisores y estados de origen; cada issue enlaza fuente, dependencias y tareas de la misma función. El índice conserva el corte inicial y el progreso vivo se registra en issues y se reconcilia aquí. Los cuatro niveles de evidencia se mantienen separados y ninguna publicación libera un gate.
