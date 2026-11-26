# H5 · Catálogo F-006 a F-010 · Matriz de integración y QA

Retest del 26/11/2026. Frontend `073b3b0` y Backend `5810045`. La [matriz HTTP](matriz-http-mock.json) registra **24 PASS, 0 FAIL, 0 BLOCKED y 1 INCONCLUSIVE** en Next → BFF **MOCK local**. El único caso inconcluso es F009-observed-ties porque el fixture carece de homónimos. La suite de Backend sí cubre el criterio de desempate con datos específicos. [Frontend probado](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/commit/073b3b0a10fac0ba9df324aa02f14ac40523f08d) · [Backend probado](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/commit/581004571d1dd62e22842526c33dd584037cc61e)

| Función | Integración | QA funcional | QA de seguridad | Validación pendiente en el corte publicado |
| --- | --- | --- | --- | --- |
| **F-006 Inicio** | [BE #45][be45] · Home y destacados observados con datos simulados. | [FE #28][fe28] · Categorías, destacados, carga, vacío y error recuperable. | [BE #46][be46] · Consulta en Home rechazada y proyección pública validada. | Confirmar Home, categorías y destacados editoriales desde el despliegue con G6. El ranking G5 está fuera de H5 por decisión del PO. |
| **F-007 Búsqueda** | [BE #49][be49] · Caso positivo, vacío y longitudes inválidas en MOCK. | [FE #30][fe30] · Búsqueda y texto, vacío, timeout y reintento con los criterios conservados. | [BE #50][be50] · Límites, rechazo de parámetros fuera del contrato y proyección pública. | Repetir resultado positivo y vacío. Registrar el error o timeout autorizado con código y traza. |
| **F-008 Filtros** | [BE #53][be53] · Maestros, categoría, combinación, rango PEN y negativos HTTP. | [FE #32][fe32] · Filtros activos, recuperación y conservación de criterios. | [BE #54][be54] · Validación de filtros inválidos y reglas de exposición. | Repetir precio y combinaciones. El BFF local autenticado ya observó tres rangos reales. |
| **F-009 Orden** | [BE #57][be57] · Nombre ascendente y descendente por HTTP. Homónimos inconclusos en el fixture. | [FE #34][fe34] · Orden global entre páginas y conservación de filtros. | [BE #58][be58] · Orden inválido rechazado. Suites de Backend prueban desempate. | Repetir ASC y DESC con los homónimos de G6. Comprobar `product_id ASC` y comparar ambas páginas. |
| **F-010 Paginación** | [BE #61][be61] · Primera, siguiente, última y fuera de rango en MOCK. | [FE #36][fe36] · Recuperación al cambiar página y conservación de filtros. | [BE #62][be62] · Límites inválidos de página y tamaño rechazados. La matriz verifica IDs y total. | Repetir página 1 y 2 de tamaño 1 con dos IDs sin duplicados y sus totales. Comprobar salida de rango y reinicio al cambiar orden. |

**Pruebas locales adicionales:** 15 del runner, 91 de Backend y 76 de Frontend, todas aprobadas. Las pruebas unitarias y el recorrido HTTP son evidencias de capas distintas.

## Retest en el despliegue

El [diagnóstico de Render en BE #53][diag] registró HTTP 503 con `G7_TOKEN_REJECTED` antes de consultar G6. El [retest del BFF local contra G7/G6][real-local] aporta 9 lecturas reales HTTP 200, incluidos tres rangos de precio, los homónimos en ambos órdenes y dos páginas de tamaño 1.

1. Confirmar con Operaciones y G7 el motivo del rechazo y el entorno autorizado del retest.
2. Repetir los casos de arriba desde el BFF publicado con el mismo dataset aprobado. Adjuntar entorno, SHA, resultado y correlation ID.
3. Registrar el alcance de QA funcional y seguridad por issue. Conservar abiertos los criterios cuya evidencia dependa del proveedor o del despliegue.

## Reproducción local

Con Frontend y Backend en carpetas hermanas `G1-Marketplace-Frontend` y `G1-Marketplace-Backend`, instalar y compilar ambos antes de ejecutar el runner desde Frontend.

```bash
npm run demo:catalogo:h4 -- --skip-build --check --matrix --featured
```

El runner levanta ambos servicios en loopback y guarda el resultado en `.local-security/catalog-h4-demo.json`. Los casos están versionados en [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/tree/581004571d1dd62e22842526c33dd584037cc61e/scripts/catalog-h4/cases).

[be45]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/45
[be46]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/46
[be49]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/49
[be50]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/50
[be53]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53
[be54]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/54
[be57]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/57
[be58]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/58
[be61]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/61
[be62]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/62
[fe28]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/28
[fe30]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/30
[fe32]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/32
[fe34]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/34
[fe36]: https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/36
[diag]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53#issuecomment-7202936915
[real-local]: https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/53#issuecomment-7202778407
