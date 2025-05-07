import tkinter as tk
import random

# Listes de loot
armures = ["Casque", "Cape", "Bracelet", "Botte", "Cuirasse", "Bouclier"]
armes = ["Épée", "Hache", "Masse", "Espadon", "Hache d'arme", "Marteau", "Arc", "Arbalète"]
objets_magiques = ["Anneau magique", "Amulette magique", "Potion de soin", "Parchemin mystique"]
bijoux = ["Bague en or", "Collier en argent", "Bracelet en platine"]

# Fonction de génération de loot
def generer_loot():
    categorie = random.choice(["Armure", "Arme", "Objet magique", "Bijou", "Pièces d'or"])
    
    if categorie == "Armure":
        loot = random.choice(armures)
    elif categorie == "Arme":
        loot = random.choice(armes)
    elif categorie == "Objet magique":
        loot = random.choice(objets_magiques)
    elif categorie == "Bijou":
        loot = random.choice(bijoux)
    else:
        loot = f"{random.randint(1, 30)} pièces d'or"
    
    resultat_label.config(text=f"Vous avez trouvé : {loot}")

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Générateur de Loot")

resultat_label = tk.Label(fenetre, text="Appuyez sur le bouton pour le loot")
resultat_label.pack(pady=10)

bouton_loot = tk.Button(fenetre, text="Générer Loot", command=generer_loot)
bouton_loot.pack(pady=10)

fenetre.mainloop()
