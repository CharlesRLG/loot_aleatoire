import tkinter as tk
import random

# Listes de loot
armures = ["Casque", "Cape", "Gants", "Botte", "Cuirasse", "Bouclier"]
armes = ["Épée", "Hache", "Masse", "Espadon", "Hache d'arme", "Marteau", "Arc", "Arbalète", "Baton"]
objets_magiques = ["Anneau magique", "Amulette magique", "Parchemin", "Baton", "Baguette", "armes", "Objets merveilleux"]
bijoux = ["Bague", "Collier"]

# Liste de qualité avec probabilités
qualite_item = ["En ruine", "Cassé", "Médiocre", "Correcte", "Assez bonne", "Bonne", "Magnifique", "Chef d'oeuvre"]
proba_qualite = [0.2, 0.2, 0.15, 0.2, 0.1, 0.1, 0.04, 0.01]

# Liste de matériaux avec probabilités
materiaux = [
    "Bronze ou chêne", "Fer ou Hêtre", "Acier ou Frêne", "Platine ou Erable argenté", 
    "Argent ou Saule blanc", "Mithril ou Bois de Lune", "Verre ou Bois de vitréalis", 
    "Obsidienne ou Ebène", "Ebonite ou Bois de Corbeau", "Infernal ou Bois du Styx", "Auréalis ou Bois Céleste"
]
proba_materiaux = [0.2, 0.2, 0.15, 0.1, 0.1, 0.1, 0.05, 0.04, 0.03, 0.02, 0.01]

# Fonction de génération de loot
def generer_loot():
    categorie = random.choice(["Armure", "Arme", "Objet magique", "Bijou"])
    if categorie == "Armure":
        loot = random.choice(armures)
    elif categorie == "Arme":
        loot = random.choice(armes)
    elif categorie == "Objet magique":
        loot = random.choice(objets_magiques)
    else:
        loot = random.choice(bijoux)
    return loot, categorie

# Détermination du matériau
def materiel_deter():
    return random.choices(materiaux, proba_materiaux)[0]

# Fonction qualité du loot
def generer_qualite():
    return random.choices(qualite_item, proba_qualite)[0]

# Fonction estimation
def generer_estimation(categorie, qualite):
    if categorie == "Armure":
        price_categorie = 1
    elif categorie == "Arme":
        price_categorie = 1
    elif categorie == "Objet magique":
        price_categorie = 50
    elif categorie == "Bijou":
        price_categorie = 5
    else:
        price_categorie = 1

    qualite_prix = {
        "En ruine": 0.001, "Cassé": 0.1, "Médiocre": 0.25, 
        "Correcte": 0.5, "Assez bonne": 1, "Bonne": 10, 
        "Magnifique": 25, "Chef d'oeuvre": 100
    }
    price = price_categorie * qualite_prix[qualite]
    return price

# Fonction combinée
def fonction_combine():
    loot, categorie = generer_loot()
    qualite_result = generer_qualite()
    estimation = generer_estimation(categorie, qualite_result)
    matiere = materiel_deter()
    resultat_label.config(text=f"Vous avez trouvé : {loot} en {matiere}\nQualité : {qualite_result}\nEstimation : {float(estimation)} pièces d'or")

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Générateur de Loot")
fenetre.geometry("400x300")

resultat_label = tk.Label(fenetre, text="Appuyez sur le bouton pour le loot")
resultat_label.pack(pady=10)

bouton_loot = tk.Button(fenetre, text="Générer Loot", command=fonction_combine)
bouton_loot.pack(pady=10)

fenetre.mainloop()
