from nltk.tokenize import sent_tokenize
import string

with open("dewey.arff", "w", encoding="utf-8") as f:
  f.write(
    "@RELATION dewey\n\n"
    "@ATTRIBUTE text   string\n"
    "@ATTRIBUTE class  {CH,IS,EA,HD,BU,JU,OT,GE}\n\n"
    "@DATA\n"
  )

#should i be doing one big arff or seperate? seperate for now...
with open("universal.arff", "w", encoding="utf-8") as u:
    u.write(
    "@RELATION dewey\n\n"
    "@ATTRIBUTE text   string\n"
    "@ATTRIBUTE class  {CH,IS,EA,HD,BU,JU,OT,GE}\n\n"
    "@DATA\n"
  )

with open("leeds.arff", "w", encoding="utf-8") as l:
    l.write(
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
    with open("leeds.arff", "a", encoding="utf-8") as l:
        for sentence in para:
            #is removing punc still necessary?:
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            #add quote mark to beginning of sentence
            sentence = '" ' + sentence
            code = sentence.split()
            #code[1] represents the number part of the line
            if ((code[1][:1]) == 'A'):
                sentence += "\", GE\n"
                l.write(sentence)
            elif (code[1][:1] == 'J'):
                sentence += "\", OT\n"
                l.write(sentence)
            else:
                sentence += "\", CH\n"
                l.write(sentence)
    return 0

def universalParse(para):
    with open("universal.arff", "a", encoding="utf-8") as u:
        for sentence in para:
            #is removing punc still necessary?:
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            #add quote mark to beginning of sentence
            sentence = '" ' + sentence
            code = sentence.split()
            #code[1] represents the number part of the line
            # print(code[1][:2])
            if ((code[1][:2]) == '21' or int(code[1][:2]) == '25'):
                sentence += "\", GE\n"
                u.write(sentence)
            elif (code[1][:2] == '22'):
                sentence += "\", EA\n"
                u.write(sentence)
            elif (code[1][:2] == '23'):
                sentence += "\", HD\n"
                u.write(sentence)
            elif (code[1][:2] == '24'):
                sentence += "\", BU\n"
                u.write(sentence)
            elif (code[1][:2] == '26'):
                sentence += "\", JU\n"
                u.write(sentence)
            elif (code[1][:2] == '27'):
                sentence += "\", CH\n"
                u.write(sentence)
            elif (code[1][:2] == '28'):
                sentence += "\", IS\n"
                u.write(sentence)
            else:
                sentence += "\", OT\n"
                u.write(sentence)
    return 0


with open("RE-" + system[0] + ".txt", "r", encoding="utf-8") as f:
    para = f.read().splitlines()
    deweyParse(para)

with open("RE-" + system[1] + ".txt", "r", encoding="utf-8") as f:
    para = f.read().splitlines()
    leedsParse(para)

with open("RE-" + system[2] + ".txt", "r", encoding="utf-8") as f:
    para = f.read().splitlines()
    universalParse(para)
