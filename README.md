
# 📚 Gestion de Bibliothèque

Projet de fin de module développé en Python. Il permet de gérer les livres, les membres, les emprunts et les retours, avec des visualisations statistiques générées à l'aide de matplotlib.

## 👤 Auteur

**LEMRANI Moad**  
Filière Génie Informatique  
École Nationale des Sciences Appliquées d'Oujda

## ⚙️ Guide d'installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/MoadLemrani/Gestion_Bibliotheque_LEMRANI_Moad.git
cd Gestion_Bibliotheque_LEMRANI_Moad
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv venv
venv\Scripts\activate  # Sous Windows
# ou
source venv/bin/activate  # Sous Linux/macOS
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Lancer le projet

```bash
python src/main.py
```

## 🧪 Exemples d'utilisation

### ➕ Ajouter un livre

- Fournir l'ISBN, le titre, l’auteur, l’année de publication et le genre.
- Le programme vérifie que l’ISBN est unique.

### 👤 Ajouter un membre

- Le programme vérifie que l’identifiant n’est pas déjà utilisé.

### 📖 Emprunter un livre

- Un membre peut emprunter jusqu’à 3 livres.
- Le programme vérifie la disponibilité du livre et l'identité du membre.

### 🔄 Retourner un livre

- Le membre ne peut retourner que les livres qu’il a empruntés.

### 📊 Visualiser les statistiques

- Nombre de livres par genre
- Top 10 des auteurs les plus empruntés
- Activité des emprunts sur les 30 derniers jours
