# Seguimiento de Jim — Hito 4 y continuidad en laptop

**Corte verificado:** 25/10/2026, hora de Lima. **Ámbito:** G1 Marketplace, S02 (semanas 9–11). **Uso:** copia este archivo a la laptop, actualiza la tabla y el checklist mientras avanzas, y borra la última sección de contexto temporal cuando ya no haga falta. Este archivo no contiene credenciales, códigos MFA, tokens ni cookies.

**Fuentes de planificación:** [S02](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/main/plan/iteraciones/S02-semanas-09-11.md), [alcance H4 Productos y Seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/main/plan/ALCANCE-H4-PRODUCTOS-SEGURIDAD.md) y [transversales](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/blob/main/plan/seguimiento/TRANSVERSALES.md). Los estados de la tabla se comprobaron en GitHub al crear este archivo; hay que volver a consultarlos al retomar.

## 1. Qué debería entregarse en H4 y quién responde

El objetivo principal de H4 son **25 funciones**: F-001–F-021 y F-036–F-039. Cada función necesita contrato, implementación G1, integración real cuando corresponda, prueba en despliegue y revisión. Un mock, un frame o un HTTP 200 aislado no equivalen al cierre de una función.

| Responsable principal | Funciones principales H4 | Entrega y dependencias |
|---|---|---|
| **Jim Segovia**; revisor Andrés Morales | **F-001–F-005** | Registro/verificación/retorno, login/MFA, sesión/refresh/logout, recuperación y restablecimiento con G7. UI y BFF de G1; pruebas reales y negativas. También coordina [AUTH-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/211). |
| **Giuliano**; revisor Sebastián | **F-006–F-010** | Inicio, búsqueda, filtros, orden y paginación con catálogo G6 REAL. F-006/F-007 arrastraban trabajo de H3. |
| **Sebastián**; revisor Giuliano | **F-011–F-015** | Ficha, precio, SKU/variantes, disponibilidad y relacionados G6; contratos y ejemplos sin datos inventados. |
| **Andrés**; revisor Leonidas | **F-016–F-021** | Carrito, cantidades, eliminación, lectura, fusión tras login y paso carrito→favoritos con G6/G7, base de datos y concurrencia. También CI/CD y guard compartido. |
| **Diego**; revisor Fernando | **F-036–F-039** | Guardar, listar, eliminar/deshacer y pasar favoritos al carrito, con identidad G7, catálogo G6 y aislamiento A/B. |

Las **otras 15 funciones también avanzan en H4** con implementación y pruebas propias G1, pero conservan su cierre integral base posterior salvo que se liberen y prueben todos los contratos externos: **Leonidas F-022–F-027**, **Fernando F-028–F-035** y **Diego F-040**. F-023–F-026 y F-031 pueden cerrar antes si superan sus gates. Checkout no confirma una compra hasta que Ventas verifique `PAGADO` (F-027).

**Responsabilidades transversales:** Jim lleva las cinco funciones de cuenta y los tres ajustes visuales de Checkout; Andrés administra CI/guard y está coordinando Render/Vercel; Leonidas lidera OpenAPI y la identidad técnica G1→G6; Diego coordina QA y gates; Fernando verifica despliegue y demo. Cada dueño sigue respondiendo por el código, prueba y evidencia de su función. Jim también figura como revisor de algunas tareas de otros compañeros; la tabla siguiente cuenta sólo las issues **asignadas a Jim**.

## 2. Issues asignadas a Jim: estado y bitácora por fila

**Cómo actualizar:** conserva la fila de cada issue. En la columna «Progreso fechado», agrega un bloque `<br><br>**AAAA-MM-DD:** situación, evidencia y siguiente paso` por cada avance. Cambia «Estado GitHub» sólo después de verificar GitHub. **Abierta** puede tener código fusionado o pruebas parciales; la casilla del checklist sólo se marca cuando la issue cumple sus criterios y está cerrada.

### F-001 — Registrar cliente, verificar y retornar

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [FE #17 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/17) | Abierta | **2026-10-25:** UI preparada en el PR FE #105 fusionado; registro real sigue apagado hasta confirmar G7. |
| [FE #18 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/18) | Abierta | **2026-10-25:** pendiente enlace válido/vencido/usado, retorno y prueba UI real. |
| [BE #24 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/24) | Abierta | **2026-10-25:** adaptador preparado en BE #229 fusionado; `registro:false` en capacidades públicas. |
| [BE #25 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/25) | Abierta | **2026-10-25:** bloqueada hasta que G7 confirme versión desplegada y prueba real de registro/verificación. |
| [BE #26 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/26) | Abierta | **2026-10-25:** pruebas locales previas; faltan negativos del despliegue y revisión independiente. |
| [BE #27 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/27) | Abierta | **2026-10-25:** contrato/documentación inicial preparados; actualizar con evidencia de G7 cuando exista. |

### F-002 — Iniciar sesión y MFA

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [FE #19 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/19) | Abierta | **2026-10-25:** código fusionado; API pública de Vercel pasó login B y desafío/verificación MFA A. Falta revisión UI manual y cierre. |
| [FE #20 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/20) | Abierta | **2026-10-25:** recorridos HTTP pasaron; faltan prueba de navegador, responsive, errores visibles y revisión. |
| [BE #28 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/28) | Abierta | **2026-10-25:** código fusionado; login B y MFA A llegaron a sesión real tras corregir JWKS. |
| [BE #29 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/29) | Abierta | **2026-10-25:** [positivo A/B](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/29#issuecomment-6400393475). [Retest posterior](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/29#issuecomment-6400837598): B devolvió 503 y JWKS G7 agotó tiempo desde equipo local; investigar intermitencia, sin asumir causa. |
| [BE #30 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/30) | Abierta | **2026-10-25:** [negativos básicos](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/30#issuecomment-6400853592): anónimo/Bearer inválido 401, Origin externo 403, cuerpo inválido 400 y OTP sin desafío 410. Faltan más casos, escaneos y revisión. |
| [BE #31 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/31) | Abierta | **2026-10-25:** contrato y evidencia inicial; enlazar el corte desplegado, fallos y revisión al cerrar. |

### F-003 — Cerrar sesión

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [FE #21 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/21) | Abierta | **2026-10-25:** código fusionado; logout A/B pasó por HTTP, sesión posterior anónima. Falta UI manual. |
| [FE #22 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/22) | Abierta | **2026-10-25:** pendiente comprobar limpieza de pantalla/caché y cambio de cuenta en navegador. |
| [BE #32 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/32) | Abierta | **2026-10-25:** código fusionado; cierre local A/B respondió 200. No atribuir revocación remota sin evidencia específica. |
| [BE #33 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/33) | Abierta | **2026-10-25:** [prueba real](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/33#issuecomment-6400393780): logout y sesión posterior anónima; faltan gates y revisión. |
| [BE #34 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/34) | Abierta | **2026-10-25:** [logout anónimo repetido 200](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/34#issuecomment-6400853889); faltan cookie previamente válida repetida, CSRF/caché y revisión. |
| [BE #35 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/35) | Abierta | **2026-10-25:** documentación inicial; actualizar límites de revocación y evidencia desplegada. |

### F-004 — Solicitar recuperación de contraseña

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [FE #23 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/23) | Abierta | **2026-10-25:** UI preparada y fusionada; capacidad pública `recuperacion:false`. |
| [FE #24 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/24) | Abierta | **2026-10-25:** pendiente correo real, antienumeración, errores y recorrido UI. |
| [BE #36 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/36) | Abierta | **2026-10-25:** adaptador preparado y fusionado; flag de G7 apagado. |
| [BE #37 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/37) | Abierta | **2026-10-25:** espera confirmación de Brenis sobre implementación/publicación v1 y pruebas reales. |
| [BE #38 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/38) | Abierta | **2026-10-25:** negativos/antienumeración desplegados pendientes; pruebas locales no liberan el gate. |
| [BE #39 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/39) | Abierta | **2026-10-25:** contrato inicial; falta corte real del proveedor y evidencia de correo. |

### F-005 — Restablecer contraseña

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [FE #25 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/25) | Abierta | **2026-10-25:** UI preparada y fusionada; recorrido real aún apagado. |
| [FE #26 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/26) | Abierta | **2026-10-25:** pendiente enlace válido/vencido/usado, cambio efectivo y retorno UI. |
| [BE #40 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/40) | Abierta | **2026-10-25:** adaptador preparado y fusionado; falta proveedor real. |
| [BE #41 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/41) | Abierta | **2026-10-25:** espera disponibilidad v1 y homologación con G7; no activar por contrato solamente. |
| [BE #42 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/42) | Abierta | **2026-10-25:** pendiente token vencido/usado, revocación y pruebas de seguridad desplegadas. |
| [BE #43 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/43) | Abierta | **2026-10-25:** documentación inicial; falta resultado REAL y revisión. |

### Transversales y diseño a cargo de Jim

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [BE #202 · Arquitectura H4](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/202) | Abierta | **2026-10-25:** por iniciar; diagrama as built, enlaces a contratos/repos y distinción funcional/bloqueado. |
| [BE #203 · Decisiones S1/H3→S02](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/203) | Abierta | **2026-10-25:** documento listo en [PR #230](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/230), checks verdes; Diego solicitado como revisor. PR e issue aún abiertos. |
| [BE #211 · AUTH-001 F-001–F-005](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/211) | Abierta | **2026-10-25:** [avance G1↔G7](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/211#issuecomment-6400402520): F-002/F-003 positivos; F-001/F-004/F-005 esperan proveedor, revisión y negativos completos. |
| [FE #99 · V-011 mobile promoción](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/99) | **Cerrada** | **2026-10-25:** frame Figma creado, enlace en SPECS PR #11 fusionado; Jim aceptó visualmente. Era tarea de diseño, no programación del flujo. |
| [FE #100 · V-013 mobile operación no preparada](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/100) | **Cerrada** | **2026-10-25:** frame Figma creado, enlace en SPECS PR #11 fusionado; aceptación visual de Jim. |
| [FE #101 · V-014 confirmado desktop/mobile](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/101) | **Cerrada** | **2026-10-25:** frames corregidos para confirmar sólo `PAGADO` verificado; SPECS PR #11 fusionado. |

### Encargos posteriores y antecedente histórico

| Issue asignada | Estado GitHub | Progreso fechado |
|---|---|---|
| [BE #223 · Gate H5](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/223) | Abierta · H5 | **2026-10-25:** encargo futuro: revisar gate H5 contra evidencia y pendientes H6; no confundir con cierre H4. |
| [BE #227 · Gate H6/release](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/227) | Abierta · H6 | **2026-10-25:** encargo futuro: riesgo de release y contribuciones verificables. |
| [SPECS #5 · Coherencia documental](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/issues/5) | **Cerrada · antecedente** | **2026-10-25:** estaba cerrada antes de este corte; conservar como referencia histórica, no reabrir por tareas H4 nuevas. |

**Conteo en este corte:** 35 abiertas (Frontend 10, Backend 25, SPECS 0) y 4 cerradas asignadas a Jim (Frontend 3, SPECS 1). De las abiertas, BE #223/#227 pertenecen a H5/H6. La tabla sigue las asignaciones actuales de GitHub; una nueva asignación debe agregarse cuando aparezca.

## 3. Checklist de cierre por issue

**Marca `[x]` y tacha sólo cuando GitHub esté cerrada y conste el criterio de aceptación.** Un PR fusionado, una prueba positiva o un diseño aprobado se anotan como progreso en la tabla aunque la issue siga abierta.

### F-001

- [ ] [FE #17 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/17)
- [ ] [FE #18 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/18)
- [ ] [BE #24 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/24)
- [ ] [BE #25 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/25)
- [ ] [BE #26 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/26)
- [ ] [BE #27 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/27)

### F-002

- [ ] [FE #19 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/19)
- [ ] [FE #20 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/20)
- [ ] [BE #28 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/28)
- [ ] [BE #29 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/29)
- [ ] [BE #30 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/30)
- [ ] [BE #31 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/31)

### F-003

- [ ] [FE #21 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/21)
- [ ] [FE #22 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/22)
- [ ] [BE #32 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/32)
- [ ] [BE #33 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/33)
- [ ] [BE #34 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/34)
- [ ] [BE #35 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/35)

### F-004

- [ ] [FE #23 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/23)
- [ ] [FE #24 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/24)
- [ ] [BE #36 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/36)
- [ ] [BE #37 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/37)
- [ ] [BE #38 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/38)
- [ ] [BE #39 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/39)

### F-005

- [ ] [FE #25 · Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/25)
- [ ] [FE #26 · QA funcional](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/26)
- [ ] [BE #40 · Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/40)
- [ ] [BE #41 · Integración](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/41)
- [ ] [BE #42 · QA seguridad](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/42)
- [ ] [BE #43 · Documentación](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/43)

### Transversales y diseño H4

- [ ] [BE #202 · Arquitectura](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/202)
- [ ] [BE #203 · Decisiones](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/203)
- [ ] [BE #211 · AUTH-001](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/211)
- [x] ~~[FE #99 · V-011 mobile](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/99)~~
- [x] ~~[FE #100 · V-013 mobile](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/100)~~
- [x] ~~[FE #101 · V-014 confirmado](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/101)~~

### Encargos posteriores e histórico

- [ ] [BE #223 · Gate H5](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/223)
- [ ] [BE #227 · Gate H6](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/227)
- [x] ~~[SPECS #5 · Coherencia documental, antecedente](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/issues/5)~~

## 4. CONTEXTO TEMPORAL PARA RETOMAR EN LA LAPTOP — BORRAR MÁS ADELANTE

Esta sección es una transferencia de contexto, no una nueva decisión de alcance. Al retomar, primero leer el estado vigente de GitHub, los PR y SPECS; luego actualizar la tabla anterior. **No subir credenciales ni este contexto con datos sensibles a ningún repo.** Las cuentas de prueba A/B existen por canal privado; este archivo no contiene sus accesos. En la máquina actual estaban en un archivo local ignorado por Git; en la laptop hay que obtenerlas o almacenarlas también fuera de Git.

### Qué se hizo recientemente

1. Se fusionaron los cambios de cuenta de Jim: [Frontend PR #105](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/pull/105), [Backend PR #229](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/229) y [SPECS PR #9](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/9). Hay UI/BFF preparados para F-001–F-005. En producción están habilitados login/MFA/sesión; registro y recuperación siguen apagados hasta confirmar G7.
2. Andrés administra la configuración de Render/Vercel. **Jim confirmó que ambos despliegan automáticamente desde sus ramas `develop` al subir commits.** Para una evidencia que exige SHA exacto, verificar el deployment concreto; no inferirlo sólo de la rama o de registros de GitHub que apuntan a un deploy antiguo.
3. URLs públicas: [Frontend Vercel](https://g1-marketplace-frontend.vercel.app/) y [BFF Render](https://g1-marketplace-backend.onrender.com/). G7 v1: `https://g7-auth-service.onrender.com/api/v1`. Las capacidades G1 llegaron a `login:true`, `registro:false`, `recuperacion:false`.
4. Un fallo inicial de MFA resultó ser `AUTH_KEYS_UNAVAILABLE` del BFF al leer JWKS. Andrés ajustó Render; después las pruebas HTTP reales pasaron: B sin MFA hizo login/sesión/logout en BFF y Vercel; A con MFA hizo login, solicitó y verificó código, consultó sesión, renovó, cerró y volvió a anónimo. La prueba anterior directa de G7 también había pasado A/B, perfil, refresh y logout. Códigos y tokens no se conservaron en evidencias.
5. Se registró ese positivo en [BE #29](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/29#issuecomment-6400393475), [#33](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/33#issuecomment-6400393780) y [#211](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/211#issuecomment-6400402520). Favoritos sin sesión respondió 401; con B, lectura 200. **No se probó aislamiento completo A/B con datos distintos.**
6. Un **retest posterior** de login B dio 503 `AUTH_UNAVAILABLE`; la consulta pública JWKS G7 agotó 30 s y luego 15 s desde este equipo, mientras G1 `/ready` y capacidades respondían. Es indicio de posible intermitencia, **no causa confirmada** del 503 en Render. No se repitió login automáticamente tras la respuesta incierta. Véase [hallazgo #29](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/29#issuecomment-6400837598). Negativos básicos quedaron en [#30](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/30#issuecomment-6400853592) y [#34](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/34#issuecomment-6400853889): anónimo/Bearer inválido 401 en favoritos, refresh anónimo 401, logout anónimo repetido 200, login mal formado 400, Origin externo 403 y OTP sin desafío 410.
7. El catálogo G1 sigue devolviendo 503 `CATALOG_UNAVAILABLE` con diagnóstico `PROVIDER_CONFIG_MISSING`. El adaptador de favoritos de Diego aún usa elegibilidad/proyección sandbox, apagada en producción. Por ello no se puede crear un favorito real de prueba para demostrar la separación completa A/B; coordinar con G6/Diego/Andrés, sin activar mocks en producción ni editar datos reales manualmente. Un 200 en lista vacía no prueba aislamiento.
8. [BE #204](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/204), de migraciones de Andrés, permanecía abierta en el último corte: arreglo en `develop`, instalación limpia PostgreSQL probada, pero auditoría/rollback/revisión del entorno compartido pendientes. Que las sesiones funcionen ahora no cierra automáticamente esa issue.
9. Los tres encargos Figma de Jim, [FE #99](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/99), [#100](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/100) y [#101](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend/issues/101), se cerraron tras aceptación visual de Jim; [SPECS PR #11](https://github.com/Taller-SW-Web/G1-Marketplace-SPECS/pull/11) se fusionó. Son diseño, **no** implementación frontend de Checkout; esta última pertenece a las issues de Leonidas/Leo.
10. [BE #203](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/203) tiene documento de decisiones y dependencias en [PR #230](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/pull/230), abierto con checks verdes y revisión solicitada a Diego. [BE #202](https://github.com/Taller-SW-Web/G1-Marketplace-Backend/issues/202) sigue disponible para avanzar arquitectura. No fusionar ni cerrar #203 sin revisar el estado actual del PR.

### Qué se espera ahora

- **Respuesta de Brenis/G7:** Jim preparó un mensaje con las URL de G1, resultados A/B sin secretos y consulta por la intermitencia de JWKS/503, además de pedir estado desplegado de registro/verificación y recuperación/restablecimiento v1. **Estamos esperando la respuesta de Brenis.** Cuando llegue, actualizar F-001/F-004/F-005 y decidir pruebas reales. No asumir que G7 confirmó disponibilidad por tener endpoints en código o contrato.
- **Productos/favoritos:** coordinar con Diego y el equipo G6 el adaptador real de elegibilidad/proyección y la configuración de catálogo. Luego crear datos controlados A/B, probar lectura de cada titular, rechazo sin sesión y acceso cruzado manipulando identificadores desde web y API. No declarar este gate cumplido por la lectura vacía de B.
- **Calidad y cierre:** comprobar estabilidad del proveedor, UI manual, negativos/timeout y revisión independiente; registrar URL/commit/deployment exactos cuando se necesiten como evidencia. Mantener abiertas las issues hasta cumplir cada criterio. El goal de integración G7 estaba en estado **blocked** al corte, pero Jim pidió continuar; no descartarlo por el avance parcial.

### Primer prompt útil para el agente de la laptop

> Lee este archivo completo y contrástalo con el estado actual de GitHub, SPECS y los repos clonados. Conserva las distinciones entre código preparado, integración real y cierre de issue. Actualiza la tabla y el checklist con fecha en cada cambio. Prioriza la respuesta de Brenis, la estabilidad G7 y la integración de favoritos A/B; avanza las tareas independientes de Jim mientras falten dependencias externas. No copies secretos al repo ni declares terminado algo que sólo pasó con fixtures o una prueba parcial.
