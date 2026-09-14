import os
import re
import json

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')
pattern = re.compile(r'{%\s*trans\s+([\'"])(.*?)\1\s*%}')

strings = set()
for root, _, filenames in os.walk(TEMPLATE_DIR):
    for filename in filenames:
        if filename.endswith('.html'):
            filepath = os.path.join(root, filename)
            with open(filepath, 'r', encoding='utf-8') as f:
                for _, text in pattern.findall(f.read()):
                    strings.add(text)

with open('strings.json', 'w', encoding='utf-8') as f:
    json.dump(list(strings), f, ensure_ascii=False, indent=2)
