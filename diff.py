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

comparisions = [0] *6
ratios = [0] * 6
comparisions[0] = SequenceMatcher(a=corpus[0], b=corpus[1]) #0.007680196613033294
comparisions[1] = SequenceMatcher(a=corpus[0], b=corpus[2]) #0.01720364041319458


comparisions[2] = SequenceMatcher(a=corpus[1], b=corpus[0]) #0.003763538283547762
comparisions[3] = SequenceMatcher(a=corpus[1], b=corpus[2]) #0.004237465326661184


comparisions[4] = SequenceMatcher(a=corpus[2], b=corpus[0]) #0.009095948397500504
comparisions[5] = SequenceMatcher(a=corpus[2], b=corpus[1]) #0.005669219915339649

def find_ratios():
    for i in range (6):
        ratios[i] = comparisions[i].ratio()

find_ratios()

# normalizing
# normalized = [0] * 6
# for i in range(6):
#     # normalized[i] = (ratios[i] - min(ratios))/(max(ratios)-min(ratios))
#     print(ratios[i])

# scaling
scaled = [0] * 6
for i in range(6):
    scaled[i] = ratios[i] * 10
    print(scaled[i])

def write_similarities():
    with open("diff_similarities.txt", "w", encoding="utf-8") as f:
        f.write("1")
        f.write("\n")
        f.write(str(scaled[0]))
        f.write("\n")
        f.write(str(scaled[1]))
        f.write("\n")
        f.write(str(scaled[2]))
        f.write("\n")
        f.write("1")
        f.write("\n")
        f.write(str(scaled[3]))
        f.write("\n")
        f.write(str(scaled[4]))
        f.write("\n")
        f.write(str(scaled[5]))
        f.write("\n")
        f.write("1")

write_similarities()
