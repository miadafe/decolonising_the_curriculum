from nltk.tokenize import sent_tokenize
import string

with open("dewey.arff", "w", encoding="utf-8") as f:
  f.write(
    "@RELATION dewey\n\n"
    "@ATTRIBUTE text   string\n"
    "@ATTRIBUTE class  {CH,IS,EA,HD,BU,JU,OT,GE}\n\n"
    "@DATA\n"
  )

religions = ["CH","IS","EA","HD","BU","JU","OT","GE"]
system = ["DD", "LU", "UD"]

#parsing functions
def deweyParse(para):
    with open("dewey.arff", "a", encoding="utf-8") as f:
        for sentence in para:
            #is removing punc still necessary?:
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            #add quote mark to beginning of sentence
            sentence = '" ' + sentence
            code = sentence.split()
            #code[1] represents the number part of the line
            if (int(code[1]) >= 200 and int(code[1]) <220):
                sentence += "\", GE\n"
                f.write(sentence)
            elif (int(code[1]) >= 220 and int(code[1]) <290):
                sentence += "\", CH\n"
                f.write(sentence)
            else:
                sentence += "\", OT\n"
                f.write(sentence)
    return 0

def leedsParse(para):
    return 0

def universalParse(para):
    return 0


with open("RE-" + system[0] + ".txt", "r", encoding="utf-8") as f:
    # para = f.readlines()
    para = f.read().splitlines()
    deweyParse(para)

with open("RE-" + system[1] + ".txt", "r", encoding="utf-8") as f:
    para = f.readlines()
    leedsParse(para)

with open("RE-" + system[2] + ".txt", "r", encoding="utf-8") as f:
    para = f.readlines()
    universalParse(para)
