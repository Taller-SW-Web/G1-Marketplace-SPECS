# Paquetes de diseño para Figma

Esta carpeta convierte el inventario visual aprobado documentalmente en cinco paquetes ejecutables. Cada paquete reúne las specs, los frames exactos, las dependencias compartidas, las decisiones abiertas y el orden de trabajo de una persona.

## Reglas comunes

1. Usar [`DS-001` v0.2.0](../DS-001-sistema-diseno-marketplace.md) como base visual y registrar cualquier excepción antes de diseñarla.
2. Leer la spec enlazada antes de crear sus frames; la lista de este paquete es un índice de ejecución, no un reemplazo de la spec.
3. Mantener literalmente el nombre de cada frame para conservar trazabilidad entre Markdown y Figma.
4. Crear desktop y mobile como composiciones propias; no reducir mecánicamente una versión para obtener la otra.
5. Reutilizar instancias de la biblioteca compartida. Un componente transversal se define una sola vez y su dueño coordina los cambios con los consumidores.
6. No inventar una respuesta para una decisión `OPEN`: resolverla con su responsable o tratarla como supuesto explícito y reversible.
7. El autor realiza la primera verificación; el revisor cruza spec, estados, responsive, accesibilidad y nombres de frames.
8. Al iniciar un entregable, sustituir `Enlace de Figma: Pendiente` en su spec por el enlace directo al frame o sección correspondiente.

## Resumen del reparto

| Integrante | Paquete | Revisor | Visual | Gobernanza | Total |
|---|---|---|---:|---:|---:|
| [Giuliano Macchiavello](./PAQUETE-GIULIANO.md) | Acceso, confirmación y sistema de diseño | Jim Segovia | 45 | 4 | **49** |
| [Leonidas Garcia](./PAQUETE-LEONIDAS.md) | Descubrimiento, producto y feedback global | Giuliano Macchiavello | 49 | 0 | **49** |
| [Sebastián Malca](./PAQUETE-SEBASTIAN.md) | Carrito, favoritos y filtros mobile | Diego Espinoza | 43 | 0 | **43** |
| [Jim Segovia](./PAQUETE-JIM.md) | Checkout | Leonidas Garcia | 42 | 0 | **42** |
| [Diego Espinoza](./PAQUETE-DIEGO.md) | Pedidos, postentrega y despacho | Sebastián Malca | 47 | 0 | **47** |
| **Total** | 29 entregables | — | **226** | **4** | **230** |

La diferencia entre el paquete mayor y el menor es de 7 puntos: `7 / 42 = 16.7 %`, dentro del límite del 20 %. El detalle del cálculo está en el [`Inventario visual y estimación`](../INVENTARIO-VISUAL-Y-ESTIMACION.md).

## Flujo de revisión

```text
Autor prepara frames y enlaza Figma
  → comprueba la spec y su checklist
  → revisor cruza desktop/mobile/estados
  → autor corrige observaciones
  → ambos registran la aprobación en la spec
```

## Estado

Los cinco paquetes están **preparados para entrega al equipo**. La aprobación humana, la resolución de decisiones abiertas y los enlaces finales de Figma siguen pendientes y no se consideran completados por este documento.
