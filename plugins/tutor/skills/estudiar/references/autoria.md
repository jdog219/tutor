# Autoría: cómo se escribe el contenido del curso

Leer antes de crear o reescribir una lección, un módulo, el detalle de un bloque o una pista
nueva, y siempre que el estudiante quiera aprender un tema que no está en su roadmap. Para la
primera pista de alguien nuevo, leer antes `bienvenida.md`.

---

## 1. El estudiante quiere aprender algo nuevo

No todo tema nuevo merece una pista aparte. Clasificarlo primero:

| Caso | Cuándo | Qué se hace |
|---|---|---|
| **a) Contexto** | Se solapa con los fundamentos de la pista activa | Se usa como **tema de los proyectos** dentro del roadmap. Ej.: en una pista de programación, un videojuego pequeño como proyecto de los primeros bloques (el game loop *es* un bucle, cada entidad es un objeto) |
| **b) Bloque** | Especialización que se apoya en el tronco de la pista activa | Nuevo bloque de especialización en su `ROADMAP.md`, después del tronco |
| **c) Pista** | No tiene relación con la pista activa | Pista nueva bajo `pistas/`, con el mismo motor |

**Regla: una pista principal activa a la vez.** Que empezar algo nuevo sea fácil es justo lo que
mata un plan largo: el tema nuevo siempre es más emocionante que el módulo 14 del actual. Lo que
no es caso (a) va a *Intereses aparcados* en `PISTAS.md` hasta que el estudiante termine un
bloque, salvo que decida conscientemente cambiar de pista principal. El caso (a) es el preferido cuando
aplica: usa el interés nuevo como gasolina para el roadmap en vez de competir con él.

Se le explica al estudiante en qué caso cae y por qué, y **decide él**.

## 2. Crear una pista nueva

1. Investigar el currículo con fuentes reales: pensums universitarios del área, cursos abiertos
   de universidades reconocidas, y qué pide hoy el mercado si es un área profesional. Citar las
   fuentes al final del `ROADMAP.md`.
2. Decir explícitamente qué se deja fuera y por qué.
3. Crear `pistas/<nombre>/ROADMAP.md` con bloques y una tabla de módulos por bloque
   (`# | Módulo | Qué sabrás hacer al terminar`), recursos principales por bloque, y una sección
   "Cómo se recorre" que distinga tronco obligatorio de especializaciones.
4. Crear `PROGRESO.md` desde `plantillas/PROGRESO.md`.
5. Detallar **solo el primer bloque** en `bloques/` (ver §3).
6. Registrar la pista en `PISTAS.md`.

## 3. Detallar un bloque — justo a tiempo

No se detallan todos los módulos de una pista por adelantado: para cuando el estudiante llegue al
módulo 60, sus intereses, el mercado y las herramientas habrán cambiado. Regla: **el bloque en curso con
detalle completo, y el siguiente al menos esbozado.** Cuando el estudiante empieza el último
tercio de un bloque, se detalla el siguiente.

El detalle vive en `bloques/<Letra>-<nombre>.md`, con el formato de `plantillas/bloque.md`. Por
cada módulo:

- **Objetivos** con ID (`M07.3`), marcando con ★ los esenciales.
- **Prerrequisitos**: IDs de objetivos o módulos que deben estar al menos en `independiente`.
- **Misconceptions típicas**: los modelos mentales torcidos que el diagnóstico debe buscar.
- **Recursos**: 2–4, preferentemente gratuitos y de nivel universitario. Sin números de capítulo
  salvo que se hayan verificado: las ediciones cambian la numeración.
- **Sesiones estimadas** y una idea de ejemplo resuelto para los objetivos difíciles.

### Cómo se escribe un objetivo

- Empieza con un **verbo observable**: explicar, predecir, escribir, elegir y justificar,
  diagnosticar, rastrear. Nunca "entender" o "conocer": no se pueden comprobar.
- Debe poder verificarse con un ejercicio concreto. Si no se te ocurre cómo evaluarlo, está mal
  escrito.
- 3–6 por módulo. Más de 6 significa que el módulo debería partirse.
- Esencial (★) = sin él, los módulos siguientes se caen.

Mal: *"Entender los diccionarios."*
Bien: *"Elegir entre `list`, `dict` y `set` para un problema dado y justificar la elección."*

## 4. Estructura de un módulo

```
modulo-NN-nombre/
├── 00-diagnostico.md     ← preguntas que se responden en el chat ANTES de leer la lección
├── 01-leccion.md         ← el material de referencia
├── 02-ejercicios.md      ← secuencia con desvanecimiento
├── 03-tarea.md           ← independiente + transferencia, para después de la sesión
├── 04-por-dentro.md      ← cómo funciona realmente
├── mis-notas.md          ← lo escribe el estudiante, de memoria (desde plantillas/mis-notas.md)
├── codigo/               ← solo en pistas de programación: el código del estudiante
├── mis-respuestas/       ← sus respuestas literales, antes de corregir
└── soluciones/           ← las correcciones comentadas
```

Los archivos se crean cuando se van necesitando, no todos de golpe.

## 5. El diagnóstico (`00-diagnostico.md`)

- 1–3 preguntas por objetivo esencial. Cortas. Sin calificar, y se dice explícitamente.
- Para objetivos genuinamente nuevos: **predicciones** ("¿qué crees que imprime esto?"), nunca
  "¿qué sabes de X?".
- Se presenta en el chat al empezar el módulo, antes de que el estudiante abra la lección. Sus respuestas
  deciden qué partes de la lección se enseñan a fondo, cuáles se repasan rápido y cuáles se saltan.

## 6. La lección (`01-leccion.md`)

- Encabezado con los **objetivos del módulo** y sus IDs.
- Una sección por objetivo o grupo de objetivos, en este orden:
  1. un **ejemplo concreto** o un problema que el concepto resuelve;
  2. la **intuición** o una analogía;
  3. la **definición** formal;
  4. un **ejemplo resuelto** paso a paso, con código ejecutable;
  5. el **error típico**: qué se rompe, el traceback real, por qué pasa, cómo se arregla.
- Los misconceptions típicos del bloque se atacan de frente, con un contraejemplo que los rompa.
- Tono: directo, con humor cuando cabe. Nunca condescendiente, nunca solemne.
- Cerrar con un resumen de una línea por objetivo.
- Si el perfil declara restricciones de contenido, las conexiones con lo real van en el chat,
  nunca en el archivo (SKILL.md §11).
- La lección es **material de consulta**, no un guion para leer en voz alta. En la sesión solo se
  enseña a fondo lo que el diagnóstico mostró que falta.

## 7. Los ejercicios (`02-ejercicios.md`)

Secuencia con **desvanecimiento de la ayuda**, cada ejercicio etiquetado con su objetivo y nivel:

| Nivel | Forma |
|---|---|
| **Resuelto** | El tutor lo resuelve completo y comenta cada paso. El estudiante solo lo estudia |
| **Parcial** | Mismo tipo de problema con huecos que el estudiante completa |
| **Con pista** | Problema completo, con una pista explícita |
| **Independiente** | Problema sin ayuda |
| **Transferencia** | Contexto distinto que exige el concepto sin nombrarlo |

- Uno o dos resueltos como mucho: después el estudiante produce.
- En temas sencillos o ya diagnosticados como conocidos, se empieza más arriba en la escalera.
- Cada bloque de ejercicios incluye al menos una pregunta de **autoexplicación** ("¿por qué…?",
  "¿qué pasaría si…?").
- **Nunca** hay soluciones en este archivo. Van a `soluciones/` después de que el estudiante responda.

Ejemplo de desvanecimiento, recursión:
1. Resuelto: factorial, explicando cada llamada.
2. Parcial: completar tres huecos en una suma recursiva de lista.
3. Con pista: contar elementos de una lista anidada ("pista: ¿cuál es el caso más pequeño?").
4. Independiente: Fibonacci.
5. Transferencia: profundidad de un árbol de carpetas, sin mencionar la palabra "recursión".

## 8. La tarea (`03-tarea.md`)

Un problema independiente más grande y uno de transferencia. Se corrige al inicio de la siguiente
sesión, antes de cualquier otra cosa.

## 9. Fuentes

- **Fundamentos:** libros universitarios reconocidos, cursos abiertos de universidades,
  artículos revisados por pares, estándares técnicos.
- **Tecnología:** documentación oficial, especificaciones, RFC.
- Preferir material **gratuito** salvo que el perfil diga otra cosa, y marcar como "(de pago)"
  lo que no lo sea.
- Verificar en la web lo que dependa de versiones antes de escribirlo.
- Todo archivo respeta las restricciones de contenido del perfil, si las hay (SKILL.md §11).
