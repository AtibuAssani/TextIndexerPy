# TextIndexerPy

# 1. Présentation du projet

TextIndexerPy est un outil en ligne de commande permettant de charger plusieurs fichiers texte, de les prétraiter (nettoyage, tokenisation), de construire un index inversé, puis de faire des recherches efficaces sur ces documents.  
Le projet permet aussi d'afficher des extraits pertinents et fournit des statistiques globales sur le corpus.

L’objectif est d’apprendre à manipuler des fichiers, des structures de données (dictionnaires, listes), des algorithmes de recherche et de tri, ainsi que de développer une interface en ligne de commande simple.

# 2. Fonctionnalités principales

- **Chargement** de fichiers texte depuis un dossier donné.
- **Prétraitement** des textes : passage en minuscules, suppression de la ponctuation, découpage en mots (tokenisation).
- **Construction d’un index inversé** : chaque mot référence les documents et les positions où il apparaît.
- **Calcul des fréquences des termes** (TF) dans chaque document.
- **Recherche** simple ou multi-mots avec intersection ou union des résultats.
- **Classement des documents** selon un score de pertinence basique.
- **Affichage d’extraits** de texte autour des mots-clés.
- **Statistiques** globales sur le corpus (nombre de documents, mots uniques, top mots).


# 3. Membres & Modules

Le projet est divisé en 5 modules, chacun confié à un étudiant différent :

| Module | Noms                         | Fonctionnalités principales                       | Fichier(s) |
|--------|-------------|----------------|----------------------------------------------------------|
| 1      | BAHATI MBEBE Claudine        | Chargement et prétraitement des documents        | `document_loader.py` |
| 2      | ASSINA BINTI MOMA Jessica    | Construction de l’index inversé et calcul des fréquences | `indexer.py` |
| 3      | ATIBU ASSANI Augustin        | Recherche dans l’index avec calcul de pertinence | `search_engine.py` |
| 4      | BAMPOLE LUKUMU David         | Tri des résultats et affichage avec extraits (snippets) | `retrieval.py` |
| 5      | ASSUMANI ARIDJA Godelive     | Statistiques globales et interface en ligne de commande | `stats.py`, `main_cli.py` |


# 4. Description détaillée des modules

# 4.1 Module 1 — Chargement & Prétraitement (`document_loader.py`)

- Lit tous les fichiers `.txt` d’un dossier donné.
- Nettoie les textes (minuscule, suppression ponctuation).
- Tokenise chaque document en une liste de mots.
- Stocke les documents dans un dictionnaire : `{nom_fichier: [liste_mots]}`.

# 4.2 Module 2 — Index Inversé (`indexer.py`)

- Construit un index inversé à partir des documents prétraités :  
  `mot -> [(doc_id, [positions])]`
- Calcule les fréquences des termes (TF) par mot et document.
- Permet d’accéder aux données courantes de l’index.

### 4.3 Module 3 — Recherche & Pertinence (`search_engine.py`)

- Recherche un ou plusieurs mots dans l’index.
- Permet des recherches en mode intersection (tous les mots) ou union (au moins un).
- Calcule un score de pertinence simple basé sur la fréquence des mots dans les documents.
- Renvoie la liste des documents triés par score.

### 4.4 Module 4 — Tri & Affichage (`retrieval.py`)

- Trie les documents résultats par score décroissant.
- Affiche les noms des fichiers, scores et extrait de texte autour des mots-clés.
- Gère les erreurs si les fichiers ne sont pas trouvés.

### 4.5 Module 5 — Statistiques & Interface CLI (`stats.py`, `main_cli.py`)

- Calcule et affiche des statistiques globales :  
  - Nombre total de documents indexés  
  - Nombre de mots uniques dans l’index  
  - Top 10 des mots les plus fréquents  
- Fournit une interface en ligne de commande interactive avec un menu.

## 5. Installation

### Prérequis

- Python 3.7 ou supérieur.
- Vs code

### Clonage du dépôt

```bash
git clone https://github.com/votre-utilisateur/TextIndexerPy.git
cd TextIndexerPy

# 6. Lancement du programme

```bash
python main_cli.py

Vous accédez à un menu avec les options suivantes :

1. Charger les documents
2. Créer l’index
3. Rechercher un document
4. Extraire un texte
5. Statistiques
6. Quitter

# 7. Exemple complet de session

=== TEXT INDEXER PROJECT ===
1. Charger les documents
2. Créer l’index
3. Rechercher un document
4. Extraire un texte
5. Statistiques
6. Quitter
Choisissez une option : 1
Chemin du dossier : D:\Bureau\TextIndexerPy\DATA
📄 Chargement du fichier : hello.txt
📄 Chargement du fichier : docs3.txt
📄 Chargement du fichier : exercice.txt
📁 Total : 3 fichiers chargés.

3 documents chargés.

Choisissez une option : 2
Voulez-vous indexer un fichier spécifique ? (o/n) : o
Liste des fichiers :
0: hello.txt
1: docs3.txt
2: exercice.txt
Entrez le numéro du fichier ou 'tous' pour tous : 0
📦 Construction de l'index pour hello.txt...
✅ Index créé avec 45 mots différents.

Choisissez une option : 3
Entrez un ou plusieurs mots-clés séparés par des espaces : bonjour monde
Mode de recherche ? (intersection / union) [par défaut: intersection] : intersection

📄 Résultats classés par pertinence :
 - hello.txt (score : 3)

Choisissez une option : 4
Entrez le nom exact du fichier à extraire : hello.txt

Extrait : ... Bonjour monde ! Ceci est un exemple ...

Choisissez une option : 5

📊 Statistiques globales :
➤ Nombre total de documents : 1
➤ Nombre total de mots uniques : 45
➤ Top 10 des mots les plus fréquents :
   - le : 6
   - bonjour : 3
   - monde : 3
   - est : 2
   - un : 2
   - test : 1
   - ...

Choisissez une option : 6
Merci d'avoir utilisé TextIndexerPy. À bientôt ! 👋

# Conclusion 

TextIndexerPy est un projet simple et structuré qui permet d’indexer et de rechercher efficacement des mots dans des fichiers texte. Il a permis de mettre en pratique des notions clés comme l’index inversé, le scoring de pertinence et la manipulation de fichiers en Python. Ce travail en groupe a aussi renforcé notre maîtrise du travail collaboratif.



