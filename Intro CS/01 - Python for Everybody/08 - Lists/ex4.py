fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error at openning file", fname)


uwords = []
for line in fhand:
    words = line.split()

    for word in words:
        word = word.strip()
        if word not in uwords: uwords.append(word)
        else: uwords.remove(word)

uwords.sort()
print(uwords)