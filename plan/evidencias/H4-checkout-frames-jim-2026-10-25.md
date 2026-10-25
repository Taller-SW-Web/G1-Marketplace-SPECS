# H4 Checkout — evidencia de frames de Jim (25/10/2026)

## Alcance y base

Trabajo de diseño para [Frontend #99](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/99), [#100](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/100) y [#101](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/101). Se partió de SPECS `main` en `a2a04b0` y se revisó Frontend `develop` en `d1f5c06`. No se modificó código de Frontend, ramas de compañeros ni sus PR. La maqueta usa datos de ejemplo y no prueba un pedido real, un despliegue ni integración con Ventas o G7.

## Evidencia verificable en Figma

| Issue | Frame directo | Comprobación estructural y visual |
|---|---|---|
| #99 | [V-011 / Mobile / Promoción automática](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=528-1644) | Frame exacto de 390 px; promoción «Club Atleta» automática por −S/ 16.00, cupón manual sin aplicar, subtotal S/ 440.00, envío S/ 15.00 y **total estimado** S/ 439.00. Vigencia y CTA aparecen después del desglose. Captura completa inspeccionada sin recortes ni solapamientos visibles. |
| #100 | [V-013 / Mobile / Operación no preparada](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=528-1696) | Frame exacto de 390 px; «NO PODEMOS CREAR TU PEDIDO» y «Operación no preparada». Acción «Revisar resumen» con retorno seguro a V-011; no hay CTA «Crear pedido», título de éxito ni afirmación de compra confirmada. Captura completa inspeccionada sin recortes ni solapamientos visibles. |
| #101 | [V-014 / Desktop / Confirmado](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=420-6225) · [V-014 / Mobile / Confirmado](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups?node-id=447-7752) | En ambos frames se leyó `PAGADO`, «Ventas verificó el estado PAGADO» y «Pago simulado confirmado por Ventas». No aparece `CREADO` ni «Pago simulado aprobado» en el texto de estos frames. Ambos conservan código, total confirmado, aviso «Te enviaremos…» y acciones «Ver mi pedido» / «Seguir comprando». Capturas completas inspeccionadas sin recortes ni solapamientos visibles. |

Se inspeccionaron estructuralmente los 13 frames V-013 de la página Checkout y se sustituyeron 26 textos que afirmaban «Pago simulado aprobado» antes de la verificación de Ventas. La lectura posterior no encontró esa frase en ningún V-013. Los estados de envío y resultado incierto indican ahora que el pedido continúa en verificación. Los cuatro frames de la tabla se volvieron a leer: IDs, nombres, tamaños, textos de estado y acciones coinciden con los enlaces.

## Correspondencia con los contratos

- [V-011](../../SPECS/ui/vistas/V-011-resumen-envio-beneficio.md) y [UI F-024](../../SPECS/ui/F-024-validar-aplicar-cupon-promocion.md): promoción automática separada del cupón ingresable; sólo el beneficio seleccionado cambia el total estimado. Aplicar el cupón no implica consumo.
- [V-013](../../SPECS/ui/vistas/V-013-creacion-orden.md) y [UI F-026](../../SPECS/ui/F-026-crear-orden-ventas.md): `OPERATION_NOT_PREPARED` ofrece recuperación sin crear ni confirmar un pedido; `CREADO` o resultado incierto requieren verificación de la operación original.
- [V-014](../../SPECS/ui/vistas/V-014-pedido-confirmado.md), [F-027 funcional](../../SPECS/funcional/F-027-confirmacion-orden.md) y [UI F-027](../../SPECS/ui/F-027-confirmacion-orden.md): el éxito se representa sólo como ejemplo de `SUCCEEDED` con `orderId` y `PAGADO` verificado para el mismo pedido por Ventas. `CREADO` no se usa como evidencia de pago. El correo es asíncrono y el diseño no promete entrega inmediata ni cobro real.

## Revisión y límites

**Pendiente:** revisión de Fernando José Saire Tello (`saire22`) de los cuatro frames y de esta correspondencia antes de cerrar #99–#101. También siguen abiertos los pendientes de contrato y las pruebas de integración de cada spec. La inspección visual de Figma y la lectura del código no sustituyen la revisión independiente, pruebas del frontend en despliegue ni respuestas reales de Ventas. Este avance no depende del despliegue de Andrés ni completa la integración G7.
