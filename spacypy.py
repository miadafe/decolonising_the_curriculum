import spacy
# nlp = spacy.load('en_core_web_sm')
nlp = spacy.load("fi_core_news_md")

corpus = ['', '', '']
def addDeweyToCorp():
    # prev dewey.txt
    with open("new_ddc.txt", "r", encoding="utf-8") as f:
         deweypara = f.read().splitlines()
    for i in range(len(deweypara)):
        corpus[0] = corpus[0] + deweypara[i] + " "

def addLeedsToCorp():
    # prev leeds.txt
    with open("new_lu.txt", "r", encoding="utf-8") as f:
         leedspara = f.read().splitlines()
    for i in range(len(leedspara)):
        corpus[1] = corpus[1] + leedspara[i] + " "

def addUniToCorp():
    # prev universal.txt
    with open("new_udc.txt", "r", encoding="utf-8") as f:
         unipara = f.read().splitlines()
    for i in range(len(unipara)):
        corpus[2] = corpus[2] + unipara[i] + " "

addDeweyToCorp()
addLeedsToCorp()
addUniToCorp()
#
doc1 = nlp(corpus[0])
doc2 = nlp(corpus[1])
doc3 = nlp(corpus[2])

print (doc1.similarity(doc2)) # 0.5506873744445974
print (doc2.similarity(doc3)) # 0.3852627349438917
print (doc1.similarity(doc3)) # 0.5432947295843005
