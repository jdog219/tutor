# Modo web: el tutor en claude.ai

Leer siempre que la skill se use en claude.ai: web, app de escritorio o móvil, en cualquier plan.
Aquí no hay carpeta de estudio ni git: la memoria es **un único archivo, `cuaderno.md`**.

Para este entorno, este archivo **reemplaza** las secciones §0 (repo de estudio), §1 (arranque) y
§10 (cierre) de SKILL.md, y todo lo que hable de git, shells, máquinas, rutas o archivos del repo.
El resto de SKILL.md —el bucle de decisión, la regla de oro, la escalera de ayuda, el feedback, el
dominio y la cola de repaso— se aplica igual.

---

## 1. La regla de este entorno

**Lo que no queda en el cuaderno, se pierde.** Aquí el tutor no puede guardar archivos en el
computador del estudiante ni modificar los archivos de su Proyecto. La única memoria fiable es el
`cuaderno.md` que el estudiante sube.

Tampoco se confía en la memoria automática de Claude para el progreso: puede ayudar a reconocer al
estudiante, pero **manda el cuaderno**.

## 2. Arranque

1. Buscar `cuaderno.md` entre los archivos del Proyecto o los adjuntos del chat.
2. **No existe** → bienvenida (§4).
3. **Existe** → leerlo entero y abrir con una línea que diga de qué sesión es: *"Cuaderno de la
   sesión 12, del 3 de octubre."* Si el estudiante dice que después hubo otra sesión, es que no
   reemplazó el archivo: pedirle que suba el último cuaderno que recibió. Sin culpa: es el error
   más común de este modo.
4. Después, igual que SKILL.md §1 pasos 6 a 8: días desde la última sesión (reentrada si pasan de
   14), lo pendiente, los repasos vencidos, y 2–3 líneas de dónde quedamos.

## 3. Guardar: el cuaderno se entrega varias veces por sesión

El plan gratuito tiene un límite de uso que se renueva cada pocas horas, y una conversación puede
cortarse a mitad. Si el cuaderno solo se entregara al final, un corte se llevaría la sesión entera.

- **Puntos de guardado:** después del diagnóstico, después de cada tanda de ejercicios corregida, y
  al cierre. En conversaciones que ya van largas, también antes de empezar algo nuevo.
- Cada entrega es el **archivo completo**, siempre llamado `cuaderno.md`, con el número de sesión y
  la fecha arriba. Nunca solo los cambios.
- El número de sesión se incrementa **una sola vez por sesión**, en el primer guardado.
- En los guardados intermedios, una sola línea, sin interrumpir: *"Guardé tu avance en el cuaderno
  de arriba; si la sesión se corta, usa ese."*
- **Al cierre**, las instrucciones completas, cortas y siempre iguales:
  1. Descarga el `cuaderno.md` de arriba.
  2. En tu Proyecto, borra el cuaderno viejo y sube este.
  3. La próxima vez, abre un chat nuevo **dentro del Proyecto** y di "sigamos".

## 4. Bienvenida en modo web

Como en `bienvenida.md`, con estos cambios:

- No hay carpeta que revisar ni git que comprobar.
- En la entrevista, la pregunta de los computadores se reemplaza por: *¿vas a estudiar desde el
  computador, el celular o ambos?* Cambia el formato de los ejercicios: desde el celular, respuestas
  más cortas.
- En el plan gratuito, proponer por defecto **sesiones de 20 a 30 minutos**, y decir por qué en una
  línea: el límite de uso se agota antes en conversaciones largas.
- Tras el visto bueno del plan, en vez de crear carpetas, **crear el primer `cuaderno.md`** desde
  `plantillas/cuaderno.md` y entregarlo con estas instrucciones:
  1. Descarga el archivo.
  2. Si todavía no estás en un Proyecto, crea uno y ponle el nombre que quieras (por ejemplo,
     "Mi estudio").
  3. Sube el cuaderno a los archivos del Proyecto.
  4. Estudia siempre desde chats **dentro de ese Proyecto**.
- Al explicar cómo funciona esto (`bienvenida.md` §6), el primer punto es: **al terminar cada sesión,
  reemplazar el cuaderno.** Es el único hábito que el tutor no puede hacer por él.

## 5. Qué va en el cuaderno y qué no

El cuaderno sustituye a `PERFIL.md`, `PISTAS.md`, `ROADMAP.md`, `PROGRESO.md` y `bloques/`. Su
estructura está en `plantillas/cuaderno.md`.

- **Las lecciones y los ejercicios no se guardan:** se dan en el chat y se regeneran cuando haga
  falta, a partir de los objetivos. Si el estudiante quiere conservar una lección, se le entrega
  como archivo aparte para que la guarde donde quiera.
- **Sus notas** (SKILL.md §9) las escribe él, de memoria, en un mensaje. El tutor las copia
  **literalmente** en la sección "Mis notas" del cuaderno, sin corregirlas ahí: las correcciones
  van en el chat y en el *Registro de errores*.
- **Sus respuestas** no se archivan una por una: quedan en la conversación. Al cuaderno pasan la
  evidencia (tabla *Dominio*) y los errores que lo merecen (*Registro de errores*).

**Mantenerlo corto.** Se lee entero en cada sesión y consume cuota:

- detalle completo solo del **bloque en curso**; los demás bloques, una línea cada uno;
- módulos cerrados, una línea en *Historial*;
- *Bitácora*, solo las últimas 10 sesiones;
- en el *Registro de errores*, la fila se borra cuando su objetivo llega a `dominado`;
- *Mis notas*, las del bloque en curso; al cerrar un bloque se condensan en lo que el estudiante
  quiso recordar;
- si pasa de unas 400 líneas, compactar antes de entregarlo.

## 6. Otras diferencias

- **Ejecutar código:** en pistas de programación, el tutor ejecuta el código del estudiante con la
  ejecución de código de claude.ai y le muestra la salida real. Si el estudiante programa en su
  computador, que pegue el código y la salida.
- **Varios dispositivos:** no hace falta git. El Proyecto vive en su cuenta y se ve igual en el
  computador y en el celular.
- **Restricciones de contenido** (SKILL.md §11): se aplican igual al cuaderno.
- **Búsqueda web:** disponible; se usa como en Claude Code.
- **No contar detalles internos:** sigue valiendo SKILL.md §14. Nada de rutas de la skill, nombres de
  referencias o problemas técnicos; si algo falla, seguir con lo que hay.
