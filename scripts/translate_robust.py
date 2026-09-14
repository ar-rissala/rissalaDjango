import json
import time
from googletrans import Translator

def translate_strings():
    with open('strings.json', 'r', encoding='utf-8') as f:
        strings = json.load(f)
        
    try:
        with open('translated.json', 'r', encoding='utf-8') as f:
            translated = json.load(f)
    except FileNotFoundError:
        translated = {}

    translator = Translator()
    
    count = 0
    for s in strings:
        if s not in translated:
            try:
                print(f"Translating: {s[:30]}...")
                res = translator.translate(s, src='fr', dest='en')
                translated[s] = res.text
                count += 1
                if count % 10 == 0:
                    time.sleep(1)
                with open('translated.json', 'w', encoding='utf-8') as f:
                    json.dump(translated, f, ensure_ascii=False, indent=2)
            except Exception as e:
                print(f"Error: {e}")
                time.sleep(2)
                
if __name__ == "__main__":
    translate_strings()
    print("Done translating strings.")
