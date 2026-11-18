#!/usr/bin/env python3
"""Build index.html from src/template.html, src/charts.js and data/municipis.json.

    python3 src/build.py                    writes index.html (the complete page served by GitHub Pages)
    python3 src/build.py --fragment OUT     also writes the page without <html>/<head>/<body>
                                            (the form the Claude artifact version is published in)
"""
import pathlib
import sys

root = pathlib.Path(__file__).resolve().parent.parent
template = (root / 'src/template.html').read_text(encoding='utf-8')
data = (root / 'data/municipis.json').read_text(encoding='utf-8')
charts = (root / 'src/charts.js').read_text(encoding='utf-8')
assert '</' not in data and '</script' not in charts.lower()

page = template.replace('/*CHARTS*/', charts, 1).replace('/*DATA*/', data, 1)
head, body = page.split('<div id="app">', 1)
doc = (
    '<!doctype html>\n<html lang="ca">\n<head>\n<meta charset="utf-8">\n'
    '<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">\n'
    '<meta name="description" content="Mapa 3D de la població dels municipis de Catalunya, 1981–2026: '
    'com ha crescut el voltant de Barcelona.">\n'
    '<style>:root{padding-top:env(safe-area-inset-top);padding-bottom:env(safe-area-inset-bottom)}'
    'body{margin:0;font:14px system-ui}[hidden]{display:none!important}</style>\n'
    + head.rstrip() + '\n</head>\n<body>\n<div id="app">' + body.rstrip() + '\n</body>\n</html>\n'
)
(root / 'index.html').write_text(doc, encoding='utf-8')
print('index.html', len(doc.encode('utf-8')), 'bytes')

if '--fragment' in sys.argv:
    out = pathlib.Path(sys.argv[sys.argv.index('--fragment') + 1])
    out.write_text(page, encoding='utf-8')
    print(out.name, len(page.encode('utf-8')), 'bytes')
