from gensim import utils
import gensim.parsing.preprocessing as gsp
from unidecode import unidecode

import sys

filters = [
           gsp.strip_tags, 
#           gsp.strip_punctuation,
           gsp.strip_multiple_whitespaces,
           gsp.strip_numeric,
#           gsp.remove_stopwords, 
           gsp.strip_short, 
#           gsp.stem_text
]

def clean_text(s):
    s = s.lower()
    s = utils.to_unicode(s)
    
    for f in filters:
        s = f(s)
    return s

if __name__ == "__main__":
    print(sys.argv[1])
    with open(sys.argv[1], "r") as file:
        byte = file.read()


    cleaned  = clean_text(unidecode(byte))
    
    with open('./cleaned/'+sys.argv[1].split("/")[-1], "w") as f:
        f.write(cleaned)
        f.close()
        
        
