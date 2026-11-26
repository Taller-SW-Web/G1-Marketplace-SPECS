# Diapositiva 1 · ¿Qué se pedía?

- **Gateway:** demostrar con tráfico y trazas JWT, rate limit, caché y correlación hasta el BFF. Versionar el XML de la revisión aplicada.
- **Asíncrono:** demostrar recepción, deduplicación, reintento con espera y recuperación para cada intercambio. No confundir un ensayo aislado con evidencia intermodular.

---

# Diapositiva 2 · Arquitectura

| Camino | Componentes |
|---|---|
| API | Frontend → APIM `/v1` → BFF. APIM valida JWT, aplica el límite y usa Redis en rutas públicas habilitadas. El paso del FE por APIM se verifica aparte. |
| Seguridad | G7 → RabbitMQ → consumidor del BFF → inbox PostgreSQL. ACK tras persistir o reconocer un duplicado. |
| Envíos | Despacho → Ventas → webhook H-05 → inbox PostgreSQL. Respuesta `200` al aceptar; el ensayo de fallo del receptor devuelve `503`. |

[Diagramas de secuencia y caminos de fallo](H5-PUNTO-4-EVIDENCIA.md#a--seguridad-g7--rabbitmq--marketplace)

---

# Diapositiva 3 · ¿Qué demuestra cada prueba?

| Política o escenario | Resultado al corte | Evidencia |
|---|---|---|
| JWT ausente / inválido | **REAL histórico:** `401` sin token, 25/11 `02:57:35.767 UTC`. Inválido **NOT_RUN**. | [Log](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/45536575477/job/138944541668) |
| Rate limit | **NOT_RUN:** falta `429` y `Retry-After`. | [#394](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/394#issuecomment-7204628542) |
| Caché | **Reportado:** `200/MISS` → `200/HIT` en docs. Falta traza con hora. | [Matriz APIM](H5-PUNTO-4-EVIDENCIA.md#apim--política--prueba--resultado--enlace) |
| Correlación | **NOT_RUN** APIM → BFF. El smoke histórico solo cotejó cabeceras. | [Log parcial](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/45536575477/job/138944541668) |
| Seguridad | **LAB LOCAL:** duplicado, backoff/DLQ y reconexión. Recepción de esta ronda **NOT_RUN**. | [#317](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/317#issuecomment-7203197884) |
| Envíos | **REAL reportado:** siete eventos. **LAB / CI:** deduplicación y `503` sin fila → `200` con una fila. | [REAL #318](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/318#issuecomment-7202913749) · [CI #399](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/actions/runs/45899560721/job/140181721101) |

---

# Diapositiva 4 · Límites del resultado

- **APIM:** el XML de Git no acredita la revisión activa. Quedan export, evidencias por política y el salto FE → APIM. No atribuir `HIT` de docs a catálogo.
- **Seguridad:** la recepción REAL de un evento no acredita backoff, reconexión ni bloqueo de una cuenta. Bloqueo se coteja aparte en #316.
- **Envíos:** siete IDs únicos no demuestran `duplicate:true`. Un reintento tras `503` no demuestra una política de backoff ni recuperación de una caída completa. #320 se limita a un evento sintético en QA aislado.
- **Corte:** actualizar solo filas con evidencia sanitizada antes del congelamiento; lo restante se presenta como **NOT_RUN**.

[Paquete de evidencia y próximos pasos](H5-PUNTO-4-EVIDENCIA.md)
