import tkinter as tk
import random

# Listes de loot
armures = ["Casque", "Cape", "Gants", "Botte", "Cuirasse", "Bouclier"]
armes = ["Épée", "Hache", "Masse", "Espadon", "Hache d'arme", "Marteau", "Arc", "Arbalète", "Baton"]
objets_magiques = ["Anneau magique", "Amulette magique", "Parchemin", "Baton", "Baguette", "armes", "Objets merveilleux"]
bijoux = ["Bague", "Collier"]
qualite_item = ["En ruine","Cassé","Médiocre", "Correcte","Assez bonne", "Bonne", "magnifique", "Chef d'oeuvre"]

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

# Détermination du matériel
def materiel_deter():
    materiel = random.choice(["Bronze ou chêne", "Fer ou Hêtre", "Acier ou Frêne", "Platine ou Erable argenté", "Argent ou Saule blanc", "Mithril ou Bois de Lune", "Verre ou Bois de vitréalis", "Obsidienne ou Ebène", "Ebonite ou Bois de Corbeau", "Infernal ou Bois du Styx", "Auréalis ou Bois Céleste"])
    return materiel

# Fonction qualité du loot

def generer_qualite():
    qualite = random.choice(qualite_item)
    return qualite

# Fonction estimation

def generer_estimation(categorie, qualite, loot):
    
    if categorie == "Armure":
        price_categorie = 1
    elif categorie == "Arme":
        price_categorie = 1
    elif categorie == "Objet magique":
        price_categorie = 50
    elif categorie == "Bijou":
        price_categorie = 5
    else:
        price_categorie = loot

    if qualite == "En ruine":
        price_qualite = 0.001
    elif qualite == "Cassé":
        price_qualite = 0.1
    elif qualite == "Médiocre":
        price_qualite = 0.25
    elif qualite == "Correcte":
        price_qualite = 0.5
    elif qualite == "Assez bonne":
        price_qualite = 1
    elif qualite == "Bonne":
        price_qualite = 10
    elif qualite == "Magnifique":
        price_qualite = 25
    else :
        price_qualite = 100

    price = price_categorie * price_qualite

    return price

# fonction combiné

def fonction_combine():
    loot, categorie = generer_loot()
    qualite_result = generer_qualite()
    estimation = generer_estimation(categorie, qualite_result, loot)
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
