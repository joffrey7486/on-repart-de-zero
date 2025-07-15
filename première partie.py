# Simulateur de porte logique

def security_access ():
    badge = input("Badge validé ? (oui/non): ").strip().lower() == "oui"
    code = input("Code secret correct ? (oui/non): ").strip().lower() == "oui"
    scan_face = input("Passage du scanner ? (oui/non): ").strip().lower() == "oui"
    empreinte = input("Votre empreinte digital ? (oui/non): ").strip().lower() == "oui"

    if badge and code and (scan_face or empreinte):
        print("✅ Porte ouverte ! Accès autorisé.")
    else:
        print("❌ Accès refusé.")

security_access()
