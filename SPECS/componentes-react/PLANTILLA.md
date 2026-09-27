# Spec de componentes React — [ID] [Nombre de la funcionalidad]

> Documento de diseño del frontend. Traduce la Spec UI y el contrato API a una estructura React implementable.

## 1. Metadatos

| Campo | Valor |
|---|---|
| ID funcional | `F-###` |
| Responsable | [Nombre] |
| Revisor | [Nombre] |
| Spec UI relacionada | [Ruta] |
| Contrato API relacionado | [Ruta] |
| Stack | Next.js / React / TypeScript |

## 2. Rutas y pantallas

| Ruta | Página o contenedor | Protección | Datos iniciales |
|---|---|---|---|
| `/ruta` | `[Page]` | [Pública/privada] | [Query o props] |

## 3. Árbol de componentes

```text
[Page]
├── [Container]
│   ├── [Component]
│   └── [Component]
└── [Component]
```

## 4. Contratos de componentes

| Componente | Responsabilidad | Props | Estado | Eventos |
|---|---|---|---|---|
| `[Component]` | [Responsabilidad] | [Props] | [Estado] | [Eventos] |

## 5. Estado y flujo de datos

- Estado local: [Qué se mantiene localmente]
- Estado global: [Store/contexto y razón]
- Datos remotos: [Query/mutation y cache]
- Flujo: `[API] → [Hook] → [Container] → [Componentes]`

## 6. Hooks, formularios y validaciones

| Elemento | Responsabilidad | Fuente de reglas |
|---|---|---|
| `[useHook]` | [Responsabilidad] | [Spec o contrato] |

## 7. Estados y errores

- Loading: [Comportamiento]
- Empty: [Comportamiento]
- Error: [Comportamiento y recuperación]
- Success: [Actualización de UI]

## 8. Pruebas previstas

- Componentes: [Casos]
- Interacciones: [Casos]
- Integración API: [Casos]
- Accesibilidad: [Casos]

## 9. Criterios de aceptación técnica

- [ ] RC-01: [Componente implementa el contrato definido]
- [ ] RC-02: [Todos los estados UI están cubiertos]
