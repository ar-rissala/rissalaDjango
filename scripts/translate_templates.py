import os
import re
import time
from deep_translator import GoogleTranslator

# Ensure scripts directory exists but we'll run from root
TEMPLATE_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'templates')

def get_html_files(directory):
    files = []
    for root, _, filenames in os.walk(directory):
        for filename in filenames:
            if filename.endswith('.html'):
                files.append(os.path.join(root, filename))
    return files

def translate_templates():
    translator = GoogleTranslator(source='fr', target='en')
    files = get_html_files(TEMPLATE_DIR)
    
    # regex for {% trans "text" %} or {% trans 'text' %}
    pattern = re.compile(r'{%\s*trans\s+([\'"])(.*?)\1\s*%}')
    
    translation_cache = {}
    
    for filepath in files:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        matches = pattern.findall(content)
        if not matches:
            continue
            
        print(f"Processing {os.path.basename(filepath)}...")
        new_content = content
        for quote, text in matches:
            if text not in translation_cache:
                try:
                    translated = translator.translate(text)
                    time.sleep(0.5) # avoid rate limits
                    translation_cache[text] = translated
                    print(f"  Translated: '{text}' -> '{translated}'")
                except Exception as e:
                    print(f"  Error translating '{text}': {e}")
                    translation_cache[text] = text
            
            # Replace in content
            original_tag = f"{{% trans {quote}{text}{quote} %}}"
            new_tag = f"{{% trans {quote}{translation_cache[text]}{quote} %}}"
            new_content = new_content.replace(original_tag, new_tag)
            
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)

if __name__ == "__main__":
    translate_templates()
