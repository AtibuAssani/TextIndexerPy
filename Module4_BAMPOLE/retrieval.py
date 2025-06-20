# retrieval.py

import re
import os

def retrieve_text(docs):
    """
    Permet à l'utilisateur de saisir un nom de fichier pour en afficher le contenu.
    :param docs: Dictionnaire {nom_fichier: liste_de_mots}
    """
    print(" Extraction de texte...")
    nom_fichier = input("Entrez le nom exact du fichier (ex: hello.txt) : ")

    if nom_fichier in docs:
        print(f"\n📄 Contenu de {nom_fichier} :")
        print(" ".join(docs[nom_fichier]))
    else:
        print("❌ Fichier introuvable.")

def sort_results(results):
    """
    Trie les documents par score de pertinence décroissant.
    :param results: Liste de tuples (doc_id, score)
    :return: Liste triée
    """
    return sorted(results, key=lambda x: x[1], reverse=True)

def extract_snippet(text, query_words, window=30):
    """
    Extrait un extrait du texte autour du premier mot-clé trouvé.
    :param text: Texte complet du document
    :param query_words: Liste de mots-clés
    :param window: Nombre de caractères autour du mot-clé
    :return: Snippet textuel
    """
    text_lower = text.lower()
    for word in query_words:
        match = re.search(r'\b' + re.escape(word.lower()) + r'\b', text_lower)
        if match:
            start = max(0, match.start() - window)
            end = min(len(text), match.end() + window)
            return text[start:end].replace('\n', ' ') + "..."
    return text[:window * 2] + "..."  # Si aucun mot trouvé

def display_results(results, query_words, folder_path):
    """
    Affiche les documents avec leur score et un extrait contenant les mots-clés.
    :param results: Liste de tuples (doc_id, score)
    :param query_words: Liste de mots-clés
    :param folder_path: Dossier contenant les fichiers texte
    """
    print("\n🔍 Résultats de la recherche :")
    if not results:
        print("Aucun résultat trouvé.")
        return

    for doc_id, score in results:
        try:
            path = os.path.join(folder_path, doc_id)
            with open(path, 'r', encoding='utf-8') as f:
                content = f.read()
            snippet = extract_snippet(content, query_words)
            print(f"\n📄 Fichier : {doc_id}")
            print(f"   ➤ Score : {score}")
            print(f"   🧩 Extrait : ...{snippet}")
        except FileNotFoundError:
            print(f"\n⚠ Fichier introuvable : {doc_id}")
