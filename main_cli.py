from Module1_BAHATI.document_loader import charger_et_traiter as load_documents_from_folder
from Module2_ASSINA.indexer import create_index
from Module3_ATIBU.search_engine import SearchEngine
from Module4_BAMPOLE.retrieval import sort_results, retrieve_text
from Module5_ASSUMANI.stats import show_statistics

docs = None  # Variable globale pour stocker les documents
inverted_index = None
term_frequencies = None
doc_names = []

def main():
    global docs, inverted_index, term_frequencies, doc_names

    while True:
        print("\n=== TEXT INDEXER PROJECT ===")
        print("1. Charger les documents")
        print("2. Créer l’index")
        print("3. Rechercher un document")
        print("4. Extraire un texte")
        print("5. Statistiques")
        print("6. Quitter")
        choix = input("Choisissez une option : ")

        if choix == "1":
            folder = input("Chemin du dossier : ")
            docs = load_documents_from_folder(folder)
            print(f"{len(docs)} documents chargés.")

        elif choix == "2":
            if docs is None:
                print("❌ Veuillez d'abord charger les documents.")
            else:
                doc_keys = list(docs.keys())
                print("\n📑 Quel(s) document(s) voulez-vous indexer ?")
                for i, name in enumerate(doc_keys):
                    print(f"{i + 1}. {name}")
                print(f"{len(doc_keys) + 1}. TOUS les documents")

                try:
                    selection = int(input("Entrez votre choix : "))
                except ValueError:
                    print("❌ Entrée invalide.")
                    continue

                if 1 <= selection <= len(doc_keys):
                    # Indexer un seul document
                    selected_doc = {doc_keys[selection - 1]: docs[doc_keys[selection - 1]]}
                    print(f"📦 Indexation de : {list(selected_doc.keys())[0]}")
                    inverted_index, term_frequencies, doc_names = create_index(selected_doc)
                elif selection == len(doc_keys) + 1:
                    # Indexer tous les documents
                    print("📦 Indexation de TOUS les documents...")
                    inverted_index, term_frequencies, doc_names = create_index(docs)
                else:
                    print("❌ Choix invalide.")
                    continue

                if not inverted_index:
                    print("⚠️ Aucun mot trouvé. Tous les documents sont peut-être vides.")
                else:
                    print(f"✅ Index créé avec {len(inverted_index)} mots différents.")
                    print("\n🔍 Index inversé :")
                    for word, postings in inverted_index.items():
                        print(f"{word}: {postings}")
                    print("\n📊 Fréquences des termes :")
                    for word, freqs in term_frequencies.items():
                        print(f"{word}: {freqs}")

        elif choix == "3":
            if inverted_index is None or term_frequencies is None:
                print("❌ Vous devez d'abord créer l’index (option 2).")
                continue

            print("🔍 Recherche de mots-clés...")
            query = input("Entrez un ou plusieurs mots-clés séparés par des espaces : ").strip().lower()
            if not query:
                print("❌ Aucun mot-clé fourni.")
                continue

            mots = query.split()
            mode = input("Mode de recherche ? (intersection / union) [par défaut: intersection] : ").strip().lower()
            if mode not in ["intersection", "union"]:
                mode = "intersection"

            search_engine = SearchEngine(inverted_index, term_frequencies)
            resultats = search_engine.ranked_search(mots, mode)

            if not resultats:
                print("❌ Aucun document trouvé.")
            else:
                print("\n📄 Résultats classés par pertinence :")
                for doc_id, score in resultats:
                    print(f" - {doc_names[doc_id]} (score : {score})")

        elif choix == "4":
            if docs is None:
                print("❌ Veuillez d'abord charger les documents.")
            else:
                retrieve_text(docs)

        elif choix == "5":
            show_statistics(inverted_index, term_frequencies)

        elif choix == "6":
            print("Merci d'avoir utilisé TextIndexerPy. À bientôt ! 👋")
            break

        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
