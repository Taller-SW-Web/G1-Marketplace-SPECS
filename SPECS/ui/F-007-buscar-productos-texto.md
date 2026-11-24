# Spec UI — F-007 Búsqueda

Campo global `role=search`; al confirmar navega `/catalogo?q=...`. Carga, resultados, cero y error; conserva query/limpiar; debounce para no buscar cada tecla.

Sugerencias H5: opcionales, desde la misma consulta y contrato de F-007; no introducen un endpoint nuevo. Se activan con 2 caracteres, cancelan la petición anterior y muestran como máximo seis resultados. “Sin sugerencias” es neutral y un fallo de sugerencias no impide enviar la búsqueda. Teclado: flechas, Enter y Escape con foco visible.

- [ ] **UI-F007-01:** Lector anuncia cantidad sin mover foco.
