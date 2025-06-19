# search_engine.py

class SearchEngine:
    def __init__(self, inverted_index, term_frequencies):
        self.inverted_index = inverted_index  # dict[str, list[tuple(doc_id, [positions])]]
        self.term_frequencies = term_frequencies  # dict[doc_id][word] = tf

    def search_single_word(self, word):
        """
        Recherche d’un mot dans l’index inversé
        :param word: str
        :return: set contenant les noms des documents
        """
        word = word.lower()
        if word in self.inverted_index:
            return set(doc_id for doc_id, _ in self.inverted_index[word])
        return set()

    def search_multiple_words(self, words, mode="intersection"):
        """
        Recherche de plusieurs mots (intersection ou union)
        :param words: list[str]
        :param mode: "intersection" ou "union"
        :return: set des documents correspondants
        """
        result_sets = [self.search_single_word(word) for word in words]

        if not result_sets:
            return set()

        if mode == "intersection":
            return set.intersection(*result_sets)
        elif mode == "union":
            return set.union(*result_sets)
        else:
            raise ValueError("Mode de recherche non supporté. Utilise 'intersection' ou 'union'.")

    def compute_relevance_scores(self, words, doc_ids):
        """
        Calcule le score de pertinence d’un document en sommant les TF des mots de la requête
        :param words: list[str]
        :param doc_ids: set[str]
        :return: dict[doc_id] = score
        """
        scores = {}
        for doc_id in doc_ids:
            score = 0
            for word in words:
                score += self.term_frequencies.get(doc_id, {}).get(word, 0)
            scores[doc_id] = score
        return scores

    def ranked_search(self, words, mode="intersection"):
        """
        Recherche avec score de pertinence et tri décroissant
        :param words: list[str]
        :param mode: "intersection" ou "union"
        :return: list de tuples (doc_id, score) triés
        """
        doc_ids = self.search_multiple_words(words, mode)
        scores = self.compute_relevance_scores(words, doc_ids)
        return sorted(scores.items(), key=lambda x: x[1], reverse=True)
    
    # Ajoute ça en bas de search_engine.py

def search_documents():
    print("🔍 Recherche de mots-clés...")
    
    # ⚠️ À adapter selon comment tu passes les index !
    from Module2_ASSINA.indexer import get_current_index_data
    
    inverted_index, term_frequencies = get_current_index_data()

    if inverted_index is None or term_frequencies is None:
        print("❌ Aucun index chargé.")
        return

    query = input("Entrez un ou plusieurs mots-clés séparés par des espaces : ").strip().lower().split()
    if not query:
        print("❌ Aucun mot-clé fourni.")
        return

    mode = input("Mode de recherche ? (intersection / union) [par défaut: intersection] : ").strip().lower()
    if mode not in ["intersection", "union"]:
        mode = "intersection"

    engine = SearchEngine(inverted_index, term_frequencies)
    results = engine.ranked_search(query, mode)

    if not results:
        print("❌ Aucun document trouvé.")
    else:
        print("📄 Résultats classés par pertinence :")
        for doc_id, score in results:
            print(f" - {doc_id} (score : {score})")

