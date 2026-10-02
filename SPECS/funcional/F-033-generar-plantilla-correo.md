# Spec funcional — F-033 Generar plantilla de correo

| Campo | Valor |
|---|---|
| ID | `F-033` |
| Estado | Aprobada para planificación. |

Genera una representación versionada de correo para confirmación de pedido o cambio de despacho. Incluye datos mínimos del evento, enlaces seguros y recomendaciones opcionales; excluye enviar correo y perfil de marketing.

- **RN-F033-01:** Usa snapshot de pedido/evento autorizado; no consulta dirección/documento para cuerpo.
- **RN-F033-02:** Recomendaciones son opcionales; su fallo no bloquea plantilla.
- **RN-F033-03:** Enlaces usan sólo identificador opaco y requieren autenticación; no incluyen tokens/PII.
- **RN-F033-04:** `payloadVersion` permite render consistente de un hecho.

- [ ] **CA-F033-01:** Fallo de recomendados conserva correo válido.
