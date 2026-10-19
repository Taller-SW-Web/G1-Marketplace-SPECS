# Corte verificable de H1–H3 y traspaso a H4

Versión 1.0.0 · Revisión: 2026-10-18 (hora de Lima). Este registro compara el plan con evidencia disponible; no sustituye la calificación del curso ni la aceptación del equipo.

## Criterio de evaluación

Se distingue **documentado**, **implementado en Git**, **probado localmente**, **integrado con otro módulo** y **desplegado con la misma revisión**. Un PR fusionado acredita presencia de código, no todos esos niveles. Los requisitos académicos de H1–H4 se tomaron de las notas de Classroom conservadas por el equipo; la ruta técnica de H3 se tomó de [S1](iteraciones/S01-semanas-07-08.md) y del [plan maestro](PLAN-IMPLEMENTACION.md).

## Hitos 1 y 2: base planificada frente a evidencia

| Hito y producto | Evidencia observada | Estado de este corte |
|---|---|---|
| H1: arquitectura preliminar | [Arquitectura](../Arquitectura%20de%20la%20Aplicación/Arquitectura.md) y [modelo C4](../Arquitectura%20de%20la%20Aplicación/Modelo%20C4.md) existen; sus snapshots anteriores no representan automáticamente el código de 18/10. | Documentado; revisión de vigencia en esta issue. |
| H1: funcionalidades distribuidas y SDD detallado | [Matriz F-001–F-040](../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md) y 40 archivos en cada familia funcional, UI, API y React. | Distribución y cobertura documental comprobadas; revisión semántica y decisiones externas aún abiertas. |
| H1: wireframes | Fuentes históricas en `Wireframes y Prototipo/` y specs V/O/C vigentes. | Existencia documental; aprobación de cada frame no comprobada aquí. |
| H2: contribuciones Git, repositorios de BD, mockups/sistema de diseño y tres propuestas UX | Repositorios FE/BE y [modelo propio de BD](../Arquitectura%20de%20la%20Aplicación/Base%20de%20Datos/README.md) existen; DS-001 y carpeta Figma están enlazados. | Parcialmente trazable. Este corte no acredita las tres propuestas UX, aprobación de todos los mockups ni aportes individuales exigidos por el docente. |

## Hito 3: resultado del corte

Repositorios consultados el 18/10: Frontend `main@ec1acfb`, `develop@1f22cf0`; Backend `main@c7e8e8e`, `develop@f821e9e`. Las PR Frontend [#15](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/15) y Backend [#22](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/22) llevaron los avances de `develop` a `main`. El código y las pruebas se atribuyen a esas revisiones; no se presume que sean las desplegadas.

| Producto H3 previsto | Evidencia y límite | Resultado |
|---|---|---|
| Descripción del módulo y diagramas | README, arquitectura y C4 existen. Se actualizan las referencias del corte en esta issue. | Disponible como documentación; corresponde validar la versión mostrada en exposición. |
| Primer demo funcional | FE/BE contienen catálogo, ficha, carrito, favoritos, login y checkout parcial. Varias rutas usan fixtures/identidad MOCK. | Avance de código real; alcance funcional parcial. |
| Integración vía API con Productos para F-006/F-007 | El [adaptador G6](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/blob/f821e9e/docs/INTEGRACION-G6-H3.md) y la [guía FE](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/blob/1f22cf0/docs/INTEGRACION-G6-H3.md) documentan categorías reales en Docker local el 17/10, pero la búsqueda devolvía 503 entonces. El 18/10 se consultaron directamente las rutas públicas de G6: categorías 200 y productos con `q=zapatillas` 200 con `items: []`. Esa consulta **no** pasó por el BFF de G1 ni prueba una búsqueda con resultados. | **Parcial; gate F-006/F-007 sin cierre.** |
| Proyecto funcionando en nube | `https://g1-marketplace-frontend.vercel.app/` respondió 200 el 18/10; `/api/catalog/home` respondió 503. No se vinculó la revisión de FE y BE al despliegue ni se obtuvo respuesta intermodular desde la web pública. | **Parcial; gate de nube funcional e integración sin cierre.** |
| Explicación del uso de IA y código generado | Existe material de exposición en la carpeta local de planificación parcial, fuera de este repositorio. | Preparación documental; no se verificó la exposición. |
| Evidencia individual | Hay PR integradas para cortes por integrante, incluidos F-002, F-011, F-016/F-019, favoritos, checkout e historial. No todas las funcionalidades del bloque de cada persona quedaron completas. | Avances parciales, predominantemente MOCK; revisar caso por caso en la matriz de responsabilidades. |

La consulta HTTP del 18/10 muestra disponibilidad puntual de G6, no contrato homologado, token de Seguridad ni continuidad del servicio. La respuesta 503 de la web pública no permite atribuir la falla a G1 o G6 sin logs correlacionados.

## Trabajo que pasa explícitamente a H4

| Pendiente y responsable | Criterio verificable de cierre |
|---|---|
| F-006/F-007 con Productos REAL — Giuliano y Leonidas; coordinación G6/G7 | Web desplegada → Next → BFF → G6; categoría y búsqueda con producto elegible, vacío y error; request ID, revisión FE/BE/G6, entorno y capturas/logs saneados. Si sólo hay `items: []`, registrar vacío, no búsqueda positiva. |
| Nube FE/BE del mismo corte — Fernando y Andrés | URL web, URL `/ready` del backend, commits desplegados, pipeline y prueba externa reproducible. |
| Auth en pantallas y APIs — Jim; Seguridad/G7 | Sesión real, autorización de API, usuario ajeno, expiración/MFA según contrato y evidencia de la revisión desplegada. El login MOCK F-002 no cuenta. |
| Detalle/SKU y carrito/favoritos — Sebastian, Andrés y Diego | Revisar F-011–F-014, F-016/F-019 y F-036–F-038 con proveedor real cuando corresponda; separar persistencia local de stock/precio real. Resolver G-SKU, G-UNDO y datos comerciales sin ampliar el contrato por suposición. |
| CI/CD y diseño de API — Andrés, Fernando y Leonidas | OpenAPI vigente; build, test y deploy ejecutados para el mismo commit y entorno, con resultado y rollback registrado. |
| E2E completo carrito → checkout — Andrés y Leonidas | Frontend [#9](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/9) y Backend [#17](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/17) siguen abiertas al corte. Exigir aserciones ejecutadas contra backend MOCK disponible y PostgreSQL real para los casos que lo requieren; después integrar y repetir. La prueba de catálogo→carrito de FE [#14](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/14) es distinta. |

El traspaso **se suma** a las metas de H4, por lo que S2 debe priorizar gates H3 y revisar su capacidad antes de prometer las 15 funcionalidades originalmente previstas. Checkout F-022–F-027, pago y Ventas reales conservan sus dependencias y calendario posteriores; su demo MOCK no los adelanta a `Terminado`.

## Decisiones de alcance tomadas en esta revisión

1. H3 se presenta como **avance parcial** hasta obtener la ruta completa y el despliegue verificable. La API G6 disponible directamente no cierra I-01 para el recorrido de G1.
2. F-006/F-007 y el gate de nube quedan al inicio de S2/H4. Si el equipo necesita sustituir o ampliar el flujo exigido por el docente, Jim registra el acuerdo académico explícito; la documentación no lo presume.
3. El código MOCK ya fusionado se conserva como base técnica y se etiqueta por modo. Ninguna spec, vista o tarea cambia a `Terminado` por una captura, PR o fixture aislado.
4. Los contratos de Productos, Seguridad, Ventas y Despacho siguen bajo sus dueños. Marketplace documenta la brecha, responsable y prueba requerida sin inventar respuesta externa.

## Evidencia pendiente para aceptación

- Captura de `Network` y logs con el mismo ID para la ruta web→G6, incluidos búsqueda positiva, vacío y fallo.
- Commit de cada servicio efectivamente desplegado y enlace al run de despliegue.
- `/ready` del backend del entorno de demo con DB conectada, más pruebas de sesión/aislamiento para APIs privadas.
- Validación de Jim/Diego de los cambios de alcance y, si corresponde, respuesta del profesor sobre el gate académico.
