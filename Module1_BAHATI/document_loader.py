import os
import re


def lire_documents(dossier):
    """
    Lit tous les fichiers .txt dans le dossier donné.
    Retourne un dictionnaire : {nom_fichier: contenu}
    """
    documents = {}
    for fichier in os.listdir(dossier):
        if fichier.endswith(".txt"):
            chemin_complet = os.path.join(dossier, fichier)
            print(f" Chargement du fichier : {fichier}")  #  LIGNE AJOUTÉE
            try:
                with open(chemin_complet, 'r', encoding='utf-8') as f:
                    documents[fichier] = f.read()
            except Exception as e:
                print(f" Erreur de lecture de {fichier} : {e}")
    print(f" Total : {len(documents)} fichiers chargés.\n")  #  FIN DE FONCTION
    return documents



def pretraitement(texte):
    """
    Met le texte en minuscules et enlève la ponctuation.
    """
    texte = texte.lower()
    texte = re.sub(r'[^\w\s]', '', texte)
    return texte


def tokenisation(texte):
    """
    Découpe le texte en mots (tokens) en utilisant les espaces.
    """
    tokens = texte.split()
    return tokens


def charger_et_traiter(dossier):
    """
    Charge et traite tous les fichiers texte dans le dossier donné.
    Retourne un dictionnaire : {nom_fichier: liste de tokens}
    """
    documents_bruts = lire_documents(dossier)
    documents_tokenises = {}
    for nom_fichier, contenu in documents_bruts.items():
        texte_nettoye = pretraitement(contenu)
        tokens = tokenisation(texte_nettoye)
        documents_tokenises[nom_fichier] = tokens
    return documents_tokenises


if __name__ == '__main__':
    # 🔧 Mets ici le chemin de ton dossier contenant les fichiers texte :
    dossier_documents = 'D:\Bureau\TextIndexerPy\DATA'

    documents = charger_et_traiter(dossier_documents)

    for nom, tokens in documents.items():
        print(f" Fichier : {nom}")
        print(f" Nombre de mots : {len(tokens)}")
        print(f" Premiers tokens : {tokens[:10]}")
        print("-" * 40)
