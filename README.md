# Tutor — estudia lo que quieras, con un tutor que no te regala las respuestas

Convierte a Claude en un tutor personal para **cualquier tema**: programación, matemáticas,
historia, un idioma, un instrumento, finanzas… Tú dices qué quieres aprender y para qué; el tutor
investiga un plan de estudio, te enseña paso a paso y guarda tu progreso, para que cada sesión siga
donde quedó la anterior.

**Funciona con el plan gratuito de Claude.** Hay dos formas de usarlo; mira cuál te conviene antes
de instalar nada.

## Cómo enseña

- **Pregunta antes de explicar.** No te repite lo que ya sabes, y encuentra las ideas equivocadas
  antes de construir encima.
- **No te da la respuesta a la primera.** Primero lo intentas; si te atascas, pistas de menos a más.
- **Recuerda qué dominas y qué no**, objetivo por objetivo, y te hace repasar cada cosa justo
  cuando empieza a olvidarse.
- **Tus notas las escribes tú**, de memoria. El tutor las lee y corrige lo que entendiste mal.
- **Tú decides el ritmo.** Si desapareces tres semanas, vuelves sin sermones.

Se basa en técnicas con buen respaldo en la investigación sobre aprendizaje: práctica de
recuperación, repaso espaciado, ejemplos resueltos que se retiran poco a poco, autoexplicación y
feedback sobre el razonamiento.

---

## Dos formas de usarlo

| | **En claude.ai** | **En Claude Code** |
|---|---|---|
| **Plan de Claude** | **Cualquiera, incluido el gratuito** | De pago: Pro, Max, Team o Enterprise (o Console) |
| **Dónde** | Navegador, app de escritorio o celular | Terminal, o la pestaña Code de la app de escritorio |
| **Instalación** | Subir un archivo `.zip` (2 minutos) | Instalar Claude Code y el plugin (5 minutos) |
| **Cómo recuerda tu progreso** | En un archivo, `cuaderno.md`, que **reemplazas tú** al terminar cada sesión | Solo: guarda los archivos en una carpeta de tu computador |
| **Varios dispositivos** | Automático: tu Proyecto está en tu cuenta | Con un repositorio git privado |
| **Duración de las sesiones** | Cortas en el plan gratuito (20–30 min), por el límite de uso | Las que quieras |
| **Actualizaciones** | Descargas el `.zip` nuevo y lo vuelves a subir | Automáticas |

**¿Cuál elijo?** Si no pagas Claude, o no has usado nunca una terminal: **claude.ai**. Si tienes un
plan de pago y quieres que todo se guarde solo: **Claude Code**. La forma de enseñar es la misma en
las dos.

---

## Opción 1 — En claude.ai (incluido el plan gratuito)

### Instalación, una sola vez

**1.** Descarga la skill: **[tutor-claude-ai.zip](https://github.com/jdog219/tutor/raw/main/descargas/tutor-claude-ai.zip)**.
No lo descomprimas.

**2.** En [claude.ai](https://claude.ai), abre **Settings → Capabilities** y activa **Code execution
and file creation**. Sin esto, las skills no funcionan.

**3.** Ve a **Customize → Skills**, pulsa **+**, luego **Create skill → Upload a skill**, y sube el
`.zip`. Comprueba que el tutor quede activado en tu lista de skills.

> Si tu cuenta está en español, esos menús pueden aparecer traducidos.

### Primer uso

**4.** Crea un **Proyecto** (en el menú lateral, *Projects*) y ponle el nombre que quieras, por
ejemplo "Mi estudio". Todo tu estudio vivirá ahí.

**5.** Abre un chat **dentro de ese Proyecto** y escribe:

> quiero aprender <lo que sea>

El tutor te hará unas pocas preguntas, investigará un plan de estudio con fuentes y te lo mostrará
para que lo apruebes o lo ajustes. Cuando lo apruebes, te dará tu primer **`cuaderno.md`**.

**6.** Descarga ese `cuaderno.md` y súbelo a los **archivos del Proyecto**.

### El cuaderno: el único hábito que depende de ti

En claude.ai, Claude no puede guardar archivos por su cuenta. **Tu progreso vive en `cuaderno.md`**,
y solo se conserva si lo actualizas tú:

1. Al terminar cada sesión, el tutor te entrega el cuaderno actualizado.
2. Descárgalo.
3. En tu Proyecto, **borra el cuaderno viejo y sube el nuevo**.

Si te olvidas, la siguiente sesión empezará desde tu cuaderno anterior y lo de ese día se perderá.
El tutor te lo recuerda siempre al cerrar, y te dice de qué sesión es el cuaderno que está leyendo,
para que notes si subiste uno viejo.

**Si la sesión se corta a mitad** (por ejemplo, porque llegaste al límite del plan gratuito), no
pasa nada grave: durante la sesión el tutor te va entregando el cuaderno varias veces. Usa el
último que te haya dado.

### Seguir estudiando

Abre un chat nuevo **dentro de tu Proyecto** y di *"sigamos"*. También puedes pedirle *"quiero
repasar"*, *"ponme un examen"* o *"quiero aprender otra cosa"*.

### Sobre el plan gratuito

El plan gratuito tiene un límite de uso que se renueva cada pocas horas, y las conversaciones
largas lo gastan antes. Por eso el tutor te propondrá sesiones de 20 a 30 minutos. Estudiar poco y
seguido es, además, de lo que mejor funciona para recordar.

### Actualizar el tutor

En claude.ai las skills no se actualizan solas. Cuando haya una versión nueva, descarga el `.zip`
otra vez (el mismo enlace de arriba), borra el tutor de tu lista de skills y sube el nuevo. Tu
cuaderno no se toca: vive en tu Proyecto.

---

## Opción 2 — En Claude Code (plan de pago)

### Requisitos

- **Claude Code**, con un plan de pago de Claude (Pro, Max, Team o Enterprise) o una cuenta de
  Console. El plan gratuito no incluye Claude Code.
- **git**, recomendado: guarda el historial de tu estudio y permite sincronizarlo entre
  computadores. Sin git el tutor funciona igual, pero sin historial.

### Instalación en Mac

**1.** Instala Claude Code. Abre la app **Terminal** y pega:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

**2.** Comprueba que tienes git. Si no lo tienes, macOS te ofrecerá instalarlo:

```bash
git --version
```

**3.** Crea una carpeta para estudiar y abre Claude Code dentro de ella:

```bash
mkdir -p ~/estudio && cd ~/estudio && claude
```

La primera vez te pedirá iniciar sesión con tu cuenta de Claude.

**4.** Ya dentro de Claude Code, añade este catálogo e instala el plugin (una línea cada vez):

```
/plugin marketplace add jdog219/tutor
```

```
/plugin install tutor@jdog219-tutor
```

### Instalación en Windows

Claude Code funciona directamente en Windows; no necesitas WSL.

**1.** Instala **Git for Windows** desde [git-scm.com/downloads/win](https://git-scm.com/downloads/win),
con las opciones por defecto. Además de git, trae Git Bash, que Claude Code usa para ejecutar
comandos.

**2.** Instala Claude Code. Abre **PowerShell** (no hace falta hacerlo como administrador) y pega:

```powershell
irm https://claude.ai/install.ps1 | iex
```

**3.** Cierra y vuelve a abrir PowerShell. Crea una carpeta para estudiar y abre Claude Code en ella:

```powershell
mkdir $HOME\estudio; cd $HOME\estudio; claude
```

La primera vez te pedirá iniciar sesión con tu cuenta de Claude.

**4.** Ya dentro de Claude Code, añade este catálogo e instala el plugin (una línea cada vez):

```
/plugin marketplace add jdog219/tutor
```

```
/plugin install tutor@jdog219-tutor
```

> ¿Prefieres WSL? También funciona: instala Claude Code **dentro** de tu distribución Linux con el
> comando de la sección de Mac, y sigue desde el paso 3 de Mac.

### Primer uso

Dentro de tu carpeta de estudio, en Claude Code:

```
/tutor:estudiar quiero aprender <lo que sea>
```

El tutor te hará unas pocas preguntas (qué, para qué, cuánto sabes, cuánto tiempo tienes),
investigará un plan de estudio con fuentes, te lo mostrará para que lo apruebes o lo ajustes, y
creará tu carpeta de estudio. Si te queda tiempo, empiezas la primera lección ese mismo día.

### Seguir estudiando

Abre Claude Code en tu carpeta de estudio y escribe:

```
/tutor:estudiar
```

O simplemente di *"sigamos"*. El tutor lee dónde quedaste, corrige lo pendiente, te hace los
repasos que tocan y continúa.

### Tu carpeta de estudio

```
estudio/
├── PERFIL.md          ← quién eres y cómo estudias (edítalo cuando quieras)
├── PISTAS.md          ← qué estás estudiando y qué tienes aparcado
└── pistas/<tema>/
    ├── ROADMAP.md     ← tu plan completo
    ├── PROGRESO.md    ← qué dominas, qué repasar y cuándo
    └── modulo-01-…/   ← lecciones, ejercicios, tus respuestas, tus notas y las correcciones
```

Todo son archivos de texto normales. Puedes leerlos, editarlos o copiarlos cuando quieras.

### Estudiar en dos computadores

Crea un repositorio **privado** en GitHub (o GitLab, u otro) y dile al tutor que quieres
sincronizar: él conectará tu carpeta y, a partir de ahí, traerá los cambios al empezar cada sesión
y los subirá al terminar. En el otro computador instalas Claude Code y el plugin igual que arriba,
y clonas ese repositorio en vez de crear una carpeta vacía.

### Actualizaciones

El plugin se actualiza solo. Si quieres forzarlo:

```
/plugin marketplace update jdog219-tutor
```

---

## Privacidad

Tu progreso es tuyo: en claude.ai vive en tu Proyecto; en Claude Code, en tu carpeta. El tutor no
lo sube a ningún otro sitio. Si en Claude Code usas un repositorio remoto, que sea **privado**. Si
estudias con material confidencial (de tu trabajo, por ejemplo), díselo al tutor en la bienvenida:
escribirá tus archivos con ejemplos ficticios y hablará de lo real solo en el chat.

## Contribuir

Las mejoras son bienvenidas. La skill tiene una sola fuente, `plugins/tutor/skills/estudiar/`, y de
ahí salen las dos versiones. Antes de proponer un cambio:

1. Regenera el `.zip` de claude.ai:

```bash
python3 scripts/empaquetar_claude_ai.py
```

2. Comprueba que todo sigue siendo válido (incluido que el `.zip` esté al día):

```bash
python3 scripts/validar.py
```

3. Sube el número de `version` en `plugins/tutor/.claude-plugin/plugin.json`. Sin eso, quienes
   usan Claude Code no reciben el cambio.

## Licencia

[MIT](LICENSE).
