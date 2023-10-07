import string


fname = input("Enter file name: ")
fhand = open(fname)


d = dict()
l = list()

for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        d[word] = d.get(word, 0) + 1



for k, v in d.items():
    l.append((v,k))


l.sort(reverse=True)    


for k, v in l[:10]:
    print((k, v))

