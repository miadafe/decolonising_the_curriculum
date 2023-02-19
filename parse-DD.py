from nltk.tokenize import sent_tokenize

with open("dewey.arff", "w", encoding="utf-8") as f:
  f.write(
    "@RELATION dewey\n\n"
    "@ATTRIBUTE text   string\n"
    "@ATTRIBUTE class  {CH,IS,EA,HD,BU,JU,OT}\n\n"
    "@DATA\n"
  )

religions = ["CH","IS","EA","HD","BU","JU","OT","GE"]

for system in ["DD", "LU", "UD"]:
  with open("RE-" + system + ".txt", "r", encoding="utf-8") as f:
    para = f.readlines()

  with open("dewey.arff", "a", encoding="utf-8") as f:
    for sentence in para:
      tokenized = sent_tokenize(sentence, language="english")
      for line in tokenized:
        # line = line.replace("\"", "\\\"")
        # line = line.replace("<p>", "\"")
        code = line.split(" ")
        if (int(code[0]) >= 200 and int(code[0]) <220):
            line = line.replace("</p>", "\", " + "GE" + "\n")
            f.write(line)
        elif (int(code[0]) >= 220 and int(code[0]) <290):
            line = line.replace("</p>", "\", " + "CH" + "\n")
            f.write(line)
        else:
            line = line.replace("</p>", "\", " + "OT" + "\n")
            f.write(line)
        if line[0] != "\"":
          line = "\" " + line


        # if "<doc" not in line and "</doc>" not in line and len(line) > 15:
        #   if line[0] != "\"":
        #     line = "\" " + line

          # if str("\", "+religions) not in line:
          #   line = line.strip() + "\", " + religions + "\n"
          #   f.write(line)
