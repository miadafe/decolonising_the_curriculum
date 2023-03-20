import string

def tabulate(para, double_tab):
    with open("crazy_lu.txt", "a", encoding="utf-8") as f:
        for s in para:
            code = s.split()
            if code[0] in double_tab:
                s = "        " + s + "\n"
                f.write(s)
            elif(len(code[0])>3):
                print("single heirarchy")
                s = "    " + s + "\n"
                f.write(s)
            else:
                f.write(s)
                f.write("\n")
        # print(para)
         # for sentence in para:
            # f.write(sentence)
    return para


# classifications which are an extra layer deeper
double_tab =["F-2.53", "F-2.55", "F-2.59", "F-2.71", "F-2.72", "F-2.74", "F-2.75", "F-2.79", "J-2.52"]

with open("crazy_lu.txt", "r", encoding="utf-8") as f:
    # open and split into lines, para array of sentences
    para = f.read().splitlines()
    # add tabs to lines
    para = tabulate(para, double_tab)
    # print(para)
