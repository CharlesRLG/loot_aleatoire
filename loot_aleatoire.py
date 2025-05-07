import tkinter as tk
import random

# Listes de loot
armures = ["Casque", "Cape", "Bracelet", "Botte", "Cuirasse", "Bouclier"]
armes = ["Épée", "Hache", "Masse", "Espadon", "Hache d'arme", "Marteau", "Arc", "Arbalète"]
objets_magiques = ["Anneau magique", "Amulette magique", "Potion de soin", "Parchemin mystique"]
bijoux = ["Bague en or", "Collier en argent", "Bracelet en platine"]
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
  

# Fonction qualité du loot

def generer_qualite():
    qualite = random.choice(qualite_item)
    return qualite

# Fonction estimation

def generer_estimation(categorie, qualite, loot):
    
    if categorie == "Armure":
        price_categorie = 2
    elif categorie == "Arme":
        price_categorie = 2
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
    resultat_label.config(text=f"Vous avez trouvé : {loot}\nQualité : {qualite_result}\nEstimation : {float(estimation)} pièces d'or")

# Interface Tkinter
fenetre = tk.Tk()
fenetre.title("Générateur de Loot")
fenetre.geometry("400x300")

resultat_label = tk.Label(fenetre, text="Appuyez sur le bouton pour le loot")
resultat_label.pack(pady=10)

bouton_loot = tk.Button(fenetre, text="Générer Loot", command=fonction_combine)
bouton_loot.pack(pady=10)

fenetre.mainloop()
