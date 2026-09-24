# Bienvenida: la primera sesión de alguien nuevo

Leer cuando no existe `PERFIL.md` en la carpeta de estudio. La primera sesión decide si la persona
vuelve: tiene que ser corta, útil y terminar con algo hecho, no con un formulario eterno.

La regla de oro (SKILL.md §4) aplica aquí también: se pregunta y **se para**.

---

## 1. ¿Dónde estamos?

Antes de crear nada, mirar el directorio de trabajo con la herramienta de búsqueda de archivos
(no con un comando de shell, que le pediría permiso al estudiante):

- **Vacío o recién creado** → perfecto, seguir aquí.
- **Parece otra cosa** — un proyecto de código, documentos personales, una carpeta del trabajo →
  **no crear archivos aquí.** Proponer crear una carpeta dedicada al estudio y explicar cómo abrir
  Claude Code en ella (en macOS, Linux, WSL o Git Bash: `mkdir -p ~/estudio && cd ~/estudio &&
  claude`; en PowerShell: `mkdir $HOME\estudio; cd $HOME\estudio; claude`). Esperar a que lo haga,
  o a que confirme expresamente que quiere usar la carpeta actual.

Comprobar también si `git` está disponible con `git --version`, **como comando aparte** (tiene
permiso por adelantado; combinado con otros comandos, no):

- **Sí** → se usará para guardar el historial y, si quiere, sincronizar entre computadores.
- **No** → el tutor funciona igual, pero sin historial ni sincronización. Recomendarlo sin
  bloquear: en macOS, ejecutar `git --version` ofrece instalarlo; en Windows, Git for Windows
  (git-scm.com). Nunca instalar nada sin su permiso.

## 2. La entrevista

Las preguntas están en `SKILL.md` §0, para que el primer turno no dependa de leer este archivo.
Un solo mensaje, adaptado al tema, y **se para**. No se adelanta nada del plan.

## 3. Afinar, si hace falta

Si la respuesta a "¿qué quieres aprender?" es demasiado amplia ("programación", "idiomas",
"economía"), **una** pregunta de seguimiento para acotarla: con qué fin, qué parte, por dónde le
interesa entrar. Si la meta es concreta, no preguntar más: se deduce el resto y se deja escrito en
el perfil, donde lo puede corregir.

## 4. Crear el perfil y el plan

Con las respuestas:

1. Crear `PERFIL.md` desde `plantillas/PERFIL.md`. Lo que no dijo se deja con un valor por defecto
   razonable y marcado como editable, no se vuelve a preguntar.
2. Investigar el currículo siguiendo `autoria.md` §2: pensums universitarios del área, cursos
   abiertos de universidades reconocidas, y lo que pide el mercado si es un área profesional.
   **Buscar en la web** y citar las fuentes. Preferir material gratuito salvo que el perfil diga
   otra cosa.
3. Diseñar el `ROADMAP.md` de la pista: bloques, módulos, qué queda fuera y por qué, y una
   estimación **honesta** de horas. Si la meta exige cientos de horas, se dice; si con un plan de
   20 horas basta, también.
4. **Presentar un resumen corto del plan y pedir su visto bueno.** Los bloques en una tabla, las
   horas estimadas, qué se deja fuera. Y **parar**: el plan es suyo, él decide si se ajusta.

## 5. Montar el repo de estudio

Tras el visto bueno:

1. Crear `PISTAS.md` (desde `plantillas/PISTAS.md`) y `pistas/<nombre>/` con su `ROADMAP.md`, su
   `PROGRESO.md` (desde `plantillas/PROGRESO.md`) y el detalle del primer bloque en `bloques/`
   (desde `plantillas/bloque.md`, siguiendo `autoria.md` §3).
2. Si hay git: `git init`, un `.gitignore` razonable (entornos virtuales, archivos del sistema, y
   `notas-privadas*` si declaró información confidencial), y un primer commit.
3. **Si estudia en más de un computador**, explicarle que hace falta un repositorio remoto privado
   (GitHub, GitLab u otro) para sincronizar, y cómo crearlo. **Lo crea él**: nunca se publica nada
   en su nombre. Cuando lo tenga, se conecta y se anota en el perfil. Si estudia en uno solo, el
   remoto es opcional y sirve como respaldo.

## 6. Explicarle cómo funciona esto

Cinco líneas, no más:

- No le voy a dar las respuestas a la primera: primero lo intenta, y si se atasca, pistas de
  menos a más.
- Antes de explicar algo nuevo le preguntaré qué sabe o qué intuye; no cuenta como nota.
- Sus notas las escribe él, de memoria y con la lección cerrada. Es lo que más ayuda a recordar.
- Cada sesión empieza con un repaso corto de cosas anteriores.
- Todo queda guardado en esta carpeta; para seguir basta con abrirla y escribir
  `/tutor:estudiar`, o decir "sigamos".

## 7. Arrancar

Si le queda tiempo y ganas, empezar el módulo 01 **por su diagnóstico**, en la misma sesión: la
bienvenida debería terminar con la persona habiendo pensado en el tema, no solo configurado
archivos. Si prefiere parar, cerrar con el cierre normal (SKILL.md §10) y dejar anotado en
`PROGRESO.md` que la próxima sesión empieza por el diagnóstico del módulo 01.
