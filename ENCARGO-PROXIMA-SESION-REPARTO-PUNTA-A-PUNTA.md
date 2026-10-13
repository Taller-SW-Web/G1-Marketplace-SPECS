# Encargo para la próxima sesión — reparto de funcionalidades punta a punta

**Preparado para Jim Bryan Segovia Valencia, PO de Marketplace · 13 de octubre de 2026.** Este archivo transmite el pedido; **no es todavía el nuevo reparto ni modifica las asignaciones vigentes**. Jim lo compartirá con otra sesión de IA junto con un clon actualizado de `G1-Marketplace-SPECS` y le pedirá realizar el análisis y las correcciones documentales en modo goal.

## Lo que aclaró el profesor

Cada uno de los **siete integrantes** debe desarrollar y poder explicar una funcionalidad **punta a punta**: interfaz, parte backend propia de Marketplace, integración o persistencia que corresponda, pruebas y evidencia. Los roles generales (PO, JP/QA, UX/UI, arquitecto/backend, DevOps, documentador/frontend y QA/cloud) **se conservan**, pero no sustituyen la responsabilidad individual sobre un flujo funcional completo. No basta repartir por capas «unos sólo frontend, otros sólo backend, otros sólo pruebas», como hace actualmente el paquete H3.

El sílabo agrupa el canal Marketplace para el cliente en estos **ocho bloques de funcionalidad**:

1. Registro e inicio de sesión del cliente.
2. Búsqueda y navegación del catálogo por categorías, marcas y filtros.
3. Visualización del detalle del producto: características, precio, imágenes y disponibilidad.
4. Carrito de compras: agregar, modificar cantidades y eliminar productos.
5. Gestión de favoritos / lista de deseos.
6. Checkout y generación del pedido, con simulación de pago con tarjeta.
7. Notificaciones por correo del pedido al cliente.
8. Consulta y seguimiento de pedidos.

Jim **no sabe con certeza** si el profesor espera exactamente un bloque del sílabo por persona. Hay ocho bloques y siete integrantes: el próximo agente debe razonar y proponer un reparto defendible (probablemente una persona con dos bloques relacionados), indicar esta interpretación como hipótesis a validar con el profesor y evitar presentarla como una exigencia confirmada. Las 40 especificaciones `F-001`–`F-040` son el desglose fino creado por el equipo, no ocho funcionalidades nuevas del sílabo. Puede haber funciones transversales o adicionales: mapearlas sin inventar correspondencias ni omitirlas.

## Fuentes que debes leer antes de decidir

Trabaja desde el estado **actual** del clon, no desde esta foto del 13/10. Primero revisa `git status`, rama, remoto y cambios de otros integrantes; actualiza sólo de forma segura, sin sobrescribir trabajo local. Luego consulta, como mínimo:

1. `README.md` para los siete nombres y roles generales.
2. `SPECS/NOMENCLATURA-SDD.md`, `SPECS/funcional/`, `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/` para alcance, dependencias y trazabilidad de las 40 `F-###`.
3. `SPECS/ui/vistas/README.md` y `SPECS/ui/INVENTARIO-VISUAL-Y-ESTIMACION.md` para vistas/overlays y mockups. El Figma de mockups es `https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups`; comprobar enlaces vigentes antes de citarlos.
4. `plan/PLAN-IMPLEMENTACION.md`, `plan/iteraciones/`, `plan/funcionalidades/`, `plan/seguimiento/` y `plan/DECISIONES-Y-BLOQUEOS.md` para hitos de semanas 8, 11, 14 y 16, tareas y gates externos.
5. `plan/repartición por integrantes/README.md`, sus siete paquetes personales y `GUIA-DE-TRABAJO-COLABORATIVO.md` para detectar qué debe cambiar. La distribución actual **por capas** se vuelve antecedente, no autoridad para el nuevo reparto.
6. Si una decisión depende de código o disponibilidad real de otro módulo, inspecciona la versión actual de los repositorios correspondientes; un contrato, mock o `render.yaml` no prueba despliegue ni integración.

No uses los ocho `SPEC-01`–`SPEC-08` de `SPECS/specs-depreciadas/` como fuente vigente: son antecedentes. Tampoco conviertas el nuevo reparto en épicas o historias de usuario dentro de las specs; utiliza **bloques del sílabo, funcionalidades F-### y responsabilidades técnicas**.

## Trabajo solicitado a la próxima sesión

### 1. Analizar y proponer el reparto completo

- Construye una **matriz trazable** `bloque del sílabo → F-### relacionadas → vistas/overlays/correos → integrante responsable → revisor → dependencias externas → hito objetivo`. Explica funciones que crucen bloques y asigna un responsable de integración claro, sin duplicar ownership por comodidad. Verifica que las 40 F queden cubiertas o identifica explícitamente las que no pertenecen literalmente al sílabo.
- Reparte los ocho bloques entre los siete nombres reales con carga razonable y afinidad técnica, pero **sin dejar a nadie sólo en tareas transversales**. Cada integrante debe tocar frontend y backend propio en por lo menos un corte funcional. Para flujos delegados a Seguridad, Productos, Ventas o Despacho, «backend propio» significa BFF/adaptador/orquestación de Marketplace, **no programar el microservicio ajeno** ni copiar su base de datos.
- Conserva roles globales y capacidades de revisión cruzada. Si alguien asume dos bloques, justifica por qué no concentra una carga imposible. Diferencia responsable del bloque, colaboradores, revisor de PR y responsables transversales (deploy, QA, arquitectura, documentación).
- No fijes código, rutas o contratos que los proveedores aún no publicaron. Estima carga y señala decisiones o dependencias que impiden prometer cierre completo.

### 2. Rehacer la repartición para H3 / semana 8

- Corrige especialmente `plan/repartición por integrantes/`: README, **un paquete práctico por integrante** y guía común si requiere ajustes. Cada paquete debe indicar su bloque/F-###, qué hará en frontend, backend, pruebas y documentación, de qué depende, qué debe enseñar y qué queda pendiente para otro hito. Debe poder entregarse individualmente a un compañero o a su agente de IA sin que pierda contexto.
- **No elimines la ruta crítica ya acordada:** F-006/F-007, `V-005` Inicio y el corte de búsqueda de `V-006` deben llegar a una web desplegada que pase por el BFF de Marketplace y consulte la API real de Productos, con estados y evidencia. Es el mínimo funcional del hito. Si Productos no ofrece aún entorno/token/datos, marcar integración bloqueada y presentar avance parcial honestamente; no contar un fixture como integración.
- El profesor quiere evidencia individual de ciclo completo. Propón para **cada persona** un incremento vertical y comprobable de su bloque que pueda comenzar o mostrarse en semana 8, aunque el bloque completo termine en semanas 11, 14 o 16. Distingue **avance parcial** de **funcionalidad terminada**; no prometas ocho flujos integrados para la primera demo si los contratos, capacidad o tiempo no lo permiten. La prioridad común de F-006/F-007 y la contribución individual deben coexistir sin que el plan se contradiga.
- Define para esos incrementos criterios observables: pantalla/componente o estado de UI, ruta/adaptador/lógica del backend propio, test positivo/negativo, evidencia en repo/PR y una breve explicación individual. Si falta proveedor, admitir fixture sólo como desarrollo local rotulado `MOCK` y registrar el gate correspondiente.

### 3. Propagar el cambio con coherencia al resto de la documentación

- Actualiza los planes y el seguimiento de S1–S5 para que la responsabilidad por bloque/F-### acompañe al proyecto después de semana 8. Ajusta responsables/revisores en tablas y tareas afectadas sin perder IDs, estados, enlaces ni criterios ya vigentes. Corrige el README principal, índices y referencias que describen erróneamente una división permanente por capas.
- Refleja la nueva matriz de responsabilidades **también en la documentación de SPECS** —por ejemplo, un índice/matriz vigente y referencias o metadatos de cada F donde sea útil—, sin alterar por asignación las reglas funcionales, contratos API ni diseño visual aprobados. Si una spec nombra responsable de **diseño de vista**, no lo confundas con el responsable de **implementación punta a punta**: documenta ambas nociones por separado.
- Mantén las decisiones técnicas ya acordadas: frontend **React + TypeScript + Next.js App Router**; UI kit/versiones siguen pendientes si no hay decisión posterior. Conserva microservicios, BFF propio, ownership de datos y los gates intermodulares.
- Haz que cada persona documente sus fuentes (specs y mockups), uso de IA, código generado y revisión humana, comandos/resultados de pruebas, PR, commit y evidencia `MOCK`/`REAL`. Conserva la política de ramas/PR a `develop` y Conventional Commits con descripción en español, salvo nueva decisión explícita del equipo.

## Criterios de cierre del encargo

Antes de darlo por terminado, comprueba: **8 bloques explicados; 7 integrantes con trabajo FE+BE propio; F-001–F-040 trazadas; H3 mantiene F-006/F-007 e integración real como gate; cada paquete individual es ejecutable; semanas 11/14/16 siguen coherentes; roles globales intactos; revisión cruzada y evidencia individual previstas; enlaces y Markdown válidos; ninguna tarea bloqueada figura como terminada sin prueba**. Resume las decisiones y las preguntas que Jim deba validar con el profesor. No escribas código de las funcionalidades sólo para cerrar este encargo: el trabajo pedido es **analizar y corregir la distribución y documentación**.

## Estado de este traspaso

Al redactarlo, `G1-Marketplace-SPECS` estaba en `main` sin cambios locales, commit `64cc824`. Esa referencia sólo ayuda a ubicar el origen del encargo; **el próximo agente debe comprobar el estado nuevo**. Este documento no asigna todavía bloques ni F-### a personas, y no debe tomarse como aceptación del profesor ni como software ejecutado.
