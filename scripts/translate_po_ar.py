import os
import polib
import time
from googletrans import Translator

def translate_po():
    po_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.mo')
    
    print(f"Loading {po_path}...")
    po = polib.pofile(po_path)
    translator = Translator()
    
    untranslated = [entry for entry in po if not entry.msgstr]
    total = len(untranslated)
    print(f"Found {total} untranslated strings.")
    
    for i, entry in enumerate(untranslated):
        try:
            # Translate from English to Arabic
            result = translator.translate(entry.msgid, src='en', dest='ar')
            entry.msgstr = result.text
            print(f"[{i+1}/{total}] Translated successfully")
            # Save progressively in case of crash
            if i % 10 == 0:
                po.save()
            time.sleep(0.5)
        except Exception as e:
            print(f"Error on item {i+1}: {str(e)[:50]}")
            time.sleep(2)
            
    # Final save
    po.save()
    print("Translation complete. Saving PO file.")
    
    # Compile to MO
    print("Compiling to MO file...")
    po.save_as_mofile(mo_path)
    print(f"Compiled MO saved to {mo_path}.")

if __name__ == '__main__':
    translate_po()
