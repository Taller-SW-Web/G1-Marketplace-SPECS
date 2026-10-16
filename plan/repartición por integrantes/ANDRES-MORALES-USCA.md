# Andres Fernando Morales Usca — DevOps / Seguridad — responsabilidad punta a punta

**Asignación decidida por el PO el 13/10/2026; estimación base fijada en la matriz.** Bloque: **4. Carrito de compras**; IDs: **F-016–F-021**. Revisor principal: **Leonidas Garcia**. Hitos: S2: F-016/019; S3: F-017/018; S5: F-020/021. Leer la [matriz vigente](../../SPECS/RESPONSABILIDADES-PUNTA-A-PUNTA.md), la [guía común](GUIA-DE-TRABAJO-COLABORATIVO.md) y las [decisiones/gates](../DECISIONES-Y-BLOQUEOS.md). Conservar el rol general del README; el ownership de implementación es distinto de los paquetes de diseño de vistas.

## Fuentes y alcance

- Specs funcionales de entrada: [F-016](../../SPECS/funcional/F-016-agregar-item-carrito.md), [F-017](../../SPECS/funcional/F-017-cambiar-cantidad-item-carrito.md), [F-018](../../SPECS/funcional/F-018-quitar-item-carrito.md), [F-019](../../SPECS/funcional/F-019-visualizar-carrito.md), [F-020](../../SPECS/funcional/F-020-fusionar-carrito-anonimo.md), [F-021](../../SPECS/funcional/F-021-mover-carrito-favoritos.md). Para cada ID leer también su archivo homónimo en `SPECS/ui/`, `SPECS/contrato-api/` y `SPECS/componentes-react/`, y su plan/tarea en `plan/funcionalidades/` y `plan/seguimiento/`.
- Entregables visuales relacionados: V-008, O-005–O-007; V-007/V-001 como puntos de entrada. El [archivo de mockups](https://www.figma.com/design/k6JZRdgbO7YtZXeFqygE8p/Mockups) fue accesible el 13/10/2026; confirmar con el PO el frame y su enlace específico antes de citarlo como definitivo.
- Gates y dependencias: I-01 Productos, G-AUTH, G-SKU, G-ADD, G-UNDO, G-DB; interfaz F-039 con Diego. No forzar migración destructiva.
- **Repositorios y tareas:** [Frontend](https://github.com/Taller-SW-Web/G1-Marketplace-Frontend) y [Backend](https://github.com/Taller-SW-Web/G1-Marketplace-Backend); tableros [F-016](../seguimiento/F-016-agregar-item-carrito.md), [F-019](../seguimiento/F-019-visualizar-carrito.md). El corte de H3 se vincula con `TASK-F016-FE-001`, `TASK-F016-BE-001` y `TASK-F016-QA-001`, `TASK-F019-FE-001`, `TASK-F019-BE-001` y `TASK-F019-QA-001`. Consultar sus dependencias, semana y estado antes de abrir el issue o PR.
- Colaboración y límite de ownership: Mantener además base FE/BE, CI/deploy, secretos, CORS y health seguro de H3; estos son roles transversales, no sustituyen su corte carrito. Revisar seguridad de cuenta de Jim.

## Incremento vertical individual de H3 / semana 8

F-016/F-019: control de agregar un ítem y V-008 con endpoint BFF y persistencia propia en sandbox aislado; caso agregado y rechazo por producto no elegible. MOCK hasta validar stock/identidad reales.

**Evidencia mínima individual:** componente o estado de UI, ruta/adaptador/lógica o persistencia propia de Marketplace, test positivo y negativo con comando/resultado, commit y PR a `develop` revisado por Leonidas Garcia, captura o log sanitizado, explicación breve de decisiones y etiqueta `MOCK` o `REAL`. Si no existe `develop` en un repo, Diego coordina su creación sin reescribir historial. Un corte `MOCK` es **avance parcial**, nunca funcionalidad terminada ni prueba de integración externa. Para F cuya semana objetivo es S2–S5, registrar el corte de H3 como avance preparatorio vinculado al mismo ID; no adelantar la semana objetivo ni cerrar FE/BE/INT por un prototipo.

## Trabajo posterior hasta el cierre

- **Frontend:** Implementar estado del carrito V-008 y O-005–O-007 según specs; mostrar totales sólo desde snapshot autorizado, sin incremento supuesto. F-020 usa identidad de Jim y F-021 coordina con Diego.
- **Backend Marketplace:** Implementar rutas, ownership de carrito y persistencia Marketplace conforme al modelo lógico; transacciones/idempotencia según contrato, sin almacenar catálogo o stock ajeno. G-UNDO requiere acuerdo antes de prometer restauración.
- **Pruebas:** Alta/duplicado, cambio/quitar, carrera, sesión ajena, stock insuficiente, timeout y rollback; DB en entorno temporal y negativos de seguridad; MOCK/REAL diferenciados.
- **Documentación y evidencia:** actualizar tareas del bloque sin cambiar IDs/estados por anticipado. Citar spec y mockup usados, IA (herramienta/propósito/código generado/revisión humana o “No se usó IA”), comandos y resultados, commit, PR, revisor, URL si existe y clasificación `MOCK`/`REAL`. Adjuntar prueba autorizada de proveedor antes de cerrar cualquier INT.
- **Handoff:** Giuliano usa el DTO público; Diego recibe contrato de mover favorito al carrito; Leonidas recibe snapshot de checkout.

## Ruta crítica compartida de H3

F-006/F-007, V-005 y búsqueda de V-006 deben llegar a frontend y BFF desplegados con **llamada real a Productos**. Este paquete aporta a esa ruta mediante su rol transversal cuando corresponda, sin desplazar el incremento vertical propio. Si I-01 no tiene URL, token/datos y respuesta comprobada, Jim/Diego registran el gate bloqueado y presentan sólo avance parcial. Ningún fixture ni `render.yaml` acredita integración o despliegue.

**Al iniciar:** usar la estimación base de la matriz, acordar archivos compartidos y comunicar bloqueos o desvíos de capacidad a Diego/Jim. No codificar contratos/rutas ajenos sin versión publicada. Si la carga o el gate impiden el objetivo del hito, proponer resecuenciación documentada antes del corte.

---

## 📑 Informe de Evidencia Individual — Hito 3 / Semana 8

| Metadato | Detalle |
|---|---|
| **Responsable** | Andrés Fernando Morales Usca (DevOps / Seguridad — Owner Bloque 4 Carrito) |
| **Revisor Principal** | Leonidas García Lescano (Arquitectura de Software) |
| **Hito / Semana** | Hito 3 / Semana 8 (Avance vertical individual preparatorio) |
| **Clasificación** | **`[MOCK]`** (Persistencia local en PostgreSQL y sandbox aislado; no acredita integración real I-01) |
| **Funcionalidades** | [`F-016 Agregar ítem`](../../SPECS/funcional/F-016-agregar-item-carrito.md) y [`F-019 Visualizar carrito`](../../SPECS/funcional/F-019-visualizar-carrito.md) |
| **Ramas de Trabajo** | `feat/h3-f016-f019-carrito` (en repositorios Frontend y Backend) |

---

### 1. Entregables de Frontend (`G1-Marketplace-Frontend`)

Se implementó el flujo completo de adición y visualización del carrito bajo **Next.js 16 (App Router)**, **React 19** y **TypeScript**, cumpliendo rigurosamente los tokens de diseño de [`DS-001`](../../SPECS/ui/DS-001-sistema-diseno-marketplace.md) y los contratos de componentes:

1. **`AddToCartAction` (`CMP-F016-001`):**
   - Acción única de 1 unidad por pulsación confirmada con área táctil accesible $\ge 44\text{ px}$.
   - Paleta oficial Inka Athletics: fondo naranja de acción (`#F76707`) con texto oscuro (`#1B1812`).
   - Bloqueo contra dobles clics y estado ocupado (`aria-busy="true"`, `RC-F-016-01`).
   - Estados deshabilitados con anuncio accesible ante variantes no seleccionadas (`UNSELECTED`) o agotadas (`UNAVAILABLE`).
2. **`AddedToCartFeedback` (`CMP-F016-002` / Overlay `O-005`):**
   - Banner/toast flotante accesible (`aria-live="polite"`) sin tapar controles críticos ni robar foco.
   - Diferenciación semántica:
     - **201 Línea creada (`ITEM_CREATED`):** Notifica creación con 1 unidad.
     - **200 Línea incrementada (`ITEM_INCREMENTED`):** Notifica cantidad total confirmada.
     - **409 Límite alcanzado (`STOCK_LIMIT_REACHED`):** Notifica ajuste de stock disponible (`RC-F-016-03`).
   - Regla `UI-O005-004`: **No muestra subtotales ni totales finales de checkout**.
3. **`CartPageContainer`, `CartLine` y `CartSubtotal` (`CMP-F019-001/002/003` — Vista `V-008`):**
   - Pantalla completa en `/carrito`, enlazada globalmente desde el [`Header`](../../src/shared/ui/Header.tsx).
   - Regla `RC-F-019-01`: Carrito vacío muestra `EmptyState` y **nunca renderiza resumen ni CTA de checkout**.
   - Regla `RC-F-019-02`: Subtotal nulo muestra "Calculando importe…" y jamás se presenta como gratuito (`S/ 0.00`).
4. **Vistas interactivas de demostración:**
   - `/productos/[slug]`: Ficha interactiva con panel de control de estados QA en vivo.
   - `/carrito`: Pantalla del carrito interactiva con eliminación y cambio de cantidades.

---

### 2. Entregables de Backend (`G1-Marketplace-Backend`)

Se implementó la persistencia y la lógica del carrito en el servicio BFF:

1. **Endpoints REST:**
   - `POST /api/v1/carts/current/items`: Crear/recuperar carrito y agregar SKU en transacción segura.
   - `GET /api/v1/carts/current`: Lectura de líneas y subtotales sin mutar cantidades.
2. **Persistencia Transaccional con Prisma:**
   - Operaciones dentro de `prisma.$transaction` garantizando consistencia atómica.
   - Restricción de unicidad relacional `[cartId, sku]`.
   - Versionado optimista (`Cart.version`) incrementado en cada mutación.
   - Manejo de sesión anónima no manipulable por cliente mediante cookie `cart_session` (`HttpOnly; SameSite=Lax`).

---

### 3. Resultados de Pruebas Automatizadas (Evidencia Verificable)

#### Suite de Frontend (`vitest run`):
```text
✓ tests/components/shared-ui.test.tsx (10 tests)
✓ tests/components/cart-view.test.tsx (5 tests)
  ✓ RC-F-019-01: carrito vacío NO renderiza resumen ni CTA de checkout
  ✓ renderiza productos y resumen cuando el carrito contiene ítems
  ✓ RC-F-019-02: subtotal nulo no es gratuito ni permite checkout
  ✓ permite iniciar checkout cuando el subtotal es válido
  ✓ dispara cambios de cantidad y eliminación
✓ tests/components/cart-add.test.tsx (11 tests)
  ✓ permite agregar 1 unidad cuando el producto tiene stock y precio listo
  ✓ RC-F-016-01: bloquea doble clic y muestra estado busy durante el envío
  ✓ muestra ayuda accesible y deshabilita si falta seleccionar variante (UNSELECTED)
  ✓ deshabilita con aviso si el producto está agotado (UNAVAILABLE) y permite reintentar
  ✓ renderiza confirmación de nueva línea agregada (201 ITEM_CREATED)
  ✓ renderiza confirmación de cantidad incrementada (200 ITEM_INCREMENTED)
  ✓ RC-F-016-03: renderiza aviso de cantidad ajustada por límite de stock (409 STOCK_LIMIT_REACHED)
  ✓ UI-O005-004: NO muestra subtotales ni total final de checkout
  ✓ dispara onViewCart y onContinue según interacción del usuario
  ✓ crea línea (201) e incrementa (200) en simulación MOCK
  ✓ rechaza con 404 SKU_NOT_AVAILABLE ante producto sin stock

Test Files: 3 passed (3) | Tests: 26 passed (26) | Duration: 2.66s
Linting: 0 errores, 0 advertencias | Typecheck: OK | Build: OK (rutas /carrito y /productos/[slug])
```

#### Suite de Backend (`node --test`):
```text
▶ TASK-F016-BE-001 & TASK-F019-BE-001: Persistencia y lógica del Carrito
  ✔ 1. Crea nueva línea en el carrito (201 ITEM_CREATED)
  ✔ 2. Mismo SKU incrementa cantidad y version (200 ITEM_INCREMENTED)
  ✔ 3. Rechaza adición con cantidad inválida (400 INVALID_QUANTITY)
  ✔ 4. Consulta el carrito actual (TASK-F019-BE-001)
✔ TASK-F016-BE-001 & TASK-F019-BE-001: Persistencia y lógica del Carrito
tests: 5 passed (5) | fail: 0 | duration_ms: 333ms
```

---

### 4. Declaración de Uso de IA (Transparencia Académica)

- **Herramienta:** Antigravity IDE (DeepMind).
- **Propósito:** Generación de estructuras de componentes React bajo el sistema de diseño Inka Athletics (`DS-001`), automatización de fixtures MOCK y creación de suites de pruebas unitarias basadas en los criterios de aceptación SDD.
- **Revisión Humana:** Verificación estricta de cumplimiento de contratos de componentes, auditoría de accesibilidad WCAG AA, validación de persistencia PostgreSQL y resolución de dependencias sin alterar el baseline.

