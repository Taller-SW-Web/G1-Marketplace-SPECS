# Repartición de implementación punta a punta — siete integrantes

Propuesta del 13/10/2026, pendiente de estimación/aceptación individual y validación del PO/profesor. La [matriz de SPECS](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) es el índice vigente de los **ocho bloques del sílabo**, F-001–F-040, responsables, revisores, vistas y gates. Esta propuesta **no acredita ejecución**. Los roles del [README principal](../../README.md#equipo) permanecen. La distribución de mockups en [inventario visual](../../SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md) describe diseño, no ownership de implementación.

| Integrante | Bloque/F bajo ownership | Revisor principal | Paquete individual |
|---|---|---|---|
| Jim Bryan Segovia Valencia | Cuenta y acceso, F-001–F-005 | Andres Morales | [Jim](JIM-SEGOVIA-VALENCIA.md) |
| Giuliano Macchiavello Perez | Catálogo y búsqueda, F-006–F-010 | Sebastian Malca | [Giuliano](GIULIANO-MACCHIAVELLO-PEREZ.md) |
| Sebastian Matias Malca Agüero | Detalle de producto, F-011–F-015 | Giuliano Macchiavello | [Sebastian](SEBASTIAN-MALCA-AGUERO.md) |
| Andres Fernando Morales Usca | Carrito, F-016–F-021 | Leonidas Garcia | [Andres](ANDRES-MORALES-USCA.md) |
| Leonidas Garcia Lescano | Checkout, F-022–F-027 | Diego Espinoza | [Leonidas](LEONIDAS-GARCIA-LESCANO.md) |
| Fernando Jose Saire Tello | Pedidos/seguimiento F-028–F-032 y notificaciones F-033–F-035 | Jim Segovia | [Fernando](FERNANDO-SAIRE-TELLO.md) |
| Diego Steven Martin Espinoza Picon | Favoritos F-036–F-039; adicional F-040 evaluación postentrega | Fernando Saire | [Diego](DIEGO-ESPINOZA-PICON.md) |

Fernando asume dos bloques relacionados porque notificaciones y seguimiento comparten el estado de pedido/Despacho. La carga y apoyos se estiman antes de S3; esta agrupación **no es una exigencia confirmada del profesor**. F-040 es capacidad adicional, no noveno bloque del sílabo. Cada persona debe producir FE+BE propio en al menos un corte, además de sus tareas transversales de PO, JP, UX/UI, arquitectura, DevOps, documentación o QA/cloud.

## H3: un gate común y siete evidencias individuales

**Ruta crítica inalterada:** F-006/F-007 → V-005 Inicio + búsqueda mínima V-006 → frontend desplegado → BFF Marketplace → API **real** de Productos. Datos visibles, carga/vacío/error/timeout, URL FE/BE, respuesta intermodular sanitizada, código y diagrama conforme al despliegue. Giuliano es dueño del bloque; Sebastian aporta integración de V-006 y tarjeta, Leonidas revisa el BFF, Andres despliega, Fernando ejecuta smoke, Diego verifica y Jim acepta. Colaborar no transfiere ownership de F-006/F-007.

Cada paquete personal define además un **avance vertical parcial** del bloque propio que puede arrancar en semana 8, con UI, backend Marketplace, positivo/negativo y evidencia individual. Jim: sesión; Sebastian: detalle; Andres: carrito; Diego: favoritos; Leonidas: resumen; Fernando: historial. Estos seis cortes pueden usar fixture local rotulado `MOCK`; no se prometen ocho flujos integrados en H3. Para funcionalidades cuyo cierre sigue en S2–S5, el corte H3 se registra como preparación vinculada a sus TASK-ID, sin adelantar la semana objetivo ni mover el estado a Terminado. Giuliano sí debe intentar prueba REAL de Productos para el gate común. Si Productos no publica URL/token/datos, I-01 y las INT siguen bloqueadas y la demo se presenta como parcial.

## Secuencia y límites de integración

1. Jim confirma contrato/versión, entorno, credenciales técnicas y datos de Productos; registra I-01. Ningún equipo programa endpoint ajeno por suposición.
2. Andres audita base FE/BE, Prisma y Render, prepara CI/entornos y coordina deploy. Leonidas revisa arquitectura del BFF y secretos; Giuliano integra el catálogo. El backend Marketplace existente no equivale a BFF completo.
3. Los demás autores construyen sus cortes verticales **aislados** con fixtures sanitizados y tareas propias, sin exponer acciones incompletas como activas en la demo pública. Cada uno registra revisión de PR, IA y pruebas.
4. Diego/Jim comparan estimaciones con capacidad, priorizan la ruta H3, verifican web→BFF→Productos desde fuera del equipo y mantienen gates abiertos donde falta prueba. F-006/F-007 sólo pasan a terminadas tras DoD completo.
5. S2–S5 mantienen los mismos owners y revisores. Cada iteración valida capacidad, contrato externo, progreso y evidencia; si no cabe un hito, se resecuencia por decisión documentada sin borrar IDs ni rebautizar mocks como integraciones.

Leer la [guía colaborativa](GUIA-DE-TRABAJO-COLABORATIVO.md) antes de abrir ramas o PR. Los paquetes personales son instrucciones prácticas; las cuatro specs F-### siguen siendo fuente de comportamiento, UI, API y React.
