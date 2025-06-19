# Module 3 : Algorithmes de Recherche

## 📄 Description
Ce module permet d’effectuer des recherches sur l’index inversé :
- Recherche simple de mots-clés dans les documents.
- Recherche multiple avec union ou intersection.
- Calcul d’un score de pertinence pour classer les résultats.

## 🧠 Compétences mises en œuvre
- Recherche dans des dictionnaires
- Opérations d’union et d’intersection
- Notions de scoring (TF)

## 📂 Fichier principal
- `search_engine.py`

## ⚙️ Fonctions principales
- `search_one_word(word, index)` : Recherche un mot.
- `search_multiple_words(words, index, mode="union")` : Recherche multi-mots.
- `compute_relevance_score(results, tf_data, query_words)` : Calcule un score.
