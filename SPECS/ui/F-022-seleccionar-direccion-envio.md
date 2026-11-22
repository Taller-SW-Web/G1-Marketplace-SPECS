# Spec UI — F-022 Capturar o seleccionar dirección de envío

Ruta `/checkout/direccion`, sólo con sesión. Muestra tarjetas de direcciones guardadas, radio para selección y acción “Agregar nueva dirección”.

| Estado | Interfaz |
|---|---|
| Cargando | Skeleton de tarjetas. |
| Sin direcciones | Formulario abierto y explicación breve. |
| Con direcciones | Tarjeta seleccionable con nombre de referencia y dirección parcialmente visible. |
| Nueva dirección | Formulario con validación por campo; referencia opcional. |
| Error | Datos ingresados preservados y Reintentar. |

Direcciones no muestran datos más allá de lo necesario; las tarjetas se construyen con los campos de dirección del BFF y no requieren un teléfono. `fieldset`/radio accesibles, errores asociados por `aria-describedby`, y botón Continuar deshabilitado hasta selección válida.

- [ ] **UI-F022-01:** El lector anuncia qué dirección está seleccionada sin anunciar campos que la tarjeta no muestra.
- [ ] **UI-F022-02:** Los errores no borran datos válidos escritos.
