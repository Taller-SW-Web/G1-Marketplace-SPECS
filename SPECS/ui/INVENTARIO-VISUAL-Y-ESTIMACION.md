# Inventario visual y estimación para reparto

Este documento consolida los entregables de diseño de alta fidelidad del Marketplace y aplica la escala definida en el plan de preparación. Es la fuente para repartir el trabajo; no sustituye las specs individuales.

## 1. Alcance validado

| Tipo | Rango | Cantidad | Índice |
|---|---|---:|---|
| Vistas | `V-001`–`V-017` | 17 | [`vistas/README.md`](./vistas/README.md) |
| Overlays | `O-001`–`O-010` | 10 | [`overlays/README.md`](./overlays/README.md) |
| Comunicaciones | `C-001`–`C-002` | 2 | [`comunicaciones/README.md`](./comunicaciones/README.md) |
| **Total** | — | **29** | — |

Todas las piezas tienen spec enlazada, estados, responsive/accesibilidad, frames requeridos y criterios de aceptación. Su estado documental es `En revisión` hasta validación humana y enlace final de Figma.

## 2. Método de estimación

Cada factor recibe 0, 1 o 2 puntos:

| Código | Factor | 0 | 1 | 2 |
|---|---|---|---|---|
| `L` | Complejidad de layout | Simple | Media | Alta |
| `F` | Formularios | Ninguno | Corto | Largo/múltiple |
| `E` | Estados visuales | 1–2 | 3–4 | 5 o más |
| `R` | Responsive | Cambio menor | Reorganización | Patrón distinto |
| `I` | Overlays/interacciones | Ninguno | Uno | Varios |
| `D` | Dependencias funcionales | 1 F | 2–3 F | 4 o más F |

`Total = L + F + E + R + I + D`, con rango de 0 a 12. Para overlays y correos se usa la misma escala interpretando `L`, `R` e `I` según su composición y variantes.

## 3. Estimación de vistas

| ID | Vista | L | F | E | R | I | D | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| [`V-001`](./vistas/V-001-inicio-sesion.md) | Inicio de sesión | 1 | 2 | 2 | 1 | 2 | 1 | **9** |
| [`V-002`](./vistas/V-002-registro.md) | Registro | 1 | 2 | 2 | 1 | 1 | 0 | **7** |
| [`V-003`](./vistas/V-003-recuperacion-contrasena.md) | Recuperación | 0 | 1 | 2 | 0 | 1 | 0 | **4** |
| [`V-004`](./vistas/V-004-restablecimiento-contrasena.md) | Restablecimiento | 1 | 1 | 2 | 0 | 1 | 0 | **5** |
| [`V-005`](./vistas/V-005-inicio.md) | Inicio | 2 | 1 | 2 | 2 | 2 | 1 | **10** |
| [`V-006`](./vistas/V-006-catalogo-resultados.md) | Catálogo y resultados | 2 | 2 | 2 | 2 | 2 | 2 | **12** |
| [`V-007`](./vistas/V-007-ficha-producto.md) | Ficha del producto | 2 | 1 | 2 | 2 | 2 | 2 | **11** |
| [`V-008`](./vistas/V-008-carrito.md) | Carrito | 2 | 1 | 2 | 2 | 2 | 2 | **11** |
| [`V-009`](./vistas/V-009-favoritos.md) | Favoritos | 2 | 0 | 2 | 1 | 2 | 1 | **8** |
| [`V-010`](./vistas/V-010-direccion-envio.md) | Dirección de envío | 2 | 2 | 2 | 2 | 2 | 0 | **10** |
| [`V-011`](./vistas/V-011-resumen-envio-beneficio.md) | Resumen, envío y beneficio | 2 | 1 | 2 | 2 | 2 | 1 | **10** |
| [`V-012`](./vistas/V-012-pago-simulado.md) | Pago simulado | 1 | 1 | 2 | 1 | 2 | 0 | **7** |
| [`V-013`](./vistas/V-013-creacion-orden.md) | Creación de orden | 2 | 2 | 2 | 1 | 2 | 0 | **9** |
| [`V-014`](./vistas/V-014-pedido-confirmado.md) | Pedido confirmado | 1 | 0 | 2 | 1 | 1 | 1 | **6** |
| [`V-015`](./vistas/V-015-historial-pedidos.md) | Historial de pedidos | 2 | 1 | 2 | 2 | 2 | 1 | **10** |
| [`V-016`](./vistas/V-016-detalle-reordenado.md) | Detalle y reordenado | 2 | 0 | 2 | 2 | 2 | 1 | **9** |
| [`V-017`](./vistas/V-017-seguimiento.md) | Seguimiento | 1 | 0 | 2 | 2 | 2 | 0 | **7** |
| **Subtotal vistas** | — | — | — | — | — | — | — | **145** |

## 4. Estimación de overlays

| ID | Overlay | L | F | E | R | I | D | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| [`O-001`](./overlays/O-001-filtros-mobile.md) | Filtros mobile | 1 | 2 | 2 | 2 | 2 | 1 | **10** |
| [`O-002`](./overlays/O-002-visor-galeria.md) | Visor de galería | 1 | 0 | 2 | 2 | 2 | 0 | **7** |
| [`O-003`](./overlays/O-003-autenticacion-requerida.md) | Autenticación requerida | 1 | 0 | 2 | 1 | 2 | 1 | **7** |
| [`O-004`](./overlays/O-004-confirmacion-cierre-checkout.md) | Confirmar cierre de checkout | 1 | 0 | 2 | 1 | 1 | 0 | **5** |
| [`O-005`](./overlays/O-005-producto-agregado-carrito.md) | Producto agregado | 0 | 0 | 1 | 1 | 1 | 0 | **3** |
| [`O-006`](./overlays/O-006-deshacer-eliminacion.md) | Deshacer eliminación | 0 | 0 | 2 | 1 | 2 | 1 | **6** |
| [`O-007`](./overlays/O-007-resultado-fusion-carrito.md) | Resultado de fusión | 1 | 0 | 2 | 1 | 1 | 0 | **5** |
| [`O-008`](./overlays/O-008-resultado-reordenado.md) | Resultado de reordenado | 1 | 0 | 2 | 1 | 1 | 0 | **5** |
| [`O-009`](./overlays/O-009-evaluacion-postentrega.md) | Evaluación postentrega | 1 | 2 | 2 | 2 | 2 | 0 | **9** |
| [`O-010`](./overlays/O-010-alertas-feedback-global.md) | Alertas y feedback global | 1 | 0 | 2 | 2 | 2 | 2 | **9** |
| **Subtotal overlays** | — | — | — | — | — | — | — | **66** |

## 5. Estimación de comunicaciones

| ID | Comunicación | L | F | E | R | I | D | Total |
|---|---|---:|---:|---:|---:|---:|---:|---:|
| [`C-001`](./comunicaciones/C-001-correo-confirmacion-pedido.md) | Confirmación de pedido | 2 | 0 | 2 | 2 | 1 | 1 | **8** |
| [`C-002`](./comunicaciones/C-002-correo-actualizacion-despacho.md) | Actualización de despacho | 1 | 0 | 2 | 2 | 1 | 1 | **7** |
| **Subtotal comunicaciones** | — | — | — | — | — | — | — | **15** |

## 6. Carga total

| Concepto | Puntos |
|---|---:|
| 17 vistas | 145 |
| 10 overlays | 66 |
| 2 comunicaciones | 15 |
| Gobernanza de `DS-001` y biblioteca compartida | 4 |
| **Total para reparto** | **230** |

La reserva de 4 puntos de gobernanza no representa un frame aislado: cubre revisión de componentes/tokens, resolución de inconsistencias visuales y control de la biblioteca compartida.

## 7. Reparto equilibrado propuesto

| Integrante | Entregables | Visual | Gobernanza | Total |
|---|---|---:|---:|---:|
| **Giuliano Macchiavello** | `V-001`–`V-004`, `O-003`, `O-004`, `C-001`; custodia de `DS-001` | 45 | 4 | **49** |
| **Fernando José Saire Tello** | `V-005`–`V-007`, `O-002`, `O-010` | 49 | 0 | **49** |
| **Sebastián Malca** | `V-008`, `V-009`, `O-001`, `O-005`–`O-007` | 43 | 0 | **43** |
| **Jim Segovia** | `V-010`–`V-014` | 42 | 0 | **42** |
| **Diego Espinoza** | `V-015`–`V-017`, `O-008`, `O-009`, `C-002` | 47 | 0 | **47** |
| **Total** | 29 entregables + gobernanza | **226** | **4** | **230** |

### Verificación de equilibrio

- Carga mínima: 42 puntos.
- Carga máxima: 49 puntos.
- Diferencia absoluta: 7 puntos.
- Diferencia conservadora respecto a la carga mínima: `7 / 42 = 16.7 %`.
- Promedio: 46 puntos; desviación máxima respecto al promedio: 4 puntos (`8.7 %`).

El reparto cumple el umbral del plan: la diferencia entre carga máxima y mínima es menor al 20 %. La asignación mantiene flujos completos; `O-001`, `O-010` y `C-001` se ubican donde equilibran carga y refuerzan responsabilidades reutilizables.

## 8. Dependencias de trabajo compartido

| Dueño | Entregable compartido | Consumidores |
|---|---|---|
| Giuliano | `DS-001`, marca y correo `C-001` | Los cinco paquetes |
| Fernando | `ProductCard`, galería y patrón global `O-010` | Inicio, catálogo, producto, carrito y favoritos |
| Sebastián | Filtros mobile `O-001`, feedback de carrito | `V-006`, `V-008`, `V-009`, `V-015` |
| Jim | Progreso y resumen de checkout | `V-010`–`V-014` y consistencia con `V-008` |
| Diego | Timeline, postentrega y correo `C-002` | `V-014`–`V-017` |

Los componentes compartidos se definen una vez en la biblioteca y se consumen como instancias. Cualquier cambio que afecte a otro paquete se registra en la spec y se coordina con su revisor.

## 9. Estado del reparto

El inventario, la estimación, los responsables/revisores y los cinco paquetes individuales están listos en [`reparto/`](./reparto/README.md). Antes de comenzar mockups finales todavía se requiere:

1. que cada integrante acepte su paquete y revisor;
2. resolver o clasificar las decisiones abiertas como bloqueantes/no bloqueantes;
3. colocar los enlaces finales de Figma al iniciar cada grupo de frames;
4. realizar la revisión cruzada definida en el plan.
