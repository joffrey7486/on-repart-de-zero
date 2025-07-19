# Cerveau logique simplifié avec feedback

# Phase 1 : Entrées
A = input("Victime identifiée ? (oui/non): ").strip().lower() == "oui"
B = input("Produit prêt ? (oui/non): ").strip().lower() == "oui"
C = input("Fréquence cardiaque anormale ? (oui/non): ").strip().lower() == "oui"
D = input("Autorisation override ? (oui/non): ").strip().lower() == "oui"

# Décision
decision = (A and B and C) or D
print("🤖 Décision du robot :", "INJECTION" if decision else "PAS D'ACTION")

# Phase 2 : Feedback
correction = input("Décision correcte ? (oui/non): ").strip().lower()

# Simuler l'apprentissage :
if correction == "non":
    print("🤖 Mise à jour interne : ajustement du schéma logique requis.")
    # Ici, on pourrait imaginer que le robot modifie son critère (par ex. supprime l'override D)
else:
    print("🤖 Confirmation : logique actuelle validée.")

