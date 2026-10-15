# Changelog — documentación de elementos compartidos

Este registro describe documentación y contratos de consumo. No acredita publicación de una biblioteca, revisión humana ni una nueva versión de DS-001.

## 0.1.0 — 14/10/2026 — En revisión

- Se crea [el catálogo de elementos compartidos](ELEMENTOS-COMPARTIDOS.md) con ubicación, responsabilidades, foundations, DTO y límites de uso.
- Se registran los elementos presentes en el corte local: Header/Footer, SearchBox, ProductCard, feedback de catálogo, skeletons, CategoryChip y hook/validadores.
- Se distinguen los estilos CSS de los componentes React todavía pendientes; ErrorState no se declara O-010 completo.
- Se documenta el subconjunto de 18 variables CSS, tipografías instaladas y diferencias responsive pendientes de aceptación.
- Se añaden guías de consumo en los repositorios Frontend y Backend, con ejemplos y handoff.
- Se registra la política actualizada de la sesión: commits y publicación de las ramas de trabajo por repositorio, sin cambios publicados a main ni apertura automática de PR; Giuliano los preparará manualmente al terminar.
- Se enlazan las guías compartidas desde las ramas de código y se registran los commits publicados de Frontend/Backend en la evidencia del corte.

Compatibilidad: este cambio es documental; no modifica exports, props, comportamiento ni contratos HTTP. Conserva como pendientes las revisiones y los gates externos.
