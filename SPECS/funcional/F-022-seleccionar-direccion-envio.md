# Spec funcional — F-022 Capturar o seleccionar dirección de envío

| Campo | Valor |
|---|---|
| ID | `F-022` |
| Estado | Aprobada para planificación; contrato de Seguridad confirmado. |

Permite a un cliente autenticado seleccionar una dirección existente o registrar una nueva para el checkout. Seguridad y Usuarios conserva la dirección; Marketplace sólo usa `addressId` y una copia transitoria para cotizar/enviar a Ventas.

- **RN-F022-01:** Checkout requiere sesión; no hay dirección de invitado en el alcance inicial.
- **RN-F022-02:** Sólo se listan/crean direcciones del titular derivado del JWT; nunca se acepta un `userId` manipulable.
- **RN-F022-03:** Una dirección válida requiere calle/avenida, departamento, provincia, distrito, referencia opcional y teléfono de contacto según contrato de Seguridad.
- **RN-F022-04:** Seleccionar no persiste una tabla local ni modifica una dirección existente.

- [ ] **CA-F022-01:** El cliente puede usar una dirección propia guardada o registrar una nueva y seleccionarla.
- [ ] **CA-F022-02:** Una dirección de otro titular no puede consultarse ni elegirse.
- [ ] **CA-F022-03:** Error de Seguridad preserva el formulario y no avanza a cotización.

Fuente: OpenAPI de Seguridad, `GET/POST /usuarios/{id}/direcciones`; Marketplace usa BFF y JWT.
