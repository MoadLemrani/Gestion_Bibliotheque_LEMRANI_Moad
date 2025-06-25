from bibliotheque import *
from exceptions import *
from visualisations import *

bib = Bibliotheque()
def menu():
    while True:
        print("\n==== GESTION BIBLIOTHEQUE ====")
        print("1. Ajouter un livre")
        print("2. Supprimer un livre")
        print("3. Inscrire un membre")
        print("4. Emprunter un livre")
        print("5. Rendre un livre")
        print("6. Lister tous les livres")
        print("7. Afficher les statistiques")
        print("8. Sauvegarder et quitter")
        choice = input("Choix : ")

        try:
            match choice:
                case "1":
                    isbn = input("ISBN : ")
                    titre = input("Titre : ")
                    auteur = input("Auteur : ")
                    annee = input("Année : ")
                    genre = input("Genre : ")
                    bib.ajouter_livre(Livre(isbn, titre, auteur, annee, genre))
                    bib.sauvegarder_donnees()
                    
                case "2":
                    isbn = input("ISBN du livre à supprimer : ")
                    bib.supprimer_livre(isbn)
                    bib.sauvegarder_donnees()
                    
                case "3":
                    id_membre = input("ID : ")
                    nom = input("Nom : ")
                    bib.enregistrer_membre(Membre(id_membre, nom))
                    bib.sauvegarder_donnees()
                    
                case "4":
                    id_membre = input("ID Membre : ")
                    isbn = input("ISBN Livre : ")
                    bib.emprunter_livre(isbn, id_membre)
                    bib.sauvegarder_donnees()
                    
                case "5":
                    id_membre = input("ID Membre : ")
                    isbn = input("ISBN Livre : ")
                    bib.retourner_livre(isbn, id_membre)
                    bib.sauvegarder_donnees()
                    
                case "6":
                    bib.lister_livres()

                case "7":
                    print("📋 Affichage des statistiques en cours...")
                    #call all
                    graphique_genre(bib.livres)
                    top_auteurs(bib.livres)
                    courbe_activite()
                    plt.show()

                case "8":
                    print("💾 Données sauvegardées avec succès")
                    break #pas besoin de sauvegarder les donnes (deja sauvegardees)

                case _:
                    print("Choix invalide")

        except (Exception, LivreIndisponibleError, QuotaEmpruntDepasseError, MembreInexistantError, LivreInexistantError) as e:
            print(f"❌ Erreur detecté: {e}")
menu()            