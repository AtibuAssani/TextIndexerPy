#  Module 4 – Tri et Affichage des Résultats (retrieval.py)

Ce module fait partie du projet TextIndexerPy et est responsable du tri des résultats de recherche par score de pertinence, ainsi que de l’*affichage lisible des résultats* (nom du fichier, score, extrait).


##  Fonctionnalités

-Tri des résultats* : trie les documents trouvés selon un score décroissant.
-Extraction d'extraits (snippets)* : identifie un passage contenant un mot-clé dans le document.
-Affichage* : montre pour chaque fichier :
  - son nom,
  - son score,
  - un extrait où apparaît le mot-clé.

---

##  Fonctions principales

### sort_results(results: List[Tuple[str, int]]) -> List[Tuple[str, int]]
Trie les résultats selon le score de pertinence (ordre décroissant).

### extract_snippet(text: str, query_words: List[str], window: int = 30) -> str
Extrait un passage centré autour du premier mot-clé trouvé dans le texte.

### display_results(results: List[Tuple[str, int]], query_words: List[str], folder_path: str) -> None
Affiche chaque résultat avec :
- le nom du document,
- le score,
- un extrait contenant le mot-clé.

---

##  Entrées attendues

- results : Liste de tuples (doc_id, score) (ex. : résultats du module 3).
- query_words : Mots-clés utilisés dans la recherche.
- folder_path : Dossier contenant les fichiers .txt.

---

##  Exemple d’utilisation

```python
from retrieval import sort_results, display_results

results = [("doc1.txt", 3), ("doc2.txt", 1), ("doc3.txt", 2)]
query_words = ["chat"]
folder = "docs"

sorted_res = sort_results(results)
display_results(sorted_res, query_words, folder)