import os
import re
import json

TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')

def apply_translations():
    with open('translated.json', 'r', encoding='utf-8') as f:
        translations = json.load(f)
        
    pattern = re.compile(r'{%\s*trans\s+([\'"])(.*?)\1\s*%}')
    
    for root, _, filenames in os.walk(TEMPLATE_DIR):
        for filename in filenames:
            if filename.endswith('.html'):
                filepath = os.path.join(root, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                matches = pattern.findall(content)
                if not matches:
                    continue
                    
                new_content = content
                for quote, text in matches:
                    if text in translations:
                        eng_text = translations[text].replace('"', '\\"').replace("'", "\\'")
                        # Use double quotes for the translated text in trans tag just to be safe
                        original_tag = f"{{% trans {quote}{text}{quote} %}}"
                        # We use double quotes to avoid issues if eng_text has single quotes
                        new_tag = f"{{% trans \"{eng_text}\" %}}"
                        new_content = new_content.replace(original_tag, new_tag)
                        
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                print(f"Updated {filepath}")

if __name__ == "__main__":
    apply_translations()
