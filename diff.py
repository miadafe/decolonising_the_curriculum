from difflib import SequenceMatcher

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

comp1 = SequenceMatcher(a=corpus[0], b=corpus[1]) #0.007680196613033294
comp2 = SequenceMatcher(a=corpus[1], b=corpus[2]) #0.003763538283547762
comp3 = SequenceMatcher(a=corpus[0], b=corpus[2]) #0.009095948397500504
print (comp1.ratio())
print (comp2.ratio())
print (comp3.ratio())
