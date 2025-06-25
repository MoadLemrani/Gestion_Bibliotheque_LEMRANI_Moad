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
    plt.figure("Répartition des livres par genre")
    plt.pie(counts.values(), labels=counts.keys(), autopct='%1.1f%%')
    plt.title("Répartition des livres par genre")

#Histogramme : Top 10 des auteurs les plus populaires
def top_auteurs(livres):
    auteurs = []
    for l in livres:
        auteurs.append(l.auteur)
    counts = Counter(auteurs).most_common(10)
    noms = []
    freqs = []
    for a in counts:
        noms.append(a[0])
        freqs.append(a[1])
    plt.figure("Top auteurs")
    plt.bar(noms, freqs)
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))
    plt.xticks(rotation=45)
    plt.title("Top 10 des auteurs")
    plt.ylabel("Nombre des livres écrits")

#Courbe temporelle : Activité des emprunts (30 derniers jours)
def courbe_activite():
    dates = []

    with open("data/historique.csv", encoding="utf-8") as f:
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
        print("Aucune activité d'emprunt dans les 30 derniers jours.")
        return

    counts = Counter(dates)
    sorted_dates = sorted(counts.items())
    x = [d.strftime("%d-%m-%Y") for d in counts.keys()]
    y = counts.values()


    plt.figure("Activité des emprunts")
    plt.plot(x, y, marker='o')
    plt.title("Activité des emprunts (30 jours)")
    plt.xlabel("Date")
    plt.ylabel("Nombre d'emprunts")
    plt.gca().yaxis.set_major_locator(MaxNLocator(integer=True))  # Pour afficher que des entiers
    plt.xticks(rotation=45)
    plt.tight_layout()