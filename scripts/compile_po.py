import os
import polib

def compile_po():
    po_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.po')
    mo_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.mo')
    
    print(f"Loading {po_path}...")
    po = polib.pofile(po_path)
    
    # Compile to MO
    print("Compiling to MO file...")
    po.save_as_mofile(mo_path)
    print(f"Compiled MO saved to {mo_path}.")

if __name__ == '__main__':
    compile_po()
