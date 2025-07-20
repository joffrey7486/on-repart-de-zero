def calcul_pente(x1, y1, x2, y2):
    print(f"Point A : ({x1}, {y1})")
    print(f"Point B : ({x2}, {y2})")

    # Vérifier la division par zéro
    if x2 - x1 == 0:
        print("❌ Division par zéro → droite verticale")
    else:
        # Calcul de la pente
        pente = (y2 - y1) / (x2 - x1)
        print(f"📐 Pente : {pente}")

        if pente > 0:
            print("🔼 Droite montante")
        elif pente < 0:
            print("🔽 Droite descendante")
        else:
            print("➡️ Droite horizontale")

# 🧪 Exemple d'utilisation
calcul_pente(-3, -6, 3, 6)
calcul_pente(1, 5, 1, 9) 
calcul_pente(-4, 5, -1, 5) 
calcul_pente(2, 3, 5, 9) 
calcul_pente(3, 7, 1, 2) 