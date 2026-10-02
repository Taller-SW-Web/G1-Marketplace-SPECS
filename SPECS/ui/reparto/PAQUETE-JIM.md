# Paquete de Jim — checkout

## 1. Control del paquete

| Campo | Valor |
|---|---|
| Responsable | Jim Segovia |
| Revisor principal | Leonidas Garcia |
| Sistema de diseño | [`DS-001` v0.2.0](../DS-001-sistema-diseno-marketplace.md) |
| Carpeta de mockups en Figma | [Marketplace — vistas](https://www.figma.com/files/team/1686774887312660587/folder/662579480?fuid=1686774885834417394); enlace directo al archivo y a los frames pendiente |
| Alcance | 5 vistas del flujo completo de checkout |
| Carga | **42 puntos** |
| Estado | Preparado para aceptación del integrante |

## 2. Entregables

| Orden | Spec | Resultado | Puntos |
|---:|---|---|---:|
| 1 | [`V-010` Dirección de envío](../vistas/V-010-direccion-envio.md) | Selección/alta de dirección | 10 |
| 2 | [`V-011` Resumen, envío y beneficio](../vistas/V-011-resumen-envio-beneficio.md) | Cotización, cupón y cobertura | 10 |
| 3 | [`V-012` Pago simulado](../vistas/V-012-pago-simulado.md) | Preparación de una operación sin tarjeta | 7 |
| 4 | [`V-013` Creación de orden](../vistas/V-013-creacion-orden.md) | Confirmación final e incertidumbre transaccional | 9 |
| 5 | [`V-014` Pedido confirmado](../vistas/V-014-pedido-confirmado.md) | Resultado y siguientes pasos | 6 |
| **Total** | — | — | **42** |

## 3. Frames exactos

### `V-010`

- `V-010 / Desktop / Con direcciones`
- `V-010 / Mobile / Con direcciones`
- `V-010 / Desktop / Sin direcciones`
- `V-010 / Mobile / Nueva dirección`
- `V-010 / Desktop / Validación`
- `V-010 / Mobile / Guardando`
- `V-010 / Desktop / Servicio no disponible`
- `V-010 / Mobile / Carrito inválido`

### `V-011`

- `V-011 / Desktop / Cotizado`
- `V-011 / Mobile / Cotizado`
- `V-011 / Desktop / Calculando`
- `V-011 / Mobile / Promoción automática`
- `V-011 / Desktop / Cupón aplicado`
- `V-011 / Mobile / Cupón no aplicable`
- `V-011 / Desktop / Cotización vencida`
- `V-011 / Mobile / Sin cobertura`
- `V-011 / Desktop / Línea no disponible`
- `V-011 / Mobile / Error de cotización`

### `V-012`

- `V-012 / Desktop / Listo`
- `V-012 / Mobile / Listo`
- `V-012 / Desktop / Procesando`
- `V-012 / Mobile / Preparado`
- `V-012 / Desktop / Cotización vencida`
- `V-012 / Mobile / Stock no disponible`
- `V-012 / Desktop / Revalidación cambió`
- `V-012 / Mobile / Error recuperable`

### `V-013`

- `V-013 / Desktop / Listo sin campos`
- `V-013 / Mobile / Campos faltantes`
- `V-013 / Desktop / Validación`
- `V-013 / Mobile / Enviando`
- `V-013 / Desktop / Resultado incierto`
- `V-013 / Mobile / Operación no preparada`
- `V-013 / Desktop / Ventas no disponible`

### `V-014`

- `V-014 / Desktop / Confirmado`
- `V-014 / Mobile / Confirmado`
- `V-014 / Desktop / Cargando`
- `V-014 / Mobile / Verificación en curso`
- `V-014 / Desktop / Creación fallida`
- `V-014 / Mobile / Pedido no accesible`
- `V-014 / Desktop / Error de consulta`

## 4. Dependencias compartidas

- Alinear con Sebastián el resumen de carrito, disponibilidad, cambios de cantidad y transición a checkout.
- Coordinar `O-004` con Giuliano para salida segura de las etapas editables o transaccionales.
- El resumen de pedido y la identidad de la orden deben reutilizarse en `C-001`, `V-015` y `V-016`.
- Coordinar con Diego la transición desde `V-014` hacia historial, detalle y seguimiento.
- No diseñar campos de tarjeta o CVV: F-025 define un pago simulado sin captura de tarjeta.

## 5. Decisiones abiertas que deben revisarse

| Entregable | IDs |
|---|---|
| `V-010` | `V-010-OPEN-01` a `V-010-OPEN-04` |
| `V-011` | `V-011-OPEN-01` a `V-011-OPEN-04` |
| `V-012` | `V-012-OPEN-01` a `V-012-OPEN-04` |
| `V-013` | `V-013-OPEN-01` a `V-013-OPEN-04` |
| `V-014` | `V-014-OPEN-01` a `V-014-OPEN-04` |

## 6. Orden de ejecución recomendado

**Secuencia actual (2026-10-01):** Jim está diseñando primero las variantes desktop de `V-010` a `V-014`. Las variantes mobile se trabajarán después y permanecen dentro del alcance del paquete. Los nuevos frames desktop de estados ya descritos en las specs se incorporarán a la sección 12 de cada vista y se enlazarán individualmente cuando estén definidos en Figma. Esta secuencia no equivale a aprobar los mockups ni a cerrar las decisiones abiertas.

1. Definir el shell de checkout, indicador de progreso y resumen persistente.
2. Diseñar `V-010` y validar edición, guardado y errores.
3. Diseñar `V-011` para fijar cotización, promoción, cupón y cobertura.
4. Diseñar `V-012` y `V-013` juntos por su continuidad transaccional.
5. Diseñar `V-014` y coordinar continuidad con Diego y correo con Giuliano.
6. Completar enlaces de Figma y solicitar revisión de Leonidas.

## 7. Definition of Ready del paquete

- [ ] Jim acepta alcance, carga y revisor.
- [ ] Las decisiones abiertas bloqueantes están resueltas o tienen supuesto aprobado.
- [ ] Shell, progreso, resumen y bloque de orden son componentes reutilizables.
- [ ] Todos los frames de la sección 3 existen con esos nombres exactos.
- [ ] Cada spec enlaza su sección o frame de Figma.
- [ ] Cálculo, validación, incertidumbre, regreso seguro, foco y responsive fueron comprobados.
- [ ] Leonidas revisó el paquete y Jim cerró las observaciones.
