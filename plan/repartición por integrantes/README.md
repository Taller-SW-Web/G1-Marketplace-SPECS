# Repartición de desarrollo — entrega de semana 8 (H3)

Propuesta de trabajo del 2026-10-10. **Sólo cubre S1 / Hito 3**, no asigna S2–S5. Los mockups están aprobados según el PO; este documento no afirma que el software, el despliegue o la integración ya estén terminados. Cada integrante confirma disponibilidad y estimación con Jim y Diego antes de pasar su tarea a «En progreso».

## Resultado común

Entregar `V-005` inicio y el mínimo de `V-006` catálogo/búsqueda para **F-006 y F-007**: navegador → frontend Marketplace → BFF Marketplace → `GET /api/v1/productos?q=...&canal=MARKETPLACE` de Productos. Mostrar carga, resultados, vacío y error; desplegar frontend/backend y exhibir una llamada **real** entre módulos. Si Productos aún no publica URL, datos o grant `catalogo:leer`, avanzar con fixture rotulado `MOCK`, registrar I-01 y escalar el riesgo: no presentar el mock como integración H3.

El alcance H3 **no incluye** login, carrito, checkout, filtros/orden/paginación completos ni destacados inventados. En `V-006` se muestra únicamente lo que soporte el contrato de búsqueda homologado; controles de funciones futuras se omiten o se identifican como no activos, sin enlaces engañosos. `V-005` puede omitir destacados si no hay curaduría aprobada. Los estados responsive exigidos por las specs siguen dentro del trabajo, aunque los mockups desktop sean la referencia visual más avanzada.

| Integrante y rol del README vigente | Paquete personal | Aporte principal de software | Revisión principal |
|---|---|---|---|
| Leonidas Garcia Lescano — arquitecto/backend | [Leonidas](LEONIDAS-GARCIA-LESCANO.md) | BFF, rutas, adaptador de Productos y contrato | Diego |
| Andres Fernando Morales Usca — DevOps/seguridad | [Andres](ANDRES-MORALES-USCA.md) | Base backend, CI/deploy, entornos y secretos | Leonidas |
| Giuliano Macchiavello Perez — UX/UI/frontend | [Giuliano](GIULIANO-MACCHIAVELLO-PEREZ.md) | Shell visual, tokens, búsqueda compartida | Fernando |
| Sebastian Matias Malca Agüero — documentación/frontend | [Sebastian](SEBASTIAN-MALCA-AGUERO.md) | `V-006`, cliente BFF, estados y documentación técnica | Giuliano |
| Fernando Jose Saire Tello — QA/cloud | [Fernando](FERNANDO-SAIRE-TELLO.md) | `V-005`, responsive y smoke cloud | Sebastian |
| Diego Steven Martin Espinoza Picon — JP/QA | [Diego](DIEGO-ESPINOZA-PICON.md) | Pruebas automatizadas E2E, gate de calidad y coordinación | Jim |
| Jim Bryan Segovia Valencia — PO | [Jim](JIM-SEGOVIA-VALENCIA.md) | Test de contrato consumidor, aceptación y evidencia intermodular | Leonidas |

El trabajo **no se asigna por el antiguo SPEC/épica ni por el paquete de mockups**. Fernando figura como responsable de diseño de `V-005/V-006` en sus specs, pero aquí implementa `V-005`; Sebastian implementa la pantalla `V-006` y Giuliano los elementos compartidos. El PO conserva la decisión funcional; la revisión de código siempre la hace otra persona.

## Orden de integración y dependencias

1. Jim confirma con Productos versión, URL de desarrollo, datos de prueba, token/grant y semántica de `q`; Leonidas define el mapeo. Esperar su implementación no bloquea crear DTOs, fixtures y tests locales.
2. Andres prepara repositorios ejecutables, entorno, CI y deploy; Leonidas implementa rutas/adaptador BFF sobre esa base, sin que `/health` se confunda con catálogo.
3. Giuliano entrega shell/buscador/tema; Fernando implementa `V-005`; Sebastian implementa `V-006` y el cliente HTTP del BFF. Compartir tipos antes de cerrar interfaces.
4. Diego y Jim prueban por capas con fixtures, luego repiten contra el entorno real. Andres publica FE/BE y Fernando ejecuta smoke desde fuera del equipo.
5. Diego y Jim cierran el gate H3 sólo con URL, commit, respuesta real, pruebas y arquitectura concordante. Si el proveedor no llega a tiempo, registrar brecha y demo parcial honesta.

## Fuentes obligatorias

- [Plan S1](../iteraciones/S01-semanas-07-08.md), [tareas F-006](../seguimiento/F-006-inicio-categorias-destacados.md), [tareas F-007](../seguimiento/F-007-buscar-productos-texto.md) y [transversales](../seguimiento/TRANSVERSALES.md).
- [Funcional F-006](../../SPECS/funcional/F-006-inicio-categorias-destacados.md), [UI F-006](../../SPECS/ui/F-006-inicio-categorias-destacados.md), [API F-006](../../SPECS/contrato-api/F-006-inicio-categorias-destacados.md), [React F-006](../../SPECS/componentes-react/F-006-inicio-categorias-destacados.md).
- [Funcional F-007](../../SPECS/funcional/F-007-buscar-productos-texto.md), [UI F-007](../../SPECS/ui/F-007-buscar-productos-texto.md), [API F-007](../../SPECS/contrato-api/F-007-buscar-productos-texto.md), [React F-007](../../SPECS/componentes-react/F-007-buscar-productos-texto.md).
- [V-005](../../SPECS/ui/vistas/V-005-inicio.md), [V-006](../../SPECS/ui/vistas/V-006-catalogo-resultados.md), [DS-001](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md), [arquitectura React](../../SPECS/componentes-react/ARQUITECTURA-REACT.md) y [Figma Mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups).
- [Contrato vigente de Productos](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/contratos/http/openapi.yaml) y [alineación Marketplace–Productos](https://github.com/Taller-SW-Web/G6-Productos-Ofertas-docs/blob/master/integraciones/ALINEACION_MARKETPLACE.md). Fijar SHA usado en la PR; no codificar por suposición a partir de una rama mutable.

Leer [GUIA-DE-TRABAJO-COLABORATIVO.md](GUIA-DE-TRABAJO-COLABORATIVO.md) **antes de iniciar**. Los paquetes personales son instrucciones de ejecución, no reemplazos de las specs.
