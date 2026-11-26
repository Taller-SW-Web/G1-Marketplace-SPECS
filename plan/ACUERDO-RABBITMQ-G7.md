# Acuerdo de prueba · RabbitMQ con Seguridad

Preparación del 24/11/2026 para [BE #313](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/313). Fuentes: propuesta de Brenis y [catálogo de eventos de G7, revisión fijada](https://github.com/Taller-SW-Web/Modulo-de-Seguridad/blob/1b8f2e35448075a6c396b70fdd4ec1d5b1aa9201/specs/catalogo-eventos.md). El congelamiento del punto 4 es el viernes 27/11.

**Acordado para preparar la prueba:** G1 aporta un RabbitMQ de pruebas. La propuesta original de Brenis usa cuentas separadas con permisos mínimos. G7 no puede crear una cuenta para Marketplace en su broker. Brenis propone publicar un `usuario.creado` originado por una cuenta de prueba y cotejar el identificador de evento con G1.

**Pendiente para ejecutar y cerrar:** Jim y G7 deben confirmar host, puerto TLS, vhost, cuentas, ventana de ejecución y coordinación de los casos de bloqueo y roles.

## Limitación del plan gratuito y decisión

Jim creó una instancia de pruebas CloudAMQP Little Lemur y comprobará RabbitMQ Manager (Admin → Users). La [FAQ del proveedor](https://www.cloudamqp.com/docs/faq/) indica que la gestión de usuarios, vhosts y permisos se reserva a planes dedicados.

- **Dos usuarios**, si el panel y la cuenta de management lo permiten: aplicar la separación de publicación y consumo de la propuesta de Brenis.
- **Un usuario compartido**, si el plan impide crear las dos cuentas: reutilizar la cuenta y el vhost existentes para que G7 publique y G1 consuma. Jim y G7 comparten esa credencial solo por el canal privado acordado. Es una desviación limitada a pruebas: no se aplica la separación de permisos. **Pendiente de confirmación de G7** antes de ejecutar la prueba REAL o compartir el acceso. El setup de este modo declara solo la topología y coloca `x-dead-letter-exchange` y `x-dead-letter-routing-key` en `marketplace.usuarios`.

## Publicación y consumo

| Elemento | Configuración de prueba |
|---|---|
| Exchange G7 | `seguridad.usuarios`, topic durable. Routing key igual a `tipo`. |
| Cola G1 | `marketplace.usuarios`, durable. Binding `usuario.*` al exchange G7. |
| Exchange de descarte | `seguridad.usuarios.dlx`, direct durable. |
| Cola y política de descarte | `seguridad.usuarios.dlq`, durable, con binding `descartado`. El DLX y la clave se aplican a `marketplace.usuarios` mediante política en modo de dos usuarios, o como argumentos de cola en modo compartido. |
| `g7_publicador` | Solo escritura en `seguridad.usuarios`. Sin lectura, configuración ni acceso a management. |
| `g1_consumidor` | Solo lectura y configuración de `marketplace.usuarios`. Sin publicación, acceso al DLQ ni acceso a management. |

Las filas de permisos anteriores aplican al modo de dos usuarios. En ese modo el administrador declara la topología, bindings y política, y G1 consume la cola ya vinculada. Redeclarar los exchanges o recrear bindings requiere permisos adicionales según [RabbitMQ](https://www.rabbitmq.com/docs/access-control). Antes de la prueba, Leonidas confirma si el consumidor #314 funciona con topología administrada y cómo aplica sus reintentos #315 con el perfil mínimo. El catálogo prevé descarte tras tres reintentos; la topología sola no los implementa.

## Contrato G7 · versión 1

| Campo | Formato |
|---|---|
| `eventoId` | UUID único. El «eventId» mencionado en coordinación corresponde a `eventoId` en el mensaje. Conservarlo en reintentos. |
| `tipo` | Nombre del evento, idéntico a la routing key. |
| `version` | Entero `1` para estas cargas. |
| `fecha` | Instante UTC con milisegundos. |
| `usuarioId` | UUID de la cuenta de prueba afectada. Excluirlo de la evidencia compartida. |
| `datos` | Carga específica, según la tabla siguiente. |

| Evento | Origen y `datos` |
|---|---|
| `usuario.creado` | Publicar al verificar el correo de una cuenta de prueba, tras confirmar la operación. Para cliente: `{"roles":["CLIENTE"]}`. El registro pendiente no lo genera. |
| `usuario.bloqueado` | Bloqueo automático o manual. Contiene `automatico` booleano y `hasta` con fecha UTC o `null` cuando no vence. Ejemplo manual: `{"automatico":false,"hasta":null}`. |
| `usuario.roles_cambiados` | Cambio de rol confirmado. `roles` contiene la lista completa resultante. Ejemplo del catálogo: `{"roles":["VENDEDOR","GESTOR_COMERCIAL"]}`. |

Marketplace debe tratar una entrega repetida con el mismo `eventoId` como un solo efecto. RabbitMQ puede entregar más de una vez y el catálogo no garantiza orden global. No usar el mensaje como fuente de verdad del perfil.

## Prueba y evidencia

1. Jim confirma el modo con Brenis y prepara el broker. Si hay dos cuentas, verifica los permisos de la tabla y entrega a G7 solo la credencial de publicación. Si se acepta el modo compartido, utiliza la cuenta existente. Comparte host, puerto TLS, vhost y la credencial correspondiente por el canal privado, y configura el acceso de G1 en su entorno. Nunca registrar URI con contraseña, secreto, cuerpo íntegro ni datos de perfil en Git o en la evidencia.
2. Si se hace un smoke previo, usar un evento sintético y marcarlo **MOCK**, aunque el broker esté desplegado. Terminar esta comprobación antes de la ventana con G7.
3. Brenis verifica el correo de la cuenta de prueba y confirma desde G7 el `eventoId`, tipo, hora UTC y publicación. G1 coteja el mismo ID con la recepción y confirmación que registre Marketplace. No usar el lector manual de colas mientras esté activo el consumidor de la prueba.
4. Registrar proveedor, entorno de prueba, revisiones, hora, routing key, `eventoId` y resultado. La entrega G7→broker→G1 observada entre despliegues se registra como **REAL**. Una publicación enrutada no acredita consumo. Si se acuerda reentrega, usar el mismo ID y comprobar un solo efecto. Bloqueo y roles se programan con G7 tras confirmar el caso inicial.

La preparación local no prueba entrega ni provisión de cuentas. [BE #313](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/313) espera confirmación e intercambio por canal seguro. #314/#315 conservan su alcance y su responsable.
