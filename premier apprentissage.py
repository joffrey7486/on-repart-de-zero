import numpy as np

# === 1. Données d'entrée (logique AND) ===
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

# Sorties attendues (truth)
T = np.array([0, 0, 0, 1])

# === 2. Initialisation ===
w = np.random.rand(2)   # poids aléatoires pour x1 et x2
b = 0.0                 # biais initial
eta = 0.1               # taux d'apprentissage

# === 3. Fonction d'activation (Step Function) ===
def activation(z):
    return 1 if z > 0 else 0

# === 4. Entraînement ===
for epoch in range(10):  # on répète 10 fois le jeu d'entraînement
    print(f"\n🔁 ÉPOQUE {epoch+1}")
    for i in range(len(X)):
        x = X[i]           # exemple courant
        t = T[i]           # sortie attendue
        
        # ---- Étape 1 : Calcul du neurone ----
        z = np.dot(w, x) + b  # somme pondérée z = Σ(w*x) + b
        y = activation(z)     # sortie prédite après activation
        
        # ---- Étape 2 : Calcul de l'erreur ----
        erreur = t - y
        
        # ---- Affichage AVANT correction ----
        print(f"\n   ▶ AVANT correction : Entrée {x} | Sortie prédite {y} | Attendue {t} | Poids {w} | Biais {b}")

        # ---- Étape 3 : Mise à jour des poids (Perceptron Rule) ----
        # w_new = w_old + η * (t - y) * x
        w = w + eta * erreur * x
        # b_new = b_old + η * (t - y)
        b = b + eta * erreur

        # ---- Affichage APRÈS correction ----
        print(f"   ✅ APRÈS correction : Nouveau poids {w} | Nouveau biais {b} | Erreur appliquée {erreur}")

# === 5. Test final du perceptron ===
print("\n🚀 TEST FINAL APRÈS APPRENTISSAGE :")
for x in X:
    z = np.dot(w, x) + b
    y = activation(z)
    print(f"   {x} → Sortie prédite {y}")
