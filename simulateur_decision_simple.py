# Simulateur de décision robotique

A = input("Ordre vocal reçu ? (oui/non): ").strip().lower() == "oui"
B = input("Main humaine détectée ? (oui/non): ").strip().lower() == "oui"
C = input("Urgence médicale détectée ? (oui/non): ").strip().lower() == "oui"

if (A and B) or C:
    print("🤖 Le robot ouvre la main. Objet tendu.")
else:
    print("🤖 Le robot garde la main fermée.")
