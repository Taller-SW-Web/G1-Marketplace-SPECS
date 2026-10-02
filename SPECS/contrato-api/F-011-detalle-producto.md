# Spec de contrato API — F-011 Visualizar ficha y galería del producto

> Contrato de lectura entre el frontend de Marketplace y su backend. Define una respuesta estable, limitada a la información descriptiva de la ficha. El backend actúa como adaptador del contrato de Productos y Ofertas; no expone su base de datos ni adopta como definitiva una ruta externa aún pendiente de homologación.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID funcional | `F-011` |
| Versión del contrato | `v1` |
| Estado | Aprobada para planificación; integración externa condicionada por `I-01`. |
| Spec funcional relacionada | `../funcional/F-011-detalle-producto.md` |
| Spec UI relacionada | `../ui/F-011-detalle-producto.md` |
| Última actualización | `2026-09-27` |

## 2. Propósito y límites

| Campo | Valor |
|---|---|
| Servicio propietario | Backend del Canal Marketplace, como BFF/adaptador de lectura. |
| Consumidor | Frontend web de Marketplace. |
| Base URL | `/api/v1` del backend Marketplace. |
| Autenticación | No requerida para esta lectura pública de productos activos. |
| Formato | `application/json`; errores `application/problem+json`. |
| Fuente externa | Productos y Ofertas, contrato semántico `EXT-OUT-CAT-01`; marca y medios requieren homologación de `I-01`. |

### Límites del contrato

- Devuelve únicamente identidad comercial, marca, descripción, especificaciones técnicas y galería.
- No devuelve precio, oferta, cupón, stock, cantidad disponible, variantes seleccionables, carrito, favoritos ni recomendaciones.
- No crea ni actualiza recursos. No requiere `Idempotency-Key`.
- Sólo devuelve productos activos y habilitados para el canal Marketplace.

## 3. Endpoints

| ID | Método | Ruta | Propósito | Autorización |
|---|---|---|---|---|
| `API-F011-001` | `GET` | `/catalog/products/{slug}` | Obtener la ficha descriptiva de un producto por su slug canónico. | Pública; sólo producto comercial activo. |

## 4. Detalle de cada endpoint

### API-F011-001 — Obtener ficha descriptiva por slug

**Método y ruta:** `GET /api/v1/catalog/products/{slug}`

**Headers de solicitud:**

```text
Accept: application/json
X-Request-Id: <UUID opcional generado por el consumidor>
If-None-Match: <ETag opcional de una respuesta anterior>
```

`X-Request-Id` es opcional para el consumidor; si falta, Marketplace genera uno y lo devuelve en la respuesta. No se acepta ni se requiere `Authorization` para esta operación.

**Parámetros:**

| Nombre | Ubicación | Tipo | Obligatorio | Regla |
|---|---|---|---:|---|
| `slug` | path | string | Sí | 1–120 caracteres; `^[a-z0-9]+(?:-[a-z0-9]+)*$`; corresponde al slug canónico del producto. |

**Solicitud:** no tiene cuerpo.

**Respuesta exitosa (`200 OK`):**

```json
{
  "data": {
    "productId": "PRD-9f419c42",
    "slug": "zapatillas-running-aero-x",
    "name": "Zapatillas Running Aero X",
    "brand": {
      "brandId": "BR-ADIDAS",
      "name": "Adidas"
    },
    "description": "Zapatillas ligeras para entrenamiento diario.",
    "technicalSpecifications": [
      {
        "group": "Características",
        "name": "Material exterior",
        "value": "Malla técnica",
        "unit": null,
        "displayOrder": 1
      },
      {
        "group": "Características",
        "name": "Peso",
        "value": "280",
        "unit": "g",
        "displayOrder": 2
      }
    ],
    "media": [
      {
        "mediaId": "MED-001",
        "type": "IMAGE",
        "url": "https://cdn.example.com/products/aero-x/front.webp",
        "alt": "Zapatillas Running Aero X, vista frontal",
        "displayOrder": 1
      },
      {
        "mediaId": "MED-002",
        "type": "IMAGE",
        "url": "https://cdn.example.com/products/aero-x/side.webp",
        "alt": "Zapatillas Running Aero X, vista lateral",
        "displayOrder": 2
      }
    ]
  },
  "meta": {
    "source": "PRODUCTS_OFFERS",
    "retrievedAt": "2026-09-27T18:15:00Z"
  }
}
```

**Headers de respuesta exitosa:**

```text
Content-Type: application/json
Cache-Control: public, max-age=60, stale-while-revalidate=300
ETag: "f011-<hash-de-representacion>"
X-Request-Id: <UUID>
```

El `ETag` representa la respuesta de Marketplace, no una versión interna de Productos y Ofertas. Si `If-None-Match` coincide y la respuesta sigue siendo utilizable según la política de caché, Marketplace responde `304 Not Modified` sin cuerpo.

**Errores:**

| HTTP | Código | Cuándo ocurre | Respuesta |
|---:|---|---|---|
| 400 | `INVALID_PRODUCT_SLUG` | El slug no cumple el formato definido. | Problem Details; no se consulta Productos y Ofertas. |
| 404 | `PRODUCT_NOT_AVAILABLE` | El producto no existe, no está activo o no está habilitado para Marketplace. | Problem Details sin distinguir estado interno. |
| 502 | `PRODUCT_CATALOG_INVALID_RESPONSE` | El proveedor respondió, pero faltan datos mínimos o el contrato no es válido. | Problem Details; se registra diagnóstico técnico. |
| 503 | `PRODUCT_CATALOG_UNAVAILABLE` | No se puede obtener la ficha desde el proveedor ni desde una caché permitida. | Problem Details recuperable. |
| 504 | `PRODUCT_CATALOG_TIMEOUT` | El proveedor no responde en el tiempo de espera acordado. | Problem Details recuperable. |

**Formato uniforme de error (`application/problem+json`):**

```json
{
  "type": "https://marketplace.example.com/problems/product-not-available",
  "title": "Producto no disponible",
  "status": 404,
  "code": "PRODUCT_NOT_AVAILABLE",
  "instance": "/api/v1/catalog/products/zapatillas-running-aero-x",
  "requestId": "0f873b84-ae5d-4cd2-a530-f88672e4af85"
}
```

No se devuelve `productId`, estado de publicación, mensajes del proveedor, trazas, URLs internas ni detalles que permitan enumerar productos privados.

## 5. Reglas del contrato

### 5.1 Campos y semántica

| Campo | Regla |
|---|---|
| `data.productId` | Obligatorio; identificador externo opaco. No se usa como ruta pública en este contrato. |
| `data.slug` | Obligatorio y exactamente igual al slug canónico solicitado. Una redirección por slug histórico requerirá una spec separada. |
| `data.name` | Obligatorio, texto plano no vacío, máximo 200 caracteres. |
| `data.brand` | Obligatorio. `brandId` es opaco; `name` es texto visible no vacío, máximo 120 caracteres. |
| `data.description` | Opcional; texto sanitizado de máximo 10 000 caracteres. Si falta, UI no muestra bloque vacío. |
| `technicalSpecifications` | Arreglo, posiblemente vacío. Cada elemento válido tiene nombre y valor no vacíos; `group` y `unit` son opcionales; se ordena por `group` y `displayOrder`. |
| `media` | Arreglo no vacío para un producto comercial activo. Se devuelven sólo medios `IMAGE` con URL HTTPS permitida, texto `alt` y orden determinista. |
| Campos excluidos | Cualquier campo de precio, stock, SKU, variante, cupón, recomendación, datos de vendedor, costos internos o administración queda fuera de `v1`. |

### 5.2 Caching, idempotencia y orden

- `GET` es seguro e idempotente; no modifica Marketplace ni Productos y Ofertas.
- El backend puede servir una representación de caché dentro de la frescura declarada. Si no existe contenido utilizable, debe consultar al proveedor o devolver error; no inventa una ficha.
- Medios y especificaciones se ordenan ascendentemente por `displayOrder`; ante empate, se usa un orden estable por identificador.
- La paginación no aplica: el contrato devuelve una única ficha completa.
- Fechas de `meta` se expresan en ISO 8601 UTC. Esta funcionalidad no devuelve moneda ni importes.

### 5.3 Compatibilidad

- Agregar campos opcionales es compatible dentro de `v1`.
- Eliminar, renombrar o cambiar el significado/tipo de un campo existente exige una nueva versión de ruta (`/api/v2`).
- Marketplace adapta cambios de Productos y Ofertas dentro de su capa de integración; no obliga al frontend a adoptar el contrato externo.

## 6. Integraciones y eventos

| Integración | Dirección | Datos intercambiados | Sincronía | Estado |
|---|---|---|---|---|
| Frontend Marketplace → Backend Marketplace | Entrada | `slug`, `If-None-Match`, `X-Request-Id`. | REST síncrona. | Definida por este contrato. |
| Backend Marketplace → Productos y Ofertas / Catálogo | Salida | Identificador por slug; recibe producto, medios y atributos. | REST síncrona mediante adaptador. | Semántica documentada; ruta y payload final pendientes (`I-01`). |
| Backend Marketplace → Productos y Ofertas / Taxonomía | Salida, si es necesario | `brandId`; recibe nombre de marca. | REST síncrona mediante adaptador. | Pendiente de homologación (`I-01`). |

No publica ni consume eventos para `F-011`. Actualizaciones de catálogo se reflejan en una consulta posterior conforme a la política de caché.

## 7. Seguridad y observabilidad

- **Permisos:** la lectura es pública sólo sobre productos habilitados comercialmente. La autorización de administración pertenece a Productos y Ofertas, no a este endpoint.
- **Validación de origen:** la URL de medio debe pertenecer a una lista permitida o pasar por un proxy de medios configurado; no se devuelven URLs arbitrarias.
- **Datos sensibles:** no hay datos personales, credenciales, inventario, costos internos ni tokens en el cuerpo o en logs.
- **Correlation ID:** se recibe o genera `X-Request-Id` UUID y se propaga al adaptador de Productos y Ofertas cuando el contrato externo lo soporte.
- **Auditoría y logs:** registrar método, slug, estado HTTP, código de error, origen de respuesta (proveedor/caché), latencia y `requestId`. No registrar encabezados de autenticación ni el cuerpo completo del proveedor.
- **Disponibilidad:** aplicar timeout y circuito de fallo en el adaptador. No realizar reintentos automáticos no acotados sobre una misma solicitud de visitante.

## 8. Criterios de aceptación del contrato

- [ ] **API-CA-F011-01:** `GET /api/v1/catalog/products/{slug}` con slug válido de producto activo responde `200` con exactamente el conjunto descriptivo definido y sin datos de precio, stock o variantes.
- [ ] **API-CA-F011-02:** Un slug con espacios, barras, caracteres no permitidos o más de 120 caracteres responde `400 INVALID_PRODUCT_SLUG` sin invocar al proveedor.
- [ ] **API-CA-F011-03:** Un producto inexistente, inactivo o no elegible responde `404 PRODUCT_NOT_AVAILABLE` con el mismo formato externo de error.
- [ ] **API-CA-F011-04:** Cada imagen devuelta contiene URL HTTPS, `alt` y `displayOrder`; un producto activo sin ninguna imagen válida se rechaza como respuesta inválida del proveedor (`502`).
- [ ] **API-CA-F011-05:** Si el proveedor no responde o excede el timeout, el contrato responde `503` o `504` con `requestId` y sin exponer su error interno.
- [ ] **API-CA-F011-06:** Una solicitud con `If-None-Match` coincidente recibe `304` sin cuerpo o una representación `200` actualizada si cambió la ficha.
- [ ] **API-CA-F011-07:** Los cambios incompatibles del proveedor se absorben en el adaptador; el frontend conserva el contrato `v1` hasta una versión mayor explícita.
- [ ] **API-CA-F011-08:** Antes de implementar contra Productos y Ofertas, se homologa la ruta, autenticación de canal y payload OpenAPI señalados en `I-01` / `OPEN-03`; el mapeo semántico de slug, producto activo, atributos vigentes e imágenes obligatorias ya está confirmado por sus fuentes.
