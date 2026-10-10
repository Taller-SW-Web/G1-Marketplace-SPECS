# Spec UI — F-026 Crear la orden en Ventas

En `/checkout/confirmacion`, tras registrar consentimiento y preparar el checkout, se muestran campos de contacto faltantes y botón “Crear pedido”. Documento usa selector `DNI/RUC/CE/PASAPORTE` con reglas visibles; no se muestra si ya fue resuelto desde perfil autorizado. Crear el pedido puede dejarlo temporalmente en `CREADO`; aún se debe verificar aptitud para pagar y confirmación simulada mediante Ventas.

| Estado | Interfaz |
|---|---|
| Listo | Resumen final, contacto y CTA. |
| Enviando | CTA no repetible, mensaje “Estamos registrando tu pedido”. |
| Preparación transaccional | Pedido `CREADO`, reserva/cupón o aptitud para pagar pendientes; muestra progreso y conserva operación original, sin check de compra confirmada. |
| Éxito | Sólo `PAGADO` confirmado por Ventas deriva a F-027. |
| Resultado incierto | “Estamos verificando tu pedido”; no invita a repetir como nueva compra. |
| Error validable | Mantiene campos y marca sólo los inválidos. |

No se muestran tokens, request IDs ni errores internos. Los campos siguen asociaciones accesibles y el foco llega al primer error o a la confirmación.

- [ ] **UI-F026-01:** El usuario no puede disparar dos envíos desde el CTA.
- [ ] **UI-F026-02:** `CREADO` y una confirmación simulada incierta muestran espera/verificación, no éxito ni una segunda compra.
