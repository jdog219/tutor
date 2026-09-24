# Tutor — estudia lo que quieras, con un tutor que no te regala las respuestas

Un plugin para [Claude Code](https://code.claude.com/docs) que convierte a Claude en un tutor
personal para **cualquier tema**: programación, matemáticas, historia, un idioma, finanzas…
Tú dices qué quieres aprender y para qué; el tutor investiga un plan de estudio, te enseña paso a
paso y guarda tu progreso en una carpeta tuya, para que cada sesión siga donde quedó la anterior.

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

## Requisitos

- **Claude Code** con un plan de pago de Claude (Pro, Max, Team o Enterprise) o una cuenta de
  Console. El plan gratuito no incluye Claude Code.
- **git**, recomendado: guarda el historial de tu estudio y permite sincronizarlo entre
  computadores. Sin git el tutor funciona igual, pero sin historial.

---

## Instalación en Mac

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

---

## Instalación en Windows

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

---

## Primer uso

Dentro de tu carpeta de estudio, en Claude Code:

```
/tutor:estudiar quiero aprender <lo que sea>
```

El tutor te hará unas pocas preguntas (qué, para qué, cuánto sabes, cuánto tiempo tienes),
investigará un plan de estudio con fuentes, te lo mostrará para que lo apruebes o lo ajustes, y
creará tu carpeta de estudio. Si te queda tiempo, empiezas la primera lección ese mismo día.

## Seguir estudiando

Abre Claude Code en tu carpeta de estudio y escribe:

```
/tutor:estudiar
```

O simplemente di *"sigamos"*. El tutor lee dónde quedaste, corrige lo pendiente, te hace los
repasos que tocan y continúa. También puedes pedirle *"quiero repasar"*, *"ponme un examen"* o
*"quiero aprender otra cosa"*.

## Tu carpeta de estudio

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

## Estudiar en dos computadores

Crea un repositorio **privado** en GitHub (o GitLab, u otro) y dile al tutor que quieres
sincronizar: él conectará tu carpeta y, a partir de ahí, traerá los cambios al empezar cada sesión
y los subirá al terminar. En el otro computador instalas Claude Code y el plugin igual que arriba,
y clonas ese repositorio en vez de crear una carpeta vacía.

## Actualizaciones

El plugin se actualiza solo. Si quieres forzarlo:

```
/plugin marketplace update jdog219-tutor
```

## Privacidad

Tu progreso vive en tu carpeta; el plugin no lo sube a ningún sitio por su cuenta. Si usas un
repositorio remoto, que sea **privado**. Si estudias con material confidencial (de tu trabajo, por
ejemplo), díselo al tutor en la bienvenida: escribirá los archivos con ejemplos ficticios y hablará
de lo real solo en el chat.

## Licencia

[MIT](LICENSE).
