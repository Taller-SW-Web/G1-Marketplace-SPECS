# Spec UI — F-026 Crear la orden en Ventas

En `/checkout/confirmacion`, tras registrar consentimiento y preparar el checkout, se muestran campos de contacto faltantes y botón “Crear pedido”. Documento usa selector `DNI/RUC/CE/PASAPORTE` con reglas visibles; no se muestra si ya fue resuelto desde perfil autorizado. Ventas responde `CREADO` con reserva y cupón confirmados, inicia su simulador y Marketplace consulta el estado hasta `PAGADO` o `ANULADO`.

| Estado | Interfaz |
|---|---|
| Listo | Resumen final, contacto y CTA. |
| Enviando | CTA no repetible, mensaje “Estamos registrando tu pedido”. |
| Simulación en curso | Pedido `CREADO` con reserva/cupón confirmados; muestra progreso y conserva operación original, sin check de compra confirmada. |
| Éxito | Sólo `PAGADO` confirmado por Ventas deriva a F-027. |
| Resultado incierto | “Estamos verificando tu pedido”; no invita a repetir como nueva compra. |
| Pago rechazado | Pedido `ANULADO` por `PAGO_NO_COMPLETADO`; explica el resultado y ofrece una salida segura, sin reutilizar la operación fallida. |
| Error validable | Mantiene campos y marca sólo los inválidos. |

No se muestran tokens, request IDs ni errores internos. Los campos siguen asociaciones accesibles y el foco llega al primer error o a la confirmación.

- [ ] **UI-F026-01:** El usuario no puede disparar dos envíos desde el CTA.
- [ ] **UI-F026-02:** `CREADO` y una confirmación simulada incierta muestran espera/verificación, no éxito ni una segunda compra.
