import os
import re
from collections import defaultdict

class indexer:
    def __init__ (self):
        self.inverted_index = defaultdict(list)#mot -> liste dec(doc_id,[positions])
        self.term_frequencies = defaultdict(dict)#doc_id -> {mot:fréquence}
        
    def preprocess(self,text):
        #minuscule, suppression ponctuation, tokenisation simple 
        text = text.lower
        text = re.sub(r'[^\w\s]','',text)#supprimer la ponctuation
        return text.split()
    
    def index_document (self,doc_id,text):
        tokens = self.preprocess(text)
        position_map = default(list)
        tf_map = default(int)
        
        for pos, word in enumerate (tokens):
            position_map[word].append(pos)
            tf_map[word] += 1
        #mise à jour de l'index inversé
        for word, positions in position_map.items():
            self.inverted_index[word].append((doc_id,positions))
            
        #stockage de la fréquence des termes (TF)
        self.term_frequencies [doc_id] = dict(tf_map)
    
    def index_corpus(self,folder_path):
        for filename in os.listdir(folder_path):
            if filename.endswith(".txt"):
                doc_id = filename
                path = os.path.join(folder_path,filename)
                with open(path, 'r',encording ='utf-8') as f:
                    content = f.read()
                    self.index_document(doc_id, content)
                    
    def get_inverted_index(self):
        return dict(self.inverted_index)
    
    def get_term_frequencies(self):
        return dict(self.term_frequencies)
        
   
