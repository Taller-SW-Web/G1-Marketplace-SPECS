# Spec de contrato API — [ID] [Nombre de la funcionalidad]

> Documento de contrato entre consumidores y proveedores. Debe ser implementable y verificable por frontend, backend y módulos integrados.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID funcional | `F-###` |
| Versión del contrato | `v1` |
| Responsable | [Nombre] |
| Revisor | [Nombre] |
| Spec funcional relacionada | [Ruta] |
| Estado | Borrador / En revisión / Aprobada |

## 2. Propósito y límites

- Servicio propietario: [Módulo]
- Consumidor: [Frontend u otro módulo]
- Base URL: `[URL]`
- Autenticación: [Bearer/OAuth/otro]
- Formato: `application/json`

## 3. Endpoints

| ID | Método | Ruta | Propósito | Autorización |
|---|---|---|---|---|
| API-01 | `GET` | `/recurso` | [Propósito] | [Permiso] |

## 4. Detalle de cada endpoint

### API-01 — [Nombre]

**Método y ruta:** `[METHOD] /ruta`

**Headers:**

```text
Authorization: Bearer <token>
Content-Type: application/json
```

**Parámetros:**

| Nombre | Ubicación | Tipo | Obligatorio | Regla |
|---|---|---|---:|---|
| [Nombre] | path/query/body | [Tipo] | Sí/No | [Regla] |

**Solicitud:**

```json
{}
```

**Respuesta exitosa (`200`/`201`):**

```json
{}
```

**Errores:**

| HTTP | Código | Cuándo ocurre | Respuesta |
|---:|---|---|---|
| 400 | `VALIDATION_ERROR` | [Condición] | [Formato] |
| 401 | `UNAUTHENTICATED` | [Condición] | [Formato] |
| 404 | `NOT_FOUND` | [Condición] | [Formato] |

## 5. Reglas del contrato

- Campos obligatorios: [Reglas]
- Idempotencia: [Reglas]
- Paginación y ordenamiento: [Reglas]
- Fechas, moneda y zona horaria: [Formato]
- Compatibilidad hacia atrás: [Regla de versionado]

## 6. Integraciones y eventos

| Integración | Dirección | Datos intercambiados | Sincronía |
|---|---|---|---|
| [Módulo] | Entrada/salida | [Datos] | Síncrona/Asíncrona |

## 7. Seguridad y observabilidad

- Permisos: [Regla]
- Datos sensibles: [Tratamiento]
- Correlation ID: [Formato]
- Auditoría y logs: [Eventos]

## 8. Criterios de aceptación del contrato

- [ ] API-CA-01: [Contrato validado con ejemplos]
- [ ] API-CA-02: [Errores y autenticación definidos]
