from collections import defaultdict
import re 
#fonction pour nettoyer et tokenizer un texte
def preprocess(text):
    text = text.lower()
    tokens = re.findall(r'\b\w+\b',text)#mots uniquement
    return tokens

#fonction pour parcourir les documents prétraités et construire l'index
def construire_index_inverse(docs):
    index_inverse = defaultdict(list)
    for doc_id, text in docs.items():
        tokens = preprocess(text)
        for position, mot in enumerate(tokens):
            index_inverse[mot].append((doc_id, position))
    return dict(index_inverse)

#calcul de la fréquence des termes(TF) pour chaque mot dans chaque document
def calculer_tf(docs):
    tf = defaultdict(lambda:defaultdict(int))
    for doc_id, text in docs.items():
        tokens = preprocess(text)
        for mot in tokens:
            tf[doc_id][mot] += 1
    return dict(tf)

#Auto-apprentissage
def main():
    index = construire_index_inverse(documents)
    tf = calculer_tf(documents)
    
    print("===Index Inversé===")
    for mot, occurrences in index.items():
        print(f"{mot}:{occurrences}")
        
    print("\n=== Fréquences des Termes (TF) ===")
    for doc_id, freqs in tf.items():
        print(f"{doc_id}:{dict(freqs)}")
        
if__name__ =="_main_":
    main()