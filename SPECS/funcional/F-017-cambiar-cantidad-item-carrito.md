# Spec funcional — F-017 Cambiar la cantidad de un ítem

| Campo | Valor |
|---|---|
| ID | `F-017` |
| Estado | Aprobada para planificación; integración condicionada por `I-01`. |

Permite cambiar explícitamente la cantidad de una línea existente. Incluye aumentar, reducir, validar el máximo y recalcular el snapshot informativo; excluir cantidad cero (es F-018), reserva y checkout.

- **RN-F017-01:** Cantidad es entero de 1 a 99; la consulta de estado comercial actual no confirma que haya N unidades. La validación cuantitativa requiere contrato `X-P0-03`.
- **RN-F017-02:** El cambio es absoluto, no relativo: reintentos concurrentes no suman dos veces.
- **RN-F017-03:** Sólo si Productos devuelve un máximo comercial contractual puede Marketplace proponer un ajuste de cantidad. Si el SKU pasa a `AGOTADO`, conserva la línea para que F-018 permita retirarla explícitamente y la marca no comprable. No infiere un máximo desde `STOCK_BAJO` o `DISPONIBLE`.
- **RN-F017-04:** Cada cambio refresca precio snapshot y aumenta `Cart.version` transaccionalmente.

- [ ] **CA-F017-01:** Cambiar 1 a 3 deja exactamente 3 unidades.
- [ ] **CA-F017-02:** Cantidad inválida no modifica la línea.
- [ ] **CA-F017-03:** La mutación no consume inventario.
- [ ] **CA-F017-04:** La UI no presenta una cantidad del carrito como stock reservado o garantizado.
