# Repartición de implementación punta a punta — siete integrantes

Asignación y estimación base decididas por Jim Segovia, PO, el 13/10/2026; no requieren aceptación individual previa. La interpretación académica se consultará al profesor. La [matriz de SPECS](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) es el índice vigente de los **ocho bloques del sílabo**, F-001–F-040, responsables, revisores, vistas y gates. Esta decisión **no acredita ejecución**. Los roles del [README principal](../../README.md#equipo) permanecen. La distribución de mockups en [inventario visual](../../SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md) describe diseño, no ownership de implementación.

| Integrante | Bloque/F bajo ownership | Revisor principal | Paquete individual |
|---|---|---|---|
| Jim Bryan Segovia Valencia | Cuenta y acceso, F-001–F-005 | Andres Morales | [Jim](JIM-SEGOVIA-VALENCIA.md) |
| Giuliano Macchiavello Perez | Catálogo y búsqueda, F-006–F-010 | Sebastian Malca | [Giuliano](GIULIANO-MACCHIAVELLO-PEREZ.md) |
| Sebastian Matias Malca Agüero | Detalle de producto, F-011–F-015 | Giuliano Macchiavello | [Sebastian](SEBASTIAN-MALCA-AGUERO.md) |
| Andres Fernando Morales Usca | Carrito, F-016–F-021 | Leonidas Garcia | [Andres](ANDRES-MORALES-USCA.md) |
| Leonidas Garcia Lescano | Checkout, F-022–F-027 | Diego Espinoza | [Leonidas](LEONIDAS-GARCIA-LESCANO.md) |
| Fernando Jose Saire Tello | Pedidos/seguimiento F-028–F-032 y notificaciones F-033–F-035 | Jim Segovia | [Fernando](FERNANDO-SAIRE-TELLO.md) |
| Diego Steven Martin Espinoza Picon | Favoritos F-036–F-039; adicional F-040 evaluación postentrega | Fernando Saire | [Diego](DIEGO-ESPINOZA-PICON.md) |

Fernando asume dos bloques relacionados porque notificaciones y seguimiento comparten el estado de pedido/Despacho. La estimación base y los apoyos constan en la matriz; esta agrupación **no es una exigencia confirmada del profesor**. F-040 es capacidad adicional, no noveno bloque del sílabo. Cada persona debe producir FE+BE propio en al menos un corte, además de sus tareas transversales de PO, JP, UX/UI, arquitectura, DevOps, documentación o QA/cloud.

## H3: un gate común y siete evidencias individuales

**Ruta crítica inalterada:** F-006/F-007 → V-005 Inicio + búsqueda mínima V-006 → frontend desplegado → BFF Marketplace → API **real** de Productos. Datos visibles, carga/vacío/error/timeout, URL FE/BE, respuesta intermodular sanitizada, código y diagrama conforme al despliegue. Giuliano es dueño del bloque; Sebastian aporta integración de V-006 y tarjeta, Leonidas revisa el BFF, Andres despliega, Fernando ejecuta smoke, Diego verifica y Jim acepta. Colaborar no transfiere ownership de F-006/F-007.

Cada paquete personal define además un **avance vertical parcial** del bloque propio que puede arrancar en semana 8, con UI, backend Marketplace, positivo/negativo y evidencia individual. Jim: sesión; Sebastian: detalle; Andres: carrito; Diego: favoritos; Leonidas: resumen; Fernando: historial. Estos seis cortes pueden usar fixture local rotulado `MOCK`; no se prometen ocho flujos integrados en H3. Para funcionalidades cuyo cierre sigue en S2–S5, el corte H3 se registra como preparación vinculada a sus TASK-ID, sin adelantar la semana objetivo ni mover el estado a Terminado. Giuliano sí debe intentar prueba REAL de Productos para el gate común. Si Productos no publica URL/token/datos, I-01 y las INT siguen bloqueadas y la demo se presenta como parcial.

## Secuencia y límites de integración

1. Jim confirma contrato/versión, entorno, credenciales técnicas y datos de Productos; registra I-01. Ningún equipo programa endpoint ajeno por suposición.
2. Andres audita base FE/BE, Prisma y Render, prepara CI/entornos y coordina deploy. Leonidas revisa arquitectura del BFF y secretos; Giuliano integra el catálogo. El backend Marketplace existente no equivale a BFF completo.
3. Los demás autores construyen sus cortes verticales **aislados** con fixtures sanitizados y tareas propias, sin exponer acciones incompletas como activas en la demo pública. Cada uno registra revisión de PR, IA y pruebas.
4. Diego/Jim verifican dependencias y evidencia, priorizan la ruta histórica H3, verifican web→BFF→Productos desde fuera del equipo y mantienen gates abiertos donde falta prueba. F-006/F-007 sólo pasan a terminadas tras DoD completo.
5. S2–S5 mantienen los mismos owners y revisores. Cada iteración valida contrato externo, entorno, progreso y evidencia; si una frontera queda bloqueada, se registra por operación sin borrar IDs ni rebautizar mocks como integraciones.

Leer la [guía colaborativa](GUIA-DE-TRABAJO-COLABORATIVO.md) antes de abrir ramas o PR. Los paquetes personales son instrucciones prácticas; las cuatro specs F-### siguen siendo fuente de comportamiento, UI, API y React.

## Entregas y responsabilidades H4

[S02](../iteraciones/S02-semanas-09-11.md) fija 25 cierres objetivo: Jim 5 (F-001–005), Giuliano 5 (F-006–010), Sebastian 5 (F-011–015), Andres 6 (F-016–021), Diego 4 (F-036–039). Leonidas implementa/prueba sus 6 F-022–027; Fernando sus 8 F-028–035; Diego además F-040 en su parte propia G1. Estos 15 cierres integrales conservan S03/S04/S05 por dependencias, aunque se adelanta código/pruebas H4.

Disponibilidad sin restricción horaria; no hay ampliaciones por tiempo. CI/guard siguen con Andres y colaboración build/deploy/runtime Fernando; API/identidad técnica Leonidas; cuenta G7 Jim; ejemplos/consumer tests Sebastian; QA/gates Diego. Se mantienen revisores y reparto visual. Toda integración y despliegue exige evidencia por F, nunca sólo contrato/mock. [Inventario completo](../ALCANCE-H4-PRODUCTOS-SEGURIDAD.md).
