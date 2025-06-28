import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator
from collections import Counter
import csv
from datetime import datetime, timedelta

#Diagramme circulaire : % de livres par genre
def graphique_genre(livres):
    genres = []
    for l in livres:
        genres.append(l.genre)
    counts = Counter(genres)
    if not genres:
        print("Pourcentage de livres par genre: Il n’y a pas de livres à ce moment-là.")
        return
    
    plt.figure("Répartition des livres par genre")
    plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%')
    plt.title("Répartition des livres par genre")
    plt.savefig("assets/Répartition_des_livres_par_genre.png")

#Histogramme : Top 10 des auteurs les plus populaires
def top_auteurs(fichier_historique, livres):
    # Dictionnaire ISBN → auteur
    isbn_auteur = {livre.isbn: livre.auteur for livre in livres}

    # Initialiser compteur avec tous les auteurs à 0
    emprunts_par_auteur = Counter({livre.auteur: 0 for livre in livres})

    # Lire le fichier historique
    with open(fichier_historique, encoding='UTF-8') as f:
        reader = csv.reader(f, delimiter=';')
        for ligne in reader:
            if len(ligne) != 4:
                continue
            date, isbn, id_membre, action = ligne
            if action.strip().lower() == "emprunt":
                auteur = isbn_auteur.get(isbn)
                if auteur:
                    emprunts_par_auteur[auteur] += 1

    # Top 10 auteurs (même ceux avec 0 emprunt)
    top_10 = emprunts_par_auteur.most_common(10)
    noms = [auteur for auteur, _ in top_10]
    freqs = [count for _, count in top_10]

    if not noms:
        print("Top 10 des auteurs : Aucun auteur trouvé.")
        return

    # Affichage graphique
    # Affichage graphique
    plt.figure("Top auteurs")
    plt.bar(noms, freqs)

    # Forcer l'axe Y à afficher uniquement des entiers
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    # Définir l'axe Y pour qu'il commence à 0 et s'ajuste étroitement à la valeur maximale
    ymax = max(freqs) if freqs else 1  # éviter une erreur si freqs est vide
    plt.ylim(bottom=0, top=ymax + 1)   # +1 pour un peu d'espace en haut

    plt.xticks(rotation=45, ha="right")
    plt.title("Top 10 des auteurs les plus empruntés")
    plt.ylabel("Nombre d'emprunts")
    plt.tight_layout()
    plt.savefig("assets/Top_auteurs.png")


#Courbe temporelle : Activité des emprunts (30 derniers jours)
def courbe_activite():
    dates = []
    with open("data/historique.csv", encoding="UTF-8") as f:
        reader = csv.reader(f, delimiter=";")
        for row in reader:
            if len(row) < 4:
                continue
            date_str, _, _, action = row
            if action.strip().lower() == "emprunt":
                date = datetime.strptime(date_str.strip(), "%d-%m-%Y")
                if datetime.now() - date <= timedelta(days=30):
                    dates.append(date.date())

    if not dates:
        print("Activité des emprunts : Aucune activité d'emprunt dans les 30 derniers jours.")
        return

    counts = Counter(dates)
    sorted_dates = sorted(counts.items())
    x = [d.strftime("%d-%m-%Y") for d, _ in sorted_dates]
    y = [c for _, c in sorted_dates]

    plt.figure("Activité des emprunts")
    plt.plot(x, y, marker='o')
    plt.title("Activité des emprunts (30 jours)")
    plt.xlabel("Date")
    plt.ylabel("Nombre d'emprunts")
    plt.xticks(rotation=45)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))

    # ⬇️ Force y-axis to start at 0 and go slightly above max value
    plt.ylim(0, max(y) + 1)

    plt.tight_layout()
    plt.savefig("assets/Activité_des_emprunts.png")
