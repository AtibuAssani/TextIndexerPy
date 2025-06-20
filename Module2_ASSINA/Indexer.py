"""
Module 2 - Construction de l'index inversé
Fichier : indexer.py
Responsable : ASSINA
"""

from collections import defaultdict

# Variables globales pour stocker l'index et fréquences courants
current_inverted_index = None
current_term_frequencies = None

def build_inverted_index(documents):
    """
    Construit un index inversé à partir d'une liste de documents.
    Chaque document est une liste de mots (tokens).

    Retourne un dictionnaire : 
    mot -> liste de tuples (id_document, [positions])
    """
    inverted_index = defaultdict(list)

    for doc_id, words in enumerate(documents):
        positions_map = defaultdict(list)
        for pos, word in enumerate(words):
            positions_map[word].append(pos)
        
        for word, positions in positions_map.items():
            inverted_index[word].append((doc_id, positions))

    return dict(inverted_index)


def compute_term_frequencies(inverted_index):
    """
    Calcule la fréquence des termes (TF) pour chaque mot dans chaque document.
    Retourne : mot -> dict(doc_id -> fréquence)
    """
    tf = {}
    for word, postings in inverted_index.items():
        tf[word] = {}
        for doc_id, positions in postings:
            tf[word][doc_id] = len(positions)
    return tf


def transpose_term_frequencies(tf):
    """
    Transpose la structure des fréquences :
    mot -> doc_id -> freq
    en
    doc_id -> mot -> freq
    """
    transposed = {}
    for mot, docs_freq in tf.items():
        for doc_id, freq in docs_freq.items():
            if doc_id not in transposed:
                transposed[doc_id] = {}
            transposed[doc_id][mot] = freq
    return transposed


def create_index(documents):
    global current_inverted_index, current_term_frequencies

    print("📦 Construction de l'index en cours...")
    current_inverted_index = build_inverted_index(list(documents.values()))
    current_term_frequencies = compute_term_frequencies(current_inverted_index)

    # Transpose la structure pour que ce soit doc_id -> mot -> tf
    current_term_frequencies = transpose_term_frequencies(current_term_frequencies)

    if not current_inverted_index:
        print("⚠️ Aucun mot trouvé. Tous les documents sont peut-être vides.")
    else:
        print("🔍 Index inversé :")
        for mot, postings in current_inverted_index.items():
            print(f"{mot}: {postings}")

        print("\n📊 Fréquences des termes :")
        for mot, freqs in compute_term_frequencies(current_inverted_index).items():
            print(f"{mot}: {freqs}")

        print(f"\n✅ Index créé avec {len(current_inverted_index)} mots différents.")

    doc_names = list(documents.keys())
    return current_inverted_index, current_term_frequencies, doc_names


def get_current_index_data():
    """
    Renvoie l'index et les fréquences stockées actuellement.
    """
    return current_inverted_index, current_term_frequencies


# Test local du module
if __name__ == "__main__":
    test_docs = {
        "doc1.txt": ["bonjour", "le", "monde", "bonjour"],
        "doc2.txt": ["test", "de", "monde"],
        "doc3.txt": ["bonjour", "test"]
    }

    index = build_inverted_index(list(test_docs.values()))
    print("\n🔍 Index inversé :")
    for mot, data in index.items():
        print(f"{mot}: {data}")

    tf = compute_term_frequencies(index)
    print("\n📊 Fréquences des termes :")
    for mot, freqs in tf.items():
        print(f"{mot}: {freqs}")
