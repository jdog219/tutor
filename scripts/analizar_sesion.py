"""Resume una sesión de prueba de Claude Code: qué herramientas usó, qué permisos se negaron y qué
le respondió al estudiante.

Uso:
  claude -p "/tutor:estudiar quiero aprender X" --plugin-dir plugins/tutor \\
         --output-format stream-json --verbose < /dev/null > sesion.jsonl
  python3 scripts/analizar_sesion.py sesion.jsonl

Hazlo en una carpeta vacía: así ves la bienvenida tal como la vería alguien nuevo. Para un segundo
turno, repite el comando con --resume <session_id> (el id aparece al final de este resumen).
"""
import json
import sys


def main(ruta: str) -> None:
    eventos = [json.loads(l) for l in open(ruta, encoding='utf-8') if l.strip()]
    print('=== herramientas usadas ===')
    for e in eventos:
        contenido = e.get('message', {}).get('content')
        if e.get('type') == 'assistant':
            for c in contenido or []:
                if c.get('type') == 'tool_use':
                    i = c['input']
                    resumen = i.get('file_path') or i.get('command') or i.get('pattern') or json.dumps(i, ensure_ascii=False)
                    print(f'- {c["name"]}: {resumen[:110]}')
        if e.get('type') == 'user' and isinstance(contenido, list):
            for c in contenido:
                if c.get('type') == 'tool_result' and c.get('is_error'):
                    print(f'    ↳ DENEGADO/ERROR: {str(c.get("content"))[:110]}')
    r = next((e for e in eventos if e.get('type') == 'result'), {})
    negados = [d.get('tool_name') for d in r.get('permission_denials', [])]
    print(f'\nturnos {r.get("num_turns")} · {r.get("duration_ms", 0) / 1000:.0f}s · '
          f'costo estimado ${r.get("total_cost_usd", 0):.3f} · permisos negados: {negados or "ninguno"}')
    print(f'session_id: {r.get("session_id")}')
    print('\n=== respuesta al estudiante ===\n' + (r.get('result') or '(vacía)'))


if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    main(sys.argv[1])
