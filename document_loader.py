import os
import re


def text(data):
    documents = {}
    # i prend le nom des différents fichiers
    for i in os.listdir(data):
        fullpath = os.path.join(data, i)
        if os.path.isfile(fullpath) and i.endswith('.txt'):
            print("Fichier trouvé :", i)
            try:
                with open(fullpath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    documents[i] = content
            except Exception as e:
                print(f"Erreur lors de la lecture du fichier {i}: {e}")
    return documents

def pretraitrement(text):
        text = text.lower()
        text = re.sub(r'[^\w\s]', '', text)
        return text
    
    
def token(text):
        tokens = text.split()
        return tokens
    
def  load_and_process(directory):
    raw_documents = text("data")
    processed_documents = {}
    for i, content in raw_documents.items():
        fichier_pretraite = pretraitrement(content)
        tokens = token(fichier_pretraite)
        processed_documents[i] = tokens
    return processed_documents

if __name__ == '__main__':
    
    directory_path = 'C:\\Users\\Claudine\\Desktop\\TextIndexerPy'
    documents_tokens = load_and_process(directory_path)
    for i, tokens in documents_tokens.items():
        print(f"Fichier: {i}")
        print(f"Nombre de mots: {len(tokens)}")
        print(f"Premiers tokens: {tokens[:10]}")
        print("-" * 40)
