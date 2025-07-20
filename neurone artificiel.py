# NEURONE ARTIFICIEL À 4 ENTRÉES
print("Bienvenue dans le simulateur de neurone artificiel 🔬🧠")

# Entrées binaires (0 ou 1)
x1 = int(input("x1 - Danger détecté ? (1/0) : "))
x2 = int(input("x2 - Victime repérée ? (1/0) : "))
x3 = int(input("x3 - Produit prêt ? (1/0) : "))
x4 = int(input("x4 - Urgence médicale ? (1/0) : "))

# Poids attribués à chaque entrée (importances)
w1 = 3
w2 = 2
w3 = 1
w4 = 4

# Biais (seuil de déclenchement)
seuil = 6

# Calcul de la somme pondérée
somme = (x1 * w1) + (x2 * w2) + (x3 * w3) + (x4 * w4)

# Fonction d’activation (seuil)
if somme > seuil:
    print("⚡ Le neurone s'active : ACTION !")
else:
    print("💤 Le neurone reste inactif : PAS D'ACTION.")

# Affichage pour suivi
print(f"Valeur totale reçue : {somme} / seuil : {seuil}")
