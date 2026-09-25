"""Valida la estructura del marketplace y del plugin antes de publicar.

Uso:  python3 scripts/validar.py [raíz-del-repo]

Comprueba lo que exige la documentación de Claude Code (JSON válido, campos obligatorios,
nombres en kebab-case, rutas existentes, frontmatter de cada skill) y además que toda
referencia cruzada entre archivos de la skill apunte a algo que existe. Si tienes el CLI
de Claude Code, complementa con:  claude plugin validate .
"""
import json
import re
import sys
from pathlib import Path

root = Path(sys.argv[1] if len(sys.argv) > 1 else '.').resolve()
errores = []
KEBAB = re.compile(r'^[a-z0-9]+(-[a-z0-9]+)*$')
# Archivos que viven en el repo de estudio de cada persona, no dentro de la skill.
ARCHIVOS_DEL_ESTUDIANTE = {'mis-notas', 'bloque'}


def err(msg):
    errores.append(msg)


def leer_json(ruta):
    try:
        return json.loads(ruta.read_text(encoding='utf-8'))
    except FileNotFoundError:
        err(f'no existe {ruta.relative_to(root)}')
    except json.JSONDecodeError as e:
        err(f'{ruta.relative_to(root)} no es JSON válido: {e}')
    return {}


mp = leer_json(root / '.claude-plugin/marketplace.json')
for campo in ('name', 'owner', 'plugins'):
    if campo not in mp:
        err(f'marketplace.json: falta "{campo}"')
if mp and not KEBAB.match(mp.get('name', '')):
    err('marketplace.json: "name" no es kebab-case')
if mp and not mp.get('owner', {}).get('name'):
    err('marketplace.json: falta owner.name')

for entrada in mp.get('plugins', []):
    nombre = entrada.get('name', '')
    if not KEBAB.match(nombre):
        err(f'plugin "{nombre}": name no es kebab-case')
    src = root / entrada.get('source', '')
    if not src.is_dir():
        err(f'plugin "{nombre}": source {entrada.get("source")!r} no existe')
        continue

    pj = leer_json(src / '.claude-plugin/plugin.json')
    for campo in ('name', 'description', 'version'):
        if pj and campo not in pj:
            err(f'plugin.json: falta "{campo}"')
    if pj and pj.get('name') != nombre:
        err(f'plugin.json name {pj.get("name")!r} no coincide con el marketplace ({nombre!r})')
    if pj and not re.match(r'^\d+\.\d+\.\d+$', pj.get('version', '')):
        err('plugin.json: version no es semver (X.Y.Z)')
    if pj and not pj.get('author', {}).get('name'):
        err('plugin.json: falta author.name')

    skills = sorted((src / 'skills').glob('*/SKILL.md'))
    if not skills:
        err(f'plugin "{nombre}": no tiene ninguna skills/*/SKILL.md')
    for sk in skills:
        d = sk.parent
        texto = sk.read_text(encoding='utf-8')
        m = re.match(r'^---\n(.*?)\n---\n', texto, re.S)
        if not m:
            err(f'{sk.relative_to(root)}: frontmatter ausente o mal cerrado')
            continue
        fm = m.group(1)
        # Solo claves YAML, continuaciones indentadas o líneas vacías. Si aparece markdown
        # (un título '#', por ejemplo), falta el '---' de cierre y se leyó parte del cuerpo.
        malas = [l for l in fm.splitlines() if l.strip() and not re.match(r'^([a-z][\w-]*:|\s)', l)]
        if malas:
            err(f'{sk.relative_to(root)}: frontmatter sin cerrar o inválido ({malas[0][:50]!r})')
            continue
        claves = dict(re.findall(r'^([a-z][\w-]*):\s*(.*)$', fm, re.M))
        if 'description' not in claves:
            err(f'{sk.relative_to(root)}: falta description')
        if claves.get('name') and claves['name'] != d.name:
            err(f'{sk.relative_to(root)}: name {claves["name"]!r} no coincide con la carpeta {d.name!r}')
        print(f'skill: /{nombre}:{d.name}  ({len(texto.splitlines())} líneas)')

        textos = {f: f.read_text(encoding='utf-8') for f in d.rglob('*.md')}
        for f, txt in textos.items():
            for ref in set(re.findall(r'((?:references|plantillas)/[\w\-]+\.md)', txt)):
                if not (d / ref).exists():
                    err(f'{f.relative_to(d)} menciona {ref}, que no existe')
            # Menciones sueltas en minúsculas (`autoria.md`) deben existir en references/ o
            # plantillas/. Las del repo de estudio (PERFIL.md, 01-leccion.md…) no se validan aquí.
            for ref in set(re.findall(r'(?<![/\w-])([a-z][a-z-]*)\.md\b', txt)):
                if ref not in ARCHIVOS_DEL_ESTUDIANTE and not (
                        (d / 'references' / f'{ref}.md').exists() or (d / 'plantillas' / f'{ref}.md').exists()):
                    err(f'{f.relative_to(d)} menciona {ref}.md, que no está en references/ ni plantillas/')
        secciones = set(re.findall(r'^## (\d+)\.', textos[sk], re.M))
        for f, txt in textos.items():
            citas = set(re.findall(r'SKILL\.md §(\d+)', txt))
            if f == sk:
                citas |= set(re.findall(r'\(§(\d+)[\.\)]', txt))
            for n in citas:
                if n not in secciones:
                    err(f'{f.relative_to(d)} cita §{n}, que no existe en SKILL.md')

# El .zip para claude.ai: al día con la fuente, y con la forma que exige claude.ai.
import subprocess
import zipfile
zip_path = root / 'descargas/tutor-claude-ai.zip'
r = subprocess.run([sys.executable, str(root / 'scripts/empaquetar_claude_ai.py'), '--verificar'],
                   capture_output=True, text=True)
if r.returncode != 0:
    err((r.stdout + r.stderr).strip().lstrip('✗ '))
elif zip_path.exists():
    with zipfile.ZipFile(zip_path) as z:
        nombres = z.namelist()
        raices = {n.split('/')[0] for n in nombres}
        if len(raices) != 1:
            err(f'el .zip de claude.ai debe tener una sola carpeta raíz; tiene {sorted(raices)}')
        raiz_zip = next(iter(raices))
        if f'{raiz_zip}/SKILL.md' not in nombres:
            err('el .zip de claude.ai no tiene SKILL.md dentro de su carpeta raíz')
        else:
            sk = z.read(f'{raiz_zip}/SKILL.md').decode('utf-8')
            fm = re.match(r'^---\n(.*?)\n---\n', sk, re.S)
            meta = dict(re.findall(r'^([a-z][\w-]*):\s*(.*)$', fm.group(1), re.M)) if fm else {}
            if meta.get('name') != raiz_zip:
                err(f'claude.ai: name {meta.get("name")!r} no coincide con la carpeta raíz {raiz_zip!r}')
            if len(meta.get('description', '')) > 200:
                err(f'claude.ai: la descripción tiene {len(meta["description"])} caracteres (máximo 200)')
            if 'allowed-tools' in meta:
                err('claude.ai: el SKILL.md empaquetado no debe llevar allowed-tools')
        restos = [n for n in nombres if '${CLAUDE_SKILL_DIR}' in z.read(n).decode('utf-8', 'ignore')]
        if restos:
            err(f'claude.ai: quedan rutas ${{CLAUDE_SKILL_DIR}} en {restos}')
    print(f'zip claude.ai: {len(nombres)} archivos en {raiz_zip}/')

print()
print('\n'.join(f'✗ {e}' for e in errores) or '✓ Sin errores')
sys.exit(1 if errores else 0)
