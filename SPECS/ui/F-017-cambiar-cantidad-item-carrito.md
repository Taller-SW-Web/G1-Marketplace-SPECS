# Spec UI — F-017 Cambiar la cantidad de un ítem

En `/carrito`, cada línea usa `QuantityStepper`: disminuir, campo numérico accesible y aumentar. El mínimo es 1; al llegar a 1, disminuir queda deshabilitado y eliminar se realiza mediante F-018.

| Estado | Interfaz |
|---|---|
| Actualizando | Línea conserva contexto y muestra indicador local. |
| Ajustado | Cantidad confirmada y aviso breve del máximo disponible. |
| Agotado | Texto “Ya no está disponible” y acción Quitar. |
| Error | Restaura cantidad confirmada anterior y muestra Reintentar. |

Campo admite sólo enteros; al perder foco o confirmar se valida. Controles de 44 px, etiqueta “Cantidad de {producto}”, foco y anuncio de subtotal actualizado.

- [ ] **UI-F017-01:** El usuario distingue valor solicitado de cantidad confirmada tras un ajuste.
- [ ] **UI-F017-02:** Es posible operar por teclado sin depender de `+`/`-` visuales.
