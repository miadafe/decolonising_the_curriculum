import string
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
import nltk
from nltk.corpus import stopwords
stopwords = stopwords.words('english')

# so this actually compares each list element as a document.. so i need the whole document as one elem and a list with 3 elems for 3 documents

corpus = ['', '', '']

def addDeweyToCorp():
    with open("dewey.txt", "r", encoding="utf-8") as f:
         deweypara = f.read().splitlines()
    for i in range(len(deweypara)):
        corpus[0] = corpus[0] + deweypara[i] + " "

def addLeedsToCorp():
    with open("leeds.txt", "r", encoding="utf-8") as f:
         leedspara = f.read().splitlines()
    for i in range(len(leedspara)):
        corpus[1] = corpus[1] + leedspara[i] + " "

def addUniToCorp():
    with open("universal.txt", "r", encoding="utf-8") as f:
         unipara = f.read().splitlines()
    for i in range(len(unipara)):
        corpus[2] = corpus[2] + unipara[i] + " "

addDeweyToCorp()
addLeedsToCorp()
addUniToCorp()


vect = TfidfVectorizer(min_df=1, stop_words="english")
tfidf = vect.fit_transform(corpus)
co_sim = cosine_similarity(tfidf, tfidf)

def write_similarities():
    with open("similarities.txt", "w", encoding="utf-8") as f:
        for i in range (3):
            for j in range(3):
                f.write(str(co_sim[i, j]))
                f.write("\n")

write_similarities()
