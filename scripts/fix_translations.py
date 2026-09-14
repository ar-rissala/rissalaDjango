import os
import polib

def fix_translations():
    po_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.po')
    print(f"Loading {po_path}...")
    po = polib.pofile(po_path)
    
    fixes = {
        "Connexion": "تسجيل الدخول",
        "Study according to your": "ادرس وفق",
        "beliefs.": "beliefs.",
        "Rissala accompanies you in the study and transmission of Islamic knowledge. Structured pathways, rigorous sources, and a thoughtful progression to understand, deepen, and transmit.": "رسالة ترافقك في دراسة ونقل العلوم الشرعية. مسارات منظمة، مصادر موثوقة، وتقدّم مدروس للفهم والتعمّق والتبليغ.",
        "About Rissala": "عن رسالة",
        "Islamic Finance": "المالية الإسلامية",
        "Arabic language": "اللغة العربية",
        "Islamic Sciences": "العلوم الإسلامية",
        "Books": "كتب",
        "Home": "الرئيسية",
        "News": "الأخبار",
        "Parcours": "المسارات",
        "Discover our routes": "اكتشف مساراتنا",
        "My Space": "مساحتي",
        "Read the articles": "اقرأ المقالات",
        "To study.To understand.Go deeper.": "للدراسة. للفهم. للتعمق.",
    }
    
    updated = 0
    for entry in po:
        if entry.msgid in fixes:
            entry.msgstr = fixes[entry.msgid]
            updated += 1
            print(f"Fixed: {entry.msgid}")
            
    # Save the updated PO
    po.save()
    print(f"Updated {updated} translations in PO.")
    
    # Compile to MO
    mo_path = os.path.join('locale', 'ar', 'LC_MESSAGES', 'django.mo')
    po.save_as_mofile(mo_path)
    print(f"Compiled MO saved to {mo_path}.")

if __name__ == '__main__':
    fix_translations()
