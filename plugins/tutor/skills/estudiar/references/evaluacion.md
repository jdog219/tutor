# Evaluación: quizzes, cierre de módulo, exámenes, proyectos y revisión del método

Leer antes de un mini-quiz o examen, al decidir si un módulo o bloque se cierra, al planear o
corregir un proyecto de bloque, y cada 10 módulos para revisar si el método funciona.

La regla de oro (SKILL.md §4) aplica a todo lo de este archivo: se presenta y **se para**.

---

## 1. Mini-quiz de consolidación

- 5 preguntas, cada una etiquetada con su objetivo (`M07.3`).
- Mezcla: una conceptual, una de aplicación, una de transferencia, una de "¿cuándo NO usarías
  esto?", y una del tipo propio de la materia (en programación: leer y escribir código; en
  matemáticas: resolver; en idiomas: producir).
- Se califica sobre 100, pero la nota es **informativa**: lo que decide es el estado por objetivo.

## 2. Criterio de cierre de módulo

Un módulo se cierra cuando se cumplen las tres:

1. Todo objetivo **esencial** (★) está al menos en `independiente` en la tabla *Dominio*.
2. Los objetivos centrales tienen al menos una evidencia de **transferencia** o de **explicación
   correcta** (teach-back).
3. El estudiante hizo el teach-back del módulo en la Consolidación.

**Una nota agregada nunca compensa un objetivo esencial fallado.** Con 100/100/100/0 el promedio es
75, y el hueco del 0 hunde los módulos siguientes.

El veredicto se da por objetivo, no en bloque:

- Mal: *"Sacaste 69, repite el módulo."*
- Bien: *"Módulo cerrado salvo M34.4 (transacciones), que sigue en `guiado`. Lo reforzamos en dos
  repasos cortos esta semana y seguimos avanzando."*

Si un objetivo esencial queda por debajo de `independiente`, no se repite el módulo entero: se hace
una actividad focalizada en ese objetivo y se reevalúa.

Los objetivos no esenciales pueden quedar en `guiado` y avanzar: la cola de repaso los retomará.

## 3. Examen de bloque

- Al final de cada bloque, según el `ROADMAP.md`.
- Estructura, con cada pregunta etiquetada por objetivo:
  - **Conceptual**: explicar, comparar, justificar.
  - **Lectura o análisis**: predecir resultados, encontrar el error (en programación: leer código).
  - **Problema**: producir algo nuevo (en programación: escribir código).
  - **Transferencia**: un contexto distinto a todo lo practicado.
  - **Intercalado**: sin indicar qué módulo o técnica aplica.
- Se presenta completo y se para. El estudiante lo resuelve sin consultar material.
- Nota sobre 100. **Se aprueba con ≥ 70 y sin ningún objetivo esencial en blanco o fallado de
  raíz.** El 70 es la meta administrativa; el segundo criterio es el que protege los bloques
  siguientes.
- Si no se aprueba: no se repite el bloque. Se arma un **módulo de refuerzo** solo con los
  objetivos fallados, y después un examen corto sobre esos objetivos.
- Resultado en la tabla *Calificaciones* de `PROGRESO.md`, con los objetivos débiles señalados.

## 4. Proyecto de bloque

- Crece **a lo largo** del bloque, no se hace todo al final. Se define al empezar el bloque y
  cada módulo le añade una pieza.
- Vive en `pistas/<pista>/proyectos/<bloque>-<nombre>/`.
- Debe poder mostrarse (en una entrevista, un portafolio o a quien le interese): trabajo propio del
  estudiante y un `README.md` que explique **qué es, cómo usarlo y por qué se decidió así**. En
  pistas de programación, con tests cuando el bloque ya los cubrió.
- Si el estudiante tiene un interés aparcado que encaja como contexto (autoria.md §1, caso a), se le ofrece
  como tema del proyecto.
- Se corrige con el mismo feedback que los ejercicios (SKILL.md §6). En pistas de programación,
  además, una revisión tipo code review: legibilidad, nombres, estructura, casos límite.

## 5. Revisión del método — cada 10 módulos

Los exámenes miden al estudiante. Esto mide **al curso**. Si el método no funciona, insistir con él es
culpar al alumno de un problema de diseño.

Se revisan, con los datos de la *Bitácora* y la tabla *Dominio* de `PROGRESO.md`:

| Indicador | Señal buena | Señal mala |
|---|---|---|
| Acierto en repasos | Sube o se mantiene alto | Baja, o se estanca bajo |
| Uso de H4–H5 | Baja con el tiempo | Se mantiene o sube |
| Objetivos que caen de estado al repasarse | Pocos | Muchos: se avanzó sin consolidar |
| Teach-back | Más fluido, con relaciones entre conceptos | Definiciones sueltas, memorizadas |
| Reentradas (> 14 días) | Pocas | Frecuentes: el ritmo no es sostenible |
| Sesiones por módulo vs. estimado | Cercano | Muy por encima: el contenido está mal escalonado |

- Se le presentan al estudiante los indicadores, en corto y con los datos.
- Si hay señales malas, se proponen **cambios concretos** al método (en la skill o en el roadmap),
  y se discuten con el estudiante antes de aplicarlos.
- Se registra la revisión en la *Bitácora* con la fecha y lo decidido.
