fname = input("Enter file name: ")

try:
    fhand = open(fname)
except:
    print("Error in openning file", fname)

count = dict()

for line in fhand:
    words = line.split()
    for word in words:
        count[word] = count.get(word, 0) + 1


print("the" in count)
print("of" in count)
print("no" in count)