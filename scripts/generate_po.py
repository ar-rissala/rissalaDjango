import os
import re

def generate_po():
    strings = set()
    
    # 1. Extract from templates
    template_dir = os.path.join('templates')
    for root, dirs, files in os.walk(template_dir):
        for file in files:
            if file.endswith('.html'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find {% trans "..." %} or {% trans '...' %}
                    matches = re.findall(r'{%\s*trans\s+([\'"])(.*?)\1\s*%}', content)
                    for m in matches:
                        strings.add(m[1])
                        
    # 2. Extract from models.py
    for root, dirs, files in os.walk('apps'):
        for file in files:
            if file.endswith('.py'):
                path = os.path.join(root, file)
                with open(path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    # Find _("...") or _('...')
                    matches = re.findall(r'_\(([\'"])(.*?)\1\)', content)
                    for m in matches:
                        strings.add(m[1])

    # 3. Write to django.po
    po_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.po')
    os.makedirs(os.path.dirname(po_path), exist_ok=True)
    
    # Read existing translations
    existing = {}
    if os.path.exists(po_path):
        import polib
        po = polib.pofile(po_path)
        for entry in po:
            if entry.msgstr:
                existing[entry.msgid] = entry.msgstr

    with open(po_path, 'w', encoding='utf-8') as f:
        f.write('msgid ""\n')
        f.write('msgstr ""\n')
        f.write('"Project-Id-Version: Rissala\\n"\n')
        f.write('"Report-Msgid-Bugs-To: \\n"\n')
        f.write('"POT-Creation-Date: 2026-09-14 23:55+0200\\n"\n')
        f.write('"PO-Revision-Date: YEAR-MO-DA HO:MI+ZONE\\n"\n')
        f.write('"Last-Translator: FULL NAME <EMAIL@ADDRESS>\\n"\n')
        f.write('"Language-Team: LANGUAGE <LL@li.org>\\n"\n')
        f.write('"Language: ar\\n"\n')
        f.write('"MIME-Version: 1.0\\n"\n')
        f.write('"Content-Type: text/plain; charset=UTF-8\\n"\n')
        f.write('"Content-Transfer-Encoding: 8bit\\n"\n')
        f.write('\n')
        
        for string in sorted(list(strings)):
            escaped_string = string.replace('"', '\\"')
            msgstr = existing.get(string, "").replace('"', '\\"')
            f.write(f'msgid "{escaped_string}"\n')
            f.write(f'msgstr "{msgstr}"\n\n')
            
    print(f"Generated django.po with {len(strings)} strings (preserved {len(existing)}).")

if __name__ == '__main__':
    generate_po()
