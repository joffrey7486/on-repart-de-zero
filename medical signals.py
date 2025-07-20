import random

def medical_signals(frequence_cardiaque, temperature_corporelle, niveau_oxygene):
    for cycle in range(5):
        secure_level = 0 

        print(f"Axe de surveillance Numéro {cycle}")
        if (60 <= frequence_cardiaque <= 180):
            secure_level += 1
        if (36.5 <= temperature_corporelle <= 42.0):
            secure_level += 1
        if (90 <= niveau_oxygene <= 100):
            secure_level += 1

        if secure_level == 3: print("🟢 STABLE")
        elif secure_level == 2: print("🟡 ATTENTION")
        else: 
            print("🚨 Diagnostic : 🔴 URGENCE")
            print("💀 Arrêt du système - intervention d'urgence requise.")
            break

         # Simulation d’évolution biologique à chaque cycle
        frequence_cardiaque -= random.randint(2, 8)
        temperature_corporelle -= round(random.uniform(0.1, 0.4), 1)
        niveau_oxygene -= random.randint(1, 3)

        # Limites réalistes (évite de descendre sous des seuils biologiques plausibles)
        frequence_cardiaque = max(frequence_cardiaque, 40)
        temperature_corporelle = max(temperature_corporelle, 34.0)
        niveau_oxygene = max(niveau_oxygene, 75)
        


statut = medical_signals(random.randint(55, 185), random.uniform(35.0, 42.5), random.randint(85, 100))

