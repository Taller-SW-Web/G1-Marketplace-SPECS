# Spec de contrato API — F-029 Filtros de historial

Extiende `GET /api/v1/orders/me` con `state`, `from`, `to`, `page` y `pageSize` como diseño BFF. En el contrato H-03 publicado, `GET /api/v1/pedidos/me` sólo admite filtro externo `estado` (`CREADO`, `PAGADO`, `EN_PREPARACION`, `DESPACHADO`, `ENTREGADO`, `ANULADO`) y `page` desde 1. El BFF mapea `state→estado` y `pageLocal+1→pageExterna`, con `pageSize` máximo 50. El rango `from/to` no tiene soporte publicado: no se habilita en integración real ni se simula filtrando una sola página; requiere extensión del proveedor o decisión de alcance. La identidad se deriva del JWT.

- [ ] **API-CA-F029-01:** Un rango invertido devuelve `400` sin llamar a Ventas.
- [ ] **API-CA-F029-02:** El filtro de estado y la paginación conservan el ámbito del titular; el rango de fechas no se anuncia como disponible hasta tener contrato externo.
