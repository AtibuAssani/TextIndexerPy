# stats.py

from collections import Counter

class Stats:
    def __init__(self, inverted_index, term_frequencies):
        """
        :param inverted_index: dict, mot -> liste de (doc_id, [positions])
        :param term_frequencies: dict, doc_id -> {mot: fréquence}
        """
        self.inverted_index = inverted_index
        self.term_frequencies = term_frequencies

    def total_documents(self):
        """Retourne le nombre total de documents indexés."""
        return len(self.term_frequencies)

    def unique_words(self):
        """Retourne le nombre total de mots uniques dans l'index."""
        return len(self.inverted_index)

    def most_frequent_words(self, top_n=10):
        """Retourne les mots les plus fréquents globalement avec leur fréquence."""
        global_counter = Counter()
        for tf_doc in self.term_frequencies.values():
            global_counter.update(tf_doc)
        return global_counter.most_common(top_n)

    def display_stats(self):
        print("\n📊 Statistiques globales :")
        print(f"➤ Nombre total de documents : {self.total_documents()}")
        print(f"➤ Nombre total de mots uniques : {self.unique_words()}")
        print("➤ Top 10 des mots les plus fréquents :")
        for word, freq in self.most_frequent_words():
            print(f"   - {word} : {freq}")

def show_statistics(inverted_index, term_frequencies):
    if inverted_index is None or term_frequencies is None:
        print("❌ Vous devez d'abord créer l’index (option 2).")
        return
    stats = Stats(inverted_index, term_frequencies)
    stats.display_stats()

# Exemple d’exécution isolée
if __name__ == "__main__":
    from indexer import indexer

    idx = indexer()
    idx.index_corpus("DONNEES")  # Dossier contenant les fichiers .txt

    stats = Stats(idx.get_inverted_index(), idx.get_term_frequencies())
    stats.display_stats()
