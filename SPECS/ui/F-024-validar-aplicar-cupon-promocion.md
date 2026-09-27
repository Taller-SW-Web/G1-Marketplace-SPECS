# Spec UI — F-024 Cupón o promoción

En `/checkout/resumen`, campo “Código de cupón”, botón Aplicar y bloque de beneficio. Promociones automáticas se muestran separadas de cupón manual; sólo el beneficio elegido se refleja en total.

| Estado | Interfaz |
|---|---|
| Sin cupón | Campo, ayuda y promociones automáticas si existen. |
| Validando | Botón ocupado y campo bloqueado temporalmente. |
| Aplicado | Código parcialmente visible, ahorro y Quitar. |
| No aplicable | Mensaje neutral, sin revelar límites de otros clientes. |
| Vencido/cambió | Aviso y acción Recalcular. |

Errores se vinculan al campo; no se usa sólo color. Quitar cupón recalcula y no afirma restitución porque aún no fue consumido.

- [ ] **UI-F024-01:** El cliente distingue promoción automática de cupón ingresado.
