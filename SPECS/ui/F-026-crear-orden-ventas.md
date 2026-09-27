# Spec UI — F-026 Crear la orden en Ventas

En `/checkout/confirmacion`, tras pago simulado preparado, se muestran campos de contacto faltantes y botón “Crear pedido”. Documento usa selector `DNI/RUC/CE/PASAPORTE` con reglas visibles; no se muestra si ya fue resuelto desde perfil autorizado.

| Estado | Interfaz |
|---|---|
| Listo | Resumen final, contacto y CTA. |
| Enviando | CTA no repetible, mensaje “Estamos registrando tu pedido”. |
| Éxito | Deriva a F-027. |
| Resultado incierto | “Estamos verificando tu pedido”; no invita a repetir como nueva compra. |
| Error validable | Mantiene campos y marca sólo los inválidos. |

No se muestran tokens, request IDs ni errores internos. Los campos siguen asociaciones accesibles y el foco llega al primer error o a la confirmación.

- [ ] **UI-F026-01:** El usuario no puede disparar dos envíos desde el CTA.
