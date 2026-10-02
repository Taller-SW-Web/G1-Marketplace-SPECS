# Paquete de Giuliano — acceso, confirmación y sistema de diseño

## 1. Control del paquete

| Campo | Valor |
|---|---|
| Responsable | Giuliano Macchiavello |
| Revisor principal | Jim Segovia |
| Sistema de diseño | [`DS-001` v0.2.0](../DS-001-sistema-diseno-marketplace.md) |
| Alcance | 7 entregables visuales + custodia de la biblioteca |
| Carga | 45 puntos visuales + 4 de gobernanza = **49 puntos** |
| Estado | Preparado para aceptación del integrante |

## 2. Entregables

| Orden | Spec | Resultado | Puntos |
|---:|---|---|---:|
| 1 | [`V-001` Inicio de sesión](../vistas/V-001-inicio-sesion.md) | Acceso, MFA, retorno y fusión de carrito | 9 |
| 2 | [`V-002` Registro](../vistas/V-002-registro.md) | Alta de cliente y aceptación de políticas | 7 |
| 3 | [`V-003` Recuperación](../vistas/V-003-recuperacion-contrasena.md) | Solicitud de enlace con respuesta uniforme | 4 |
| 4 | [`V-004` Restablecimiento](../vistas/V-004-restablecimiento-contrasena.md) | Validación del enlace y nueva contraseña | 5 |
| 5 | [`O-003` Autenticación requerida](../overlays/O-003-autenticacion-requerida.md) | Retorno seguro a una acción protegida | 7 |
| 6 | [`O-004` Confirmación de cierre](../overlays/O-004-confirmacion-cierre-checkout.md) | Protección ante abandono de checkout | 5 |
| 7 | [`C-001` Confirmación de pedido](../comunicaciones/C-001-correo-confirmacion-pedido.md) | Correo transaccional responsive | 8 |
| 8 | [`DS-001`](../DS-001-sistema-diseno-marketplace.md) | Custodia de tokens, componentes y biblioteca | 4 |
| **Total** | — | — | **49** |

## 3. Frames exactos

### `V-001`

- `V-001 / Desktop / Principal`
- `V-001 / Mobile / Principal`
- `V-001 / Desktop / Validación`
- `V-001 / Mobile / Credenciales inválidas`
- `V-001 / Desktop / MFA`
- `V-001 / Mobile / MFA error`
- `V-001 / Desktop / Fusionando carrito`
- `V-001 / Desktop / Fusión fallida`
- `V-001 / Mobile / Fusión fallida`

### `V-002`

- `V-002 / Desktop / Principal`
- `V-002 / Mobile / Principal`
- `V-002 / Desktop / Validación`
- `V-002 / Mobile / Política contraseña`
- `V-002 / Desktop / Enviando`
- `V-002 / Mobile / Correo no disponible`
- `V-002 / Desktop / Política rechazada`
- `V-002 / Mobile / Solicitud aceptada`

### `V-003`

- `V-003 / Desktop / Principal`
- `V-003 / Mobile / Principal`
- `V-003 / Desktop / Validación`
- `V-003 / Mobile / Enviando`
- `V-003 / Desktop / Confirmación uniforme`
- `V-003 / Mobile / Límite temporal`

### `V-004`

- `V-004 / Desktop / Validando enlace`
- `V-004 / Mobile / Principal`
- `V-004 / Desktop / Principal`
- `V-004 / Mobile / Validación`
- `V-004 / Desktop / Política rechazada`
- `V-004 / Mobile / Enlace inválido`
- `V-004 / Desktop / Enlace vencido`
- `V-004 / Mobile / Actualizada`

### `O-003`

- `O-003 / Desktop / Favorito`
- `O-003 / Mobile / Checkout`
- `O-003 / Desktop / Área privada`
- `O-003 / Mobile / Sesión vencida`

### `O-004`

- `O-004 / Desktop / Checkout en edición`
- `O-004 / Mobile / Pago preparado`
- `O-004 / Desktop / Orden verificándose`
- `O-004 / Mobile / Error al cerrar`

### `C-001`

- `C-001 / Desktop / Principal`
- `C-001 / Mobile / Principal`
- `C-001 / Desktop / Con recomendados`
- `C-001 / Mobile / Sin imágenes`

## 4. Dependencias compartidas

- Definir primero los componentes de autenticación: `AuthShell`, campo de contraseña, medidor de política, alerta de seguridad y bloque MFA.
- Coordinar con Sebastián el retorno a favoritos/carrito y con Jim la protección de salida del checkout.
- Entregar a todo el equipo los tokens y componentes aceptados de `DS-001`; evitar cambios silenciosos en instancias ya consumidas.
- Alinear `C-001` con el resumen visual de pedido de Jim y la familia de correos de Diego.
- Mantener logo, tipografía, contraste y espaciado compatibles con clientes de correo cuando se trabaje `C-001`.

## 5. Decisiones abiertas que deben revisarse

| Entregable | IDs |
|---|---|
| `V-001` | `V-001-OPEN-01` a `V-001-OPEN-03` |
| `V-002` | `V-002-OPEN-01` a `V-002-OPEN-04` |
| `V-003` | `V-003-OPEN-01` a `V-003-OPEN-02` |
| `V-004` | `V-004-OPEN-01` a `V-004-OPEN-03` |
| `O-003` | `O-003-OPEN-01` a `O-003-OPEN-03` |
| `O-004` | `O-004-OPEN-01` a `O-004-OPEN-02` |
| `C-001` | `C-001-OPEN-01` a `C-001-OPEN-05` |
| Sistema de diseño | `DS-OPEN-01` a `DS-OPEN-08` |

La pregunta completa, su responsable y su fecha/estado están en cada spec. Las decisiones que alteren layout, componente o copy se resuelven antes de la revisión final.

## 6. Orden de ejecución recomendado

1. Congelar tokens y componentes base de formularios en `DS-001`.
2. Diseñar `V-001` y `V-002` para fijar el patrón de autenticación.
3. Reutilizar ese patrón en `V-003` y `V-004`.
4. Diseñar `O-003` y comprobar el retorno con los paquetes de Sebastián y Diego.
5. Diseñar `O-004` junto con Jim para validar estados del checkout.
6. Diseñar `C-001` y armonizarlo con `C-002` de Diego.
7. Completar enlaces de Figma y solicitar revisión de Jim.

## 7. Definition of Ready del paquete

- [ ] Giuliano acepta alcance, carga y revisor.
- [ ] Las decisiones abiertas bloqueantes están resueltas o tienen supuesto aprobado.
- [ ] Los componentes compartidos tienen nombre y dueño en la biblioteca.
- [ ] Todos los frames de la sección 3 existen con esos nombres exactos.
- [ ] Cada spec enlaza su sección o frame de Figma.
- [ ] Desktop, mobile, teclado, foco, errores y contraste fueron comprobados.
- [ ] Jim revisó el paquete y Giuliano cerró las observaciones.
