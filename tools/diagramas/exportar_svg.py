"""Converte SVG renderizado em arquivo autocontido, sem fonts remotas/CSS vars."""
from pathlib import Path
import re
import sys
import xml.etree.ElementTree as ET

path = Path(sys.argv[1])
text = re.sub(r'<style>.*?</style>', '', path.read_text(encoding='utf-8'), flags=re.S)
values = {'--_text': '#1e293b', '--_text-sec': '#475569', '--_text-muted': '#64748b',
          '--_text-faint': '#94a3b8', '--_line': '#94a3b8', '--_arrow': '#64748b',
          '--_node-fill': '#eef2ff', '--_node-stroke': '#6366f1',
          '--_group-fill': '#ffffff', '--_group-hdr': '#f1f5f9',
          '--_inner-stroke': '#cbd5e1', '--_key-badge': '#e2e8f0',
          '--bg': '#ffffff', '--fg': '#1e293b'}
for name, value in values.items():
    text = text.replace('var(' + name + ')', value)
root = ET.fromstring(text)
root.set('style', 'background:#ffffff')
for node in root.iter():
    if node.tag.endswith('text'):
        node.set('font-family', 'Arial, sans-serif')
ET.register_namespace('', 'http://www.w3.org/2000/svg')
result = ET.tostring(root, encoding='unicode')
if 'var(' in result or '@import' in result:
    raise ValueError('SVG still depends on CSS variables or remote fonts')
path.write_text(result + '\n', encoding='utf-8')
print('Self-contained SVG exported:', path)
