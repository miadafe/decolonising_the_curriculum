import string

# leeds
def leedstext(para):
    with open("leeds.txt", "a", encoding="utf-8") as l:
        for sentence in para:
            s = sentence.split(' ', 1)[1]
            # print(s)
            l.write(s + "\n")

with open("RE-LU.txt", "r", encoding="utf-8") as f:
     para = f.read().splitlines()
     leedstext(para)

# dewey
def deweytext(para):
    with open("dewey.txt", "a", encoding="utf-8") as d:
        for sentence in para:
            s = sentence.split(' ', 1)[1]
            # print(s)
            d.write(s + "\n")

with open("RE-DD.txt", "r", encoding="utf-8") as f:
     para = f.read().splitlines()
     deweytext(para)

# universal
def universaltext(para):
    with open("universal.txt", "a", encoding="utf-8") as u:
        for sentence in para:
            s = sentence.split(' ', 1)[1]
            # print(s)
            u.write(s + "\n")

with open("RE-UD.txt", "r", encoding="utf-8") as f:
     para = f.read().splitlines()
     universaltext(para)
