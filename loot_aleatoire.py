import tkinter as tk
import random

# === Données ===
armures = ["Casque", "Cape", "Gants", "Botte", "Cuirasse", "Bouclier"]
armes = ["Épée", "Hache", "Masse", "Espadon", "Hache d'arme", "Marteau", "Arc", "Arbalète", "Bâton"]
objets_magiques = ["Anneau magique", "Amulette magique", "Bâton", "Baguette", "Armes", "Objets merveilleux"]
bijoux = ["Bague", "Collier"]

# Catégories et leur coefficient de prix de base
prix_categorie = {
    "Armure": 1,
    "Arme": 1,
    "Objet magique": 50,
    "Bijou": 5
}

# Liste de qualité avec probabilités
qualite_item = ["En ruine", "Cassé", "Médiocre", "Correcte", "Assez bonne", "Bonne", "Magnifique", "Chef d'oeuvre"]
proba_qualite = [0.2, 0.2, 0.15, 0.2, 0.1, 0.1, 0.04, 0.01]
prix_qualite = {
    "En ruine": 0.001, "Cassé": 0.1, "Médiocre": 0.25,
    "Correcte": 0.5, "Assez bonne": 1, "Bonne": 10,
    "Magnifique": 25, "Chef d'oeuvre": 100
}

# Liste de matériaux avec probabilités et leurs prix
materiaux = [
    "Bronze ou chêne", "Fer ou Hêtre", "Acier ou Frêne", "Platine ou Érable argenté",
    "Argent ou Saule blanc", "Mithril ou Bois de Lune", "Verre ou Bois de vitréalis",
    "Obsidienne ou Ébène", "Ebonite ou Bois de Corbeau", "Infernal ou Bois du Styx", "Auréalis ou Bois Céleste"
]
proba_materiaux = [0.2, 0.2, 0.15, 0.1, 0.1, 0.1, 0.05, 0.04, 0.03, 0.02, 0.01]
prix_materiaux = {
    "Bronze ou chêne": 1, "Fer ou Hêtre": 2, "Acier ou Frêne": 5,
    "Platine ou Érable argenté": 10, "Argent ou Saule blanc": 15,
    "Mithril ou Bois de Lune": 30, "Verre ou Bois de vitréalis": 50,
    "Obsidienne ou Ébène": 75, "Ebonite ou Bois de Corbeau": 100,
    "Infernal ou Bois du Styx": 150, "Auréalis ou Bois Céleste": 300
}

# === Fonctions de génération ===
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

def materiel_deter():
    return random.choices(materiaux, proba_materiaux)[0]

def generer_qualite():
    return random.choices(qualite_item, proba_qualite)[0]

def calculer_bonus(categorie, qualite, materiel):
    index_materiau = materiaux.index(materiel)
    bonus = ""

    if categorie == "Arme":
        degats = index_materiau * 10
        bonus = f"+{degats} dégâts"
        if qualite == "Chef d'oeuvre":
            if materiel in ["Arc", "Arbalète"]:
                bonus += ", +5 en CT"
            else:
                bonus += ", +5 en CC"
    elif categorie == "Armure":
        armure = index_materiau * 10
        bonus = f"+{armure} en protection"
        if qualite == "Chef d'oeuvre":
            bonus += ", +5 en Sociabilité"
    return bonus

def calculer_prix(categorie, qualite, materiel):
    """ Calcule le prix total en pièces de cuivre (base la plus petite) """
    prix_total = prix_categorie[categorie] * prix_qualite[qualite] * prix_materiaux[materiel] * 240  # 1 PO = 240 PC
    return int(prix_total)

def conversion_monnaie(prix_pc):
    """ Convertit le prix en pièces d'or, d'argent et de cuivre """
    pieces_or = prix_pc // 240
    reste = prix_pc % 240
    pieces_argent = reste // 12
    pieces_cuivre = reste % 12
    return pieces_or, pieces_argent, pieces_cuivre

# === Interface Tkinter ===
fenetre = tk.Tk()
fenetre.title("Générateur de Loot")
fenetre.geometry("400x400")

resultat_label = tk.Label(fenetre, text="Appuyez sur le bouton pour le loot")
resultat_label.pack(pady=10)

def fonction_combine():
    loot, categorie = generer_loot()
    qualite = generer_qualite()
    materiel = materiel_deter()
    bonus = calculer_bonus(categorie, qualite, materiel)
    prix_pc = calculer_prix(categorie, qualite, materiel)
    pieces_or, pieces_argent, pieces_cuivre = conversion_monnaie(prix_pc)
    
    resultat_label.config(
        text=(f"Vous avez trouvé : {loot} en {materiel}\n"
              f"Qualité : {qualite}\n"
              f"Bonus : {bonus}\n"
              f"Valeur estimée : {pieces_or} PO, {pieces_argent} PA, {pieces_cuivre} PC")
    )

bouton_loot = tk.Button(fenetre, text="Générer Loot", command=fonction_combine)
bouton_loot.pack(pady=10)

fenetre.mainloop()