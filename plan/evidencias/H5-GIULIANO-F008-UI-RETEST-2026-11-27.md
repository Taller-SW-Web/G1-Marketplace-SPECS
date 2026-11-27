# F-008 QA de rangos de precio en UI publicada — 27/11/2026

Backend #52 está cerrada. Frontend #31 y QA funcional #32 siguen abiertas; la PR Frontend #124 está integrada con aprobación previa de Jim, pero eso no cierra #31 ni acredita aceptación de #32. No se cambió el estado de ninguna issue.

## Evidencia previa reutilizada — 26/11/2026

El BFF Render `https://g1-marketplace-backend.onrender.com` devolvió 200 con fuente REAL en los tres rangos. El deploy registrado fue `dep-dc4b7u3l550s738o8jd0`, Backend SHA `f17896d7ee24876ffd33db1bb7dd91d65623ed37`.

| Rango PEN | IDs de producto registrados por el retest Render | Request ID | Resultado |
|---|---|---|---|
| 0–45 | `g6-qa-marketplace-ord-001` (G6 product ID `93f7f500-077d-432e-be98-31cb9ee0d66d`) | `15ec70a4-46f0-4e69-a590-b22fa30ec7e5` | Solo producto 001 |
| 0–60 | `g6-qa-marketplace-ord-002` (`8ad24563-c9da-4305-b650-1dd47a14fffb`) y `g6-qa-marketplace-ord-001` (`93f7f500-077d-432e-be98-31cb9ee0d66d`) | `e5c26b66-a2f8-41d8-b9d6-869ad7118a77` | Ambos productos |
| 0–100 | `g6-qa-marketplace-ord-002` (`8ad24563-c9da-4305-b650-1dd47a14fffb`) y `g6-qa-marketplace-ord-001` (`93f7f500-077d-432e-be98-31cb9ee0d66d`) | `592265d0-da0a-4004-8e27-e198ecf66a98` | Ambos productos |

La traza Vercel anterior usa `https://g1-marketplace-frontend.vercel.app`. En móvil se registró HTTP 200/source REAL y `mobile-filtros` mostró `g6-qa-marketplace-ord-001` con categoría, marca y rango 0–45. La matriz dice que esos criterios se aplicaron abriendo URLs preparadas; no demuestra interacción actual con controles. La traza no contiene un recorrido UI de 0–60 ni de 0–100, ni registra un SHA/deploy Vercel. [JSON Vercel](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/8347a891a8f0acd50fb78af33c95159234ec1b37/plan/evidencias/h5-giuliano-catalogo/retest-real-vercel.json) · [JSON Render](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/8347a891a8f0acd50fb78af33c95159234ec1b37/plan/evidencias/h5-giuliano-catalogo/retest-real-render.json) · [Matriz de ejecución](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/8347a891a8f0acd50fb78af33c95159234ec1b37/plan/evidencias/h5-giuliano-catalogo/README.md#retest-de-cat%C3%A1logo-en-vercel).

## Nuevo intento de interacción

Se inició una única navegación Playwright de solo lectura a `https://g1-marketplace-frontend.vercel.app/catalogo`. La herramienta no devolvió HTTP status, snapshot de página ni registro de solicitudes; tras aproximadamente 42 segundos se canceló la llamada pendiente. No hubo un segundo intento. Resultado de este intento: **BLOCKED — interacción actual no verificable por falta de respuesta de la herramienta**. Esto no demuestra que Vercel esté caído ni altera los resultados registrados el 26/11.

## Corte

Render acredita respuestas API para los tres rangos. La evidencia Vercel existente solo acredita la URL preparada de 0–45; la interacción actual de UI no se pudo comprobar y no hay evidencia visible previa de los rangos 0–60/0–100. Queda pendiente una ejecución Playwright que responda para aplicar los controles publicados y registrar tarjetas/IDs, requests, `X-Catalog-Source`, URL y SHA Vercel si están expuestos. No se enviaron formularios ni se modificaron datos.
