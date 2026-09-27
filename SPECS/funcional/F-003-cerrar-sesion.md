# Spec funcional — F-003 Cerrar sesión

| ID | Estado |
|---|---|
| `F-003` | Aprobada para planificación; Seguridad revoca refresh. |

Cierra sesión actual, revoca refresh en Seguridad y limpia contexto local. No elimina cuenta, favoritos ni carrito autenticado.

- Cierre local sucede aun si revocación remota falla.
- Se redirige a inicio público y limpia UI protegida.

- [ ] **CA-F003-01:** Después de cerrar, rutas protegidas exigen login.
