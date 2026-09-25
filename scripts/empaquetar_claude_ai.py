"""Genera el .zip de la skill para subirla a claude.ai (Customize > Skills).

Uso:
  python3 scripts/empaquetar_claude_ai.py              # (re)genera descargas/tutor-claude-ai.zip
  python3 scripts/empaquetar_claude_ai.py --verificar  # falla si el .zip publicado está desactualizado

La skill fuente es la del plugin de Claude Code. claude.ai exige cosas distintas, así que el
empaquetado:
  - usa `name: tutor` y una descripción de 200 caracteres como máximo (el límite de claude.ai);
  - quita `allowed-tools`, que es propio de Claude Code;
  - cambia las rutas `${CLAUDE_SKILL_DIR}/…` por rutas relativas a la carpeta de la skill;
  - pone la carpeta de la skill como raíz del .zip, como pide claude.ai.

El .zip es determinista (orden y fechas fijos): el mismo código siempre da los mismos bytes, y así
--verificar puede comparar sin falsos positivos.
"""
import io
import re
import sys
import zipfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parent.parent
FUENTE = RAIZ / 'plugins/tutor/skills/estudiar'
SALIDA = RAIZ / 'descargas/tutor-claude-ai.zip'
NOMBRE = 'tutor'
DESCRIPCION = ('Tutor para aprender cualquier tema con un plan, ejercicios y repasos. Úsalo cuando '
               'alguien quiera aprender algo, seguir su curso, repasar o pedir un examen, o suba su '
               'cuaderno.md.')
LIMITE_DESCRIPCION = 200
NOTA_RUTAS = ('> En claude.ai, las rutas `references/…` y `plantillas/…` son relativas a la carpeta '
              'de esta skill.\n')
FECHA_FIJA = (1980, 1, 1, 0, 0, 0)


def adaptar(ruta_relativa: str, texto: str) -> str:
    texto = texto.replace('${CLAUDE_SKILL_DIR}/', '')
    if ruta_relativa == 'SKILL.md':
        m = re.match(r'^---\n.*?\n---\n', texto, re.S)
        if not m:
            raise SystemExit('SKILL.md no tiene frontmatter')
        cuerpo = texto[m.end():]
        cuerpo = cuerpo.replace('# Tutor adaptativo\n', '# Tutor adaptativo\n\n' + NOTA_RUTAS, 1)
        texto = f'---\nname: {NOMBRE}\ndescription: {DESCRIPCION}\n---\n' + cuerpo
    return texto


def construir() -> bytes:
    if len(DESCRIPCION) > LIMITE_DESCRIPCION:
        raise SystemExit(f'La descripción tiene {len(DESCRIPCION)} caracteres; claude.ai admite {LIMITE_DESCRIPCION}.')
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w', zipfile.ZIP_DEFLATED) as z:
        for archivo in sorted(p for p in FUENTE.rglob('*') if p.is_file() and p.name != '.DS_Store'):
            rel = archivo.relative_to(FUENTE).as_posix()
            info = zipfile.ZipInfo(f'{NOMBRE}/{rel}', date_time=FECHA_FIJA)
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o644 << 16
            z.writestr(info, adaptar(rel, archivo.read_text(encoding='utf-8')).encode('utf-8'))
    return buffer.getvalue()


def main() -> int:
    nuevo = construir()
    if '--verificar' in sys.argv:
        if not SALIDA.exists():
            print(f'✗ no existe {SALIDA.relative_to(RAIZ)}: ejecuta scripts/empaquetar_claude_ai.py')
            return 1
        if SALIDA.read_bytes() != nuevo:
            print(f'✗ {SALIDA.relative_to(RAIZ)} está desactualizado: ejecuta scripts/empaquetar_claude_ai.py')
            return 1
        print(f'✓ {SALIDA.relative_to(RAIZ)} está al día')
        return 0
    SALIDA.parent.mkdir(exist_ok=True)
    SALIDA.write_bytes(nuevo)
    print(f'✓ generado {SALIDA.relative_to(RAIZ)} ({len(nuevo) / 1024:.1f} KB)')
    return 0


if __name__ == '__main__':
    sys.exit(main())
