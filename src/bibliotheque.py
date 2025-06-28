from exceptions import *
from datetime import datetime
import os

class Livre:
    #constructeur
    def __init__(self,isbn,titre,auteur,annee,genre,statut="disponible"):
        #validation des donnes
        if not isbn.strip():
            raise ValueError("L'ISBN ne peut pas être vide")
        if not titre.strip():
            raise ValueError("Le titre ne peut pas être vide")
        if not auteur.strip():
            raise ValueError("L'auteur ne peut pas être vide")
        if not annee.isdigit() or not (868 <= int(annee) <= datetime.now().year): #868 est l’année où le premier livre entièrement imprimé a été créé
            raise ValueError("L'année doit être un nombre valide (entre 868 et l'année courante)")
        if not genre.strip():
            raise ValueError("Le genre ne peut pas être vide")
        if statut not in ["disponible", "emprunté"]:
            raise ValueError("Statut invalide")
        
        self.isbn = isbn
        self.titre = titre
        self.auteur = auteur
        self.annee = annee
        self.genre = genre
        self.statut = statut

    #transformer l'objet à une ligne du texte pour le sauvegarder
    def object_to_txt(self):
        return f"{self.isbn};{self.titre};{self.auteur};{self.annee};{self.genre};{self.statut}"

    #transformer la ligne à un objet pour charger les donnees    
    def txt_to_object(txt):
        isbn, titre, auteur, annee, genre, statut = txt.strip().split(";") #strip pour ignorer le vide
        return Livre(isbn,titre,auteur,annee,genre,statut)
    

class Membre:

    #constructeur
    def __init__(self,id_membre,nom,livres_empruntes=None):
        #validation des donnees
        if not id_membre.strip():
            raise ValueError("L'identifiant du membre ne peut pas être vide")
        if not nom.strip():
            raise ValueError("Le nom du membre ne peut pas être vide")
        
        self.id_membre = id_membre
        self.nom = nom
        if livres_empruntes:
            self.livres_empruntes = livres_empruntes
        else:
            self.livres_empruntes = []
    
    #transformer l'objet à une ligne du texte pour le sauvegarder
    def object_to_txt(self):
        livres = ",".join(self.livres_empruntes)
        return f"{self.id_membre};{self.nom};{livres}"
    
    #transformer la ligne à un objet pour charger les donnees
    def txt_to_object(txt):
        parts = txt.strip().split(";")
        id_membre = parts[0]
        nom = parts[1]
        if len(parts) > 2 and parts[2]:
            livres = parts[2].split(",")
        else:
            livres = []
        return Membre(id_membre,nom,livres)
    
class Bibliotheque:
    #constructeur
    def __init__(self):
        self.livres = []
        self.membres = []
        self.charger_donnees()

    #ajout d'un livre
    def ajouter_livre(self,livre):
        for l in self.livres:
            if l.isbn == livre.isbn:
                raise ValueError("Un livre avec cet ISBN existe déjà")
        self.livres.append(livre)
        print(f"✅ Livre ajouté avec succès")

    #suppression d'un livre
    def supprimer_livre(self,isbn):
        livre = self.trouver_livre(isbn)
        if livre.statut == "emprunté" :
            raise LivreDejaEmprunteError()
        nouvelle_liste = []
        for l in self.livres:
            if l.isbn != isbn:
                nouvelle_liste.append(l)
        self.livres = nouvelle_liste
        print(f"🗑️ Livre supprimé : ISBN {isbn}")

    #enregistrement d'un membre
    def enregistrer_membre(self,membre):
        for m in self.membres:
           if m.id_membre == membre.id_membre:
                raise ValueError("Un membre avec cet identifiant existe déjà")
        self.membres.append(membre)
        print("📝 Membre enregistré")

    #emprunt d'un livre
    def emprunter_livre(self,isbn,id_membre):
        livre = self.trouver_livre(isbn)
        membre = self.trouver_membre(id_membre)

        if livre.statut != "disponible":
            raise LivreIndisponibleError()
        if len(membre.livres_empruntes) >= 3:
            raise QuotaEmpruntDepasseError()
        
        livre.statut = "emprunté"
        membre.livres_empruntes.append(isbn)
        self.enregistrer_action(isbn,id_membre,"emprunt")
        print("📖 Le livre a été emprunté")
    
    #rendre un livre
    def retourner_livre(self, isbn, id_membre):
        livre = self.trouver_livre(isbn)
        membre = self.trouver_membre(id_membre)

        if isbn not in membre.livres_empruntes:
            raise LivreNonEmprunteParCeMembreError()
    
        if isbn in membre.livres_empruntes:
            membre.livres_empruntes.remove(isbn)

        livre.statut = "disponible"
        self.enregistrer_action(isbn, id_membre, "retour")
        print(f"🔄 Le livre a été retourné")

    #affichage de la liste des livres
    def lister_livres(self):
        if not self.livres:
            print("Aucun livre disponible.")
            return

        print("📋Liste des livres :\n")
        for livre in self.livres:
            print(f"ISBN : {livre.isbn}")
            print(f"Titre : {livre.titre}")
            print(f"Auteur : {livre.auteur}")
            print(f"Année : {livre.annee}")
            print(f"Genre : {livre.genre}")
            print(f"Statut : {livre.statut}")
            print("-" * 40)
    
    #verifier que le livre existe ou non
    def trouver_livre(self, isbn):
        for l in self.livres:
            if l.isbn == isbn:
                return l
        raise LivreInexistantError()
    
    #verifier que le membre existe ou non
    def trouver_membre(self, id_membre):
        for m in self.membres:
            if m.id_membre == id_membre:
                return m
        raise MembreInexistantError()

    #sauvegarder les donnes dans des fichiers .txt
    def sauvegarder_donnees(self):
        with open("data/livres.txt","w",encoding="utf-8") as f: #Always specify encoding explicitly when writing
            for livre in self.livres:
                f.write(livre.object_to_txt() + "\n")
        with open("data/membres.txt","w",encoding="utf-8") as f:
            for membre in self.membres:
                f.write(membre.object_to_txt() + "\n")
    
    #charger les donnes des fichiers .txt
    def charger_donnees(self):
        if os.path.exists("data/livres.txt"):
            with open("data/livres.txt", encoding="UTF-8") as f:#eviter que les cara comme é deviennent illisibles
                livres = []
                for l in f:
                    if l.strip():
                        livre = Livre.txt_to_object(l)
                        livres.append(livre)
                self.livres = livres
        if os.path.exists("data/membres.txt"):
            with open("data/membres.txt", encoding="UTF-8") as f:
                membres = []
                for l in f:
                    if l.strip():
                        membre = Membre.txt_to_object(l)
                        membres.append(membre)
                self.membres = membres
    
    #sauvegarder les actions (emprunts)
    def enregistrer_action(self,isbn,id_membre,action):
        with open("data/historique.csv", "a",encoding="UTF-8") as f: #Always specify encoding explicitly
            date = datetime.now().strftime("%d-%m-%Y")
            f.write(f"{date};{isbn};{id_membre};{action}\n")